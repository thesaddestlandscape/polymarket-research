# Hipótesis automáticas — 2026-09-22 20:49 UTC
_Generado por shadow_postmortem.py sobre 562782 resoluciones (PNL=+62820.06€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.252 (n=502)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=455)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.252 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.136)

- **PATRÓN** `n_total_lado` > `76.0` → IC=+0.208 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 76.0 (IC base=+0.136)

- **PATRÓN** `banda_hit_calibrado` > `0.8039` → IC=+0.251 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8039 (IC base=+0.136)

- **PATRÓN** `banda_z` > `9.862` → IC=+0.225 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.862 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=565)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4766.038` → IC=+0.152 (n=176)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4766.038 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.127 (n=159)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 96.0 (IC base=+0.041)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=399)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=328)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.258 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.145)

- **PATRÓN** `n_total_lado` > `71.0` → IC=+0.215 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 71.0 (IC base=+0.145)

- **PATRÓN** `banda_hit_calibrado` > `0.8017` → IC=+0.263 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8017 (IC base=+0.145)

- **PATRÓN** `banda_z` > `4.443` → IC=+0.172 (n=422)

  - _Acción_: Kelly boost +0.86€ cuando `banda_z` > 4.443 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.161 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=478)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.145)

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
- **FILTRO** `restante_s_al_confirmar` < `146.18` → IC=-0.231 (n=6765)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.18
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=20306)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `140.51` → IC=-0.236 (n=892)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.51
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2676)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `497.2` → IC=-0.145 (n=356)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 497.2
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1069)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `134.5` → IC=-0.279 (n=832)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 134.5
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2499)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `163.51` → IC=-0.227 (n=1605)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 163.51
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4816)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `124.33` → IC=-0.361 (n=1350)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.33
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=4052)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.48` → IC=-0.226 (n=377)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=377)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.180 (n=229)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=472)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=551)

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
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=187)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.183 (n=77)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=154)

- **FILTRO** `py_entrada` < `0.47` → IC=-0.167 (n=70)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=161)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.202 (n=13407)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3357)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5585.0055` → IC=+0.175 (n=2140)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 5585.0055 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=10836)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=13109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.233 (n=10406)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=5468)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `1668.6416` → IC=+0.157 (n=6172)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1668.6416 (IC base=+0.128)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.210 (n=1404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1618)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.352 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2030)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `15809.9496` → IC=+0.230 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15809.9496 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.203 (n=1458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.263 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=2059)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `13909.3637` → IC=+0.208 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13909.3637 (IC base=+0.199)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=2306)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.334 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.245 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.356 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.239 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.234)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.153 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=569)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.230 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=516)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `1302.9991` → IC=+0.151 (n=629)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1302.9991 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.236 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.432 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.169 (n=1049)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 7.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.165 (n=565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 7.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` < `0.27` → IC=+0.313 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.27 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=710)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.165)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=297)
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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=10949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=10468)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.224 (n=3693)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=2535)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.184 (n=1850)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.263 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.250 (n=743)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.250)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.356 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.250)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=2481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=2501)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.188 (n=1131)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.73 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=2337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.318 (n=824)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=2542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=2444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.199 (n=1860)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.195)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.431 (n=449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.470 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `2060.1801` → IC=+0.438 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2060.1801 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.435 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.434 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=32470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.232 (n=17593)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=6602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=5569)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=6029)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.228 (n=5813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.227 (n=5795)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.277 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.180 (n=5572)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=5931)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=2918)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.264 (n=2033)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.211 (n=5373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.255 (n=2188)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=5437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=5399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2093)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=4977)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.14` → IC=+0.128 (n=4552)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.14 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.140 (n=4870)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.132 (n=5993)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.03` → IC=+0.142 (n=4541)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.03 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.200 (n=2509)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.122)

- **PATRÓN** `restante_min` < `4.09` → IC=+0.132 (n=2256)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` < 4.09 (IC base=+0.122)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.140 (n=2412)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.141 (n=2593)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 6.0 (IC base=+0.122)

- **PATRÓN** `lag_apertura_s` < `3.46` → IC=+0.145 (n=2259)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.46 (IC base=+0.122)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=2468)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` < `4.18` → IC=+0.125 (n=2292)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.18 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.137 (n=2465)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.32` → IC=+0.140 (n=2298)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.32 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.322 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.386 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1560.0097` → IC=+0.298 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1560.0097 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.301 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.341 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `4209.1188` → IC=+0.301 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4209.1188 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.335 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.297 (n=510)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.386 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1466.4356` → IC=+0.314 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1466.4356 (IC base=+0.297)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4749` → IC=+0.121 (n=7629)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.4749 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.9831` → IC=+0.241 (n=2543)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9831 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.834` → IC=+0.246 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.834 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.6292` → IC=+0.245 (n=2115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6292 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.931` → IC=+0.177 (n=2946)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 5.931 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `1.0481` → IC=+0.256 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0481 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.3054` → IC=+0.215 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3054 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.9086` → IC=+0.206 (n=3464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9086 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.5702` → IC=+0.131 (n=9186)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5702 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.5935` → IC=+0.192 (n=703)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.5935 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` < `0.1486` → IC=+0.172 (n=2841)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1486 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` < `0.6997` → IC=+0.176 (n=1398)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6997 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` > `0.8705` → IC=+0.175 (n=2117)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8705 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.168` → IC=+0.219 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.168 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` > `1.5762` → IC=+0.200 (n=4740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5762 (IC base=+0.062)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.210 (n=5088)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.062)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.179 (n=578)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.005 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.171 (n=578)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0082 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3452` → IC=+0.165 (n=1728)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3452 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.172 (n=1154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.117` → IC=+0.271 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.117 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.211 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.164 (n=1613)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.251 (n=1143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.288 (n=427)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=1160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.062` → IC=+0.293 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.062 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.39` → IC=+0.249 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.39 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0914` → IC=+0.231 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0914 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.263 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.6401` → IC=+0.245 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6401 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1788.08` → IC=+0.240 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1788.08 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.230 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.235 (n=582)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.251 (n=439)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=1318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.9902` → IC=+0.264 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9902 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.1987` → IC=+0.222 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1987 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.579` → IC=+0.218 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.579 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.83` → IC=+0.250 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.83 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.2525` → IC=+0.217 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2525 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `1.0825` → IC=+0.225 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0825 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.229 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.4011` → IC=+0.225 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4011 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.3728` → IC=+0.220 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3728 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `12276.9296` → IC=+0.218 (n=1176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12276.9296 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.174 (n=458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.159 (n=456)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6849` → IC=+0.170 (n=1367)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6849 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1279` → IC=+0.158 (n=1209)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1279 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.208` → IC=+0.159 (n=221)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.208 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.208` → IC=+0.141 (n=1244)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.208 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.149 (n=1367)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2044 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.8523` → IC=+0.139 (n=911)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.8523 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0963` → IC=+0.171 (n=494)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0963 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.150 (n=1257)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.77` → IC=+0.145 (n=838)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.77 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.147 (n=1177)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 411.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.217 (n=563)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=1686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=1505)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.142` → IC=+0.256 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.142 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.2115` → IC=+0.190 (n=1673)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.2115 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.3629` → IC=+0.201 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3629 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.8806` → IC=+0.206 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8806 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.197 (n=1175)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.02 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `1944.5584` → IC=+0.189 (n=561)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 1944.5584 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.222 (n=1435)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.5811` → IC=+0.215 (n=1435)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5811 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=673)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.0636` → IC=+0.241 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0636 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.55` → IC=+0.238 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.55 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3585` → IC=+0.264 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3585 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.8718` → IC=+0.227 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8718 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `1866.1532` → IC=+0.226 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1866.1532 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.216 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.214)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.156 (n=94)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2110)

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

- **PATRÓN** `dist_vwap_pct` > `0.661` → IC=+0.190 (n=140)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.661 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.158 (n=516)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8521 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2244` → IC=+0.209 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2244 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `1.5138` → IC=+0.174 (n=643)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.5138 (IC base=+0.012)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.161 (n=57)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=309)

- **FILTRO** `ibs_20min` < `0.2692` → IC=-0.199 (n=91)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2692
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=275)

- **FILTRO** `ibs_20min` > `0.2581` → IC=-0.126 (n=2088)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2581
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=1031)

- **FILTRO** `sigma_ewma_delta_pct` > `8.667` → IC=-0.204 (n=336)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.667
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2783)

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

- **PATRÓN** `ibs_20min` < `0.2581` → IC=+0.122 (n=1031)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.2581 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.68` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.68 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` < `0.4301` → IC=+0.210 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4301 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` < `1.1044` → IC=+0.220 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1044 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` > `0.9031` → IC=+0.211 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9031 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1022` → IC=+0.226 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1022 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.1582` → IC=+0.241 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1582 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` < `2.4396` → IC=+0.260 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4396 (IC base=-0.044)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6469` → IC=-0.187 (n=532)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6469
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1600)

