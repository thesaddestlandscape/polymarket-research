# Hipótesis automáticas — 2026-10-09 00:53 UTC
_Generado por shadow_postmortem.py sobre 814763 resoluciones (PNL=+101394.81€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.232 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.119)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.198 (n=233)

  - _Acción_: Kelly boost +0.99€ cuando `n_total_lado` > 69.0 (IC base=+0.119)

- **PATRÓN** `banda_hit_calibrado` > `0.6165` → IC=+0.234 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6165 (IC base=+0.119)

- **PATRÓN** `banda_z` > `8.976` → IC=+0.191 (n=228)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.976 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=727)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.119)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.227 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.208 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.8118` → IC=+0.260 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8118 (IC base=+0.123)

- **PATRÓN** `banda_z` > `9.563` → IC=+0.179 (n=185)

  - _Acción_: Kelly boost +0.90€ cuando `banda_z` > 9.563 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=629)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.123)

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
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=97)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=97)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=110)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.000)

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
- **FILTRO** `restante_s_al_confirmar` < `144.01` → IC=-0.208 (n=8864)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=26597)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.93` → IC=-0.267 (n=1103)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.93
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3311)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `123.47` → IC=-0.304 (n=1024)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 123.47
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3072)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `164.76` → IC=-0.229 (n=2264)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 164.76
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=6797)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.06` → IC=-0.301 (n=1730)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.06
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=5192)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.207 (n=18432)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=3975)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `9526.1642` → IC=+0.182 (n=1770)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9526.1642 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.134 (n=15317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=18485)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=14109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=6537)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7492.2756` → IC=+0.167 (n=2514)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 7492.2756 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=1919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=1871)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2355)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `16107.9712` → IC=+0.209 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16107.9712 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.198 (n=1694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=1877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=2409)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `16052.1822` → IC=+0.206 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16052.1822 (IC base=+0.193)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.160 (n=410)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.61 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `4988.4492` → IC=+0.126 (n=228)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 4988.4492 (IC base=+0.087)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.090)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.138 (n=985)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.090)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.364 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.228 (n=1603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.361 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=894)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=762)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.250 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `1328.2803` → IC=+0.141 (n=853)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1328.2803 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.410 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=1248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.289 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=822)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.179 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.376 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.225 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=15265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=12906)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.229 (n=6424)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=3382)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.176 (n=3560)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 18.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=3446)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.174)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=1572)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.233 (n=1637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.315 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.226)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=3329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=3345)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.190 (n=1945)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.72 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=3077)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.331 (n=1070)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=3439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=2193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.190 (n=2617)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.71 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.429 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.426 (n=605)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.427 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `2776.9049` → IC=+0.432 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2776.9049 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.430 (n=270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.444 (n=178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `17845.9528` → IC=+0.434 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 17845.9528 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.435 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.435 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `3408.2761` → IC=+0.437 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3408.2761 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.405)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.408 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.405)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.408 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.405)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.410 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.405)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `6345.2155` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 6345.2155
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.209 (n=16951)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=19924)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.192 (n=2932)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=6260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.199 (n=8686)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.184)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=4107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.282 (n=2878)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=7807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.177 (n=6249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=8308)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=4142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=2825)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=7574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.203 (n=6003)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=2957)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=3283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=3449)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=7001)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.125 (n=6499)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.2 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.137 (n=6829)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=8558)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.45` → IC=+0.137 (n=6475)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.45 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=3480)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.126 (n=3220)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=3435)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.136 (n=3725)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `3.05` → IC=+0.146 (n=3214)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.05 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=3521)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.131 (n=3734)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.134 (n=3266)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.313 (n=967)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.289 (n=1418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1555.5576` → IC=+0.292 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1555.5576 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.291 (n=645)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.340 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `5330.8584` → IC=+0.306 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5330.8584 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.290 (n=680)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.386 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1448.5782` → IC=+0.302 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1448.5782 (IC base=+0.286)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.445 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.449 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.462 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.450 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.444 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `2138.537` → IC=+0.459 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2138.537 (IC base=+0.442)

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
- **PATRÓN** `drift_60min` |x|≤ `0.3722` → IC=+0.135 (n=9607)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.3722 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9835` → IC=+0.243 (n=3639)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9835 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2216` → IC=+0.254 (n=2529)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2216 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.439` → IC=+0.193 (n=2840)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.439 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.8523` → IC=+0.249 (n=2047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8523 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6158` → IC=+0.254 (n=3069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6158 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.3009` → IC=+0.231 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3009 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.3218` → IC=+0.218 (n=3474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3218 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.564` → IC=+0.141 (n=13356)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.564 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.5874` → IC=+0.203 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5874 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` < `1.193` → IC=+0.183 (n=4959)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.193 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` > `0.6242` → IC=+0.181 (n=4959)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6242 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2949` → IC=+0.229 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2949 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` > `1.4477` → IC=+0.203 (n=8500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4477 (IC base=+0.072)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.217 (n=8312)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.072)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.219 (n=810)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.191 (n=811)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.008 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3515` → IC=+0.188 (n=2423)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3515 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=1183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.279 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.783` → IC=+0.294 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.783 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.237 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.183 (n=2296)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2512)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2083.8` → IC=+0.194 (n=808)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2083.8 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.233 (n=1317)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.241 (n=1765)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.0884` → IC=+0.266 (n=657)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0884 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=729)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0605` → IC=+0.279 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0605 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.544` → IC=+0.246 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.544 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.405` → IC=+0.236 (n=2063)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.405 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` < `0.0951` → IC=+0.234 (n=1739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0951 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.259 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.6222` → IC=+0.253 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6222 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=2166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.232 (n=857)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1796` → IC=+0.242 (n=1295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1796 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=1951)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.3188` → IC=+0.233 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3188 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1985` → IC=+0.221 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1985 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.572` → IC=+0.258 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.572 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `1.2468` → IC=+0.220 (n=1942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2468 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.6188` → IC=+0.222 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6188 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.245 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7583` → IC=+0.219 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7583 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.4058` → IC=+0.237 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4058 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.152 (n=1939)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0056 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.167 (n=647)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7224` → IC=+0.178 (n=1937)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7224 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.157 (n=1789)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1327 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.236` → IC=+0.156 (n=309)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.236 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.301` → IC=+0.143 (n=1776)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.301 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1873` → IC=+0.148 (n=1937)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1873 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.6228` → IC=+0.139 (n=1937)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6228 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0967` → IC=+0.167 (n=703)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0967 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4485` → IC=+0.149 (n=1822)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4485 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7828` → IC=+0.145 (n=1216)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7828 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.176 (n=767)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 229.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.201 (n=2455)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.197 (n=2458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=2193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.414` → IC=+0.258 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.414 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.194 (n=2160)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.194 (n=322)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.1498` → IC=+0.201 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1498 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=2931)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.226 (n=1455)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.1338` → IC=+0.229 (n=728)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1338 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=1009)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.0652` → IC=+0.238 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0652 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.686` → IC=+0.255 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.686 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.259 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.7127` → IC=+0.219 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7127 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.7169` → IC=+0.228 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7169 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.217 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.214)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.144 (n=133)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=2933)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.147 (n=460)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0036 (IC base=+0.044)

- **PATRÓN** `ibs_20min` > `0.9584` → IC=+0.220 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9584 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` < `0.188` → IC=+0.323 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.188 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.987` → IC=+0.177 (n=964)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 4.987 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` < `0.8536` → IC=+0.326 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8536 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.340 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.339 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.353 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` > `2.1967` → IC=+0.317 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1967 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.321 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.0976` → IC=+0.166 (n=768)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.0976 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `0.31` → IC=+0.195 (n=332)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.31 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.8497` → IC=+0.153 (n=825)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8497 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.213 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.5239` → IC=+0.166 (n=1054)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5239 (IC base=+0.032)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.179 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=457)

- **FILTRO** `ibs_20min` < `0.3056` → IC=-0.191 (n=134)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3056
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=402)

- **FILTRO** `ibs_20min` > `0.2258` → IC=-0.126 (n=2971)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2258
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=1467)

- **FILTRO** `sigma_ewma_delta_pct` > `8.773` → IC=-0.221 (n=456)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.773
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=3982)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.199 (n=184)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.8 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `1.7756` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.7756 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.383` → IC=+0.133 (n=186)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 2.383 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.57` → IC=+0.267 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.57 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `1.0233` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0233 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.0752` → IC=+0.285 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0752 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.5152` → IC=+0.280 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5152 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.272 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.2258` → IC=+0.141 (n=1467)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.2258 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.1869` → IC=+0.274 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1869 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.7007` → IC=+0.282 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7007 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.297 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.3699` → IC=+0.294 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3699 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6434` → IC=-0.186 (n=772)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6434
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2321)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.210 (n=870)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2223)

- **FILTRO** `ibs_20min` > `0.7628` → IC=-0.207 (n=1153)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7628
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=3460)

- **PATRÓN** `dist_vwap_pct` > `0.4652` → IC=+0.317 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4652 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2049` → IC=+0.316 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2049 (IC base=-0.073)

- **PATRÓN** `volumen_regimen` < `0.988` → IC=+0.297 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.988 (IC base=-0.073)

- **PATRÓN** `volumen_regimen` > `0.6389` → IC=+0.315 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6389 (IC base=-0.073)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.303 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=-0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.301 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.4802` → IC=+0.300 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4802 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` > `2.1732` → IC=+0.305 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1732 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` > `0.8365` → IC=+0.288 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8365 (IC base=-0.011)

- **PATRÓN** `volumen_regimen` > `1.0723` → IC=+0.276 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0723 (IC base=-0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.275 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` < `2.1667` → IC=+0.256 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1667 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` > `1.4248` → IC=+0.258 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4248 (IC base=-0.011)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.200 (n=4798)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4656` → IC=+0.186 (n=12854)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4656 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.6792` → IC=+0.285 (n=1427)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6792 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.69` → IC=+0.153 (n=6477)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.69 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.173` → IC=+0.249 (n=5264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.173 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6894` → IC=+0.256 (n=4703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6894 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` < `0.0795` → IC=+0.245 (n=7790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0795 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.260 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4633` → IC=+0.247 (n=2829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4633 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6278` → IC=+0.256 (n=2829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6278 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.279 (n=8042)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.166 (n=4644)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0089 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.5406` → IC=+0.160 (n=12242)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.5406 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.8744` → IC=+0.252 (n=2830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8744 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.1973` → IC=+0.260 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1973 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.2951` → IC=+0.308 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2951 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `1.5864` → IC=+0.281 (n=2620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5864 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `2.2739` → IC=+0.271 (n=2697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2739 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.284 (n=5848)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.076)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2578` → IC=-0.170 (n=1004)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2578
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=3015)

- **FILTRO** `ibs_20min` > `0.7546` → IC=-0.179 (n=829)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7546
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=2488)

