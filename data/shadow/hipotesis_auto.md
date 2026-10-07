# Hipótesis automáticas — 2026-10-07 00:50 UTC
_Generado por shadow_postmortem.py sobre 783412 resoluciones (PNL=+96031.83€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=575)

- **PATRÓN** `py_entrada` > `0.51` → IC=+0.233 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.51 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.209 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.6242` → IC=+0.253 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6242 (IC base=+0.125)

- **PATRÓN** `banda_z` > `9.189` → IC=+0.185 (n=217)

  - _Acción_: Kelly boost +0.92€ cuando `banda_z` > 9.189 (IC base=+0.125)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.701` → IC=+0.124 (n=581)

  - _Acción_: Kelly boost +0.62€ cuando `ballenas_wallet_edge_medio` > 0.701 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=677)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=688)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.125)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.242 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.131)

- **PATRÓN** `n_total_lado` > `42.0` → IC=+0.164 (n=483)

  - _Acción_: Kelly boost +0.82€ cuando `n_total_lado` > 42.0 (IC base=+0.131)

- **PATRÓN** `banda_hit_calibrado` > `0.6164` → IC=+0.241 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6164 (IC base=+0.131)

- **PATRÓN** `banda_z` > `9.852` → IC=+0.195 (n=175)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 9.852 (IC base=+0.131)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.903` → IC=+0.131 (n=426)

  - _Acción_: Kelly boost +0.65€ cuando `ballenas_wallet_edge_medio` > 0.903 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.131 (n=380)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 12.0 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=590)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.131)

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

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=94)

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
- **FILTRO** `restante_s_al_confirmar` < `143.9` → IC=-0.213 (n=8592)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.9
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=25779)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.69` → IC=-0.270 (n=1089)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.69
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3267)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `124.35` → IC=-0.303 (n=1010)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.35
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3031)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `165.07` → IC=-0.224 (n=2168)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 165.07
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=6507)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `129.15` → IC=-0.307 (n=1668)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 129.15
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=5006)

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
- **PATRÓN** `py_entrada` > `0.685` → IC=+0.213 (n=16595)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.685 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=3919)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `9614.35` → IC=+0.183 (n=1738)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 9614.35 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=14771)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=17843)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=13645)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=6435)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7567.3464` → IC=+0.168 (n=2470)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7567.3464 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=1902)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=1854)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=2334)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `16074.9801` → IC=+0.213 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16074.9801 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.199 (n=1678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=1860)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=2388)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `16023.7287` → IC=+0.210 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16023.7287 (IC base=+0.194)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.125 (n=1048)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.555 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `4614.6151` → IC=+0.123 (n=253)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 4614.6151 (IC base=+0.091)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=441)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.088)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.134 (n=958)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.44 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.140 (n=234)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.088)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=3490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.355 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.232 (n=1559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` < `0.24` → IC=+0.360 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.24 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=1805)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.222)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=741)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.249 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=675)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `1317.494` → IC=+0.145 (n=828)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1317.494 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.216 (n=1508)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.216)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.409 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=655)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.289 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=812)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.183 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.375 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.219 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.116)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.205 (n=13974)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=14029)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.228 (n=6267)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.178 (n=3277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=3273)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=3330)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.238 (n=1309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.237 (n=1533)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.231)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.318 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.231)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.191 (n=3229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=3244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=2710)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.252 (n=2995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.331 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.242)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=3331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=2845)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.192 (n=2519)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.197 (n=1196)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.431 (n=604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=693)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `2181.7842` → IC=+0.433 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2181.7842 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.433 (n=265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.444 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `19915.0896` → IC=+0.444 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 19915.0896 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.444 (n=177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=261)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `3379.9672` → IC=+0.441 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3379.9672 (IC base=+0.429)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.203 (n=44050)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=19285)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=7585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=6042)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.198 (n=8353)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=7973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.281 (n=2781)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=7539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=6045)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=8001)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=3983)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.275 (n=2709)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=7310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.203 (n=5799)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=2871)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=3158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=3346)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=6751)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.125 (n=6280)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.2 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=6570)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.44` → IC=+0.135 (n=6227)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.44 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=3360)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.127 (n=3111)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.140 (n=3285)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.135 (n=3587)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.12` → IC=+0.145 (n=3096)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.12 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=3391)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.129 (n=3599)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.24` → IC=+0.133 (n=3139)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.24 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.315 (n=943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.289 (n=1322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.290)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `4196.1086` → IC=+0.301 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4196.1086 (IC base=+0.290)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.292 (n=628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.351 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `3804.2812` → IC=+0.291 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3804.2812 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.295 (n=663)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.389 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1438.1591` → IC=+0.305 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1438.1591 (IC base=+0.289)

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

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.443 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.439 (n=292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.447 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.460 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.442 (n=102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.452 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.444 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `2133.31` → IC=+0.457 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2133.31 (IC base=+0.443)

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
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=76)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.287 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=51)

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
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=76)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.287 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=51)

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
- **PATRÓN** `drift_60min` |x|≤ `0.37` → IC=+0.135 (n=9268)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.37 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9836` → IC=+0.242 (n=3510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9836 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2186` → IC=+0.255 (n=2368)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2186 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.434` → IC=+0.192 (n=2741)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.434 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.250 (n=1968)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.856 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6169` → IC=+0.255 (n=2951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6169 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.3028` → IC=+0.230 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3028 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.3293` → IC=+0.219 (n=3343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3293 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5655` → IC=+0.140 (n=12812)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5655 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.7454` → IC=+0.207 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7454 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.1486` → IC=+0.180 (n=4323)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1486 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.180 (n=4727)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.1951 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `0.6245` → IC=+0.179 (n=4727)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6245 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.227 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `1.568` → IC=+0.202 (n=7228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.568 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.215 (n=7907)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.071)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.218 (n=785)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.184 (n=781)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0079 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3485` → IC=+0.184 (n=2341)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3485 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.194 (n=1140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.275 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.773` → IC=+0.290 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.773 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.231 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.4359` → IC=+0.180 (n=2214)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4359 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.193 (n=2416)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2065.52` → IC=+0.183 (n=780)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2065.52 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.243 (n=1681)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.088` → IC=+0.266 (n=627)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.088 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=699)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0604` → IC=+0.284 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0604 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.552` → IC=+0.251 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.552 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.421` → IC=+0.237 (n=1967)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.421 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0942` → IC=+0.234 (n=1653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0942 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2849` → IC=+0.256 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2849 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6252` → IC=+0.253 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6252 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=2069)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.236 (n=823)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1794` → IC=+0.243 (n=1241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1794 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.234 (n=1873)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.9776` → IC=+0.261 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9776 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.1942` → IC=+0.221 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1942 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.3452` → IC=+0.223 (n=1737)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3452 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.769` → IC=+0.259 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.769 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.2485` → IC=+0.221 (n=1861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2485 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6189` → IC=+0.225 (n=1860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6189 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.242 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.7633` → IC=+0.219 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7633 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.4169` → IC=+0.242 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4169 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `16011.8358` → IC=+0.220 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16011.8358 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.149 (n=1859)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0056 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.160 (n=622)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=716)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=843)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7237` → IC=+0.176 (n=1859)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7237 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1305` → IC=+0.155 (n=1683)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1305 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.323` → IC=+0.143 (n=295)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 11.323 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.302` → IC=+0.143 (n=1702)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.302 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.1958` → IC=+0.145 (n=1859)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1958 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.6214` → IC=+0.136 (n=1859)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6214 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0979` → IC=+0.170 (n=676)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0979 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4565` → IC=+0.147 (n=1746)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4565 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7857` → IC=+0.144 (n=1165)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7857 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.169 (n=739)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 230.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.203 (n=2366)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.197 (n=2370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=2119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.369` → IC=+0.261 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.369 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.196 (n=2072)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.3499` → IC=+0.197 (n=315)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.3499 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.162` → IC=+0.203 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.162 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=2830)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `1972.7784` → IC=+0.201 (n=1073)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1972.7784 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.224 (n=1839)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.1778` → IC=+0.226 (n=920)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1778 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=969)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.0643` → IC=+0.238 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0643 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.697` → IC=+0.252 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.697 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.3471` → IC=+0.254 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3471 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.7208` → IC=+0.219 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7208 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.7264` → IC=+0.227 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7264 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1963.9614` → IC=+0.214 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1963.9614 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.215 (n=1901)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.213)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.157 (n=129)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=2824)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.150 (n=446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0036 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9602` → IC=+0.223 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9602 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1871` → IC=+0.323 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1871 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.971` → IC=+0.176 (n=932)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 4.971 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.329 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8553 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.340 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.3064` → IC=+0.340 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3064 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4292` → IC=+0.362 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4292 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.2171` → IC=+0.320 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2171 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.321 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.0987` → IC=+0.160 (n=739)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.0987 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.455` → IC=+0.204 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.455 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.154 (n=788)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8509 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.210 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.5277` → IC=+0.166 (n=1008)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5277 (IC base=+0.028)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.171 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=435)

- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.185 (n=128)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=384)

- **FILTRO** `ibs_20min` > `0.2302` → IC=-0.126 (n=2851)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2302
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=1405)

- **FILTRO** `sigma_ewma_delta_pct` > `8.806` → IC=-0.221 (n=442)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.806
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3814)

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

- **PATRÓN** `ibs_20min` < `0.2302` → IC=+0.138 (n=1405)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.2302 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.2491` → IC=+0.271 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2491 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.6807` → IC=+0.271 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6807 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.1602` → IC=+0.320 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1602 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.38` → IC=+0.291 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.38 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6369` → IC=-0.179 (n=746)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6369
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2244)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.208 (n=790)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2200)

- **FILTRO** `ibs_20min` > `0.7639` → IC=-0.208 (n=1107)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7639
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=3325)

- **PATRÓN** `dist_vwap_pct` > `0.4581` → IC=+0.312 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4581 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2747` → IC=+0.313 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2747 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` < `0.988` → IC=+0.298 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.988 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.6478` → IC=+0.313 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6478 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1029` → IC=+0.304 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1029 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.298 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `2.4802` → IC=+0.301 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4802 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.8611` → IC=+0.301 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8611 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.8075` → IC=+0.286 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8075 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` > `1.0691` → IC=+0.278 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0691 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.1003` → IC=+0.267 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1003 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.1667` → IC=+0.253 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1667 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` > `1.5313` → IC=+0.258 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5313 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.198 (n=4613)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0094 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.469` → IC=+0.187 (n=12339)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.469 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.6711` → IC=+0.283 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6711 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.691` → IC=+0.154 (n=6244)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.691 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `1.1763` → IC=+0.247 (n=5053)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1763 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `0.6923` → IC=+0.256 (n=4514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6923 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` < `0.0809` → IC=+0.242 (n=7468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0809 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.2947` → IC=+0.258 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2947 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.4688` → IC=+0.243 (n=2716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4688 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `2.6435` → IC=+0.256 (n=2716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6435 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.276 (n=7702)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.165 (n=4452)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0089 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.158 (n=11751)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5455 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.6724` → IC=+0.253 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6724 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.1707` → IC=+0.251 (n=3685)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1707 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1971` → IC=+0.259 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1971 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.307 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5914` → IC=+0.278 (n=2475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5914 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2837` → IC=+0.269 (n=2550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2837 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.282 (n=5533)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.259` → IC=-0.166 (n=961)

  - _Acción_: SKIP cuando `ibs_20min` < 0.259
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=2883)

- **FILTRO** `ibs_20min` > `0.7572` → IC=-0.172 (n=790)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7572
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=2374)

- **FILTRO** `sigma_ewma_delta_pct` > `4.629` → IC=-0.171 (n=706)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.629
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2458)

- **PATRÓN** `ibs_20min` > `0.9061` → IC=+0.270 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9061 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.31` → IC=+0.199 (n=678)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 7.31 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2262` → IC=+0.272 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2262 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `1.4454` → IC=+0.207 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4454 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.230 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.222 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.040)