- **FILTRO** `ibs_20min` < `0.7025` → IC=-0.157 (n=1407)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7025
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=725)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.198 (n=399)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1733)

- **FILTRO** `ibs_20min` > `0.7727` → IC=-0.205 (n=789)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7727
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2368)

- **PATRÓN** `dist_vwap_pct` > `0.7625` → IC=+0.309 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7625 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2654` → IC=+0.319 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2654 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.304 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.305 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` < `1.5219` → IC=+0.297 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5219 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.7955` → IC=+0.295 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7955 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.8075` → IC=+0.271 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8075 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `0.7407` → IC=+0.244 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7407 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.288 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1041` → IC=+0.271 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1041 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.1777` → IC=+0.251 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1777 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.4444` → IC=+0.247 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4444 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.198 (n=3181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0097 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.4717` → IC=+0.187 (n=8526)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4717 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `1.0665` → IC=+0.292 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0665 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.571` → IC=+0.156 (n=4513)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.571 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6862` → IC=+0.245 (n=3015)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6862 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2977` → IC=+0.264 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2977 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4711` → IC=+0.239 (n=1827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4711 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6883` → IC=+0.236 (n=1826)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6883 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.267 (n=4989)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.147 (n=3181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.009 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.55` → IC=+0.151 (n=8400)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.55 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.2434` → IC=+0.239 (n=2602)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2434 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` < `0.7129` → IC=+0.237 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7129 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `1.2035` → IC=+0.248 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2035 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2466` → IC=+0.301 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2466 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.4857` → IC=+0.255 (n=1212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4857 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `2.3311` → IC=+0.257 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3311 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.262 (n=3506)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.071)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.493` → IC=-0.169 (n=502)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.493
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1692)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.260 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8889 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.299` → IC=+0.164 (n=902)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.299 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2239` → IC=+0.270 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2239 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4401` → IC=+0.175 (n=275)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4401 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.1594` → IC=+0.186 (n=374)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.1594 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.173 (n=362)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 15.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1791` → IC=+0.477 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1791 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4624` → IC=+0.458 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4624 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.458 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.021)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.458 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8636` → IC=+0.158 (n=639)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.8636 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1246` → IC=+0.169 (n=496)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1246 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6702` → IC=+0.158 (n=782)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6702 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.212 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.200 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4208 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `248.0` → IC=+0.190 (n=372)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 248.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.1592` → IC=+0.218 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1592 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `0.6093` → IC=+0.211 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6093 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.209 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2731` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2731 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.4573` → IC=+0.227 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4573 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.229 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1598 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `481.0` → IC=+0.214 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 481.0 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.286 (n=684)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=1517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.250 (n=1340)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.741` → IC=+0.282 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.741 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.1384` → IC=+0.257 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1384 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `2.898` → IC=+0.259 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.898 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.257 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `1937.8734` → IC=+0.253 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1937.8734 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.307 (n=797)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.5933` → IC=+0.283 (n=1194)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5933 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.328 (n=406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` < `0.2262` → IC=+0.286 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2262 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.808` → IC=+0.298 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.808 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.3432` → IC=+0.305 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3432 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` < `1.6079` → IC=+0.283 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6079 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `2.7879` → IC=+0.288 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7879 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.291 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `1919.06` → IC=+0.300 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.06 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.290 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.282)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2815` → IC=-0.190 (n=463)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2815
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=1392)

- **FILTRO** `ibs_20min` > `0.7783` → IC=-0.183 (n=563)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7783
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=1691)

- **PATRÓN** `ibs_20min` > `0.9075` → IC=+0.180 (n=464)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.9075 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.223 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.9978` → IC=+0.230 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9978 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `0.5819` → IC=+0.204 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5819 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.0791` → IC=+0.250 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0791 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `1.5025` → IC=+0.256 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5025 (IC base=+0.008)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.253 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.203 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1534 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` < `0.6579` → IC=+0.193 (n=431)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.6579 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1615` → IC=+0.203 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1615 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8288` → IC=+0.251 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8288 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.1499` → IC=+0.250 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1499 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.242 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7143` → IC=-0.204 (n=1004)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=+0.275 (n=1019)

- **FILTRO** `ibs_20min` > `0.6901` → IC=-0.230 (n=531)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6901
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=1594)

- **FILTRO** `sigma_ewma_delta_pct` > `4.678` → IC=-0.179 (n=465)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.678
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=1660)

- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.275 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7143 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` > `0.3001` → IC=+0.321 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3001 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.526` → IC=+0.157 (n=322)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.526 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.297 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8646 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` > `0.6396` → IC=+0.288 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6396 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` < `0.1034` → IC=+0.291 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1034 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.2256` → IC=+0.292 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2256 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `1.443` → IC=+0.318 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.443 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.311 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.037)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.209 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.2123` → IC=+0.224 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2123 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.7014` → IC=+0.257 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7014 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1552` → IC=+0.206 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1552 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.209 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.5012` → IC=+0.221 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5012 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.240 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0166` → IC=+0.319 (n=828)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0166 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.294 (n=577)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` > `0.6316` → IC=+0.313 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6316 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2002` → IC=+0.321 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2002 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.503` → IC=+0.304 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.503 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `0.8627` → IC=+0.305 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8627 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.322 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.1646` → IC=+0.290 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1646 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.285 (n=1318)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2616.2022` → IC=+0.295 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2616.2022 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.296 (n=900)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.277 (n=473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.272 (n=670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.3985` → IC=+0.303 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3985 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` > `0.2886` → IC=+0.279 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2886 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` < `0.9381` → IC=+0.270 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9381 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.991` → IC=+0.294 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.991 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `1.2419` → IC=+0.314 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2419 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.337 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `1.5411` → IC=+0.263 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5411 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.1632` → IC=+0.275 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1632 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `2603.4728` → IC=+0.275 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2603.4728 (IC base=+0.270)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.169 (n=2500)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.204 (n=2498)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.09` → IC=+0.185 (n=2499)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.09 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=7844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.5791` → IC=+0.217 (n=7490)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5791 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.1743` → IC=+0.195 (n=3312)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1743 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.266` → IC=+0.259 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.266 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.160 (n=4961)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2177 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.160 (n=4961)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6285 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2456` → IC=+0.195 (n=1511)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2456 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5621` → IC=+0.172 (n=3156)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5621 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.6286` → IC=+0.175 (n=2391)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6286 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2399.5624` → IC=+0.168 (n=4993)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2399.5624 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.181 (n=6403)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 117.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.181 (n=4741)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0066 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.207 (n=2372)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.206 (n=2369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` < `0.4773` → IC=+0.225 (n=7103)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4773 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.158 (n=5129)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2288 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.239` → IC=+0.191 (n=1210)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 10.239 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `1.1764` → IC=+0.150 (n=5162)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.1764 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.220 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.569` → IC=+0.163 (n=2829)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.569 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.2625` → IC=+0.170 (n=2915)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2625 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `119.0` → IC=+0.171 (n=6066)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 119.0 (IC base=+0.166)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.217 (n=429)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.186 (n=580)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0076 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3413` → IC=+0.206 (n=1279)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3413 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.198 (n=626)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.122` → IC=+0.311 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.122 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.234 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.180 (n=1179)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.238 (n=804)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.252 (n=820)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1839` → IC=+0.294 (n=610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1839 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.246 (n=824)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3437` → IC=+0.262 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3437 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.073` → IC=+0.252 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.073 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0953` → IC=+0.236 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0953 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.252 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `2.2616` → IC=+0.245 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2616 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1793.28` → IC=+0.248 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1793.28 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.242 (n=374)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.0751` → IC=+0.203 (n=372)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0751 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=1177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.4097` → IC=+0.224 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4097 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.2074` → IC=+0.212 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2074 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.482` → IC=+0.237 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.482 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.162 (n=1114)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2653 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `1.0742` → IC=+0.167 (n=505)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0742 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.2324` → IC=+0.200 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2324 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.193 (n=360)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `15840.9937` → IC=+0.167 (n=505)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 15840.9937 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.155 (n=1213)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0057 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.2896` → IC=+0.157 (n=1213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2896 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.172 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.5606` → IC=+0.182 (n=1213)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.5606 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1331` → IC=+0.161 (n=1194)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1331 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.828` → IC=+0.209 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.828 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.2129` → IC=+0.153 (n=1213)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2129 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1575` → IC=+0.155 (n=372)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1575 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4292` → IC=+0.143 (n=1102)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4292 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.164 (n=340)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 218.0 (IC base=+0.135)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.227 (n=569)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.2236` → IC=+0.216 (n=835)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2236 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.876` → IC=+0.279 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.876 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.2104` → IC=+0.199 (n=1212)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.2104 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.1335` → IC=+0.202 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1335 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.6453` → IC=+0.199 (n=396)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.6453 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.8829` → IC=+0.211 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8829 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `1941.8048` → IC=+0.205 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1941.8048 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.237 (n=1027)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.0941` → IC=+0.257 (n=343)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0941 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.281 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.2429` → IC=+0.256 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2429 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.704` → IC=+0.267 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.704 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3581` → IC=+0.266 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3581 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.2254` → IC=+0.229 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2254 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1870.8984` → IC=+0.222 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1870.8984 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.222 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.221)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.210 (n=401)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.4318` → IC=+0.160 (n=1197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4318 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.164 (n=1197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.3868` → IC=+0.197 (n=1197)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3868 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1571` → IC=+0.179 (n=809)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1571 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.884` → IC=+0.227 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.884 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.048` → IC=+0.149 (n=1053)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.048 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6318` → IC=+0.150 (n=1197)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6318 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2466` → IC=+0.201 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2466 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.5356` → IC=+0.151 (n=516)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5356 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.5331` → IC=+0.172 (n=391)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5331 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `6960.2205` → IC=+0.185 (n=798)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 6960.2205 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.146 (n=1136)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 166.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.153 (n=1255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0073 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.3836` → IC=+0.140 (n=1254)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3836 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.181 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 18.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6259` → IC=+0.168 (n=1254)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6259 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.1585` → IC=+0.142 (n=1204)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1585 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.878` → IC=+0.171 (n=442)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 6.878 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.849` → IC=+0.144 (n=836)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.849 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.194 (n=181)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.7931` → IC=+0.129 (n=757)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7931 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `9950.2818` → IC=+0.160 (n=569)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 9950.2818 (IC base=+0.121)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.5652` → IC=-0.180 (n=454)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5652
  - _Potencial_: sin este filtro IC_bueno=+0.207 (n=1363)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.147 (n=903)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0082 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=1393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.5169` → IC=+0.202 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5169 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.8344` → IC=+0.215 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8344 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.679` → IC=+0.252 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.679 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.2233` → IC=+0.129 (n=1355)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2233 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `0.6379` → IC=+0.120 (n=1355)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` > 0.6379 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1645` → IC=+0.130 (n=1359)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1645 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.144 (n=436)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1416)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2897.8254` → IC=+0.194 (n=615)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2897.8254 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.136 (n=1033)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 50.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.148 (n=601)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0061 (IC base=+0.110)

- **PATRÓN** `drift_60min` |x|≤ `0.1031` → IC=+0.148 (n=455)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1031 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.207 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` > `0.9737` → IC=+0.139 (n=189)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.9737 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` < `0.1963` → IC=+0.135 (n=1243)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1963 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.445` → IC=+0.146 (n=283)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 7.445 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.6341` → IC=+0.132 (n=455)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.6341 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.4556` → IC=+0.128 (n=406)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.4556 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` > `2.4253` → IC=+0.124 (n=405)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.4253 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `3081.0348` → IC=+0.157 (n=455)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3081.0348 (IC base=+0.110)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0188` → IC=+0.215 (n=864)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0188 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=1353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.203 (n=583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.7368` → IC=+0.261 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7368 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `1.3338` → IC=+0.228 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3338 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.525` → IC=+0.246 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.525 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.2103` → IC=+0.205 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2103 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.8598` → IC=+0.224 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8598 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.271 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.1481` → IC=+0.215 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1481 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.208 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.205 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2796.6944` → IC=+0.205 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2796.6944 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.236 (n=445)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.212 (n=605)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.220 (n=445)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.222 (n=653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=615)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.246 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `1.1415` → IC=+0.225 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1415 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.8635` → IC=+0.204 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8635 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.355` → IC=+0.245 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.355 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6303` → IC=+0.216 (n=1334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6303 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.288 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.2298` → IC=+0.191 (n=1050)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2298 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4468` → IC=+0.199 (n=1193)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4468 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2574.4443` → IC=+0.206 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2574.4443 (IC base=+0.203)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.160 (n=584)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0039 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.177 (n=586)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0089 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1344` → IC=+0.153 (n=770)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1344 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=889)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.5522` → IC=+0.188 (n=1563)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5522 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.3876` → IC=+0.186 (n=543)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3876 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.692` → IC=+0.176 (n=809)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.692 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8753` → IC=+0.163 (n=1018)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8753 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.21` → IC=+0.156 (n=509)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.21 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1634` → IC=+0.178 (n=483)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1634 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4373` → IC=+0.164 (n=561)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4373 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5495` → IC=+0.161 (n=561)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5495 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.150 (n=1974)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `12247.1343` → IC=+0.150 (n=583)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 12247.1343 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.164 (n=1529)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 165.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.131 (n=1219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0057 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.0577` → IC=+0.191 (n=610)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0577 (IC base=+0.101)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3375` → IC=+0.125 (n=441)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.3375 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.147 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 9.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` > `0.2517` → IC=+0.141 (n=441)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.2517 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.3052` → IC=+0.156 (n=158)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3052 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.264` → IC=+0.125 (n=198)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 3.264 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.6182` → IC=+0.144 (n=147)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6182 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `12416.0462` → IC=+0.134 (n=394)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 12416.0462 (IC base=+0.103)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.205 (n=198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3378` → IC=+0.150 (n=586)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3378 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.144 (n=526)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6012` → IC=+0.179 (n=515)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6012 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.2995` → IC=+0.153 (n=614)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2995 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.388` → IC=+0.154 (n=229)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.388 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `1.0619` → IC=+0.164 (n=266)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.0619 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.1607` → IC=+0.204 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1607 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.1106` → IC=+0.152 (n=507)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1106 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4187` → IC=+0.140 (n=576)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4187 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `331.0` → IC=+0.144 (n=487)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 331.0 (IC base=+0.130)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.265 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.213 (n=176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.0958` → IC=+0.219 (n=176)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0958 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.7033` → IC=+0.254 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7033 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.3816` → IC=+0.227 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3816 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.996` → IC=+0.236 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.996 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.8419` → IC=+0.208 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8419 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `1.156` → IC=+0.219 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.156 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2564` → IC=+0.323 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2564 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.3853` → IC=+0.237 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3853 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.405` → IC=+0.237 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.405 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `12307.7364` → IC=+0.208 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12307.7364 (IC base=+0.198)

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
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0089 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.162 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 8.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.231 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.6295` → IC=+0.219 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6295 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.127` → IC=+0.202 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.127 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.0699` → IC=+0.140 (n=337)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.0699 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.7273` → IC=+0.145 (n=342)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7273 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.288` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.288 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.2114` → IC=+0.165 (n=165)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.2114 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=416)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `3060.3888` → IC=+0.200 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3060.3888 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.167 (n=94)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 18.0 (IC base=+0.125)

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
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.207 (n=3181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=9987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.4717` → IC=+0.215 (n=9538)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4717 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.953` → IC=+0.207 (n=1391)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.953 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.613` → IC=+0.227 (n=4629)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.613 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8826` → IC=+0.165 (n=4253)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8826 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2402` → IC=+0.201 (n=1789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2402 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.6107` → IC=+0.188 (n=3050)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6107 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2341.6493` → IC=+0.171 (n=6358)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2341.6493 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.194 (n=7194)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 88.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.187 (n=7588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0092 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1458` → IC=+0.188 (n=3794)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1458 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=3280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.566` → IC=+0.237 (n=8619)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.566 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.2436` → IC=+0.161 (n=5306)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2436 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.938` → IC=+0.196 (n=1212)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.938 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.719` → IC=+0.182 (n=8356)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.719 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.705` → IC=+0.158 (n=2618)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.705 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `1.205` → IC=+0.153 (n=1983)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.205 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2879` → IC=+0.238 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2879 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6339` → IC=+0.192 (n=2625)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6339 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.190 (n=5002)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 48.0 (IC base=+0.180)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.209 (n=545)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.217 (n=543)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3504` → IC=+0.189 (n=1623)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3504 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.198 (n=1093)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.321 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.999` → IC=+0.311 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.999 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2734` → IC=+0.250 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2734 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.5813` → IC=+0.203 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5813 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.259 (n=1248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.263 (n=568)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1277` → IC=+0.288 (n=549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1277 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=1129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3505` → IC=+0.290 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3505 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.458` → IC=+0.266 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.458 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2243` → IC=+0.290 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2243 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `1.8649` → IC=+0.275 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8649 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1952.5048` → IC=+0.275 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1952.5048 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.192 (n=511)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0028 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0845` → IC=+0.164 (n=510)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0845 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.3136` → IC=+0.201 (n=1529)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3136 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1309` → IC=+0.185 (n=882)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1309 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.171 (n=351)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.234` → IC=+0.151 (n=1372)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.234 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6287` → IC=+0.176 (n=510)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6287 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.199 (n=217)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.1148` → IC=+0.161 (n=1297)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1148 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7577` → IC=+0.155 (n=983)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7577 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `15620.3876` → IC=+0.149 (n=693)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 15620.3876 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `478.0` → IC=+0.157 (n=1405)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 478.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.3196` → IC=+0.159 (n=1319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3196 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.173 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.149 (n=597)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.6489` → IC=+0.192 (n=1319)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6489 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6888` → IC=+0.154 (n=229)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.6888 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1321` → IC=+0.167 (n=1182)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1321 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.199` → IC=+0.155 (n=633)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.199 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.1888` → IC=+0.161 (n=1319)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1888 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1513` → IC=+0.196 (n=357)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1513 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4164` → IC=+0.170 (n=407)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4164 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.099` → IC=+0.162 (n=554)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.099 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `425.0` → IC=+0.157 (n=990)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 425.0 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.245 (n=512)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=1616)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=1564)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.6721` → IC=+0.255 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6721 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.81` → IC=+0.295 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.81 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.212` → IC=+0.221 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.212 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.8669` → IC=+0.245 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8669 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.229 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1944.5584` → IC=+0.220 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1944.5584 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.233 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.240 (n=1423)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1629` → IC=+0.242 (n=627)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1629 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.237 (n=675)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3623` → IC=+0.269 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3623 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.722` → IC=+0.278 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.722 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3451` → IC=+0.290 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3451 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.233 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1999` → IC=+0.238 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1999 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.245 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1867.9131` → IC=+0.248 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1867.9131 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.247 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.184 (n=548)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0035 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.436` → IC=+0.144 (n=1627)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.436 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=1708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.8773` → IC=+0.260 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8773 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3671` → IC=+0.167 (n=659)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.3671 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.157` → IC=+0.162 (n=675)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.157 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8779` → IC=+0.159 (n=1085)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8779 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.221 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5207` → IC=+0.148 (n=692)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5207 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.1389` → IC=+0.150 (n=713)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1389 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8151.7402` → IC=+0.231 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8151.7402 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.155 (n=502)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 80.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.155 (n=1319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0076 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4461` → IC=+0.153 (n=1319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4461 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6941` → IC=+0.185 (n=1319)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6941 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.7976` → IC=+0.140 (n=1522)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.7976 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.146` → IC=+0.170 (n=195)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.146 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8615` → IC=+0.143 (n=880)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8615 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1852` → IC=+0.145 (n=440)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1852 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2834` → IC=+0.244 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2834 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4416` → IC=+0.151 (n=1248)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4416 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `10973.4331` → IC=+0.210 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10973.4331 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `181.0` → IC=+0.142 (n=1243)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 181.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.136 (n=1075)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0081 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` > `0.4717` → IC=+0.188 (n=1611)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4717 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `1.0701` → IC=+0.201 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0701 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.442` → IC=+0.233 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.442 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.8926` → IC=+0.134 (n=1074)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8926 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=1622)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2913.9614` → IC=+0.246 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2913.9614 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.127 (n=1226)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 54.0 (IC base=+0.109)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.171 (n=527)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0057 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.1303` → IC=+0.158 (n=527)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1303 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.122 (n=1635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.203 (n=1580)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.129 (n=1274)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.454` → IC=+0.124 (n=1527)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.454 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.72` → IC=+0.150 (n=696)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.72 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.226` → IC=+0.167 (n=244)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.226 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.5239` → IC=+0.128 (n=474)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.5239 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2851.5493` → IC=+0.165 (n=527)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2851.5493 (IC base=+0.111)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0194` → IC=+0.218 (n=1076)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0194 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.209 (n=1441)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.5143` → IC=+0.249 (n=1616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5143 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.8917` → IC=+0.246 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8917 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.512` → IC=+0.252 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.512 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `0.6367` → IC=+0.216 (n=1614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6367 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2346` → IC=+0.249 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2346 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.5125` → IC=+0.239 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5125 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.217 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2613.5209` → IC=+0.219 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2613.5209 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.224 (n=578)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.217 (n=578)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.207 (n=1225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.5208` → IC=+0.254 (n=1733)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5208 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.8771` → IC=+0.203 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8771 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.731` → IC=+0.262 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.731 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.233` → IC=+0.240 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.233 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.262 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.2099` → IC=+0.192 (n=1364)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2099 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.197 (n=1550)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.137 (n=2885)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.158 (n=2448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0093 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.151 (n=2486)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0056 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.5252` → IC=+0.160 (n=2779)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5252 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.157 (n=933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.170 (n=959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 4.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.9415` → IC=+0.211 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9415 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1927` → IC=+0.158 (n=1010)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1927 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.5004` → IC=+0.142 (n=1648)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.5004 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.154` → IC=+0.183 (n=455)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 10.154 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.9016` → IC=+0.164 (n=1178)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.9016 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1729` → IC=+0.182 (n=762)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1729 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.157 (n=915)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.8864` → IC=+0.162 (n=1830)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8864 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `3678.1703` → IC=+0.154 (n=1852)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3678.1703 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.193 (n=727)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0038 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.3786` → IC=+0.159 (n=1915)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3786 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.164 (n=732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 4.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.1841` → IC=+0.162 (n=958)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1841 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.9174` → IC=+0.149 (n=340)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.9174 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.212` → IC=+0.144 (n=2166)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.212 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.2471` → IC=+0.140 (n=2074)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2471 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.144 (n=1010)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4259` → IC=+0.144 (n=717)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4259 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.8118` → IC=+0.140 (n=1433)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.8118 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=2885)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `6937.818` → IC=+0.149 (n=1943)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6937.818 (IC base=+0.135)

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

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.154 (n=714)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0084 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.395` → IC=+0.170 (n=628)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.395 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.153 (n=246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 4.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.1001` → IC=+0.153 (n=713)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.1001 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.6137` → IC=+0.169 (n=167)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.6137 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.3831` → IC=+0.142 (n=714)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.3831 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.716` → IC=+0.150 (n=115)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 10.716 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.281` → IC=+0.141 (n=648)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.281 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6434` → IC=+0.167 (n=238)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6434 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.7259` → IC=+0.143 (n=637)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.7259 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.171 (n=302)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.152 (n=616)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.7747` → IC=+0.158 (n=466)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7747 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7593.5796` → IC=+0.166 (n=713)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 7593.5796 (IC base=+0.140)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.220 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.177` → IC=+0.196 (n=44)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.177 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.219 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `3406.9619` → IC=+0.146 (n=179)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3406.9619 (IC base=+0.090)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.200 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.5393` → IC=+0.130 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.5393 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.144 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 10.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.1538` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1538 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.6259` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.6259 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.747` → IC=+0.128 (n=111)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.747 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` < `0.0885` → IC=+0.158 (n=150)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.0885 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3219.71` → IC=+0.138 (n=194)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3219.71 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.154 (n=163)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 55.0 (IC base=+0.100)

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

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.208 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.133 (n=793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 8.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.5517` → IC=+0.188 (n=758)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5517 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1486` → IC=+0.161 (n=426)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1486 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.45` → IC=+0.216 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.45 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.220 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `2.098` → IC=+0.144 (n=569)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.098 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=610)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2432.8034` → IC=+0.151 (n=333)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2432.8034 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.256 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.0685` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0685 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.132 (n=207)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.5975 (IC base=-0.005)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.277 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.120 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 8.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` > `0.5656` → IC=+0.199 (n=260)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.5656 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.1318` → IC=+0.188 (n=139)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1318 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `1.067` → IC=+0.128 (n=229)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.067 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.2764` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2764 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `2.0198` → IC=+0.190 (n=195)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.0198 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=265)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `4009.9429` → IC=+0.140 (n=112)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 4009.9429 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.0889` → IC=+0.255 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0889 (IC base=+0.045)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.147 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` > `0.5412` → IC=+0.209 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5412 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.1269` → IC=+0.162 (n=146)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1269 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.815` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.815 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `0.8141` → IC=+0.129 (n=173)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8141 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` > `0.6345` → IC=+0.128 (n=232)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6345 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.2901` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2901 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` < `1.7369` → IC=+0.167 (n=139)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.7369 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` > `2.4553` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.4553 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=168)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `1792.581` → IC=+0.190 (n=85)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 1792.581 (IC base=+0.108)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.121 (n=270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 7.0 (IC base=+0.076)

- **PATRÓN** `ibs_20min` > `0.6774` → IC=+0.176 (n=214)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6774 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.1957` → IC=+0.155 (n=140)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1957 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.244` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.244 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.0662` → IC=+0.159 (n=80)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.0662 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.0847` → IC=+0.173 (n=99)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0847 (IC base=+0.076)

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
- **FILTRO** `ibs_20min` < `0.8798` → IC=-0.409 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8798
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=23)

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

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.131 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0057 (IC base=+0.084)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.128 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.084)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.161 (n=240)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.6522 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.4724` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.4724 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.032)

- **PATRÓN** `libro_liquidez` > `3771.3449` → IC=+0.141 (n=115)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3771.3449 (IC base=+0.032)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.5739` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5739
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=78)

- **PATRÓN** `volumen_spike_ratio` > `1.4745` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4745 (IC base=-0.019)

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

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.196 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0052 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.202 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.182 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 18.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.7083` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7083 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.7975` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7975 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.166` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.166 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.179 (n=76)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.06 (IC base=+0.179)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=651)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2892.6924` → IC=+0.167 (n=220)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2892.6924 (IC base=+0.107)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=651)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.107)

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
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=204)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=190)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=1648)

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
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=736)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=133)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9164` → IC=-0.147 (n=49)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9164
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=100)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.122 (n=72)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=77)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=610)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=610)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=482)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=329)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=329)

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
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=194)

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
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=119)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=7350)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.173 (n=3181)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=10156)

- **FILTRO** `py_entrada` > `0.595` → IC=-0.171 (n=3434)

  - _Acción_: SKIP cuando `py_entrada` > 0.595
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=10341)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.212 (n=564)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1736)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.173 (n=563)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=1905)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.201 (n=580)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=1768)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.206 (n=603)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=1854)

- **FILTRO** `ibs_20min` > `0.2826` → IC=-0.162 (n=614)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2826
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1843)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.176 (n=553)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1731)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.183 (n=607)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1850)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2681)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=2839)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=2845)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` > `0.1742` → IC=-0.138 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1742
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=345)

- **FILTRO** `libro_liquidez` < `16884.2168` → IC=-0.141 (n=215)

  - _Acción_: SKIP cuando `libro_liquidez` < 16884.2168
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=647)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=232)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.253 (n=75)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=225)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=218)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=748)

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
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=21285)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.274 (n=7447)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=23272)