- **FILTRO** `sigma_ewma_delta_pct` > `4.623` → IC=-0.180 (n=729)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.623
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2588)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.277 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.333` → IC=+0.201 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.333 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2273` → IC=+0.280 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2273 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.4426` → IC=+0.218 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4426 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `2.2071` → IC=+0.239 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2071 (IC base=+0.038)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.237 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.038)

- **PATRÓN** `ibs_20min` < `0.1591` → IC=+0.150 (n=830)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.1591 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.0743` → IC=+0.418 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0743 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.6255` → IC=+0.411 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6255 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.5396` → IC=+0.412 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5396 (IC base=-0.024)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.404 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=-0.024)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8619` → IC=+0.149 (n=970)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.8619 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1204` → IC=+0.194 (n=710)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1204 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.6787` → IC=+0.180 (n=1228)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6787 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.217 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4212` → IC=+0.202 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4212 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.4118` → IC=+0.189 (n=451)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4118 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `226.0` → IC=+0.231 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 226.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.1608` → IC=+0.230 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1608 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.234 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0734` → IC=+0.225 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0734 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2731` → IC=+0.296 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2731 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5482` → IC=+0.235 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5482 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1745` → IC=+0.240 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1745 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.272 (n=2159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.259 (n=2173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.255 (n=1924)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.792` → IC=+0.283 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.792 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.266 (n=1966)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `3.1961` → IC=+0.265 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1961 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2554)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.254)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.303 (n=1824)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.184` → IC=+0.307 (n=803)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.184 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.322 (n=610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.3644` → IC=+0.292 (n=1824)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3644 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.672` → IC=+0.302 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.672 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.1935` → IC=+0.284 (n=1779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1935 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.3385` → IC=+0.297 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3385 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.7089` → IC=+0.303 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7089 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.624` → IC=+0.292 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.624 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.287 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.287)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7614` → IC=-0.179 (n=834)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7614
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=2503)

- **PATRÓN** `ibs_20min` > `0.8986` → IC=+0.165 (n=770)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8986 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.0092` → IC=+0.234 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0092 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1681` → IC=+0.227 (n=1084)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1681 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.228 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4092` → IC=+0.255 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4092 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.285 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1267` → IC=+0.220 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1267 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` < `1.1978` → IC=+0.226 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1978 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.291 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.8558` → IC=+0.265 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8558 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.252 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7645` → IC=-0.189 (n=1531)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7645
  - _Potencial_: sin este filtro IC_bueno=+0.288 (n=1531)

- **FILTRO** `ibs_20min` > `0.6667` → IC=-0.246 (n=750)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=2338)

- **FILTRO** `sigma_ewma_delta_pct` > `8.654` → IC=-0.232 (n=353)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.654
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=2735)

- **PATRÓN** `ibs_20min` > `0.7645` → IC=+0.288 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7645 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `1.0387` → IC=+0.332 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0387 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.707` → IC=+0.169 (n=481)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.707 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8524` → IC=+0.315 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8524 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `0.6339` → IC=+0.307 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6339 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.304 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.334 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.326 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.333 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.561` → IC=+0.135 (n=2039)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.561 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.2732` → IC=+0.239 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2732 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.261 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.233 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.256 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4188` → IC=+0.253 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4188 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.266 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.025)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.336 (n=1524)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.309 (n=801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.325 (n=1707)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2129` → IC=+0.320 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2129 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.778` → IC=+0.314 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.778 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.017` → IC=+0.293 (n=1930)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.017 (IC base=+0.292)

