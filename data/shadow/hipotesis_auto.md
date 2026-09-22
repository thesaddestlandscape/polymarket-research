# Hipótesis automáticas — 2026-09-22 23:07 UTC
_Generado por shadow_postmortem.py sobre 564134 resoluciones (PNL=+62979.35€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=504)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=455)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.253 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.137)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.207 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.137)

- **PATRÓN** `banda_hit_calibrado` > `0.8038` → IC=+0.253 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8038 (IC base=+0.137)

- **PATRÓN** `banda_z` > `4.245` → IC=+0.165 (n=530)

  - _Acción_: Kelly boost +0.83€ cuando `banda_z` > 4.245 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=565)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4766.038` → IC=+0.154 (n=177)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 4766.038 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.127 (n=159)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 96.0 (IC base=+0.041)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.259 (n=401)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=328)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.259 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.146)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.208 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.146)

- **PATRÓN** `banda_hit_calibrado` > `0.8014` → IC=+0.264 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8014 (IC base=+0.146)

- **PATRÓN** `banda_z` > `4.443` → IC=+0.174 (n=424)

  - _Acción_: Kelly boost +0.87€ cuando `banda_z` > 4.443 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.163 (n=301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=478)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.145 (n=119)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 96.0 (IC base=+0.042)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.515` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=89)

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

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.258 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.109)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.233 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.109)

- **PATRÓN** `banda_z` > `6.035` → IC=+0.162 (n=66)

  - _Acción_: Kelly boost +0.81€ cuando `banda_z` > 6.035 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.164 (n=105)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `879.7655` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 879.7655 (IC base=+0.109)

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
- **FILTRO** `restante_s_al_confirmar` < `146.2` → IC=-0.231 (n=6783)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.2
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=20350)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `140.51` → IC=-0.236 (n=892)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.51
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2676)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `497.2` → IC=-0.145 (n=356)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 497.2
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1071)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `134.67` → IC=-0.279 (n=835)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 134.67
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2506)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `163.45` → IC=-0.228 (n=1608)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 163.45
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4827)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `124.33` → IC=-0.360 (n=1354)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.33
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=4065)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.48` → IC=-0.226 (n=377)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=378)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.178 (n=231)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=472)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=553)

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
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=188)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.179 (n=79)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=154)

- **FILTRO** `py_entrada` < `0.47` → IC=-0.167 (n=70)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=163)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.201 (n=13434)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3361)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5585.2315` → IC=+0.175 (n=2143)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 5585.2315 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.140 (n=10916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=13109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.234 (n=10422)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=5476)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7705.2031` → IC=+0.173 (n=2060)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7705.2031 (IC base=+0.128)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.211 (n=1408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1618)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.352 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2034)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `15816.1808` → IC=+0.229 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15816.1808 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=1462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.264 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=2063)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `13925.3414` → IC=+0.210 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13925.3414 (IC base=+0.200)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.59` → IC=+0.167 (n=452)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.59 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.144 (n=234)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4624.034 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.151 (n=336)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.109)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.149 (n=795)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.44 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=556)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `5871.1399` → IC=+0.161 (n=219)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 5871.1399 (IC base=+0.109)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2712)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=2306)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.334 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.356 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.240 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.234)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=569)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.230 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=516)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `1302.9991` → IC=+0.150 (n=630)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1302.9991 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.237 (n=596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.432 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.169 (n=1051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 7.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.165 (n=565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 7.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` < `0.27` → IC=+0.313 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.27 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=711)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.165)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.114)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.197 (n=368)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.355 (IC base=+0.114)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=106)

- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=10978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=10468)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.225 (n=3697)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=2535)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.184 (n=1854)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.258 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.250 (n=743)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.356 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.248)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=2489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=2501)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.188 (n=1132)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.73 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=2341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.319 (n=825)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=2547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=2444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.198 (n=1865)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.194)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=480)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.431 (n=449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.470 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `2062.8229` → IC=+0.438 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2062.8229 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.435 (n=197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.453 (n=168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.471 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.437 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `3355.2252` → IC=+0.445 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3355.2252 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.405 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.403)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.405 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.403)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.418 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.403)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.406 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.403)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=32592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.232 (n=17642)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.177 (n=5637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 8.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=5569)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=6042)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=5832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.227 (n=5795)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.275 (n=2090)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.180 (n=5593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=5946)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=2939)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.264 (n=2042)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.211 (n=5394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.254 (n=2193)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.197 (n=5457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=5399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2098)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=4985)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.14` → IC=+0.128 (n=4564)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.14 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.141 (n=4883)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.129 (n=6756)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 8.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.03` → IC=+0.142 (n=4551)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.03 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.200 (n=2514)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.122)

- **PATRÓN** `restante_min` < `4.09` → IC=+0.132 (n=2263)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` < 4.09 (IC base=+0.122)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.141 (n=2419)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.94 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.141 (n=2593)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 6.0 (IC base=+0.122)

- **PATRÓN** `lag_apertura_s` < `3.45` → IC=+0.145 (n=2259)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.45 (IC base=+0.122)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=2471)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` < `4.18` → IC=+0.124 (n=2297)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.18 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.137 (n=2471)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.32` → IC=+0.140 (n=2303)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.32 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.386 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1556.4998` → IC=+0.298 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1556.4998 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.302 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.341 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `4209.1188` → IC=+0.302 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4209.1188 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.332 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.304 (n=534)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.386 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `1466.4356` → IC=+0.312 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1466.4356 (IC base=+0.296)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.445 (n=416)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `2554.5498` → IC=+0.439 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2554.5498 (IC base=+0.439)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.445 (n=215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.453 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `2025.2696` → IC=+0.460 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2025.2696 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.370 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.381)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=51)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=51)

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
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=51)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=51)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4748` → IC=+0.121 (n=7646)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.60€ cuando `drift_60min` |x|≤ 0.4748 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.9829` → IC=+0.242 (n=2549)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9829 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.8352` → IC=+0.248 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8352 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.156` → IC=+0.247 (n=1492)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.156 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.934` → IC=+0.176 (n=2953)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.934 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `1.0476` → IC=+0.257 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0476 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.3051` → IC=+0.214 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3051 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.9075` → IC=+0.206 (n=3473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9075 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.57` → IC=+0.131 (n=9211)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.57 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.5936` → IC=+0.195 (n=709)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.5936 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` < `0.1492` → IC=+0.172 (n=2842)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1492 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` < `0.6983` → IC=+0.176 (n=1403)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6983 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` > `0.8688` → IC=+0.175 (n=2125)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.8688 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` > `0.1683` → IC=+0.221 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1683 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` > `1.5771` → IC=+0.201 (n=4757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5771 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.210 (n=5107)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.063)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.180 (n=582)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.005 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.171 (n=578)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0082 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3452` → IC=+0.166 (n=1732)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3452 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.172 (n=1154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.119` → IC=+0.270 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.119 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.211 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.164 (n=1616)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.251 (n=1145)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.288 (n=428)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=1164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0604` → IC=+0.293 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0604 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.39` → IC=+0.249 (n=1338)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.39 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0914` → IC=+0.231 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0914 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.264 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.6401` → IC=+0.246 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6401 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1788.1199` → IC=+0.239 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1788.1199 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.230 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.233 (n=585)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.0842` → IC=+0.251 (n=440)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0842 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=1322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.9902` → IC=+0.262 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9902 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.1993` → IC=+0.221 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1993 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.7398` → IC=+0.216 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7398 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.827` → IC=+0.250 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.827 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.2524` → IC=+0.217 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2524 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `1.0803` → IC=+0.224 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0803 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.0741` → IC=+0.227 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0741 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.4011` → IC=+0.223 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4011 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.3728` → IC=+0.221 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3728 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `12278.145` → IC=+0.217 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12278.145 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.175 (n=460)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.159 (n=459)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.165 (n=461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6888` → IC=+0.170 (n=1372)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6888 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1289` → IC=+0.158 (n=1209)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1289 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.208` → IC=+0.159 (n=221)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.208 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.218` → IC=+0.141 (n=1247)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.218 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.148 (n=1372)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.204 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0963` → IC=+0.172 (n=495)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0963 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4267` → IC=+0.151 (n=1261)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4267 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.77` → IC=+0.145 (n=841)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.77 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.147 (n=1182)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 411.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.214 (n=562)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.189 (n=1692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=1505)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.173` → IC=+0.253 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.173 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` < `0.2115` → IC=+0.189 (n=1678)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.2115 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.3635` → IC=+0.196 (n=222)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.3635 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.8806` → IC=+0.206 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8806 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.195 (n=1180)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.02 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.223 (n=1438)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.5795` → IC=+0.215 (n=1438)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5795 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=673)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.240 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.554` → IC=+0.239 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.554 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.359` → IC=+0.270 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.359 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.8783` → IC=+0.228 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8783 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `1867.4117` → IC=+0.229 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1867.4117 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.216 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.214)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.160 (n=95)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2115)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.211 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.3604` → IC=+0.325 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3604 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.7698` → IC=+0.326 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7698 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.643` → IC=+0.152 (n=679)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.643 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.6634` → IC=+0.332 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6634 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.1956` → IC=+0.338 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1956 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1771` → IC=+0.319 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1771 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.337 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4007` → IC=+0.332 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4007 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.1835` → IC=+0.318 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1835 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.328 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 163.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.6579` → IC=+0.192 (n=141)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6579 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `0.852` → IC=+0.156 (n=518)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.852 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.212 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `1.5154` → IC=+0.174 (n=646)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.5154 (IC base=+0.012)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.161 (n=57)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=309)

- **FILTRO** `ibs_20min` < `0.2692` → IC=-0.199 (n=91)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2692
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=275)

- **FILTRO** `ibs_20min` > `0.2576` → IC=-0.126 (n=2093)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2576
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=1032)

- **FILTRO** `sigma_ewma_delta_pct` > `8.655` → IC=-0.205 (n=337)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.655
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2788)

- **PATRÓN** `ibs_20min` > `0.7846` → IC=+0.224 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7846 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `1.6434` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6434 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` < `0.7056` → IC=+0.267 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7056 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` < `0.6528` → IC=+0.260 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6528 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` > `0.7776` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7776 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` < `0.0735` → IC=+0.307 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0735 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` < `2.2644` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2644 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.287 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.2576` → IC=+0.123 (n=1032)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.2576 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.6842` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6842 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` < `0.7131` → IC=+0.233 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7131 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` > `0.9027` → IC=+0.212 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9027 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1038` → IC=+0.227 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1038 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.253 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` < `2.4396` → IC=+0.261 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4396 (IC base=-0.044)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6458` → IC=-0.187 (n=534)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6458
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1605)

- **FILTRO** `ibs_20min` < `0.7037` → IC=-0.158 (n=1411)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7037
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=728)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.198 (n=399)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1740)

- **FILTRO** `ibs_20min` > `0.7708` → IC=-0.205 (n=791)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7708
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2374)

- **PATRÓN** `dist_vwap_pct` > `0.7824` → IC=+0.333 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7824 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2662` → IC=+0.316 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2662 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` < `0.9948` → IC=+0.287 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9948 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.306 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` < `0.1692` → IC=+0.291 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1692 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.306 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` < `1.3932` → IC=+0.304 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3932 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.7955` → IC=+0.296 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7955 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.8149` → IC=+0.280 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8149 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `0.7369` → IC=+0.244 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7369 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` > `1.2494` → IC=+0.294 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2494 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.276 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.1851` → IC=+0.249 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1851 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.4459` → IC=+0.248 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4459 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.197 (n=3189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0097 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.4717` → IC=+0.187 (n=8544)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4717 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.7508` → IC=+0.287 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7508 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.571` → IC=+0.155 (n=4523)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.571 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.686` → IC=+0.246 (n=3024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.686 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2979` → IC=+0.264 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2979 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4712` → IC=+0.239 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4712 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6883` → IC=+0.236 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6883 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.267 (n=5005)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.147 (n=3193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.009 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.5491` → IC=+0.151 (n=8412)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5491 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.2436` → IC=+0.239 (n=2603)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2436 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` < `0.7107` → IC=+0.239 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7107 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `1.2033` → IC=+0.248 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2033 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2467` → IC=+0.303 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2467 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.6141` → IC=+0.255 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6141 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `2.3325` → IC=+0.258 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3325 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.262 (n=3515)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.071)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.484` → IC=-0.169 (n=503)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.484
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1692)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.260 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8889 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.303` → IC=+0.163 (n=904)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.303 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2241` → IC=+0.270 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2241 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4401` → IC=+0.175 (n=275)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4401 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.1594` → IC=+0.186 (n=374)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.1594 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.173 (n=362)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 15.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1791` → IC=+0.477 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1791 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4624` → IC=+0.458 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4624 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.460 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.020)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.458 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8131` → IC=-0.147 (n=690)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8131
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=2074)

- **PATRÓN** `ibs_20min` > `0.8641` → IC=+0.159 (n=640)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.8641 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.169 (n=497)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6688` → IC=+0.159 (n=784)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6688 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.212 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.198 (n=286)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `248.0` → IC=+0.192 (n=374)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 248.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.1032` → IC=+0.220 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1032 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `0.6059` → IC=+0.212 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6059 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.0734` → IC=+0.208 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0734 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.4584` → IC=+0.222 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4584 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.231 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `481.0` → IC=+0.215 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 481.0 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.291 (n=505)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=1522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.248 (n=1521)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.742` → IC=+0.279 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.742 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.1385` → IC=+0.257 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1385 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `2.8983` → IC=+0.258 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8983 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.256 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `1939.2081` → IC=+0.253 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1939.2081 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.307 (n=798)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.5924` → IC=+0.283 (n=1197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5924 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.328 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` < `0.3388` → IC=+0.288 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3388 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.808` → IC=+0.299 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.808 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.3437` → IC=+0.306 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3437 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` < `1.6093` → IC=+0.283 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6093 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `2.7907` → IC=+0.288 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7907 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.291 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `1861.0222` → IC=+0.296 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1861.0222 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.291 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.282)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2817` → IC=-0.191 (n=464)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2817
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=1394)

- **FILTRO** `ibs_20min` > `0.7783` → IC=-0.184 (n=564)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7783
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=1696)