- **FILTRO** `ibs_7min` < `0.2903` → IC=-0.235 (n=7677)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2903
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=23042)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=10407)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=20312)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.230 (n=9482)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=28818)

- **FILTRO** `ibs_7min` > `0.2941` → IC=-0.180 (n=9548)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=28752)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.135 (n=1544)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=3512)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=1205)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3851)

- **FILTRO** `ibs_7min` < `0.7099` → IC=-0.252 (n=1668)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7099
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3388)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.183 (n=1175)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3881)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.261 (n=1635)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=4957)

- **FILTRO** `drift_7min_pct` |x|> `0.1117` → IC=-0.124 (n=2240)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1117
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4352)

- **FILTRO** `ibs_7min` > `0.7945` → IC=-0.209 (n=1646)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7945
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=4946)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=1237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=4085)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1280)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4042)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.191 (n=1330)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3992)

- **FILTRO** `ballena_activa_n` > `160.0` → IC=-0.171 (n=1326)

  - _Acción_: SKIP cuando `ballena_activa_n` > 160.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=3996)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.255 (n=1326)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=4028)

- **FILTRO** `ibs_7min` > `0.2599` → IC=-0.178 (n=1338)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2599
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=4016)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.189 (n=1331)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4023)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.172 (n=1174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=3614)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.309 (n=1166)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=3622)