- **PATRÓN** `ibs_20min` < `0.1631` → IC=+0.154 (n=792)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.1631 (IC base=-0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2235` → IC=+0.440 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2235 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.6397` → IC=+0.424 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6397 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.5249` → IC=+0.428 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5249 (IC base=-0.021)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.430 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8641` → IC=+0.158 (n=927)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.8641 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.1166` → IC=+0.193 (n=708)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1166 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.6802` → IC=+0.182 (n=1172)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6802 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2755` → IC=+0.218 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2755 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4286` → IC=+0.197 (n=430)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4286 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.4308` → IC=+0.188 (n=430)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4308 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.232 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 229.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1527` → IC=+0.226 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1527 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `0.6146` → IC=+0.230 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6146 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.308 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.565` → IC=+0.229 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.565 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1868` → IC=+0.234 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1868 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.273 (n=2087)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.258 (n=2104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.254 (n=2100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.786` → IC=+0.284 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.786 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.268 (n=1789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `1.6106` → IC=+0.259 (n=1999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6106 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=2473)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `2034.0327` → IC=+0.277 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2034.0327 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.302 (n=1745)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.1807` → IC=+0.302 (n=767)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1807 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.322 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.3602` → IC=+0.291 (n=1744)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3602 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.693` → IC=+0.301 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.693 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` < `0.1935` → IC=+0.282 (n=1696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1935 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.1196` → IC=+0.291 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1196 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.571` → IC=+0.300 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.571 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.6325` → IC=+0.291 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6325 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `2032.743` → IC=+0.298 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2032.743 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.287 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.286)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7664` → IC=-0.180 (n=801)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7664
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=2404)

- **PATRÓN** `ibs_20min` > `0.902` → IC=+0.168 (n=732)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.902 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.2112` → IC=+0.220 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2112 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` < `1.0103` → IC=+0.239 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0103 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.1712` → IC=+0.229 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1712 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.0821` → IC=+0.229 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0821 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.263 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.286 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.1234` → IC=+0.224 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1234 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `1.0451` → IC=+0.220 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0451 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.281 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.8566` → IC=+0.259 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8566 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.250 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7632` → IC=-0.186 (n=1469)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7632
  - _Potencial_: sin este filtro IC_bueno=+0.285 (n=1474)

- **FILTRO** `ibs_20min` > `0.6667` → IC=-0.246 (n=737)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2221)

- **FILTRO** `sigma_ewma_delta_pct` > `8.679` → IC=-0.233 (n=342)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.679
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=2616)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.285 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `1.0179` → IC=+0.337 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0179 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.71` → IC=+0.165 (n=463)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.71 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.86` → IC=+0.313 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.86 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `0.6366` → IC=+0.305 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6366 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.302 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2759` → IC=+0.329 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2759 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.7985` → IC=+0.317 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7985 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `2.4083` → IC=+0.299 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4083 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.327 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.132 (n=1954)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5667 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.2661` → IC=+0.240 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2661 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.7031` → IC=+0.263 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7031 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.1889` → IC=+0.229 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1889 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.0707` → IC=+0.262 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0707 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4456` → IC=+0.249 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4456 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.260 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.022)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.332 (n=1483)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.306 (n=778)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.321 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.2129` → IC=+0.320 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2129 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.76` → IC=+0.311 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.76 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.017` → IC=+0.289 (n=1877)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.017 (IC base=+0.288)

