# Hipótesis automáticas — 2026-10-07 15:13 UTC
_Generado por shadow_postmortem.py sobre 792919 resoluciones (PNL=+97754.30€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.212 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.201 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.6177` → IC=+0.243 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6177 (IC base=+0.122)

- **PATRÓN** `banda_z` > `9.03` → IC=+0.190 (n=224)

  - _Acción_: Kelly boost +0.95€ cuando `banda_z` > 9.03 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=705)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.122)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.232 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.126)

- **PATRÓN** `n_total_lado` > `76.0` → IC=+0.203 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 76.0 (IC base=+0.126)

- **PATRÓN** `banda_hit_calibrado` > `0.6153` → IC=+0.231 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6153 (IC base=+0.126)

- **PATRÓN** `banda_z` > `9.666` → IC=+0.181 (n=180)

  - _Acción_: Kelly boost +0.91€ cuando `banda_z` > 9.666 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=607)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.126)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.355` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.234 (n=107)

- **FILTRO** `banda_hit_calibrado` < `0.8019` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8019
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=96)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=115)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=94)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=107)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8019` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8019 (IC base=+0.125)

- **PATRÓN** `banda_z` > `7.17` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 7.17 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.128 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `1207.4096` → IC=+0.185 (n=71)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1207.4096 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.5 (IC base=+0.004)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.154)

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
- **FILTRO** `restante_s_al_confirmar` < `143.87` → IC=-0.211 (n=8676)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.87
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=26028)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.69` → IC=-0.270 (n=1090)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.69
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3273)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `123.59` → IC=-0.305 (n=1017)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 123.59
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3054)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `164.76` → IC=-0.223 (n=2199)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 164.76
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=6598)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `129.62` → IC=-0.305 (n=1686)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 129.62
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=5061)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.48` → IC=-0.224 (n=385)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=385)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=174)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=542)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=566)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.259 (n=164)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=169)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.218 (n=69)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=234)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.270 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=156)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.175 (n=78)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=161)

- **FILTRO** `py_entrada` < `0.47` → IC=-0.167 (n=70)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=169)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.685` → IC=+0.213 (n=16706)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.685 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=3933)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `9612.6791` → IC=+0.182 (n=1746)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9612.6791 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=14771)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=18118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=13787)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=6460)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7543.5205` → IC=+0.168 (n=2482)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7543.5205 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=1907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=1861)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=2340)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `16057.1675` → IC=+0.212 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16057.1675 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.199 (n=1682)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=1865)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=2393)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `16023.7287` → IC=+0.209 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16023.7287 (IC base=+0.193)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.122 (n=1054)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.555 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `4614.6151` → IC=+0.123 (n=253)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 4614.6151 (IC base=+0.087)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.139 (n=449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.091)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.138 (n=967)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `5784.0902` → IC=+0.133 (n=235)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 5784.0902 (IC base=+0.091)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=3515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.354 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.232 (n=1568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` < `0.24` → IC=+0.361 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.24 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=751)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` > `0.645` → IC=+0.227 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.645 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=962)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `1320.9779` → IC=+0.138 (n=835)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1320.9779 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.078)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.216 (n=1527)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.216)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.408 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=657)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.289 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=814)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.179 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.375 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.222 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.120)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=14875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=14213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.228 (n=6309)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=3497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=3313)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=3364)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=1498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=993)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.229)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.317 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.229)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=3431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=3279)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.191 (n=1914)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.72 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=3017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.331 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.241)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=3356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=2156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.191 (n=2546)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.71 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.197 (n=1203)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.428 (n=679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=697)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.427 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `6922.3689` → IC=+0.441 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6922.3689 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.433 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.444 (n=177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `19915.0896` → IC=+0.444 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 19915.0896 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.433 (n=252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.424 (n=263)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.433 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.425 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `3382.6049` → IC=+0.435 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3382.6049 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.405)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.407 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.405)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.408 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.405)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.420 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.405)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=44381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=19451)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=7640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.187 (n=6141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.198 (n=8450)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=3960)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.269 (n=4538)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.180 (n=8062)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=6136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=8081)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=3983)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=2744)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=7365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.203 (n=5899)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=2897)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=3158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=3368)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=6829)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.126 (n=6353)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.2 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=6641)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=8387)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.45` → IC=+0.136 (n=6301)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.45 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=3394)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.127 (n=3151)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.141 (n=3324)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=4152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `3.12` → IC=+0.145 (n=3133)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.12 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=3435)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` < `4.23` → IC=+0.123 (n=3191)

  - _Acción_: Kelly boost +0.61€ cuando `restante_min` < 4.23 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.129 (n=3638)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.133 (n=3195)

  - _Acción_: Kelly boost +0.66€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=1411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.379 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `4200.4566` → IC=+0.299 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4200.4566 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.291 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.351 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `3806.0389` → IC=+0.290 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3806.0389 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.292 (n=667)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.385 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1440.426` → IC=+0.301 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1440.426 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.357 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.350)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.375 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.350)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.350)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.354 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.350)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.350)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.443 (n=599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.446 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.443 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.439 (n=294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.447 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.460 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.443 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.452 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.445 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `2138.537` → IC=+0.457 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2138.537 (IC base=+0.443)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.385 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.396)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.409 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.396)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.396)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `5.0` → IC=-0.273 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=78)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `983.8593` → IC=+0.277 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 983.8593 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.273 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=78)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `983.8593` → IC=+0.277 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 983.8593 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.3699` → IC=+0.134 (n=9363)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.3699 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9825` → IC=+0.241 (n=3547)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9825 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.3746` → IC=+0.252 (n=2799)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3746 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.42` → IC=+0.190 (n=2764)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 8.42 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.249 (n=2984)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2089 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6912` → IC=+0.255 (n=2667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6912 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.302` → IC=+0.231 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.302 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.3282` → IC=+0.219 (n=3381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3282 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5639` → IC=+0.141 (n=12982)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5639 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.7477` → IC=+0.206 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7477 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.1493` → IC=+0.182 (n=4415)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1493 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` < `1.1973` → IC=+0.181 (n=4801)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.1973 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` > `1.0532` → IC=+0.182 (n=2176)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0532 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2953` → IC=+0.230 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2953 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` > `1.4487` → IC=+0.203 (n=8220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4487 (IC base=+0.072)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.217 (n=8038)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.072)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.221 (n=789)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.186 (n=790)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0079 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.2797` → IC=+0.182 (n=2083)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.2797 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.194 (n=1140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.183 (n=1587)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 11.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.777` → IC=+0.292 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.777 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.235 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.4344` → IC=+0.182 (n=2239)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4344 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=2445)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `2070.925` → IC=+0.188 (n=789)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2070.925 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.243 (n=1706)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.088` → IC=+0.265 (n=636)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.088 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=699)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0603` → IC=+0.284 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0603 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.526` → IC=+0.251 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.526 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.408` → IC=+0.239 (n=1992)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.408 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.236 (n=1677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2843` → IC=+0.260 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2843 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6222` → IC=+0.253 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6222 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=2098)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1995.52` → IC=+0.237 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1995.52 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.234 (n=832)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1077` → IC=+0.254 (n=830)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1077 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=1892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.3257` → IC=+0.232 (n=1887)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3257 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1942` → IC=+0.221 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1942 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.3455` → IC=+0.222 (n=1772)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3455 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.688` → IC=+0.262 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.688 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `1.2485` → IC=+0.221 (n=1887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2485 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.6188` → IC=+0.222 (n=1888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6188 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.242 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7632` → IC=+0.219 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7632 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.4155` → IC=+0.240 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4155 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.175 (n=632)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0026 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.161 (n=630)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=716)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=858)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7231` → IC=+0.176 (n=1887)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7231 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1316` → IC=+0.154 (n=1722)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1316 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.325` → IC=+0.150 (n=301)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.325 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.31` → IC=+0.142 (n=1731)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.31 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.145 (n=1887)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2025 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.6214` → IC=+0.137 (n=1887)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6214 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0977` → IC=+0.170 (n=685)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0977 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4531` → IC=+0.146 (n=1774)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4531 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7855` → IC=+0.145 (n=1182)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7855 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.169 (n=750)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 230.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.202 (n=2394)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=2520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=2152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.388` → IC=+0.255 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.388 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0965` → IC=+0.193 (n=2102)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0965 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.3482` → IC=+0.195 (n=316)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3482 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.1604` → IC=+0.202 (n=1534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1604 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2856)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `1977.8984` → IC=+0.197 (n=1084)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1977.8984 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.225 (n=1869)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.1785` → IC=+0.226 (n=933)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1785 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=985)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.0636` → IC=+0.240 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0636 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.687` → IC=+0.256 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.687 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3464` → IC=+0.258 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3464 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.716` → IC=+0.220 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.716 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.719` → IC=+0.227 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.719 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2046.5484` → IC=+0.221 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2046.5484 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.216 (n=1929)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.214)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=132)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2859)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.146 (n=450)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0036 (IC base=+0.041)

- **PATRÓN** `ibs_20min` > `0.9588` → IC=+0.221 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9588 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` < `0.1896` → IC=+0.316 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1896 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.981` → IC=+0.176 (n=939)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 4.981 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8538` → IC=+0.322 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8538 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `1.2251` → IC=+0.342 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2251 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.341 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.350 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `2.2083` → IC=+0.322 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2083 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.319 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.0982` → IC=+0.164 (n=748)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.0982 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.4587` → IC=+0.202 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4587 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `0.8497` → IC=+0.155 (n=797)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8497 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.212 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `1.5272` → IC=+0.168 (n=1019)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.5272 (IC base=+0.030)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.171 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=435)

- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.185 (n=128)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=384)

- **FILTRO** `ibs_20min` > `0.2273` → IC=-0.126 (n=2882)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2273
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=1429)

- **FILTRO** `sigma_ewma_delta_pct` > `8.798` → IC=-0.220 (n=445)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.798
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=3866)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.195 (n=175)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.8 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.9668` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9668 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.359` → IC=+0.137 (n=177)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 2.359 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8994` → IC=+0.271 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8994 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `1.0782` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0782 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.1539` → IC=+0.281 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1539 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.5152` → IC=+0.290 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5152 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.278 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.2273` → IC=+0.138 (n=1429)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.2273 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.2491` → IC=+0.273 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2491 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.6807` → IC=+0.276 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6807 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.312 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.3831` → IC=+0.296 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3831 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6378` → IC=-0.183 (n=755)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6378
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2267)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.212 (n=817)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2205)

- **FILTRO** `ibs_20min` > `0.7628` → IC=-0.208 (n=1121)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7628
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=3364)

- **PATRÓN** `dist_vwap_pct` > `0.4581` → IC=+0.313 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4581 (IC base=-0.072)

- **PATRÓN** `dist_vwap_pct` < `0.1935` → IC=+0.315 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1935 (IC base=-0.072)

- **PATRÓN** `volumen_regimen` < `0.988` → IC=+0.298 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.988 (IC base=-0.072)

- **PATRÓN** `volumen_regimen` > `0.6478` → IC=+0.314 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6478 (IC base=-0.072)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.304 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=-0.072)

- **PATRÓN** `volumen_spike_ratio` < `2.4802` → IC=+0.301 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4802 (IC base=-0.072)

- **PATRÓN** `volumen_spike_ratio` > `1.4422` → IC=+0.301 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4422 (IC base=-0.072)

- **PATRÓN** `dist_vwap_pct` > `0.8069` → IC=+0.286 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8069 (IC base=-0.011)