- **FILTRO** `ibs_7min` < `0.1971` → IC=-0.259 (n=1197)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1971
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3591)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.214 (n=1126)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3662)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.238 (n=1628)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=5404)

- **FILTRO** `ibs_7min` > `0.7545` → IC=-0.178 (n=1757)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7545
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=5275)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.232 (n=1493)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=3570)

- **FILTRO** `ibs_7min` < `0.7427` → IC=-0.179 (n=1264)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7427
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3799)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.168 (n=1241)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3822)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.265 (n=1141)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=4001)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.175 (n=1285)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3857)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.192 (n=1259)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3883)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.263 (n=1275)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=4103)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.240 (n=1321)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4057)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.179 (n=1745)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=5534)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.271 (n=1208)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3904)

- **FILTRO** `ibs_7min` < `0.7037` → IC=-0.228 (n=1277)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7037
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3835)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.212 (n=1228)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3884)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.204 (n=1682)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=5219)

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
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=523)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=734)

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
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.147 (n=477)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `464.449` → IC=+0.151 (n=239)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 464.449 (IC base=+0.116)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4386` → IC=+0.138 (n=56)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.4386 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `445.688` → IC=+0.144 (n=147)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 445.688 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 13.0 (IC base=+0.134)

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
- **FILTRO** `sigma_h` > `0.0055` → IC=-0.306 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=179)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0058` → IC=-0.339 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
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
- **FILTRO** `T_h` > `98.1124` → IC=-0.211 (n=50)

  - _Acción_: SKIP cuando `T_h` > 98.1124
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=52)

- **FILTRO** `pct_vs_K` |x|> `2.4552` → IC=-0.343 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4552
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=53)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.315 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=76)

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
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=706)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=712)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=561)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1108)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=705)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=685)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2793)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1430)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1438)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.231 (n=674)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.0756` → IC=+0.202 (n=655)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0756 (IC base=+0.189)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2134` → IC=+0.195 (n=496)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.2134 (IC base=+0.189)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1268` → IC=+0.234 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1268 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=1390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.189)

- **PATRÓN** `ibs_15` > `0.6087` → IC=+0.264 (n=1487)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6087 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.2972` → IC=+0.196 (n=534)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.2972 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.915` → IC=+0.274 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.915 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `2986.1526` → IC=+0.193 (n=991)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2986.1526 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.209 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.189)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=526)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.210 (n=346)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.288 (n=116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.198)

- **PATRÓN** `drift_15min` |x|≤ `0.3811` → IC=+0.212 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3811 (IC base=+0.198)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.235 (n=115)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.260 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.7031` → IC=+0.262 (n=346)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7031 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.250 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.503` → IC=+0.250 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.503 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `15931.8012` → IC=+0.229 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15931.8012 (IC base=+0.198)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.889` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.889
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=341)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.145 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0065 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.168 (n=233)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0051 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.069` → IC=+0.162 (n=155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.069 (IC base=+0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.181 (n=117)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2579` → IC=+0.171 (n=247)

  - _Acción_: Kelly boost +0.85€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2579 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.167 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.6675` → IC=+0.240 (n=313)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6675 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.4333` → IC=+0.149 (n=109)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.4333 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1631` → IC=+0.161 (n=272)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1631 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.389` → IC=+0.203 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.389 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3459.7073` → IC=+0.154 (n=313)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3459.7073 (IC base=+0.143)

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
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=816)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `16.21` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.21 (IC base=+0.019)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0177` → IC=+0.240 (n=267)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0177 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0859` → IC=+0.204 (n=177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0859 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0605` → IC=+0.201 (n=359)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0605 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0898` → IC=+0.260 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0898 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.235 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.5455` → IC=+0.284 (n=401)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5455 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1292` → IC=+0.207 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1292 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.853` → IC=+0.225 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.853 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.408` → IC=+0.190 (n=359)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 7.408 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.188 (n=408)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2902.476` → IC=+0.279 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2902.476 (IC base=+0.188)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.157 (n=444)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1176 (IC base=+0.045)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.334 (n=263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.335)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.373 (n=179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.335)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.339 (n=265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.335)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.360 (n=262)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=+0.335)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.13` → IC=+0.370 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.13 (IC base=+0.335)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.357 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.335)

- **PATRÓN** `ibs_15` > `0.7856` → IC=+0.379 (n=393)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7856 (IC base=+0.335)

- **PATRÓN** `dist_vwap_pct` > `0.4313` → IC=+0.379 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4313 (IC base=+0.335)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.085` → IC=+0.343 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.085 (IC base=+0.335)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.018` → IC=+0.335 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.018 (IC base=+0.335)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.341 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `3532.3524` → IC=+0.351 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3532.3524 (IC base=+0.335)

- **PATRÓN** `ballena_activa_n` < `474.0` → IC=+0.358 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 474.0 (IC base=+0.335)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.347 (n=194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.337)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.368 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.337)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.355 (n=74)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.337)

- **PATRÓN** `drift_15min` |x|≤ `0.4288` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4288 (IC base=+0.337)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.347 (n=220)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.337)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.378 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.337)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.365 (n=205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.337)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.374 (n=220)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.337)

- **PATRÓN** `dist_vwap_pct` > `0.4016` → IC=+0.409 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4016 (IC base=+0.337)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.381` → IC=+0.348 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.381 (IC base=+0.337)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.339 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.337)

- **PATRÓN** `libro_liquidez` > `15620.9367` → IC=+0.342 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15620.9367 (IC base=+0.337)

- **PATRÓN** `ballena_activa_n` < `582.0` → IC=+0.385 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 582.0 (IC base=+0.337)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.378 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.328)

- **PATRÓN** `drift_60min` |x|≤ `0.1054` → IC=+0.339 (n=116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1054 (IC base=+0.328)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.348 (n=156)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.328)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.355 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.328)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.392 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.328)

- **PATRÓN** `ibs_15` > `0.7401` → IC=+0.386 (n=174)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7401 (IC base=+0.328)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.328)

- **PATRÓN** `dist_vwap_pct` < `0.1227` → IC=+0.338 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1227 (IC base=+0.328)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.717` → IC=+0.339 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.717 (IC base=+0.328)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.333 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.328)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.343 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.328)

- **PATRÓN** `libro_liquidez` > `3546.8859` → IC=+0.356 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3546.8859 (IC base=+0.328)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.337 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 166.0 (IC base=+0.328)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.013` → IC=-0.214 (n=627)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1884)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.187 (n=836)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1675)