- **PATRÓN** `volumen_regimen` > `0.6275` → IC=+0.301 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6275 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.337 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.301 (n=1585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.288)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.290 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `2653.0544` → IC=+0.305 (n=1106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2653.0544 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.325 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.319 (n=1175)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1867` → IC=+0.288 (n=775)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1867 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.295 (n=886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.3679` → IC=+0.313 (n=1759)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3679 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.3053` → IC=+0.295 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3053 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.484` → IC=+0.301 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.484 (IC base=+0.287)

- **PATRÓN** `volumen_regimen` > `1.2272` → IC=+0.317 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2272 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.336 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.4225` → IC=+0.295 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4225 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.139` → IC=+0.289 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.139 (IC base=+0.287)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.188 (n=3439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0047 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.209 (n=3421)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.352` → IC=+0.185 (n=9027)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.352 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=10728)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.5675` → IC=+0.227 (n=10257)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5675 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.1712` → IC=+0.199 (n=4416)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1712 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.476` → IC=+0.251 (n=2062)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.476 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.167 (n=6826)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2068 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6301` → IC=+0.163 (n=6824)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6301 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2955` → IC=+0.200 (n=1522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2955 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.5662` → IC=+0.174 (n=4354)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5662 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.6103` → IC=+0.183 (n=3298)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6103 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `1999.8384` → IC=+0.178 (n=9163)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1999.8384 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.190 (n=9173)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 104.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.189 (n=6532)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0066 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.223 (n=3264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=3741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.4853` → IC=+0.232 (n=9779)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4853 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` < `0.1682` → IC=+0.170 (n=6800)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1682 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.32` → IC=+0.199 (n=1635)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.32 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.1777` → IC=+0.164 (n=7007)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1777 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.218 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `1.4462` → IC=+0.174 (n=3025)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4462 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.6131` → IC=+0.177 (n=3024)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.6131 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.185 (n=8739)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 106.0 (IC base=+0.176)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.229 (n=574)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.203 (n=574)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.3383` → IC=+0.218 (n=1719)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3383 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.201 (n=1722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.198 (n=1255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 12.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.9158` → IC=+0.283 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9158 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.324` → IC=+0.326 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.324 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.252 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.194 (n=1611)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.209 (n=1786)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.248 (n=1159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0041` → IC=+0.248 (n=1311)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0041 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0699` → IC=+0.306 (n=437)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0699 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.247 (n=1172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=659)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.1034` → IC=+0.277 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1034 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.286` → IC=+0.249 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.286 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.240 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.273 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4211` → IC=+0.254 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4211 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.6397` → IC=+0.240 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6397 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1980.22` → IC=+0.257 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1980.22 (IC base=+0.242)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.218 (n=683)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.1657` → IC=+0.185 (n=1031)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1657 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=1554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.3884` → IC=+0.225 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3884 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.2011` → IC=+0.212 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2011 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.528` → IC=+0.234 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.528 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.6929` → IC=+0.169 (n=680)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6929 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.0753` → IC=+0.162 (n=701)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.0753 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2838` → IC=+0.198 (n=246)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2838 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.4168` → IC=+0.187 (n=503)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4168 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `11927.4558` → IC=+0.162 (n=1381)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11927.4558 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.171 (n=646)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 235.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1615)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.2309` → IC=+0.173 (n=1421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2309 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.5918` → IC=+0.198 (n=1615)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5918 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1357` → IC=+0.170 (n=1603)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1357 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.889` → IC=+0.201 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.889 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.162 (n=1615)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2025 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1606` → IC=+0.147 (n=497)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1606 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4908` → IC=+0.153 (n=1501)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4908 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7719` → IC=+0.143 (n=1001)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7719 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.170 (n=474)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 207.0 (IC base=+0.142)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.215 (n=1716)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.4087` → IC=+0.218 (n=1510)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4087 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=1791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.543` → IC=+0.277 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.543 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.206 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.1281` → IC=+0.208 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1281 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.7707` → IC=+0.210 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7707 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.7274` → IC=+0.214 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7274 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `1960.7584` → IC=+0.228 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1960.7584 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.244 (n=1288)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.1435` → IC=+0.263 (n=644)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1435 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.280 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` < `0.3486` → IC=+0.250 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3486 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.677` → IC=+0.260 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.677 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.3506` → IC=+0.262 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3506 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.7245` → IC=+0.244 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7245 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.724` → IC=+0.234 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.724 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2032.0984` → IC=+0.241 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2032.0984 (IC base=+0.228)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.220 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.228)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.202 (n=727)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.203 (n=550)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1719)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.3317` → IC=+0.207 (n=1648)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3317 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1386` → IC=+0.187 (n=1072)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1386 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.002` → IC=+0.206 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.002 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8567` → IC=+0.159 (n=1099)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8567 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.170 (n=689)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4355` → IC=+0.169 (n=539)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4355 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.5292` → IC=+0.159 (n=538)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5292 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5059.0224` → IC=+0.196 (n=1098)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 5059.0224 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.153 (n=1584)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 150.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.161 (n=1512)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.006 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3806` → IC=+0.149 (n=1718)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3806 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.67` → IC=+0.185 (n=1718)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.67 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.879` → IC=+0.162 (n=596)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.879 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8556` → IC=+0.159 (n=1146)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8556 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.186 (n=262)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.8211` → IC=+0.140 (n=1061)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8211 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.5239` → IC=+0.129 (n=1422)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.5239 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `4380.8668` → IC=+0.165 (n=1145)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4380.8668 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.128 (n=1531)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 149.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.159 (n=851)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0098 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.444` → IC=+0.130 (n=1650)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.444 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=1923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.214 (n=1886)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `1.026` → IC=+0.216 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.026 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.919` → IC=+0.262 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.919 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.139 (n=1875)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2036 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.131 (n=1875)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6434 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.1642` → IC=+0.137 (n=1890)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1642 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.4408` → IC=+0.145 (n=604)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4408 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.4868` → IC=+0.132 (n=604)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4868 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=1965)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2895.2022` → IC=+0.205 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2895.2022 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.150 (n=1491)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 46.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.157 (n=829)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0061 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.103` → IC=+0.177 (n=627)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.103 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=1900)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.5778` → IC=+0.218 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5778 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.1956` → IC=+0.148 (n=1725)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1956 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.393` → IC=+0.133 (n=570)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 5.393 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.174` → IC=+0.132 (n=1880)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.174 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.155 (n=331)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4517` → IC=+0.137 (n=576)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4517 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `1.8144` → IC=+0.124 (n=1151)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.8144 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2755.5964` → IC=+0.185 (n=853)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2755.5964 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.129 (n=1685)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 52.0 (IC base=+0.121)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.233 (n=1570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.2839` → IC=+0.217 (n=1172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2839 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=1181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.6494` → IC=+0.247 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6494 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.1984` → IC=+0.215 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1984 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.2868` → IC=+0.209 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2868 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.6` → IC=+0.244 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.6 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.1875` → IC=+0.213 (n=1759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1875 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.6251` → IC=+0.218 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6251 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.277 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `2.4727` → IC=+0.212 (n=1705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4727 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.8141` → IC=+0.224 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8141 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2643.0166` → IC=+0.217 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2643.0166 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.229 (n=790)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0222` → IC=+0.222 (n=814)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0222 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.242 (n=600)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=887)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0196` → IC=+0.288 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0196 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `1.1462` → IC=+0.233 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1462 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.365` → IC=+0.252 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.365 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `0.6364` → IC=+0.229 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6364 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.276 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `1.4386` → IC=+0.217 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4386 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2615.2506` → IC=+0.223 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2615.2506 (IC base=+0.217)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.191 (n=1187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0041 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.170 (n=899)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0083 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3342` → IC=+0.178 (n=2374)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3342 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.187 (n=2462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.3357` → IC=+0.196 (n=2697)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3357 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.7717` → IC=+0.183 (n=430)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.7717 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.759` → IC=+0.194 (n=1166)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.759 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8705` → IC=+0.186 (n=1612)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8705 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.2057` → IC=+0.179 (n=806)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.2057 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1634` → IC=+0.178 (n=716)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1634 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4431` → IC=+0.183 (n=874)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4431 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.5336` → IC=+0.172 (n=873)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5336 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=3088)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2770.1155` → IC=+0.171 (n=2410)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2770.1155 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.185 (n=2477)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 147.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.156 (n=923)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0036 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=2607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.0725` → IC=+0.197 (n=923)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.0725 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.6979` → IC=+0.126 (n=1104)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.6979 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.0755` → IC=+0.128 (n=1055)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.0755 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4408` → IC=+0.147 (n=896)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4408 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2819.637` → IC=+0.130 (n=2471)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2819.637 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.128 (n=1155)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 29.0 (IC base=+0.111)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.202 (n=334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1007` → IC=+0.193 (n=333)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1007 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.188 (n=700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.6376` → IC=+0.204 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6376 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.2999` → IC=+0.167 (n=253)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2999 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.181` → IC=+0.175 (n=324)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.181 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.8832` → IC=+0.176 (n=505)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8832 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.1557` → IC=+0.154 (n=795)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.1557 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.153 (n=298)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.2348` → IC=+0.159 (n=651)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.2348 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5264` → IC=+0.153 (n=661)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5264 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `14653.7158` → IC=+0.163 (n=505)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 14653.7158 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.198 (n=322)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 148.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.195 (n=296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0027 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.34` → IC=+0.157 (n=887)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.34 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.147 (n=896)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.611` → IC=+0.183 (n=781)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.611 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1864` → IC=+0.160 (n=885)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1864 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.564` → IC=+0.149 (n=936)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.564 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.208` → IC=+0.144 (n=887)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.208 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `1.0687` → IC=+0.166 (n=402)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0687 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.203 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.121` → IC=+0.162 (n=772)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.121 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.77` → IC=+0.147 (n=585)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.77 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1148)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `12062.2629` → IC=+0.144 (n=792)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 12062.2629 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `348.0` → IC=+0.155 (n=855)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 348.0 (IC base=+0.144)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.235 (n=572)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.2023` → IC=+0.214 (n=572)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2023 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.6723` → IC=+0.249 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6723 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.3558` → IC=+0.204 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3558 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.2068` → IC=+0.204 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2068 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.086` → IC=+0.223 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.086 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.8419` → IC=+0.204 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8419 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.1833` → IC=+0.226 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1833 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.233 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.4274` → IC=+0.223 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4274 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.4732` → IC=+0.225 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4732 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.150 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0038 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.131 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 11.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.0873` → IC=+0.162 (n=273)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.0873 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.459` → IC=+0.154 (n=212)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 6.459 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.6877` → IC=+0.152 (n=360)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6877 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.136 (n=289)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `4077.438` → IC=+0.132 (n=731)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 4077.438 (IC base=+0.107)

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

- **PATRÓN** `volumen_regimen` > `0.7239` → IC=+0.167 (n=547)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.7239 (IC base=+0.159)

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
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.180 (n=4430)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.212 (n=4433)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=13934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.9912` → IC=+0.309 (n=4430)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9912 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1642` → IC=+0.186 (n=5022)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1642 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.406` → IC=+0.245 (n=3263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.406 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.2331` → IC=+0.165 (n=8902)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2331 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.200 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6011` → IC=+0.197 (n=4285)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6011 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `1984.2` → IC=+0.181 (n=11868)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1984.2 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.203 (n=10508)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.195 (n=5287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0052 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.1462` → IC=+0.195 (n=5268)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1462 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=4536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.239 (n=11986)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5714 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.1736` → IC=+0.167 (n=7070)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1736 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.111` → IC=+0.210 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.111 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.059` → IC=+0.160 (n=7135)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.059 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2897` → IC=+0.248 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2897 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `1.8619` → IC=+0.191 (n=7463)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.8619 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.207 (n=7261)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.185)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.252 (n=736)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.225 (n=737)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.3504` → IC=+0.209 (n=2204)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3504 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=1071)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.208 (n=1476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.328 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.766` → IC=+0.347 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.766 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.268 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.5831` → IC=+0.221 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5831 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=2259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `1996.3386` → IC=+0.208 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1996.3386 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.263 (n=1599)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.261 (n=1821)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1233` → IC=+0.280 (n=801)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1233 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=1646)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.359` → IC=+0.284 (n=1599)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.359 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.511` → IC=+0.266 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.511 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.286 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6325` → IC=+0.280 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6325 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=2000)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1988.6158` → IC=+0.266 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1988.6158 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.209 (n=713)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1788` → IC=+0.165 (n=1420)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1788 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=2240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.2815` → IC=+0.207 (n=2129)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2815 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1284` → IC=+0.187 (n=1195)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1284 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.719` → IC=+0.176 (n=356)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.719 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.232` → IC=+0.154 (n=1949)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.232 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.6276` → IC=+0.171 (n=710)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6276 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.192 (n=306)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1476` → IC=+0.160 (n=1823)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1476 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5244` → IC=+0.156 (n=1851)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5244 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `276.0` → IC=+0.182 (n=886)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 276.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1770)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2579` → IC=+0.161 (n=1557)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.2579 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.146 (n=804)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6871` → IC=+0.194 (n=1769)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.6871 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1329` → IC=+0.165 (n=1615)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1329 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.56` → IC=+0.161 (n=299)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.56 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.346` → IC=+0.145 (n=1598)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.346 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.1862` → IC=+0.157 (n=1769)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1862 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1543` → IC=+0.199 (n=473)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1543 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4364` → IC=+0.153 (n=1668)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4364 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7778` → IC=+0.159 (n=1112)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7778 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `416.0` → IC=+0.143 (n=1385)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 416.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.234 (n=2183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=2183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.227 (n=2199)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.435` → IC=+0.303 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.435 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` < `0.2044` → IC=+0.227 (n=2197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2044 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.615` → IC=+0.229 (n=2100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.615 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2602)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2040.9736` → IC=+0.241 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2040.9736 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.243 (n=1803)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1804` → IC=+0.250 (n=901)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1804 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.260 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=954)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0152` → IC=+0.303 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0152 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.96` → IC=+0.285 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.96 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3416` → IC=+0.293 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3416 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7067` → IC=+0.241 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7067 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1309` → IC=+0.240 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1309 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1958.2205` → IC=+0.244 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1958.2205 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.254 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=1005)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3326` → IC=+0.153 (n=2001)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3326 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2701` → IC=+0.190 (n=2275)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2701 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.5335` → IC=+0.167 (n=619)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.5335 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.171` → IC=+0.151 (n=929)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.171 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8743` → IC=+0.161 (n=1516)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8743 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1667` → IC=+0.174 (n=599)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1667 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.529` → IC=+0.162 (n=974)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.529 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1928` → IC=+0.150 (n=1003)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1928 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7316.3105` → IC=+0.236 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7316.3105 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.181 (n=719)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 70.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.187 (n=615)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0033 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.3462` → IC=+0.142 (n=1614)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3462 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=677)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.137 (n=637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.735` → IC=+0.184 (n=1834)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.735 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.337` → IC=+0.173 (n=374)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.337 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.876` → IC=+0.141 (n=1223)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.876 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2976` → IC=+0.231 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2976 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.444` → IC=+0.142 (n=1759)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.444 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `8613.5062` → IC=+0.200 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8613.5062 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.133 (n=1757)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 166.0 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.136 (n=2289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0055 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.4545` → IC=+0.202 (n=2286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4545 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `1.0123` → IC=+0.211 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0123 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.529` → IC=+0.243 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.529 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8916` → IC=+0.149 (n=1524)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8916 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1625` → IC=+0.129 (n=2353)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1625 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.126 (n=303)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.1968` → IC=+0.138 (n=1008)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.1968 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2334)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2556.0551` → IC=+0.238 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2556.0551 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.148 (n=697)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 27.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.175 (n=728)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0056 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.1294` → IC=+0.169 (n=726)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1294 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6316` → IC=+0.213 (n=2178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6316 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.2143` → IC=+0.140 (n=1798)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2143 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.315` → IC=+0.130 (n=298)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 9.315 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.49` → IC=+0.134 (n=2099)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.49 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.7133` → IC=+0.160 (n=958)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7133 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.183 (n=354)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `2.1596` → IC=+0.139 (n=1769)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.1596 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2804.9182` → IC=+0.199 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2804.9182 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.142 (n=1765)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 50.0 (IC base=+0.123)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.234 (n=2215)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=2324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.222 (n=1593)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.265 (n=1983)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.2086` → IC=+0.235 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2086 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.623` → IC=+0.257 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.623 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `1.2349` → IC=+0.222 (n=2215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2349 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `0.6422` → IC=+0.223 (n=2215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6422 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2366` → IC=+0.247 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2366 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.5113` → IC=+0.248 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5113 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=2069)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2646.4017` → IC=+0.229 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2646.4017 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.217 (n=778)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.229 (n=1057)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.231 (n=1656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.4167` → IC=+0.264 (n=2049)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4167 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `1.1616` → IC=+0.216 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1616 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.2936` → IC=+0.219 (n=2178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2936 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.876` → IC=+0.256 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.876 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.2318` → IC=+0.244 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2318 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.282 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.432` → IC=+0.216 (n=2136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.432 (IC base=+0.215)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.168 (n=3905)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.228 (n=1334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3886` → IC=+0.199 (n=3505)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3886 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=1494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.190 (n=1785)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.241 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.17` → IC=+0.197 (n=1496)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.17 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.212` → IC=+0.214 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.212 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.7093` → IC=+0.196 (n=1222)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.7093 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` > `0.89` → IC=+0.193 (n=1850)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.89 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.169` → IC=+0.217 (n=1122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.169 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.459` → IC=+0.192 (n=1309)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.459 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.6322` → IC=+0.197 (n=1310)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6322 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=2959)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `3816.9421` → IC=+0.197 (n=2655)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3816.9421 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.217 (n=989)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3799` → IC=+0.187 (n=2588)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3799 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=1039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.185 (n=1319)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 6.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` < `0.1802` → IC=+0.190 (n=1294)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.1802 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.6343` → IC=+0.183 (n=547)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6343 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.201` → IC=+0.173 (n=2932)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 6.201 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `1.2562` → IC=+0.171 (n=2776)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2562 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.170 (n=2683)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2231` → IC=+0.170 (n=607)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2231 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `2.5555` → IC=+0.169 (n=2901)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.5555 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.8277` → IC=+0.176 (n=1934)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.8277 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=3905)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `188.0` → IC=+0.177 (n=2524)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 188.0 (IC base=+0.166)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.235 (n=462)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.263 (n=175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.233 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.7622` → IC=+0.217 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7622 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.3165` → IC=+0.221 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3165 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.039` → IC=+0.231 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.039 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.526` → IC=+0.213 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.526 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.221 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.5931` → IC=+0.221 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5931 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `2.2945` → IC=+0.220 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2945 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `12467.3842` → IC=+0.235 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12467.3842 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.228 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3655` → IC=+0.161 (n=1061)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3655 (IC base=+0.148)

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

- **PATRÓN** `dist_vwap_pct` < `0.211` → IC=+0.149 (n=1076)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.211 (IC base=+0.148)

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
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.219 (n=400)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.1496` → IC=+0.218 (n=526)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1496 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.195 (n=546)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` < `0.5225` → IC=+0.207 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5225 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.8854` → IC=+0.198 (n=399)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.8854 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.14` → IC=+0.206 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.14 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.152` → IC=+0.201 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.152 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `1.082` → IC=+0.199 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.082 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` > `1.2441` → IC=+0.196 (n=399)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.2441 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.195 (n=1099)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.208 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `2.4777` → IC=+0.200 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4777 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=1199)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.226 (n=316)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.3836` → IC=+0.195 (n=834)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3836 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.174 (n=636)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 10.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.7588` → IC=+0.170 (n=948)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7588 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.0908` → IC=+0.170 (n=948)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.0908 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.6041` → IC=+0.186 (n=205)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6041 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.654` → IC=+0.169 (n=970)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.654 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.6426` → IC=+0.201 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6426 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.7253` → IC=+0.164 (n=847)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.7253 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` < `0.1511` → IC=+0.166 (n=979)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.1511 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.183 (n=399)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.1949` → IC=+0.181 (n=817)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.1949 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.7864` → IC=+0.167 (n=619)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.7864 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `7427.0836` → IC=+0.179 (n=948)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7427.0836 (IC base=+0.164)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.220 (n=344)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3083` → IC=+0.184 (n=343)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3083 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.204 (n=481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.253 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.1981` → IC=+0.207 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1981 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.514` → IC=+0.219 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.514 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `0.8838` → IC=+0.190 (n=343)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8838 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `1.2781` → IC=+0.184 (n=172)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.2781 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1634` → IC=+0.222 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1634 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.468` → IC=+0.193 (n=500)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.468 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=620)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `3406.9619` → IC=+0.222 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3406.9619 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.195 (n=440)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 48.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.185 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0059 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.216 (n=174)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3764` → IC=+0.236 (n=256)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3764 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.187 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 16.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.215 (n=268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.1852` → IC=+0.237 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1852 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.7855` → IC=+0.229 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7855 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.236` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.236 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.048` → IC=+0.186 (n=329)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 3.048 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.9715` → IC=+0.194 (n=256)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.9715 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.221 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.631` → IC=+0.193 (n=164)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.631 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.202 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `3848.659` → IC=+0.190 (n=256)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3848.659 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.218 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.182)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.154 (n=571)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0038 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.4548` → IC=+0.157 (n=1206)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.4548 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1425` → IC=+0.141 (n=663)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1425 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.448` → IC=+0.187 (n=276)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.448 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.182 (n=168)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.243 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` < `0.1153` → IC=+0.129 (n=505)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1153 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.074` → IC=+0.127 (n=429)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 4.074 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.146` → IC=+0.180 (n=120)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.146 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.135 (n=439)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.5975 (IC base=+0.049)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.143 (n=443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0058 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4181` → IC=+0.175 (n=411)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.4181 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1286` → IC=+0.161 (n=219)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1286 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.571` → IC=+0.129 (n=243)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 3.571 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `2.5088` → IC=+0.125 (n=369)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.5088 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.122 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0036 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.289 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.1953` → IC=+0.124 (n=267)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1953 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.157` → IC=+0.141 (n=235)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 7.157 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.0709` → IC=+0.136 (n=97)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.0709 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.5595` → IC=+0.129 (n=219)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.5595 (IC base=+0.073)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.154 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=158)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.156 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0046 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.131 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.6872` → IC=+0.209 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6872 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.123` → IC=+0.174 (n=219)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.123 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.447` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.447 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.8141` → IC=+0.126 (n=265)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.8141 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.7915` → IC=+0.132 (n=229)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.7915 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `1167.2157` → IC=+0.149 (n=351)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1167.2157 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.7041` → IC=+0.150 (n=135)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.7041 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2423` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2423 (IC base=+0.005)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.236 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=156)

- **FILTRO** `ibs_20min` > `0.1875` → IC=-0.314 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1875
  - _Potencial_: sin este filtro IC_bueno=+0.256 (n=125)

- **PATRÓN** `ibs_20min` > `0.7727` → IC=+0.175 (n=266)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.7727 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` > `0.712` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.712 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.144` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 8.144 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.051)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.169 (n=137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0081 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.1875` → IC=+0.256 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1875 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` < `0.1829` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1829 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.936` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.936 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8172` → IC=+0.128 (n=84)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8172 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.0794` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0794 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `2.1886` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.1886 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `1.4839` → IC=+0.174 (n=93)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.4839 (IC base=+0.050)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` < `5.0` → IC=-0.203 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=137)

- **FILTRO** `dist_vwap_pct` > `0.2351` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2351
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=240)

- **FILTRO** `volumen_regimen` < `0.7435` → IC=-0.348 (n=64)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7435
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=192)

- **FILTRO** `volumen_spike_ratio` > `2.9666` → IC=-0.202 (n=45)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.9666
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=137)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.206 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=207)

- **FILTRO** `sigma_h` > `0.0054` → IC=-0.377 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=168)

- **FILTRO** `dist_vwap_pct` > `0.3287` → IC=-0.389 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3287
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=189)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=193)

- **FILTRO** `volumen_pendiente_norm` > `0.0549` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0549
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=112)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.221 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=42)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=48)

- **FILTRO** `volumen_regimen` < `0.8402` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8402
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=63)

- **FILTRO** `volumen_spike_ratio` > `3.1256` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.1256
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=40)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.300 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=72)

- **FILTRO** `sigma_ewma_delta_pct` > `2.335` → IC=-0.288 (n=31)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.335
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=64)

- **FILTRO** `volumen_regimen` > `0.8359` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8359
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=72)

- **FILTRO** `volumen_regimen` < `0.5486` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.5486
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=72)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0026` → IC=-0.370 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=64)

- **FILTRO** `ibs_20min` < `0.6002` → IC=-0.467 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6002
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=57)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.354 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=44)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=55)

- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9583 (IC base=-0.155)

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
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.178 (n=181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0057 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.129 (n=195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 15.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.6616` → IC=+0.142 (n=398)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6616 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.4722` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.4722 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.657` → IC=+0.137 (n=133)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.657 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.1711` → IC=+0.122 (n=294)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1711 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.5351` → IC=+0.162 (n=131)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5351 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.160 (n=369)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.156 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.988` → IC=+0.188 (n=123)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 8.988 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `2753.3423` → IC=+0.138 (n=280)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2753.3423 (IC base=+0.070)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6472` → IC=-0.256 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6472
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=120)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.184 (n=169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0024 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.151 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.191 (n=189)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1524 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.0931` → IC=+0.148 (n=194)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.0931 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.925` → IC=+0.171 (n=153)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 4.925 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.6197` → IC=+0.160 (n=189)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6197 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` < `0.1846` → IC=+0.177 (n=159)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.1846 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.2515` → IC=+0.179 (n=138)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.2515 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4468` → IC=+0.160 (n=157)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.4468 (IC base=+0.140)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1638` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1638
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=109)

- **FILTRO** `libro_liquidez` < `1529.3843` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `libro_liquidez` < 1529.3843
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=129)

- **PATRÓN** `volumen_spike_ratio` < `1.8285` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8285 (IC base=+0.052)

- **PATRÓN** `libro_liquidez` > `1529.3843` → IC=+0.126 (n=129)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1529.3843 (IC base=+0.052)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.132 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 12.0 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.3236` → IC=+0.127 (n=148)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.3236 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.497` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.497 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.058)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `dist_vwap_pct` > `0.2724` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2724
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=89)

- **FILTRO** `volumen_regimen` < `1.0339` → IC=-0.167 (n=55)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0339
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=56)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.197)

- **PATRÓN** `elapsed_s` > `184.2` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.2 (IC base=+0.197)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.197)

- **PATRÓN** `drift_15min` |x|≤ `1.3142` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.3142 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.271 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.197)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.197)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.197)

- **PATRÓN** `elapsed_s` > `184.2` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.2 (IC base=+0.197)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.197)

