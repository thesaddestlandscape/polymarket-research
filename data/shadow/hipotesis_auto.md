# Hipótesis automáticas — 2026-09-22 01:24 UTC
_Generado por shadow_postmortem.py sobre 550001 resoluciones (PNL=+61324.21€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.246 (n=490)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=453)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.246 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.130)

- **PATRÓN** `n_total_lado` > `76.0` → IC=+0.208 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 76.0 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.8046` → IC=+0.250 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8046 (IC base=+0.130)

- **PATRÓN** `banda_z` > `9.932` → IC=+0.226 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.932 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=556)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2915.0872` → IC=+0.135 (n=346)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2915.0872 (IC base=+0.130)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.251 (n=388)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=326)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.251 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.138)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.214 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.138)

- **PATRÓN** `banda_hit_calibrado` > `0.8036` → IC=+0.258 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8036 (IC base=+0.138)

- **PATRÓN** `banda_z` > `10.993` → IC=+0.221 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.993 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.158 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=470)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 96.0 (IC base=+0.042)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.515` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.256 (n=88)

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

- **PATRÓN** `libro_liquidez` > `2784.9288` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2784.9288 (IC base=+0.154)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `145.9` → IC=-0.233 (n=6635)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.9
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=19907)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `140.57` → IC=-0.237 (n=891)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.57
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2674)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `494.42` → IC=-0.152 (n=352)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 494.42
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1057)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `134.67` → IC=-0.277 (n=808)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 134.67
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2425)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `162.17` → IC=-0.229 (n=1567)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 162.17
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4703)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `122.87` → IC=-0.365 (n=1314)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.87
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=3947)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.233 (n=346)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=396)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.175 (n=226)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=462)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.149 (n=149)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=539)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.259 (n=164)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=169)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.218 (n=69)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=234)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.333 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=178)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.171 (n=74)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=147)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=171)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.201 (n=13252)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3317)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `9509.4092` → IC=+0.191 (n=1436)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 9509.4092 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.140 (n=10668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.139 (n=12771)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.129)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.234 (n=10201)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=5388)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `7640.0936` → IC=+0.171 (n=2026)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7640.0936 (IC base=+0.129)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=1449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.206 (n=1582)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1993)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `15752.6972` → IC=+0.233 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15752.6972 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.203 (n=1433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.204 (n=1575)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.263 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=2020)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `15469.3164` → IC=+0.206 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15469.3164 (IC base=+0.198)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.182 (n=306)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.62 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.144 (n=234)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4624.034 (IC base=+0.106)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.146 (n=329)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.148 (n=791)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.44 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=556)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `5871.1399` → IC=+0.161 (n=219)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 5871.1399 (IC base=+0.110)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=2660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=2266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.332 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.356 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.243 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.236)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.142 (n=560)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.230 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=513)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `1301.6177` → IC=+0.150 (n=621)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1301.6177 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.235 (n=587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.431 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=1039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.27` → IC=+0.313 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.27 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=706)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.168)

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
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.115)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.212 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.115)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=106)

- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=10718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=10226)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.224 (n=3656)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=2487)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.183 (n=1817)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.71 (IC base=+0.169)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.260 (n=694)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.258)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.360 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.258)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=2436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=2452)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.190 (n=1120)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.73 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=2293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.319 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.239)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=2494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.195 (n=2395)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.197 (n=1817)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.193)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.438 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.430 (n=440)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.470 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.427 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `2048.1399` → IC=+0.437 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.1399 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.433 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.433 (n=191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.452 (n=165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.470 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.436 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `3322.2122` → IC=+0.444 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3322.2122 (IC base=+0.435)

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
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

- **FILTRO** `libro_liquidez` < `6836.9618` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 6836.9618
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=31797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.241 (n=11796)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=6460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=5444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=5905)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=5690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.226 (n=5656)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.275 (n=2046)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=3065)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=5822)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=2869)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=2147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.264 (n=1997)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.211 (n=5265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.254 (n=2151)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.195 (n=5319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=5271)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.251 (n=2068)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.199 (n=4877)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.12` → IC=+0.130 (n=4441)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` < 4.12 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=4706)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.131 (n=6591)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 8.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.14` → IC=+0.144 (n=4441)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.14 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.201 (n=2462)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.122)

- **PATRÓN** `restante_min` < `4.07` → IC=+0.131 (n=2203)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` < 4.07 (IC base=+0.122)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.141 (n=2328)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.143 (n=2531)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.122)

- **PATRÓN** `lag_apertura_s` < `3.49` → IC=+0.145 (n=2204)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.49 (IC base=+0.122)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=2415)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.127 (n=2239)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=2383)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.34` → IC=+0.142 (n=2238)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.34 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=746)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.385 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1570.4643` → IC=+0.298 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1570.4643 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.299 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.340 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `5005.426` → IC=+0.310 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5005.426 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.335 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.302 (n=528)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.385 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1467.8527` → IC=+0.315 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1467.8527 (IC base=+0.297)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.445 (n=414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `1834.428` → IC=+0.440 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1834.428 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=224)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.446 (n=203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.444 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.446 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `2031.364` → IC=+0.460 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2031.364 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.370 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.381)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `5.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=41)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=38)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=41)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=38)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4714` → IC=+0.120 (n=7444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.60€ cuando `drift_60min` |x|≤ 0.4714 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.9821` → IC=+0.241 (n=2482)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9821 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.8353` → IC=+0.247 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8353 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.2176` → IC=+0.247 (n=1570)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2176 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.935` → IC=+0.179 (n=2871)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.935 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `1.2128` → IC=+0.243 (n=1993)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2128 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `1.0517` → IC=+0.252 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0517 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.306` → IC=+0.213 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.306 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.9116` → IC=+0.207 (n=3377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9116 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.131 (n=8987)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5714 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.5923` → IC=+0.190 (n=679)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.5923 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` < `0.1449` → IC=+0.174 (n=2759)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1449 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` < `0.6983` → IC=+0.175 (n=1354)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6983 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` > `0.8688` → IC=+0.174 (n=2052)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.8688 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.1677` → IC=+0.225 (n=1480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1677 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` > `1.5795` → IC=+0.202 (n=4586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5795 (IC base=+0.062)

- **PATRÓN** `ballena_activa_n` < `141.0` → IC=+0.211 (n=4916)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 141.0 (IC base=+0.062)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.178 (n=563)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0051 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.174 (n=562)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0082 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.3452` → IC=+0.166 (n=1688)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3452 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=824)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.176 (n=835)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 8.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.269 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.116` → IC=+0.276 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.116 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.211 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.167 (n=1572)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.253 (n=1108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.290 (n=413)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.248 (n=852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.062` → IC=+0.297 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.062 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.415` → IC=+0.252 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.415 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0914` → IC=+0.234 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0914 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.268 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6401` → IC=+0.253 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6401 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1774.82` → IC=+0.250 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.82 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.231 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.234 (n=566)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.252 (n=429)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=1352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.4827` → IC=+0.237 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4827 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.1922` → IC=+0.219 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1922 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.5823` → IC=+0.217 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5823 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.863` → IC=+0.249 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.863 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.2554` → IC=+0.219 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2554 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.222 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.232 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4011` → IC=+0.223 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4011 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.3728` → IC=+0.223 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3728 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `15865.6176` → IC=+0.224 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15865.6176 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.176 (n=445)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0026 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.156 (n=446)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.162 (n=448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6836` → IC=+0.167 (n=1333)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6836 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1262` → IC=+0.155 (n=1182)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1262 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.535` → IC=+0.157 (n=427)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.535 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.195` → IC=+0.137 (n=1207)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.195 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2085` → IC=+0.147 (n=1333)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2085 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.8526` → IC=+0.137 (n=888)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.8526 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.175 (n=358)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4376` → IC=+0.146 (n=1223)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4376 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.144 (n=815)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.144 (n=1139)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 411.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.214 (n=746)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=1645)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=625)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.101` → IC=+0.252 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.101 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.2116` → IC=+0.193 (n=1631)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.2116 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.3638` → IC=+0.194 (n=217)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3638 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.9002` → IC=+0.207 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9002 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.199 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.222 (n=1399)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.215 (n=1249)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.559` → IC=+0.215 (n=1397)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.559 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.253 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.0643` → IC=+0.243 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0643 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.679` → IC=+0.239 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.679 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.277 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.8944` → IC=+0.230 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8944 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `1857.0584` → IC=+0.231 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1857.0584 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.216 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.215)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=92)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2069)

- **PATRÓN** `ibs_20min` > `0.9414` → IC=+0.205 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9414 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.3625` → IC=+0.320 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3625 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.7852` → IC=+0.328 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7852 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.692` → IC=+0.152 (n=662)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.692 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.6634` → IC=+0.328 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6634 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.1956` → IC=+0.333 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1956 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.1771` → IC=+0.319 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1771 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.3004` → IC=+0.335 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3004 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.6117` → IC=+0.319 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6117 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.8429` → IC=+0.315 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8429 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.331 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.6717` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6717 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` < `0.852` → IC=+0.158 (n=501)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.852 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2244` → IC=+0.235 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2244 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` > `1.5114` → IC=+0.182 (n=624)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.5114 (IC base=+0.013)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.155 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=301)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.192 (n=89)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=268)

- **FILTRO** `ibs_20min` > `0.2619` → IC=-0.126 (n=2048)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2619
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=1010)

- **FILTRO** `sigma_ewma_delta_pct` > `8.667` → IC=-0.207 (n=329)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.667
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2729)

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

- **PATRÓN** `ibs_20min` < `0.2619` → IC=+0.123 (n=1010)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.2619 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.6684` → IC=+0.238 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6684 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` < `0.4202` → IC=+0.208 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4202 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` < `0.7129` → IC=+0.248 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7129 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.1582` → IC=+0.256 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1582 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` < `2.456` → IC=+0.259 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.456 (IC base=-0.044)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6434` → IC=-0.183 (n=516)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6434
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1555)

- **FILTRO** `ibs_20min` < `0.6977` → IC=-0.156 (n=1365)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6977
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=706)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.196 (n=396)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=1675)

- **FILTRO** `ibs_20min` > `0.775` → IC=-0.203 (n=772)

  - _Acción_: SKIP cuando `ibs_20min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2318)