- **FILTRO** `libro_liquidez` < `3911.5181` → IC=-0.134 (n=1657)

  - _Acción_: SKIP cuando `libro_liquidez` < 3911.5181
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=854)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.250 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.060)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.266 (n=608)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` > `0.5693` → IC=+0.178 (n=116)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.5693 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` < `0.2735` → IC=+0.176 (n=477)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2735 (IC base=-0.060)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1175` → IC=+0.237 (n=1052)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1175 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1774` → IC=+0.234 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1774 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.276 (n=1576)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.6682` → IC=+0.287 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6682 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.221 (n=381)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=1147)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.227 (n=382)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1146)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.208 (n=972)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=556)

- **FILTRO** `sigma_ewma_delta_pct` > `19.708` → IC=-0.253 (n=273)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.708
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1255)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.167 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0028 (IC base=+0.076)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.276 (n=74)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.076)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=+0.076)

- **PATRÓN** `ibs_15` > `0.7374` → IC=+0.311 (n=162)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7374 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.0996` → IC=+0.276 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0996 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.536` → IC=+0.267 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.536 (IC base=+0.076)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6647` → IC=-0.194 (n=96)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6647
  - _Potencial_: sin este filtro IC_bueno=+0.261 (n=291)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=370)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.189 (n=194)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0051 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.215 (n=128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.148)

- **PATRÓN** `drift_15min` |x|≤ `0.4246` → IC=+0.167 (n=97)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.4246 (IC base=+0.148)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1323` → IC=+0.158 (n=194)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.1323 (IC base=+0.148)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.240 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.6647` → IC=+0.261 (n=291)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6647 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.4741` → IC=+0.155 (n=85)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.4741 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1187` → IC=+0.179 (n=207)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1187 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.951` → IC=+0.159 (n=247)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 8.951 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=370)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `11008.7835` → IC=+0.194 (n=132)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 11008.7835 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.238 (n=631)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.226)

- **PATRÓN** `drift_15min` |x|≤ `0.7826` → IC=+0.231 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7826 (IC base=+0.226)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2028` → IC=+0.250 (n=286)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2028 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.246 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.226)

- **PATRÓN** `ibs_15` < `0.2696` → IC=+0.281 (n=556)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2696 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.7515` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7515 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.01` → IC=+0.255 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.01 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.221` → IC=+0.230 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.221 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `3551.8492` → IC=+0.227 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3551.8492 (IC base=+0.226)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.230 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.137 (n=442)

- **FILTRO** `drift_60min` |x|> `0.17` → IC=-0.216 (n=199)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.17
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=389)

- **FILTRO** `drift_15min` |x|> `0.8847` → IC=-0.250 (n=146)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8847
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=442)

- **FILTRO** `sigma_ewma_delta_pct` > `17.987` → IC=-0.133 (n=311)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.987
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2530)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.161)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.161)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0764` → IC=+0.219 (n=258)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0764 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.260 (n=289)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.4766` → IC=+0.203 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4766 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` < `0.199` → IC=+0.212 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.199 (IC base=-0.044)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.257 (n=373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=375)

- **FILTRO** `drift_15min` |x|> `1.2211` → IC=-0.250 (n=186)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2211
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=562)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.263 (n=184)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=564)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1533` → IC=+0.274 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1533 (IC base=-0.047)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.103` → IC=+0.358 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.103 (IC base=-0.047)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.304 (n=432)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.047)