- **PATRÓN** `volumen_regimen` > `1.0773` → IC=+0.282 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0773 (IC base=-0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.101` → IC=+0.269 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.101 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.257 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1671 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` > `1.4248` → IC=+0.257 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4248 (IC base=-0.011)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.197 (n=4665)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0093 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4671` → IC=+0.186 (n=12491)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4671 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.6692` → IC=+0.283 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6692 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.691` → IC=+0.152 (n=6303)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.691 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.1748` → IC=+0.247 (n=5118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1748 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.256 (n=4574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` < `0.0803` → IC=+0.242 (n=7572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0803 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.258 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4667` → IC=+0.245 (n=2751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4667 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6397` → IC=+0.256 (n=2750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6397 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.276 (n=7800)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.166 (n=4519)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0089 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5433` → IC=+0.159 (n=11906)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5433 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.676` → IC=+0.252 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.676 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1717` → IC=+0.252 (n=3776)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1717 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1978` → IC=+0.261 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1978 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.310 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5881` → IC=+0.279 (n=2523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5881 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2751` → IC=+0.269 (n=2599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2751 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.283 (n=5641)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2587` → IC=-0.167 (n=974)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2587
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=2923)

- **FILTRO** `ibs_20min` > `0.7564` → IC=-0.174 (n=802)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7564
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=2409)

- **FILTRO** `sigma_ewma_delta_pct` > `4.624` → IC=-0.174 (n=713)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.624
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2498)

- **PATRÓN** `ibs_20min` > `0.9049` → IC=+0.272 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9049 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.301` → IC=+0.200 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.301 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2273` → IC=+0.272 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2273 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `1.4426` → IC=+0.214 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4426 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.235 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.228 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.1616` → IC=+0.155 (n=803)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.1616 (IC base=-0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.0743` → IC=+0.418 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0743 (IC base=-0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.426 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.6397` → IC=+0.427 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6397 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.5288` → IC=+0.427 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5288 (IC base=-0.021)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.418 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8632` → IC=+0.155 (n=939)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.8632 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.1166` → IC=+0.193 (n=708)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1166 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` > `0.6783` → IC=+0.183 (n=1189)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6783 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.217 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4273` → IC=+0.203 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4273 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` > `2.423` → IC=+0.187 (n=436)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.423 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `227.0` → IC=+0.234 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 227.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.155` → IC=+0.226 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.155 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `0.6187` → IC=+0.232 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6187 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0736` → IC=+0.221 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0736 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2721` → IC=+0.306 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2721 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5536` → IC=+0.229 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5536 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1744` → IC=+0.240 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1744 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.272 (n=2109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.252)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=2120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.253 (n=2127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.252)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.781` → IC=+0.283 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.781 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` < `0.1318` → IC=+0.264 (n=1916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1318 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` > `2.1675` → IC=+0.262 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1675 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=2495)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.252)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.303 (n=1773)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1822` → IC=+0.303 (n=780)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1822 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.322 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.3602` → IC=+0.292 (n=1772)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3602 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.304 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.1935` → IC=+0.283 (n=1725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1935 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.339` → IC=+0.296 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.339 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.5684` → IC=+0.304 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5684 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.6195` → IC=+0.292 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6195 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `2041.8956` → IC=+0.303 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2041.8956 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.288 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.287)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7639` → IC=-0.181 (n=812)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7639
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=2437)

- **PATRÓN** `ibs_20min` > `0.8996` → IC=+0.164 (n=744)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8996 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.218 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.0092` → IC=+0.234 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0092 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1688` → IC=+0.226 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1688 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.0807` → IC=+0.228 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0807 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4079` → IC=+0.262 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4079 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.245 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1237` → IC=+0.223 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1237 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `1.1974` → IC=+0.221 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1974 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.8558` → IC=+0.260 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8558 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.251 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7632` → IC=-0.188 (n=1490)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7632
  - _Potencial_: sin este filtro IC_bueno=+0.285 (n=1494)

- **FILTRO** `ibs_20min` > `0.6667` → IC=-0.244 (n=741)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2259)

- **FILTRO** `sigma_ewma_delta_pct` > `8.658` → IC=-0.233 (n=346)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.658
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=2654)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.285 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `1.0126` → IC=+0.334 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0126 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.707` → IC=+0.165 (n=469)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.707 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8573` → IC=+0.313 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8573 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.6344` → IC=+0.305 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6344 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.1016` → IC=+0.302 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1016 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2759` → IC=+0.329 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2759 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.7989` → IC=+0.317 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7989 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `2.4149` → IC=+0.299 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4149 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.328 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.5625` → IC=+0.133 (n=1983)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5625 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.267` → IC=+0.238 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.267 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.263 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.231 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.2599` → IC=+0.261 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2599 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.248 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.262 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.023)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.333 (n=1491)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.307 (n=786)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.289)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.322 (n=1668)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2128` → IC=+0.320 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2128 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.77` → IC=+0.312 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.77 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.947` → IC=+0.290 (n=1886)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.947 (IC base=+0.289)

- **PATRÓN** `volumen_regimen` > `0.8578` → IC=+0.314 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8578 (IC base=+0.289)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.337 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` > `1.4345` → IC=+0.302 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4345 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `2658.4002` → IC=+0.306 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2658.4002 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.326 (n=1391)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.320 (n=1187)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.1867` → IC=+0.288 (n=783)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1867 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.293 (n=1689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.3675` → IC=+0.314 (n=1778)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3675 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.3068` → IC=+0.294 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3068 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.477` → IC=+0.302 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.477 (IC base=+0.288)

- **PATRÓN** `volumen_regimen` > `1.2282` → IC=+0.319 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2282 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.335 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.297 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `2.139` → IC=+0.289 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.139 (IC base=+0.288)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.189 (n=3457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0047 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.210 (n=3451)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3505` → IC=+0.186 (n=9103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3505 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=10811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.566` → IC=+0.228 (n=10346)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.566 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.1709` → IC=+0.200 (n=4428)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1709 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.468` → IC=+0.250 (n=2081)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.468 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.167 (n=6880)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2044 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` > `0.629` → IC=+0.163 (n=6879)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.629 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2951` → IC=+0.198 (n=1533)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2951 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.4521` → IC=+0.174 (n=3328)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4521 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.6084` → IC=+0.183 (n=3327)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6084 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `2004.561` → IC=+0.179 (n=9241)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2004.561 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.190 (n=9266)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 104.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.190 (n=6632)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0065 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.0805` → IC=+0.222 (n=3312)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0805 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=3741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.4839` → IC=+0.234 (n=9931)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4839 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.309` → IC=+0.202 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.309 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1803` → IC=+0.165 (n=7111)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1803 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.222 (n=1449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6119` → IC=+0.178 (n=3074)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.6119 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.187 (n=8898)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 107.0 (IC base=+0.177)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.232 (n=580)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.206 (n=580)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3381` → IC=+0.219 (n=1735)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3381 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=1839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.204 (n=1161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.916` → IC=+0.284 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.916 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.324` → IC=+0.329 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.324 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.256 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.2347` → IC=+0.205 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2347 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1804)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.249 (n=1176)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.243)

- **PATRÓN** `sigma_h` > `0.0041` → IC=+0.249 (n=1332)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0041 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.0702` → IC=+0.302 (n=447)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0702 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=1192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=669)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.251` → IC=+0.266 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.251 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.25` → IC=+0.250 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.25 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.241 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.277 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.254 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=1472)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1990.1048` → IC=+0.257 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1990.1048 (IC base=+0.243)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.218 (n=687)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.1651` → IC=+0.186 (n=1039)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1651 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=1562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.3877` → IC=+0.224 (n=1558)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3877 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.1993` → IC=+0.213 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1993 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.230 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `0.6895` → IC=+0.169 (n=686)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6895 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `1.0745` → IC=+0.160 (n=707)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.0745 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.200 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.4154` → IC=+0.184 (n=507)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4154 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `2.4825` → IC=+0.160 (n=507)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4825 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `11950.6339` → IC=+0.161 (n=1392)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11950.6339 (IC base=+0.160)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.175 (n=653)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 234.0 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1642)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.2309` → IC=+0.174 (n=1445)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2309 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.5918` → IC=+0.199 (n=1642)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5918 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1372` → IC=+0.171 (n=1640)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1372 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.883` → IC=+0.206 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.883 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.2077` → IC=+0.162 (n=1642)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2077 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.2297` → IC=+0.145 (n=1693)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.2297 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1603` → IC=+0.149 (n=502)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1603 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.4908` → IC=+0.153 (n=1528)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4908 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7701` → IC=+0.144 (n=1019)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7701 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.170 (n=489)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 208.0 (IC base=+0.143)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.222 (n=1157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.2464` → IC=+0.223 (n=1155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2464 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=1807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.554` → IC=+0.277 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.554 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` < `0.0963` → IC=+0.205 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0963 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.1273` → IC=+0.210 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1273 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.208 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.7073` → IC=+0.215 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7073 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=2060)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `1964.6432` → IC=+0.224 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1964.6432 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.246 (n=1311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1443` → IC=+0.264 (n=655)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1443 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.280 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.3456` → IC=+0.252 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3456 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.676` → IC=+0.264 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.676 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.266 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.7192` → IC=+0.246 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7192 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.7161` → IC=+0.236 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7161 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `2040.8584` → IC=+0.245 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2040.8584 (IC base=+0.229)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.225 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.229)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.201 (n=731)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.201 (n=554)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1734)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.3311` → IC=+0.205 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3311 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.139` → IC=+0.188 (n=1068)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.139 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.202 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.158 (n=1108)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.856 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1012` → IC=+0.172 (n=693)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1012 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4335` → IC=+0.168 (n=543)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4335 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5288` → IC=+0.158 (n=542)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5288 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5061.8528` → IC=+0.195 (n=1107)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 5061.8528 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.152 (n=1597)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 150.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.162 (n=1538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.006 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.3811` → IC=+0.151 (n=1747)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3811 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.669` → IC=+0.188 (n=1747)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.669 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.878` → IC=+0.165 (n=604)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.878 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.162 (n=1165)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8554 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2971` → IC=+0.191 (n=267)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2971 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.8146` → IC=+0.141 (n=1080)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8146 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.133 (n=1620)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.42 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4439.3642` → IC=+0.168 (n=1165)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4439.3642 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.134 (n=1043)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 97.0 (IC base=+0.131)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.159 (n=860)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0098 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4421` → IC=+0.130 (n=1664)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4421 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=1938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.215 (n=1898)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `1.0247` → IC=+0.216 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0247 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.92` → IC=+0.263 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.92 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.2007` → IC=+0.140 (n=1891)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2007 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.129 (n=1891)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6411 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.1645` → IC=+0.137 (n=1909)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.1645 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.549` → IC=+0.141 (n=805)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.549 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4864` → IC=+0.132 (n=610)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4864 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=1982)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2388.5554` → IC=+0.186 (n=1261)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2388.5554 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.151 (n=1508)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 46.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.158 (n=841)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.006 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.1034` → IC=+0.180 (n=635)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.1034 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=1924)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.220 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.196` → IC=+0.150 (n=1755)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.196 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.38` → IC=+0.135 (n=578)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 5.38 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1785` → IC=+0.135 (n=1905)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1785 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.160 (n=239)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.4527` → IC=+0.138 (n=584)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4527 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2780.1246` → IC=+0.185 (n=864)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2780.1246 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.132 (n=1712)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 52.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.234 (n=1581)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.2839` → IC=+0.219 (n=1180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2839 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=1843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.215 (n=1195)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.6494` → IC=+0.247 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6494 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.1969` → IC=+0.215 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1969 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.2855` → IC=+0.210 (n=1269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2855 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.594` → IC=+0.244 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.594 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `1.1852` → IC=+0.216 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1852 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `0.6232` → IC=+0.219 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6232 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.271 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `2.4722` → IC=+0.215 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4722 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4264` → IC=+0.218 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4264 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2645.2402` → IC=+0.218 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2645.2402 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.228 (n=800)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.219)

- **PATRÓN** `sigma_h` > `0.0223` → IC=+0.226 (n=825)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0223 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.0901` → IC=+0.241 (n=607)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0901 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=887)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.0196` → IC=+0.289 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0196 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `1.1533` → IC=+0.236 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1533 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.365` → IC=+0.256 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.365 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6367` → IC=+0.231 (n=1818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6367 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.275 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `2.1933` → IC=+0.213 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1933 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `1.4384` → IC=+0.219 (n=1671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4384 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `2623.1942` → IC=+0.227 (n=1212)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2623.1942 (IC base=+0.219)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.195 (n=907)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0036 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.168 (n=908)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0083 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3328` → IC=+0.178 (n=2394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3328 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=1337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.3333` → IC=+0.196 (n=2722)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3333 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.7694` → IC=+0.183 (n=430)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.7694 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.759` → IC=+0.193 (n=1172)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.759 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.8703` → IC=+0.187 (n=1629)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8703 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.2045` → IC=+0.176 (n=814)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.2045 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1633` → IC=+0.177 (n=722)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1633 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.182 (n=881)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.5274` → IC=+0.172 (n=881)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5274 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=3119)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2779.754` → IC=+0.169 (n=2431)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2779.754 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.186 (n=2500)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 148.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.159 (n=933)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0036 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=2640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.0726` → IC=+0.197 (n=933)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.0726 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.2039` → IC=+0.121 (n=2529)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2039 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.6982` → IC=+0.127 (n=1118)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.6982 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.0752` → IC=+0.128 (n=1067)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.0752 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.4389` → IC=+0.146 (n=906)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4389 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2828.5762` → IC=+0.132 (n=2499)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2828.5762 (IC base=+0.112)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.128 (n=883)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 20.0 (IC base=+0.112)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.204 (n=343)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1007` → IC=+0.201 (n=342)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1007 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.182 (n=713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.6334` → IC=+0.204 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6334 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.3035` → IC=+0.168 (n=251)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.3035 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.137` → IC=+0.170 (n=331)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 3.137 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8817` → IC=+0.177 (n=518)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8817 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.0925` → IC=+0.150 (n=747)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0925 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.153 (n=306)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.22` → IC=+0.160 (n=668)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.22 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.4165` → IC=+0.152 (n=759)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4165 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `14653.7158` → IC=+0.156 (n=518)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 14653.7158 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.201 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.199 (n=304)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2682` → IC=+0.163 (n=801)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2682 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.152 (n=816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.149 (n=927)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6098` → IC=+0.182 (n=801)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.6098 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.551` → IC=+0.149 (n=962)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.551 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2138` → IC=+0.147 (n=910)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2138 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6954` → IC=+0.156 (n=813)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6954 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1607` → IC=+0.203 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1607 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.1178` → IC=+0.160 (n=793)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1178 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.406` → IC=+0.152 (n=900)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.406 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=1178)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `12101.0434` → IC=+0.145 (n=813)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 12101.0434 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.159 (n=773)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 288.0 (IC base=+0.145)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.233 (n=578)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.2048` → IC=+0.212 (n=575)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2048 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.6714` → IC=+0.250 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6714 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.3563` → IC=+0.206 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3563 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.207` → IC=+0.202 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.207 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.057` → IC=+0.223 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.057 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8407` → IC=+0.202 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8407 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `1.1833` → IC=+0.223 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1833 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.16` → IC=+0.233 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.16 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.227 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4231 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.4608` → IC=+0.224 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4608 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.154 (n=365)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0038 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.131 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 11.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.0873` → IC=+0.162 (n=276)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.0873 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.451` → IC=+0.157 (n=214)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.451 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.6877` → IC=+0.153 (n=364)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6877 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.140 (n=134)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.147 (n=267)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `4108.2759` → IC=+0.135 (n=737)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 4108.2759 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.475` → IC=-0.126 (n=268)

  - _Acción_: SKIP cuando `ibs_20min` > 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=523)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.172 (n=614)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0051 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.5423` → IC=+0.162 (n=613)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.5423 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.192 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.277 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.947` → IC=+0.233 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.947 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.329` → IC=+0.218 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.329 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.0674` → IC=+0.176 (n=539)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0674 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `0.6528` → IC=+0.166 (n=612)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6528 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.17` → IC=+0.172 (n=172)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.17 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `2.4855` → IC=+0.159 (n=591)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4855 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.1991` → IC=+0.174 (n=268)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.1991 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.164 (n=649)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `3078.7088` → IC=+0.194 (n=204)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3078.7088 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.475` → IC=+0.148 (n=523)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.475 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.5709` → IC=+0.126 (n=249)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5709 (IC base=+0.055)

- **PATRÓN** `libro_liquidez` > `2865.6878` → IC=+0.153 (n=269)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2865.6878 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.143 (n=242)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 15.0 (IC base=+0.055)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.170 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0238 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.200 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.167 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.5556` → IC=+0.184 (n=172)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5556 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.2393` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2393 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `1.115` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 1.115 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.385` → IC=+0.181 (n=164)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.385 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6949 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.1233` → IC=+0.175 (n=155)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.1233 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2503.8283` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2503.8283 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.160 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0119 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.131 (n=212)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.025` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.025 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.126 (n=212)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6515 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2293` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2293 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.8124` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.8124 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 17.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.180 (n=4487)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.212 (n=4482)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=14068)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.9896` → IC=+0.308 (n=4478)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9896 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1642` → IC=+0.187 (n=5033)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1642 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.395` → IC=+0.246 (n=3282)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.395 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.2326` → IC=+0.165 (n=9007)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2326 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.199 (n=1819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.601` → IC=+0.196 (n=4335)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.601 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2441.2681` → IC=+0.180 (n=8956)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2441.2681 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.203 (n=10639)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.195 (n=5343)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0052 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.1463` → IC=+0.196 (n=5337)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1463 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=4536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.4512` → IC=+0.250 (n=10672)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4512 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.1739` → IC=+0.168 (n=7203)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1739 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.114` → IC=+0.213 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.114 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.163 (n=3613)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7049 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2897` → IC=+0.252 (n=1627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2897 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.2668` → IC=+0.195 (n=5145)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.2668 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.209 (n=7369)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.252 (n=744)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.226 (n=742)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=1071)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=1500)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.769` → IC=+0.346 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.769 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.269 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.5899` → IC=+0.224 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5899 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=2284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2002.24` → IC=+0.213 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2002.24 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.265 (n=1233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.262 (n=1845)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.2046` → IC=+0.275 (n=1229)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2046 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.3587` → IC=+0.285 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3587 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.502` → IC=+0.266 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.502 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2846` → IC=+0.286 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2846 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `2.6294` → IC=+0.282 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6294 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=2029)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1994.92` → IC=+0.271 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1994.92 (IC base=+0.260)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.205 (n=723)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1782` → IC=+0.166 (n=1440)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1782 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2805` → IC=+0.206 (n=2159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2805 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1298` → IC=+0.188 (n=1193)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1298 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.708` → IC=+0.174 (n=360)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.708 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.221` → IC=+0.153 (n=1977)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.221 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6273` → IC=+0.173 (n=720)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6273 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.192 (n=310)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1426` → IC=+0.159 (n=1849)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1426 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5244` → IC=+0.155 (n=1878)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5244 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `275.0` → IC=+0.182 (n=897)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 275.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1794)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.2566` → IC=+0.162 (n=1579)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2566 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.684` → IC=+0.194 (n=1794)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.684 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.165 (n=1649)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.56` → IC=+0.167 (n=304)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.56 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.1888` → IC=+0.157 (n=1794)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1888 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1548` → IC=+0.200 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1548 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.434` → IC=+0.152 (n=1693)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.434 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.161 (n=1128)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `348.0` → IC=+0.143 (n=1068)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 348.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.233 (n=2202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.226 (n=2228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.306 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.2042` → IC=+0.226 (n=2225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2042 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.6122` → IC=+0.227 (n=2122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6122 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2624)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1977.8984` → IC=+0.235 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1977.8984 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.246 (n=1826)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.1813` → IC=+0.252 (n=913)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1813 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.260 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.239 (n=746)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0141` → IC=+0.303 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0141 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.997` → IC=+0.286 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.997 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.3416` → IC=+0.297 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3416 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.705` → IC=+0.243 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.705 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.128` → IC=+0.242 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.128 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2039.4384` → IC=+0.251 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2039.4384 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.256 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.236)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=1016)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3325` → IC=+0.152 (n=2023)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3325 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2686` → IC=+0.190 (n=2298)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2686 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.5416` → IC=+0.165 (n=612)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.5416 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.17` → IC=+0.151 (n=934)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.17 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8732` → IC=+0.161 (n=1533)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8732 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.166` → IC=+0.173 (n=603)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.166 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5241` → IC=+0.163 (n=985)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5241 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1819` → IC=+0.151 (n=1014)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1819 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7316.6924` → IC=+0.234 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7316.6924 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.181 (n=728)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 70.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.192 (n=624)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0033 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.3452` → IC=+0.144 (n=1635)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3452 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=677)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.138 (n=649)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 5.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7339` → IC=+0.187 (n=1858)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7339 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.343` → IC=+0.178 (n=380)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.343 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8747` → IC=+0.142 (n=1240)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8747 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2976` → IC=+0.235 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2976 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.145 (n=1782)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `5530.0694` → IC=+0.196 (n=843)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 5530.0694 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.136 (n=1784)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 166.0 (IC base=+0.133)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.136 (n=2315)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0055 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.4524` → IC=+0.200 (n=2314)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4524 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `1.0123` → IC=+0.211 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0123 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.54` → IC=+0.241 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.54 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8904` → IC=+0.149 (n=1543)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8904 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1625` → IC=+0.129 (n=2383)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1625 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.1976` → IC=+0.139 (n=1021)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.1976 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=2363)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2913.9614` → IC=+0.250 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2913.9614 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.147 (n=718)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 27.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.157 (n=1474)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0077 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1302` → IC=+0.168 (n=736)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1302 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6296` → IC=+0.214 (n=2207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6296 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.2143` → IC=+0.140 (n=1833)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2143 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.474` → IC=+0.134 (n=2128)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.474 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.713` → IC=+0.159 (n=971)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.713 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2237` → IC=+0.184 (n=359)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2237 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.4341` → IC=+0.154 (n=680)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4341 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2811.5163` → IC=+0.202 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2811.5163 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.142 (n=1789)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 50.0 (IC base=+0.124)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.234 (n=2237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=2342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.224 (n=1619)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.266 (n=2002)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.207` → IC=+0.235 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.207 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.623` → IC=+0.258 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.623 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `1.2346` → IC=+0.223 (n=2237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2346 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.223 (n=2237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2366` → IC=+0.245 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2366 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.5125` → IC=+0.246 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5125 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=2073)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `2654.5546` → IC=+0.229 (n=1491)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2654.5546 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.220 (n=787)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.233 (n=1067)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.233 (n=1666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.4151` → IC=+0.266 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4151 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.2938` → IC=+0.222 (n=2205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2938 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.876` → IC=+0.259 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.876 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.248 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.285 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.4345` → IC=+0.219 (n=2160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4345 (IC base=+0.218)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.172 (n=4013)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.230 (n=1357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.3901` → IC=+0.201 (n=3568)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3901 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=1494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.194 (n=1834)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `0.9404` → IC=+0.241 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9404 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.1706` → IC=+0.198 (n=1506)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1706 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.223` → IC=+0.217 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.223 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.199 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` > `1.2573` → IC=+0.199 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2573 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.1688` → IC=+0.219 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1688 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `1.4563` → IC=+0.197 (n=1332)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4563 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `1.866` → IC=+0.196 (n=2663)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.866 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=3037)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `3842.2142` → IC=+0.202 (n=2703)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3842.2142 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.221 (n=1008)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.4845` → IC=+0.187 (n=3022)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.4845 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=1039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.190 (n=1375)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.1758` → IC=+0.193 (n=1330)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1758 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.6424` → IC=+0.181 (n=540)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6424 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.181` → IC=+0.177 (n=3015)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.181 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.2537` → IC=+0.176 (n=2857)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.2537 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.174 (n=2758)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.177 (n=1373)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.5479` → IC=+0.173 (n=2980)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.5479 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `1.8256` → IC=+0.181 (n=1987)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8256 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=4013)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.185 (n=1970)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 74.0 (IC base=+0.171)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.237 (n=352)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.258 (n=176)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.234 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.7622` → IC=+0.214 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7622 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.1783` → IC=+0.213 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1783 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.039` → IC=+0.231 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.039 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.529` → IC=+0.213 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.529 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.220 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2212 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.596` → IC=+0.220 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.596 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.4501` → IC=+0.230 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4501 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `12505.1299` → IC=+0.233 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12505.1299 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.228 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1116` → IC=+0.178 (n=467)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1116 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.198 (n=355)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 4.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.1485` → IC=+0.180 (n=467)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1485 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.152 (n=481)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6078 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6649` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6649 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.391` → IC=+0.165 (n=1044)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.391 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8847` → IC=+0.186 (n=708)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8847 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2218` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2218 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.5397` → IC=+0.153 (n=1057)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5397 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.8221` → IC=+0.169 (n=705)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8221 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `13473.7476` → IC=+0.164 (n=707)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 13473.7476 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `700.0` → IC=+0.160 (n=1015)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 700.0 (IC base=+0.148)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.200 (n=231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.186 (n=313)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0098 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.581` → IC=+0.179 (n=689)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.581 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.494` → IC=+0.222 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.494 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2079` → IC=+0.222 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2079 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.6744` → IC=+0.172 (n=230)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.6744 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `3.3613` → IC=+0.184 (n=229)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 3.3613 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.241 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.295 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.1988` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1988 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `2.3165` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3165 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.237)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.222 (n=412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.4577` → IC=+0.208 (n=1228)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4577 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.201 (n=1268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.200 (n=1085)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.519` → IC=+0.215 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.519 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.881` → IC=+0.204 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.881 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.134` → IC=+0.206 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.134 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `1.0845` → IC=+0.201 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0845 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `1.2457` → IC=+0.204 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2457 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.1054` → IC=+0.199 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1054 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.164` → IC=+0.208 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.164 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.424` → IC=+0.217 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.424 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.236 (n=327)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.194 (n=980)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.183 (n=383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 16.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.182 (n=664)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 10.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.748` → IC=+0.176 (n=980)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.748 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.0817` → IC=+0.171 (n=980)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.0817 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.6238` → IC=+0.194 (n=194)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6238 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.748` → IC=+0.174 (n=1003)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 6.748 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.2516` → IC=+0.182 (n=980)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.2516 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.191 (n=412)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `2.1885` → IC=+0.183 (n=844)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.1885 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `7437.397` → IC=+0.184 (n=980)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 7437.397 (IC base=+0.169)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.222 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.3034` → IC=+0.185 (n=350)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3034 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.207 (n=490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.9259` → IC=+0.242 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9259 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1947` → IC=+0.209 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1947 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.541` → IC=+0.223 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.541 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `0.694` → IC=+0.204 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.694 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` > `1.2699` → IC=+0.184 (n=175)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.2699 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.1658` → IC=+0.224 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1658 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `1.4694` → IC=+0.193 (n=510)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4694 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.185 (n=633)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `3418.9396` → IC=+0.224 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3418.9396 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.197 (n=454)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 48.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.211 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.209 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3725` → IC=+0.238 (n=265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3725 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.216 (n=269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.1849` → IC=+0.240 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1849 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.772` → IC=+0.230 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.772 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.053` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.053 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.99` → IC=+0.194 (n=344)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 2.99 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.9487` → IC=+0.193 (n=265)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.9487 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` > `0.6848` → IC=+0.189 (n=397)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.6848 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.225 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `1.8988` → IC=+0.191 (n=257)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.8988 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.2105` → IC=+0.206 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2105 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `3870.9486` → IC=+0.200 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3870.9486 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.225 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.187)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.152 (n=581)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0038 (IC base=+0.077)

- **PATRÓN** `ibs_20min` > `0.4419` → IC=+0.152 (n=1221)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.4419 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.1412` → IC=+0.140 (n=665)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1412 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.465` → IC=+0.181 (n=280)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.465 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.184 (n=169)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.077)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.122 (n=400)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0044 (IC base=+0.063)

- **PATRÓN** `ibs_20min` < `0.1905` → IC=+0.263 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1905 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` < `0.0843` → IC=+0.148 (n=510)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.0843 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.146` → IC=+0.141 (n=447)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.146 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` < `0.9649` → IC=+0.123 (n=459)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.9649 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` > `0.1466` → IC=+0.200 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1466 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` < `2.5724` → IC=+0.151 (n=460)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.5724 (IC base=+0.063)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.138 (n=446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0057 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.4165` → IC=+0.174 (n=415)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.4165 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1286` → IC=+0.161 (n=219)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1286 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.549` → IC=+0.125 (n=246)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 3.549 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `2.4916` → IC=+0.124 (n=373)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4916 (IC base=+0.096)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.120 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0045 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.0582` → IC=+0.296 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0582 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` < `0.201` → IC=+0.137 (n=279)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.201 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.155` → IC=+0.150 (n=244)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 7.155 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` < `1.0039` → IC=+0.128 (n=221)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0039 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.1526` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.1526 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` < `2.5035` → IC=+0.148 (n=228)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.5035 (IC base=+0.084)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.146 (n=289)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0046 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.6872` → IC=+0.201 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6872 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1226` → IC=+0.171 (n=220)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1226 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.447` → IC=+0.274 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.447 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2829` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2829 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `1173.2149` → IC=+0.139 (n=355)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1173.2149 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.7041` → IC=+0.167 (n=142)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.7041 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1753` → IC=+0.129 (n=157)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1753 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.906` → IC=+0.122 (n=125)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.906 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.0706` → IC=+0.131 (n=120)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.0706 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1376` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1376 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.7076` → IC=+0.159 (n=83)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.7076 (IC base=+0.025)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=130)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.025)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0101` → IC=-0.227 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0101
  - _Potencial_: sin este filtro IC_bueno=+0.163 (n=161)

- **FILTRO** `ibs_20min` > `0.1786` → IC=-0.278 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1786
  - _Potencial_: sin este filtro IC_bueno=+0.265 (n=130)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.176 (n=270)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.7647 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `0.7076` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.7076 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2436` → IC=+0.183 (n=80)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2436 (IC base=+0.044)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.194 (n=109)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0061 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.1786` → IC=+0.265 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1786 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.1905` → IC=+0.159 (n=130)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1905 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.949` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.949 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.6377` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6377 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` > `0.9765` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.9765 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.0818` → IC=+0.315 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0818 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `2.1906` → IC=+0.194 (n=96)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.1906 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` > `1.4883` → IC=+0.197 (n=97)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4883 (IC base=+0.065)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.211 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `754.8738` → IC=+0.179 (n=76)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 754.8738 (IC base=+0.065)

### GBM_LATE_60M_FADE
- **FILTRO** `dist_vwap_pct` > `0.2351` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2351
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=243)

- **FILTRO** `volumen_regimen` < `0.7435` → IC=-0.348 (n=64)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7435
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=195)

- **FILTRO** `volumen_spike_ratio` > `2.6594` → IC=-0.188 (n=62)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.6594
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=123)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.206 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=210)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.379 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=169)

- **FILTRO** `dist_vwap_pct` > `0.3287` → IC=-0.389 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3287
  - _Potencial_: sin este filtro IC_bueno=-0.251 (n=191)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=195)

- **FILTRO** `volumen_pendiente_norm` > `0.0549` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0549
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=114)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.250 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=43)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=64)

- **FILTRO** `volumen_spike_ratio` > `3.7991` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.7991
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=47)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.308 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=72)