- **PATRÓN** `dist_vwap_pct` > `0.7356` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7356 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2591` → IC=+0.316 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2591 (IC base=-0.073)

- **PATRÓN** `volumen_regimen` > `0.616` → IC=+0.299 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.616 (IC base=-0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.298 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.5359` → IC=+0.295 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5359 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.8242` → IC=+0.291 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8242 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` > `1.0601` → IC=+0.277 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0601 (IC base=-0.025)

- **PATRÓN** `volumen_regimen` < `0.7389` → IC=+0.250 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7389 (IC base=-0.025)

- **PATRÓN** `volumen_regimen` > `1.0811` → IC=+0.297 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0811 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1041` → IC=+0.283 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1041 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.2057` → IC=+0.253 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2057 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.4591` → IC=+0.250 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4591 (IC base=-0.025)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.247 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.025)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.196 (n=3099)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0096 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.4713` → IC=+0.187 (n=8304)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4713 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.7521` → IC=+0.286 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7521 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.655` → IC=+0.152 (n=4859)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 2.655 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.685` → IC=+0.244 (n=2932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.685 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2974` → IC=+0.262 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2974 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4707` → IC=+0.239 (n=1784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4707 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6923` → IC=+0.237 (n=1784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6923 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.267 (n=4864)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.145 (n=3124)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0089 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.5523` → IC=+0.149 (n=8245)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.5523 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2411` → IC=+0.237 (n=2523)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2411 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.236 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7144 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.2033` → IC=+0.244 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2033 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2466` → IC=+0.305 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2466 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.6154` → IC=+0.254 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6154 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.3372` → IC=+0.260 (n=1597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3372 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.261 (n=3392)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.070)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2606` → IC=-0.148 (n=637)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2606
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=1914)

- **FILTRO** `sigma_ewma_delta_pct` > `4.494` → IC=-0.168 (n=501)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.494
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1687)

- **PATRÓN** `ibs_20min` > `0.8947` → IC=+0.263 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8947 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.29` → IC=+0.164 (n=879)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.29 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2239` → IC=+0.270 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2239 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4401` → IC=+0.175 (n=275)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4401 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` > `2.1594` → IC=+0.188 (n=373)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.1594 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.173 (n=362)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 15.0 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8156` → IC=-0.149 (n=674)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8156
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=2024)

- **PATRÓN** `ibs_20min` > `0.8635` → IC=+0.159 (n=625)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.8635 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.3002` → IC=+0.167 (n=352)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.3002 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.0445` → IC=+0.146 (n=752)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0445 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6606` → IC=+0.160 (n=763)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6606 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.209 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.196 (n=278)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4208 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `249.0` → IC=+0.189 (n=364)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 249.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.216 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1526 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `0.6059` → IC=+0.209 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6059 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.4584` → IC=+0.218 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4584 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1745` → IC=+0.226 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1745 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `483.0` → IC=+0.208 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 483.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.290 (n=668)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.247)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=1482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.257 (n=550)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.247)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.247)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.672` → IC=+0.283 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.672 (IC base=+0.247)