- **PATRÓN** `drift_15min` |x|≤ `1.3142` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.3142 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.271 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.197)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.197)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=998)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2857.8344` → IC=+0.141 (n=466)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2857.8344 (IC base=+0.103)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=998)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2857.8344` → IC=+0.141 (n=466)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2857.8344 (IC base=+0.103)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=150)

- **FILTRO** `libro_liquidez` < `10077.5355` → IC=-0.185 (n=109)

  - _Acción_: SKIP cuando `libro_liquidez` < 10077.5355
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=57)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=239)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=225)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=49)

- **FILTRO** `hora_utc` < `3.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=53)

- **FILTRO** `libro_liquidez` < `10893.2451` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 10893.2451
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=52)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.133 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

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
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=2701)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=97)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=97)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=105)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.126 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 15.0 (IC base=+0.055)

- **PATRÓN** `libro_liquidez` > `2582.9138` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2582.9138 (IC base=+0.055)

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

- **PATRÓN** `liq_usd_total` > `59740.4` → IC=+0.137 (n=144)

  - _Acción_: Kelly boost +0.68€ cuando `liq_usd_total` > 59740.4 (IC base=+0.044)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.133 (n=175)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.495 (IC base=+0.044)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=1027)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=981)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=617)

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
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=342)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.495 (IC base=+0.031)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=770)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=770)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=604)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=551)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=551)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=212)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=212)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=174)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=139)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=138)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=162)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=151)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=301)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=301)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=201)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.142 (n=702)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1768)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.146 (n=588)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.47 (IC base=+0.024)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.517` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.517
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=12)

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
- **FILTRO** `py_entrada` < `0.52` → IC=-0.130 (n=171)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=67)