- **PATRÓN** `ibs_20min` > `0.8141` → IC=+0.159 (n=632)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.8141 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` > `0.4516` → IC=+0.220 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4516 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` < `0.9969` → IC=+0.233 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9969 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` > `0.5846` → IC=+0.205 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5846 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.249 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.5053` → IC=+0.257 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5053 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.255 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.204 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1534 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` < `0.6516` → IC=+0.193 (n=431)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.6516 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1607` → IC=+0.206 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1607 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.1651` → IC=+0.267 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1651 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8288` → IC=+0.251 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8288 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.1439` → IC=+0.252 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1439 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.243 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7176` → IC=-0.201 (n=1013)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7176
  - _Potencial_: sin este filtro IC_bueno=+0.277 (n=1014)

- **FILTRO** `ibs_20min` > `0.6897` → IC=-0.229 (n=532)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6897
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=1597)

- **FILTRO** `sigma_ewma_delta_pct` > `4.685` → IC=-0.177 (n=466)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.685
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=1663)

- **PATRÓN** `ibs_20min` > `0.7176` → IC=+0.277 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7176 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` > `0.302` → IC=+0.322 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.302 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.526` → IC=+0.159 (n=323)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.526 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.298 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8646 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.288 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6398 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` < `0.1034` → IC=+0.292 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1034 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2256` → IC=+0.292 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2256 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.4432` → IC=+0.319 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4432 (IC base=+0.038)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.311 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.038)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.210 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.2123` → IC=+0.224 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2123 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.7031` → IC=+0.259 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7031 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1552` → IC=+0.206 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1552 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.206 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.5012` → IC=+0.221 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5012 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.239 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0167` → IC=+0.317 (n=829)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0167 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.294 (n=577)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` > `0.63` → IC=+0.313 (n=1245)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.63 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2003` → IC=+0.320 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2003 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.503` → IC=+0.304 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.503 (IC base=+0.279)

- **PATRÓN** `volumen_regimen` > `0.8624` → IC=+0.305 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8624 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.322 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.291 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `2616.3452` → IC=+0.294 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2616.3452 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.296 (n=901)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.278 (n=476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.272 (n=670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.3985` → IC=+0.303 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3985 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` > `0.2887` → IC=+0.280 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2887 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` < `0.9429` → IC=+0.270 (n=1514)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9429 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.991` → IC=+0.294 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.991 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `1.241` → IC=+0.315 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.241 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2407` → IC=+0.338 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2407 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `1.543` → IC=+0.263 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.543 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.1642` → IC=+0.276 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1642 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `2604.596` → IC=+0.276 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2604.596 (IC base=+0.270)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.169 (n=2508)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.203 (n=2502)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0898` → IC=+0.186 (n=2502)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0898 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=7863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.5798` → IC=+0.217 (n=7504)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5798 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.1749` → IC=+0.194 (n=3323)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1749 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.267` → IC=+0.258 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.267 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.2168` → IC=+0.160 (n=4969)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2168 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.6283` → IC=+0.160 (n=4968)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6283 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2458` → IC=+0.194 (n=1514)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2458 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5622` → IC=+0.172 (n=3163)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5622 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.6293` → IC=+0.176 (n=2395)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6293 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2399.5624` → IC=+0.168 (n=5003)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2399.5624 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.181 (n=6418)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 117.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.181 (n=4747)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0066 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.207 (n=2377)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.206 (n=2389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.4773` → IC=+0.225 (n=7118)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4773 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.2292` → IC=+0.158 (n=5132)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2292 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.238` → IC=+0.191 (n=1211)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 10.238 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.150 (n=5172)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.1756 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2914` → IC=+0.222 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2914 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5701` → IC=+0.162 (n=2837)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5701 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.2636` → IC=+0.171 (n=2921)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2636 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `119.0` → IC=+0.171 (n=6081)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 119.0 (IC base=+0.167)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.218 (n=431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.187 (n=583)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0075 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3411` → IC=+0.207 (n=1280)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3411 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.198 (n=626)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.122` → IC=+0.311 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.122 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.233 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.180 (n=1181)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.238 (n=808)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.252 (n=821)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1831` → IC=+0.293 (n=612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1831 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.246 (n=828)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3437` → IC=+0.262 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3437 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.083` → IC=+0.252 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.083 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0953` → IC=+0.235 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0953 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.252 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.5076` → IC=+0.255 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5076 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1794.16` → IC=+0.249 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1794.16 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.240 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.0745` → IC=+0.201 (n=373)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0745 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=1180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.4118` → IC=+0.224 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4118 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.2078` → IC=+0.211 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2078 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.482` → IC=+0.237 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.482 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.162 (n=1117)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2653 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `1.0736` → IC=+0.167 (n=506)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0736 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.2324` → IC=+0.198 (n=246)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2324 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.4114` → IC=+0.194 (n=361)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4114 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `15841.68` → IC=+0.165 (n=506)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 15841.68 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.196 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0025 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.2886` → IC=+0.157 (n=1216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2886 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.173 (n=414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.5622` → IC=+0.183 (n=1216)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.5622 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.161 (n=1194)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.806` → IC=+0.209 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.806 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.153 (n=1216)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2116 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1578` → IC=+0.156 (n=373)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1578 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4267` → IC=+0.144 (n=1105)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4267 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `216.0` → IC=+0.165 (n=341)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 216.0 (IC base=+0.135)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.228 (n=420)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.2234` → IC=+0.215 (n=838)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2234 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.877` → IC=+0.274 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.877 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` < `0.2104` → IC=+0.198 (n=1217)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.2104 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.1335` → IC=+0.200 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1335 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.6453` → IC=+0.198 (n=398)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.6453 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.8829` → IC=+0.210 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8829 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `1943.141` → IC=+0.208 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1943.141 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.236 (n=1030)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.0942` → IC=+0.257 (n=344)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0942 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.280 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.2429` → IC=+0.256 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2429 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.718` → IC=+0.270 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.718 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3589` → IC=+0.273 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3589 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.2259` → IC=+0.229 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2259 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1871.1464` → IC=+0.225 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1871.1464 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.222 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.221)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.174 (n=1055)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0067 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.4315` → IC=+0.160 (n=1198)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4315 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.164 (n=1199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.3868` → IC=+0.198 (n=1198)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3868 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1585` → IC=+0.179 (n=810)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1585 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.868` → IC=+0.227 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.868 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.048` → IC=+0.149 (n=1055)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.048 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6319` → IC=+0.149 (n=1198)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6319 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.200 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.5356` → IC=+0.151 (n=516)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5356 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.5403` → IC=+0.172 (n=391)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5403 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `6954.443` → IC=+0.185 (n=799)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 6954.443 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.146 (n=1138)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 166.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.154 (n=1257)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0073 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.3834` → IC=+0.141 (n=1255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3834 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.182 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 18.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6258` → IC=+0.168 (n=1255)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6258 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.571` → IC=+0.132 (n=1440)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.571 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.878` → IC=+0.172 (n=443)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 6.878 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.8503` → IC=+0.144 (n=837)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8503 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2894` → IC=+0.196 (n=182)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2894 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.129 (n=758)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7982 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `9966.3147` → IC=+0.160 (n=569)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 9966.3147 (IC base=+0.121)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.148 (n=906)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0082 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=1396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5169` → IC=+0.202 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5169 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.836` → IC=+0.215 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.836 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.679` → IC=+0.252 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.679 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2233` → IC=+0.130 (n=1358)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2233 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.638` → IC=+0.121 (n=1357)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.638 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1645` → IC=+0.131 (n=1362)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1645 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.0711` → IC=+0.121 (n=570)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_pendiente_norm` > 0.0711 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4424` → IC=+0.145 (n=437)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4424 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1419)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2898.521` → IC=+0.194 (n=616)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2898.521 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.137 (n=1036)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 50.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.150 (n=603)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0061 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.103` → IC=+0.148 (n=456)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.103 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.207 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.7402` → IC=+0.138 (n=277)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.7402 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.1963` → IC=+0.135 (n=1243)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1963 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.434` → IC=+0.146 (n=283)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 7.434 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.6337` → IC=+0.133 (n=456)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.6337 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.173 (n=166)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `3082.2041` → IC=+0.157 (n=456)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3082.2041 (IC base=+0.111)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0188` → IC=+0.214 (n=865)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0188 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=1356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.203 (n=583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.7368` → IC=+0.261 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7368 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `1.341` → IC=+0.225 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.341 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.526` → IC=+0.245 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.526 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.2102` → IC=+0.205 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2102 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.8596` → IC=+0.224 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8596 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.234` → IC=+0.268 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.234 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.1508` → IC=+0.216 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1508 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.4095` → IC=+0.206 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4095 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.205 (n=1373)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2795.977` → IC=+0.206 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2795.977 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.234 (n=446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.212 (n=606)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.222 (n=447)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.223 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=615)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.247 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.1432` → IC=+0.228 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1432 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.8691` → IC=+0.204 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8691 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.349` → IC=+0.245 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.349 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6295` → IC=+0.216 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6295 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.288 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.2351` → IC=+0.192 (n=1052)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2351 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4476` → IC=+0.199 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4476 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2574.543` → IC=+0.208 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2574.543 (IC base=+0.204)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.161 (n=585)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0039 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.177 (n=586)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0089 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0992` → IC=+0.154 (n=584)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0992 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.5522` → IC=+0.188 (n=1565)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5522 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.3878` → IC=+0.185 (n=544)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.3878 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.692` → IC=+0.176 (n=810)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.692 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8743` → IC=+0.163 (n=1019)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8743 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `1.2097` → IC=+0.154 (n=510)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2097 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1633` → IC=+0.177 (n=484)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1633 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4373` → IC=+0.165 (n=562)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4373 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.5493` → IC=+0.160 (n=562)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5493 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.150 (n=1977)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `12247.1343` → IC=+0.150 (n=584)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 12247.1343 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.164 (n=1532)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 165.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.132 (n=1222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0057 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.120 (n=1233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 11.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.192 (n=611)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0588 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3375` → IC=+0.126 (n=442)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.3375 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.148 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 9.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` > `0.6659` → IC=+0.179 (n=294)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6659 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.158 (n=159)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.291` → IC=+0.127 (n=199)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 3.291 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.6182` → IC=+0.147 (n=148)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6182 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `12605.7065` → IC=+0.134 (n=394)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 12605.7065 (IC base=+0.103)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.206 (n=199)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.3374` → IC=+0.150 (n=589)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3374 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.6012` → IC=+0.179 (n=518)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6012 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.3005` → IC=+0.152 (n=616)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.3005 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.388` → IC=+0.155 (n=230)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 4.388 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `0.7202` → IC=+0.148 (n=526)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7202 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.1607` → IC=+0.204 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1607 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.1023` → IC=+0.152 (n=509)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1023 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.4187` → IC=+0.142 (n=579)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4187 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `332.0` → IC=+0.142 (n=490)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 332.0 (IC base=+0.131)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.265 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.213 (n=176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.219 (n=176)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.7033` → IC=+0.254 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7033 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.3876` → IC=+0.223 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3876 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.015` → IC=+0.234 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.015 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8419` → IC=+0.206 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8419 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `1.156` → IC=+0.219 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.156 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.2564` → IC=+0.323 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2564 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.3885` → IC=+0.233 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3885 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.405` → IC=+0.237 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.405 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `12307.7364` → IC=+0.208 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12307.7364 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.0811` → IC=+0.159 (n=162)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.0811 (IC base=+0.076)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4188` → IC=-0.129 (n=165)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4188
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=322)

- **FILTRO** `dist_vwap_pct` > `0.3335` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3335
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=452)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.171 (n=174)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0089 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.163 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 8.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.232 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.6296` → IC=+0.219 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6296 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.1` → IC=+0.202 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.1 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.0699` → IC=+0.141 (n=338)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.0699 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.288` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.288 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.2097` → IC=+0.167 (n=166)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.2097 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=417)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3060.3888` → IC=+0.200 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3060.3888 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.4188` → IC=+0.157 (n=322)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4188 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` < `1.5981` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5981 (IC base=+0.060)

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
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.207 (n=3187)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=10012)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.4721` → IC=+0.215 (n=9555)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4721 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.955` → IC=+0.207 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.955 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.61` → IC=+0.227 (n=4640)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.61 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8819` → IC=+0.164 (n=4261)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8819 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2403` → IC=+0.200 (n=1789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2403 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.6103` → IC=+0.189 (n=3057)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6103 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2342.0046` → IC=+0.171 (n=6370)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2342.0046 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.194 (n=7215)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 88.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.187 (n=7604)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0092 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1457` → IC=+0.188 (n=3803)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1457 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=3307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5657` → IC=+0.237 (n=8639)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5657 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.2444` → IC=+0.161 (n=5310)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2444 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.938` → IC=+0.197 (n=1214)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.938 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.72` → IC=+0.182 (n=8374)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.72 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.160 (n=2624)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7044 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `1.2044` → IC=+0.153 (n=1988)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.2044 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.241 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.8643` → IC=+0.188 (n=5264)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8643 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.191 (n=5011)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 48.0 (IC base=+0.180)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.208 (n=542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.217 (n=543)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3502` → IC=+0.189 (n=1626)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3502 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.198 (n=1093)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.322 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.999` → IC=+0.312 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.999 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.253 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.5813` → IC=+0.204 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5813 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.260 (n=1250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.264 (n=1117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1278` → IC=+0.288 (n=550)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1278 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=1133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3505` → IC=+0.289 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3505 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.458` → IC=+0.266 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.458 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.291 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `1.8654` → IC=+0.276 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8654 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1953.8` → IC=+0.273 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1953.8 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.191 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0028 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0842` → IC=+0.163 (n=511)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0842 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.3137` → IC=+0.201 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3137 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1314` → IC=+0.185 (n=885)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1314 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.171 (n=351)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.233` → IC=+0.150 (n=1374)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.233 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.628` → IC=+0.174 (n=511)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.628 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2695` → IC=+0.199 (n=217)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2695 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.1158` → IC=+0.160 (n=1299)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1158 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7596` → IC=+0.154 (n=984)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7596 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `15623.8467` → IC=+0.151 (n=694)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 15623.8467 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `478.0` → IC=+0.157 (n=1408)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 478.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1326)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.3183` → IC=+0.159 (n=1324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3183 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.173 (n=448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.149 (n=597)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.6508` → IC=+0.192 (n=1324)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6508 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.688` → IC=+0.154 (n=229)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.688 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.167 (n=1182)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1327 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.209` → IC=+0.155 (n=635)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.209 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.1862` → IC=+0.161 (n=1324)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1862 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1532` → IC=+0.196 (n=357)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1532 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4185` → IC=+0.167 (n=409)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4185 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.099` → IC=+0.161 (n=556)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.099 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `424.0` → IC=+0.156 (n=992)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 424.0 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.237 (n=1027)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=1621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=1564)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.6721` → IC=+0.255 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6721 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.811` → IC=+0.293 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.811 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.2118` → IC=+0.221 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2118 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.8557` → IC=+0.246 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8557 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.228 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.232 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.240 (n=1427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1629` → IC=+0.243 (n=628)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1629 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.237 (n=675)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3621` → IC=+0.269 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3621 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.722` → IC=+0.279 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.722 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3456` → IC=+0.291 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3456 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7665` → IC=+0.232 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7665 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2015` → IC=+0.238 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2015 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.245 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1868.6968` → IC=+0.247 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1868.6968 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.247 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.182 (n=549)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0035 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4353` → IC=+0.144 (n=1629)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4353 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=1711)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.8773` → IC=+0.260 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8773 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.5717` → IC=+0.170 (n=477)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.5717 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.157` → IC=+0.162 (n=675)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.157 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8772` → IC=+0.158 (n=1086)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8772 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.217 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5208` → IC=+0.149 (n=693)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5208 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7664` → IC=+0.149 (n=1049)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7664 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8151.5866` → IC=+0.230 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8151.5866 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.154 (n=504)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 80.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.155 (n=1324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0076 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4454` → IC=+0.153 (n=1323)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4454 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6936` → IC=+0.185 (n=1323)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6936 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.7968` → IC=+0.141 (n=1526)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.7968 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.233` → IC=+0.172 (n=196)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.233 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.145 (n=582)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.695 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1867` → IC=+0.143 (n=441)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1867 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.245 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.151 (n=1252)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `10960.0179` → IC=+0.209 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10960.0179 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `181.0` → IC=+0.142 (n=1248)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 181.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.134 (n=1078)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0081 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=613)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.189 (n=1614)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4722 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` > `1.0701` → IC=+0.202 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0701 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.442` → IC=+0.234 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.442 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.8919` → IC=+0.135 (n=1077)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8919 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=1627)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2913.9614` → IC=+0.246 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2913.9614 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.128 (n=1231)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 54.0 (IC base=+0.110)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.171 (n=530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0057 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.1302` → IC=+0.159 (n=528)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1302 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.122 (n=1639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.204 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.129 (n=1274)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.454` → IC=+0.124 (n=1530)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.454 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.72` → IC=+0.151 (n=698)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.72 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2267` → IC=+0.169 (n=246)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2267 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.5242` → IC=+0.127 (n=475)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.5242 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2851.5493` → IC=+0.164 (n=528)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2851.5493 (IC base=+0.111)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0194` → IC=+0.217 (n=1078)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0194 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1695)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.209 (n=1441)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.5146` → IC=+0.249 (n=1618)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5146 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.8993` → IC=+0.244 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8993 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.143` → IC=+0.269 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.143 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.6363` → IC=+0.216 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6363 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2346` → IC=+0.249 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2346 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.5119` → IC=+0.237 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5119 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.217 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2613.6699` → IC=+0.219 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2613.6699 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.225 (n=579)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.218 (n=579)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.207 (n=1228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.5207` → IC=+0.254 (n=1735)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5207 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `1.1781` → IC=+0.199 (n=297)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 1.1781 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.8782` → IC=+0.203 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8782 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.731` → IC=+0.262 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.731 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.238 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.262 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.2114` → IC=+0.192 (n=1366)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2114 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4357` → IC=+0.198 (n=1552)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4357 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=2888)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.159 (n=2449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0093 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.152 (n=2487)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0056 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.5243` → IC=+0.160 (n=2779)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5243 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.157 (n=934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 18.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.170 (n=959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 4.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.9415` → IC=+0.211 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9415 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1927` → IC=+0.158 (n=1011)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1927 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.5004` → IC=+0.142 (n=1648)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.5004 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.152` → IC=+0.181 (n=456)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 10.152 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.9013` → IC=+0.163 (n=1179)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.9013 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1729` → IC=+0.182 (n=762)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1729 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4565` → IC=+0.156 (n=916)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4565 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.8864` → IC=+0.162 (n=1830)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8864 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `3678.1703` → IC=+0.154 (n=1853)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3678.1703 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.194 (n=726)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3779` → IC=+0.160 (n=1916)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3779 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.164 (n=732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 4.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.184` → IC=+0.163 (n=958)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.184 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.6916` → IC=+0.149 (n=428)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.6916 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.208` → IC=+0.144 (n=2168)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.208 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2467` → IC=+0.140 (n=2076)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2467 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.144 (n=1010)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.4267` → IC=+0.144 (n=718)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4267 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.8118` → IC=+0.141 (n=1435)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.8118 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=2888)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `6935.3546` → IC=+0.150 (n=1946)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6935.3546 (IC base=+0.136)

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
- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.162 (n=853)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0044 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.124` → IC=+0.155 (n=285)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.124 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.172 (n=297)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 4.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5617` → IC=+0.155 (n=569)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5617 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.8892` → IC=+0.169 (n=285)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8892 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.9785` → IC=+0.167 (n=199)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.9785 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.4249` → IC=+0.164 (n=784)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.4249 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.676` → IC=+0.161 (n=854)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.676 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.7185` → IC=+0.156 (n=762)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7185 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.1125` → IC=+0.156 (n=783)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1125 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1738` → IC=+0.158 (n=252)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1738 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.2097` → IC=+0.159 (n=736)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.2097 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.5194` → IC=+0.154 (n=747)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5194 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=830)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.155 (n=716)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0084 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3946` → IC=+0.170 (n=629)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3946 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.153 (n=246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 4.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.1015` → IC=+0.154 (n=714)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.1015 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.6132` → IC=+0.169 (n=167)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.6132 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.3831` → IC=+0.143 (n=715)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.3831 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.738` → IC=+0.150 (n=115)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 10.738 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.281` → IC=+0.143 (n=650)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.281 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.6452` → IC=+0.165 (n=240)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6452 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.7259` → IC=+0.144 (n=638)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.7259 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.171 (n=302)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.153 (n=617)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.7747` → IC=+0.159 (n=467)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7747 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7593.8032` → IC=+0.166 (n=714)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 7593.8032 (IC base=+0.141)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.220 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9583 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.1983` → IC=+0.122 (n=141)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.1983 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.177` → IC=+0.196 (n=44)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.177 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.223 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` > `1.3923` → IC=+0.120 (n=193)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` > 1.3923 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `3417.5406` → IC=+0.146 (n=179)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3417.5406 (IC base=+0.091)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.140 (n=195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0068 (IC base=+0.102)

- **PATRÓN** `drift_60min` |x|≤ `0.3981` → IC=+0.144 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3981 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.144 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 10.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.1508` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1508 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.6259` → IC=+0.180 (n=98)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6259 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.747` → IC=+0.128 (n=111)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.747 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` < `0.1131` → IC=+0.156 (n=158)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1131 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3219.71` → IC=+0.140 (n=195)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3219.71 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.157 (n=164)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 55.0 (IC base=+0.102)

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

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.205 (n=378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.131 (n=799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 8.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.5536` → IC=+0.186 (n=762)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.5536 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1487` → IC=+0.158 (n=431)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1487 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.442` → IC=+0.219 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.442 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.210 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `2.098` → IC=+0.140 (n=573)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.098 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=614)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2432.8034` → IC=+0.150 (n=335)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2432.8034 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.256 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.0685` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0685 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.132 (n=207)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.5975 (IC base=-0.005)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.271 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.126 (n=292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` > `0.5717` → IC=+0.196 (n=261)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5717 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.1343` → IC=+0.185 (n=141)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1343 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `1.0669` → IC=+0.125 (n=230)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.0669 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `2.0198` → IC=+0.187 (n=196)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.0198 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=267)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `4019.6586` → IC=+0.143 (n=113)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4019.6586 (IC base=+0.109)

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

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.195 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0039 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.143 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.6869` → IC=+0.232 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6869 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1269` → IC=+0.153 (n=148)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1269 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.807` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.807 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.5886` → IC=+0.129 (n=87)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.5886 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `0.9612` → IC=+0.133 (n=118)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.9612 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.291` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.291 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `1.7354` → IC=+0.155 (n=140)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.7354 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=169)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `1774.3116` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 1774.3116 (IC base=+0.105)

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
- **FILTRO** `ibs_20min` > `0.0882` → IC=-0.278 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0882
  - _Potencial_: sin este filtro IC_bueno=+0.287 (n=45)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.134 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0055 (IC base=+0.076)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.120 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 7.0 (IC base=+0.076)

- **PATRÓN** `ibs_20min` > `0.6774` → IC=+0.174 (n=216)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.6774 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.198` → IC=+0.153 (n=142)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.198 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.244` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.244 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.0643` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0643 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.0852` → IC=+0.173 (n=99)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0852 (IC base=+0.076)

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

- **FILTRO** `dist_vwap_pct` > `0.338` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.338
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=131)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.291 (n=132)

- **FILTRO** `volumen_pendiente_norm` > `0.0765` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0765
  - _Potencial_: sin este filtro IC_bueno=-0.290 (n=60)

- **FILTRO** `volumen_spike_ratio` > `1.9996` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.9996
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=58)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=53)

- **FILTRO** `volumen_regimen` < `0.8127` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8127
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=51)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.292 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=46)

- **FILTRO** `drift_60min` |x|> `0.1081` → IC=-0.324 (n=32)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1081
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

- **FILTRO** `volumen_regimen` > `1.0011` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0011
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=52)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6568` → IC=-0.441 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=33)

- **FILTRO** `volumen_regimen` > `0.8808` → IC=-0.235 (n=32)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8808
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=33)

- **FILTRO** `volumen_regimen` > `0.5614` → IC=-0.361 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.5614
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=18)

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
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=224)

- **FILTRO** `dist_vwap_pct` > `0.6226` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6226
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=311)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.134 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0057 (IC base=+0.085)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.129 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 15.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.160 (n=242)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.6522 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.4857` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.4857 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.032)

- **PATRÓN** `libro_liquidez` > `3771.3449` → IC=+0.141 (n=115)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3771.3449 (IC base=+0.032)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=87)

- **FILTRO** `ibs_20min` < `0.5739` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5739
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=80)