- **PATRÓN** `volumen_pendiente_norm` < `0.1385` → IC=+0.260 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1385 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` > `3.4856` → IC=+0.263 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4856 (IC base=+0.247)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.259 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.247)

- **PATRÓN** `libro_liquidez` > `1924.86` → IC=+0.255 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1924.86 (IC base=+0.247)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.322 (n=527)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.327 (n=402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` < `0.2262` → IC=+0.289 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2262 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.816` → IC=+0.302 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.816 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.3432` → IC=+0.317 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3432 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` < `1.6136` → IC=+0.290 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6136 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.8021` → IC=+0.290 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8021 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.294 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `1910.06` → IC=+0.313 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.06 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.290 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.284)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2789` → IC=-0.192 (n=449)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2789
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=1349)

- **FILTRO** `ibs_20min` > `0.7796` → IC=-0.181 (n=553)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7796
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1662)

- **PATRÓN** `ibs_20min` > `0.9034` → IC=+0.175 (n=450)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.9034 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` > `0.462` → IC=+0.219 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.462 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.9855` → IC=+0.230 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9855 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `0.6488` → IC=+0.208 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6488 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.0768` → IC=+0.260 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0768 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `2.0972` → IC=+0.240 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0972 (IC base=+0.008)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.257 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.194 (n=194)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1525 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` < `0.6724` → IC=+0.182 (n=410)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.6724 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` < `1.1615` → IC=+0.193 (n=366)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.1615 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `0.7202` → IC=+0.181 (n=327)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.7202 (IC base=-0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.269 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.8285` → IC=+0.238 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8285 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.1439` → IC=+0.252 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1439 (IC base=-0.009)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.231 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7143` → IC=-0.203 (n=984)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=+0.274 (n=987)

- **FILTRO** `ibs_20min` > `0.6909` → IC=-0.233 (n=518)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6909
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=1555)

- **FILTRO** `sigma_ewma_delta_pct` > `4.677` → IC=-0.180 (n=458)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.677
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=1615)

- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.274 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7143 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.2978` → IC=+0.326 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2978 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.526` → IC=+0.157 (n=310)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.526 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8657` → IC=+0.297 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8657 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `0.6388` → IC=+0.287 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6388 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` < `0.1045` → IC=+0.289 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1045 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2259` → IC=+0.291 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2259 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.4442` → IC=+0.317 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4442 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.312 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.207 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1 (IC base=+0.013)

- **PATRÓN** `dist_vwap_pct` < `0.2123` → IC=+0.223 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2123 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` < `0.7014` → IC=+0.272 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7014 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.208 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.208 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.5036` → IC=+0.222 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5036 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.235 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.013)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0164` → IC=+0.318 (n=807)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0164 (IC base=+0.277)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.283 (n=1267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` > `0.6293` → IC=+0.311 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6293 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.2838` → IC=+0.322 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2838 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.487` → IC=+0.302 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.487 (IC base=+0.277)

- **PATRÓN** `volumen_regimen` > `0.8632` → IC=+0.302 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8632 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.317 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `2.5276` → IC=+0.289 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5276 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.282 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `2607.6531` → IC=+0.289 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2607.6531 (IC base=+0.277)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.324 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.015` → IC=+0.297 (n=885)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.015 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.276 (n=609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.273 (n=658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.3953` → IC=+0.304 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3953 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` > `0.288` → IC=+0.280 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.288 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` < `0.929` → IC=+0.270 (n=1492)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.929 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.991` → IC=+0.289 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.991 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `1.2419` → IC=+0.313 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2419 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.339 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `2.5151` → IC=+0.266 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5151 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.17` → IC=+0.275 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.17 (IC base=+0.270)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.270 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `2591.6802` → IC=+0.275 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2591.6802 (IC base=+0.270)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.170 (n=2455)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.205 (n=2445)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3536` → IC=+0.176 (n=6449)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3536 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=7665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.581` → IC=+0.218 (n=7329)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.581 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.1722` → IC=+0.196 (n=3238)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1722 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.237` → IC=+0.259 (n=1502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.237 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.2181` → IC=+0.161 (n=4848)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2181 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.6269` → IC=+0.161 (n=4848)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6269 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2462` → IC=+0.194 (n=1473)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2462 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5632` → IC=+0.171 (n=3084)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5632 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.6318` → IC=+0.176 (n=2337)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6318 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.182 (n=6238)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 117.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.183 (n=4625)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0065 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.205 (n=2312)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.205 (n=2347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.4773` → IC=+0.226 (n=6932)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4773 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.2271` → IC=+0.160 (n=5015)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2271 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.234` → IC=+0.196 (n=1176)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.234 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.176` → IC=+0.152 (n=5051)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.176 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.224 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.571` → IC=+0.165 (n=2755)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.571 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.2717` → IC=+0.173 (n=2839)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.2717 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `120.0` → IC=+0.172 (n=5898)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 120.0 (IC base=+0.168)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.218 (n=420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.188 (n=838)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0065 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.3418` → IC=+0.206 (n=1255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3418 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.199 (n=616)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.105` → IC=+0.311 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.105 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2299` → IC=+0.241 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2299 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.183 (n=1155)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.240 (n=780)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.255 (n=793)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1842` → IC=+0.294 (n=590)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1842 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.247 (n=801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=431)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.1095` → IC=+0.274 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1095 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.135` → IC=+0.254 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.135 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.241 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.254 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4156` → IC=+0.261 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4156 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.631` → IC=+0.235 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.631 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.242 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1781.7648` → IC=+0.253 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1781.7648 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.244 (n=365)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.0757` → IC=+0.204 (n=363)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0757 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=1147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.4138` → IC=+0.228 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4138 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.204` → IC=+0.214 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.204 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.523` → IC=+0.238 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.523 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.2679` → IC=+0.169 (n=1087)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2679 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.8798` → IC=+0.168 (n=724)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.8798 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.202 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.4139` → IC=+0.203 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4139 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `15815.2628` → IC=+0.173 (n=493)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 15815.2628 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.197 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0025 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.2906` → IC=+0.156 (n=1184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2906 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.5583` → IC=+0.182 (n=1185)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.5583 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1323` → IC=+0.161 (n=1173)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1323 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.856` → IC=+0.211 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.856 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.153 (n=1184)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.2116 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1573` → IC=+0.158 (n=363)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1573 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.143 (n=1074)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.154 (n=333)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 221.0 (IC base=+0.135)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.237 (n=557)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.2196` → IC=+0.218 (n=818)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2196 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.831` → IC=+0.284 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.831 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.21` → IC=+0.200 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.21 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.198 (n=534)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.648` → IC=+0.199 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.648 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.8991` → IC=+0.210 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8991 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.215 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `1927.2984` → IC=+0.206 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1927.2984 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.237 (n=997)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.255 (n=333)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.278 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.2479` → IC=+0.258 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2479 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.626` → IC=+0.274 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.626 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.359` → IC=+0.275 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.359 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.6139` → IC=+0.224 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6139 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.8783` → IC=+0.234 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8783 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1861.0222` → IC=+0.225 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1861.0222 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.228 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.222)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.208 (n=392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.4327` → IC=+0.161 (n=1171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4327 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.163 (n=1170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.3926` → IC=+0.197 (n=1170)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3926 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.157` → IC=+0.181 (n=794)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.157 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.946` → IC=+0.238 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.946 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.0478` → IC=+0.150 (n=1030)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0478 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6318` → IC=+0.150 (n=1170)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6318 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.210 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4163` → IC=+0.154 (n=382)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4163 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.529` → IC=+0.169 (n=382)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.529 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `6989.1384` → IC=+0.183 (n=780)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 6989.1384 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.147 (n=1106)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 166.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.157 (n=1222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0073 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3836` → IC=+0.143 (n=1221)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3836 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.181 (n=415)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 18.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6176` → IC=+0.169 (n=1221)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6176 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.3524` → IC=+0.138 (n=1299)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.3524 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.878` → IC=+0.177 (n=429)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 6.878 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8503` → IC=+0.145 (n=814)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8503 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2894` → IC=+0.208 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2894 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.7891` → IC=+0.129 (n=736)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7891 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.4834` → IC=+0.143 (n=368)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.4834 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `9966.3147` → IC=+0.162 (n=554)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 9966.3147 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.161 (n=602)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0101 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.5217` → IC=+0.201 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5217 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `0.8401` → IC=+0.215 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8401 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.609` → IC=+0.254 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.609 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `1.2251` → IC=+0.128 (n=1328)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.2251 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `0.6368` → IC=+0.120 (n=1326)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` > 0.6368 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.7979` → IC=+0.134 (n=853)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.7979 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=1384)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2895.2022` → IC=+0.194 (n=602)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2895.2022 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.137 (n=1009)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 50.0 (IC base=+0.116)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.150 (n=589)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0061 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.1031` → IC=+0.145 (n=446)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1031 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=1357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.208 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5667 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.9839` → IC=+0.137 (n=188)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.9839 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.1956` → IC=+0.138 (n=1209)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1956 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.473` → IC=+0.152 (n=277)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 7.473 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `1.1889` → IC=+0.122 (n=1336)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.1889 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.169 (n=164)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.4572` → IC=+0.132 (n=397)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4572 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `3069.3649` → IC=+0.159 (n=446)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3069.3649 (IC base=+0.112)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0186` → IC=+0.212 (n=844)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0186 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=1319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.7367` → IC=+0.259 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7367 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `1.2943` → IC=+0.235 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2943 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.452` → IC=+0.247 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.452 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2103` → IC=+0.204 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2103 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.8611` → IC=+0.220 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8611 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2345` → IC=+0.270 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2345 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.1643` → IC=+0.214 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1643 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.8078` → IC=+0.207 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8078 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.203 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2598.267` → IC=+0.203 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2598.267 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.234 (n=438)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0223` → IC=+0.217 (n=595)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0223 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.218 (n=438)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.222 (n=648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.215 (n=601)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.4412` → IC=+0.247 (n=1312)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4412 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `1.1437` → IC=+0.223 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1437 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.2681` → IC=+0.204 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2681 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.356` → IC=+0.243 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.356 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6302` → IC=+0.218 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6302 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.285 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.6033` → IC=+0.195 (n=1171)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.6033 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.4555` → IC=+0.199 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4555 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2566.217` → IC=+0.211 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2566.217 (IC base=+0.205)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.158 (n=571)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0039 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.173 (n=570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0089 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1356` → IC=+0.152 (n=753)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1356 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.3963` → IC=+0.180 (n=1710)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.3963 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.8737` → IC=+0.195 (n=283)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.8737 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.707` → IC=+0.175 (n=793)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.707 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8739` → IC=+0.164 (n=991)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8739 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `0.7005` → IC=+0.149 (n=1328)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7005 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1633` → IC=+0.178 (n=473)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1633 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4373` → IC=+0.164 (n=548)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4373 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5508` → IC=+0.166 (n=548)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5508 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.149 (n=1926)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `2496.5092` → IC=+0.147 (n=1527)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2496.5092 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.164 (n=1489)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 166.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.141 (n=597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0038 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.0548` → IC=+0.192 (n=596)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0548 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3431` → IC=+0.122 (n=427)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.3431 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.144 (n=386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 9.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `0.2517` → IC=+0.140 (n=426)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.2517 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.2955` → IC=+0.149 (n=152)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.2955 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `0.9061` → IC=+0.127 (n=285)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.9061 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `12288.3929` → IC=+0.127 (n=381)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 12288.3929 (IC base=+0.102)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.207 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3387` → IC=+0.142 (n=565)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3387 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.141 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 7.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.127 (n=579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6012` → IC=+0.173 (n=497)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.6012 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.2919` → IC=+0.149 (n=597)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2919 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.41` → IC=+0.152 (n=219)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.41 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `0.7202` → IC=+0.142 (n=504)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.7202 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.203 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.1106` → IC=+0.147 (n=488)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.1106 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.4187` → IC=+0.134 (n=555)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4187 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `333.0` → IC=+0.138 (n=468)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 333.0 (IC base=+0.126)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.269 (n=223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.213 (n=169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.219 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.7028` → IC=+0.262 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7028 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.15` → IC=+0.231 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.15 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.996` → IC=+0.243 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.996 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `0.8422` → IC=+0.218 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8422 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `1.156` → IC=+0.213 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.156 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2555` → IC=+0.329 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2555 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.3759` → IC=+0.246 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3759 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.3941` → IC=+0.252 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3941 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.0789` → IC=+0.165 (n=156)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.0789 (IC base=+0.070)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4189` → IC=-0.127 (n=164)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4189
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=320)

- **FILTRO** `dist_vwap_pct` > `0.3414` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3414
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=450)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.165 (n=171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0088 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.154 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 8.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.7317` → IC=+0.190 (n=337)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.7317 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.6295` → IC=+0.210 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6295 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.234` → IC=+0.200 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.234 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.0699` → IC=+0.135 (n=332)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.0699 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.7268` → IC=+0.140 (n=337)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.7268 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.288` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.288 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.2097` → IC=+0.161 (n=163)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.2097 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=411)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `3064.7088` → IC=+0.203 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3064.7088 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.4189` → IC=+0.158 (n=320)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4189 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` < `1.604` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.604 (IC base=+0.062)

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
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.206 (n=3106)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=9738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.4725` → IC=+0.217 (n=9303)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4725 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.9628` → IC=+0.208 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9628 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.609` → IC=+0.228 (n=4531)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.609 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8827` → IC=+0.166 (n=4150)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8827 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2401` → IC=+0.199 (n=1746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2401 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.6156` → IC=+0.188 (n=2973)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6156 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2334.7045` → IC=+0.170 (n=6202)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2334.7045 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.195 (n=7000)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 89.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.188 (n=7404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0091 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.183 (n=8413)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=3239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.238 (n=8415)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2421` → IC=+0.162 (n=5185)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2421 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.923` → IC=+0.200 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.923 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.71` → IC=+0.182 (n=8162)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.71 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.159 (n=2561)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7044 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `1.2044` → IC=+0.152 (n=1941)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.2044 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2883` → IC=+0.245 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2883 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.868` → IC=+0.188 (n=5113)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.868 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.190 (n=4901)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 49.0 (IC base=+0.181)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.207 (n=530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.219 (n=531)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3502` → IC=+0.190 (n=1583)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3502 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.201 (n=1062)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.321 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.978` → IC=+0.314 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.978 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2734` → IC=+0.252 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2734 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.5711` → IC=+0.209 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5711 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.267 (n=1082)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.1272` → IC=+0.290 (n=532)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1272 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1098)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=1097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.292 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.458` → IC=+0.268 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.458 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.297 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `1.8682` → IC=+0.279 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8682 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.262 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1774.62` → IC=+0.275 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.62 (IC base=+0.260)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.194 (n=502)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0842` → IC=+0.165 (n=497)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0842 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3137` → IC=+0.202 (n=1491)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3137 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1264` → IC=+0.185 (n=864)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1264 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.756` → IC=+0.169 (n=342)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.756 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.234` → IC=+0.153 (n=1336)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.234 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6267` → IC=+0.176 (n=498)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6267 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2695` → IC=+0.201 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2695 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1166` → IC=+0.160 (n=1264)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1166 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7608` → IC=+0.155 (n=957)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7608 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `13725.8693` → IC=+0.152 (n=994)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 13725.8693 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `480.0` → IC=+0.157 (n=1367)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 480.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.162 (n=1286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3224` → IC=+0.161 (n=1285)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3224 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.171 (n=436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6459` → IC=+0.191 (n=1285)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6459 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1297` → IC=+0.166 (n=1155)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1297 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.174` → IC=+0.159 (n=622)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.174 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.161 (n=1285)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1913 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1509` → IC=+0.197 (n=348)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1509 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4232` → IC=+0.159 (n=1187)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4232 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7532` → IC=+0.158 (n=791)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7532 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `428.0` → IC=+0.153 (n=959)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 428.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.245 (n=680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=1573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=1519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.6739` → IC=+0.259 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6739 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.775` → IC=+0.295 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.775 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` < `0.2136` → IC=+0.226 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2136 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.8814` → IC=+0.240 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8814 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.233 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1927.5618` → IC=+0.225 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1927.5618 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.241 (n=1387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.239 (n=924)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.242 (n=610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.283 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.741` → IC=+0.281 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.741 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.294 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.7706` → IC=+0.236 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7706 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.2115` → IC=+0.237 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2115 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.247 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1913.1775` → IC=+0.252 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1913.1775 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.254 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.235)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.183 (n=534)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0035 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4371` → IC=+0.143 (n=1588)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4371 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=1667)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.8784` → IC=+0.262 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8784 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3692` → IC=+0.168 (n=648)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.3692 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.195` → IC=+0.162 (n=661)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.195 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8779` → IC=+0.159 (n=1059)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8779 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.228 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5155` → IC=+0.151 (n=675)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5155 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.1357` → IC=+0.153 (n=696)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1357 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8151.5866` → IC=+0.229 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8151.5866 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.150 (n=498)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 81.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.155 (n=1291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0076 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4454` → IC=+0.154 (n=1291)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4454 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=586)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6931` → IC=+0.184 (n=1291)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6931 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.5941` → IC=+0.141 (n=1409)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.5941 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.137` → IC=+0.184 (n=191)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 11.137 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8608` → IC=+0.143 (n=862)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8608 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.1808` → IC=+0.146 (n=430)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1808 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.261 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4415` → IC=+0.152 (n=1219)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4415 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `11034.1392` → IC=+0.208 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11034.1392 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `182.0` → IC=+0.143 (n=1215)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 182.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.136 (n=1049)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0081 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.188 (n=1574)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4722 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `1.081` → IC=+0.199 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.081 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.428` → IC=+0.235 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.428 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `0.8919` → IC=+0.136 (n=1050)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8919 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=1581)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.02 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2912.6118` → IC=+0.246 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2912.6118 (IC base=+0.108)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.128 (n=1374)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 62.0 (IC base=+0.108)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.176 (n=517)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0057 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.1294` → IC=+0.158 (n=515)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1294 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=1598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.205 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.131 (n=1233)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.446` → IC=+0.127 (n=1492)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.446 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.717` → IC=+0.158 (n=679)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.717 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.2252` → IC=+0.174 (n=237)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2252 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.4555` → IC=+0.140 (n=462)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4555 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `2.1911` → IC=+0.127 (n=628)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.1911 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2852.4784` → IC=+0.167 (n=514)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2852.4784 (IC base=+0.112)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0191` → IC=+0.218 (n=1049)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0191 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=1644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.207 (n=1402)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.5143` → IC=+0.247 (n=1574)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5143 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.88` → IC=+0.243 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.88 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.504` → IC=+0.252 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.504 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.6367` → IC=+0.215 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6367 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2346` → IC=+0.244 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2346 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.5218` → IC=+0.238 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5218 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.215 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2603.3702` → IC=+0.215 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2603.3702 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.225 (n=569)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.221 (n=568)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5207` → IC=+0.255 (n=1702)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5207 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.8728` → IC=+0.203 (n=1886)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8728 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.731` → IC=+0.260 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.731 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.232` → IC=+0.240 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.232 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.259 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2192` → IC=+0.193 (n=1338)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2192 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4403` → IC=+0.200 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4403 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=2843)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.158 (n=2416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0093 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.526` → IC=+0.159 (n=2743)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.526 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.157 (n=921)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.170 (n=954)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 4.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.9407` → IC=+0.209 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9407 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1905` → IC=+0.159 (n=986)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1905 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `1.1512` → IC=+0.140 (n=1936)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 1.1512 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.14` → IC=+0.182 (n=448)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 10.14 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.9028` → IC=+0.161 (n=1155)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.9028 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1729` → IC=+0.185 (n=750)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1729 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4583` → IC=+0.155 (n=905)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4583 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.8927` → IC=+0.162 (n=1807)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8927 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=1831)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3653.4314` → IC=+0.152 (n=1829)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3653.4314 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.194 (n=716)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4837` → IC=+0.153 (n=2144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4837 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.161 (n=726)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 4.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.1824` → IC=+0.163 (n=944)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1824 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.9325` → IC=+0.150 (n=335)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.9325 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.2453` → IC=+0.126 (n=1902)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.2453 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.214` → IC=+0.141 (n=2132)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.214 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.9017` → IC=+0.149 (n=1363)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.9017 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0721` → IC=+0.145 (n=1004)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0721 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.4296` → IC=+0.139 (n=708)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4296 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.8153` → IC=+0.140 (n=1413)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.8153 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=2843)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `7124.482` → IC=+0.149 (n=1915)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 7124.482 (IC base=+0.133)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.167 (n=316)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0056 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.164 (n=322)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0033 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.0902` → IC=+0.180 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0902 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.5204` → IC=+0.190 (n=240)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5204 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.2159` → IC=+0.175 (n=167)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.2159 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.4017` → IC=+0.161 (n=352)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4017 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.366` → IC=+0.167 (n=388)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 2.366 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.2737` → IC=+0.154 (n=359)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.2737 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.849` → IC=+0.189 (n=239)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.849 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.3073` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3073 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.189 (n=120)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.6869` → IC=+0.205 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6869 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `12537.6672` → IC=+0.194 (n=321)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 12537.6672 (IC base=+0.154)

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

- **PATRÓN** `drift_60min` |x|≤ `0.4173` → IC=+0.173 (n=548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.4173 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `2.8576` → IC=+0.167 (n=547)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.8576 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.312 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.254)

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

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.160 (n=368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.005 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.159 (n=836)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0044 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.1262` → IC=+0.156 (n=280)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1262 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.171 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 4.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.5456` → IC=+0.157 (n=558)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5456 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.8883` → IC=+0.173 (n=279)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.8883 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `1.006` → IC=+0.162 (n=196)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 1.006 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.4256` → IC=+0.163 (n=773)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.4256 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.678` → IC=+0.160 (n=837)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.678 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.0946` → IC=+0.159 (n=736)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0946 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `0.7181` → IC=+0.157 (n=747)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7181 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1724` → IC=+0.169 (n=246)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1724 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.5174` → IC=+0.159 (n=820)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.5174 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.5168` → IC=+0.154 (n=733)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5168 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=815)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.152 (n=697)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0084 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3917` → IC=+0.168 (n=612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3917 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.150 (n=244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 4.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.7335` → IC=+0.138 (n=697)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.7335 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.0998` → IC=+0.150 (n=696)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.0998 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.6358` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.6358 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.3872` → IC=+0.140 (n=697)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.3872 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.906` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.906 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.261` → IC=+0.138 (n=628)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.261 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.0948` → IC=+0.150 (n=612)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0948 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.7218` → IC=+0.141 (n=622)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.7218 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0726` → IC=+0.175 (n=300)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0726 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1843` → IC=+0.152 (n=601)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1843 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7743` → IC=+0.157 (n=455)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7743 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7614.1842` → IC=+0.163 (n=696)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 7614.1842 (IC base=+0.138)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 1.0 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.026` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.026 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.067)

- **PATRÓN** `libro_liquidez` > `3398.8602` → IC=+0.123 (n=165)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 3398.8602 (IC base=+0.067)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.202 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.077)

- **PATRÓN** `drift_60min` |x|≤ `0.3939` → IC=+0.131 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.3939 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.125` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.125 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.6658` → IC=+0.160 (n=92)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.6658 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` < `0.0885` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.0885 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 57.0 (IC base=+0.077)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.006` → IC=-0.195 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=291)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.235 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=344)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.213 (n=364)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=854)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.5632` → IC=+0.190 (n=730)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.5632 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.3636` → IC=+0.164 (n=293)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3636 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.45` → IC=+0.209 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.45 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.211 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `2.0983` → IC=+0.151 (n=546)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.0983 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=593)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2438.1282` → IC=+0.152 (n=320)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2438.1282 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.0482` → IC=+0.254 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0482 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.0685` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0685 (IC base=-0.016)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.272 (n=125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.125 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5284` → IC=+0.197 (n=252)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5284 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.179 (n=135)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.0596` → IC=+0.130 (n=222)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0596 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` < `0.067` → IC=+0.145 (n=187)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.067 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2692` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2692 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `2.0118` → IC=+0.198 (n=187)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.0118 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=257)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `3986.8232` → IC=+0.127 (n=108)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3986.8232 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.4946` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.4946 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.5944` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.5944 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.0668` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0668 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `2.4111` → IC=+0.148 (n=86)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4111 (IC base=+0.034)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.271 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=102)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.243 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=102)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.179 (n=188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.005 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.143 (n=253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 8.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` > `0.6967` → IC=+0.234 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6967 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` > `0.3424` → IC=+0.164 (n=105)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3424 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` < `0.7657` → IC=+0.130 (n=279)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.7657 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.825` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.825 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.8144` → IC=+0.135 (n=168)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8144 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` > `0.5884` → IC=+0.129 (n=251)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.5884 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.2987` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2987 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.7369` → IC=+0.154 (n=134)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.7369 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` > `1.503` → IC=+0.130 (n=179)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.503 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=166)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1118.6691` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 1118.6691 (IC base=+0.110)

- **PATRÓN** `drift_60min` |x|≤ `0.1124` → IC=+0.174 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1124 (IC base=-0.040)

- **PATRÓN** `ibs_20min` < `0.1419` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1419 (IC base=-0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.924` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 2.924 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=-0.040)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=72)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=-0.040)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.0882` → IC=-0.278 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0882
  - _Potencial_: sin este filtro IC_bueno=+0.287 (n=45)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.129 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.006 (IC base=+0.078)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.140 (n=173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.078)

- **PATRÓN** `ibs_20min` > `0.6863` → IC=+0.180 (n=204)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6863 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` > `1.0159` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 1.0159 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.244` → IC=+0.208 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.244 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `1.0643` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0643 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.0847` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0847 (IC base=+0.078)

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
- **FILTRO** `hora_utc` > `10.0` → IC=-0.409 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=142)