- **FILTRO** `profundidad_ratio` < `228.3` → IC=-0.138 (n=78)

  - _Acción_: SKIP cuando `profundidad_ratio` < 228.3
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=160)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.220 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.049)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `restante_min` < `8.28` → IC=-0.167 (n=40)

  - _Acción_: SKIP cuando `restante_min` < 8.28
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=122)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.147 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=113)

- **FILTRO** `lag_apertura_s` > `402.96` → IC=-0.167 (n=40)

  - _Acción_: SKIP cuando `lag_apertura_s` > 402.96
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=122)

- **FILTRO** `profundidad_ratio` < `31.0` → IC=-0.130 (n=106)

  - _Acción_: SKIP cuando `profundidad_ratio` < 31.0
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=56)

- **PATRÓN** `py_entrada` < `0.519` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.519 (IC base=+0.014)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=118)

- **FILTRO** `restante_min` < `3.74` → IC=-0.131 (n=82)

  - _Acción_: SKIP cuando `restante_min` < 3.74
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=83)

- **FILTRO** `lag_apertura_s` > `75.7` → IC=-0.131 (n=82)

  - _Acción_: SKIP cuando `lag_apertura_s` > 75.7
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=83)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.245 (n=45)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=173)

- **FILTRO** `profundidad_ratio` < `53.7` → IC=-0.185 (n=71)

  - _Acción_: SKIP cuando `profundidad_ratio` < 53.7
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=147)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.239 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=183)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.123 (n=75)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.5 (IC base=-0.015)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.141 (n=179)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=105)

- **FILTRO** `restante_min` < `3.4` → IC=-0.226 (n=93)

  - _Acción_: SKIP cuando `restante_min` < 3.4
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=191)

- **FILTRO** `lag_apertura_s` > `94.28` → IC=-0.225 (n=96)

  - _Acción_: SKIP cuando `lag_apertura_s` > 94.28
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=188)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.172 (n=62)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` < 0.45 (IC base=+0.032)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=164)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.45` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.45 (IC base=+0.012)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.138 (n=172)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=93)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` > 0.5 (IC base=-0.036)

- **PATRÓN** `profundidad_ratio` > `14.7` → IC=+0.147 (n=66)

  - _Acción_: Kelly boost +0.74€ cuando `profundidad_ratio` > 14.7 (IC base=+0.036)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.198 (n=84)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=246)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.163 (n=4746)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14304)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.165 (n=4908)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=14787)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.194 (n=840)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=2540)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.148 (n=824)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=2705)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.121 (n=1635)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.5 (IC base=+0.016)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.174 (n=854)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=2578)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.198 (n=828)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=2748)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.162 (n=814)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=2570)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2508)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3248)

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
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=297)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1991.6564` → IC=-0.164 (n=334)

  - _Acción_: SKIP cuando `libro_liquidez` < 1991.6564
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=680)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=13191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=29662)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=10066)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=32787)

- **FILTRO** `ibs_7min` < `0.2609` → IC=-0.234 (n=10711)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2609
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=32142)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=14418)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=28435)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.235 (n=13142)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=41252)

- **FILTRO** `ibs_7min` > `0.2879` → IC=-0.178 (n=13595)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2879
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=40799)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.143 (n=2143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=5143)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.235 (n=3593)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=3693)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.252 (n=2401)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=4885)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.187 (n=1568)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5718)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.266 (n=2294)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=7151)

- **FILTRO** `ibs_7min` > `0.7805` → IC=-0.210 (n=2361)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7805
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=7084)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.132 (n=1733)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5597)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.247 (n=1805)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=5525)

- **FILTRO** `ibs_7min` < `0.7415` → IC=-0.197 (n=1830)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7415
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=5500)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.181 (n=1832)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=5498)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=1766)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=5666)

- **FILTRO** `ibs_7min` > `0.2659` → IC=-0.191 (n=1857)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2659
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5575)

- **FILTRO** `ballena_activa_n` > `149.0` → IC=-0.189 (n=1852)

  - _Acción_: SKIP cuando `ballena_activa_n` > 149.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5580)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.163 (n=1710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=5237)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.317 (n=1642)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=5305)

- **FILTRO** `ibs_7min` < `0.7038` → IC=-0.245 (n=2292)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7038
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4655)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.217 (n=1559)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5388)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.244 (n=2272)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=7767)

- **FILTRO** `ibs_7min` > `0.7377` → IC=-0.173 (n=2509)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7377
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=7530)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=2266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4776)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.240 (n=2083)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4959)

- **FILTRO** `ibs_7min` < `0.7409` → IC=-0.183 (n=1760)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7409
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5282)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.184 (n=1738)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5304)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.268 (n=1792)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=5461)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.182 (n=1812)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5441)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.183 (n=1757)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5496)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.272 (n=1684)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=5552)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.232 (n=1784)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=5452)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=2453)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=7917)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.277 (n=1675)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=5337)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.221 (n=1753)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5259)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.200 (n=1717)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=5295)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.206 (n=2421)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=7434)

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

- **FILTRO** `py_entrada` > `0.54` → IC=-0.139 (n=164)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=499)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

- **FILTRO** `libro_liquidez` < `7941.0101` → IC=-0.131 (n=348)

  - _Acción_: SKIP cuando `libro_liquidez` < 7941.0101
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=707)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=356)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=410)

- **FILTRO** `libro_liquidez` < `3306.2556` → IC=-0.153 (n=165)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.2556
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=495)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.137 (n=936)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.136 (n=429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 14.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `441.7389` → IC=+0.153 (n=312)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 441.7389 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.142 (n=300)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 14.0 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4377` → IC=+0.167 (n=73)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4377 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.232 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `2615.3166` → IC=+0.220 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2615.3166 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.194 (n=96)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 11.0 (IC base=+0.145)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 10.0 (IC base=+0.104)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.174 (n=127)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.202 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `384.1453` → IC=+0.209 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 384.1453 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.186 (n=84)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 73.0 (IC base=+0.116)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.182 (n=168)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.224 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.149)

- **PATRÓN** `total_vol_5m` < `8043.774` → IC=+0.171 (n=168)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 8043.774 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 28.0 (IC base=+0.149)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=112)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `3599.4239` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3599.4239 (IC base=+0.097)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.6961` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.6961
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=122)

- **FILTRO** `sigma_h` > `0.0035` → IC=-0.199 (n=400)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0035
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=134)

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
- **FILTRO** `sigma_h` > `0.0058` → IC=-0.189 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=25)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `71.8388` → IC=-0.155 (n=363)

  - _Acción_: SKIP cuando `T_h` > 71.8388
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=122)

- **FILTRO** `pct_vs_K` |x|> `3.7555` → IC=-0.256 (n=121)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7555
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=364)

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
- **FILTRO** `sigma_h` < `0.0049` → IC=-0.261 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=90)

- **FILTRO** `T_h` > `135.986` → IC=-0.265 (n=32)

  - _Acción_: SKIP cuando `T_h` > 135.986
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=102)

- **FILTRO** `sigma_h` > `0.0088` → IC=-0.348 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=97)

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.318 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=97)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` > `0.006` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `T_h` > `113.6692` → IC=-0.156 (n=59)

  - _Acción_: SKIP cuando `T_h` > 113.6692
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=61)

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

- **PATRÓN** `T_h` > `0.4292` → IC=+0.377 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4292 (IC base=+0.338)

- **PATRÓN** `dist_50` > `0.3298` → IC=+0.418 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3298 (IC base=+0.338)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.357 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.338)

- **PATRÓN** `edge` > `0.0946` → IC=+0.456 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0946 (IC base=+0.421)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.451 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.421)

- **PATRÓN** `T_h` < `0.9804` → IC=+0.426 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9804 (IC base=+0.421)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.452 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.421)

- **PATRÓN** `dist_50` > `0.3811` → IC=+0.478 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3811 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.476 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.421)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1026` → IC=+0.454 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1026 (IC base=+0.425)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.413 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.425)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.457 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.425)

- **PATRÓN** `T_h` < `1.0313` → IC=+0.454 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0313 (IC base=+0.425)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.417 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.425)

- **PATRÓN** `dist_50` > `0.4122` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4122 (IC base=+0.425)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.425)

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

- **PATRÓN** `edge` > `0.1155` → IC=+0.472 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1155 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0148` → IC=+0.483 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0148 (IC base=+0.465)

- **PATRÓN** `T_h` > `0.77` → IC=+0.467 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.77 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.491 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.469 (n=129)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=249)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=337)

- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.023)

- **PATRÓN** `streak_estiramiento` < `0.437` → IC=+0.200 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.437 (IC base=+0.039)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=25)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4881` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4881
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=55)

- **FILTRO** `ballena_activa_n` > `51.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 51.0
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=57)

- **PATRÓN** `volumen_racha` < `945898.4` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_racha` < 945898.4 (IC base=+0.013)