- **FILTRO** `volumen_regimen` < `0.7797` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7797
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=80)

- **PATRÓN** `volumen_spike_ratio` > `1.4594` → IC=+0.139 (n=59)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4594 (IC base=-0.018)

- **PATRÓN** `ibs_20min` < `0.1218` → IC=+0.170 (n=101)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1218 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` < `0.1782` → IC=+0.140 (n=84)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.1782 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `2.9499` → IC=+0.128 (n=84)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.9499 (IC base=+0.093)

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
- **FILTRO** `volumen_pendiente_norm` < `0.0772` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0772
  - _Potencial_: sin este filtro IC_bueno=+0.262 (n=19)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.222 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.210 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.7083` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7083 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.379` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.379 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.166` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.166 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.06 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.050)

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

- **PATRÓN** `elapsed_s` > `190.7` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 190.7 (IC base=+0.189)

- **PATRÓN** `drift_15min` |x|≤ `2.0335` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.0335 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.6484` → IC=+0.292 (n=22)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6484 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `1508.0` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1508.0 (IC base=+0.189)

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

- **PATRÓN** `elapsed_s` > `190.7` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 190.7 (IC base=+0.189)

- **PATRÓN** `drift_15min` |x|≤ `2.0335` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.0335 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.6484` → IC=+0.292 (n=22)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6484 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `1508.0` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1508.0 (IC base=+0.189)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=652)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2892.6924` → IC=+0.167 (n=220)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2892.6924 (IC base=+0.107)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=652)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2892.6924` → IC=+0.167 (n=220)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2892.6924 (IC base=+0.107)

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
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=205)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=191)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=1650)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9583` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9583
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=76)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=60)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.167 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=62)

### LIQUIDACIONES_5M#BTC#5min
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

- **PATRÓN** `liq_n` > `18.0` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.038)

- **PATRÓN** `liq_usd_total` > `80598.37` → IC=+0.186 (n=84)

  - _Acción_: Kelly boost +0.93€ cuando `liq_usd_total` > 80598.37 (IC base=+0.038)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.495 (IC base=+0.038)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9842` → IC=-0.186 (n=33)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9842
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=100)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=737)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=427)

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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=134)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9164` → IC=-0.147 (n=49)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9164
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=101)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.122 (n=72)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=78)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=612)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=612)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=484)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=330)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=330)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=170)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=170)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.138 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=140)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.122 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=38)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=95)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=196)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=85)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=78)

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
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=120)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=7356)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.174 (n=3188)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=10179)

- **FILTRO** `py_entrada` > `0.595` → IC=-0.171 (n=3440)

  - _Acción_: SKIP cuando `py_entrada` > 0.595
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=10372)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.213 (n=566)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1741)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.173 (n=564)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=1911)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.202 (n=581)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=1773)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=605)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=1858)

- **FILTRO** `ibs_20min` > `0.2825` → IC=-0.163 (n=615)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2825
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1848)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.176 (n=554)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1736)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.182 (n=608)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1856)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2686)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=2845)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2851)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.135 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=350)

- **FILTRO** `ibs_20min` > `0.1742` → IC=-0.138 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1742
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=349)

- **FILTRO** `libro_liquidez` < `16888.8114` → IC=-0.142 (n=216)

  - _Acción_: SKIP cuando `libro_liquidez` < 16888.8114
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=649)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=232)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.253 (n=75)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=225)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=214)

- **FILTRO** `ballena_activa_n` > `116.0` → IC=-0.243 (n=68)

  - _Acción_: SKIP cuando `ballena_activa_n` > 116.0
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=207)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=749)

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
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=21355)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.274 (n=7466)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=23323)

- **FILTRO** `ibs_7min` < `0.29` → IC=-0.235 (n=7697)

  - _Acción_: SKIP cuando `ibs_7min` < 0.29
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=23092)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=10432)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=20357)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.230 (n=9508)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=28901)

- **FILTRO** `ibs_7min` > `0.2941` → IC=-0.180 (n=9583)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=28826)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.135 (n=1544)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=3526)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=1209)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3861)

- **FILTRO** `ibs_7min` < `0.7098` → IC=-0.252 (n=1673)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7098
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3397)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.184 (n=1177)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3893)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.262 (n=1638)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4974)

- **FILTRO** `drift_7min_pct` |x|> `0.1117` → IC=-0.124 (n=2245)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1117
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4367)

- **FILTRO** `ibs_7min` > `0.7945` → IC=-0.209 (n=1652)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7945
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=4960)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=1237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4093)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1281)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4049)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.191 (n=1332)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3998)

- **FILTRO** `ballena_activa_n` > `160.0` → IC=-0.171 (n=1327)

  - _Acción_: SKIP cuando `ballena_activa_n` > 160.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=4003)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.253 (n=1332)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=4040)

- **FILTRO** `ibs_7min` > `0.2602` → IC=-0.177 (n=1342)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2602
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=4030)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.188 (n=1335)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4037)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.172 (n=1174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=3627)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.309 (n=1170)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=3631)

- **FILTRO** `ibs_7min` < `0.1966` → IC=-0.259 (n=1200)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1966
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3601)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.215 (n=1128)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3673)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.238 (n=1631)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=5422)

- **FILTRO** `ibs_7min` > `0.7545` → IC=-0.177 (n=1763)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7545
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=5290)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.233 (n=1498)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=3580)

- **FILTRO** `ibs_7min` < `0.7425` → IC=-0.179 (n=1267)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7425
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3811)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.168 (n=1246)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3832)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.265 (n=1145)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4009)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.175 (n=1288)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3866)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.192 (n=1262)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3892)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.264 (n=1280)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=4111)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.241 (n=1327)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4064)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.179 (n=1751)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=5546)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.271 (n=1209)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3910)

- **FILTRO** `ibs_7min` < `0.7037` → IC=-0.228 (n=1277)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7037
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3842)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.212 (n=1230)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3889)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.204 (n=1686)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=5235)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1047)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=524)

- **FILTRO** `libro_liquidez` < `10599.4565` → IC=-0.146 (n=142)

  - _Acción_: SKIP cuando `libro_liquidez` < 10599.4565
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=428)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=759)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=323)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.138 (n=139)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=286)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=546)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.148 (n=478)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.153 (n=240)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 459.6089 (IC base=+0.116)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4386` → IC=+0.138 (n=56)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.4386 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `total_vol_5m` < `422.506` → IC=+0.140 (n=148)

  - _Acción_: Kelly boost +0.70€ cuando `total_vol_5m` < 422.506 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 12.0 (IC base=+0.133)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.121 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 10.0 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 13.0 (IC base=+0.096)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4131` → IC=+0.177 (n=97)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4131 (IC base=+0.095)

- **PATRÓN** `total_vol_5m` < `394.3776` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 394.3776 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 69.0 (IC base=+0.095)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.177 (n=125)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.189 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.143)

- **PATRÓN** `total_vol_5m` < `6272.013` → IC=+0.170 (n=110)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 6272.013 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 34.0 (IC base=+0.143)

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
- **FILTRO** `sigma_h` > `0.0055` → IC=-0.306 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=179)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `51.3763` → IC=-0.339 (n=54)

  - _Acción_: SKIP cuando `T_h` > 51.3763
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=56)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.167 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0053 (IC base=-0.143)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.167 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=43)

- **FILTRO** `T_h` < `39.9942` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `T_h` < 39.9942
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.232 (n=181)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=183)

- **FILTRO** `pct_vs_K` |x|> `3.3681` → IC=-0.434 (n=104)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3681
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=206)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `0.8662` → IC=-0.218 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 0.8662
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=45)

- **FILTRO** `T_h` < `96.6729` → IC=-0.368 (n=36)

  - _Acción_: SKIP cuando `T_h` < 96.6729
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=76)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `1.6258` → IC=-0.379 (n=64)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.6258
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=38)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.352 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=76)

- **FILTRO** `T_h` > `49.1198` → IC=-0.318 (n=75)

  - _Acción_: SKIP cuando `T_h` > 49.1198
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0144` → IC=-0.152 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0144
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=64)