- **FILTRO** `sigma_ewma_delta_pct` > `2.482` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.482
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=64)

- **FILTRO** `volumen_regimen` > `0.8359` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8359
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=73)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0026` → IC=-0.370 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=65)

- **FILTRO** `ibs_20min` < `0.6002` → IC=-0.467 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6002
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=58)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.354 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=45)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `ibs_20min` > `0.9508` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.9508 (IC base=-0.159)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=72)

- **FILTRO** `volumen_spike_ratio` < `1.5474` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5474
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=48)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=62)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.176 (n=183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0056 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.129 (n=195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 15.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.6616` → IC=+0.139 (n=402)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.6616 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.4722` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.4722 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` < `1.5351` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5351 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.1558` → IC=+0.174 (n=384)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1558 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.099` → IC=+0.212 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.099 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `2.627` → IC=+0.123 (n=359)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.627 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=378)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `1295.3706` → IC=+0.123 (n=436)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1295.3706 (IC base=+0.085)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6466` → IC=-0.262 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6466
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=123)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.197 (n=176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0024 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.1414` → IC=+0.214 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1414 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.879` → IC=+0.183 (n=159)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 4.879 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `0.627` → IC=+0.178 (n=197)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.627 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.1895` → IC=+0.188 (n=168)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1895 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.8898` → IC=+0.164 (n=111)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.8898 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.177 (n=165)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.155)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1606` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1606
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=110)