- **PATRÓN** `streak_estiramiento` < `0.4177` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `streak_estiramiento` < 0.4177 (IC base=+0.013)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.140 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 10.0 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 48.0 (IC base=+0.077)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=89)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=95)

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
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=576)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` > `3.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `libro_liquidez` < `2775.6672` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 2775.6672
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

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
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=798)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=947)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=947)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3468)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1821)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.197 (n=817)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0042 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.236 (n=817)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.1592` → IC=+0.201 (n=2156)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1592 (IC base=+0.194)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2223` → IC=+0.200 (n=817)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2223 (IC base=+0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1307` → IC=+0.217 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1307 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=2450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.196 (n=2523)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `ibs_15` > `0.6077` → IC=+0.272 (n=2450)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6077 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.1207` → IC=+0.197 (n=1214)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1207 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.915` → IC=+0.274 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.915 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `7103.48` → IC=+0.206 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7103.48 (IC base=+0.194)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1038)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.229 (n=426)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.274 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.214)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2014` → IC=+0.242 (n=219)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2014 (IC base=+0.214)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.251 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `ibs_15` > `0.7143` → IC=+0.276 (n=484)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7143 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.1382` → IC=+0.245 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1382 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.772` → IC=+0.290 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.772 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `16217.9862` → IC=+0.250 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16217.9862 (IC base=+0.214)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.548` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.548
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=612)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.167 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0033 (IC base=+0.135)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.138 (n=241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0057 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.148 (n=234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.135)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2368` → IC=+0.154 (n=177)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.2368 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.157 (n=202)

  - _Acción_: Kelly boost +0.78€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.141 (n=555)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.5749` → IC=+0.234 (n=531)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5749 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.145 (n=294)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1534 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.2646` → IC=+0.138 (n=495)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2646 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.827` → IC=+0.243 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.827 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `3470.8581` → IC=+0.146 (n=475)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3470.8581 (IC base=+0.135)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `20.733` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.733
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=201)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.163 (n=158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0054 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.244 (n=119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1941` → IC=+0.192 (n=358)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1941 (IC base=+0.157)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0615` → IC=+0.166 (n=357)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio_macro` |x|> 0.0615 (IC base=+0.157)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3457` → IC=+0.199 (n=310)

  - _Acción_: Kelly boost +0.99€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3457 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.168 (n=242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 12.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.160 (n=368)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 17.0 (IC base=+0.157)

- **PATRÓN** `ibs_15` > `0.5152` → IC=+0.244 (n=358)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5152 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` < `0.3286` → IC=+0.171 (n=350)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.3286 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.263` → IC=+0.272 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.263 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=395)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `3001.7364` → IC=+0.179 (n=238)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3001.7364 (IC base=+0.157)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.788` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 15.788 (IC base=+0.000)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.253 (n=536)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.215 (n=265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.044` → IC=+0.216 (n=600)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.044 (IC base=+0.212)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0888` → IC=+0.259 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0888 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.241 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` > `0.5854` → IC=+0.292 (n=600)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5854 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.2029` → IC=+0.221 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2029 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.77` → IC=+0.242 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.77 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.408` → IC=+0.214 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.408 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2955.5044` → IC=+0.292 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2955.5044 (IC base=+0.212)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.156 (n=647)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1111 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.362 (n=353)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.357)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.377 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.357)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.356 (n=353)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.357)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.381 (n=352)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.357)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1356` → IC=+0.393 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1356 (IC base=+0.357)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.373 (n=535)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.357)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.393 (n=529)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.357)

- **PATRÓN** `dist_vwap_pct` > `0.4165` → IC=+0.388 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4165 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.370 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.357)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.363 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.357)

- **PATRÓN** `libro_liquidez` > `3823.0046` → IC=+0.369 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3823.0046 (IC base=+0.357)

- **PATRÓN** `ballena_activa_n` < `443.0` → IC=+0.376 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 443.0 (IC base=+0.357)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.359 (n=253)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.357)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.367 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.357)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.357 (n=96)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.357)

- **PATRÓN** `drift_15min` |x|≤ `0.5096` → IC=+0.361 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5096 (IC base=+0.357)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1528` → IC=+0.381 (n=191)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1528 (IC base=+0.357)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.393 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.357)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.376 (n=289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.357)

- **PATRÓN** `ibs_15` > `0.8057` → IC=+0.386 (n=287)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8057 (IC base=+0.357)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.397 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.859` → IC=+0.370 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.859 (IC base=+0.357)

- **PATRÓN** `libro_liquidez` > `16049.8465` → IC=+0.388 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.8465 (IC base=+0.357)

- **PATRÓN** `ballena_activa_n` < `500.0` → IC=+0.406 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 500.0 (IC base=+0.357)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.354 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.355)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.375 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.355)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.366 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.355)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.372 (n=217)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.355)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2986` → IC=+0.380 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2986 (IC base=+0.355)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.415 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.355)

- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.402 (n=243)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.355)

- **PATRÓN** `dist_vwap_pct` > `0.4419` → IC=+0.365 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4419 (IC base=+0.355)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.356 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2815 (IC base=+0.355)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.939` → IC=+0.375 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.939 (IC base=+0.355)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.354 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.355)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.362 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.355)

- **PATRÓN** `libro_liquidez` > `4278.0994` → IC=+0.380 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4278.0994 (IC base=+0.355)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.363 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.355)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.224 (n=884)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2653)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.204 (n=1311)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2226)

- **PATRÓN** `delta_ratio_macro` |x|> `0.14` → IC=+0.177 (n=567)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.14 (IC base=-0.067)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.229 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.276 (n=850)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1071` → IC=+0.200 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1071 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2596` → IC=+0.192 (n=702)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.2596 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1287` → IC=+0.257 (n=1834)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1287 (IC base=-0.016)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1883` → IC=+0.249 (n=1795)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1883 (IC base=-0.016)

- **PATRÓN** `ibs_15` < `0.3508` → IC=+0.278 (n=2750)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3508 (IC base=-0.016)

- **PATRÓN** `dist_vwap_pct` > `0.8426` → IC=+0.295 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8426 (IC base=-0.016)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.216 (n=502)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1510)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.227 (n=503)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=1509)

- **FILTRO** `sigma_ewma_delta_pct` > `23.719` → IC=-0.266 (n=289)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.719
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=1723)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.180 (n=201)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0027 (IC base=+0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2011` → IC=+0.302 (n=114)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2011 (IC base=+0.086)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.307 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.7503` → IC=+0.327 (n=252)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7503 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.298 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.4975` → IC=+0.294 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4975 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.533` → IC=+0.124 (n=296)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 8.533 (IC base=+0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0613` → IC=+0.229 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0613 (IC base=-0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0902` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0902 (IC base=-0.192)

- **PATRÓN** `ibs_15` < `0.6473` → IC=+0.312 (n=46)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6473 (IC base=-0.192)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.192)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.439 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=-0.192)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=543)

- **PATRÓN** `sigma_h` > `0.0037` → IC=+0.161 (n=376)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0037 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1112` → IC=+0.182 (n=281)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1112 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1405` → IC=+0.149 (n=280)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio_macro` |x|> 0.1405 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.193 (n=311)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.171 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.6409` → IC=+0.249 (n=420)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6409 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.5648` → IC=+0.159 (n=83)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.5648 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2612` → IC=+0.151 (n=394)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2612 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.224 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=543)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `11190.1247` → IC=+0.176 (n=140)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 11190.1247 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.249 (n=433)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.3481` → IC=+0.240 (n=866)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3481 (IC base=+0.238)

- **PATRÓN** `drift_15min` |x|≤ `0.761` → IC=+0.249 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.761 (IC base=+0.238)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2104` → IC=+0.266 (n=446)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2104 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.240 (n=872)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.238)