- **PATRÓN** `volumen_regimen` > `0.8551` → IC=+0.316 (n=1136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8551 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.339 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.304 (n=1629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `2988.5082` → IC=+0.312 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2988.5082 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.330 (n=1429)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.292)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.322 (n=1211)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.1875` → IC=+0.291 (n=799)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1875 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.300 (n=911)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.3675` → IC=+0.317 (n=1813)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3675 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.3121` → IC=+0.293 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3121 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.494` → IC=+0.301 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.494 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.038` → IC=+0.291 (n=2164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.038 (IC base=+0.291)

- **PATRÓN** `volumen_regimen` < `0.8901` → IC=+0.291 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8901 (IC base=+0.291)

- **PATRÓN** `volumen_regimen` > `1.2273` → IC=+0.322 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2273 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` > `0.2325` → IC=+0.339 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2325 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `2.4599` → IC=+0.291 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4599 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` > `2.1367` → IC=+0.291 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1367 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `2864.917` → IC=+0.291 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2864.917 (IC base=+0.291)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.186 (n=3544)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0047 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.213 (n=3538)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3532` → IC=+0.186 (n=9338)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3532 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=11113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.565` → IC=+0.229 (n=10611)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.565 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.1718` → IC=+0.200 (n=4434)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1718 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.483` → IC=+0.250 (n=2135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.483 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.2004` → IC=+0.168 (n=7058)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2004 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` > `0.6274` → IC=+0.161 (n=7056)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6274 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.194 (n=1567)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.562` → IC=+0.175 (n=4508)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.562 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.5959` → IC=+0.183 (n=3415)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.5959 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `2509.581` → IC=+0.178 (n=7074)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2509.581 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.191 (n=9544)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 104.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.190 (n=6825)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0066 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0816` → IC=+0.223 (n=3410)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0816 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=3860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.4865` → IC=+0.233 (n=10228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4865 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.275` → IC=+0.201 (n=1693)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.275 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.181` → IC=+0.167 (n=7321)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.181 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.224 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6119` → IC=+0.181 (n=3171)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.6119 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.188 (n=9191)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 106.0 (IC base=+0.178)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.235 (n=597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.209 (n=593)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.3412` → IC=+0.221 (n=1779)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3412 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.206 (n=1781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.201 (n=1293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9178` → IC=+0.287 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9178 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.337` → IC=+0.330 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.337 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.258 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.2201` → IC=+0.205 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2201 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=1856)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2016.0` → IC=+0.207 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2016.0 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.248 (n=1217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.246 (n=1382)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.102` → IC=+0.298 (n=607)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.102 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=1238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=688)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.3515` → IC=+0.258 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3515 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.224` → IC=+0.246 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.224 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.240 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.275 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4252` → IC=+0.249 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4252 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.6397` → IC=+0.244 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6397 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=1520)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.221 (n=535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.1657` → IC=+0.186 (n=1069)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1657 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.177 (n=1610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.3757` → IC=+0.224 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3757 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.2021` → IC=+0.211 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2021 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.230 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.6889` → IC=+0.169 (n=705)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6889 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.197 (n=255)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.5109` → IC=+0.177 (n=688)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.5109 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.4711` → IC=+0.156 (n=521)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.4711 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.170 (n=674)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 233.0 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.165 (n=1698)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2337` → IC=+0.177 (n=1492)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2337 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.5967` → IC=+0.201 (n=1696)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5967 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.75` → IC=+0.206 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.75 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.166 (n=1696)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.204 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.2284` → IC=+0.147 (n=1751)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.2284 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1593` → IC=+0.149 (n=516)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1593 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4911` → IC=+0.154 (n=1579)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4911 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7682` → IC=+0.146 (n=1052)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7682 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.174 (n=508)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 208.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.233 (n=594)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.4087` → IC=+0.218 (n=1563)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4087 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1862)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.566` → IC=+0.280 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.566 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.0963` → IC=+0.208 (n=1506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0963 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.1269` → IC=+0.210 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1269 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.7647` → IC=+0.209 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7647 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.6772` → IC=+0.213 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6772 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=2115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.246 (n=1345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1458` → IC=+0.266 (n=673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1458 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.277 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.3506` → IC=+0.252 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3506 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.651` → IC=+0.261 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.651 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.266 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.7153` → IC=+0.246 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7153 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.7161` → IC=+0.236 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7161 (IC base=+0.229)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.233 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.229)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.179 (n=1501)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0064 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0783` → IC=+0.197 (n=569)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0783 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=1783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.3279` → IC=+0.205 (n=1706)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3279 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1399` → IC=+0.188 (n=1071)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1399 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.201 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.161 (n=1138)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8554 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1013` → IC=+0.168 (n=712)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1013 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4307` → IC=+0.163 (n=559)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4307 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.5072` → IC=+0.153 (n=557)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.5072 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `5139.067` → IC=+0.196 (n=1137)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 5139.067 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.152 (n=1643)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 149.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.161 (n=1802)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0071 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.3868` → IC=+0.151 (n=1802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3868 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.6697` → IC=+0.187 (n=1802)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6697 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.845` → IC=+0.165 (n=621)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.845 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8571` → IC=+0.164 (n=1202)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8571 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.195 (n=273)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.8112` → IC=+0.140 (n=1115)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8112 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.133 (n=1672)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.42 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4565.8096` → IC=+0.167 (n=1201)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4565.8096 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.129 (n=1624)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 149.0 (IC base=+0.131)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.163 (n=881)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0098 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.1485` → IC=+0.133 (n=854)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1485 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=1991)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.216 (n=1945)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `1.0629` → IC=+0.215 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0629 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.945` → IC=+0.261 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.945 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.196` → IC=+0.144 (n=1942)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.196 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.1634` → IC=+0.139 (n=1960)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.1634 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.5481` → IC=+0.145 (n=826)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5481 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.4817` → IC=+0.132 (n=626)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4817 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2036)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2389.1426` → IC=+0.190 (n=1294)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2389.1426 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.150 (n=1535)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 45.0 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.144 (n=1727)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0091 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.180 (n=654)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=1983)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.5758` → IC=+0.221 (n=1960)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5758 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.347` → IC=+0.131 (n=592)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 5.347 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.585` → IC=+0.126 (n=1728)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 2.585 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.1798` → IC=+0.137 (n=1960)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.1798 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.163 (n=247)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.4487` → IC=+0.143 (n=601)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4487 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.8141` → IC=+0.129 (n=1202)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.8141 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2793.6768` → IC=+0.188 (n=889)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2793.6768 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.137 (n=1747)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 51.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.235 (n=1616)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.2868` → IC=+0.223 (n=1206)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2868 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1887)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.216 (n=1215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.249 (n=1810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1979` → IC=+0.216 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1979 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2855` → IC=+0.215 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2855 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.244 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.1817` → IC=+0.217 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1817 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.221 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.273 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `2.4722` → IC=+0.217 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4722 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4263` → IC=+0.220 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4263 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1671)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2662.7024` → IC=+0.223 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2662.7024 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.229 (n=821)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.012 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.223 (n=846)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.245 (n=622)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=917)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.02` → IC=+0.290 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.02 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.231 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.409` → IC=+0.246 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.409 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6367` → IC=+0.230 (n=1866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6367 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.280 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.4377` → IC=+0.220 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4377 (IC base=+0.220)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.191 (n=1227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0041 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.169 (n=928)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0083 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3355` → IC=+0.179 (n=2447)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3355 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.205 (n=1389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.3273` → IC=+0.197 (n=2780)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3273 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.7873` → IC=+0.184 (n=422)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.7873 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.754` → IC=+0.192 (n=1188)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.754 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8649` → IC=+0.187 (n=1667)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8649 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.2005` → IC=+0.177 (n=834)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.2005 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1024` → IC=+0.176 (n=995)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1024 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4359` → IC=+0.190 (n=900)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4359 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.5135` → IC=+0.172 (n=900)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5135 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=2580)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.187 (n=2558)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 150.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.166 (n=961)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0036 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.3339` → IC=+0.123 (n=2521)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.3339 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=2709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.0759` → IC=+0.196 (n=956)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.0759 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.22` → IC=+0.121 (n=2606)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.22 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.125 (n=1095)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.434` → IC=+0.147 (n=927)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.434 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `5226.6861` → IC=+0.142 (n=1908)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 5226.6861 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.132 (n=928)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 21.0 (IC base=+0.114)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.198 (n=356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1013` → IC=+0.200 (n=355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1013 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.6262` → IC=+0.207 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6262 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.172 (n=248)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.174 (n=339)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8791` → IC=+0.175 (n=537)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8791 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.160 (n=316)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.8213` → IC=+0.166 (n=525)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.8213 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `14715.6452` → IC=+0.157 (n=537)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 14715.6452 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.201 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.206 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2682` → IC=+0.165 (n=830)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2682 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.155 (n=851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.148 (n=952)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.185 (n=830)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6112 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.742` → IC=+0.148 (n=180)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.742 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.506` → IC=+0.150 (n=995)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.506 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.2004` → IC=+0.151 (n=943)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2004 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6986` → IC=+0.158 (n=843)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6986 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.194 (n=250)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.1142` → IC=+0.162 (n=820)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1142 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=1222)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.160 (n=802)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 288.0 (IC base=+0.147)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.234 (n=592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.2084` → IC=+0.212 (n=592)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2084 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=935)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.34` → IC=+0.235 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.34 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.3604` → IC=+0.203 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3604 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.2103` → IC=+0.203 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2103 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.007` → IC=+0.216 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.007 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8363` → IC=+0.202 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8363 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `1.1822` → IC=+0.215 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1822 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.16` → IC=+0.225 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.16 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.4127` → IC=+0.235 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4127 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.4439` → IC=+0.214 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4439 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.163 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0038 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.096` → IC=+0.132 (n=286)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.096 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.135 (n=590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 11.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.0873` → IC=+0.162 (n=285)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.0873 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.407` → IC=+0.144 (n=223)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 6.407 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.6872` → IC=+0.158 (n=375)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6872 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.140 (n=276)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `7708.578` → IC=+0.144 (n=568)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 7708.578 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.134 (n=356)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 41.0 (IC base=+0.111)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4722` → IC=-0.125 (n=270)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4722
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=526)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.172 (n=617)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0051 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.193 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.9739` → IC=+0.241 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9739 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.339` → IC=+0.214 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.339 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `1.0661` → IC=+0.179 (n=543)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.0661 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `0.7177` → IC=+0.166 (n=551)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.7177 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.177 (n=91)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.4594` → IC=+0.167 (n=199)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4594 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `2.1945` → IC=+0.173 (n=270)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1945 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.165 (n=654)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `3080.6393` → IC=+0.197 (n=206)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3080.6393 (IC base=+0.160)

- **PATRÓN** `ibs_20min` < `0.4722` → IC=+0.146 (n=526)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.4722 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `2878.0292` → IC=+0.148 (n=271)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2878.0292 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.145 (n=243)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 15.0 (IC base=+0.054)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.170 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0238 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.186 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.007 (IC base=+0.154)

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

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.175 (n=192)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6182 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.2537` → IC=+0.184 (n=188)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.2537 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2503.8283` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2503.8283 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.162 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0119 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.133 (n=213)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.6 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.025` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.025 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.128 (n=213)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6515 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.8124` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.8124 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 17.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.179 (n=4612)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0046 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.216 (n=4600)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=14461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.4545` → IC=+0.225 (n=13793)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4545 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1661` → IC=+0.187 (n=5032)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1661 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.443` → IC=+0.246 (n=3391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.443 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.2312` → IC=+0.167 (n=9247)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2312 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.199 (n=1863)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.5936` → IC=+0.195 (n=4453)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5936 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2474.7486` → IC=+0.182 (n=9195)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2474.7486 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.204 (n=10984)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.197 (n=5488)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.1474` → IC=+0.197 (n=5488)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1474 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=4708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.4523` → IC=+0.251 (n=10973)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4523 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.094` → IC=+0.211 (n=1750)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.094 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.722` → IC=+0.187 (n=12026)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.722 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.705` → IC=+0.164 (n=3710)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.705 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.252 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `1.8577` → IC=+0.193 (n=7790)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.8577 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.209 (n=7664)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.252 (n=761)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.231 (n=760)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3566` → IC=+0.213 (n=2281)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3566 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=1111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=1527)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.783` → IC=+0.349 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.783 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.272 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.5813` → IC=+0.227 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5813 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2347)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2014.2192` → IC=+0.221 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2014.2192 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.267 (n=1271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.261 (n=1704)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.124` → IC=+0.275 (n=838)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.124 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.265 (n=1734)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3605` → IC=+0.284 (n=1675)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3605 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.334` → IC=+0.268 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.334 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.286 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.6294` → IC=+0.279 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6294 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=2095)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.201 (n=743)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1794` → IC=+0.166 (n=1482)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1794 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.2726` → IC=+0.206 (n=2223)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2726 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1319` → IC=+0.186 (n=1194)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1319 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.719` → IC=+0.168 (n=372)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.719 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.21` → IC=+0.153 (n=2033)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.21 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6272` → IC=+0.174 (n=741)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6272 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2704` → IC=+0.190 (n=317)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2704 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1415` → IC=+0.159 (n=1905)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1415 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5244` → IC=+0.153 (n=1935)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5244 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `273.0` → IC=+0.181 (n=924)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 273.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1841)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2576` → IC=+0.165 (n=1619)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2576 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6839` → IC=+0.196 (n=1840)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6839 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.5` → IC=+0.168 (n=311)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.5 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.1835` → IC=+0.159 (n=1840)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1835 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1536` → IC=+0.202 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1536 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4311` → IC=+0.155 (n=1738)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4311 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.160 (n=1159)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `257.0` → IC=+0.150 (n=549)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 257.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.232 (n=2266)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.229 (n=2268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2026)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.522` → IC=+0.306 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.522 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.2044` → IC=+0.225 (n=2295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2044 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.7621` → IC=+0.228 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7621 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2700)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.242 (n=1423)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1859` → IC=+0.257 (n=939)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1859 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.259 (n=816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.239 (n=765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0148` → IC=+0.302 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0148 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.96` → IC=+0.289 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.96 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3408` → IC=+0.299 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3408 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7062` → IC=+0.243 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7062 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.1254` → IC=+0.243 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1254 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.258 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.237)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.196 (n=1038)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3332` → IC=+0.152 (n=2077)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3332 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=2467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.2661` → IC=+0.191 (n=2360)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2661 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.5539` → IC=+0.164 (n=602)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.5539 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.183` → IC=+0.152 (n=962)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.183 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.163 (n=1574)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8725 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2367` → IC=+0.174 (n=421)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2367 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5223` → IC=+0.165 (n=1011)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5223 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.1723` → IC=+0.151 (n=1042)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.1723 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7338.742` → IC=+0.236 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7338.742 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.180 (n=764)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 70.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.198 (n=636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0033 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.3462` → IC=+0.146 (n=1676)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3462 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.135 (n=663)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.7344` → IC=+0.188 (n=1905)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.7344 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.325` → IC=+0.179 (n=388)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 9.325 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6234` → IC=+0.150 (n=635)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6234 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.235 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4415` → IC=+0.145 (n=1827)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4415 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `5620.3886` → IC=+0.198 (n=864)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 5620.3886 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.136 (n=1829)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 165.0 (IC base=+0.134)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.138 (n=2376)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0056 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.4521` → IC=+0.202 (n=2376)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4521 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `1.0401` → IC=+0.214 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0401 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.567` → IC=+0.241 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.567 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8893` → IC=+0.153 (n=1585)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8893 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.1611` → IC=+0.133 (n=2454)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1611 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.5777` → IC=+0.128 (n=1018)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5777 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.1893` → IC=+0.138 (n=1049)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.1893 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.134 (n=2429)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2932.5833` → IC=+0.254 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2932.5833 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.149 (n=753)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 27.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.175 (n=759)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0056 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1316` → IC=+0.169 (n=759)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1316 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=2351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.235 (n=2014)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.141 (n=1929)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.241` → IC=+0.126 (n=311)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 9.241 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.463` → IC=+0.136 (n=2195)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.463 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.7137` → IC=+0.157 (n=1001)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7137 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2227` → IC=+0.185 (n=370)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2227 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `2.1505` → IC=+0.143 (n=1853)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1505 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2831.9125` → IC=+0.204 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2831.9125 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.144 (n=1860)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 50.0 (IC base=+0.125)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.238 (n=2289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=2401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.225 (n=1647)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.267 (n=2054)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.2081` → IC=+0.235 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2081 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.776` → IC=+0.265 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.776 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2332` → IC=+0.226 (n=2290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2332 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.64` → IC=+0.224 (n=2289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.64 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.242 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.5119` → IC=+0.245 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5119 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=2085)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2670.4746` → IC=+0.233 (n=1526)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2670.4746 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.220 (n=805)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.234 (n=1094)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.231 (n=1718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.416` → IC=+0.267 (n=2124)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.416 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.933` → IC=+0.257 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.933 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.247 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.288 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.432` → IC=+0.220 (n=2221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.432 (IC base=+0.218)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.173 (n=4101)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.233 (n=1389)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.5011` → IC=+0.202 (n=4158)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5011 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=1550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.195 (n=1859)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.9407` → IC=+0.241 (n=1387)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9407 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.1717` → IC=+0.198 (n=1507)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1717 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.246` → IC=+0.194 (n=2552)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.246 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.223` → IC=+0.219 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.223 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.7028` → IC=+0.206 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7028 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` > `0.8852` → IC=+0.195 (n=1949)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 0.8852 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.1685` → IC=+0.218 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1685 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.4558` → IC=+0.201 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4558 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `1.8532` → IC=+0.196 (n=2731)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.8532 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=3128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `3861.7729` → IC=+0.206 (n=2772)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3861.7729 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.223 (n=1030)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.4871` → IC=+0.187 (n=3089)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.4871 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=1076)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.190 (n=1392)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.1739` → IC=+0.195 (n=1359)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1739 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.6561` → IC=+0.180 (n=532)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6561 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.168` → IC=+0.178 (n=3087)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.168 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1015` → IC=+0.181 (n=2548)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.1015 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.176 (n=2816)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.176 (n=1406)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.5373` → IC=+0.177 (n=1340)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.5373 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.181 (n=2029)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=4101)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.183 (n=1334)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 36.0 (IC base=+0.172)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.239 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.260 (n=177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.5153` → IC=+0.236 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5153 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.7702` → IC=+0.216 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7702 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.179` → IC=+0.216 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.179 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.039` → IC=+0.236 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.039 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.526` → IC=+0.215 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.526 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.222 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.8398` → IC=+0.228 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8398 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4501` → IC=+0.232 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4501 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `12545.7532` → IC=+0.237 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12545.7532 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.227 (n=470)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1125` → IC=+0.180 (n=470)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.1125 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.198 (n=356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 4.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.1496` → IC=+0.182 (n=470)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1496 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.6071` → IC=+0.154 (n=484)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.6071 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6681` → IC=+0.186 (n=100)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6681 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.2114` → IC=+0.152 (n=1086)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2114 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.379` → IC=+0.167 (n=1053)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.379 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8802` → IC=+0.188 (n=712)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8802 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.538` → IC=+0.156 (n=1064)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.538 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.168 (n=709)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11538.052` → IC=+0.163 (n=1068)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11538.052 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `699.0` → IC=+0.162 (n=1022)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 699.0 (IC base=+0.149)

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
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.213 (n=1102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.1487` → IC=+0.222 (n=551)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1487 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.201 (n=567)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.2837` → IC=+0.218 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2837 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.88` → IC=+0.207 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.88 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.148` → IC=+0.207 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.148 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.207 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2423` → IC=+0.205 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2423 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.201 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.1655` → IC=+0.210 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1655 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.4222` → IC=+0.215 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4222 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.235 (n=334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.194 (n=999)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.179 (n=668)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 10.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.7503` → IC=+0.178 (n=999)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7503 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.0817` → IC=+0.172 (n=999)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.0817 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.6433` → IC=+0.188 (n=190)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6433 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.74` → IC=+0.174 (n=1023)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 6.74 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.1021` → IC=+0.186 (n=879)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.1021 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.7215` → IC=+0.172 (n=892)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.7215 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.190 (n=421)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `2.1843` → IC=+0.184 (n=860)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.1843 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `1.7774` → IC=+0.173 (n=652)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.7774 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `7411.0388` → IC=+0.187 (n=999)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 7411.0388 (IC base=+0.170)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.217 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.3032` → IC=+0.181 (n=359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3032 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.196 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 3.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5469` → IC=+0.204 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5469 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1937` → IC=+0.210 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1937 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.559` → IC=+0.220 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.559 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `0.694` → IC=+0.211 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.694 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.225 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `1.468` → IC=+0.188 (n=524)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.468 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=645)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `3413.2842` → IC=+0.223 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3413.2842 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.191 (n=464)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 48.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.213 (n=134)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.206 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.372` → IC=+0.236 (n=267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.372 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.217 (n=270)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.1837` → IC=+0.242 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1837 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.772` → IC=+0.230 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.772 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.035` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.035 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.985` → IC=+0.191 (n=347)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.985 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.756` → IC=+0.202 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.756 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` > `0.6799` → IC=+0.187 (n=400)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6799 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.223 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.6271` → IC=+0.194 (n=171)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.6271 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.2075` → IC=+0.202 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2075 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `3873.4371` → IC=+0.199 (n=267)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3873.4371 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.223 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.186)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.153 (n=594)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0038 (IC base=+0.073)

- **PATRÓN** `ibs_20min` > `0.4221` → IC=+0.146 (n=1257)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.4221 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.1469` → IC=+0.138 (n=661)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1469 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.484` → IC=+0.171 (n=284)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.484 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.169 (n=176)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.073)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.145 (n=212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0029 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.1905` → IC=+0.262 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1905 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.0873` → IC=+0.136 (n=559)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.0873 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.023` → IC=+0.137 (n=235)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.023 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.1466` → IC=+0.202 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1466 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.4646` → IC=+0.145 (n=218)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4646 (IC base=+0.059)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.139 (n=460)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0058 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.140 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 18.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.3879` → IC=+0.168 (n=429)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3879 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.161 (n=219)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.090)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.122 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0046 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.297 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` < `0.2112` → IC=+0.132 (n=294)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2112 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.179` → IC=+0.143 (n=256)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 7.179 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` > `0.8132` → IC=+0.138 (n=175)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.8132 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.1526` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1526 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `2.5091` → IC=+0.139 (n=239)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5091 (IC base=+0.082)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.144 (n=296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0046 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.124 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.6816` → IC=+0.203 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6816 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.1239` → IC=+0.176 (n=217)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1239 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.74` → IC=+0.248 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.74 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `1184.9665` → IC=+0.139 (n=364)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1184.9665 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.0162` → IC=+0.318 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0162 (IC base=+0.013)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.103` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 11.103 (IC base=+0.013)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0097` → IC=-0.207 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0097
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=169)

- **FILTRO** `ibs_20min` > `0.16` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` > 0.16
  - _Potencial_: sin este filtro IC_bueno=+0.266 (n=139)

- **PATRÓN** `ibs_20min` > `0.7609` → IC=+0.164 (n=278)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.7609 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` > `0.73` → IC=+0.145 (n=105)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.73 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.182 (n=83)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.038)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.178 (n=150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0081 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.16` → IC=+0.266 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.16 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.196` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.196 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.936` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.936 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `0.9765` → IC=+0.177 (n=63)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.9765 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.1474` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1474 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `2.18` → IC=+0.186 (n=103)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.18 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `2.5298` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5298 (IC base=+0.068)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.208 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.068)

- **PATRÓN** `libro_liquidez` > `774.2903` → IC=+0.179 (n=82)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 774.2903 (IC base=+0.068)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1826` → IC=-0.306 (n=65)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1826
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=197)

- **FILTRO** `dist_vwap_pct` > `0.2381` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=249)

- **FILTRO** `volumen_regimen` < `0.7468` → IC=-0.338 (n=66)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=198)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.379 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=172)