- **FILTRO** `libro_liquidez` < `1529.3843` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `libro_liquidez` < 1529.3843
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=131)

- **PATRÓN** `volumen_spike_ratio` < `1.8267` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.8267 (IC base=+0.051)

- **PATRÓN** `libro_liquidez` > `1529.3843` → IC=+0.124 (n=131)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1529.3843 (IC base=+0.051)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.139 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 12.0 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.1832` → IC=+0.157 (n=138)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1832 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.629` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.629 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.8247` → IC=+0.136 (n=105)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8247 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.218` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.218 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `1970.1487` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1970.1487 (IC base=+0.076)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `dist_vwap_pct` > `0.2724` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2724
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=89)

- **FILTRO** `volumen_spike_ratio` > `2.1493` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.1493
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=49)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.275 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.257 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.234 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.9298` → IC=+0.245 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9298 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` > `0.6353` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6353 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` < `0.1348` → IC=+0.234 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1348 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.349` → IC=+0.286 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.349 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.284 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` < `0.2516` → IC=+0.283 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2516 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.1536` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1536 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.231 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.231)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4522` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4522 (IC base=+0.288)

- **PATRÓN** `elapsed_s` > `189.2` → IC=+0.360 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 189.2 (IC base=+0.288)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.8028` → IC=+0.367 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8028 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.288)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.202)

- **PATRÓN** `elapsed_s` < `209.7` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 209.7 (IC base=+0.202)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.271 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.202)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `1814.0` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1814.0 (IC base=+0.202)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4522` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4522 (IC base=+0.288)

- **PATRÓN** `elapsed_s` > `189.2` → IC=+0.360 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 189.2 (IC base=+0.288)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.8028` → IC=+0.367 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8028 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.288)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.202)

- **PATRÓN** `elapsed_s` < `209.7` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 209.7 (IC base=+0.202)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.271 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.202)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `1814.0` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1814.0 (IC base=+0.202)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=1004)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2859.3431` → IC=+0.133 (n=469)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2859.3431 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.101)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=1004)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2859.3431` → IC=+0.133 (n=469)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2859.3431 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.101)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=151)

- **FILTRO** `libro_liquidez` < `10452.0502` → IC=-0.179 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 10452.0502
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=57)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=244)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=230)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=50)

- **FILTRO** `hora_utc` < `3.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=54)

- **FILTRO** `libro_liquidez` < `10893.2451` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 10893.2451
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=53)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=105)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2772)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=98)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=55)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=87)

- **FILTRO** `ballena_activa_n` > `98.0` → IC=-0.208 (n=63)

  - _Acción_: SKIP cuando `ballena_activa_n` > 98.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=22)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=107)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.124 (n=107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 15.0 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `2582.9138` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2582.9138 (IC base=+0.054)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=20)

- **FILTRO** `libro_liquidez` < `15247.5472` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 15247.5472
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.129 (n=176)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.495 (IC base=+0.040)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1044)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=998)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9855` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9855
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `142.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 142.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=630)

- **FILTRO** `liq_n` < `11.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `liq_n` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `liq_usd_total` < `13082.51` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `liq_usd_total` < 13082.51
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=354)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=335)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.151 (n=124)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.495 (IC base=+0.019)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=775)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=775)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=609)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=568)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=568)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=215)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=215)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=177)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=142)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=142)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=166)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=160)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=303)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=303)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=205)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.128 (n=1312)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1374)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.146 (n=600)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.47 (IC base=+0.024)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` > `0.45` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `restante_min` < `3.89` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `lag_apertura_s` > `66.61` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.61
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.137 (n=169)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=92)

- **FILTRO** `profundidad_ratio` < `462.7` → IC=-0.121 (n=130)

  - _Acción_: SKIP cuando `profundidad_ratio` < 462.7
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=131)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.223 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.048)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `restante_min` < `8.84` → IC=-0.189 (n=43)

  - _Acción_: SKIP cuando `restante_min` < 8.84
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=130)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=134)

- **FILTRO** `lag_apertura_s` > `369.74` → IC=-0.189 (n=43)

  - _Acción_: SKIP cuando `lag_apertura_s` > 369.74
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=130)

- **FILTRO** `profundidad_ratio` < `33.3` → IC=-0.121 (n=114)

  - _Acción_: SKIP cuando `profundidad_ratio` < 33.3
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=59)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.175 (n=81)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=100)

- **FILTRO** `restante_min` < `3.99` → IC=-0.131 (n=128)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=53)

- **FILTRO** `lag_apertura_s` > `60.69` → IC=-0.128 (n=135)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.69
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=46)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `restante_min` < `13.49` → IC=-0.124 (n=176)

  - _Acción_: SKIP cuando `restante_min` < 13.49
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=64)

- **FILTRO** `lag_apertura_s` > `90.84` → IC=-0.124 (n=179)

  - _Acción_: SKIP cuando `lag_apertura_s` > 90.84
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=61)

- **FILTRO** `profundidad_ratio` < `37.2` → IC=-0.210 (n=60)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.2
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=180)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.229 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=185)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.133 (n=77)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.5 (IC base=-0.011)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.123 (n=197)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=110)

- **FILTRO** `restante_min` < `3.34` → IC=-0.186 (n=100)

  - _Acción_: SKIP cuando `restante_min` < 3.34
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=207)

- **FILTRO** `lag_apertura_s` > `97.61` → IC=-0.198 (n=104)

  - _Acción_: SKIP cuando `lag_apertura_s` > 97.61
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=203)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.45 (IC base=+0.035)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.130 (n=52)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=181)

- **PATRÓN** `lag_apertura_s` < `92.51` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `lag_apertura_s` < 92.51 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.133 (n=88)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.5 (IC base=+0.010)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.124 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=74)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` > 0.55 (IC base=-0.049)