- **PATRÓN** `dist_vwap_pct` > `0.8592` → IC=+0.364 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8592 (IC base=-0.047)

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
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.291 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.286 (n=288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.313 (n=212)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2388` → IC=+0.299 (n=212)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2388 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1083` → IC=+0.342 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1083 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=667)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.323 (n=635)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.1575` → IC=+0.318 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1575 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.164` → IC=+0.326 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.164 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.290 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `13020.8583` → IC=+0.297 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13020.8583 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.317 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.284 (n=160)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.342 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.279)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.298 (n=117)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.279)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3729` → IC=+0.299 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3729 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.298 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.279)

- **PATRÓN** `ibs_15` > `0.8305` → IC=+0.310 (n=351)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8305 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.4333` → IC=+0.354 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4333 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.355 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `16027.7188` → IC=+0.315 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16027.7188 (IC base=+0.279)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.304 (n=284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.297 (n=190)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.226` → IC=+0.314 (n=95)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.226 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.333 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.330 (n=256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8475` → IC=+0.336 (n=284)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8475 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.167` → IC=+0.313 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.167 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.307 (n=324)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6087 sube el IC de +0.189 a +0.264 en UPDOWN_GBM#15min (n=1487). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7031 sube el IC de +0.198 a +0.262 en UPDOWN_GBM#BTC#15min (n=346). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6675 sube el IC de +0.143 a +0.240 en UPDOWN_GBM#ETH#15min (n=313). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6111 sube el IC de +0.173 a +0.257 en UPDOWN_GBM#SOL#15min (n=183). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5455 sube el IC de +0.188 a +0.284 en UPDOWN_GBM#XRP#15min (n=401). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.045 a +0.157 en UPDOWN_GBM#XRP#15min (n=444). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.060 a +0.266 en UPDOWN_GBM_15M_TARDIO (n=608). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.039 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=1576). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7374 sube el IC de +0.076 a +0.311 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=162). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6647 sube el IC de +0.148 a +0.261 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=291). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2696 sube el IC de +0.226 a +0.281 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=556). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.161 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.044 a +0.260 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=289). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.047 a +0.304 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=432). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.287 a +0.323 en UPDOWN_GBM_IBS_ALTO (n=635). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8305 sube el IC de +0.279 a +0.310 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=351). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8475 sube el IC de +0.295 a +0.336 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=284). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7856 sube el IC de +0.335 a +0.379 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=393). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.337 a +0.374 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=220). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7401 sube el IC de +0.328 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=174). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1271 | +0.094 | +172.02€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1271 | +0.094 | +172.02€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 941 | +0.103 | +146.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 941 | +0.103 | +146.23€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 244 | +0.049 | +7.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 244 | +0.049 | +7.13€ | 4 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 6 |
| ✅ BALLENAS_TARDIAS | 24114 | -0.090 | -3046.97€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1425 | -0.046 | -216.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 22689 | -0.093 | -2830.25€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3568 | -0.084 | -575.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3568 | -0.084 | -575.55€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1425 | -0.046 | -216.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1425 | -0.046 | -216.71€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 6924 | -0.023 | -592.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 6924 | -0.023 | -592.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6421 | -0.095 | -417.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6421 | -0.095 | -417.36€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5402 | -0.183 | -1083.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5402 | -0.183 | -1083.64€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 16758 | -0.030 | +4104.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4394 | -0.001 | +1832.19€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 12364 | -0.040 | +2272.43€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 16758 | -0.030 | +4104.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4394 | -0.001 | +1832.19€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 12364 | -0.040 | +2272.43€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1455 | -0.103 | -190.30€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 168 | -0.053 | -21.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1287 | -0.109 | -168.94€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 780 | -0.091 | -97.63€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 144 | -0.048 | -16.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 477 | -0.128 | -78.79€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 453 | -0.131 | -73.56€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 88456 | +0.113 | -4469.72€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 13492 | +0.184 | -430.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 353 | -0.094 | -49.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 68793 | +0.100 | -3787.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5818 | +0.109 | -202.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 11446 | +0.098 | -984.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 44 | -0.174 | -3.33€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 11387 | +0.100 | -969.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 17891 | +0.132 | -366.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4221 | +0.202 | -144.51€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 11402 | +0.112 | -174.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2226 | +0.106 | -25.52€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 11487 | +0.089 | -1073.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 51 | -0.085 | -5.77€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 11421 | +0.091 | -1056.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 18849 | +0.124 | -374.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5216 | +0.175 | -78.24€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 11519 | +0.106 | -237.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2102 | +0.098 | -50.96€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 17319 | +0.115 | -998.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3916 | +0.188 | -207.21€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 256 | -0.054 | +4.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 11657 | +0.092 | -670.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1490 | +0.127 | -125.72€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 11464 | +0.102 | -670.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 44 | -0.022 | +8.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 11407 | +0.102 | -679.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 14040 | +0.193 | -904.66€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 14040 | +0.193 | -904.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3365 | +0.169 | -354.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3365 | +0.169 | -354.39€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1089 | +0.195 | -6.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1089 | +0.195 | -6.38€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3303 | +0.182 | -274.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3303 | +0.182 | -274.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2961 | +0.238 | -95.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2961 | +0.238 | -95.31€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3243 | +0.195 | -187.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3243 | +0.195 | -187.56€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 663 | +0.429 | -19.07€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 663 | +0.429 | -19.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 253 | +0.433 | -4.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 253 | +0.433 | -4.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 249 | +0.436 | -2.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 249 | +0.436 | -2.52€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 153 | +0.403 | -10.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 153 | +0.403 | -10.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 48187 | +0.198 | -3725.07€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 48187 | +0.198 | -3725.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8348 | +0.176 | -971.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8348 | +0.176 | -971.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 7690 | +0.225 | -262.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 7690 | +0.225 | -262.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8317 | +0.174 | -982.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8317 | +0.174 | -982.67€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 7784 | +0.220 | -289.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 7784 | +0.220 | -289.22€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 7956 | +0.204 | -514.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 7956 | +0.204 | -514.16€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8092 | +0.194 | -704.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8092 | +0.194 | -704.57€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 18158 | +0.117 | +127.33€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 18158 | +0.117 | +127.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 9010 | +0.122 | +123.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 9010 | +0.122 | +123.67€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 9148 | +0.113 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 9148 | +0.113 | +3.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1413 | +0.293 | -2.16€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1413 | +0.293 | -2.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 630 | +0.279 | -14.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 630 | +0.279 | -14.17€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 679 | +0.297 | +10.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 679 | +0.297 | +10.22€ | 0 | 4 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1055 | +0.077 | -38.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 367 | +0.066 | -25.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 688 | +0.083 | -12.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 830 | +0.084 | -13.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 142 | +0.090 | -0.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 688 | +0.083 | -12.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 164 | +0.024 | -27.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 164 | +0.024 | -27.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 33297 | +0.097 | -1052.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2760 | +0.089 | +18.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 30537 | +0.098 | -1070.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 18754 | +0.102 | -310.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2760 | +0.089 | +18.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 15994 | +0.104 | -328.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 6169 | +0.105 | -58.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 6169 | +0.105 | -58.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 8374 | +0.081 | -683.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 8374 | +0.081 | -683.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 779 | +0.214 | -97.46€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 779 | +0.214 | -97.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 779 | +0.214 | -97.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 779 | +0.214 | -97.46€ | 2 | 4 |
| ✅ GBM_LATE_15M | 24089 | +0.081 | +11278.59€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 24089 | +0.081 | +11278.59€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4007 | +0.192 | +2899.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4007 | +0.192 | +2899.95€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 3577 | +0.175 | +2452.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3577 | +0.175 | +2452.05€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 4154 | +0.200 | +3125.23€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4154 | +0.200 | +3125.23€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 3577 | +0.016 | +691.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3577 | +0.016 | +691.99€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3485 | -0.034 | +791.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3485 | -0.034 | +791.69€ | 4 | 16 |
| ✅ GBM_LATE_15M#XRP | 5289 | -0.043 | +1317.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5289 | -0.043 | +1317.67€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 25444 | +0.084 | +13242.82€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 25444 | +0.084 | +13242.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4823 | +0.014 | +2591.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4823 | +0.014 | +2591.85€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5311 | +0.013 | +1071.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5311 | +0.013 | +1071.24€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3601 | +0.262 | +3624.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3601 | +0.262 | +3624.41€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4109 | -0.000 | +743.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4109 | -0.000 | +743.02€ | 2 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4148 | +0.025 | +1544.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4148 | +0.025 | +1544.92€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3452 | +0.275 | +3667.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3452 | +0.275 | +3667.38€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 19455 | +0.167 | +14356.22€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 19455 | +0.167 | +14356.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2922 | +0.205 | +2304.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2922 | +0.205 | +2304.08€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3101 | +0.147 | +2213.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3101 | +0.147 | +2213.14€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3038 | +0.210 | +2439.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3038 | +0.210 | +2439.99€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3266 | +0.133 | +2211.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3266 | +0.133 | +2211.36€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3623 | +0.114 | +2424.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3623 | +0.114 | +2424.33€ | 1 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3505 | +0.203 | +2763.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3505 | +0.203 | +2763.31€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4768 | +0.123 | +1929.29€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4768 | +0.123 | +1929.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1367 | +0.119 | +587.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1367 | +0.119 | +587.88€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 369 | +0.147 | +180.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 369 | +0.147 | +180.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1347 | +0.140 | +580.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1347 | +0.140 | +580.39€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 997 | +0.094 | +287.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 997 | +0.094 | +287.33€ | 2 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 504 | +0.134 | +216.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 504 | +0.134 | +216.54€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 24206 | +0.174 | +17808.84€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 24206 | +0.174 | +17808.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3825 | +0.219 | +3195.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3825 | +0.219 | +3195.79€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3796 | +0.149 | +2478.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3796 | +0.149 | +2478.59€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3945 | +0.226 | +3405.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3945 | +0.226 | +3405.05€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3926 | +0.136 | +2625.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3926 | +0.136 | +2625.55€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4253 | +0.110 | +2619.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4253 | +0.110 | +2619.30€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4461 | +0.204 | +3484.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4461 | +0.204 | +3484.54€ | 0 | 22 |
| ✅ GBM_LATE_5M | 6604 | +0.144 | +3669.17€ | 1 | 27 |
| ✅ GBM_LATE_5M#5min | 6604 | +0.144 | +3669.17€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1691 | +0.139 | +1068.26€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1691 | +0.139 | +1068.26€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2087 | +0.147 | +1141.68€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2087 | +0.147 | +1141.68€ | 0 | 30 |
| ✅ GBM_LATE_5M#SOL | 524 | +0.095 | +161.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 524 | +0.095 | +161.84€ | 0 | 13 |
| ✅ GBM_LATE_5M#XRP | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1587 | +0.069 | +710.30€ | 3 | 12 |
| ✅ GBM_LATE_60M#60min | 1587 | +0.069 | +710.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 572 | +0.089 | +249.82€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 572 | +0.089 | +249.82€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 527 | +0.073 | +269.92€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 527 | +0.073 | +269.92€ | 2 | 19 |
| ✅ GBM_LATE_60M#SOL | 488 | +0.041 | +190.56€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 488 | +0.041 | +190.56€ | 1 | 11 |
| 🚫 GBM_LATE_60M_FADE | 355 | -0.259 | -26.23€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 355 | -0.259 | -26.23€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 136 | -0.225 | -11.33€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 136 | -0.225 | -11.33€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 117 | -0.265 | -9.64€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 117 | -0.265 | -9.64€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 102 | -0.288 | -5.26€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 102 | -0.288 | -5.26€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 656 | +0.058 | +122.46€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 656 | +0.058 | +122.46€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 257 | +0.048 | +43.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 257 | +0.048 | +43.03€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 189 | +0.029 | -3.13€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 189 | +0.029 | -3.13€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 210 | +0.094 | +82.56€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 210 | +0.094 | +82.56€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN | 91 | +0.253 | +70.64€ | 0 | 8 |
| ✅ LATE_WINDOW_5MIN#5min | 91 | +0.253 | +70.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 91 | +0.253 | +70.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 91 | +0.253 | +70.64€ | 0 | 8 |
| ✅ LEADLAG_BTC_XRP_15M | 1805 | +0.097 | +484.96€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1805 | +0.097 | +484.96€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1805 | +0.097 | +484.96€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1805 | +0.097 | +484.96€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 371 | -0.082 | -34.64€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 371 | -0.082 | -34.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 94 | -0.062 | -5.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 94 | -0.062 | -5.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 129 | -0.027 | -4.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 129 | -0.027 | -4.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1846 | +0.007 | +19.36€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1846 | +0.007 | +19.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 96 | +0.000 | -2.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 96 | +0.000 | -2.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 201 | +0.003 | +15.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 201 | +0.003 | +15.26€ | 4 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 137 | -0.040 | -6.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 137 | -0.040 | -6.83€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 783 | +0.034 | +28.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 783 | +0.034 | +28.00€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 467 | -0.001 | -5.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 467 | -0.001 | -5.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 162 | -0.049 | -8.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 162 | -0.049 | -8.66€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M | 1034 | -0.048 | -31.16€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1034 | -0.048 | -31.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 295 | -0.042 | -12.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 295 | -0.042 | -12.66€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 344 | -0.041 | -6.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 344 | -0.041 | -6.36€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 395 | -0.059 | -12.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 395 | -0.059 | -12.14€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 280 | -0.007 | +9.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 132 | +0.015 | +11.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 148 | -0.027 | -2.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 7 | -0.019 | -0.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 83 | +0.053 | +14.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 37 | +0.064 | +7.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 46 | +0.042 | +7.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 48 | -0.040 | -2.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 25 | -0.056 | -2.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 23 | -0.020 | +0.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 45 | -0.032 | -0.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 20 | +0.000 | +1.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 25 | -0.056 | -1.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 36 | +0.000 | +1.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 19 | +0.113 | +7.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 17 | -0.112 | -6.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 61 | -0.040 | -3.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 27 | -0.052 | -2.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 34 | -0.028 | -0.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 14214 | -0.012 | -207.90€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14214 | -0.012 | -207.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2931 | -0.022 | -61.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2931 | -0.022 | -61.08€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 27112 | -0.008 | +1177.15€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 27112 | -0.008 | +1177.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4768 | +0.015 | +586.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4768 | +0.015 | +586.44€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4238 | -0.028 | -50.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4238 | -0.028 | -50.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4805 | +0.013 | +423.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4805 | +0.013 | +423.61€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4019 | -0.053 | -146.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4019 | -0.053 | -146.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4541 | -0.012 | +169.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4541 | -0.012 | +169.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4741 | +0.006 | +193.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4741 | +0.006 | +193.59€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5621 | -0.055 | -132.19€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5621 | -0.055 | -132.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1321 | -0.073 | -31.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1321 | -0.073 | -31.85€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 582 | -0.120 | -21.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 582 | -0.120 | -21.72€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1625 | -0.076 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1625 | -0.076 | -31.94€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 69019 | -0.073 | +1590.78€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 69019 | -0.073 | +1590.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 11648 | -0.080 | +638.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 11648 | -0.080 | +638.86€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 10676 | -0.094 | -485.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 10676 | -0.094 | -485.65€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 11820 | -0.068 | +634.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 11820 | -0.068 | +634.22€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 10205 | -0.093 | -135.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 10205 | -0.093 | -135.13€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 12657 | -0.049 | +367.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 12657 | -0.049 | +367.45€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 12013 | -0.062 | +571.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 12013 | -0.062 | +571.03€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7100 | -0.022 | -100.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7100 | -0.022 | -100.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1631 | -0.026 | -3.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1631 | -0.026 | -3.87€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1706 | -0.014 | -5.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1706 | -0.014 | -5.08€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1026 | -0.040 | -17.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1026 | -0.040 | -17.10€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1089 | +0.109 | +368.32€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 953 | +0.116 | +355.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 222 | +0.134 | +108.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 222 | +0.134 | +108.00€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 186 | +0.096 | +44.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 186 | +0.096 | +44.24€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 193 | +0.095 | +62.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 193 | +0.095 | +62.76€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 165 | +0.141 | +80.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 165 | +0.141 | +80.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 187 | +0.108 | +59.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 187 | +0.108 | +59.86€ | 0 | 5 |
| ✅ ORDER_FLOW_5M_REACTIVO | 419 | -0.053 | -42.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 419 | -0.053 | -42.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 91 | -0.005 | +3.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 91 | -0.005 | +3.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 54 | -0.125 | -15.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 54 | -0.125 | -15.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 118 | -0.075 | -22.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 118 | -0.075 | -22.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 84 | +0.012 | +4.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 84 | +0.012 | +4.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 72 | -0.095 | -12.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 72 | -0.095 | -12.67€ | 0 | 0 |
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
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 203 | -0.237 | -26.74€ | 5 | 0 |
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
| ✅ STREAK_FADE_5M | 2668 | -0.022 | -110.55€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2668 | -0.022 | -110.55€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 565 | -0.022 | -22.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 565 | -0.022 | -22.81€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1144 | -0.022 | -45.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1144 | -0.022 | -45.87€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 69 | -0.063 | -7.52€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 69 | -0.063 | -7.52€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 37 | -0.090 | -3.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 37 | -0.090 | -3.93€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 32 | -0.029 | -3.59€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 32 | -0.029 | -3.59€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7490 | +0.023 | +107.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7490 | +0.023 | +107.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2122 | +0.021 | +20.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2122 | +0.021 | +20.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1655 | +0.036 | +52.67€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1655 | +0.036 | +52.67€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2281 | +0.011 | +0.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2281 | +0.011 | +0.41€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1432 | +0.028 | +34.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1432 | +0.028 | +34.38€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7025 | +0.010 | -56.74€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7025 | +0.010 | -56.74€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2812 | +0.014 | -12.33€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2812 | +0.014 | -12.33€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2751 | +0.010 | -22.13€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2751 | +0.010 | -22.13€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1462 | +0.000 | -22.28€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1462 | +0.000 | -22.28€ | 2 | 0 |
| ✅ UPDOWN_GBM | 34158 | +0.030 | +2029.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 9219 | +0.064 | +1633.88€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 1275 | +0.004 | +6.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 21462 | +0.021 | +364.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2069 | +0.009 | +25.60€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3347 | +0.067 | +353.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 539 | +0.149 | +211.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 29 | -0.016 | -0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2779 | +0.052 | +142.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 6335 | +0.034 | +414.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1170 | +0.079 | +250.70€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 348 | +0.020 | +7.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 3836 | +0.030 | +138.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 930 | +0.004 | +16.87€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 51 | -0.104 | +0.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 3992 | +0.040 | +234.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 502 | +0.143 | +188.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 25 | -0.018 | -1.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3465 | +0.025 | +47.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 7259 | +0.019 | +291.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2408 | +0.045 | +271.48€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 336 | +0.006 | +7.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 3765 | +0.007 | +10.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 707 | +0.006 | -0.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 43 | -0.144 | +3.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 8251 | +0.016 | +213.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2299 | +0.024 | +155.16€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 330 | -0.006 | -3.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5153 | +0.014 | +55.28€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 432 | +0.023 | +9.18€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 37 | -0.167 | -2.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 4972 | +0.035 | +523.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2301 | +0.078 | +556.15€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 207 | -0.002 | -2.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2464 | -0.002 | -29.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 131 | -0.139 | +1.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 524 | +0.335 | +148.30€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 524 | +0.335 | +148.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 293 | +0.337 | +78.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 293 | +0.337 | +78.86€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 231 | +0.328 | +69.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 231 | +0.328 | +69.45€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 11168 | -0.043 | +2274.06€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 11168 | -0.043 | +2274.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 662 | -0.048 | +322.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 662 | -0.048 | +322.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2094 | -0.124 | +22.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2094 | -0.124 | +22.09€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 310 | +0.167 | +189.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 310 | +0.167 | +189.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1228 | +0.202 | +709.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1228 | +0.202 | +709.22€ | 2 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3429 | -0.065 | +519.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3429 | -0.065 | +519.71€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3445 | -0.079 | +510.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3445 | -0.079 | +510.75€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 132 | +0.045 | +9.79€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 132 | +0.045 | +9.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 132 | +0.045 | +9.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 132 | +0.045 | +9.79€ | 2 | 3 |
| ✅ UPDOWN_GBM_IBS_ALTO | 846 | +0.287 | +672.20€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 846 | +0.287 | +672.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 468 | +0.279 | +344.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 468 | +0.279 | +344.22€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 378 | +0.295 | +327.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 378 | +0.295 | +327.98€ | 0 | 9 |
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
  - _Estado_: 520 celda(s) pasan gate riguroso completo de 2179 evaluadas (n>=40) y 3180 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.024 < 0.08 — monitorear
  - _Datos_: n=2297 IC=+0.024 PNL=+154.11€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.090 n=266/60 | contraria IC=+0.151 n=262 | gap=-0.062 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=271, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=707/40 IC=+0.006 PNL=-0.44€ | BTC#60min: n=930/40 IC=+0.004 PNL=+16.87€ | SOL#60min: n=432/40 IC=+0.023 PNL=+9.18€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.051 n=316064 | tras_1loss IC=+0.076 n=246074 | tras_2loss IC=+0.045 n=104151/40 | gap=+0.006 (umbral 0.05)

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
  - _Estado_: n=1489 IC=+0.018 PNL=+17.73€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1489 IC=+0.018 PNL=+17.73€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=580 IC=-0.015 PNL=+7.87€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=580 IC=-0.015 PNL=+7.87€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.1 con n=1982 PNL=+1256.76€
  - _Datos_: n=1982 IC=+0.189 PNL=+1256.76€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1168 IC=+0.080 PNL=+250.69€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1168 IC=+0.080 PNL=+250.69€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.02 con n=624 PNL=+248.33€
  - _Datos_: n=624 IC=+0.126 PNL=+248.33€

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
  - _Estado_: n=11835 IC=+0.057 PNL=+1502.17€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=11835 IC=+0.057 PNL=+1502.17€

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
  - _Estado_: n=1765 IC=+0.044 PNL=+178.94€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1765 IC=+0.044 PNL=+178.94€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.1 con n=372 PNL=+104.16€
  - _Datos_: n=372 IC=+0.126 PNL=+104.16€

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
  - _Estado_: n=16777 IC=-0.137 PNL=+1165.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=16777 IC=-0.137 PNL=+1165.94€

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
  - _Estado_: n=1820 IC=+0.138 PNL=+980.52€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1820 IC=+0.138 PNL=+980.52€

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
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.238 < -0.1 con n=1649 PNL=-178.05€
  - _Datos_: n=1649 IC=-0.238 PNL=-178.05€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.087 n=925) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=925 IC=+0.087 PNL=+207.67€

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
  - _Estado_: n=8344 IC=+0.176 PNL=-970.21€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8344 IC=+0.176 PNL=-970.21€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.1 con n=132 PNL=+75.67€
  - _Datos_: n=132 IC=+0.194 PNL=+75.67€