- **FILTRO** `dist_vwap_pct` > `0.2334` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2334
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=168)

- **FILTRO** `volumen_regimen` < `0.7363` → IC=-0.355 (n=60)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7363
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=124)

- **FILTRO** `dist_vwap_pct` > `0.3412` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3412
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=128)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=127)

- **FILTRO** `volumen_pendiente_norm` > `0.074` → IC=-0.400 (n=18)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.074
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=55)

- **FILTRO** `volumen_spike_ratio` > `2.0323` → IC=-0.400 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.0323
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=55)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=50)

- **FILTRO** `volumen_regimen` < `0.7761` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7761
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=49)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.283 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=44)

- **FILTRO** `drift_60min` |x|> `0.1778` → IC=-0.324 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1778
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=48)

- **FILTRO** `volumen_regimen` > `0.807` → IC=-0.333 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.807
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=43)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8396` → IC=-0.429 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8396
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=22)

- **FILTRO** `volumen_regimen` > `0.5719` → IC=-0.357 (n=33)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.5719
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.1179` → IC=-0.397 (n=27)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1179
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=29)

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
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.160 (n=236)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.6522 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.4724` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.4724 (IC base=+0.081)

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
- **FILTRO** `volumen_pendiente_norm` < `0.0772` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0772
  - _Potencial_: sin este filtro IC_bueno=+0.262 (n=19)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.214 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.186 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0081 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.173 (n=102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 18.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.7619` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.7619 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.03 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `864.5816` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 864.5816 (IC base=+0.172)

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
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 16.0 (IC base=+0.105)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=630)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2868.9974` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2868.9974 (IC base=+0.105)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.134 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 16.0 (IC base=+0.105)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=630)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2868.9974` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2868.9974 (IC base=+0.105)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=76)

- **FILTRO** `py_entrada` < `0.435` → IC=-0.176 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=110)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=129)