- **FILTRO** `T_h` > `133.663` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `T_h` > 133.663
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **FILTRO** `pct_vs_K` |x|> `4.625` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.625
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=57)

- **FILTRO** `sigma_h` < `0.0148` → IC=-0.372 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0148
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `T_h` > `74.8914` → IC=-0.381 (n=40)

  - _Acción_: SKIP cuando `T_h` > 74.8914
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=21)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.131` → IC=+0.464 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.131 (IC base=+0.390)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.473 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.390)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.446 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.390)

- **PATRÓN** `dist_50` > `0.4444` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4444 (IC base=+0.390)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.466 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.390)

- **PATRÓN** `edge` > `0.1` → IC=+0.460 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.416)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.464 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.416)

- **PATRÓN** `T_h` < `0.6559` → IC=+0.455 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6559 (IC base=+0.416)

- **PATRÓN** `T_h` > `1.3776` → IC=+0.431 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.3776 (IC base=+0.416)

- **PATRÓN** `dist_50` > `0.4027` → IC=+0.484 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4027 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.462 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.416)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1535` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1535 (IC base=+0.402)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.380 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0088 (IC base=+0.402)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.450 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.402)

- **PATRÓN** `T_h` < `1.0863` → IC=+0.438 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0863 (IC base=+0.402)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.402)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.382 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.402)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.481)