- **FILTRO** `ibs_20min` > `0.9063` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9063
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=172)

- **FILTRO** `dist_vwap_pct` > `0.3328` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3328
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=195)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=198)

- **FILTRO** `volumen_pendiente_norm` > `0.0718` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=123)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.233 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=44)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=66)

- **FILTRO** `volumen_spike_ratio` > `3.7991` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.7991
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=49)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.308 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=75)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=75)

- **FILTRO** `volumen_spike_ratio` > `1.5538` → IC=-0.324 (n=32)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5538
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0026` → IC=-0.375 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=66)

- **FILTRO** `ibs_20min` < `0.6037` → IC=-0.435 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6037
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=59)

- **FILTRO** `drift_60min` |x|> `0.1855` → IC=-0.273 (n=20)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1855
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=61)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.354 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=45)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `ibs_20min` > `0.9508` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.9508 (IC base=-0.156)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=73)

- **FILTRO** `volumen_spike_ratio` < `1.5614` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5614
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=48)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=63)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.168 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0058 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.127 (n=210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.6645` → IC=+0.135 (n=420)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.6645 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.4941` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.4941 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` < `0.8589` → IC=+0.122 (n=281)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.8589 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` < `1.5351` → IC=+0.162 (n=140)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5351 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.175 (n=411)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.156 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.376` → IC=+0.215 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.376 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.083)

- **PATRÓN** `libro_liquidez` > `1330.8385` → IC=+0.125 (n=467)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1330.8385 (IC base=+0.083)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6496` → IC=-0.273 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6496
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=128)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.236 (n=70)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.158 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.1381` → IC=+0.209 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1381 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.925` → IC=+0.179 (n=166)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 4.925 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.6869` → IC=+0.190 (n=188)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.6869 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.1891` → IC=+0.187 (n=180)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1891 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.2815` → IC=+0.181 (n=158)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.2815 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.4468` → IC=+0.180 (n=179)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4468 (IC base=+0.156)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1521` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1521
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=122)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `1535.3678` → IC=+0.129 (n=141)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1535.3678 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.2061` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.2061 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.629` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.629 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `2393.5742` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2393.5742 (IC base=+0.070)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.1679` → IC=-0.207 (n=56)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1679
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=58)

- **FILTRO** `dist_vwap_pct` > `0.2725` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2725
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=92)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.288 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.264 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.250 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.6388` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6388 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` < `0.1413` → IC=+0.244 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1413 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.349` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.349 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.2519` → IC=+0.291 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2519 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.1062` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1062 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.239 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.069)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.283)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.283)

- **PATRÓN** `drift_15min` |x|≤ `0.9257` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.9257 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.351 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.283)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.212)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.212)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `1.251` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.251 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.263 (n=36)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.212)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.212)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.283)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.283)

- **PATRÓN** `drift_15min` |x|≤ `0.9257` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.9257 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.351 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.283)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.212)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.212)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `1.251` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.251 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.263 (n=36)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.212)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.212)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=1026)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2870.5456` → IC=+0.135 (n=478)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2870.5456 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=1026)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2870.5456` → IC=+0.135 (n=478)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2870.5456 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=158)

- **FILTRO** `libro_liquidez` < `2669.5667` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `libro_liquidez` < 2669.5667
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=131)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=246)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=232)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=55)

- **FILTRO** `hora_utc` < `3.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=59)

- **FILTRO** `libro_liquidez` < `10893.2451` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 10893.2451
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=57)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4919.88` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `liq_usd_total` < 4919.88
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

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
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

### LIQUIDACIONES_15M#XRP#15min
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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2895)

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
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=116)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.130 (n=98)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 13.0 (IC base=+0.041)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.132 (n=183)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.495 (IC base=+0.039)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=1074)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1028)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=672)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=358)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=339)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.154 (n=128)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.021)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=780)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=780)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=614)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=601)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=601)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=217)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=217)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=179)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=144)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=149)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=173)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=175)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=306)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=306)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=216)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.145 (n=74)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=157)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.123 (n=1487)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1559)

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
- **FILTRO** `py_entrada` < `0.5` → IC=-0.146 (n=193)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=101)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.140 (n=98)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=262)

- **PATRÓN** `py_entrada` < `0.48` → IC=+0.122 (n=125)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.48 (IC base=+0.014)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.214 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.043)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.122 (n=141)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=52)

- **FILTRO** `restante_min` < `12.46` → IC=-0.133 (n=96)

  - _Acción_: SKIP cuando `restante_min` < 12.46
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=97)