- **PATRÓN** `profundidad_ratio` > `15.0` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `profundidad_ratio` > 15.0 (IC base=+0.033)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.201 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=268)

- **FILTRO** `restante_min` < `3.28` → IC=-0.136 (n=116)

  - _Acción_: SKIP cuando `restante_min` < 3.28
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=237)

- **FILTRO** `lag_apertura_s` > `101.39` → IC=-0.139 (n=120)

  - _Acción_: SKIP cuando `lag_apertura_s` > 101.39
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=233)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7798)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.165 (n=4813)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14463)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.166 (n=4953)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=15016)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.195 (n=857)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2571)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.149 (n=838)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2743)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.121 (n=1657)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.176 (n=692)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2188)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.177 (n=866)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=2608)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.183 (n=900)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=2726)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.165 (n=827)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=2605)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2527)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3267)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `libro_liquidez` < `16920.0467` → IC=-0.163 (n=176)

  - _Acción_: SKIP cuando `libro_liquidez` < 16920.0467
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=359)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=302)

- **FILTRO** `libro_liquidez` < `2870.8573` → IC=-0.187 (n=97)

  - _Acción_: SKIP cuando `libro_liquidez` < 2870.8573
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=291)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `2005.4917` → IC=-0.163 (n=336)

  - _Acción_: SKIP cuando `libro_liquidez` < 2005.4917
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=683)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=232)

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
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.037)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=13420)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=29892)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=10195)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=33117)

- **FILTRO** `ibs_7min` < `0.2577` → IC=-0.233 (n=10828)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2577
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=32484)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=14555)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=28757)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.235 (n=13281)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=41820)

- **FILTRO** `ibs_7min` > `0.2865` → IC=-0.177 (n=13774)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2865
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=41327)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.144 (n=2176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=5192)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.236 (n=3640)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=3728)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.251 (n=2431)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=4937)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.188 (n=1571)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5797)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.268 (n=2328)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=7234)

- **FILTRO** `ibs_7min` > `0.7794` → IC=-0.211 (n=2390)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7794
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=7172)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=1759)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=5640)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.247 (n=1820)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=5579)

- **FILTRO** `ibs_7min` < `0.7404` → IC=-0.196 (n=1849)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7404
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5550)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.181 (n=1841)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=5558)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=1791)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=5744)

- **FILTRO** `ibs_7min` > `0.2655` → IC=-0.191 (n=1881)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2655
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5654)

- **FILTRO** `ballena_activa_n` > `148.0` → IC=-0.190 (n=1879)

  - _Acción_: SKIP cuando `ballena_activa_n` > 148.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5656)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.162 (n=1993)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=5026)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.319 (n=1660)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5359)

- **FILTRO** `ibs_7min` < `0.7032` → IC=-0.246 (n=2316)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7032
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=4703)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.218 (n=1574)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5445)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.243 (n=2300)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=7874)

- **FILTRO** `ibs_7min` > `0.7358` → IC=-0.172 (n=2543)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7358
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=7631)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=2308)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4811)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.239 (n=2111)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5008)

- **FILTRO** `ibs_7min` < `0.7399` → IC=-0.183 (n=1779)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7399
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5340)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.185 (n=1753)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5366)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.268 (n=1809)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=5538)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.180 (n=1836)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=5511)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.183 (n=1776)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5571)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=1712)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=5597)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.233 (n=1808)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5501)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.173 (n=2622)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=7883)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.277 (n=1698)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5400)

- **FILTRO** `ibs_7min` < `0.2432` → IC=-0.220 (n=1774)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2432
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5324)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.200 (n=1733)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5365)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.205 (n=2438)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=7540)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.153 (n=295)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=963)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1243)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.140 (n=48)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=616)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

- **FILTRO** `libro_liquidez` < `7941.0101` → IC=-0.131 (n=348)

  - _Acción_: SKIP cuando `libro_liquidez` < 7941.0101
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=708)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=357)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.143 (n=155)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=304)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=411)

- **FILTRO** `libro_liquidez` < `3305.4837` → IC=-0.153 (n=165)

  - _Acción_: SKIP cuando `libro_liquidez` < 3305.4837
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=498)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.137 (n=945)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.137 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 14.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `442.2457` → IC=+0.153 (n=315)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 442.2457 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3757.1854` → IC=+0.127 (n=429)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 3757.1854 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.142 (n=305)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 14.0 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4376` → IC=+0.158 (n=74)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.4376 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.232 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `2615.3166` → IC=+0.224 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2615.3166 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.190 (n=98)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 11.0 (IC base=+0.144)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 8.0 (IC base=+0.102)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.174 (n=130)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.202 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.118)

- **PATRÓN** `total_vol_5m` < `384.339` → IC=+0.213 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 384.339 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.190 (n=85)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 73.0 (IC base=+0.118)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.184 (n=169)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.229 (n=57)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.152)

- **PATRÓN** `total_vol_5m` < `8082.459` → IC=+0.167 (n=169)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 8082.459 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 28.0 (IC base=+0.152)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.122 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 13.0 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=112)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `3599.4239` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3599.4239 (IC base=+0.098)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.6961` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.6961
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=122)

- **FILTRO** `sigma_h` > `0.0054` → IC=-0.272 (n=266)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=268)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0049` → IC=-0.248 (n=105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0049
  - _Potencial_: sin este filtro IC_bueno=+0.259 (n=52)

- **FILTRO** `T_h` > `87.9981` → IC=-0.378 (n=39)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=118)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.259 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.079)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7678` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `pct_vs_K` |x|≤ 1.7678 (IC base=-0.079)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.128 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `pct_vs_K` |x|> `8.3214` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.3214
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.182 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=33)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0048` → IC=-0.183 (n=121)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=364)

- **FILTRO** `T_h` > `71.8388` → IC=-0.155 (n=363)

  - _Acción_: SKIP cuando `T_h` > 71.8388
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=122)

- **FILTRO** `sigma_h` > `0.009` → IC=-0.313 (n=105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.009
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=317)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.313 (n=105)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=317)

- **FILTRO** `T_h` > `57.2342` → IC=-0.311 (n=316)

  - _Acción_: SKIP cuando `T_h` > 57.2342
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=106)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `81.2732` → IC=-0.146 (n=111)

  - _Acción_: SKIP cuando `T_h` > 81.2732
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.384 (n=41)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=126)

- **FILTRO** `T_h` > `142.6109` → IC=-0.315 (n=52)

  - _Acción_: SKIP cuando `T_h` > 142.6109
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=103)

- **FILTRO** `pct_vs_K` |x|> `2.7927` → IC=-0.426 (n=52)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7927
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=103)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.235 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=68)

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.261 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=90)

- **FILTRO** `T_h` > `135.986` → IC=-0.265 (n=32)

  - _Acción_: SKIP cuando `T_h` > 135.986
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=102)

- **FILTRO** `pct_vs_K` |x|> `3.3706` → IC=-0.456 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3706
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=85)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` > `0.006` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `pct_vs_K` |x|> `3.7818` → IC=-0.262 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7818
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=80)

- **FILTRO** `sigma_h` > `0.0077` → IC=-0.345 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=29)

- **FILTRO** `T_h` > `41.2311` → IC=-0.377 (n=63)

  - _Acción_: SKIP cuando `T_h` > 41.2311
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=22)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1221` → IC=+0.459 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1221 (IC base=+0.338)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.389 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.338)

- **PATRÓN** `T_h` < `1.0409` → IC=+0.361 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0409 (IC base=+0.338)

- **PATRÓN** `T_h` > `0.4292` → IC=+0.377 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4292 (IC base=+0.338)

- **PATRÓN** `dist_50` > `0.3298` → IC=+0.418 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3298 (IC base=+0.338)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.357 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.338)

- **PATRÓN** `edge` > `0.095` → IC=+0.457 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.095 (IC base=+0.423)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.452 (n=124)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.423)

- **PATRÓN** `T_h` < `1.0173` → IC=+0.429 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0173 (IC base=+0.423)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.469 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.423)

- **PATRÓN** `dist_50` > `0.3938` → IC=+0.479 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3938 (IC base=+0.423)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.477 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.423)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.455 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.426)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.413 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.426)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.458 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.426)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.454 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.426)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.418 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.426)

- **PATRÓN** `dist_50` > `0.4122` → IC=+0.477 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4122 (IC base=+0.426)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.439 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.426)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1975` → IC=+0.480 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1975 (IC base=+0.441)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.460 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0099 (IC base=+0.441)

- **PATRÓN** `T_h` > `0.801` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.801 (IC base=+0.441)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.460 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.441)

- **PATRÓN** `edge` > `0.1135` → IC=+0.473 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1135 (IC base=+0.467)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.484 (n=124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.467)

- **PATRÓN** `T_h` > `0.8072` → IC=+0.468 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8072 (IC base=+0.467)

- **PATRÓN** `dist_50` > `0.4568` → IC=+0.492 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4568 (IC base=+0.467)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.471 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.467)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=253)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=338)

- **PATRÓN** `streak_estiramiento` < `0.4511` → IC=+0.121 (n=85)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.4511 (IC base=+0.018)

- **PATRÓN** `streak_estiramiento` < `0.437` → IC=+0.203 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.437 (IC base=+0.040)

- **PATRÓN** `libro_liquidez` > `2504.4582` → IC=+0.132 (n=123)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2504.4582 (IC base=+0.040)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=25)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4846` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4846
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=57)

- **FILTRO** `ballena_activa_n` > `51.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 51.0
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=60)

- **PATRÓN** `volumen_racha` < `964809.7` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_racha` < 964809.7 (IC base=+0.006)