- **PATRÓN** `sigma_h` < `0.0138` → IC=+0.471 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0138 (IC base=+0.481)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.471 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.481)

- **PATRÓN** `T_h` < `1.3025` → IC=+0.471 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.3025 (IC base=+0.481)

- **PATRÓN** `T_h` > `0.8566` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8566 (IC base=+0.481)

- **PATRÓN** `dist_50` > `0.376` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.376 (IC base=+0.481)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.463 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.481)

- **PATRÓN** `edge` > `0.1` → IC=+0.476 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.475)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.476 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.475)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.464 (n=81)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.475)

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
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=280)

- **PATRÓN** `streak_estiramiento` < `0.4763` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `streak_estiramiento` < 0.4763 (IC base=+0.023)

- **PATRÓN** `streak_estiramiento` < `0.4159` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4159 (IC base=+0.038)

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

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 34.0 (IC base=+0.057)

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
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=713)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=719)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=378)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=563)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1108)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=709)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=688)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=2794)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1431)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1439)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.227 (n=679)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.204 (n=660)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2136` → IC=+0.191 (n=500)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2136 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1267` → IC=+0.234 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1267 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.197 (n=1404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.188 (n=1506)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 16.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.6087` → IC=+0.264 (n=1497)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6087 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.2994` → IC=+0.191 (n=539)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2994 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.899` → IC=+0.273 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.899 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2980.6496` → IC=+0.193 (n=998)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2980.6496 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.210 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.188)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=530)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.209 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.290 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.197)

- **PATRÓN** `drift_15min` |x|≤ `0.3811` → IC=+0.206 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3811 (IC base=+0.197)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.237 (n=116)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.197)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.262 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.229 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.197)

- **PATRÓN** `ibs_15` > `0.7036` → IC=+0.263 (n=348)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7036 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.3935` → IC=+0.245 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3935 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.503` → IC=+0.251 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.503 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `15942.3752` → IC=+0.229 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15942.3752 (IC base=+0.197)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.889` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.889
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=343)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.144 (n=352)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0065 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.170 (n=234)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0051 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.0688` → IC=+0.156 (n=155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0688 (IC base=+0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2346` → IC=+0.172 (n=117)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.2346 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2561` → IC=+0.171 (n=247)

  - _Acción_: Kelly boost +0.85€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2561 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.165 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.6675` → IC=+0.240 (n=314)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6675 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.5575` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.5575 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1651` → IC=+0.161 (n=272)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1651 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.56` → IC=+0.203 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.56 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3462.5082` → IC=+0.155 (n=314)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3462.5082 (IC base=+0.143)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.294 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1511` → IC=+0.212 (n=161)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1511 (IC base=+0.173)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0669` → IC=+0.209 (n=163)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0669 (IC base=+0.173)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2717` → IC=+0.232 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2717 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.219 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.173)

- **PATRÓN** `ibs_15` > `0.6111` → IC=+0.257 (n=183)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6111 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.2696` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2696 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.786` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.786 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=141)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `3053.6476` → IC=+0.288 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3053.6476 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.230 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.173)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.7011` → IC=-0.150 (n=98)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.7011
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=818)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `16.21` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.21 (IC base=+0.019)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0237` → IC=+0.257 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0237 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0859` → IC=+0.204 (n=177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0859 (IC base=+0.186)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0605` → IC=+0.197 (n=361)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.0605 (IC base=+0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0898` → IC=+0.252 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0898 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=199)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.186)

- **PATRÓN** `ibs_15` > `0.5429` → IC=+0.282 (n=402)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5429 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.1302` → IC=+0.204 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1302 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.853` → IC=+0.217 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.853 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.396` → IC=+0.187 (n=359)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 7.396 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `2902.476` → IC=+0.279 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2902.476 (IC base=+0.186)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.158 (n=445)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1176 (IC base=+0.045)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.335 (n=264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.336)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.374 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.1082` → IC=+0.342 (n=264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1082 (IC base=+0.336)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.360 (n=263)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=+0.336)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.370 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.336)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.358 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.336)

- **PATRÓN** `ibs_15` > `0.7856` → IC=+0.379 (n=396)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7856 (IC base=+0.336)

- **PATRÓN** `dist_vwap_pct` > `0.4313` → IC=+0.380 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4313 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.188` → IC=+0.340 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.188 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.336 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.336)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.342 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `3532.3524` → IC=+0.352 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3532.3524 (IC base=+0.336)

- **PATRÓN** `ballena_activa_n` < `474.0` → IC=+0.358 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 474.0 (IC base=+0.336)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.348 (n=195)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.338)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.368 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.338)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.355 (n=74)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.338)

- **PATRÓN** `drift_15min` |x|≤ `0.4288` → IC=+0.350 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4288 (IC base=+0.338)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.347 (n=221)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.338)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.380 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.338)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.366 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.338)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.375 (n=222)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.338)