- **FILTRO** `libro_liquidez` < `2453.3967` → IC=-0.263 (n=36)

  - _Acción_: SKIP cuando `libro_liquidez` < 2453.3967
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=109)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=201)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=187)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1592)

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
- **FILTRO** `liq_usd_total` < `41013.19` → IC=-0.130 (n=52)

  - _Acción_: SKIP cuando `liq_usd_total` < 41013.19
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=108)

- **FILTRO** `libro_liquidez` < `15405.8709` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 15405.8709
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `ballena_activa_n` > `569.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 569.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **PATRÓN** `liq_n` > `18.0` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.037)

- **PATRÓN** `liq_usd_total` > `76612.5` → IC=+0.183 (n=80)

  - _Acción_: Kelly boost +0.91€ cuando `liq_usd_total` > 76612.5 (IC base=+0.037)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9773` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9773
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=90)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=714)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=425)

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
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=121)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.897` → IC=-0.138 (n=45)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.897
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=92)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=474)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=316)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=316)

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

- **FILTRO** `hora_utc` > `10.0` → IC=-0.123 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=37)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=89)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=187)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=72)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=75)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=230)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=230)

- **FILTRO** `libro_liquidez` < `730.7333` → IC=-0.121 (n=130)

  - _Acción_: SKIP cuando `libro_liquidez` < 730.7333
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=130)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=115)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7287)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.175 (n=3118)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=9883)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.174 (n=3269)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=10169)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.212 (n=554)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=1687)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.172 (n=556)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=1846)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.203 (n=557)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=1727)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.206 (n=593)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=1800)

- **FILTRO** `ibs_20min` > `0.2846` → IC=-0.165 (n=598)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2846
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1795)

- **PATRÓN** `libro_liquidez` > `1728.8336` → IC=+0.121 (n=777)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1728.8336 (IC base=+0.031)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.182 (n=545)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=1676)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.181 (n=597)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=1796)

- **PATRÓN** `libro_liquidez` > `2534.9978` → IC=+0.121 (n=756)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2534.9978 (IC base=+0.019)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2652)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=2806)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=2812)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.170 (n=95)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=354)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.125 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=339)

- **FILTRO** `libro_liquidez` < `16874.9653` → IC=-0.142 (n=213)

  - _Acción_: SKIP cuando `libro_liquidez` < 16874.9653
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=640)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=226)

- **FILTRO** `ibs_20min` < `0.1006` → IC=-0.247 (n=73)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1006
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=221)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.200 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=207)

- **FILTRO** `hora_utc` > `18.0` → IC=-0.151 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=211)

- **FILTRO** `drift_20min_pct` |x|> `0.1785` → IC=-0.171 (n=68)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1785
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=207)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=735)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=9201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=20796)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.275 (n=7245)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=22752)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.236 (n=7494)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=22503)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=10161)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=19836)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.229 (n=9314)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=28138)

- **FILTRO** `ibs_7min` > `0.2941` → IC=-0.180 (n=9343)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=28109)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.307 (n=1174)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3752)

- **FILTRO** `ibs_7min` < `0.7105` → IC=-0.252 (n=1624)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7105
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3302)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.182 (n=1156)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3770)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.258 (n=1608)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4846)

- **FILTRO** `drift_7min_pct` |x|> `0.1122` → IC=-0.125 (n=2194)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1122
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4260)

- **FILTRO** `ibs_7min` > `0.7929` → IC=-0.206 (n=1613)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7929
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4841)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=1211)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=3996)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.249 (n=1250)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3957)

- **FILTRO** `ibs_7min` < `0.7512` → IC=-0.191 (n=1301)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7512
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3906)

- **FILTRO** `ballena_activa_n` > `160.0` → IC=-0.172 (n=1299)

  - _Acción_: SKIP cuando `ballena_activa_n` > 160.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=3908)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.259 (n=1295)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=3941)

- **FILTRO** `ibs_7min` > `0.2588` → IC=-0.176 (n=1308)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2588
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3928)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.187 (n=1307)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3929)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.173 (n=1138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=3523)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.309 (n=1132)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=3529)

- **FILTRO** `ibs_7min` < `0.1972` → IC=-0.258 (n=1165)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1972
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3496)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.213 (n=1110)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3551)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.238 (n=1602)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=5271)

- **FILTRO** `ibs_7min` > `0.7565` → IC=-0.180 (n=1718)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7565
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=5155)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=1574)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=3361)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.243 (n=1211)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3724)

- **FILTRO** `ibs_7min` < `0.7433` → IC=-0.182 (n=1233)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7433
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3702)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.174 (n=1212)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=3723)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.266 (n=1116)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=3920)

- **FILTRO** `ibs_7min` > `0.2747` → IC=-0.175 (n=1258)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2747
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3778)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.190 (n=1231)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3805)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.262 (n=1242)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=4029)

- **FILTRO** `ibs_7min` < `0.7027` → IC=-0.231 (n=1317)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7027
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3954)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.178 (n=1708)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=5401)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.276 (n=1172)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3825)

- **FILTRO** `ibs_7min` < `0.7087` → IC=-0.233 (n=1249)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7087
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3748)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1197)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3800)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.203 (n=1650)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=5094)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1040)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=518)

- **FILTRO** `libro_liquidez` < `10575.5071` → IC=-0.143 (n=141)

  - _Acción_: SKIP cuando `libro_liquidez` < 10575.5071
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=423)

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
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=323)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.138 (n=139)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=286)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=543)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.147 (n=474)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.115)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.153 (n=237)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 459.6089 (IC base=+0.115)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `312.745` → IC=+0.143 (n=110)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 312.745 (IC base=+0.138)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.121 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 10.0 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 13.0 (IC base=+0.096)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.413` → IC=+0.173 (n=96)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.413 (IC base=+0.091)

- **PATRÓN** `total_vol_5m` < `394.3776` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 394.3776 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 69.0 (IC base=+0.091)

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
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.153 (n=125)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.106)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.141 (n=126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 13.0 (IC base=+0.106)

- **PATRÓN** `total_vol_5m` < `258575.4` → IC=+0.156 (n=94)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 258575.4 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `3729.2002` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3729.2002 (IC base=+0.106)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0073` → IC=-0.339 (n=116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=227)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.392 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=70)

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

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.310 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=200)

- **FILTRO** `T_h` > `63.9947` → IC=-0.317 (n=222)

  - _Acción_: SKIP cuando `T_h` > 63.9947
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=76)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.004` → IC=-0.227 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=94)

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

- **PATRÓN** `edge` > `0.1023` → IC=+0.457 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.422)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.462 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.422)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.452 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.422)

- **PATRÓN** `dist_50` > `0.3938` → IC=+0.483 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3938 (IC base=+0.422)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.447 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.422)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `dist_50` > `0.47` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.433)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.413 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.433)

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

- **PATRÓN** `edge` > `0.1043` → IC=+0.474 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1043 (IC base=+0.474)

- **PATRÓN** `sigma_h` < `0.0163` → IC=+0.475 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0163 (IC base=+0.474)

- **PATRÓN** `T_h` > `0.9178` → IC=+0.472 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9178 (IC base=+0.474)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.486 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.474)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.464 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.474)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.464 (n=82)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.474)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=151)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=275)

- **PATRÓN** `streak_estiramiento` < `0.4576` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.4576 (IC base=+0.024)

- **PATRÓN** `streak_estiramiento` < `0.4095` → IC=+0.200 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4095 (IC base=+0.037)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `ballena_activa_n` > `52.0` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 52.0
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=33)

- **PATRÓN** `volumen_racha` < `990711.2` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_racha` < 990711.2 (IC base=+0.000)

- **PATRÓN** `streak_estiramiento` < `0.4152` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `streak_estiramiento` < 0.4152 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 52.0 (IC base=+0.000)

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
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=693)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=699)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=372)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `libro_liquidez` < `2389.5844` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2389.5844
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=550)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1101)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=676)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=674)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2733)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1405)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1413)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.225 (n=649)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.1629` → IC=+0.193 (n=1260)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1629 (IC base=+0.186)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2158` → IC=+0.193 (n=477)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.2158 (IC base=+0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1293` → IC=+0.225 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1293 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.200 (n=1014)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.186 (n=1443)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 16.0 (IC base=+0.186)

- **PATRÓN** `ibs_15` > `0.6111` → IC=+0.261 (n=1431)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6111 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.2918` → IC=+0.189 (n=519)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.2918 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.023` → IC=+0.274 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.023 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `2980.0928` → IC=+0.189 (n=954)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2980.0928 (IC base=+0.186)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=505)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.218 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.283 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.201)

- **PATRÓN** `drift_15min` |x|≤ `0.3806` → IC=+0.204 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3806 (IC base=+0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.239 (n=113)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.201)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1484` → IC=+0.263 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1484 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.223 (n=355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.201)

- **PATRÓN** `ibs_15` > `0.7004` → IC=+0.267 (n=337)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7004 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.3854` → IC=+0.260 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3854 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.495` → IC=+0.256 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.495 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `15901.5027` → IC=+0.230 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15901.5027 (IC base=+0.201)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `25.173` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 25.173
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=323)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.144 (n=116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0035 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.165 (n=228)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0051 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0691` → IC=+0.154 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0691 (IC base=+0.140)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2346` → IC=+0.172 (n=114)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.2346 (IC base=+0.140)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2558` → IC=+0.164 (n=239)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2558 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.165 (n=255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.140)

- **PATRÓN** `ibs_15` > `0.617` → IC=+0.215 (n=342)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.617 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.4333` → IC=+0.142 (n=107)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.4333 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.158 (n=264)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.57` → IC=+0.210 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.57 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `3459.7073` → IC=+0.146 (n=306)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3459.7073 (IC base=+0.140)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=75)

- **PATRÓN** `drift_60min` |x|≤ `0.1422` → IC=+0.122 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.1422 (IC base=-0.019)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.254 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.1481` → IC=+0.203 (n=156)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1481 (IC base=+0.162)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0662` → IC=+0.194 (n=158)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.0662 (IC base=+0.162)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2813` → IC=+0.218 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2813 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.205 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.162)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.244 (n=178)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.118` → IC=+0.186 (n=103)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.118 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.532` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.532 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=138)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `3004.732` → IC=+0.268 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3004.732 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.219 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.162)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.7105` → IC=-0.146 (n=97)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.7105
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=779)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `24.851` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 24.851 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.662` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 15.662 (IC base=+0.010)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0174` → IC=+0.229 (n=260)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0174 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.201 (n=172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.183)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0605` → IC=+0.194 (n=348)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.0605 (IC base=+0.183)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0904` → IC=+0.240 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0904 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.227 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.183)