- **PATRÓN** `streak_estiramiento` < `0.4177` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.4177 (IC base=+0.006)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.140 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 10.0 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.147 (n=100)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 47.0 (IC base=+0.080)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=94)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=100)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=37)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=32)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=25)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=581)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_FADE_60M#SOL#60min
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.038)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=809)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=953)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=959)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3487)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1833)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.196 (n=839)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0043 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.233 (n=838)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.0513` → IC=+0.210 (n=839)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0513 (IC base=+0.195)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2229` → IC=+0.202 (n=838)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2229 (IC base=+0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1309` → IC=+0.216 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1309 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.201 (n=2332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=2609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `ibs_15` > `0.6047` → IC=+0.271 (n=2516)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6047 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.197 (n=1228)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.886` → IC=+0.271 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.886 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `7056.133` → IC=+0.202 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7056.133 (IC base=+0.195)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=1073)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.236 (n=328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.271 (n=164)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.215)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2011` → IC=+0.243 (n=224)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2011 (IC base=+0.215)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1446` → IC=+0.250 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1446 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=495)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_15` > `0.7141` → IC=+0.279 (n=491)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7141 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.1369` → IC=+0.248 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1369 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.772` → IC=+0.290 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.772 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `13449.5003` → IC=+0.233 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13449.5003 (IC base=+0.215)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.513` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.513
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=625)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.170 (n=180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0034 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0671` → IC=+0.153 (n=237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0671 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2358` → IC=+0.159 (n=180)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.2358 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1251` → IC=+0.152 (n=205)

  - _Acción_: Kelly boost +0.76€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1251 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.141 (n=564)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.5731` → IC=+0.233 (n=538)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5731 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.1536` → IC=+0.144 (n=293)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1536 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.2658` → IC=+0.138 (n=504)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2658 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.827` → IC=+0.245 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.827 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `3489.2833` → IC=+0.144 (n=481)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3489.2833 (IC base=+0.136)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `20.733` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.733
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=212)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.165 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0054 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.236 (n=127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1676` → IC=+0.198 (n=336)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1676 (IC base=+0.155)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0614` → IC=+0.163 (n=381)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio_macro` |x|> 0.0614 (IC base=+0.155)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.345` → IC=+0.188 (n=334)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.345 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.169 (n=270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.157 (n=400)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 17.0 (IC base=+0.155)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.229 (n=385)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.138` → IC=+0.156 (n=213)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.138 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.3265` → IC=+0.168 (n=377)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.3265 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.265` → IC=+0.256 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.265 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=241)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `3038.6807` → IC=+0.164 (n=254)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3038.6807 (IC base=+0.155)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.788` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.788 (IC base=+0.021)

- **PATRÓN** `libro_liquidez` > `3333.6591` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3333.6591 (IC base=+0.021)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.258 (n=543)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.0797` → IC=+0.218 (n=268)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0797 (IC base=+0.214)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1081` → IC=+0.222 (n=405)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1081 (IC base=+0.214)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.263 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.230 (n=539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.214)

- **PATRÓN** `ibs_15` > `0.5849` → IC=+0.293 (n=608)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5849 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.1332` → IC=+0.223 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1332 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.749` → IC=+0.248 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.749 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2959.5754` → IC=+0.300 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2959.5754 (IC base=+0.214)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.156 (n=655)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1111 (IC base=+0.069)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.363 (n=355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.358)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.377 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.358)

- **PATRÓN** `drift_60min` |x|≤ `0.1109` → IC=+0.357 (n=355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1109 (IC base=+0.358)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1493` → IC=+0.382 (n=354)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1493 (IC base=+0.358)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1344` → IC=+0.394 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1344 (IC base=+0.358)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.374 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.358)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.393 (n=532)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.388 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.247` → IC=+0.370 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.247 (IC base=+0.358)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.358)

- **PATRÓN** `libro_liquidez` > `3836.614` → IC=+0.370 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3836.614 (IC base=+0.358)

- **PATRÓN** `ballena_activa_n` < `441.0` → IC=+0.376 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 441.0 (IC base=+0.358)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.359 (n=254)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.357)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.367 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.357)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.359 (n=97)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.357)

- **PATRÓN** `drift_15min` |x|≤ `0.5086` → IC=+0.361 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5086 (IC base=+0.357)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1524` → IC=+0.381 (n=192)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1524 (IC base=+0.357)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.394 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.357)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.377 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.357)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.386 (n=288)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.357)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.398 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.575` → IC=+0.363 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.575 (IC base=+0.357)

- **PATRÓN** `libro_liquidez` > `16163.1166` → IC=+0.388 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16163.1166 (IC base=+0.357)

- **PATRÓN** `ballena_activa_n` < `499.0` → IC=+0.406 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 499.0 (IC base=+0.357)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.354 (n=163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.356)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.376 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.356)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.367 (n=163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.356)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.373 (n=218)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.356)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.380 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.356)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.415 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.356)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.402 (n=243)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.356)

- **PATRÓN** `dist_vwap_pct` > `0.4406` → IC=+0.365 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4406 (IC base=+0.356)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.357 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2815 (IC base=+0.356)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.375 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.356)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.355 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.356)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.362 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.356)

- **PATRÓN** `libro_liquidez` > `4286.2041` → IC=+0.380 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4286.2041 (IC base=+0.356)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.361 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 147.0 (IC base=+0.356)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.224 (n=896)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2691)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=1340)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=2247)

- **PATRÓN** `delta_ratio_macro` |x|> `0.14` → IC=+0.180 (n=573)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.14 (IC base=-0.068)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.229 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=-0.068)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.277 (n=860)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.200 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2596` → IC=+0.193 (n=715)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.2596 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.22` → IC=+0.266 (n=942)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.22 (IC base=-0.014)

- **PATRÓN** `ibs_15` < `0.3508` → IC=+0.281 (n=2820)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3508 (IC base=-0.014)

- **PATRÓN** `dist_vwap_pct` > `0.8451` → IC=+0.295 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8451 (IC base=-0.014)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.214 (n=508)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1528)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.228 (n=509)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=1527)

- **FILTRO** `sigma_ewma_delta_pct` > `23.719` → IC=-0.265 (n=292)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.719
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=1744)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.178 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0027 (IC base=+0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2011` → IC=+0.305 (n=116)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2011 (IC base=+0.087)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.312 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.087)

- **PATRÓN** `ibs_15` > `0.7503` → IC=+0.330 (n=256)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7503 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.0996` → IC=+0.293 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0996 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.4912` → IC=+0.294 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4912 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.533` → IC=+0.125 (n=299)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 8.533 (IC base=+0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0613` → IC=+0.240 (n=48)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0613 (IC base=-0.191)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.191)

- **PATRÓN** `ibs_15` < `0.6473` → IC=+0.320 (n=48)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6473 (IC base=-0.191)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.191)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.441 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=-0.191)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=549)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.149 (n=374)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0057 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0037` → IC=+0.160 (n=380)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0037 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1111` → IC=+0.182 (n=284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1111 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1402` → IC=+0.149 (n=283)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio_macro` |x|> 0.1402 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.194 (n=315)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.169 (n=303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.6395` → IC=+0.249 (n=425)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6395 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.5705` → IC=+0.155 (n=82)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.5705 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2628` → IC=+0.153 (n=401)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2628 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.224 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=549)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `11185.367` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 11185.367 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.254 (n=441)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.345` → IC=+0.241 (n=881)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.345 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `0.7573` → IC=+0.251 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7573 (IC base=+0.239)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2115` → IC=+0.268 (n=454)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2115 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.247 (n=390)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.239)

- **PATRÓN** `ibs_15` < `0.3657` → IC=+0.271 (n=1001)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3657 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.7436` → IC=+0.306 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7436 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.365` → IC=+0.262 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.365 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.584` → IC=+0.243 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.584 (IC base=+0.239)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1705` → IC=-0.240 (n=283)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1705
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=552)

- **FILTRO** `drift_15min` |x|> `0.8773` → IC=-0.276 (n=208)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8773
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=627)

- **FILTRO** `sigma_ewma_delta_pct` > `6.602` → IC=-0.179 (n=207)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.602
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=628)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.259 (n=81)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=754)

- **FILTRO** `sigma_ewma_delta_pct` > `18.298` → IC=-0.143 (n=432)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.298
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3474)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.174 (n=44)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.177)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.238 (n=59)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=-0.177)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.177)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.177)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.177)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0785` → IC=+0.239 (n=401)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0785 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.189` → IC=+0.238 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.189 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.283 (n=450)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.172` → IC=+0.245 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.172 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1255` → IC=-0.225 (n=504)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1255
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=505)

- **FILTRO** `sigma_h` > `0.0192` → IC=-0.257 (n=504)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0192
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=505)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.201)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1483` → IC=+0.281 (n=317)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1483 (IC base=-0.027)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1113` → IC=+0.307 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1113 (IC base=-0.027)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.297 (n=702)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.027)

- **PATRÓN** `dist_vwap_pct` > `0.7832` → IC=+0.355 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7832 (IC base=-0.027)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `dist_vwap_pct` > `0.1515` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1515 (IC base=+0.033)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1515` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1515 (IC base=+0.033)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.291 (n=583)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.289 (n=873)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0029 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.327 (n=292)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.291 (n=582)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2235` → IC=+0.311 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2235 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=915)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8395` → IC=+0.321 (n=873)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8395 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.1554` → IC=+0.317 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1554 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.656` → IC=+0.355 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.656 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `12879.5491` → IC=+0.306 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12879.5491 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.307 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0557` → IC=+0.326 (n=159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0557 (IC base=+0.287)

- **PATRÓN** `drift_15min` |x|≤ `0.4172` → IC=+0.287 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4172 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2491` → IC=+0.306 (n=158)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2491 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.109` → IC=+0.296 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.109 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.309 (n=474)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.315 (n=474)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2565` → IC=+0.333 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2565 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.366 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `16322.5844` → IC=+0.331 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16322.5844 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.295 (n=267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.295 (n=399)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.324 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3007` → IC=+0.313 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3007 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.305 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.330 (n=399)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2774` → IC=+0.311 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2774 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.656` → IC=+0.331 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.656 (IC base=+0.290)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0872` → IC=-0.256 (n=76)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0872
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=229)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.252 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=202)

- **FILTRO** `drift_60min` |x|> `0.2527` → IC=-0.154 (n=76)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2527
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=229)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.187 (n=113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=345)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0682` → IC=-0.145 (n=60)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0682
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=117)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.174 (n=44)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=133)

- **FILTRO** `drift_15min` |x|> `0.3691` → IC=-0.265 (n=15)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3691
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1819` → IC=-0.260 (n=23)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1819
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=24)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1931` → IC=-0.167 (n=25)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1931
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.222 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

### UPDOWN_OU_5M#XRP#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1195` → IC=-0.206 (n=15)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1195
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.265 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.3593` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3593
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.3119` → IC=-0.184 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3119
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `81.6124` → IC=+0.234 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 81.6124 (IC base=+0.219)

- **PATRÓN** `ratio` < `0.9766` → IC=+0.473 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9766 (IC base=+0.219)