- **PATRÓN** `dist_vwap_pct` > `0.4016` → IC=+0.410 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4016 (IC base=+0.338)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.348 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.338)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.763` → IC=+0.341 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.763 (IC base=+0.338)

- **PATRÓN** `libro_liquidez` > `15670.1365` → IC=+0.342 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15670.1365 (IC base=+0.338)

- **PATRÓN** `ballena_activa_n` < `581.0` → IC=+0.386 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 581.0 (IC base=+0.338)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.378 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.329)

- **PATRÓN** `drift_60min` |x|≤ `0.1054` → IC=+0.340 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1054 (IC base=+0.329)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.349 (n=157)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.329)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.355 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.329)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.393 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.329)

- **PATRÓN** `ibs_15` > `0.7403` → IC=+0.386 (n=174)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7403 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` < `0.1256` → IC=+0.338 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1256 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.717` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.717 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.334 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.329)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.344 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.329)

- **PATRÓN** `libro_liquidez` > `3553.0968` → IC=+0.356 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3553.0968 (IC base=+0.329)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.338 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 166.0 (IC base=+0.329)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.013` → IC=-0.213 (n=629)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1891)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.187 (n=839)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1681)

- **FILTRO** `libro_liquidez` < `3915.9217` → IC=-0.134 (n=1663)

  - _Acción_: SKIP cuando `libro_liquidez` < 3915.9217
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=857)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.251 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.060)

- **PATRÓN** `ibs_15` > `0.6349` → IC=+0.266 (n=610)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6349 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` < `0.2752` → IC=+0.176 (n=477)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2752 (IC base=-0.060)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1175` → IC=+0.238 (n=1055)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1175 (IC base=-0.038)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1778` → IC=+0.235 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1778 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.276 (n=1582)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.6682` → IC=+0.288 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6682 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.219 (n=382)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=1148)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.229 (n=382)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1148)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.209 (n=974)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=556)

- **FILTRO** `sigma_ewma_delta_pct` > `19.574` → IC=-0.253 (n=273)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.574
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1257)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.169 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0028 (IC base=+0.074)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.276 (n=74)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.074)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.074)

- **PATRÓN** `ibs_15` > `0.7413` → IC=+0.312 (n=163)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7413 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.278 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.536` → IC=+0.268 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.536 (IC base=+0.074)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=371)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.189 (n=194)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0051 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.218 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.149)

- **PATRÓN** `drift_15min` |x|≤ `0.4253` → IC=+0.170 (n=98)

  - _Acción_: Kelly boost +0.85€ cuando `drift_15min` |x|≤ 0.4253 (IC base=+0.149)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1323` → IC=+0.158 (n=194)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.1323 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.241 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.6675` → IC=+0.261 (n=291)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6675 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.4741` → IC=+0.155 (n=85)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.4741 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.164` → IC=+0.176 (n=223)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.164 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.009` → IC=+0.159 (n=247)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 9.009 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=371)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11008.7835` → IC=+0.194 (n=132)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 11008.7835 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.239 (n=633)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.227)

- **PATRÓN** `drift_15min` |x|≤ `0.7826` → IC=+0.232 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7826 (IC base=+0.227)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2028` → IC=+0.251 (n=287)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2028 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.228 (n=252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=317)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.227)

- **PATRÓN** `ibs_15` < `0.2696` → IC=+0.282 (n=557)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2696 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.7515` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7515 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.065` → IC=+0.257 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.065 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.251` → IC=+0.229 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.251 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `3546.5572` → IC=+0.228 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3546.5572 (IC base=+0.227)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.225 (n=147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=442)

- **FILTRO** `drift_60min` |x|> `0.1682` → IC=-0.218 (n=200)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=389)

- **FILTRO** `drift_15min` |x|> `0.8847` → IC=-0.252 (n=147)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8847
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=442)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.162)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.162)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0761` → IC=+0.216 (n=259)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0761 (IC base=-0.045)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.260 (n=290)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` > `0.489` → IC=+0.203 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.489 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` < `0.199` → IC=+0.212 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.199 (IC base=-0.045)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.258 (n=374)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=375)

- **FILTRO** `drift_15min` |x|> `1.2211` → IC=-0.251 (n=187)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2211
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=562)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.263 (n=184)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=565)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1533` → IC=+0.274 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1533 (IC base=-0.047)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.103` → IC=+0.358 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.103 (IC base=-0.047)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.305 (n=433)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.047)

- **PATRÓN** `dist_vwap_pct` > `0.8607` → IC=+0.365 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8607 (IC base=-0.047)

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
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.292 (n=426)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.287 (n=289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.057` → IC=+0.319 (n=213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.057 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2389` → IC=+0.299 (n=212)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2389 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.343 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=670)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8411` → IC=+0.323 (n=637)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8411 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.1578` → IC=+0.319 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1578 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.327 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.290 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `13060.5836` → IC=+0.297 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13060.5836 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.317 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.284 (n=160)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.342 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.280)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.300 (n=118)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.280)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3729` → IC=+0.300 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3729 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.299 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.8305` → IC=+0.311 (n=353)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8305 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.4357` → IC=+0.354 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4357 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.355 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `16027.7188` → IC=+0.317 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16027.7188 (IC base=+0.280)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.305 (n=285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.298 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.226` → IC=+0.314 (n=95)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.226 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2866` → IC=+0.333 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2866 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.330 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8475` → IC=+0.336 (n=285)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8475 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.315 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.307 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2656` → IC=-0.186 (n=68)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2656
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=205)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1131` → IC=-0.171 (n=68)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1131
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=205)

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
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=107)

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
- **PATRÓN** `T_h` > `87.9957` → IC=+0.200 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9957 (IC base=+0.193)

- **PATRÓN** `ratio` < `0.9771` → IC=+0.466 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9771 (IC base=+0.193)

- **PATRÓN** `T_h` > `145.7851` → IC=+0.394 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7851 (IC base=+0.333)

- **PATRÓN** `ratio` > `1.008` → IC=+0.286 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.008 (IC base=+0.333)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `88.3739` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `T_h` < 88.3739 (IC base=+0.165)

- **PATRÓN** `T_h` > `144.0548` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `T_h` > 144.0548 (IC base=+0.165)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.165)

- **PATRÓN** `T_h` < `111.9952` → IC=+0.285 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9952 (IC base=+0.284)

- **PATRÓN** `T_h` > `98.314` → IC=+0.295 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 98.314 (IC base=+0.284)

- **PATRÓN** `ratio` > `1.0449` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0449 (IC base=+0.284)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `87.9936` → IC=+0.258 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9936 (IC base=+0.239)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.408 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.239)

- **PATRÓN** `T_h` > `102.672` → IC=+0.329 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 102.672 (IC base=+0.309)