- **PATRÓN** `ibs_15` > `0.5455` → IC=+0.278 (n=390)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5455 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.1268` → IC=+0.204 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1268 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.941` → IC=+0.227 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.941 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.489` → IC=+0.186 (n=348)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 7.489 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2864.0056` → IC=+0.273 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2864.0056 (IC base=+0.183)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.163 (n=434)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.81€ cuando `ibs_15` < 0.1176 (IC base=+0.045)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.376 (n=175)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.337)

- **PATRÓN** `drift_60min` |x|≤ `0.1082` → IC=+0.342 (n=257)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1082 (IC base=+0.337)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.365 (n=257)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.337)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1304` → IC=+0.374 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1304 (IC base=+0.337)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.361 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.337)

- **PATRÓN** `ibs_15` > `0.7853` → IC=+0.384 (n=385)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7853 (IC base=+0.337)

- **PATRÓN** `dist_vwap_pct` > `0.4313` → IC=+0.375 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4313 (IC base=+0.337)

- **PATRÓN** `dist_vwap_pct` < `0.1081` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1081 (IC base=+0.337)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.117` → IC=+0.348 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.117 (IC base=+0.337)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.342 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.337)

- **PATRÓN** `libro_liquidez` > `3525.4286` → IC=+0.353 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3525.4286 (IC base=+0.337)

- **PATRÓN** `ballena_activa_n` < `475.0` → IC=+0.360 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 475.0 (IC base=+0.337)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.344 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.341)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.378 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.341)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.351 (n=72)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.341)

- **PATRÓN** `drift_15min` |x|≤ `0.4231` → IC=+0.345 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4231 (IC base=+0.341)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.363 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.341)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1231` → IC=+0.390 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1231 (IC base=+0.341)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.367 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.341)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.381 (n=216)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.341)

- **PATRÓN** `dist_vwap_pct` > `0.4016` → IC=+0.406 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4016 (IC base=+0.341)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.381` → IC=+0.357 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.381 (IC base=+0.341)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.472` → IC=+0.341 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.472 (IC base=+0.341)

- **PATRÓN** `ballena_activa_n` < `582.0` → IC=+0.394 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 582.0 (IC base=+0.341)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.370 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.329)

- **PATRÓN** `drift_60min` |x|≤ `0.1039` → IC=+0.336 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1039 (IC base=+0.329)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0587` → IC=+0.343 (n=170)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0587 (IC base=+0.329)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.350 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.329)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.389 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.329)

- **PATRÓN** `ibs_15` > `0.7403` → IC=+0.390 (n=170)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7403 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` < `0.1227` → IC=+0.342 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1227 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.717` → IC=+0.346 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.717 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.330 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.329)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.340 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.329)

- **PATRÓN** `libro_liquidez` > `4001.8474` → IC=+0.361 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4001.8474 (IC base=+0.329)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.013` → IC=-0.214 (n=607)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1823)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.191 (n=785)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1645)

- **FILTRO** `libro_liquidez` < `3944.0493` → IC=-0.134 (n=1603)

  - _Acción_: SKIP cuando `libro_liquidez` < 3944.0493
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=827)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.262 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=-0.060)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.267 (n=600)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` > `0.4333` → IC=+0.175 (n=155)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.4333 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` < `0.1129` → IC=+0.180 (n=367)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1129 (IC base=-0.060)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1171` → IC=+0.237 (n=997)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1171 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1786` → IC=+0.244 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1786 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.3519` → IC=+0.282 (n=1497)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3519 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.6682` → IC=+0.289 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6682 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.217 (n=373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=1122)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.223 (n=493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1002)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.207 (n=951)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=544)

- **FILTRO** `sigma_ewma_delta_pct` > `19.716` → IC=-0.244 (n=264)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.716
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=1231)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.171 (n=138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0028 (IC base=+0.081)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.284 (n=72)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.081)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.346 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.081)

- **PATRÓN** `ibs_15` > `0.7413` → IC=+0.330 (n=157)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7413 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1352` → IC=+0.286 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1352 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.5415` → IC=+0.282 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5415 (IC base=+0.081)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6642` → IC=-0.208 (n=94)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6642
  - _Potencial_: sin este filtro IC_bueno=+0.260 (n=289)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=366)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.180 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0051 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0768` → IC=+0.213 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0768 (IC base=+0.144)

- **PATRÓN** `drift_15min` |x|≤ `0.4246` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `drift_15min` |x|≤ 0.4246 (IC base=+0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1323` → IC=+0.155 (n=192)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.1323 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.236 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.6642` → IC=+0.260 (n=289)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6642 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.4713` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.4713 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1175` → IC=+0.180 (n=204)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1175 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.661` → IC=+0.155 (n=227)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 6.661 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=366)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `10970.0273` → IC=+0.177 (n=131)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 10970.0273 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.241 (n=611)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.229)

- **PATRÓN** `drift_15min` |x|≤ `0.778` → IC=+0.237 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.778 (IC base=+0.229)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2` → IC=+0.253 (n=277)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_15` < `0.3482` → IC=+0.268 (n=611)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3482 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.764` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.764 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.074` → IC=+0.262 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.074 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.283` → IC=+0.231 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.283 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `3539.2271` → IC=+0.234 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3539.2271 (IC base=+0.229)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0101` → IC=-0.224 (n=143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0101
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=430)

- **FILTRO** `drift_60min` |x|> `0.1682` → IC=-0.219 (n=194)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=379)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.252 (n=143)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=430)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.161)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.161)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0746` → IC=+0.217 (n=249)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0746 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.3542` → IC=+0.262 (n=279)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3542 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.7153` → IC=+0.208 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7153 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` < `0.1873` → IC=+0.217 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1873 (IC base=-0.044)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0196` → IC=-0.262 (n=364)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0196
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=366)

- **FILTRO** `drift_15min` |x|> `1.2028` → IC=-0.245 (n=182)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2028
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=548)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.260 (n=181)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=549)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1035` → IC=+0.374 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1035 (IC base=-0.046)