- **FILTRO** `lag_apertura_s` > `152.45` → IC=-0.133 (n=96)

  - _Acción_: SKIP cuando `lag_apertura_s` > 152.45
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=97)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.128 (n=127)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=73)

- **FILTRO** `lag_apertura_s` > `76.6` → IC=-0.144 (n=99)

  - _Acción_: SKIP cuando `lag_apertura_s` > 76.6
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=101)

- **PATRÓN** `py_entrada` < `0.58` → IC=+0.129 (n=60)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.58 (IC base=+0.058)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.144 (n=203)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=70)

- **FILTRO** `profundidad_ratio` < `37.6` → IC=-0.200 (n=68)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.6
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=205)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.240 (n=48)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=205)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.125 (n=222)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=125)

- **FILTRO** `restante_min` < `3.33` → IC=-0.190 (n=114)

  - _Acción_: SKIP cuando `restante_min` < 3.33
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=233)

- **FILTRO** `lag_apertura_s` > `98.98` → IC=-0.198 (n=117)

  - _Acción_: SKIP cuando `lag_apertura_s` > 98.98
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=230)

- **FILTRO** `profundidad_ratio` < `22.7` → IC=-0.124 (n=91)

  - _Acción_: SKIP cuando `profundidad_ratio` < 22.7
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=186)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.132 (n=55)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=207)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=207)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=109)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.159 (n=174)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=221)

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

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.169 (n=4674)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=15148)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.166 (n=5133)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=15415)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.192 (n=855)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=2674)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.152 (n=861)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=2822)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.172 (n=714)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2252)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.176 (n=890)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=2694)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.186 (n=924)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=2803)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.160 (n=851)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=2687)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2565)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=3305)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=403)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=312)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=383)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `2028.3639` → IC=-0.163 (n=339)

  - _Acción_: SKIP cuando `libro_liquidez` < 2028.3639
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=689)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=13705)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=30831)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=10556)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=33980)

- **FILTRO** `ibs_7min` < `0.2535` → IC=-0.233 (n=11134)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2535
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=33402)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=14929)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=29607)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.235 (n=13608)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=43069)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.178 (n=14144)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=42533)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=2219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=5363)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=1818)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=5764)

- **FILTRO** `ibs_7min` < `0.7083` → IC=-0.249 (n=2502)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=5080)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.191 (n=1588)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5994)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.269 (n=2387)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=7470)

- **FILTRO** `ibs_7min` > `0.7778` → IC=-0.210 (n=2461)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=7396)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.132 (n=1801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=5802)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.245 (n=1887)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=5716)

- **FILTRO** `ibs_7min` < `0.7391` → IC=-0.195 (n=1899)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7391
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5704)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.184 (n=1892)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=5711)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=1839)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=5894)

- **FILTRO** `ibs_7min` > `0.2655` → IC=-0.192 (n=1931)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2655
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5802)

- **FILTRO** `ballena_activa_n` > `147.0` → IC=-0.186 (n=1933)

  - _Acción_: SKIP cuando `ballena_activa_n` > 147.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=5800)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.166 (n=1780)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=5458)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.319 (n=1724)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=5514)

- **FILTRO** `ibs_7min` < `0.703` → IC=-0.248 (n=2386)

  - _Acción_: SKIP cuando `ibs_7min` < 0.703
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=4852)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.222 (n=1609)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5629)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.244 (n=2356)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=8107)

- **FILTRO** `ibs_7min` > `0.7342` → IC=-0.172 (n=2615)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=7848)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=2362)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=4959)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.240 (n=2184)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=5137)

- **FILTRO** `ibs_7min` < `0.7381` → IC=-0.184 (n=1830)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7381
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5491)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.187 (n=1798)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5523)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.268 (n=1853)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=5697)

- **FILTRO** `ibs_7min` > `0.2762` → IC=-0.180 (n=1887)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2762
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5663)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.179 (n=1887)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5663)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.272 (n=1775)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5709)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.233 (n=1868)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=5616)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.174 (n=2694)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=8113)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.279 (n=1761)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5547)

- **FILTRO** `ibs_7min` < `0.2353` → IC=-0.222 (n=1824)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2353
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5484)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.201 (n=1769)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5539)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.207 (n=2488)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=7779)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.154 (n=296)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=967)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1248)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.153 (n=148)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=522)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

- **FILTRO** `libro_liquidez` < `7941.0101` → IC=-0.131 (n=348)

  - _Acción_: SKIP cuando `libro_liquidez` < 7941.0101
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=709)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=362)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.146 (n=156)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=308)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=416)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=599)

- **FILTRO** `libro_liquidez` < `3306.2556` → IC=-0.155 (n=166)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.2556
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=501)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=288)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3979` → IC=+0.141 (n=972)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.3979 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.136 (n=448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 14.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.131 (n=361)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 4.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `445.688` → IC=+0.158 (n=325)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 445.688 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `3779.4381` → IC=+0.130 (n=441)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3779.4381 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.148 (n=319)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 14.0 (IC base=+0.127)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4372` → IC=+0.154 (n=76)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.4372 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.223 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `2659.7686` → IC=+0.244 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2659.7686 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.201 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.145)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.163 (n=87)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 10.0 (IC base=+0.109)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4144` → IC=+0.187 (n=132)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio` |x|> 0.4144 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.219 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7275.4252` → IC=+0.137 (n=177)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 7275.4252 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.200 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 73.0 (IC base=+0.126)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4335` → IC=+0.228 (n=79)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4335 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.233 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.148)

- **PATRÓN** `total_vol_5m` < `4970.298` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 4970.298 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `3420.0004` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3420.0004 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 28.0 (IC base=+0.148)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.139 (n=167)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.125 (n=166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 13.0 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=116)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3657.3836` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3657.3836 (IC base=+0.102)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.6961` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.6961
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=122)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.266 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=278)

- **FILTRO** `T_h` > `129.5932` → IC=-0.257 (n=138)

  - _Acción_: SKIP cuando `T_h` > 129.5932
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=416)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `88.6373` → IC=-0.357 (n=40)

  - _Acción_: SKIP cuando `T_h` > 88.6373
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=124)

- **FILTRO** `pct_vs_K` |x|> `4.2515` → IC=-0.286 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2515
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=124)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.272 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.054)

- **PATRÓN** `pct_vs_K` |x|≤ `1.73` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `pct_vs_K` |x|≤ 1.73 (IC base=-0.054)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `8.3214` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.3214
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.186 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=34)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.214 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=-0.077)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.202 (n=377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=126)

- **FILTRO** `sigma_h` > `0.0089` → IC=-0.307 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=329)

- **FILTRO** `sigma_h` < `0.0048` → IC=-0.311 (n=109)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=327)

- **FILTRO** `T_h` > `54.8663` → IC=-0.299 (n=326)

  - _Acción_: SKIP cuando `T_h` > 54.8663
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=110)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0042` → IC=-0.189 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=131)

- **FILTRO** `T_h` > `77.6652` → IC=-0.161 (n=116)

  - _Acción_: SKIP cuando `T_h` > 77.6652
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

- **FILTRO** `T_h` > `73.6519` → IC=-0.285 (n=119)

  - _Acción_: SKIP cuando `T_h` > 73.6519
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=41)

- **FILTRO** `pct_vs_K` |x|> `2.8429` → IC=-0.407 (n=52)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8429
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=108)

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
- **FILTRO** `sigma_h` < `0.0094` → IC=-0.300 (n=103)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=37)

- **FILTRO** `T_h` > `135.9851` → IC=-0.250 (n=34)

  - _Acción_: SKIP cuando `T_h` > 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=106)

- **FILTRO** `sigma_h` > `0.0086` → IC=-0.300 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0086
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=100)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.300 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=100)

- **FILTRO** `T_h` > `56.6209` → IC=-0.291 (n=89)

  - _Acción_: SKIP cuando `T_h` > 56.6209
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=44)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0078` → IC=-0.197 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=94)

- **FILTRO** `T_h` > `113.0501` → IC=-0.156 (n=62)

  - _Acción_: SKIP cuando `T_h` > 113.0501
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=63)

- **FILTRO** `sigma_h` > `0.0132` → IC=-0.344 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=59)

- **FILTRO** `T_h` > `36.4645` → IC=-0.382 (n=66)

  - _Acción_: SKIP cuando `T_h` > 36.4645
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1221` → IC=+0.460 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1221 (IC base=+0.332)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.380 (n=81)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.332)

- **PATRÓN** `T_h` < `1.0173` → IC=+0.349 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0173 (IC base=+0.332)

- **PATRÓN** `T_h` > `0.8229` → IC=+0.393 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8229 (IC base=+0.332)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.332)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.347 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.332)

- **PATRÓN** `edge` > `0.095` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.095 (IC base=+0.422)

- **PATRÓN** `sigma_h` < `0.0121` → IC=+0.430 (n=169)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0121 (IC base=+0.422)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.446 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.422)

- **PATRÓN** `T_h` > `1.48` → IC=+0.455 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.48 (IC base=+0.422)

- **PATRÓN** `dist_50` > `0.3811` → IC=+0.474 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3811 (IC base=+0.422)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.422)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1026` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1026 (IC base=+0.429)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.417 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.429)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.458 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.429)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.429)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.422 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.429)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.478 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.429)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.439 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.429)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1885` → IC=+0.480 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1885 (IC base=+0.427)

- **PATRÓN** `sigma_h` < `0.0161` → IC=+0.461 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0161 (IC base=+0.427)

- **PATRÓN** `T_h` > `0.7758` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7758 (IC base=+0.427)

- **PATRÓN** `dist_50` > `0.3288` → IC=+0.461 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3288 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.427)

- **PATRÓN** `edge` > `0.2005` → IC=+0.477 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.477 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.462)

- **PATRÓN** `T_h` > `1.2259` → IC=+0.477 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2259 (IC base=+0.462)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.492 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=257)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=343)

- **PATRÓN** `streak_estiramiento` < `0.4511` → IC=+0.125 (n=86)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.4511 (IC base=+0.022)

- **PATRÓN** `streak_estiramiento` < `0.4302` → IC=+0.206 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4302 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `2507.3405` → IC=+0.122 (n=125)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2507.3405 (IC base=+0.038)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=25)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `982893.6` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `volumen_racha` > 982893.6
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=42)

- **FILTRO** `streak_estiramiento` > `0.479` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.479
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=58)

- **PATRÓN** `volumen_racha` < `982893.6` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_racha` < 982893.6 (IC base=+0.018)

- **PATRÓN** `streak_estiramiento` < `0.4177` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.4177 (IC base=+0.018)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.141 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 10.0 (IC base=+0.082)