- **PATRÓN** `ratio` > `1.01` → IC=+0.310 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.01 (IC base=+0.309)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1402` → IC=+0.455 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1402 (IC base=+0.403)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6087 sube el IC de +0.188 a +0.264 en UPDOWN_GBM#15min (n=1497). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7036 sube el IC de +0.197 a +0.263 en UPDOWN_GBM#BTC#15min (n=348). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6675 sube el IC de +0.143 a +0.240 en UPDOWN_GBM#ETH#15min (n=314). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6111 sube el IC de +0.173 a +0.257 en UPDOWN_GBM#SOL#15min (n=183). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5429 sube el IC de +0.186 a +0.282 en UPDOWN_GBM#XRP#15min (n=402). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.045 a +0.158 en UPDOWN_GBM#XRP#15min (n=445). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6349 sube el IC de -0.060 a +0.266 en UPDOWN_GBM_15M_TARDIO (n=610). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.038 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=1582). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7413 sube el IC de +0.074 a +0.312 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=163). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6675 sube el IC de +0.149 a +0.261 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=291). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2696 sube el IC de +0.227 a +0.282 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=557). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.162 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.045 a +0.260 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=290). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.047 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=433). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8411 sube el IC de +0.287 a +0.323 en UPDOWN_GBM_IBS_ALTO (n=637). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8305 sube el IC de +0.280 a +0.311 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=353). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8475 sube el IC de +0.295 a +0.336 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=285). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7856 sube el IC de +0.336 a +0.379 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=396). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.338 a +0.375 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=222). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7403 sube el IC de +0.329 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=174). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1273 | +0.095 | +175.55€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1273 | +0.095 | +175.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 943 | +0.104 | +149.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 943 | +0.104 | +149.77€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 244 | +0.049 | +7.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 244 | +0.049 | +7.13€ | 4 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 6 |
| ✅ BALLENAS_TARDIAS | 24166 | -0.090 | -3060.47€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1427 | -0.046 | -218.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 22739 | -0.093 | -2841.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3568 | -0.084 | -575.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3568 | -0.084 | -575.55€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1427 | -0.046 | -218.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1427 | -0.046 | -218.85€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 6943 | -0.023 | -599.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 6943 | -0.023 | -599.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6435 | -0.095 | -419.25€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6435 | -0.095 | -419.25€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5419 | -0.182 | -1086.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5419 | -0.182 | -1086.31€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 16824 | -0.030 | +4101.80€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4410 | -0.001 | +1830.02€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 12414 | -0.040 | +2271.78€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 16824 | -0.030 | +4101.80€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4410 | -0.001 | +1830.02€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 12414 | -0.040 | +2271.78€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1458 | -0.103 | -190.01€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 168 | -0.053 | -21.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1290 | -0.109 | -168.66€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 780 | -0.091 | -97.63€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 144 | -0.048 | -16.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 480 | -0.129 | -78.50€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 456 | -0.131 | -73.28€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 88644 | +0.113 | -4462.36€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 13514 | +0.185 | -424.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 353 | -0.094 | -49.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 68951 | +0.100 | -3786.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5826 | +0.109 | -202.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 11473 | +0.098 | -983.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 44 | -0.174 | -3.33€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 11414 | +0.100 | -968.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 17928 | +0.132 | -363.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4229 | +0.202 | -140.23€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 11428 | +0.112 | -176.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2229 | +0.106 | -24.95€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 11513 | +0.089 | -1072.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 51 | -0.085 | -5.77€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 11447 | +0.091 | -1055.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 18888 | +0.124 | -375.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5225 | +0.175 | -76.62€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 11546 | +0.106 | -239.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2105 | +0.098 | -51.39€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 17352 | +0.115 | -997.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3921 | +0.189 | -207.28€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 256 | -0.054 | +4.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 11683 | +0.092 | -668.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1492 | +0.127 | -126.17€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 11490 | +0.102 | -669.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 44 | -0.022 | +8.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 11433 | +0.102 | -678.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 14069 | +0.192 | -910.75€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 14069 | +0.192 | -910.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3371 | +0.169 | -354.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3371 | +0.169 | -354.90€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1095 | +0.194 | -8.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1095 | +0.194 | -8.31€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3311 | +0.182 | -277.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3311 | +0.182 | -277.51€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2965 | +0.238 | -95.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2965 | +0.238 | -95.38€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3248 | +0.195 | -188.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3248 | +0.195 | -188.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 664 | +0.429 | -18.95€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 664 | +0.429 | -18.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 254 | +0.434 | -4.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 254 | +0.434 | -4.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 249 | +0.436 | -2.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 249 | +0.436 | -2.52€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 153 | +0.403 | -10.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 153 | +0.403 | -10.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 48309 | +0.198 | -3749.14€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 48309 | +0.198 | -3749.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8368 | +0.176 | -973.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8368 | +0.176 | -973.07€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 7709 | +0.224 | -271.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 7709 | +0.224 | -271.69€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8338 | +0.174 | -989.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8338 | +0.174 | -989.80€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 7805 | +0.220 | -294.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 7805 | +0.220 | -294.80€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 7977 | +0.204 | -515.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 7977 | +0.204 | -515.15€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8112 | +0.194 | -704.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8112 | +0.194 | -704.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 18198 | +0.117 | +130.72€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 18198 | +0.117 | +130.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 9031 | +0.122 | +127.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 9031 | +0.122 | +127.77€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 9167 | +0.113 | +2.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 9167 | +0.113 | +2.95€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1415 | +0.292 | -3.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1415 | +0.292 | -3.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 631 | +0.279 | -13.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 631 | +0.279 | -13.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 680 | +0.296 | +8.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 680 | +0.296 | +8.18€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 104 | +0.340 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 104 | +0.340 | +1.79€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 618 | +0.439 | +0.86€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 618 | +0.439 | +0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 292 | +0.439 | +0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 292 | +0.439 | +0.19€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 286 | +0.441 | +0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 286 | +0.441 | +0.79€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 40 | +0.381 | -0.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 40 | +0.381 | -0.11€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1057 | +0.076 | -40.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 367 | +0.066 | -25.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 690 | +0.081 | -14.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 832 | +0.083 | -15.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 142 | +0.090 | -0.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 690 | +0.081 | -14.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 164 | +0.024 | -27.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 164 | +0.024 | -27.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 33389 | +0.097 | -1044.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2766 | +0.090 | +20.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 30623 | +0.098 | -1065.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 18803 | +0.102 | -308.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2766 | +0.090 | +20.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 16037 | +0.104 | -329.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 6191 | +0.105 | -56.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 6191 | +0.105 | -56.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 8395 | +0.081 | -679.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 8395 | +0.081 | -679.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 779 | +0.214 | -97.46€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 779 | +0.214 | -97.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 779 | +0.214 | -97.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 779 | +0.214 | -97.46€ | 2 | 4 |
| ✅ GBM_LATE_15M | 24146 | +0.081 | +11320.54€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 24146 | +0.081 | +11320.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4015 | +0.193 | +2907.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4015 | +0.193 | +2907.67€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 3587 | +0.175 | +2464.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3587 | +0.175 | +2464.61€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 4165 | +0.200 | +3130.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4165 | +0.200 | +3130.75€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 3584 | +0.016 | +695.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3584 | +0.016 | +695.53€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3491 | -0.034 | +797.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3491 | -0.034 | +797.82€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 5304 | -0.043 | +1324.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5304 | -0.043 | +1324.16€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 25497 | +0.084 | +13275.51€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 25497 | +0.084 | +13275.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4832 | +0.015 | +2591.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4832 | +0.015 | +2591.94€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5321 | +0.013 | +1077.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5321 | +0.013 | +1077.41€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3610 | +0.262 | +3630.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3610 | +0.262 | +3630.01€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4118 | +0.000 | +748.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4118 | +0.000 | +748.71€ | 2 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4156 | +0.026 | +1552.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4156 | +0.026 | +1552.39€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3460 | +0.274 | +3675.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3460 | +0.274 | +3675.06€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 19494 | +0.167 | +14402.32€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 19494 | +0.167 | +14402.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2928 | +0.205 | +2311.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2928 | +0.205 | +2311.88€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3108 | +0.147 | +2227.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3108 | +0.147 | +2227.26€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3047 | +0.209 | +2441.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3047 | +0.209 | +2441.59€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3270 | +0.133 | +2221.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3270 | +0.133 | +2221.55€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3630 | +0.114 | +2432.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3630 | +0.114 | +2432.96€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3511 | +0.203 | +2767.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3511 | +0.203 | +2767.07€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4776 | +0.124 | +1943.01€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4776 | +0.124 | +1943.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1372 | +0.119 | +601.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1372 | +0.119 | +601.98€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 369 | +0.147 | +180.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 369 | +0.147 | +180.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1349 | +0.140 | +579.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1349 | +0.140 | +579.70€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 998 | +0.094 | +287.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 998 | +0.094 | +287.62€ | 2 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 504 | +0.134 | +216.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 504 | +0.134 | +216.54€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 24258 | +0.174 | +17862.03€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 24258 | +0.174 | +17862.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3833 | +0.219 | +3203.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3833 | +0.219 | +3203.51€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3805 | +0.149 | +2491.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3805 | +0.149 | +2491.41€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3955 | +0.226 | +3412.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3955 | +0.226 | +3412.61€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3934 | +0.136 | +2629.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3934 | +0.136 | +2629.22€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4262 | +0.110 | +2633.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4262 | +0.110 | +2633.06€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4469 | +0.204 | +3492.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4469 | +0.204 | +3492.22€ | 0 | 23 |
| ✅ GBM_LATE_5M | 6608 | +0.144 | +3676.76€ | 1 | 27 |
| ✅ GBM_LATE_5M#5min | 6608 | +0.144 | +3676.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1691 | +0.139 | +1068.26€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1691 | +0.139 | +1068.26€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2089 | +0.147 | +1145.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2089 | +0.147 | +1145.52€ | 0 | 30 |
| ✅ GBM_LATE_5M#SOL | 526 | +0.097 | +165.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 526 | +0.097 | +165.59€ | 0 | 15 |
| ✅ GBM_LATE_5M#XRP | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1593 | +0.068 | +703.88€ | 3 | 12 |
| ✅ GBM_LATE_60M#60min | 1593 | +0.068 | +703.88€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 574 | +0.088 | +248.16€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 574 | +0.088 | +248.16€ | 0 | 14 |
| ✅ GBM_LATE_60M#ETH | 529 | +0.071 | +265.84€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 529 | +0.071 | +265.84€ | 2 | 18 |
| ✅ GBM_LATE_60M#SOL | 490 | +0.041 | +189.87€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 490 | +0.041 | +189.87€ | 1 | 12 |
| 🚫 GBM_LATE_60M_FADE | 355 | -0.259 | -26.23€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 355 | -0.259 | -26.23€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 136 | -0.225 | -11.33€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 136 | -0.225 | -11.33€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 117 | -0.265 | -9.64€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 117 | -0.265 | -9.64€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 102 | -0.288 | -5.26€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 102 | -0.288 | -5.26€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 659 | +0.058 | +122.71€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 659 | +0.058 | +122.71€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 259 | +0.048 | +42.89€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 259 | +0.048 | +42.89€ | 3 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 189 | +0.029 | -3.13€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 189 | +0.029 | -3.13€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 211 | +0.096 | +82.95€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 211 | +0.096 | +82.95€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN | 91 | +0.253 | +70.64€ | 0 | 8 |
| ✅ LATE_WINDOW_5MIN#5min | 91 | +0.253 | +70.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 91 | +0.253 | +70.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 91 | +0.253 | +70.64€ | 0 | 8 |
| ✅ LEADLAG_BTC_XRP_15M | 1807 | +0.097 | +484.72€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1807 | +0.097 | +484.72€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1807 | +0.097 | +484.72€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1807 | +0.097 | +484.72€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 372 | -0.083 | -35.15€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 372 | -0.083 | -35.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 94 | -0.062 | -5.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 94 | -0.062 | -5.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 130 | -0.030 | -5.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 130 | -0.030 | -5.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1848 | +0.006 | +18.34€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1848 | +0.006 | +18.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 96 | +0.000 | -2.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 96 | +0.000 | -2.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 201 | +0.003 | +15.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 201 | +0.003 | +15.26€ | 4 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 137 | -0.040 | -6.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 137 | -0.040 | -6.83€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 784 | +0.033 | +27.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 784 | +0.033 | +27.49€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 467 | -0.001 | -5.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 467 | -0.001 | -5.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 163 | -0.051 | -9.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 163 | -0.051 | -9.17€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M | 1037 | -0.050 | -32.69€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1037 | -0.050 | -32.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 295 | -0.042 | -12.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 295 | -0.042 | -12.66€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 346 | -0.043 | -7.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 346 | -0.043 | -7.38€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 396 | -0.060 | -12.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 396 | -0.060 | -12.65€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 299 | -0.018 | +3.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 141 | -0.004 | +6.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 158 | -0.031 | -3.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 7 | -0.019 | -0.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 85 | +0.052 | +13.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 39 | +0.061 | +6.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 46 | +0.042 | +7.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 51 | -0.047 | -3.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 26 | -0.071 | -3.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 25 | -0.018 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 48 | -0.060 | -3.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 22 | -0.042 | -0.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 26 | -0.071 | -2.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 41 | +0.012 | +2.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 21 | +0.109 | +7.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 20 | -0.091 | -4.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 67 | -0.065 | -6.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 29 | -0.081 | -4.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 38 | -0.050 | -2.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 14220 | -0.012 | -206.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14220 | -0.012 | -206.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2937 | -0.022 | -60.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2937 | -0.022 | -60.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 27179 | -0.008 | +1181.07€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 27179 | -0.008 | +1181.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4782 | +0.015 | +584.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4782 | +0.015 | +584.35€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4247 | -0.027 | -49.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4247 | -0.027 | -49.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4817 | +0.013 | +427.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4817 | +0.013 | +427.90€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4027 | -0.053 | -147.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4027 | -0.053 | -147.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4552 | -0.013 | +168.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4552 | -0.013 | +168.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4754 | +0.006 | +197.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4754 | +0.006 | +197.35€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5632 | -0.056 | -132.86€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5632 | -0.056 | -132.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1328 | -0.074 | -31.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1328 | -0.074 | -31.72€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 583 | -0.120 | -22.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 583 | -0.120 | -22.23€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1628 | -0.077 | -32.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1628 | -0.077 | -32.23€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 69198 | -0.073 | +1579.61€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 69198 | -0.073 | +1579.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 11682 | -0.080 | +632.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 11682 | -0.080 | +632.36€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 10702 | -0.094 | -487.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 10702 | -0.094 | -487.94€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 11854 | -0.068 | +637.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 11854 | -0.068 | +637.89€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 10232 | -0.093 | -139.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 10232 | -0.093 | -139.62€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 12688 | -0.049 | +362.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 12688 | -0.049 | +362.54€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 12040 | -0.062 | +574.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 12040 | -0.062 | +574.38€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7126 | -0.023 | -102.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7126 | -0.023 | -102.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1632 | -0.026 | -4.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1632 | -0.026 | -4.38€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1731 | -0.014 | -5.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1731 | -0.014 | -5.95€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1026 | -0.040 | -17.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1026 | -0.040 | -17.10€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1092 | +0.109 | +370.20€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 956 | +0.116 | +357.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 224 | +0.133 | +107.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 224 | +0.133 | +107.92€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 186 | +0.096 | +44.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 186 | +0.096 | +44.24€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 193 | +0.095 | +62.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 193 | +0.095 | +62.76€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 166 | +0.143 | +82.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 166 | +0.143 | +82.83€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 187 | +0.108 | +59.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 187 | +0.108 | +59.86€ | 0 | 5 |
| ✅ ORDER_FLOW_5M_REACTIVO | 422 | -0.052 | -41.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 422 | -0.052 | -41.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 92 | +0.000 | +4.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 92 | +0.000 | +4.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 54 | -0.125 | -15.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 54 | -0.125 | -15.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 118 | -0.075 | -22.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 118 | -0.075 | -22.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 85 | +0.017 | +4.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 85 | +0.017 | +4.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 73 | -0.100 | -13.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 73 | -0.100 | -13.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 542 | -0.101 | -35.89€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 249 | -0.149 | -53.42€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 201 | -0.195 | -56.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 48 | +0.040 | +2.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 188 | -0.084 | -0.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 144 | -0.096 | -9.02€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 44 | -0.043 | +8.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 105 | -0.014 | +18.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 83 | -0.029 | +11.72€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 428 | -0.130 | -53.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 674 | -0.209 | -32.15€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 277 | -0.199 | -27.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 240 | -0.194 | -27.18€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 235 | -0.226 | -22.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 203 | -0.237 | -26.74€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 162 | -0.195 | +17.51€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 146 | -0.196 | +12.84€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 589 | -0.211 | -41.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 268 | +0.411 | +209.26€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 71 | +0.377 | +57.18€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 71 | +0.377 | +57.18€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 169 | +0.482 | +156.84€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 169 | +0.482 | +156.84€ | 0 | 14 |
| ✅ RESOLUTION_SNIPER#sniper | 268 | +0.411 | +209.26€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 475 | +0.033 | +15.02€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 475 | +0.033 | +15.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 224 | +0.035 | +5.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 224 | +0.035 | +5.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 30 | +0.062 | +0.07€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 30 | +0.062 | +0.07€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 49 | -0.029 | -4.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 49 | -0.029 | -4.03€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 172 | +0.040 | +13.11€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 172 | +0.040 | +13.11€ | 2 | 4 |
| ✅ STREAK_FADE_5M | 2675 | -0.023 | -111.15€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2675 | -0.023 | -111.15€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 565 | -0.022 | -22.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 565 | -0.022 | -22.81€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1151 | -0.022 | -46.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1151 | -0.022 | -46.47€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 70 | -0.056 | -7.02€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 70 | -0.056 | -7.02€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 37 | -0.090 | -3.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 37 | -0.090 | -3.93€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 33 | -0.014 | -3.09€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 33 | -0.014 | -3.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7507 | +0.023 | +111.18€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7507 | +0.023 | +111.18€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2123 | +0.021 | +19.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2123 | +0.021 | +19.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1659 | +0.037 | +53.62€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1659 | +0.037 | +53.62€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2286 | +0.011 | +0.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2286 | +0.011 | +0.85€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1439 | +0.029 | +36.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1439 | +0.029 | +36.83€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7028 | +0.010 | -56.29€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7028 | +0.010 | -56.29€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2813 | +0.014 | -12.84€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2813 | +0.014 | -12.84€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2752 | +0.010 | -21.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2752 | +0.010 | -21.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1463 | +0.000 | -21.80€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1463 | +0.000 | -21.80€ | 2 | 0 |
| ✅ UPDOWN_GBM | 34290 | +0.030 | +2038.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 9264 | +0.064 | +1638.48€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1275 | +0.004 | +6.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 21540 | +0.021 | +367.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2078 | +0.009 | +25.99€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3367 | +0.067 | +359.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 547 | +0.150 | +217.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 29 | -0.016 | -0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2791 | +0.052 | +141.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 6363 | +0.034 | +418.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1176 | +0.080 | +250.88€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 348 | +0.020 | +7.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 3854 | +0.031 | +142.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 934 | +0.004 | +16.83€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 51 | -0.104 | +0.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4007 | +0.040 | +237.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 512 | +0.142 | +191.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 25 | -0.018 | -1.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3470 | +0.025 | +47.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 7298 | +0.019 | +290.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2417 | +0.045 | +270.78€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 336 | +0.006 | +7.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 3791 | +0.007 | +9.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 711 | +0.006 | -0.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 43 | -0.144 | +3.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 8269 | +0.016 | +213.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2305 | +0.024 | +154.09€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 330 | -0.006 | -3.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5164 | +0.014 | +55.68€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 433 | +0.024 | +9.66€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 37 | -0.167 | -2.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 4984 | +0.035 | +521.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2307 | +0.078 | +553.75€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 207 | -0.002 | -2.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2470 | -0.002 | -29.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 131 | -0.139 | +1.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 527 | +0.336 | +150.49€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 527 | +0.336 | +150.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 295 | +0.338 | +80.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 295 | +0.338 | +80.28€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 232 | +0.329 | +70.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 232 | +0.329 | +70.21€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 11201 | -0.043 | +2279.02€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 11201 | -0.043 | +2279.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 664 | -0.048 | +322.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 664 | -0.048 | +322.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2101 | -0.124 | +17.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2101 | -0.124 | +17.81€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 314 | +0.168 | +193.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 314 | +0.168 | +193.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1231 | +0.202 | +711.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1231 | +0.202 | +711.66€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3438 | -0.065 | +521.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3438 | -0.065 | +521.62€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3453 | -0.079 | +512.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3453 | -0.079 | +512.58€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 132 | +0.045 | +9.79€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 132 | +0.045 | +9.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 132 | +0.045 | +9.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 132 | +0.045 | +9.79€ | 2 | 3 |
| ✅ UPDOWN_GBM_IBS_ALTO | 849 | +0.287 | +674.39€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 849 | +0.287 | +674.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 470 | +0.280 | +345.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 470 | +0.280 | +345.65€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 379 | +0.295 | +328.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 379 | +0.295 | +328.74€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 705 | -0.107 | -79.69€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 705 | -0.107 | -79.69€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 198 | -0.065 | -11.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 198 | -0.065 | -11.77€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 69 | -0.162 | -8.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 69 | -0.162 | -8.81€ | 3 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 60 | -0.210 | -9.56€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 60 | -0.210 | -9.56€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 2280 | +0.300 | +1133.71€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 784 | +0.248 | +107.00€ | 0 | 6 |
| ✅ WEEKLY_PRICE#ETH | 845 | +0.287 | +348.98€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 651 | +0.376 | +677.73€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.017 n=464 — no justifica filtro, seguir monitorizando
  - _Datos_: n=464 IC=+0.017 PNL=+21.72€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 520 celda(s) pasan gate riguroso completo de 2181 evaluadas (n>=40) y 3181 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.024 < 0.08 — monitorear
  - _Datos_: n=2305 IC=+0.024 PNL=+154.09€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=845/15 IC=+0.287 PNL=+348.98€ | BTC: n=784/15 IC=+0.248 PNL=+107.00€ | SOL: n=651/15 IC=+0.376 PNL=+677.73€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.094 n=269/60 | contraria IC=+0.147 n=267 | gap=-0.053 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=272, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=711/40 IC=+0.006 PNL=-0.50€ | BTC#60min: n=934/40 IC=+0.004 PNL=+16.83€ | SOL#60min: n=433/40 IC=+0.024 PNL=+9.66€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.051 n=316914 | tras_1loss IC=+0.077 n=246739 | tras_2loss IC=+0.045 n=104421/40 | gap=+0.006 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.220 > 0.08 con n=366 PNL=+267.19€
  - _Datos_: n=366 IC=+0.220 PNL=+267.19€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.275 > 0.08 con n=38 PNL=+33.67€
  - _Datos_: n=38 IC=+0.275 PNL=+33.67€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.328 > 0.1 con n=1884 PNL=+1054.79€
  - _Datos_: n=1884 IC=+0.328 PNL=+1054.79€

**🟡 H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=264 PNL=+35.29€
  - _Datos_: n=264 IC=+0.086 PNL=+35.29€

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
  - _Estado_: n=1494 IC=+0.018 PNL=+17.18€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1494 IC=+0.018 PNL=+17.18€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=584 IC=-0.014 PNL=+8.80€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=584 IC=-0.014 PNL=+8.80€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=464 IC=+0.017 PNL=+21.72€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=464 IC=+0.017 PNL=+21.72€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.187 > 0.1 con n=1992 PNL=+1251.39€
  - _Datos_: n=1992 IC=+0.187 PNL=+1251.39€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1174 IC=+0.080 PNL=+250.38€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1174 IC=+0.080 PNL=+250.38€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.253 n=91) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=91 IC=+0.253 PNL=+70.64€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.02 con n=626 PNL=+248.25€
  - _Datos_: n=626 IC=+0.126 PNL=+248.25€

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
  - _Estado_: n=11872 IC=+0.057 PNL=+1495.87€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=11872 IC=+0.057 PNL=+1495.87€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.165 < -0.1 con n=216 PNL=+17.63€
  - _Datos_: n=216 IC=-0.165 PNL=+17.63€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1771 IC=+0.045 PNL=+181.60€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1771 IC=+0.045 PNL=+181.60€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=71 IC=-0.130 PNL=+3.08€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=71 IC=-0.130 PNL=+3.08€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.1 con n=378 PNL=+103.85€
  - _Datos_: n=378 IC=+0.126 PNL=+103.85€

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
  - _Estado_: n=16835 IC=-0.137 PNL=+1128.12€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=16835 IC=-0.137 PNL=+1128.12€

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
  - _Estado_: n=1827 IC=+0.138 PNL=+996.06€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1827 IC=+0.138 PNL=+996.06€

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
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.238 < -0.1 con n=1656 PNL=-183.41€
  - _Datos_: n=1656 IC=-0.238 PNL=-183.41€

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
  - _Estado_: 35/40 ops en el filtro definido (IC actual=-0.041 PNL=+2.93€)
  - _Datos_: n=35 IC=-0.041 PNL=+2.93€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.088 n=927) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=927 IC=+0.088 PNL=+209.37€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.412 n=430) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=430 IC=+0.412 PNL=+606.70€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=8364 IC=+0.176 PNL=-974.21€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8364 IC=+0.176 PNL=-974.21€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.1 con n=132 PNL=+75.67€
  - _Datos_: n=132 IC=+0.194 PNL=+75.67€