- **PATRÓN** `ibs_15` < `0.3448` → IC=+0.318 (n=415)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3448 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` > `0.8408` → IC=+0.369 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8408 (IC base=-0.046)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.179 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1565` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1565 (IC base=+0.069)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.179 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1565` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1565 (IC base=+0.069)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.292 (n=622)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.293 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.309 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.296 (n=415)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1084` → IC=+0.344 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1084 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.325 (n=622)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2755` → IC=+0.326 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2755 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.164` → IC=+0.331 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.164 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.292 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `14286.1908` → IC=+0.309 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14286.1908 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.312 (n=115)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.291 (n=156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.338 (n=115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.295 (n=115)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3729` → IC=+0.304 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3729 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.304 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8303` → IC=+0.317 (n=343)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8303 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2601` → IC=+0.350 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2601 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.364 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `15942.3752` → IC=+0.329 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15942.3752 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.301 (n=280)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.113` → IC=+0.294 (n=187)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.113 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.308 (n=186)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.330 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.330 (n=251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8475` → IC=+0.333 (n=279)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8475 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.6362` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6362 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` < `0.167` → IC=+0.293 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.167 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.320 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.304 (n=320)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6111 sube el IC de +0.186 a +0.261 en UPDOWN_GBM#15min (n=1431). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7004 sube el IC de +0.201 a +0.267 en UPDOWN_GBM#BTC#15min (n=337). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.617 sube el IC de +0.140 a +0.215 en UPDOWN_GBM#ETH#15min (n=342). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.162 a +0.244 en UPDOWN_GBM#SOL#15min (n=178). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5455 sube el IC de +0.183 a +0.278 en UPDOWN_GBM#XRP#15min (n=390). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.045 a +0.163 en UPDOWN_GBM#XRP#15min (n=434). Ya aplicado como kelly_boost=+0.81€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.060 a +0.267 en UPDOWN_GBM_15M_TARDIO (n=600). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3519 sube el IC de -0.039 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=1497). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7413 sube el IC de +0.081 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=157). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6642 sube el IC de +0.144 a +0.260 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=289). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3482 sube el IC de +0.229 a +0.268 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=611). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.161 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3542 sube el IC de -0.044 a +0.262 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=279). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3448 sube el IC de -0.046 a +0.318 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=415). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.289 a +0.325 en UPDOWN_GBM_IBS_ALTO (n=622). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.284 a +0.317 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=343). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8475 sube el IC de +0.294 a +0.333 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=279). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7853 sube el IC de +0.337 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=385). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.341 a +0.381 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=216). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7403 sube el IC de +0.329 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=170). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1257 | +0.090 | +150.46€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1257 | +0.090 | +150.46€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 928 | +0.099 | +125.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 928 | +0.099 | +125.27€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 243 | +0.047 | +6.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 243 | +0.047 | +6.54€ | 4 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 6 |
| ✅ BALLENAS_TARDIAS | 23683 | -0.091 | -3114.94€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1409 | -0.046 | -215.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 22274 | -0.094 | -2899.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3565 | -0.084 | -573.90€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3565 | -0.084 | -573.90€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1409 | -0.046 | -215.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1409 | -0.046 | -215.52€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 6804 | -0.028 | -606.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 6804 | -0.028 | -606.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6270 | -0.094 | -415.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6270 | -0.094 | -415.73€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5261 | -0.184 | -1142.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5261 | -0.184 | -1142.46€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 16184 | -0.031 | +4127.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4251 | -0.001 | +1836.18€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 11933 | -0.042 | +2291.61€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 16184 | -0.031 | +4127.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4251 | -0.001 | +1836.18€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 11933 | -0.042 | +2291.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1430 | -0.102 | -182.85€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 163 | -0.051 | -20.01€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1267 | -0.108 | -162.85€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 775 | -0.091 | -96.28€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 139 | -0.046 | -14.78€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 457 | -0.128 | -72.69€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 433 | -0.130 | -67.47€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 86723 | +0.113 | -4413.03€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 13268 | +0.184 | -427.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 343 | -0.097 | -49.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 67377 | +0.100 | -3741.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5735 | +0.110 | -194.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 11213 | +0.098 | -981.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 44 | -0.174 | -3.33€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 11154 | +0.099 | -965.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 17539 | +0.132 | -360.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4140 | +0.201 | -144.23€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 11168 | +0.112 | -172.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2189 | +0.108 | -21.00€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 11253 | +0.089 | -1072.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 51 | -0.085 | -5.77€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 11187 | +0.090 | -1055.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 18490 | +0.124 | -371.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5126 | +0.175 | -78.11€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 11279 | +0.105 | -232.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2073 | +0.098 | -51.96€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 16999 | +0.115 | -969.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3863 | +0.188 | -204.52€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 246 | -0.057 | +4.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 11417 | +0.093 | -648.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1473 | +0.129 | -121.21€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 11229 | +0.102 | -658.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 44 | -0.022 | +8.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 11172 | +0.102 | -666.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 13759 | +0.193 | -886.40€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 13759 | +0.193 | -886.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3310 | +0.169 | -349.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3310 | +0.169 | -349.61€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1032 | +0.199 | +2.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1032 | +0.199 | +2.79€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3246 | +0.183 | -268.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3246 | +0.183 | -268.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2907 | +0.239 | -93.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2907 | +0.239 | -93.29€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3185 | +0.193 | -191.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3185 | +0.193 | -191.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 651 | +0.428 | -20.39€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 651 | +0.428 | -20.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 247 | +0.432 | -5.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 247 | +0.432 | -5.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 245 | +0.435 | -2.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 245 | +0.435 | -2.93€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 151 | +0.402 | -11.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 151 | +0.402 | -11.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 47190 | +0.198 | -3690.09€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 47190 | +0.198 | -3690.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8177 | +0.176 | -950.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8177 | +0.176 | -950.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 7530 | +0.225 | -265.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 7530 | +0.225 | -265.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8151 | +0.174 | -967.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8151 | +0.174 | -967.27€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 7618 | +0.220 | -291.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 7618 | +0.220 | -291.52€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 7795 | +0.204 | -508.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 7795 | +0.204 | -508.33€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 7919 | +0.193 | -706.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 7919 | +0.193 | -706.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 17748 | +0.119 | +170.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 17748 | +0.119 | +170.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 8804 | +0.122 | +131.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 8804 | +0.122 | +131.93€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 8944 | +0.115 | +38.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 8944 | +0.115 | +38.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1399 | +0.292 | -5.26€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1399 | +0.292 | -5.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 623 | +0.278 | -15.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 623 | +0.278 | -15.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 672 | +0.297 | +8.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 672 | +0.297 | +8.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 104 | +0.340 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 104 | +0.340 | +1.79€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 615 | +0.438 | +0.50€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 615 | +0.438 | +0.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 291 | +0.439 | +0.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 291 | +0.439 | +0.08€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 284 | +0.441 | +0.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 284 | +0.441 | +0.53€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 40 | +0.381 | -0.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 40 | +0.381 | -0.11€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1031 | +0.077 | -37.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 359 | +0.065 | -25.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 672 | +0.083 | -11.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 810 | +0.085 | -12.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 138 | +0.093 | -0.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 672 | +0.083 | -11.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 160 | +0.018 | -29.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 160 | +0.018 | -29.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 32431 | +0.098 | -1004.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2688 | +0.089 | +15.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 29743 | +0.098 | -1020.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 18286 | +0.102 | -296.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2688 | +0.089 | +15.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 15598 | +0.104 | -312.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 5966 | +0.108 | -30.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 5966 | +0.108 | -30.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 8179 | +0.081 | -676.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 8179 | +0.081 | -676.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 770 | +0.223 | -92.87€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 770 | +0.223 | -92.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 770 | +0.223 | -92.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 770 | +0.223 | -92.87€ | 2 | 4 |
| ✅ GBM_LATE_15M | 23522 | +0.080 | +11026.24€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 23522 | +0.080 | +11026.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3898 | +0.194 | +2838.28€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3898 | +0.194 | +2838.28€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 3491 | +0.175 | +2377.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3491 | +0.175 | +2377.89€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 4051 | +0.201 | +3059.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4051 | +0.201 | +3059.54€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 3506 | +0.016 | +685.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3506 | +0.016 | +685.03€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3415 | -0.034 | +781.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3415 | -0.034 | +781.40€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 5161 | -0.044 | +1284.10€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5161 | -0.044 | +1284.10€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 24885 | +0.083 | +12976.40€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 24885 | +0.083 | +12976.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4739 | +0.014 | +2588.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4739 | +0.014 | +2588.34€ | 2 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5195 | +0.011 | +1026.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5195 | +0.011 | +1026.52€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3512 | +0.263 | +3550.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3512 | +0.263 | +3550.12€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4013 | -0.002 | +723.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4013 | -0.002 | +723.32€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4044 | +0.024 | +1505.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4044 | +0.024 | +1505.63€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3382 | +0.274 | +3582.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3382 | +0.274 | +3582.46€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 19011 | +0.168 | +14060.80€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 19011 | +0.168 | +14060.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2850 | +0.207 | +2266.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2850 | +0.207 | +2266.66€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3026 | +0.149 | +2169.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3026 | +0.149 | +2169.93€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2964 | +0.210 | +2386.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2964 | +0.210 | +2386.75€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3187 | +0.134 | +2157.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3187 | +0.134 | +2157.50€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3549 | +0.114 | +2374.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3549 | +0.114 | +2374.26€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3435 | +0.203 | +2705.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3435 | +0.203 | +2705.70€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4660 | +0.122 | +1861.40€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4660 | +0.122 | +1861.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1320 | +0.116 | +548.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1320 | +0.116 | +548.52€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 369 | +0.147 | +180.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 369 | +0.147 | +180.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1297 | +0.139 | +557.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1297 | +0.139 | +557.60€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 986 | +0.091 | +281.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 986 | +0.091 | +281.58€ | 2 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 504 | +0.134 | +216.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 504 | +0.134 | +216.54€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 23621 | +0.174 | +17392.17€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 23621 | +0.174 | +17392.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3721 | +0.220 | +3127.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3721 | +0.220 | +3127.92€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3700 | +0.149 | +2402.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3700 | +0.149 | +2402.18€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3844 | +0.227 | +3335.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3844 | +0.227 | +3335.28€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3837 | +0.136 | +2564.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3837 | +0.136 | +2564.18€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4154 | +0.110 | +2553.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4154 | +0.110 | +2553.98€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4365 | +0.203 | +3408.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4365 | +0.203 | +3408.63€ | 0 | 22 |
| ✅ GBM_LATE_5M | 6515 | +0.142 | +3588.77€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 6515 | +0.142 | +3588.77€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1688 | +0.140 | +1074.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1688 | +0.140 | +1074.38€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 2041 | +0.146 | +1108.61€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2041 | +0.146 | +1108.61€ | 0 | 32 |
| ✅ GBM_LATE_5M#SOL | 484 | +0.072 | +108.39€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 484 | +0.072 | +108.39€ | 0 | 10 |
| ✅ GBM_LATE_5M#XRP | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1535 | +0.067 | +662.97€ | 2 | 11 |
| ✅ GBM_LATE_60M#60min | 1535 | +0.067 | +662.97€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 552 | +0.087 | +230.35€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 552 | +0.087 | +230.35€ | 0 | 14 |
| ✅ GBM_LATE_60M#ETH | 510 | +0.070 | +258.31€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 510 | +0.070 | +258.31€ | 2 | 19 |
| ✅ GBM_LATE_60M#SOL | 473 | +0.041 | +174.31€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 473 | +0.041 | +174.31€ | 1 | 12 |
| 🚫 GBM_LATE_60M_FADE | 341 | -0.261 | -26.11€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 341 | -0.261 | -26.11€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 130 | -0.212 | -8.27€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 130 | -0.212 | -8.27€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 112 | -0.281 | -11.47€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 112 | -0.281 | -11.47€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 99 | -0.292 | -6.37€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 99 | -0.292 | -6.37€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 649 | +0.058 | +124.03€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 649 | +0.058 | +124.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 254 | +0.051 | +45.16€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 254 | +0.051 | +45.16€ | 2 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 189 | +0.029 | -3.13€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 189 | +0.029 | -3.13€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 206 | +0.091 | +82.00€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 206 | +0.091 | +82.00€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN | 88 | +0.267 | +72.88€ | 0 | 4 |
| ✅ LATE_WINDOW_5MIN#5min | 88 | +0.267 | +72.88€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 88 | +0.267 | +72.88€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 88 | +0.267 | +72.88€ | 0 | 4 |
| ✅ LEADLAG_BTC_XRP_15M | 1754 | +0.097 | +471.05€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1754 | +0.097 | +471.05€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1754 | +0.097 | +471.05€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1754 | +0.097 | +471.05€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 367 | -0.080 | -33.57€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 367 | -0.080 | -33.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 94 | -0.062 | -5.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 94 | -0.062 | -5.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 125 | -0.020 | -3.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 125 | -0.020 | -3.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1790 | +0.006 | +14.64€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1790 | +0.006 | +14.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 96 | +0.000 | -2.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 96 | +0.000 | -2.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 194 | +0.000 | +12.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 194 | +0.000 | +12.80€ | 3 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 124 | -0.032 | -5.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 124 | -0.032 | -5.20€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 761 | +0.031 | +25.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 761 | +0.031 | +25.02€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 465 | -0.003 | -6.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 465 | -0.003 | -6.48€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 150 | -0.053 | -8.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 150 | -0.053 | -8.55€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 1013 | -0.047 | -28.68€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1013 | -0.047 | -28.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 289 | -0.043 | -12.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 289 | -0.043 | -12.32€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 334 | -0.036 | -4.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 334 | -0.036 | -4.55€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 390 | -0.059 | -11.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 390 | -0.059 | -11.82€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M | 14151 | -0.012 | -213.14€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14151 | -0.012 | -213.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2868 | -0.024 | -66.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2868 | -0.024 | -66.32€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 26439 | -0.008 | +1154.15€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 26439 | -0.008 | +1154.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4643 | +0.015 | +581.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4643 | +0.015 | +581.77€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4151 | -0.027 | -43.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4151 | -0.027 | -43.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4677 | +0.012 | +400.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4677 | +0.012 | +400.70€ | 3 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3929 | -0.053 | -140.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3929 | -0.053 | -140.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4425 | -0.012 | +164.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4425 | -0.012 | +164.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4614 | +0.006 | +190.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4614 | +0.006 | +190.96€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE | 5559 | -0.055 | -136.69€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5559 | -0.055 | -136.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1302 | -0.073 | -33.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1302 | -0.073 | -33.71€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 569 | -0.123 | -23.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 569 | -0.123 | -23.65€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1595 | -0.075 | -32.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1595 | -0.075 | -32.65€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 67449 | -0.073 | +1556.24€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 67449 | -0.073 | +1556.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 11380 | -0.079 | +658.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 11380 | -0.079 | +658.21€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 10443 | -0.093 | -468.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 10443 | -0.093 | -468.58€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 11534 | -0.069 | +622.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 11534 | -0.069 | +622.37€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 9971 | -0.093 | -169.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 9971 | -0.093 | -169.27€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 12380 | -0.049 | +353.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 12380 | -0.049 | +353.27€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 11741 | -0.062 | +560.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 11741 | -0.062 | +560.24€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6916 | -0.024 | -104.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6916 | -0.024 | -104.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1619 | -0.025 | -3.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1619 | -0.025 | -3.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1537 | -0.021 | -9.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1537 | -0.021 | -9.98€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1023 | -0.040 | -16.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1023 | -0.040 | -16.69€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1083 | +0.108 | +364.09€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 947 | +0.115 | +351.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 219 | +0.138 | +109.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 219 | +0.138 | +109.49€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 186 | +0.096 | +44.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 186 | +0.096 | +44.24€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 191 | +0.091 | +58.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 191 | +0.091 | +58.77€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 165 | +0.141 | +80.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 165 | +0.141 | +80.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 186 | +0.106 | +58.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 186 | +0.106 | +58.13€ | 0 | 5 |
| ✅ ORDER_FLOW_5M_REACTIVO | 390 | -0.046 | -32.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 390 | -0.046 | -32.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 84 | +0.035 | +11.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 84 | +0.035 | +11.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 50 | -0.115 | -13.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 50 | -0.115 | -13.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 111 | -0.084 | -22.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 111 | -0.084 | -22.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 75 | +0.006 | +3.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 75 | +0.006 | +3.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 70 | -0.083 | -10.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 70 | -0.083 | -10.53€ | 0 | 0 |
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
| 🚫 PRICE_TARGET_GBM_FADE | 653 | -0.210 | -35.95€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 268 | -0.200 | -30.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 231 | -0.195 | -30.34€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 229 | -0.227 | -23.00€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 197 | -0.239 | -27.66€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 156 | -0.196 | +17.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 140 | -0.197 | +13.11€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 568 | -0.212 | -44.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 256 | +0.415 | +207.32€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#BTC | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 65 | +0.396 | +60.03€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 65 | +0.396 | +60.03€ | 0 | 3 |
| ✅ RESOLUTION_SNIPER#SOL | 163 | +0.482 | +152.04€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 163 | +0.482 | +152.04€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#sniper | 256 | +0.415 | +207.32€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 464 | +0.032 | +13.35€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 464 | +0.032 | +13.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 217 | +0.034 | +4.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 217 | +0.034 | +4.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 30 | +0.062 | +0.07€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 30 | +0.062 | +0.07€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 48 | -0.020 | -3.52€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 48 | -0.020 | -3.52€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 169 | +0.038 | +12.00€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 169 | +0.038 | +12.00€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 2649 | -0.024 | -113.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2649 | -0.024 | -113.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 565 | -0.022 | -22.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 565 | -0.022 | -22.81€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1125 | -0.025 | -49.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1125 | -0.025 | -49.10€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 67 | -0.051 | -6.33€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 67 | -0.051 | -6.33€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 37 | -0.090 | -3.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 37 | -0.090 | -3.93€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 30 | +0.000 | -2.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 30 | +0.000 | -2.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7374 | +0.023 | +107.98€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7374 | +0.023 | +107.98€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2121 | +0.021 | +20.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2121 | +0.021 | +20.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1614 | +0.035 | +49.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1614 | +0.035 | +49.53€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2247 | +0.011 | +1.70€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2247 | +0.011 | +1.70€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1392 | +0.029 | +35.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1392 | +0.029 | +35.84€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 6892 | +0.009 | -58.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 6892 | +0.009 | -58.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2752 | +0.013 | -16.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2752 | +0.013 | -16.31€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2703 | +0.011 | -19.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2703 | +0.011 | -19.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1437 | -0.000 | -22.40€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1437 | -0.000 | -22.40€ | 2 | 0 |
| ✅ UPDOWN_GBM | 33017 | +0.030 | +1943.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 8855 | +0.062 | +1534.39€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 1224 | +0.005 | +8.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 20804 | +0.022 | +379.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2007 | +0.008 | +22.58€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3150 | +0.068 | +332.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 467 | +0.155 | +191.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 23 | -0.020 | -0.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2660 | +0.054 | +141.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 6154 | +0.033 | +399.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1120 | +0.078 | +241.18€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 338 | +0.021 | +7.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 3747 | +0.030 | +135.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 900 | +0.003 | +15.04€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 49 | -0.108 | +0.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 3857 | +0.040 | +217.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 441 | +0.141 | +165.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 20 | +0.000 | +0.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3396 | +0.026 | +51.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 7007 | +0.019 | +287.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2346 | +0.045 | +259.75€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 326 | +0.006 | +7.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 3604 | +0.009 | +15.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 690 | +0.007 | +0.85€ | 1 | 1 |
| ✅ UPDOWN_GBM#ETH#daily | 41 | -0.151 | +3.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 8011 | +0.016 | +201.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2242 | +0.023 | +140.63€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 320 | -0.006 | -3.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4997 | +0.015 | +60.34€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 417 | +0.020 | +6.69€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#daily | 35 | -0.176 | -2.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 4836 | +0.036 | +507.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2239 | +0.077 | +535.66€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 197 | -0.003 | -2.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2400 | -0.000 | -25.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 125 | -0.146 | +0.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 513 | +0.337 | +149.18€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 513 | +0.337 | +149.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 287 | +0.341 | +80.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 287 | +0.341 | +80.26€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 226 | +0.329 | +68.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 226 | +0.329 | +68.92€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 10865 | -0.044 | +2252.10€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 10865 | -0.044 | +2252.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 629 | -0.045 | +333.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 629 | -0.045 | +333.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2046 | -0.123 | +31.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2046 | -0.123 | +31.72€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 268 | +0.159 | +155.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 268 | +0.159 | +155.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1197 | +0.202 | +694.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1197 | +0.202 | +694.83€ | 2 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3356 | -0.064 | +520.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3356 | -0.064 | +520.96€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3369 | -0.079 | +516.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3369 | -0.079 | +516.28€ | 3 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 127 | +0.050 | +9.69€ | 2 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 127 | +0.050 | +9.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 127 | +0.050 | +9.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 127 | +0.050 | +9.69€ | 2 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO | 829 | +0.289 | +665.43€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 829 | +0.289 | +665.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 457 | +0.284 | +345.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 457 | +0.284 | +345.18€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 372 | +0.294 | +320.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 372 | +0.294 | +320.24€ | 0 | 10 |
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
| ✅ WEEKLY_PRICE#BTC | 761 | +0.248 | +106.26€ | 0 | 4 |
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
  - _Estado_: 506 celda(s) pasan gate riguroso completo de 2149 evaluadas (n>=40) y 3158 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.023 < 0.08 — monitorear
  - _Datos_: n=2241 IC=+0.023 PNL=+140.15€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=820/15 IC=+0.288 PNL=+332.38€ | BTC: n=761/15 IC=+0.248 PNL=+106.26€ | SOL: n=642/15 IC=+0.376 PNL=+668.23€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.091 n=252/60 | contraria IC=+0.147 n=242 | gap=-0.057 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=269, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=690/40 IC=+0.007 PNL=+0.85€ | BTC#60min: n=900/40 IC=+0.003 PNL=+15.04€ | SOL#60min: n=417/40 IC=+0.020 PNL=+6.69€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.052 n=309043 | tras_1loss IC=+0.076 n=240546 | tras_2loss IC=+0.045 n=101946/40 | gap=+0.007 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=294 PNL=+187.59€
  - _Datos_: n=294 IC=+0.179 PNL=+187.59€

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
  - _Estado_: n=1448 IC=+0.018 PNL=+16.00€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1448 IC=+0.018 PNL=+16.00€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=559 IC=-0.017 PNL=+6.58€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=559 IC=-0.017 PNL=+6.58€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.186 > 0.1 con n=1907 PNL=+1181.12€
  - _Datos_: n=1907 IC=+0.186 PNL=+1181.12€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1120 IC=+0.078 PNL=+241.18€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1120 IC=+0.078 PNL=+241.18€

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
  - _Estado_: n=482 IC=+0.012 PNL=+33.84€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=482 IC=+0.012 PNL=+33.84€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=43 IC=+0.056 PNL=+2.44€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=43 IC=+0.056 PNL=+2.44€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.267 n=88) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=88 IC=+0.267 PNL=+72.88€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.02 con n=620 PNL=+244.42€
  - _Datos_: n=620 IC=+0.125 PNL=+244.42€

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
  - _Estado_: n=11434 IC=+0.057 PNL=+1422.87€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=11434 IC=+0.057 PNL=+1422.87€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.170 < -0.1 con n=210 PNL=+16.26€
  - _Datos_: n=210 IC=-0.170 PNL=+16.26€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1719 IC=+0.045 PNL=+180.38€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1719 IC=+0.045 PNL=+180.38€

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
  - _Estado_: n=16290 IC=-0.137 PNL=+1121.23€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=16290 IC=-0.137 PNL=+1121.23€

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
  - _Estado_: n=1775 IC=+0.136 PNL=+942.99€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1775 IC=+0.136 PNL=+942.99€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=3406 IC=+0.018 PNL=+107.38€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3406 IC=+0.018 PNL=+107.38€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.085 > 0.08 con n=1885 PNL=+981.47€
  - _Datos_: n=1885 IC=+0.085 PNL=+981.47€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.239 < -0.1 con n=1609 PNL=-181.74€
  - _Datos_: n=1609 IC=-0.239 PNL=-181.74€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.090 n=900) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=900 IC=+0.090 PNL=+209.11€

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
  - _Estado_: n=8175 IC=+0.176 PNL=-949.68€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8175 IC=+0.176 PNL=-949.68€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.202 > 0.1 con n=129 PNL=+76.64€
  - _Datos_: n=129 IC=+0.202 PNL=+76.64€