- **PATRÓN** `streak_estiramiento` < `0.3368` → IC=+0.167 (n=61)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.3368 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.148 (n=103)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 47.0 (IC base=+0.082)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=607)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `volumen_racha` > `9229.0178` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 9229.0178
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

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

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.050)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=833)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1320)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=980)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=985)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3524)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1883)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.202 (n=889)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.234 (n=888)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.1628` → IC=+0.202 (n=2344)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1628 (IC base=+0.194)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2233` → IC=+0.198 (n=888)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio_macro` |x|> 0.2233 (IC base=+0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1309` → IC=+0.212 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1309 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.203 (n=2477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.195 (n=2730)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `ibs_15` > `0.6032` → IC=+0.268 (n=2662)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6032 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.1214` → IC=+0.194 (n=1238)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1214 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.956` → IC=+0.272 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.956 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `6719.9729` → IC=+0.200 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6719.9729 (IC base=+0.194)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=1126)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.227 (n=503)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.271 (n=168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.216)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2012` → IC=+0.248 (n=228)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2012 (IC base=+0.216)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1462` → IC=+0.242 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1462 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `ibs_15` > `0.7143` → IC=+0.280 (n=503)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7143 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.246 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.287 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `16217.9862` → IC=+0.253 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16217.9862 (IC base=+0.216)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.513` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.513
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=651)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.5731` → IC=-0.158 (n=185)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5731
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=556)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.170 (n=186)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0034 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0667` → IC=+0.152 (n=245)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0667 (IC base=+0.135)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2368` → IC=+0.156 (n=187)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.2368 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.151 (n=213)

  - _Acción_: Kelly boost +0.76€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.138 (n=580)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.5731` → IC=+0.233 (n=556)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5731 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.1536` → IC=+0.139 (n=297)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1536 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.11` → IC=+0.136 (n=402)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.11 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.973` → IC=+0.271 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.973 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `3507.1457` → IC=+0.141 (n=497)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3507.1457 (IC base=+0.135)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `20.209` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.209
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=228)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.147 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0052 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.198 (n=147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0089 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1927` → IC=+0.186 (n=390)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1927 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0624` → IC=+0.159 (n=441)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.0624 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3427` → IC=+0.171 (n=393)

  - _Acción_: Kelly boost +0.85€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3427 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.161 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 12.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.9286` → IC=+0.339 (n=147)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9286 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.72` → IC=+0.196 (n=44)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.72 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1943` → IC=+0.149 (n=411)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1943 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.026` → IC=+0.204 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.026 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=283)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.146)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.167 (n=61)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.029)

- **PATRÓN** `libro_liquidez` > `3357.6986` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3357.6986 (IC base=+0.029)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.261 (n=563)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1659` → IC=+0.218 (n=555)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1659 (IC base=+0.217)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0668` → IC=+0.224 (n=563)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0668 (IC base=+0.217)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.272 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.231 (n=556)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.217)

- **PATRÓN** `ibs_15` > `0.5882` → IC=+0.296 (n=630)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5882 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.1342` → IC=+0.224 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1342 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.758` → IC=+0.254 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.758 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2980.6496` → IC=+0.302 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2980.6496 (IC base=+0.217)

- **PATRÓN** `ibs_15` < `0.1081` → IC=+0.160 (n=674)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` < 0.1081 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.365 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.380 (n=181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.359 (n=361)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1503` → IC=+0.387 (n=360)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1503 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1362` → IC=+0.391 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1362 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.376 (n=547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.395 (n=541)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.4169` → IC=+0.388 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4169 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.188` → IC=+0.373 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.188 (IC base=+0.360)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `3836.614` → IC=+0.372 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3836.614 (IC base=+0.360)

- **PATRÓN** `ballena_activa_n` < `440.0` → IC=+0.379 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 440.0 (IC base=+0.360)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.361 (n=257)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.359)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.369 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.359)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.360 (n=98)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.359)

- **PATRÓN** `drift_15min` |x|≤ `0.5096` → IC=+0.363 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5096 (IC base=+0.359)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1528` → IC=+0.383 (n=194)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1528 (IC base=+0.359)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1344` → IC=+0.395 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1344 (IC base=+0.359)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.359)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.387 (n=291)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` > `0.3935` → IC=+0.395 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3935 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.481` → IC=+0.363 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.481 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` < `25.57` → IC=+0.359 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 25.57 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `15251.5468` → IC=+0.388 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15251.5468 (IC base=+0.359)

- **PATRÓN** `ballena_activa_n` < `499.0` → IC=+0.407 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 499.0 (IC base=+0.359)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.358 (n=111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.379 (n=114)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.370 (n=167)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.377 (n=225)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.383 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.418 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.405 (n=250)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.4419` → IC=+0.365 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4419 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` < `0.1212` → IC=+0.358 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1212 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.379 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.358 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.360)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `4293.66` → IC=+0.384 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4293.66 (IC base=+0.360)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.366 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.360)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.217 (n=925)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2777)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=1401)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2301)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.189 (n=593)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=-0.067)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.221 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.279 (n=890)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.200 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2619` → IC=+0.196 (n=755)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2619 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2224` → IC=+0.268 (n=993)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2224 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.3519` → IC=+0.281 (n=2979)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3519 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.6551` → IC=+0.295 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6551 (IC base=-0.012)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.211 (n=524)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1574)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.228 (n=524)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=1574)

- **FILTRO** `sigma_ewma_delta_pct` > `23.641` → IC=-0.264 (n=299)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.641
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=1799)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=2042)

- **FILTRO** `libro_liquidez` < `16316.9902` → IC=-0.196 (n=1384)

  - _Acción_: SKIP cuando `libro_liquidez` < 16316.9902
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=714)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.176 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0027 (IC base=+0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1979` → IC=+0.305 (n=121)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1979 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1066` → IC=+0.295 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1066 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.123 (n=422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 12.0 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.7533` → IC=+0.332 (n=265)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7533 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.1012` → IC=+0.300 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1012 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.2456` → IC=+0.281 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2456 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.459` → IC=+0.125 (n=307)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 8.459 (IC base=+0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.236 (n=51)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.190)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.311 (n=51)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.190)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.190)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=-0.190)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=574)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.151 (n=391)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0058 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.163 (n=396)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0038 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.178 (n=296)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1103 (IC base=+0.146)

- **PATRÓN** `drift_15min` |x|≤ `0.4046` → IC=+0.147 (n=148)

  - _Acción_: Kelly boost +0.73€ cuando `drift_15min` |x|≤ 0.4046 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1405` → IC=+0.158 (n=296)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.1405 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2962` → IC=+0.191 (n=331)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2962 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.174 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.6326` → IC=+0.251 (n=444)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6326 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.148 (n=325)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.656` → IC=+0.244 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.656 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=574)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `11008.7835` → IC=+0.180 (n=148)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 11008.7835 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.245 (n=1041)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.3509` → IC=+0.243 (n=916)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3509 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.757` → IC=+0.253 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.757 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2128` → IC=+0.262 (n=472)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2128 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.248 (n=403)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.3647` → IC=+0.270 (n=1041)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3647 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.7746` → IC=+0.308 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7746 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.574` → IC=+0.254 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.574 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.584` → IC=+0.244 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.584 (IC base=+0.241)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1716` → IC=-0.250 (n=290)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1716
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=566)

- **FILTRO** `drift_15min` |x|> `0.8879` → IC=-0.281 (n=213)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8879
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=643)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.220 (n=369)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=487)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.177)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.177)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.177)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.177)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0787` → IC=+0.244 (n=416)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0787 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.3462` → IC=+0.286 (n=465)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3462 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.172` → IC=+0.248 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.172 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1276` → IC=-0.224 (n=520)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1276
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=521)

- **FILTRO** `sigma_h` > `0.0193` → IC=-0.247 (n=520)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0193
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=521)

- **FILTRO** `drift_15min` |x|> `1.2161` → IC=-0.256 (n=260)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2161
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=781)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.200)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.200)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1482` → IC=+0.275 (n=332)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1482 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1101` → IC=+0.302 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1101 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=730)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.8075` → IC=+0.350 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8075 (IC base=-0.026)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.032)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.032)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.291 (n=787)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.288 (n=799)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.327 (n=299)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.301 (n=299)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.224` → IC=+0.306 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.224 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=937)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.320 (n=894)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.327 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.754` → IC=+0.353 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.754 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `12879.5491` → IC=+0.306 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12879.5491 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.312 (n=163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.324 (n=163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.286)

- **PATRÓN** `drift_15min` |x|≤ `0.4183` → IC=+0.287 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4183 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2522` → IC=+0.311 (n=162)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2522 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.310 (n=487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.314 (n=486)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2565` → IC=+0.334 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2565 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.837` → IC=+0.362 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.837 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.285 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16341.0554` → IC=+0.329 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16341.0554 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.296 (n=273)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.295 (n=408)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.320 (n=137)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.292 (n=272)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3017` → IC=+0.314 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3017 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.312 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.329 (n=408)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2774` → IC=+0.311 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2774 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.173` → IC=+0.333 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.173 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0872` → IC=-0.256 (n=76)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0872
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=230)

- **FILTRO** `sigma_h` > `0.0042` → IC=-0.245 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=202)

- **FILTRO** `drift_60min` |x|> `0.2527` → IC=-0.154 (n=76)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2527
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=230)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.196 (n=67)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=134)

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

- **FILTRO** `drift_15min` |x|> `0.3481` → IC=-0.278 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3481
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1941` → IC=-0.231 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.296` → IC=-0.370 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.296
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.222 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0624` → IC=-0.206 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0624
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=31)

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
- **PATRÓN** `T_h` > `82.5234` → IC=+0.218 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 82.5234 (IC base=+0.203)

- **PATRÓN** `ratio` < `0.9763` → IC=+0.444 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9763 (IC base=+0.203)

- **PATRÓN** `T_h` > `145.7409` → IC=+0.388 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7409 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0572` → IC=+0.451 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0572 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.3918` → IC=+0.209 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.182)

- **PATRÓN** `ratio` < `0.972` → IC=+0.415 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.972 (IC base=+0.182)

- **PATRÓN** `T_h` > `109.696` → IC=+0.300 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.696 (IC base=+0.291)

- **PATRÓN** `ratio` > `1.0228` → IC=+0.330 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0228 (IC base=+0.291)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.256 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.238)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.417 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.238)