- **PATRÓN** `ibs_15` < `0.3657` → IC=+0.271 (n=984)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3657 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.7268` → IC=+0.298 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7268 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.337` → IC=+0.259 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.337 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.558` → IC=+0.242 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.558 (IC base=+0.238)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.240 (n=279)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=543)

- **FILTRO** `drift_15min` |x|> `0.8765` → IC=-0.268 (n=205)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8765
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=617)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.215 (n=349)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=473)

- **FILTRO** `sigma_ewma_delta_pct` > `18.332` → IC=-0.145 (n=426)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.332
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3434)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.174 (n=44)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.176)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.226 (n=60)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.176)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.176)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.176)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.176)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0786` → IC=+0.239 (n=393)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0786 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1879` → IC=+0.236 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1879 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.279 (n=441)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.1715` → IC=+0.241 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1715 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1263` → IC=-0.223 (n=496)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1263
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=498)

- **FILTRO** `sigma_h` > `0.0192` → IC=-0.259 (n=496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0192
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=498)

- **FILTRO** `drift_15min` |x|> `1.198` → IC=-0.264 (n=248)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.198
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=746)

- **FILTRO** `sigma_ewma_delta_pct` > `7.295` → IC=-0.203 (n=308)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.295
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=686)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.201)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0664` → IC=+0.273 (n=615)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0664 (IC base=-0.029)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1114` → IC=+0.307 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1114 (IC base=-0.029)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=690)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.029)

- **PATRÓN** `dist_vwap_pct` > `0.786` → IC=+0.355 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.786 (IC base=-0.029)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.030)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.030)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.290 (n=578)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.288 (n=772)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.325 (n=289)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.297 (n=288)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2237` → IC=+0.309 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2237 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=905)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.321 (n=864)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.1565` → IC=+0.317 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1565 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.656` → IC=+0.354 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.656 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `14636.8174` → IC=+0.307 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14636.8174 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.305 (n=157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.324 (n=157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.285)

- **PATRÓN** `drift_15min` |x|≤ `0.4181` → IC=+0.285 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4181 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2522` → IC=+0.310 (n=156)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2522 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3979` → IC=+0.302 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3979 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.313 (n=469)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2573` → IC=+0.333 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2573 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.366 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `16334.7136` → IC=+0.330 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16334.7136 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.297 (n=264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.292)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.299 (n=396)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0518` → IC=+0.321 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0518 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3007` → IC=+0.315 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3007 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.318 (n=383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.329 (n=396)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.4335` → IC=+0.318 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4335 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.656` → IC=+0.329 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.656 (IC base=+0.292)

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

- **PATRÓN** `T_h` < `115.2222` → IC=+0.290 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 115.2222 (IC base=+0.287)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6077 sube el IC de +0.194 a +0.272 en UPDOWN_GBM#15min (n=2450). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7143 sube el IC de +0.214 a +0.276 en UPDOWN_GBM#BTC#15min (n=484). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5749 sube el IC de +0.135 a +0.234 en UPDOWN_GBM#ETH#15min (n=531). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5152 sube el IC de +0.157 a +0.244 en UPDOWN_GBM#SOL#15min (n=358). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5854 sube el IC de +0.212 a +0.292 en UPDOWN_GBM#XRP#15min (n=600). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.156 en UPDOWN_GBM#XRP#15min (n=647). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.067 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=850). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3508 sube el IC de -0.016 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=2750). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7503 sube el IC de +0.086 a +0.327 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=252). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6473 sube el IC de -0.192 a +0.312 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=46). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6409 sube el IC de +0.146 a +0.249 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=420). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3657 sube el IC de +0.238 a +0.271 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=984). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.176 a +0.226 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=60). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.039 a +0.279 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=441). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.201 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.029 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=690). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.289 a +0.321 en UPDOWN_GBM_IBS_ALTO (n=864). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.285 a +0.313 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=469). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.292 a +0.329 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=396). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.357 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=529). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.357 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=287). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.355 a +0.402 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=243). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1555 | +0.095 | +185.05€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1555 | +0.095 | +185.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1187 | +0.101 | +156.63€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1187 | +0.101 | +156.63€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 265 | +0.069 | +12.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 265 | +0.069 | +12.71€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 227 | +0.020 | +52.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 227 | +0.020 | +52.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 186 | +0.016 | +46.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 186 | +0.016 | +46.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 19 | +0.113 | +3.72€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 19 | +0.113 | +3.72€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 34371 | -0.085 | -4563.91€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1735 | -0.015 | -219.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 32636 | -0.088 | -4344.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4356 | -0.121 | -763.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4356 | -0.121 | -763.13€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1735 | -0.015 | -219.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1735 | -0.015 | -219.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4041 | -0.113 | -884.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4041 | -0.113 | -884.57€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8890 | +0.003 | -844.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8890 | +0.003 | -844.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8675 | -0.105 | -613.35€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8675 | -0.105 | -613.35€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6674 | -0.151 | -1238.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6674 | -0.151 | -1238.44€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 26388 | -0.020 | +3757.65€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6826 | +0.002 | +1771.65€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 19562 | -0.027 | +1986.00€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 26388 | -0.020 | +3757.65€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6826 | +0.002 | +1771.65€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 19562 | -0.027 | +1986.00€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 117915 | +0.113 | -5267.23€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 16414 | +0.183 | -488.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 504 | -0.047 | -63.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 93691 | +0.103 | -4446.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7306 | +0.103 | -269.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 15561 | +0.103 | -1087.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 55 | -0.149 | +10.33€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 15491 | +0.104 | -1086.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 23322 | +0.129 | -396.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4877 | +0.197 | -136.28€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 15538 | +0.115 | -170.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2865 | +0.090 | -67.85€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 15606 | +0.094 | -1233.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 62 | -0.109 | -4.45€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 15529 | +0.096 | -1217.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 25050 | +0.124 | -433.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6675 | +0.175 | -100.05€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 15709 | +0.106 | -275.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2654 | +0.101 | -49.94€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 22799 | +0.114 | -1254.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4689 | +0.190 | -268.49€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 407 | -0.011 | -9.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 15916 | +0.093 | -825.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1787 | +0.129 | -152.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 15577 | +0.101 | -861.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 56 | -0.035 | +10.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 15508 | +0.102 | -872.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 18826 | +0.195 | -1170.28€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 18826 | +0.195 | -1170.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4365 | +0.173 | -412.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4365 | +0.173 | -412.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2053 | +0.203 | -30.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2053 | +0.203 | -30.92€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4300 | +0.183 | -338.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4300 | +0.183 | -338.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3788 | +0.242 | -133.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3788 | +0.242 | -133.72€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4241 | +0.190 | -268.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4241 | +0.190 | -268.11€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 879 | +0.426 | -31.76€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 879 | +0.426 | -31.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 346 | +0.434 | -6.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 346 | +0.434 | -6.59€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 334 | +0.429 | -9.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 334 | +0.429 | -9.78€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 187 | +0.405 | -12.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 187 | +0.405 | -12.95€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 65414 | +0.200 | -4865.38€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 65414 | +0.200 | -4865.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 11252 | +0.183 | -1199.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 11252 | +0.183 | -1199.16€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 10527 | +0.224 | -371.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 10527 | +0.224 | -371.05€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 11243 | +0.177 | -1250.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 11243 | +0.177 | -1250.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10587 | +0.220 | -394.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10587 | +0.220 | -394.37€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10840 | +0.202 | -720.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10840 | +0.202 | -720.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10965 | +0.194 | -929.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10965 | +0.194 | -929.77€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 24904 | +0.117 | +190.23€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 24904 | +0.117 | +190.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 12370 | +0.120 | +158.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 12370 | +0.120 | +158.46€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 12534 | +0.114 | +31.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 12534 | +0.114 | +31.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1761 | +0.290 | -18.88€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1761 | +0.290 | -18.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 796 | +0.279 | -17.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 796 | +0.279 | -17.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 847 | +0.289 | -5.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 847 | +0.289 | -5.56€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 118 | +0.350 | +4.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 118 | +0.350 | +4.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 795 | +0.440 | +1.53€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 795 | +0.440 | +1.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 383 | +0.438 | -1.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 383 | +0.438 | -1.75€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 366 | +0.443 | +2.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 366 | +0.443 | +2.72€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1358 | +0.072 | -57.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 496 | +0.062 | -36.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 862 | +0.077 | -21.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1061 | +0.078 | -27.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 199 | +0.077 | -6.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 862 | +0.077 | -21.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 231 | +0.036 | -31.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 231 | +0.036 | -31.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 47859 | +0.100 | -1234.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3886 | +0.091 | +47.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 43973 | +0.100 | -1281.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 26540 | +0.104 | -305.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3886 | +0.091 | +47.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 22654 | +0.106 | -352.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 9491 | +0.110 | -12.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 9491 | +0.110 | -12.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 11828 | +0.081 | -916.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 11828 | +0.081 | -916.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 869 | +0.205 | -100.14€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 869 | +0.205 | -100.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 869 | +0.205 | -100.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 869 | +0.205 | -100.14€ | 2 | 4 |
| ✅ GBM_LATE_15M | 33449 | +0.088 | +16609.16€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 33449 | +0.088 | +16609.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5627 | +0.203 | +4335.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5627 | +0.203 | +4335.26€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 4958 | +0.177 | +3568.23€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4958 | +0.177 | +3568.23€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 5939 | +0.201 | +4515.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5939 | +0.201 | +4515.30€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 4735 | +0.033 | +1178.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4735 | +0.033 | +1178.71€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4768 | -0.031 | +1037.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4768 | -0.031 | +1037.99€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 7422 | -0.036 | +1973.68€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7422 | -0.036 | +1973.68€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 36203 | +0.087 | +19278.91€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 36203 | +0.087 | +19278.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7008 | +0.012 | +3618.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7008 | +0.012 | +3618.92€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7498 | +0.013 | +1604.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7498 | +0.013 | +1604.51€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5106 | +0.268 | +5268.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5106 | +0.268 | +5268.55€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 6133 | +0.011 | +1360.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 6133 | +0.011 | +1360.42€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5901 | +0.036 | +2354.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5901 | +0.036 | +2354.52€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4557 | +0.288 | +5071.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4557 | +0.288 | +5071.99€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 26714 | +0.175 | +20863.86€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 26714 | +0.175 | +20863.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4038 | +0.216 | +3371.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4038 | +0.216 | +3371.30€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4212 | +0.150 | +3066.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4212 | +0.150 | +3066.32€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4237 | +0.217 | +3524.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4237 | +0.217 | +3524.01€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4486 | +0.138 | +3322.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4486 | +0.138 | +3322.27€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5005 | +0.125 | +3669.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5005 | +0.125 | +3669.40€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4736 | +0.213 | +3910.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4736 | +0.213 | +3910.55€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7284 | +0.139 | +3500.91€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7284 | +0.139 | +3500.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 341 | +0.141 | +188.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 341 | +0.141 | +188.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2191 | +0.147 | +1217.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2191 | +0.147 | +1217.16€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2233 | +0.154 | +1100.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2233 | +0.154 | +1100.64€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1607 | +0.108 | +579.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1607 | +0.108 | +579.43€ | 1 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 537 | +0.135 | +240.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 537 | +0.135 | +240.44€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 33673 | +0.181 | +26056.17€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 33673 | +0.181 | +26056.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5360 | +0.230 | +4749.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5360 | +0.230 | +4749.39€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5196 | +0.148 | +3411.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5196 | +0.148 | +3411.92€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5635 | +0.228 | +4925.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5635 | +0.228 | +4925.95€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5476 | +0.136 | +3813.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5476 | +0.136 | +3813.32€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5949 | +0.125 | +4122.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5949 | +0.125 | +4122.48€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6057 | +0.216 | +5033.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6057 | +0.216 | +5033.11€ | 0 | 22 |
| ✅ GBM_LATE_5M | 9229 | +0.179 | +6318.40€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 9229 | +0.179 | +6318.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2113 | +0.169 | +1523.04€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2113 | +0.169 | +1523.04€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 992 | +0.176 | +650.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 992 | +0.176 | +650.38€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 2856 | +0.181 | +1879.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2856 | +0.181 | +1879.64€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 1196 | +0.178 | +817.14€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1196 | +0.178 | +817.14€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 1237 | +0.162 | +718.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1237 | +0.162 | +718.80€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2498 | +0.072 | +909.30€ | 0 | 10 |
| ✅ GBM_LATE_60M#60min | 2498 | +0.072 | +909.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 942 | +0.089 | +346.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 942 | +0.089 | +346.03€ | 0 | 12 |
| ✅ GBM_LATE_60M#ETH | 778 | +0.072 | +347.16€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 778 | +0.072 | +347.16€ | 1 | 11 |
| ✅ GBM_LATE_60M#SOL | 778 | +0.051 | +216.11€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 778 | +0.051 | +216.11€ | 2 | 12 |
| 🚫 GBM_LATE_60M_FADE | 479 | -0.238 | -14.03€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 479 | -0.238 | -14.03€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 178 | -0.222 | -8.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 178 | -0.222 | -8.07€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 168 | -0.224 | -0.29€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 168 | -0.224 | -0.29€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 133 | -0.270 | -5.66€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 133 | -0.270 | -5.66€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1089 | +0.083 | +258.39€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1089 | +0.083 | +258.39€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 410 | +0.075 | +79.69€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 410 | +0.075 | +79.69€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 369 | +0.055 | +47.74€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 369 | +0.055 | +47.74€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 310 | +0.125 | +130.95€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 310 | +0.125 | +130.95€ | 2 | 13 |
| ✅ LATE_WINDOW_5MIN | 128 | +0.246 | +105.36€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 128 | +0.246 | +105.36€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 128 | +0.246 | +105.36€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 128 | +0.246 | +105.36€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 2792 | +0.103 | +732.68€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2792 | +0.103 | +732.68€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2792 | +0.103 | +732.68€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2792 | +0.103 | +732.68€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 426 | -0.068 | -31.31€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 426 | -0.068 | -31.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 116 | -0.034 | -1.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 116 | -0.034 | -1.97€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 161 | -0.021 | -4.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 161 | -0.021 | -4.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 2904 | +0.023 | +78.07€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2904 | +0.023 | +78.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 141 | +0.038 | +0.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 141 | +0.038 | +0.40€ | 1 | 2 |
| ✅ LIQUIDACIONES_5M#BTC | 456 | +0.026 | +31.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 456 | +0.026 | +31.75€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 202 | -0.020 | -5.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 202 | -0.020 | -5.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1076 | +0.031 | +30.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1076 | +0.031 | +30.96€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 658 | +0.017 | +3.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 658 | +0.017 | +3.83€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 371 | +0.023 | +16.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 371 | +0.023 | +16.73€ | 1 | 1 |
| ✅ LIQUIDACIONES_60M | 1416 | -0.043 | -27.47€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1416 | -0.043 | -27.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 404 | -0.039 | -12.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 404 | -0.039 | -12.94€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 465 | -0.020 | +1.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 465 | -0.020 | +1.95€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 547 | -0.065 | -16.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 547 | -0.065 | -16.48€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 4749 | -0.010 | +175.23€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2249 | -0.017 | +49.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2500 | -0.004 | +125.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 134 | -0.007 | +3.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 66 | +0.044 | +10.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 68 | -0.057 | -6.91€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1180 | -0.003 | +46.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 558 | -0.013 | +7.82€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 622 | +0.006 | +38.81€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 539 | -0.012 | +21.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 269 | -0.024 | +3.02€ | 4 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 270 | +0.000 | +18.70€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 975 | -0.030 | -14.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 445 | -0.046 | -24.37€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 530 | -0.017 | +9.87€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 928 | -0.007 | +48.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 454 | -0.009 | +26.36€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 474 | -0.006 | +22.23€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 993 | -0.002 | +68.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 457 | -0.005 | +25.93€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 536 | +0.002 | +43.03€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 38745 | -0.003 | +1862.81€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 38745 | -0.003 | +1862.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6909 | +0.024 | +925.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6909 | +0.024 | +925.60€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5767 | -0.033 | -95.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5767 | -0.033 | -95.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 7008 | +0.020 | +689.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 7008 | +0.020 | +689.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5571 | -0.051 | -147.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5571 | -0.051 | -147.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6534 | -0.008 | +211.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6534 | -0.008 | +211.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6956 | +0.012 | +279.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6956 | +0.012 | +279.57€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6191 | -0.059 | -144.32€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6191 | -0.059 | -144.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1219 | +0.001 | -13.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1219 | +0.001 | -13.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1522 | -0.077 | -32.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1522 | -0.077 | -32.57€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 46 | -0.104 | -4.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 46 | -0.104 | -4.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 717 | -0.124 | -33.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 717 | -0.124 | -33.88€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1831 | -0.077 | -34.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1831 | -0.077 | -34.86€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 97247 | -0.073 | +1666.72€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 97247 | -0.073 | +1666.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 16731 | -0.074 | +914.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 16731 | -0.074 | +914.44€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 14762 | -0.098 | -783.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 14762 | -0.098 | -783.97€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 16986 | -0.066 | +939.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 16986 | -0.066 | +939.32€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 14295 | -0.095 | -423.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 14295 | -0.095 | -423.63€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 17606 | -0.052 | +324.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 17606 | -0.052 | +324.53€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 16867 | -0.064 | +696.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 16867 | -0.064 | +696.02€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8074 | -0.031 | -153.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8074 | -0.031 | -153.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1921 | -0.042 | -17.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1921 | -0.042 | -17.94€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2244 | -0.025 | -31.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2244 | -0.025 | -31.45€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1119 | -0.050 | -23.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1119 | -0.050 | -23.95€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 786 | -0.025 | -27.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 786 | -0.025 | -27.78€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1382 | +0.117 | +519.00€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1246 | +0.123 | +506.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 291 | +0.145 | +154.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 291 | +0.145 | +154.91€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 238 | +0.104 | +64.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 238 | +0.104 | +64.19€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 253 | +0.116 | +100.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 253 | +0.116 | +100.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 223 | +0.149 | +119.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 223 | +0.149 | +119.32€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 241 | +0.097 | +67.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 241 | +0.097 | +67.12€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 952 | -0.014 | -13.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 952 | -0.014 | -13.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 186 | +0.011 | +10.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 186 | +0.011 | +10.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 141 | -0.004 | +1.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 141 | -0.004 | +1.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 253 | -0.037 | -17.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 253 | -0.037 | -17.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 210 | +0.005 | +0.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 210 | +0.005 | +0.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 162 | -0.037 | -9.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 162 | -0.037 | -9.45€ | 0 | 0 |
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
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 205 | -0.186 | +7.90€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 789 | -0.207 | -65.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 118 | -0.175 | +9.51€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 378 | +0.397 | +331.12€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 45 | +0.096 | +25.91€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 45 | +0.096 | +25.91€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 97 | +0.369 | +76.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 97 | +0.369 | +76.24€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 236 | +0.462 | +228.97€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 236 | +0.462 | +228.97€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 378 | +0.397 | +331.12€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 624 | +0.032 | +25.20€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 624 | +0.032 | +25.20€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 46 | +0.042 | -0.04€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 46 | +0.042 | -0.04€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 65 | -0.007 | -1.72€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 65 | -0.007 | -1.72€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 218 | +0.054 | +24.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 218 | +0.054 | +24.65€ | 2 | 4 |
| ✅ STREAK_FADE_5M | 3103 | -0.021 | -119.58€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3103 | -0.021 | -119.58€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 911 | -0.020 | -31.14€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 911 | -0.020 | -31.14€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 580 | -0.026 | -25.19€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 580 | -0.026 | -25.19€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1456 | -0.016 | -48.84€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1456 | -0.016 | -48.84€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 90 | -0.054 | -9.27€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 90 | -0.054 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 52 | -0.018 | -4.83€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 52 | -0.018 | -4.83€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 9759 | +0.019 | +102.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9759 | +0.019 | +102.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2636 | +0.021 | +28.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2636 | +0.021 | +28.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2326 | +0.027 | +48.48€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2326 | +0.027 | +48.48€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2861 | +0.010 | -0.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2861 | +0.010 | -0.81€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1936 | +0.019 | +26.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1936 | +0.019 | +26.23€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8839 | +0.013 | -47.94€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8839 | +0.013 | -47.94€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3487 | +0.017 | -8.64€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3487 | +0.017 | -8.64€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3497 | +0.012 | -24.51€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3497 | +0.012 | -24.51€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1855 | +0.007 | -14.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1855 | +0.007 | -14.78€ | 1 | 0 |
| ✅ UPDOWN_GBM | 58757 | +0.046 | +4552.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 14591 | +0.080 | +3077.44€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1941 | +0.005 | +6.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 38661 | +0.039 | +1420.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3361 | +0.006 | +48.80€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6058 | +0.081 | +821.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1231 | +0.152 | +519.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 50 | -0.019 | -1.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4777 | +0.064 | +302.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 11352 | +0.050 | +907.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1853 | +0.090 | +425.31€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 510 | +0.012 | +5.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 7390 | +0.054 | +432.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1524 | +0.005 | +41.91€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 75 | -0.084 | +2.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 7083 | +0.057 | +610.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1203 | +0.138 | +439.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 48 | +0.000 | -2.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 5832 | +0.040 | +172.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 12836 | +0.036 | +697.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3491 | +0.055 | +443.60€ | 0 | 12 |
| ✅ UPDOWN_GBM#ETH#240min | 503 | +0.007 | +8.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 7634 | +0.035 | +241.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1141 | +0.004 | +0.03€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 67 | -0.109 | +3.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 13014 | +0.025 | +495.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3442 | +0.034 | +300.19€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 493 | -0.001 | -0.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 8324 | +0.025 | +194.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 696 | +0.010 | +6.85€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 59 | -0.156 | -5.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 8412 | +0.054 | +1021.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3371 | +0.101 | +948.78€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 337 | +0.004 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4704 | +0.024 | +75.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 201 | -0.116 | +0.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 705 | +0.357 | +239.94€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 705 | +0.357 | +239.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 382 | +0.357 | +123.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 382 | +0.357 | +123.90€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 323 | +0.355 | +116.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 323 | +0.355 | +116.05€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 16152 | -0.027 | +3774.40€ | 2 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 16152 | -0.027 | +3774.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1328 | -0.050 | +446.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1328 | -0.050 | +446.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2814 | -0.113 | +120.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2814 | -0.113 | +120.50€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 742 | +0.208 | +581.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 742 | +0.208 | +581.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1871 | +0.211 | +1165.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1871 | +0.211 | +1165.08€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4682 | -0.063 | +623.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4682 | -0.063 | +623.62€ | 4 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4715 | -0.065 | +836.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4715 | -0.065 | +836.91€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 178 | +0.028 | +6.60€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 178 | +0.028 | +6.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 178 | +0.028 | +6.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 178 | +0.028 | +6.60€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1152 | +0.289 | +935.60€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1152 | +0.289 | +935.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 625 | +0.285 | +477.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 625 | +0.285 | +477.13€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 527 | +0.292 | +458.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 527 | +0.292 | +458.47€ | 0 | 8 |
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
| ✅ WEEKLY_PRICE#BTC | 1055 | +0.261 | +156.12€ | 0 | 5 |
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
  - _Estado_: 627 celda(s) pasan gate riguroso completo de 2477 evaluadas (n>=40) y 3454 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.034 < 0.08 — monitorear
  - _Datos_: n=3436 IC=+0.034 PNL=+302.36€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.132 n=571/60 | contraria IC=+0.188 n=585 | gap=-0.056 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=381, boost estimado=+0.008. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1140/40 IC=+0.004 PNL=-0.50€ | BTC#60min: n=1522/40 IC=+0.005 PNL=+41.84€ | SOL#60min: n=695/40 IC=+0.011 PNL=+7.36€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=442908 | tras_1loss IC=+0.089 n=339619 | tras_2loss IC=+0.058 n=139430/40 | gap=-0.010 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.204 > 0.08 con n=485 PNL=+365.85€
  - _Datos_: n=485 IC=+0.204 PNL=+365.85€

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
  - _Estado_: n=66 IC=+0.176 PNL=+41.61€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=66 IC=+0.176 PNL=+41.61€

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
  - _Estado_: n=2266 IC=+0.010 PNL=+11.12€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2266 IC=+0.010 PNL=+11.12€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1091 IC=-0.003 PNL=+37.58€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1091 IC=-0.003 PNL=+37.58€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.196 > 0.1 con n=3259 PNL=+2230.16€
  - _Datos_: n=3259 IC=+0.196 PNL=+2230.16€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1849 IC=+0.090 PNL=+426.44€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1849 IC=+0.090 PNL=+426.44€

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
  - _Estado_: n=752 IC=+0.025 PNL=+58.26€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=752 IC=+0.025 PNL=+58.26€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=80 IC=+0.037 PNL=+3.22€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=80 IC=+0.037 PNL=+3.22€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.246 n=128) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=128 IC=+0.246 PNL=+105.36€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.02 con n=792 PNL=+314.39€
  - _Datos_: n=792 IC=+0.122 PNL=+314.39€

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
  - _Estado_: n=21999 IC=+0.070 PNL=+3057.46€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=21999 IC=+0.070 PNL=+3057.46€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.141 < -0.1 con n=346 PNL=+36.70€
  - _Datos_: n=346 IC=-0.141 PNL=+36.70€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2570 IC=+0.066 PNL=+308.16€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2570 IC=+0.066 PNL=+308.16€

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
  - _Estado_: n=24242 IC=-0.136 PNL=+1787.66€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=24242 IC=-0.136 PNL=+1787.66€

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
  - _Estado_: n=2476 IC=+0.136 PNL=+1432.89€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2476 IC=+0.136 PNL=+1432.89€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=6026 IC=+0.042 PNL=+385.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6026 IC=+0.042 PNL=+385.51€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.088 > 0.08 con n=2723 PNL=+1438.09€
  - _Datos_: n=2723 IC=+0.088 PNL=+1438.09€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.227 < -0.1 con n=2477 PNL=-205.22€
  - _Datos_: n=2477 IC=-0.227 PNL=-205.22€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1421) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1421 IC=+0.102 PNL=+325.31€

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
  - _Estado_: n=11243 IC=+0.183 PNL=-1199.58€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=11243 IC=+0.183 PNL=-1199.58€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.211 > 0.1 con n=178 PNL=+111.12€
  - _Datos_: n=178 IC=+0.211 PNL=+111.12€