- **PATRÓN** `T_h` > `145.7419` → IC=+0.388 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7419 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0104` → IC=+0.320 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0104 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `126.6969` → IC=+0.256 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 126.6969 (IC base=+0.202)

- **PATRÓN** `ratio` < `0.973` → IC=+0.458 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.202)

- **PATRÓN** `T_h` > `106.9024` → IC=+0.294 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 106.9024 (IC base=+0.287)

- **PATRÓN** `ratio` > `1.0479` → IC=+0.401 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0479 (IC base=+0.287)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.270 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.251)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.433 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.251)

- **PATRÓN** `T_h` > `111.9558` → IC=+0.345 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9558 (IC base=+0.321)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.359 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.321)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1131` → IC=+0.457 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1131 (IC base=+0.401)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6047 sube el IC de +0.195 a +0.271 en UPDOWN_GBM#15min (n=2516). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7141 sube el IC de +0.215 a +0.279 en UPDOWN_GBM#BTC#15min (n=491). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5731 sube el IC de +0.136 a +0.233 en UPDOWN_GBM#ETH#15min (n=538). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.155 a +0.229 en UPDOWN_GBM#SOL#15min (n=385). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5849 sube el IC de +0.214 a +0.293 en UPDOWN_GBM#XRP#15min (n=608). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.069 a +0.156 en UPDOWN_GBM#XRP#15min (n=655). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.068 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=860). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3508 sube el IC de -0.014 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=2820). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7503 sube el IC de +0.087 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=256). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6473 sube el IC de -0.191 a +0.320 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=48). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6395 sube el IC de +0.146 a +0.249 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=425). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3657 sube el IC de +0.239 a +0.271 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1001). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de -0.177 a +0.238 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=59). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.039 a +0.283 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=450). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.201 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.027 a +0.297 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=702). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8395 sube el IC de +0.289 a +0.321 en UPDOWN_GBM_IBS_ALTO (n=873). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.287 a +0.315 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=474). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.290 a +0.330 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=399). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.358 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=532). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.357 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=288). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.356 a +0.402 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=243). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1577 | +0.093 | +179.40€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1577 | +0.093 | +179.40€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1209 | +0.098 | +150.98€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1209 | +0.098 | +150.98€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 265 | +0.069 | +12.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 265 | +0.069 | +12.71€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 262 | +0.015 | +63.62€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 262 | +0.015 | +63.62€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 211 | +0.012 | +53.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 211 | +0.012 | +53.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 29 | +0.081 | +8.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 29 | +0.081 | +8.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 34704 | -0.084 | -4600.33€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1752 | -0.013 | -219.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 32952 | -0.088 | -4380.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4363 | -0.120 | -762.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4363 | -0.120 | -762.84€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1752 | -0.013 | -219.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1752 | -0.013 | -219.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4071 | -0.114 | -901.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4071 | -0.114 | -901.52€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8974 | +0.005 | -845.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8974 | +0.005 | -845.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8797 | -0.106 | -634.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8797 | -0.106 | -634.24€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6747 | -0.150 | -1236.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6747 | -0.150 | -1236.60€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 26787 | -0.019 | +3754.30€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6929 | +0.002 | +1783.17€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 19858 | -0.027 | +1971.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 26787 | -0.019 | +3754.30€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6929 | +0.002 | +1783.17€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 19858 | -0.027 | +1971.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1486 | -0.102 | -190.28€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 176 | -0.045 | -19.67€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1310 | -0.110 | -170.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 788 | -0.089 | -95.94€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 152 | -0.039 | -14.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 491 | -0.125 | -74.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 467 | -0.127 | -69.10€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 119121 | +0.113 | -5314.83€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 16504 | +0.183 | -495.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 508 | -0.045 | -62.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 94735 | +0.103 | -4485.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7374 | +0.104 | -270.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 15733 | +0.103 | -1086.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 55 | -0.149 | +10.33€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 15663 | +0.105 | -1084.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 23534 | +0.129 | -408.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4889 | +0.196 | -143.72€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 15710 | +0.116 | -171.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2893 | +0.089 | -71.75€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 15778 | +0.094 | -1240.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 62 | -0.109 | -4.45€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 15701 | +0.096 | -1224.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 25301 | +0.124 | -439.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6726 | +0.175 | -100.54€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 15885 | +0.106 | -274.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2678 | +0.101 | -55.77€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 23026 | +0.114 | -1263.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4716 | +0.190 | -267.93€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 411 | -0.009 | -8.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 16096 | +0.093 | -844.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1803 | +0.132 | -143.07€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 15749 | +0.101 | -875.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 56 | -0.035 | +10.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 15680 | +0.102 | -886.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 19010 | +0.194 | -1194.42€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 19010 | +0.194 | -1194.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4405 | +0.173 | -414.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4405 | +0.173 | -414.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2092 | +0.202 | -35.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2092 | +0.202 | -35.71€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4335 | +0.182 | -346.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4335 | +0.182 | -346.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3820 | +0.241 | -137.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3820 | +0.241 | -137.50€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4279 | +0.189 | -273.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4279 | +0.189 | -273.49€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 883 | +0.425 | -33.40€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 883 | +0.425 | -33.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 348 | +0.434 | -6.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 348 | +0.434 | -6.27€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 336 | +0.426 | -11.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 336 | +0.426 | -11.74€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 187 | +0.405 | -12.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 187 | +0.405 | -12.95€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 66097 | +0.200 | -4917.49€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 66097 | +0.200 | -4917.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 11370 | +0.183 | -1202.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 11370 | +0.183 | -1202.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 10644 | +0.224 | -377.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 10644 | +0.224 | -377.07€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 11351 | +0.177 | -1262.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 11351 | +0.177 | -1262.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10700 | +0.220 | -397.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10700 | +0.220 | -397.68€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10955 | +0.202 | -730.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10955 | +0.202 | -730.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 11077 | +0.193 | -946.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 11077 | +0.193 | -946.76€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 25197 | +0.118 | +227.51€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 25197 | +0.118 | +227.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 12514 | +0.121 | +181.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 12514 | +0.121 | +181.08€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 12683 | +0.114 | +46.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 12683 | +0.114 | +46.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1768 | +0.288 | -25.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1768 | +0.288 | -25.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 799 | +0.279 | -18.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 799 | +0.279 | -18.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 851 | +0.287 | -10.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 851 | +0.287 | -10.93€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 118 | +0.350 | +4.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 118 | +0.350 | +4.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 798 | +0.440 | +1.78€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 798 | +0.440 | +1.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 385 | +0.438 | -1.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 385 | +0.438 | -1.57€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 367 | +0.443 | +2.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 367 | +0.443 | +2.80€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1374 | +0.068 | -68.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 502 | +0.059 | -38.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 872 | +0.072 | -29.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1074 | +0.072 | -37.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 202 | +0.073 | -7.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 872 | +0.072 | -29.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 234 | +0.034 | -33.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 234 | +0.034 | -33.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 48493 | +0.100 | -1257.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3935 | +0.092 | +54.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 44558 | +0.100 | -1312.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 26876 | +0.104 | -305.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3935 | +0.092 | +54.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 22941 | +0.106 | -360.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 9642 | +0.110 | -16.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 9642 | +0.110 | -16.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 11975 | +0.081 | -935.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 11975 | +0.081 | -935.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 871 | +0.203 | -101.16€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 871 | +0.203 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 871 | +0.203 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 871 | +0.203 | -101.16€ | 2 | 4 |
| ✅ GBM_LATE_15M | 33855 | +0.089 | +16856.54€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 33855 | +0.089 | +16856.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5696 | +0.204 | +4418.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5696 | +0.204 | +4418.16€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 5030 | +0.177 | +3622.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5030 | +0.177 | +3622.15€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 6012 | +0.201 | +4566.93€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6012 | +0.201 | +4566.93€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 4787 | +0.034 | +1199.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4787 | +0.034 | +1199.24€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4823 | -0.030 | +1053.36€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4823 | -0.030 | +1053.36€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 7507 | -0.036 | +1996.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7507 | -0.036 | +1996.71€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 36680 | +0.087 | +19496.09€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 36680 | +0.087 | +19496.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7108 | +0.012 | +3652.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7108 | +0.012 | +3652.85€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7603 | +0.013 | +1628.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7603 | +0.013 | +1628.61€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5171 | +0.268 | +5336.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5171 | +0.268 | +5336.50€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 6222 | +0.012 | +1373.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 6222 | +0.012 | +1373.83€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5984 | +0.036 | +2375.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5984 | +0.036 | +2375.14€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4592 | +0.289 | +5129.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4592 | +0.289 | +5129.17€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 27031 | +0.176 | +21221.44€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 27031 | +0.176 | +21221.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4089 | +0.218 | +3443.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4089 | +0.218 | +3443.12€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4266 | +0.151 | +3116.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4266 | +0.151 | +3116.57€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4290 | +0.217 | +3581.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4290 | +0.217 | +3581.16€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4543 | +0.138 | +3375.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4543 | +0.138 | +3375.72€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5060 | +0.126 | +3721.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5060 | +0.126 | +3721.25€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4783 | +0.214 | +3983.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4783 | +0.214 | +3983.61€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7356 | +0.139 | +3545.05€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7356 | +0.139 | +3545.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 341 | +0.141 | +188.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 341 | +0.141 | +188.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2248 | +0.147 | +1254.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2248 | +0.147 | +1254.22€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2248 | +0.154 | +1107.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2248 | +0.154 | +1107.72€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1607 | +0.108 | +579.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1607 | +0.108 | +579.43€ | 1 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 537 | +0.135 | +240.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 537 | +0.135 | +240.44€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 34078 | +0.181 | +26419.02€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 34078 | +0.181 | +26419.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5423 | +0.232 | +4836.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5423 | +0.232 | +4836.57€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5269 | +0.148 | +3457.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5269 | +0.148 | +3457.53€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5701 | +0.229 | +4991.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5701 | +0.229 | +4991.86€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5541 | +0.137 | +3856.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5541 | +0.137 | +3856.69€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6026 | +0.125 | +4159.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6026 | +0.125 | +4159.04€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6118 | +0.218 | +5117.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6118 | +0.218 | +5117.34€ | 0 | 21 |
| ✅ GBM_LATE_5M | 9433 | +0.182 | +6579.81€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 9433 | +0.182 | +6579.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2115 | +0.168 | +1523.00€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2115 | +0.168 | +1523.00€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 992 | +0.176 | +650.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 992 | +0.176 | +650.38€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 2943 | +0.185 | +1988.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2943 | +0.185 | +1988.35€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 1228 | +0.181 | +855.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1228 | +0.181 | +855.11€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 1320 | +0.174 | +833.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1320 | +0.174 | +833.55€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2546 | +0.073 | +920.96€ | 0 | 12 |
| ✅ GBM_LATE_60M#60min | 2546 | +0.073 | +920.96€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 960 | +0.091 | +354.01€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 960 | +0.091 | +354.01€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 793 | +0.072 | +350.36€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 793 | +0.072 | +350.36€ | 0 | 14 |
| ✅ GBM_LATE_60M#SOL | 793 | +0.050 | +216.59€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 793 | +0.050 | +216.59€ | 2 | 14 |
| 🚫 GBM_LATE_60M_FADE | 484 | -0.239 | -15.40€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 484 | -0.239 | -15.40€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 181 | -0.227 | -9.60€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 181 | -0.227 | -9.60€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 170 | -0.221 | -0.14€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 170 | -0.221 | -0.14€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 133 | -0.270 | -5.66€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 133 | -0.270 | -5.66€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1117 | +0.088 | +287.79€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1117 | +0.088 | +287.79€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 425 | +0.081 | +91.92€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 425 | +0.081 | +91.92€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 382 | +0.065 | +64.92€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 382 | +0.065 | +64.92€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 310 | +0.125 | +130.95€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 310 | +0.125 | +130.95€ | 2 | 13 |
| ✅ LATE_WINDOW_5MIN | 129 | +0.248 | +107.36€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 129 | +0.248 | +107.36€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 129 | +0.248 | +107.36€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 129 | +0.248 | +107.36€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2807 | +0.102 | +726.94€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2807 | +0.102 | +726.94€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2807 | +0.102 | +726.94€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2807 | +0.102 | +726.94€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 432 | -0.067 | -31.10€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 432 | -0.067 | -31.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 119 | -0.029 | -1.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 119 | -0.029 | -1.27€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 164 | -0.024 | -5.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 164 | -0.024 | -5.01€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 2976 | +0.020 | +72.77€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2976 | +0.020 | +72.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 143 | +0.038 | +0.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 143 | +0.038 | +0.68€ | 1 | 2 |
| ✅ LIQUIDACIONES_5M#BTC | 483 | +0.024 | +31.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 483 | +0.024 | +31.36€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1093 | +0.030 | +30.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1093 | +0.030 | +30.24€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 671 | +0.014 | +2.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 671 | +0.014 | +2.19€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 383 | +0.012 | +13.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 383 | +0.012 | +13.39€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1438 | -0.039 | -21.46€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1438 | -0.039 | -21.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 411 | -0.037 | -12.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 411 | -0.037 | -12.30€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 474 | -0.013 | +6.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 474 | -0.013 | +6.10€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 553 | -0.062 | -15.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 553 | -0.062 | -15.27€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 5001 | -0.015 | +124.35€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2358 | -0.022 | +22.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2643 | -0.010 | +101.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 138 | -0.007 | +3.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 68 | +0.043 | +10.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 70 | -0.056 | -7.18€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1249 | -0.007 | +36.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 587 | -0.013 | +5.81€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 662 | -0.002 | +30.46€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 569 | -0.025 | +6.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 282 | -0.035 | -3.35€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 287 | -0.016 | +9.93€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1030 | -0.029 | -10.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 471 | -0.052 | -31.79€ | 4 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 559 | -0.010 | +21.40€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 977 | -0.010 | +42.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 475 | -0.009 | +24.62€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 502 | -0.010 | +17.98€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1038 | -0.013 | +46.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 475 | -0.016 | +16.90€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 563 | -0.010 | +29.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 39245 | -0.003 | +1853.25€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 39245 | -0.003 | +1853.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 7009 | +0.024 | +925.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 7009 | +0.024 | +925.16€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5828 | -0.032 | -93.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5828 | -0.032 | -93.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 7100 | +0.020 | +689.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 7100 | +0.020 | +689.54€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5636 | -0.050 | -148.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5636 | -0.050 | -148.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6617 | -0.008 | +205.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6617 | -0.008 | +205.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 7055 | +0.013 | +274.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 7055 | +0.013 | +274.52€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6210 | -0.059 | -143.79€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6210 | -0.059 | -143.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1220 | +0.001 | -13.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1220 | +0.001 | -13.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1528 | -0.076 | -30.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1528 | -0.076 | -30.99€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 48 | -0.080 | -3.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 48 | -0.080 | -3.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 722 | -0.124 | -34.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 722 | -0.124 | -34.04€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1836 | -0.078 | -36.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1836 | -0.078 | -36.36€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3353 | +0.004 | -3.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3353 | +0.004 | -3.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1320 | +0.005 | +5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1320 | +0.005 | +5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 98413 | -0.073 | +1766.08€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 98413 | -0.073 | +1766.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 16930 | -0.074 | +896.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 16930 | -0.074 | +896.41€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 14934 | -0.098 | -810.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 14934 | -0.098 | -810.91€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 17193 | -0.065 | +1051.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 17193 | -0.065 | +1051.53€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 14466 | -0.094 | -416.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 14466 | -0.094 | -416.58€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 17814 | -0.052 | +336.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 17814 | -0.052 | +336.51€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 17076 | -0.064 | +709.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 17076 | -0.064 | +709.12€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8085 | -0.032 | -156.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8085 | -0.032 | -156.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1922 | -0.043 | -18.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1922 | -0.043 | -18.45€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2245 | -0.026 | -31.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2245 | -0.026 | -31.96€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1123 | -0.050 | -24.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1123 | -0.050 | -24.48€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 791 | -0.027 | -29.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 791 | -0.027 | -29.27€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1395 | +0.118 | +529.99€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1259 | +0.124 | +517.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 293 | +0.144 | +154.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 293 | +0.144 | +154.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 242 | +0.102 | +65.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 242 | +0.102 | +65.75€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 257 | +0.118 | +104.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 257 | +0.118 | +104.46€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 225 | +0.152 | +123.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 225 | +0.152 | +123.37€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 242 | +0.098 | +68.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 242 | +0.098 | +68.95€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 976 | -0.013 | -14.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 976 | -0.013 | -14.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 193 | +0.003 | +7.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 193 | +0.003 | +7.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 147 | +0.003 | +4.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 147 | +0.003 | +4.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 258 | -0.031 | -15.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 258 | -0.031 | -15.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 214 | +0.005 | +0.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 214 | +0.005 | +0.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 164 | -0.042 | -11.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 164 | -0.042 | -11.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 763 | -0.092 | -76.95€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 349 | -0.144 | -83.44€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 269 | -0.186 | -76.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 80 | +0.000 | -7.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 270 | -0.051 | -5.72€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 191 | -0.054 | -6.49€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 79 | -0.043 | +0.77€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 144 | -0.041 | +12.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 115 | -0.056 | +6.80€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 29 | +0.016 | +5.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 575 | -0.117 | -75.98€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 188 | -0.016 | -0.96€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 907 | -0.203 | -56.19€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 377 | -0.197 | -34.24€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 322 | -0.201 | -35.03€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 55 | -0.167 | +0.79€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 306 | -0.217 | -32.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 262 | -0.227 | -38.57€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 44 | -0.152 | +5.58€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 224 | -0.190 | +11.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 205 | -0.186 | +7.90€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 789 | -0.207 | -65.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 118 | -0.175 | +9.51€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 387 | +0.400 | +333.24€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 45 | +0.096 | +25.91€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 45 | +0.096 | +25.91€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 98 | +0.370 | +76.40€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 98 | +0.370 | +76.40€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 244 | +0.463 | +230.93€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 244 | +0.463 | +230.93€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 387 | +0.400 | +333.24€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 629 | +0.031 | +25.01€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 629 | +0.031 | +25.01€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 47 | +0.031 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 47 | +0.031 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 65 | -0.007 | -1.72€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 65 | -0.007 | -1.72€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 222 | +0.054 | +25.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 222 | +0.054 | +25.03€ | 2 | 4 |
| ✅ STREAK_FADE_5M | 3129 | -0.021 | -121.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3129 | -0.021 | -121.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 927 | -0.022 | -33.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 927 | -0.022 | -33.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 585 | -0.026 | -25.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 585 | -0.026 | -25.65€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1461 | -0.015 | -48.42€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1461 | -0.015 | -48.42€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 91 | -0.059 | -9.78€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 91 | -0.059 | -9.78€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 53 | -0.027 | -5.34€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 53 | -0.027 | -5.34€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 9802 | +0.018 | +99.44€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9802 | +0.018 | +99.44€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2639 | +0.021 | +28.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2639 | +0.021 | +28.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2348 | +0.025 | +45.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2348 | +0.025 | +45.30€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2861 | +0.010 | -0.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2861 | +0.010 | -0.81€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1954 | +0.019 | +26.12€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1954 | +0.019 | +26.12€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8885 | +0.013 | -44.90€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8885 | +0.013 | -44.90€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3506 | +0.018 | -5.53€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3506 | +0.018 | -5.53€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3512 | +0.012 | -24.40€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3512 | +0.012 | -24.40€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1867 | +0.007 | -14.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1867 | +0.007 | -14.96€ | 1 | 0 |
| ✅ UPDOWN_GBM | 59979 | +0.047 | +4766.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 14886 | +0.082 | +3207.73€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1976 | +0.005 | +7.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 39489 | +0.041 | +1500.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3425 | +0.006 | +52.78€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6205 | +0.082 | +862.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1279 | +0.153 | +545.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 56 | -0.017 | -1.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4870 | +0.065 | +317.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 11601 | +0.050 | +929.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1884 | +0.091 | +438.21€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 516 | +0.012 | +5.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 7575 | +0.054 | +442.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1551 | +0.005 | +41.47€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 75 | -0.084 | +2.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 7263 | +0.060 | +666.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1255 | +0.144 | +477.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 54 | +0.000 | -2.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 5954 | +0.043 | +191.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 13075 | +0.037 | +717.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3544 | +0.056 | +452.62€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 509 | +0.007 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 7792 | +0.036 | +252.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1163 | +0.004 | +0.07€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 67 | -0.109 | +3.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 13278 | +0.026 | +525.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3510 | +0.035 | +316.51€ | 0 | 13 |
| ✅ UPDOWN_GBM#SOL#240min | 499 | -0.001 | -1.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 8499 | +0.026 | +204.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 711 | +0.013 | +11.24€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#daily | 59 | -0.156 | -5.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 8555 | +0.057 | +1067.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3414 | +0.103 | +976.84€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 342 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4799 | +0.027 | +91.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 201 | -0.116 | +0.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 708 | +0.358 | +241.67€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 708 | +0.358 | +241.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 384 | +0.357 | +124.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 384 | +0.357 | +124.94€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 324 | +0.356 | +116.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 324 | +0.356 | +116.73€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 16404 | -0.026 | +3859.03€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 16404 | -0.026 | +3859.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1366 | -0.051 | +447.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1366 | -0.051 | +447.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2847 | -0.112 | +128.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2847 | -0.112 | +128.49€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 773 | +0.213 | +621.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 773 | +0.213 | +621.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1900 | +0.211 | +1182.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1900 | +0.211 | +1182.72€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4741 | -0.063 | +622.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4741 | -0.063 | +622.79€ | 5 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4777 | -0.064 | +855.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4777 | -0.064 | +855.43€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 182 | +0.033 | +7.26€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 182 | +0.033 | +7.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 182 | +0.033 | +7.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 182 | +0.033 | +7.26€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1164 | +0.289 | +947.60€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1164 | +0.289 | +947.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 632 | +0.287 | +488.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 632 | +0.287 | +488.97€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 532 | +0.290 | +458.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 532 | +0.290 | +458.63€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 763 | -0.114 | -84.80€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 763 | -0.114 | -84.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 224 | -0.088 | -18.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 224 | -0.088 | -18.30€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 77 | -0.158 | -8.42€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 77 | -0.158 | -8.42€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 83 | -0.194 | -8.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 83 | -0.194 | -8.02€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2967 | +0.307 | +1456.33€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1055 | +0.261 | +156.12€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1135 | +0.299 | +500.36€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 777 | +0.378 | +799.85€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.019 n=728 — no justifica filtro, seguir monitorizando
  - _Datos_: n=728 IC=+0.019 PNL=+37.09€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 638 celda(s) pasan gate riguroso completo de 2489 evaluadas (n>=40) y 3475 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.035 < 0.08 — monitorear
  - _Datos_: n=3505 IC=+0.035 PNL=+320.23€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1135/15 IC=+0.299 PNL=+500.36€ | BTC: n=1055/15 IC=+0.261 PNL=+156.12€ | SOL: n=777/15 IC=+0.378 PNL=+799.85€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 31 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: alineada_con_outcome_prev IC=+0.133 n=586/60 | contraria IC=+0.192 n=605 | gap=-0.059 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=386, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1161/40 IC=+0.004 PNL=+0.22€ | BTC#60min: n=1549/40 IC=+0.005 PNL=+41.44€ | SOL#60min: n=710/40 IC=+0.013 PNL=+9.89€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=448416 | tras_1loss IC=+0.090 n=343525 | tras_2loss IC=+0.059 n=140856/40 | gap=-0.011 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.213 > 0.08 con n=514 PNL=+402.21€
  - _Datos_: n=514 IC=+0.213 PNL=+402.21€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.08 con n=570 PNL=+412.58€
  - _Datos_: n=570 IC=+0.206 PNL=+412.58€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.198 > 0.08 con n=51 PNL=+31.30€
  - _Datos_: n=51 IC=+0.198 PNL=+31.30€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.331 > 0.1 con n=2422 PNL=+1313.95€
  - _Datos_: n=2422 IC=+0.331 PNL=+1313.95€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=478 IC=+0.069 PNL=+50.65€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=478 IC=+0.069 PNL=+50.65€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=68 IC=+0.186 PNL=+45.65€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=68 IC=+0.186 PNL=+45.65€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 4/15 ops en el filtro definido (IC actual=+0.067 PNL=+7.14€)
  - _Datos_: n=4 IC=+0.067 PNL=+7.14€

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
  - _Estado_: n=2296 IC=+0.006 PNL=+0.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2296 IC=+0.006 PNL=+0.74€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1124 IC=+0.007 PNL=+50.80€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1124 IC=+0.007 PNL=+50.80€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=728 IC=+0.019 PNL=+37.09€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=728 IC=+0.019 PNL=+37.09€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.197 > 0.1 con n=3343 PNL=+2295.66€
  - _Datos_: n=3343 IC=+0.197 PNL=+2295.66€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1882 IC=+0.090 PNL=+437.19€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1882 IC=+0.090 PNL=+437.19€

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
  - _Estado_: n=778 IC=+0.033 PNL=+67.83€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=778 IC=+0.033 PNL=+67.83€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=85 IC=+0.040 PNL=+3.74€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=85 IC=+0.040 PNL=+3.74€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.248 n=129) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=129 IC=+0.248 PNL=+107.36€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=801 PNL=+323.72€
  - _Datos_: n=801 IC=+0.124 PNL=+323.72€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=191 IC=-0.070 PNL=+27.59€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=191 IC=-0.070 PNL=+27.59€

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
  - _Estado_: n=22449 IC=+0.070 PNL=+3140.86€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=22449 IC=+0.070 PNL=+3140.86€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.138 < -0.1 con n=357 PNL=+43.76€
  - _Datos_: n=357 IC=-0.138 PNL=+43.76€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2601 IC=+0.068 PNL=+318.44€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2601 IC=+0.068 PNL=+318.44€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=110 IC=-0.125 PNL=+3.29€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=110 IC=-0.125 PNL=+3.29€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.1 con n=616 PNL=+160.80€
  - _Datos_: n=616 IC=+0.118 PNL=+160.80€

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
  - _Estado_: n=24556 IC=-0.136 PNL=+1746.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=24556 IC=-0.136 PNL=+1746.74€

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
  - _Estado_: n=2511 IC=+0.135 PNL=+1449.85€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2511 IC=+0.135 PNL=+1449.85€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=6242 IC=+0.043 PNL=+422.35€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6242 IC=+0.043 PNL=+422.35€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.089 > 0.08 con n=2776 PNL=+1460.10€
  - _Datos_: n=2776 IC=+0.089 PNL=+1460.10€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.228 < -0.1 con n=2512 PNL=-217.04€
  - _Datos_: n=2512 IC=-0.228 PNL=-217.04€

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

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=51 IC=+0.009 PNL=+7.79€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=51 IC=+0.009 PNL=+7.79€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1430) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1430 IC=+0.101 PNL=+324.09€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=499) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=499 IC=+0.410 PNL=+707.28€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=11361 IC=+0.183 PNL=-1198.84€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=11361 IC=+0.183 PNL=-1198.84€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.211 > 0.1 con n=178 PNL=+111.12€
  - _Datos_: n=178 IC=+0.211 PNL=+111.12€