- **PATRÓN** `T_h` > `111.9712` → IC=+0.347 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9712 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.0127` → IC=+0.363 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0127 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.401)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6032 sube el IC de +0.194 a +0.268 en UPDOWN_GBM#15min (n=2662). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7143 sube el IC de +0.216 a +0.280 en UPDOWN_GBM#BTC#15min (n=503). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5731 sube el IC de +0.135 a +0.233 en UPDOWN_GBM#ETH#15min (n=556). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9286 sube el IC de +0.146 a +0.339 en UPDOWN_GBM#SOL#15min (n=147). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5882 sube el IC de +0.217 a +0.296 en UPDOWN_GBM#XRP#15min (n=630). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1081 sube el IC de +0.068 a +0.160 en UPDOWN_GBM#XRP#15min (n=674). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.067 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=890). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3519 sube el IC de -0.012 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=2979). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.088 a +0.332 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=265). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.190 a +0.311 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6326 sube el IC de +0.146 a +0.251 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=444). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3647 sube el IC de +0.241 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1041). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.177 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3462 sube el IC de -0.038 a +0.286 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=465). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.200 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=730). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.288 a +0.320 en UPDOWN_GBM_IBS_ALTO (n=894). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.286 a +0.314 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=486). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.289 a +0.329 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=408). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.360 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=541). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.359 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=291). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.360 a +0.405 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=250). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1627 | +0.087 | +177.95€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1627 | +0.087 | +177.95€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1256 | +0.091 | +150.92€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1256 | +0.091 | +150.92€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 268 | +0.067 | +11.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 268 | +0.067 | +11.32€ | 6 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 330 | +0.003 | +61.83€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 330 | +0.003 | +61.83€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 257 | +0.006 | +52.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 257 | +0.006 | +52.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 51 | +0.009 | +6.63€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 51 | +0.009 | +6.63€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 35461 | -0.084 | -4648.98€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1782 | -0.017 | -235.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 33679 | -0.087 | -4413.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4414 | -0.116 | -759.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4414 | -0.116 | -759.01€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1782 | -0.017 | -235.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1782 | -0.017 | -235.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4096 | -0.113 | -841.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4096 | -0.113 | -841.60€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9186 | +0.008 | -858.50€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9186 | +0.008 | -858.50€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9061 | -0.110 | -690.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9061 | -0.110 | -690.52€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6922 | -0.151 | -1263.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6922 | -0.151 | -1263.43€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 27729 | -0.019 | +3697.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 7171 | +0.002 | +1763.68€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 20558 | -0.027 | +1933.45€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 27729 | -0.019 | +3697.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 7171 | +0.002 | +1763.68€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 20558 | -0.027 | +1933.45€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 121976 | +0.113 | -5358.52€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 16741 | +0.182 | -524.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 522 | -0.040 | -61.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 97197 | +0.103 | -4499.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7516 | +0.104 | -272.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 16136 | +0.103 | -1106.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 56 | -0.155 | +9.14€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 16065 | +0.105 | -1103.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 24030 | +0.128 | -414.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4920 | +0.195 | -152.31€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 16116 | +0.116 | -162.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2952 | +0.089 | -77.60€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 16185 | +0.095 | -1241.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 64 | -0.106 | -4.03€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 16106 | +0.096 | -1226.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 25916 | +0.124 | -439.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6867 | +0.175 | -115.99€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 16304 | +0.107 | -260.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2733 | +0.101 | -55.12€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 23555 | +0.114 | -1286.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4776 | +0.191 | -270.33€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 425 | -0.004 | -7.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 16523 | +0.093 | -868.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1831 | +0.133 | -139.91€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 16154 | +0.102 | -869.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 58 | -0.050 | +9.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 16083 | +0.102 | -878.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 19484 | +0.194 | -1222.96€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 19484 | +0.194 | -1222.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4507 | +0.174 | -419.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4507 | +0.174 | -419.32€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2184 | +0.200 | -43.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2184 | +0.200 | -43.98€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4438 | +0.181 | -357.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4438 | +0.181 | -357.15€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3897 | +0.242 | -138.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3897 | +0.242 | -138.65€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4379 | +0.190 | -277.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4379 | +0.190 | -277.62€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 896 | +0.425 | -34.01€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 896 | +0.425 | -34.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 352 | +0.432 | -7.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 352 | +0.432 | -7.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 344 | +0.428 | -10.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 344 | +0.428 | -10.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 188 | +0.405 | -12.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 188 | +0.405 | -12.81€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 67801 | +0.200 | -5018.95€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 67801 | +0.200 | -5018.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 11662 | +0.184 | -1220.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 11662 | +0.184 | -1220.05€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 10923 | +0.224 | -384.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 10923 | +0.224 | -384.03€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 11640 | +0.177 | -1295.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 11640 | +0.177 | -1295.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10984 | +0.221 | -406.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10984 | +0.221 | -406.54€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 11232 | +0.202 | -752.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 11232 | +0.202 | -752.57€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 11360 | +0.194 | -960.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 11360 | +0.194 | -960.46€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 25853 | +0.118 | +245.35€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 25853 | +0.118 | +245.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 12843 | +0.121 | +195.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 12843 | +0.121 | +195.54€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 13010 | +0.114 | +49.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 13010 | +0.114 | +49.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1804 | +0.288 | -25.67€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1804 | +0.288 | -25.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 815 | +0.280 | -17.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 815 | +0.280 | -17.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 871 | +0.286 | -12.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 871 | +0.286 | -12.44€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 118 | +0.350 | +4.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 118 | +0.350 | +4.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 820 | +0.440 | +2.33€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 820 | +0.440 | +2.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 396 | +0.440 | -0.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 396 | +0.440 | -0.26€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 378 | +0.442 | +2.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 378 | +0.442 | +2.05€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1400 | +0.068 | -68.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 517 | +0.057 | -41.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 883 | +0.074 | -26.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 68 | +0.100 | +1.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 68 | +0.100 | +1.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1090 | +0.074 | -33.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 207 | +0.074 | -7.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 883 | +0.074 | -26.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 242 | +0.029 | -36.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 242 | +0.029 | -36.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 49947 | +0.100 | -1286.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4056 | +0.093 | +62.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 45891 | +0.100 | -1348.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 27659 | +0.104 | -296.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4056 | +0.093 | +62.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 23603 | +0.106 | -359.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 9980 | +0.109 | -28.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 9980 | +0.109 | -28.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 12308 | +0.080 | -961.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 12308 | +0.080 | -961.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 871 | +0.203 | -101.16€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 871 | +0.203 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 871 | +0.203 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 871 | +0.203 | -101.16€ | 2 | 4 |
| ✅ GBM_LATE_15M | 34790 | +0.090 | +17388.21€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 34790 | +0.090 | +17388.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5857 | +0.205 | +4553.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5857 | +0.205 | +4553.77€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 5171 | +0.178 | +3743.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5171 | +0.178 | +3743.61€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 6180 | +0.202 | +4708.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6180 | +0.202 | +4708.70€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 4902 | +0.036 | +1251.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4902 | +0.036 | +1251.70€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4974 | -0.029 | +1078.19€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4974 | -0.029 | +1078.19€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 7706 | -0.036 | +2052.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7706 | -0.036 | +2052.25€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 37730 | +0.087 | +20121.01€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 37730 | +0.087 | +20121.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7336 | +0.010 | +3725.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7336 | +0.010 | +3725.00€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7834 | +0.013 | +1673.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7834 | +0.013 | +1673.87€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5309 | +0.269 | +5505.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5309 | +0.269 | +5505.87€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 6414 | +0.013 | +1448.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 6414 | +0.013 | +1448.09€ | 1 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6150 | +0.037 | +2477.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6150 | +0.037 | +2477.82€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4687 | +0.292 | +5290.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4687 | +0.292 | +5290.36€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 27784 | +0.177 | +21902.39€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 27784 | +0.177 | +21902.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4210 | +0.218 | +3544.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4210 | +0.218 | +3544.71€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4396 | +0.151 | +3213.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4396 | +0.151 | +3213.22€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4405 | +0.218 | +3687.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4405 | +0.218 | +3687.36€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4676 | +0.138 | +3475.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4676 | +0.138 | +3475.81€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5199 | +0.128 | +3876.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5199 | +0.128 | +3876.50€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4898 | +0.216 | +4104.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4898 | +0.216 | +4104.80€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7522 | +0.140 | +3676.34€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7522 | +0.140 | +3676.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 341 | +0.141 | +188.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 341 | +0.141 | +188.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2330 | +0.148 | +1316.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2330 | +0.148 | +1316.72€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 376 | +0.140 | +173.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 376 | +0.140 | +173.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2319 | +0.155 | +1167.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2319 | +0.155 | +1167.43€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1618 | +0.108 | +588.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1618 | +0.108 | +588.62€ | 1 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 538 | +0.135 | +242.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 538 | +0.135 | +242.32€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 35012 | +0.182 | +27280.10€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 35012 | +0.182 | +27280.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5577 | +0.232 | +4977.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5577 | +0.232 | +4977.59€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5416 | +0.148 | +3561.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5416 | +0.148 | +3561.62€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5866 | +0.229 | +5150.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5866 | +0.229 | +5150.40€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5684 | +0.138 | +3980.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5684 | +0.138 | +3980.72€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6200 | +0.127 | +4333.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6200 | +0.127 | +4333.47€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6269 | +0.219 | +5276.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6269 | +0.219 | +5276.30€ | 0 | 20 |
| ✅ GBM_LATE_5M | 9659 | +0.184 | +6814.95€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 9659 | +0.184 | +6814.95€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 909 | +0.231 | +802.63€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 909 | +0.231 | +802.63€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2130 | +0.170 | +1543.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2130 | +0.170 | +1543.66€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 992 | +0.176 | +650.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 992 | +0.176 | +650.38€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 3000 | +0.187 | +2057.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3000 | +0.187 | +2057.37€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 1250 | +0.178 | +871.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1250 | +0.178 | +871.81€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1378 | +0.177 | +889.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1378 | +0.177 | +889.10€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2642 | +0.069 | +930.39€ | 0 | 11 |
| ✅ GBM_LATE_60M#60min | 2642 | +0.069 | +930.39€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 993 | +0.087 | +359.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 993 | +0.087 | +359.27€ | 0 | 11 |
| ✅ GBM_LATE_60M#ETH | 828 | +0.068 | +347.33€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 828 | +0.068 | +347.33€ | 0 | 9 |
| ✅ GBM_LATE_60M#SOL | 821 | +0.047 | +223.79€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 821 | +0.047 | +223.79€ | 2 | 13 |
| 🚫 GBM_LATE_60M_FADE | 492 | -0.241 | -16.92€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 492 | -0.241 | -16.92€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 186 | -0.234 | -12.15€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 186 | -0.234 | -12.15€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 172 | -0.218 | +1.41€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 172 | -0.218 | +1.41€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 134 | -0.272 | -6.17€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 134 | -0.272 | -6.17€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1182 | +0.087 | +307.20€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1182 | +0.087 | +307.20€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 450 | +0.080 | +93.35€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 450 | +0.080 | +93.35€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 415 | +0.064 | +70.79€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 415 | +0.064 | +70.79€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 317 | +0.127 | +143.06€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 317 | +0.127 | +143.06€ | 2 | 14 |
| ✅ LATE_WINDOW_5MIN | 138 | +0.250 | +117.05€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 138 | +0.250 | +117.05€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 138 | +0.250 | +117.05€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 138 | +0.250 | +117.05€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 2869 | +0.101 | +734.24€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2869 | +0.101 | +734.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2869 | +0.101 | +734.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2869 | +0.101 | +734.24€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 441 | -0.069 | -32.11€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 441 | -0.069 | -32.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 124 | -0.032 | -1.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 124 | -0.032 | -1.54€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 168 | -0.029 | -5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 168 | -0.029 | -5.75€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 3099 | +0.019 | +73.95€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3099 | +0.019 | +73.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 152 | +0.026 | -1.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 152 | +0.026 | -1.43€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 521 | +0.024 | +33.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 521 | +0.024 | +33.50€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1123 | +0.028 | +28.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1123 | +0.028 | +28.97€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 713 | +0.013 | +2.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 713 | +0.013 | +2.01€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 387 | +0.014 | +16.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 387 | +0.014 | +16.00€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1476 | -0.039 | -22.57€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1476 | -0.039 | -22.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 420 | -0.033 | -10.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 420 | -0.033 | -10.52€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 489 | -0.017 | +3.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 489 | -0.017 | +3.62€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 567 | -0.062 | -15.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 567 | -0.062 | -15.66€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 5577 | -0.021 | +80.52€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2624 | -0.026 | -2.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2953 | -0.015 | +83.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 162 | +0.000 | +9.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 77 | +0.044 | +12.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 85 | -0.040 | -2.60€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1387 | -0.012 | +26.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 654 | -0.018 | -2.25€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 733 | -0.006 | +29.05€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 621 | -0.026 | +5.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 310 | -0.042 | -8.44€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 311 | -0.011 | +14.40€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1150 | -0.039 | -35.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 526 | -0.057 | -41.32€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 624 | -0.024 | +5.43€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1089 | -0.011 | +42.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 521 | -0.011 | +25.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 568 | -0.012 | +16.18€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1168 | -0.021 | +31.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 536 | -0.022 | +11.18€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 632 | -0.019 | +20.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 40370 | -0.002 | +1943.94€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 40370 | -0.002 | +1943.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 7212 | +0.024 | +949.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 7212 | +0.024 | +949.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5972 | -0.032 | -95.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5972 | -0.032 | -95.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 7311 | +0.021 | +719.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 7311 | +0.021 | +719.11€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5798 | -0.049 | -151.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5798 | -0.049 | -151.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6812 | -0.007 | +210.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6812 | -0.007 | +210.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 7265 | +0.014 | +312.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 7265 | +0.014 | +312.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6248 | -0.059 | -142.76€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6248 | -0.059 | -142.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1220 | +0.001 | -13.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1220 | +0.001 | -13.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1545 | -0.075 | -29.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1545 | -0.075 | -29.69€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 50 | -0.077 | -3.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 50 | -0.077 | -3.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 732 | -0.123 | -33.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 732 | -0.123 | -33.18€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1845 | -0.078 | -37.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1845 | -0.078 | -37.52€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3355 | +0.004 | -3.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3355 | +0.004 | -3.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1320 | +0.005 | +5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1320 | +0.005 | +5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1389 | +0.007 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1389 | +0.007 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 101213 | -0.073 | +1694.61€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 101213 | -0.073 | +1694.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 17439 | -0.074 | +890.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 17439 | -0.074 | +890.71€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 15336 | -0.098 | -826.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 15336 | -0.098 | -826.29€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 17701 | -0.065 | +1037.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 17701 | -0.065 | +1037.25€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 14871 | -0.095 | -447.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 14871 | -0.095 | -447.18€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 18291 | -0.052 | +368.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 18291 | -0.052 | +368.39€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 17575 | -0.064 | +671.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 17575 | -0.064 | +671.73€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8143 | -0.032 | -155.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8143 | -0.032 | -155.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1933 | -0.043 | -19.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1933 | -0.043 | -19.40€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2246 | -0.026 | -32.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2246 | -0.026 | -32.47€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1132 | -0.051 | -25.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1132 | -0.051 | -25.82€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 828 | -0.022 | -25.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 828 | -0.022 | -25.46€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1432 | +0.121 | +562.23€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#5min | 1296 | +0.127 | +549.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 302 | +0.145 | +160.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 302 | +0.145 | +160.43€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 251 | +0.109 | +75.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 251 | +0.109 | +75.35€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 263 | +0.126 | +116.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 263 | +0.126 | +116.34€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 231 | +0.148 | +123.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 231 | +0.148 | +123.09€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 249 | +0.102 | +74.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 249 | +0.102 | +74.43€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1039 | -0.017 | -17.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1039 | -0.017 | -17.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 204 | -0.010 | +3.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 204 | -0.010 | +3.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 161 | -0.003 | +4.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 161 | -0.003 | +4.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 276 | -0.032 | -15.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 276 | -0.032 | -15.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 226 | +0.009 | +2.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 226 | +0.009 | +2.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 172 | -0.046 | -13.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 172 | -0.046 | -13.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 783 | -0.078 | -61.26€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 357 | -0.132 | -77.72€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 277 | -0.170 | -70.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 80 | +0.000 | -7.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 277 | -0.038 | +3.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 198 | -0.035 | +2.25€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 79 | -0.043 | +0.77€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 149 | -0.023 | +13.44€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 120 | -0.033 | +8.03€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 29 | +0.016 | +5.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 595 | -0.098 | -60.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 188 | -0.016 | -0.96€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 939 | -0.200 | -42.91€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 389 | -0.196 | -30.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 334 | -0.199 | -30.91€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 55 | -0.167 | +0.79€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 317 | -0.212 | -27.02€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 273 | -0.220 | -32.60€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 44 | -0.152 | +5.58€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 233 | -0.189 | +14.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 214 | -0.185 | +11.09€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 821 | -0.203 | -52.42€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 118 | -0.175 | +9.51€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 396 | +0.397 | +364.69€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 46 | +0.104 | +40.61€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 46 | +0.104 | +40.61€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 101 | +0.374 | +91.49€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 101 | +0.374 | +91.49€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 249 | +0.456 | +232.60€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 249 | +0.456 | +232.60€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 396 | +0.397 | +364.69€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 638 | +0.031 | +26.40€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 638 | +0.031 | +26.40€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 49 | +0.010 | -2.27€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 49 | +0.010 | -2.27€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 66 | -0.015 | -2.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 66 | -0.015 | -2.23€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 227 | +0.059 | +27.47€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 227 | +0.059 | +27.47€ | 2 | 5 |
| ✅ STREAK_FADE_5M | 3255 | -0.021 | -127.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3255 | -0.021 | -127.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1027 | -0.024 | -38.28€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1027 | -0.024 | -38.28€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 585 | -0.026 | -25.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 585 | -0.026 | -25.65€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1487 | -0.015 | -48.83€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1487 | -0.015 | -48.83€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 93 | -0.047 | -8.86€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 93 | -0.047 | -8.86€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 39 | -0.085 | -3.98€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 39 | -0.085 | -3.98€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 54 | -0.018 | -4.88€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 54 | -0.018 | -4.88€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 9929 | +0.019 | +105.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9929 | +0.019 | +105.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2641 | +0.021 | +28.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2641 | +0.021 | +28.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2418 | +0.026 | +47.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2418 | +0.026 | +47.79€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2863 | +0.009 | -1.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2863 | +0.009 | -1.83€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2007 | +0.021 | +31.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2007 | +0.021 | +31.08€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8979 | +0.013 | -45.59€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8979 | +0.013 | -45.59€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3543 | +0.018 | -4.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3543 | +0.018 | -4.09€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3519 | +0.011 | -25.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3519 | +0.011 | -25.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1917 | +0.007 | -15.71€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1917 | +0.007 | -15.71€ | 1 | 0 |
| ✅ UPDOWN_GBM | 62409 | +0.049 | +5152.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 15557 | +0.084 | +3436.79€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2075 | +0.005 | +9.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 41003 | +0.043 | +1648.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3559 | +0.007 | +60.13€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6470 | +0.085 | +936.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1374 | +0.158 | +602.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 72 | -0.013 | -1.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5024 | +0.066 | +336.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 12132 | +0.052 | +996.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1958 | +0.091 | +468.34€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 534 | +0.011 | +5.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 7952 | +0.055 | +477.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1609 | +0.005 | +43.14€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 79 | -0.080 | +1.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 7605 | +0.063 | +736.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1362 | +0.147 | +526.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 69 | +0.007 | -2.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6174 | +0.045 | +212.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 13590 | +0.039 | +773.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3659 | +0.057 | +463.58€ | 1 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 527 | +0.007 | +8.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 8120 | +0.039 | +297.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1213 | +0.004 | +0.98€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 71 | -0.103 | +3.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 13754 | +0.027 | +578.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3669 | +0.038 | +347.08€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 516 | +0.000 | +0.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 8769 | +0.026 | +221.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 737 | +0.016 | +16.01€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#daily | 63 | -0.146 | -5.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 8856 | +0.058 | +1130.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3535 | +0.104 | +1029.09€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 357 | +0.007 | -1.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4964 | +0.028 | +103.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 213 | -0.109 | -0.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 721 | +0.360 | +251.67€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 721 | +0.360 | +251.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 388 | +0.359 | +127.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 388 | +0.359 | +127.73€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 333 | +0.360 | +123.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 333 | +0.360 | +123.94€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 17027 | -0.024 | +4141.61€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 17027 | -0.024 | +4141.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1482 | -0.052 | +487.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1482 | -0.052 | +487.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2929 | -0.111 | +148.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2929 | -0.111 | +148.48€ | 5 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 842 | +0.218 | +692.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 842 | +0.218 | +692.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1978 | +0.213 | +1251.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1978 | +0.213 | +1251.29€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4871 | -0.063 | +651.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4871 | -0.063 | +651.80€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4925 | -0.063 | +910.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4925 | -0.063 | +910.06€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 187 | +0.034 | +6.83€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 187 | +0.034 | +6.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 187 | +0.034 | +6.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 187 | +0.034 | +6.83€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1192 | +0.288 | +976.52€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1192 | +0.288 | +976.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 648 | +0.286 | +511.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 648 | +0.286 | +511.22€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 544 | +0.289 | +465.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 544 | +0.289 | +465.30€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 768 | -0.114 | -84.12€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 768 | -0.114 | -84.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 226 | -0.088 | -18.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 226 | -0.088 | -18.31€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 80 | -0.159 | -7.73€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 80 | -0.159 | -7.73€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 83 | -0.194 | -8.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 83 | -0.194 | -8.02€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 3058 | +0.306 | +1505.31€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1094 | +0.259 | +157.21€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1169 | +0.299 | +524.07€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 795 | +0.378 | +824.02€ | 0 | 1 |