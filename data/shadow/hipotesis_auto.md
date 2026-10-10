# Hipótesis automáticas — 2026-10-10 13:49 UTC
_Generado por shadow_postmortem.py sobre 837845 resoluciones (PNL=+104780.03€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.233 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.196 (n=235)

  - _Acción_: Kelly boost +0.98€ cuando `n_total_lado` > 69.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.617` → IC=+0.242 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.617 (IC base=+0.123)

- **PATRÓN** `banda_z` > `9.03` → IC=+0.192 (n=235)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 9.03 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=748)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.123)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.229 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.128)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.206 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.128)

- **PATRÓN** `banda_hit_calibrado` > `0.614` → IC=+0.232 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.614 (IC base=+0.128)

- **PATRÓN** `banda_z` > `9.581` → IC=+0.189 (n=191)

  - _Acción_: Kelly boost +0.95€ cuando `banda_z` > 9.581 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=650)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.128)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
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
- **FILTRO** `restante_s_al_confirmar` < `144.02` → IC=-0.207 (n=9003)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.02
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=27009)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.93` → IC=-0.266 (n=1105)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.93
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3317)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `123.26` → IC=-0.302 (n=1026)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 123.26
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3081)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `165.33` → IC=-0.228 (n=2312)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 165.33
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6939)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.56` → IC=-0.300 (n=1757)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.56
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=5271)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.207 (n=18876)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=4027)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `9485.1977` → IC=+0.183 (n=1797)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9485.1977 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.134 (n=15599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=19097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=14494)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=6641)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7453.3789` → IC=+0.164 (n=2553)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 7453.3789 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1932)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=1890)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2374)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `16120.1033` → IC=+0.211 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16120.1033 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.198 (n=1707)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.196 (n=1906)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=2438)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `16044.722` → IC=+0.207 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16044.722 (IC base=+0.191)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.164 (n=420)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.61 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `6984.5162` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 6984.5162 (IC base=+0.087)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.124 (n=472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.087)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.138 (n=998)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `5830.4537` → IC=+0.128 (n=237)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 5830.4537 (IC base=+0.087)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.366 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.240 (n=595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.362 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.224 (n=1906)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=914)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.142 (n=784)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.255 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=715)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2151.7929` → IC=+0.152 (n=397)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2151.7929 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=870)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.410 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=1251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=662)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.289 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=826)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.176 (n=334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.368 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3371.7925` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3371.7925 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.223 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=15669)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=13333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.230 (n=6595)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=3672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=3475)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3539)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.175)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.228 (n=1649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.227 (n=1648)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.317 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=3599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=3444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.181 (n=3680)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=2850)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=3143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.347 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.242)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=3521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=2264)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.190 (n=2689)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.71 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=1245)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.427 (n=619)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `2839.9084` → IC=+0.433 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2839.9084 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.432 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.446 (n=184)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `18111.1478` → IC=+0.436 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 18111.1478 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.442 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `3434.6605` → IC=+0.444 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3434.6605 (IC base=+0.429)

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

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=20075)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=20519)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.187 (n=8041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=6476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=8956)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.184)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.225 (n=4125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.284 (n=2971)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.181 (n=8492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=6462)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=8565)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=4216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=2910)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.204 (n=7756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.202 (n=6219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=3042)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=3342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=3540)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=7220)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.125 (n=6669)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.2 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=7034)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=8859)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.45` → IC=+0.138 (n=6652)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.45 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=3577)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.126 (n=3303)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=3542)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.95 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=4388)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `2.99` → IC=+0.147 (n=3302)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.99 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=3643)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.132 (n=3851)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.135 (n=3348)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.303 (n=1464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.293 (n=1445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `4253.2686` → IC=+0.305 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4253.2686 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.294 (n=655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.343 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `5371.2351` → IC=+0.309 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5371.2351 (IC base=+0.283)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.322 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.295 (n=696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.290)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `1450.7635` → IC=+0.306 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1450.7635 (IC base=+0.290)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=307)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.449 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `5265.735` → IC=+0.442 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5265.735 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.463 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.451 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.444)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.445 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.444)

- **PATRÓN** `libro_liquidez` > `2131.4162` → IC=+0.460 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2131.4162 (IC base=+0.444)

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
- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=55)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.237 (n=55)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=46)

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
- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=55)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.237 (n=55)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=46)

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
- **PATRÓN** `drift_60min` |x|≤ `0.3679` → IC=+0.136 (n=9872)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.3679 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.9835` → IC=+0.244 (n=3740)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9835 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.2149` → IC=+0.254 (n=2592)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2149 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.023` → IC=+0.186 (n=4245)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 6.023 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.8528` → IC=+0.251 (n=2102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8528 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `0.617` → IC=+0.255 (n=3153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.617 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.231 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.3284` → IC=+0.222 (n=3576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3284 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.141 (n=13734)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5652 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.5687` → IC=+0.203 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5687 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.147` → IC=+0.185 (n=4777)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.147 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `1.1873` → IC=+0.183 (n=5131)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.1873 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.0526` → IC=+0.181 (n=2326)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0526 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.227 (n=1289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.4488` → IC=+0.203 (n=8793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4488 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.217 (n=8610)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.073)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.219 (n=830)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.201 (n=830)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.2801` → IC=+0.188 (n=2191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.2801 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.199 (n=1204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.189 (n=1671)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.237` → IC=+0.290 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.237 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.240 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.186 (n=2361)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=2596)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.235 (n=2031)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.241 (n=1817)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.088` → IC=+0.264 (n=677)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.088 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0036` → IC=+0.282 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0036 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.444` → IC=+0.243 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.444 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.342` → IC=+0.236 (n=2128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.342 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` < `0.0942` → IC=+0.234 (n=1795)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0942 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.252 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.6252` → IC=+0.250 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6252 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=2236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.234 (n=883)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1067` → IC=+0.257 (n=879)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1067 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.234 (n=2000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.220 (n=2041)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.9721` → IC=+0.264 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9721 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.1324` → IC=+0.223 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1324 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.479` → IC=+0.259 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.479 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2468` → IC=+0.222 (n=1998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2468 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.224 (n=1998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.246 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.7638` → IC=+0.222 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7638 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.4223` → IC=+0.247 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4223 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.188 (n=671)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0749` → IC=+0.178 (n=665)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0749 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.7248` → IC=+0.179 (n=1995)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.7248 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1299` → IC=+0.159 (n=1827)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1299 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.204` → IC=+0.155 (n=320)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.204 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.301` → IC=+0.144 (n=1829)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.301 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1838` → IC=+0.148 (n=1995)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1838 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.158` → IC=+0.165 (n=538)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.158 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4481` → IC=+0.149 (n=1879)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4481 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4156` → IC=+0.144 (n=1879)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4156 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `226.0` → IC=+0.174 (n=793)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 226.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.201 (n=2532)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=2666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=2274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.388` → IC=+0.264 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.388 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.196 (n=2231)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.3472` → IC=+0.196 (n=333)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.3472 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.1507` → IC=+0.203 (n=1629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1507 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=3023)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.227 (n=1501)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.1781` → IC=+0.227 (n=989)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1781 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=842)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=1046)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.0667` → IC=+0.237 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0667 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.641` → IC=+0.256 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.641 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3448` → IC=+0.254 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3448 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.7192` → IC=+0.215 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7192 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.7146` → IC=+0.228 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7146 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.215 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.216 (n=2054)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.214)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.138 (n=136)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=3016)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.152 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0036 (IC base=+0.046)

- **PATRÓN** `ibs_20min` > `0.9588` → IC=+0.226 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9588 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.022` → IC=+0.180 (n=991)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.022 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8538` → IC=+0.331 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8538 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `1.2251` → IC=+0.350 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2251 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1815` → IC=+0.323 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1815 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.343 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.358 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` > `2.21` → IC=+0.327 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.21 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.327 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.0982` → IC=+0.170 (n=789)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.0982 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.4593` → IC=+0.201 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4593 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.154 (n=862)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8504 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2284` → IC=+0.206 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2284 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `1.5239` → IC=+0.164 (n=1103)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.5239 (IC base=+0.034)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.171 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=465)

- **FILTRO** `ibs_20min` > `0.2245` → IC=-0.129 (n=3051)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2245
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=1503)

- **FILTRO** `sigma_ewma_delta_pct` > `8.719` → IC=-0.222 (n=466)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.719
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=4088)

- **PATRÓN** `ibs_20min` > `0.8077` → IC=+0.192 (n=186)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.8077 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `1.6532` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6532 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.383` → IC=+0.130 (n=190)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 2.383 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.8709` → IC=+0.263 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8709 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `1.0006` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0006 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.0757` → IC=+0.280 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0757 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.282 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.266 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.2245` → IC=+0.141 (n=1503)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.2245 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.1828` → IC=+0.275 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1828 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.704` → IC=+0.284 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.704 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.0805` → IC=+0.293 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0805 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.3699` → IC=+0.294 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3699 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6369` → IC=-0.181 (n=794)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6369
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2386)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.206 (n=939)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2241)

- **FILTRO** `ibs_20min` > `0.76` → IC=-0.207 (n=1184)

  - _Acción_: SKIP cuando `ibs_20min` > 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=3557)

- **PATRÓN** `dist_vwap_pct` > `0.4585` → IC=+0.313 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4585 (IC base=-0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2747` → IC=+0.310 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2747 (IC base=-0.074)

- **PATRÓN** `volumen_regimen` < `0.9898` → IC=+0.298 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9898 (IC base=-0.074)

- **PATRÓN** `volumen_regimen` > `0.6389` → IC=+0.311 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6389 (IC base=-0.074)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.300 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=-0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.305 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.074)

- **PATRÓN** `volumen_spike_ratio` < `2.4745` → IC=+0.300 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4745 (IC base=-0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.1732` → IC=+0.304 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1732 (IC base=-0.074)

- **PATRÓN** `dist_vwap_pct` > `0.8089` → IC=+0.290 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8089 (IC base=-0.011)

- **PATRÓN** `volumen_regimen` > `1.0773` → IC=+0.274 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0773 (IC base=-0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.1027` → IC=+0.276 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1027 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` < `2.1721` → IC=+0.256 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1721 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` > `1.4298` → IC=+0.260 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4298 (IC base=-0.011)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.202 (n=4950)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4648` → IC=+0.187 (n=13235)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4648 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.9315` → IC=+0.285 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9315 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.685` → IC=+0.155 (n=6664)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.685 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.1724` → IC=+0.251 (n=5422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1724 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6901` → IC=+0.258 (n=4844)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6901 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2404` → IC=+0.263 (n=1633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2404 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4639` → IC=+0.248 (n=2915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4639 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6323` → IC=+0.260 (n=2915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6323 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.282 (n=8290)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.162 (n=4773)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0089 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.54` → IC=+0.159 (n=12579)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.54 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.7061` → IC=+0.253 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7061 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1947` → IC=+0.261 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1947 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.310 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5864` → IC=+0.281 (n=2708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5864 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.274` → IC=+0.273 (n=2788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.274 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.285 (n=6059)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2594` → IC=-0.172 (n=1031)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2594
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=3095)

- **FILTRO** `ibs_20min` > `0.7564` → IC=-0.187 (n=852)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7564
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2559)

- **FILTRO** `sigma_ewma_delta_pct` > `4.599` → IC=-0.186 (n=753)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.599
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2658)

- **PATRÓN** `ibs_20min` > `0.9137` → IC=+0.283 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9137 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.28` → IC=+0.204 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.28 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.286 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `1.4426` → IC=+0.224 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4426 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `2.2222` → IC=+0.248 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2222 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.244 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.1596` → IC=+0.149 (n=853)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.1596 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.0751` → IC=+0.420 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0751 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.5496` → IC=+0.408 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5496 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` > `1.5399` → IC=+0.407 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5399 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.410 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8601` → IC=+0.145 (n=1001)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.8601 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1149` → IC=+0.194 (n=743)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1149 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.6783` → IC=+0.183 (n=1269)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6783 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.217 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.201 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.4378` → IC=+0.197 (n=466)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.4378 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `225.0` → IC=+0.233 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 225.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.1491` → IC=+0.231 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1491 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.6194` → IC=+0.235 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6194 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0734` → IC=+0.227 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0734 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2715` → IC=+0.302 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2715 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5482` → IC=+0.232 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5482 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1744` → IC=+0.245 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1744 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.276 (n=2221)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.261 (n=2228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.257 (n=1482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.288 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.269 (n=1917)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.1663` → IC=+0.265 (n=1421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1663 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.267 (n=2626)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.302 (n=1874)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1807` → IC=+0.305 (n=823)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1807 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.3647` → IC=+0.291 (n=1869)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3647 (IC base=+0.287)

- **PATRÓN** `ibs_20min` > `0.1034` → IC=+0.288 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1034 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.761` → IC=+0.305 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.761 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.1935` → IC=+0.285 (n=1819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1935 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.3365` → IC=+0.300 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3365 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.7149` → IC=+0.303 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7149 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.6261` → IC=+0.291 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6261 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.288 (n=1522)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.287)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7583` → IC=-0.181 (n=864)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7583
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=2596)

- **PATRÓN** `ibs_20min` > `0.8975` → IC=+0.163 (n=801)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.8975 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` < `1.0113` → IC=+0.235 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0113 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.1683` → IC=+0.228 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1683 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.081` → IC=+0.231 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.081 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4112` → IC=+0.254 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4112 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` > `2.4784` → IC=+0.225 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4784 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.298 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.1219` → IC=+0.223 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1219 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` < `1.0403` → IC=+0.233 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0403 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.285 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.8569` → IC=+0.263 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8569 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.5231` → IC=+0.244 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5231 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.253 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7645` → IC=-0.194 (n=1575)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7645
  - _Potencial_: sin este filtro IC_bueno=+0.292 (n=1575)

- **FILTRO** `ibs_20min` > `0.6667` → IC=-0.248 (n=761)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=2394)

- **FILTRO** `sigma_ewma_delta_pct` > `8.635` → IC=-0.229 (n=360)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.635
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=2795)

- **PATRÓN** `ibs_20min` > `0.7645` → IC=+0.292 (n=1575)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7645 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `1.018` → IC=+0.337 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.018 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.668` → IC=+0.169 (n=491)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.668 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8524` → IC=+0.319 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8524 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.6354` → IC=+0.310 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6354 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.307 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.339 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.329 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.334 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.5588` → IC=+0.135 (n=2083)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5588 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.2712` → IC=+0.239 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2712 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.263 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.235 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.0707` → IC=+0.251 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0707 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4125` → IC=+0.251 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4125 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.266 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.025)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.337 (n=1551)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.309 (n=822)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.326 (n=1740)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2135` → IC=+0.321 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2135 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.778` → IC=+0.315 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.778 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.953` → IC=+0.294 (n=1969)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.953 (IC base=+0.293)

- **PATRÓN** `volumen_regimen` > `0.6266` → IC=+0.304 (n=1737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6266 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.343 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.305 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `2996.8018` → IC=+0.318 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2996.8018 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.329 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.293)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.324 (n=1225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.1858` → IC=+0.293 (n=809)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1858 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.301 (n=918)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` < `0.3696` → IC=+0.319 (n=1838)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3696 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.3081` → IC=+0.295 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3081 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.516` → IC=+0.302 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.516 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.036` → IC=+0.293 (n=2195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.036 (IC base=+0.292)

- **PATRÓN** `volumen_regimen` < `0.8891` → IC=+0.293 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8891 (IC base=+0.292)

- **PATRÓN** `volumen_regimen` > `1.2246` → IC=+0.321 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2246 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.343 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` < `2.4652` → IC=+0.292 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4652 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `2.1375` → IC=+0.293 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1375 (IC base=+0.292)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.186 (n=3643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0047 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.215 (n=3644)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3481` → IC=+0.188 (n=9610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3481 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=11382)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.5636` → IC=+0.230 (n=10918)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5636 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1674` → IC=+0.202 (n=4555)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1674 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.446` → IC=+0.253 (n=2186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.446 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1981` → IC=+0.169 (n=7249)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.1981 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.163 (n=7249)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6279 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.197 (n=1610)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.4508` → IC=+0.177 (n=3517)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4508 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.5936` → IC=+0.184 (n=3517)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5936 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2535.4382` → IC=+0.179 (n=7279)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2535.4382 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.193 (n=9836)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 102.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.189 (n=6996)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0066 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.0806` → IC=+0.223 (n=3494)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0806 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=3917)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.49` → IC=+0.232 (n=10477)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.49 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.239` → IC=+0.196 (n=1733)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.239 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.18` → IC=+0.166 (n=7495)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.18 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.221 (n=1534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6087` → IC=+0.180 (n=3252)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.6087 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.186 (n=9438)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 105.0 (IC base=+0.177)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.234 (n=612)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.219 (n=613)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.3361` → IC=+0.223 (n=1836)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3361 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1939)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.208 (n=1235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.918` → IC=+0.287 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.918 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.282` → IC=+0.331 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.282 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.262 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.8166` → IC=+0.196 (n=1151)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.8166 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.202 (n=1725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=1928)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.250 (n=1241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.246 (n=1260)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1009` → IC=+0.295 (n=622)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1009 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.242 (n=1271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3547` → IC=+0.256 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3547 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.165` → IC=+0.244 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.165 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.238 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.279 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4266` → IC=+0.248 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4266 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.6401` → IC=+0.243 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6401 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.212 (n=725)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1629` → IC=+0.187 (n=1095)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1629 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.177 (n=1641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.3742` → IC=+0.224 (n=1641)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3742 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.1973` → IC=+0.211 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1973 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.228 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.167 (n=724)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6892 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.187 (n=260)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.413` → IC=+0.180 (n=535)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.413 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.4812` → IC=+0.160 (n=534)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4812 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `232.0` → IC=+0.171 (n=688)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 232.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.165 (n=1732)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2299` → IC=+0.176 (n=1522)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2299 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6031` → IC=+0.202 (n=1729)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6031 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.719` → IC=+0.209 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.719 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.1987` → IC=+0.165 (n=1729)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1987 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.2281` → IC=+0.147 (n=1787)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.2281 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4807` → IC=+0.153 (n=1612)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4807 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7663` → IC=+0.144 (n=1075)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7663 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `206.0` → IC=+0.171 (n=512)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 206.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.233 (n=612)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.405` → IC=+0.220 (n=1614)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.405 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1912)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.555` → IC=+0.288 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.555 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.208 (n=1560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.1297` → IC=+0.210 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1297 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.7659` → IC=+0.211 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7659 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.6745` → IC=+0.216 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6745 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=2184)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.249 (n=1048)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.5666` → IC=+0.241 (n=1570)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5666 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.275 (n=603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` < `0.3509` → IC=+0.250 (n=1570)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3509 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.634` → IC=+0.260 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.634 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.263 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.7153` → IC=+0.243 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7153 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.7146` → IC=+0.234 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7146 (IC base=+0.228)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.228 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.228)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.181 (n=1546)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0063 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0762` → IC=+0.202 (n=585)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0762 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=1827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.3254` → IC=+0.207 (n=1754)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3254 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1366` → IC=+0.187 (n=1099)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1366 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.995` → IC=+0.205 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.995 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8559` → IC=+0.160 (n=1170)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8559 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.173 (n=728)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4335` → IC=+0.163 (n=573)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4335 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.516` → IC=+0.163 (n=573)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.516 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5117.2517` → IC=+0.199 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5117.2517 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.154 (n=1696)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 148.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.163 (n=1622)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0061 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3831` → IC=+0.150 (n=1843)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3831 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6715` → IC=+0.188 (n=1843)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6715 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.834` → IC=+0.158 (n=641)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.834 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8557` → IC=+0.165 (n=1229)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8557 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.188 (n=280)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.81` → IC=+0.136 (n=1142)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.81 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.133 (n=1713)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.42 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `4545.4038` → IC=+0.170 (n=1229)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4545.4038 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.130 (n=1656)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 146.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.165 (n=906)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0099 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4366` → IC=+0.132 (n=1755)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.4366 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=2037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.217 (n=1997)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.1953` → IC=+0.188 (n=1189)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1953 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.874` → IC=+0.264 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.874 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.1894` → IC=+0.145 (n=1995)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1894 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.1617` → IC=+0.138 (n=2018)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.1617 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.5446` → IC=+0.147 (n=850)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.5446 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=2083)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2908.3422` → IC=+0.211 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2908.3422 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.166 (n=614)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 21.0 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.161 (n=889)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0061 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1064` → IC=+0.171 (n=673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1064 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=2041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5789` → IC=+0.217 (n=2020)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5789 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.295` → IC=+0.128 (n=608)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 5.295 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.132 (n=2019)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1756 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.158 (n=258)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4487` → IC=+0.137 (n=621)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4487 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4234` → IC=+0.126 (n=621)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4234 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2173.4569` → IC=+0.171 (n=1346)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2173.4569 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.130 (n=1817)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 51.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.236 (n=1861)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.1766` → IC=+0.228 (n=819)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1766 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=1933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.219 (n=1259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.252 (n=1866)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.1938` → IC=+0.218 (n=1234)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1938 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.2785` → IC=+0.216 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2785 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.247 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.1817` → IC=+0.219 (n=1861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1817 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.6199` → IC=+0.221 (n=1860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6199 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.272 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `2.4668` → IC=+0.219 (n=1808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4668 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.8029` → IC=+0.228 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8029 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2674.5492` → IC=+0.226 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2674.5492 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.230 (n=838)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.012 (IC base=+0.221)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.225 (n=864)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.250 (n=635)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.240 (n=928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.02` → IC=+0.289 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.02 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `1.1534` → IC=+0.235 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1534 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.42` → IC=+0.247 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.42 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.6367` → IC=+0.231 (n=1905)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6367 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.284 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `2.1966` → IC=+0.214 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1966 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.4377` → IC=+0.223 (n=1757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4377 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2648.2226` → IC=+0.230 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2648.2226 (IC base=+0.221)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.197 (n=1258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0041 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3322` → IC=+0.181 (n=2503)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3322 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.205 (n=1410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.3288` → IC=+0.198 (n=2843)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3288 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.7717` → IC=+0.184 (n=431)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.7717 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.726` → IC=+0.195 (n=1215)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.726 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.189 (n=1709)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8646 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.173 (n=2290)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6949 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1018` → IC=+0.182 (n=1022)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1018 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.190 (n=921)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.5135` → IC=+0.176 (n=921)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.5135 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=2637)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `4142.643` → IC=+0.171 (n=1895)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4142.643 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.186 (n=2622)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 151.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.158 (n=976)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0036 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=2757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.0789` → IC=+0.197 (n=973)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.0789 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.124 (n=1170)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.6986 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.0748` → IC=+0.123 (n=1113)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0748 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.433` → IC=+0.143 (n=945)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.433 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `4923.9421` → IC=+0.138 (n=1945)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 4923.9421 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.134 (n=954)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 21.0 (IC base=+0.111)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.204 (n=363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1004` → IC=+0.209 (n=362)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1004 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.188 (n=754)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.6334` → IC=+0.209 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6334 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.3086` → IC=+0.183 (n=257)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.3086 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.092` → IC=+0.178 (n=349)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 3.092 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.878` → IC=+0.182 (n=549)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.878 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.164 (n=319)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.2117` → IC=+0.166 (n=708)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.2117 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.4164` → IC=+0.156 (n=804)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.4164 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `14731.9311` → IC=+0.167 (n=548)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 14731.9311 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.205 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.203 (n=321)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2654` → IC=+0.159 (n=839)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2654 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.152 (n=860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6152` → IC=+0.180 (n=839)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6152 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.162` → IC=+0.148 (n=867)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.162 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2002` → IC=+0.145 (n=954)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2002 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6986` → IC=+0.157 (n=852)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6986 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.191 (n=254)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.1142` → IC=+0.158 (n=829)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1142 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=1236)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `290.0` → IC=+0.156 (n=812)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 290.0 (IC base=+0.144)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.239 (n=604)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.2022` → IC=+0.220 (n=601)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2022 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.6714` → IC=+0.258 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6714 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3573` → IC=+0.207 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3573 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.2068` → IC=+0.208 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2068 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.951` → IC=+0.220 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.951 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `0.836` → IC=+0.208 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.836 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `1.1822` → IC=+0.220 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1822 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.16` → IC=+0.230 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.16 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.4142` → IC=+0.239 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4142 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.4481` → IC=+0.219 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4481 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.155 (n=384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.128 (n=600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 11.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.0884` → IC=+0.168 (n=290)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.0884 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `0.6877` → IC=+0.147 (n=383)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6877 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `4077.438` → IC=+0.130 (n=777)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 4077.438 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.129 (n=370)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.158 (n=434)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0073 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.163 (n=648)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0052 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.186 (n=580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.939` → IC=+0.225 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.939 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.207 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.0652` → IC=+0.174 (n=571)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.0652 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.6526` → IC=+0.160 (n=648)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6526 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1655` → IC=+0.176 (n=183)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1655 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4599` → IC=+0.159 (n=209)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4599 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.1893` → IC=+0.171 (n=284)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1893 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=683)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `3103.1049` → IC=+0.188 (n=216)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3103.1049 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.4667` → IC=+0.150 (n=550)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.4667 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` < `1.5684` → IC=+0.126 (n=263)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5684 (IC base=+0.061)

- **PATRÓN** `libro_liquidez` > `2433.7064` → IC=+0.129 (n=416)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2433.7064 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.134 (n=380)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 22.0 (IC base=+0.061)

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
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.179 (n=4736)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.217 (n=4735)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=14843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.4542` → IC=+0.227 (n=14194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4542 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1629` → IC=+0.188 (n=5180)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1629 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.406` → IC=+0.250 (n=3482)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.406 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.8781` → IC=+0.175 (n=6341)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8781 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2891` → IC=+0.202 (n=1917)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2891 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.595` → IC=+0.198 (n=4587)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.595 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2506.7192` → IC=+0.184 (n=9463)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2506.7192 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.206 (n=11285)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.197 (n=5636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0053 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.1458` → IC=+0.197 (n=5636)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1458 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=4782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.4561` → IC=+0.250 (n=11273)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4561 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.048` → IC=+0.210 (n=1792)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.048 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.71` → IC=+0.188 (n=12363)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.71 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.165 (n=3808)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7051 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.249 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.6081` → IC=+0.196 (n=4007)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6081 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.210 (n=7786)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.248 (n=785)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.244 (n=782)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3513` → IC=+0.216 (n=2346)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3513 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=1132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.216 (n=1581)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.325 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.74` → IC=+0.349 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.74 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2731` → IC=+0.270 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2731 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.5769` → IC=+0.228 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5769 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2429)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.227 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.261 (n=1960)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.261 (n=1960)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.2039` → IC=+0.271 (n=1308)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2039 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.264 (n=1779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.4871` → IC=+0.283 (n=1960)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4871 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.444` → IC=+0.262 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.444 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.2845` → IC=+0.286 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2845 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.6332` → IC=+0.278 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6332 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=2163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.257)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.199 (n=762)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1769` → IC=+0.167 (n=1522)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1769 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2728` → IC=+0.207 (n=2283)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2728 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1279` → IC=+0.188 (n=1239)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1279 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.71` → IC=+0.168 (n=383)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.71 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.186` → IC=+0.154 (n=2089)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.186 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6276` → IC=+0.176 (n=761)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6276 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.188 (n=325)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1529` → IC=+0.158 (n=1957)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1529 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5264` → IC=+0.154 (n=1988)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5264 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `272.0` → IC=+0.182 (n=957)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 272.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.197 (n=632)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0026 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.078` → IC=+0.189 (n=631)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.078 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.692` → IC=+0.198 (n=1892)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.692 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.170 (n=1745)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.479` → IC=+0.164 (n=319)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.479 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.1813` → IC=+0.160 (n=1891)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1813 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1533` → IC=+0.194 (n=505)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1533 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.432` → IC=+0.155 (n=1789)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.432 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7778` → IC=+0.163 (n=1192)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.7778 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `255.0` → IC=+0.146 (n=569)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 255.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.232 (n=2341)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=2456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.307 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.507` → IC=+0.310 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.507 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` < `0.1327` → IC=+0.226 (n=2164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1327 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.6911` → IC=+0.239 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6911 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=2788)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.244 (n=1465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.237 (n=1963)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1813` → IC=+0.255 (n=966)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1813 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=828)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=1027)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0182` → IC=+0.302 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0182 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.137` → IC=+0.288 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.137 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3399` → IC=+0.302 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3399 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.708` → IC=+0.241 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.708 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.1247` → IC=+0.245 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1247 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.240 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.258 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.237)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.198 (n=1068)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1269` → IC=+0.164 (n=1068)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1269 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=2532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.2655` → IC=+0.192 (n=2426)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2655 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.5408` → IC=+0.164 (n=614)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.5408 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.201` → IC=+0.159 (n=989)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.201 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.163 (n=1619)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8725 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1662` → IC=+0.174 (n=633)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1662 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.5279` → IC=+0.165 (n=1040)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5279 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.1817` → IC=+0.155 (n=1071)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1817 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `7308.1777` → IC=+0.240 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7308.1777 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.180 (n=782)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 69.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.196 (n=656)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0032 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.3419` → IC=+0.146 (n=1729)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3419 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=716)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.7364` → IC=+0.189 (n=1965)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.7364 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.238` → IC=+0.181 (n=299)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 11.238 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6234` → IC=+0.153 (n=655)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6234 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.230 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.2449` → IC=+0.138 (n=1658)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.2449 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.441` → IC=+0.146 (n=1884)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.441 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `5477.3482` → IC=+0.202 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5477.3482 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.136 (n=1893)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 163.0 (IC base=+0.134)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.144 (n=1634)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0079 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.45` → IC=+0.202 (n=2449)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.45 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `1.0168` → IC=+0.212 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0168 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.016` → IC=+0.259 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.016 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.2251` → IC=+0.140 (n=2449)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2251 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1612` → IC=+0.131 (n=2534)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1612 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.132 (n=324)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.8368` → IC=+0.127 (n=1591)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8368 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.1877` → IC=+0.136 (n=1082)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.1877 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2501)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2933.8625` → IC=+0.256 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2933.8625 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.150 (n=755)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 26.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.171 (n=1027)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0063 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1316` → IC=+0.163 (n=779)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1316 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.158 (n=1091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6327` → IC=+0.213 (n=2334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6327 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.2143` → IC=+0.138 (n=1977)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2143 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.43` → IC=+0.134 (n=2252)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.43 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.154 (n=1029)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7144 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2224` → IC=+0.174 (n=384)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2224 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4342` → IC=+0.158 (n=722)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4342 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2811.6854` → IC=+0.208 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2811.6854 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.139 (n=1895)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 49.0 (IC base=+0.121)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.240 (n=2353)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=2460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.228 (n=1702)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.6038` → IC=+0.269 (n=2103)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6038 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.2033` → IC=+0.237 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2033 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.791` → IC=+0.267 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.791 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.2317` → IC=+0.228 (n=2353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2317 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.225 (n=2352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6398 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.247 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.5113` → IC=+0.248 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5113 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=2103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2997.2954` → IC=+0.240 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2997.2954 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.223 (n=822)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.236 (n=1119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.228 (n=2312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.5094` → IC=+0.261 (n=2466)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5094 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.971` → IC=+0.258 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.971 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.2299` → IC=+0.248 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2299 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.289 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.4345` → IC=+0.223 (n=2273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4345 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2668.4592` → IC=+0.220 (n=1644)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2668.4592 (IC base=+0.220)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=4216)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.233 (n=1438)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.4948` → IC=+0.204 (n=4297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4948 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=1574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=2956)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.9409` → IC=+0.244 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9409 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.1684` → IC=+0.196 (n=1594)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1684 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.239` → IC=+0.196 (n=2642)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.239 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.2` → IC=+0.212 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.2 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.205 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` > `0.8864` → IC=+0.197 (n=2034)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.8864 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.1679` → IC=+0.218 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1679 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `1.4558` → IC=+0.201 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4558 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.6115` → IC=+0.201 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6115 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=3237)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `3869.425` → IC=+0.207 (n=2865)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3869.425 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.227 (n=1058)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.4837` → IC=+0.194 (n=3174)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4837 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=1087)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=1447)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.18` → IC=+0.197 (n=1398)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.18 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.6412` → IC=+0.185 (n=547)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6412 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.182` → IC=+0.182 (n=3175)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 6.182 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2488` → IC=+0.182 (n=2981)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.2488 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.180 (n=2894)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.181 (n=1445)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `2.538` → IC=+0.179 (n=3129)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.538 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `1.8147` → IC=+0.183 (n=2086)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.8147 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=4216)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.186 (n=1379)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 36.0 (IC base=+0.176)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.247 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0811` → IC=+0.270 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0811 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.228 (n=255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.5099` → IC=+0.244 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5099 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.761` → IC=+0.223 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.761 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.3158` → IC=+0.230 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3158 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.054` → IC=+0.239 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.054 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.566` → IC=+0.222 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.566 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.228 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.5968` → IC=+0.232 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5968 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.317 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.238 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `12574.1361` → IC=+0.248 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12574.1361 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.233 (n=484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.0835` → IC=+0.188 (n=366)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0835 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.187 (n=416)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.1561` → IC=+0.186 (n=482)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1561 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.6091` → IC=+0.159 (n=497)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.6091 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.6648` → IC=+0.191 (n=108)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6648 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.421` → IC=+0.171 (n=1077)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.421 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.8813` → IC=+0.193 (n=731)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8813 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.193 (n=229)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.5318` → IC=+0.161 (n=1092)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.5318 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.8136` → IC=+0.174 (n=728)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8136 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `11556.4503` → IC=+0.171 (n=1095)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 11556.4503 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.167 (n=1050)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 701.0 (IC base=+0.155)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.201 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.185 (n=316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0098 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.5794` → IC=+0.180 (n=696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.5794 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.235 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.51` → IC=+0.217 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.51 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.226 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `3.3854` → IC=+0.184 (n=232)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 3.3854 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.241 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.295 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.288 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.237)

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
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.212 (n=1125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.4577` → IC=+0.208 (n=1277)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4577 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5211` → IC=+0.214 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5211 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.8799` → IC=+0.206 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8799 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.174` → IC=+0.207 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.174 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.7064` → IC=+0.207 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7064 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2441` → IC=+0.208 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2441 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.202 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.1655` → IC=+0.211 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1655 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.424` → IC=+0.216 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.424 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.238 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.4878` → IC=+0.200 (n=1028)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4878 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.188 (n=402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 16.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.189 (n=699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 10.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.7599` → IC=+0.179 (n=1028)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7599 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.087` → IC=+0.178 (n=1028)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.087 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.6243` → IC=+0.194 (n=194)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6243 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.748` → IC=+0.179 (n=1052)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 6.748 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.2459` → IC=+0.188 (n=1028)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.2459 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.7214` → IC=+0.175 (n=918)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.7214 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.195 (n=434)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.183` → IC=+0.188 (n=886)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.183 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.7774` → IC=+0.178 (n=671)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.7774 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `7366.3592` → IC=+0.189 (n=1028)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7366.3592 (IC base=+0.174)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.223 (n=380)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.2945` → IC=+0.164 (n=379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2945 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.195 (n=532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 4.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.249 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.1887` → IC=+0.194 (n=344)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1887 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.474` → IC=+0.205 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.474 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.6985` → IC=+0.202 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6985 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` < `0.1075` → IC=+0.168 (n=507)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.1075 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1633` → IC=+0.198 (n=177)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1633 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.5566` → IC=+0.169 (n=243)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5566 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.5357` → IC=+0.220 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5357 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.174 (n=675)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3350.8386` → IC=+0.211 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3350.8386 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.182 (n=492)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 48.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.202 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.212 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.3638` → IC=+0.235 (n=277)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3638 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.222 (n=282)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.2034` → IC=+0.246 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2034 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.7663` → IC=+0.228 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7663 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.03` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.03 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.93` → IC=+0.194 (n=364)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 2.93 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.7555` → IC=+0.219 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7555 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.226 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.6214` → IC=+0.193 (n=177)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.6214 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.208 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `3309.2496` → IC=+0.205 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3309.2496 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.224 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.190)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.156 (n=615)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.075)

- **PATRÓN** `ibs_20min` > `0.4182` → IC=+0.148 (n=1304)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.4182 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.1388` → IC=+0.139 (n=688)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1388 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.45` → IC=+0.179 (n=294)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.45 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.161 (n=175)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.1849` → IC=+0.253 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1849 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.1229` → IC=+0.125 (n=620)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.1229 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.1468` → IC=+0.199 (n=154)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1468 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.4788` → IC=+0.143 (n=236)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4788 (IC base=+0.057)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.134 (n=476)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0056 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.140 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 18.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.5412` → IC=+0.193 (n=398)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.5412 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.154 (n=229)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.090)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.124 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0036 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.0468` → IC=+0.278 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0468 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.1052` → IC=+0.135 (n=288)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1052 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.655` → IC=+0.139 (n=242)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.655 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` < `1.0125` → IC=+0.122 (n=247)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0125 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` < `2.5091` → IC=+0.129 (n=257)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.5091 (IC base=+0.080)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.153 (n=306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0046 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.127 (n=429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.6816` → IC=+0.208 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6816 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1226` → IC=+0.171 (n=226)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1226 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.658` → IC=+0.273 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.658 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2854` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2854 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `1727.3747` → IC=+0.150 (n=141)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1727.3747 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.0163` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0163 (IC base=+0.011)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.678` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.678 (IC base=+0.011)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0094` → IC=-0.195 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=175)

- **FILTRO** `ibs_20min` > `0.1429` → IC=-0.255 (n=47)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1429
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=144)

- **PATRÓN** `ibs_20min` > `0.7586` → IC=+0.170 (n=289)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.7586 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.7176` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.7176 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2453` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2453 (IC base=+0.040)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.173 (n=154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0076 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.253 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1429 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1328` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1328 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.3549` → IC=+0.165 (n=159)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.3549 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.815` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.815 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `0.9765` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.9765 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.1476` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1476 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.8571` → IC=+0.199 (n=81)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.8571 (IC base=+0.068)

- **PATRÓN** `libro_liquidez` > `774.2903` → IC=+0.178 (n=85)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 774.2903 (IC base=+0.068)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` < `5.0` → IC=-0.206 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=149)

- **FILTRO** `dist_vwap_pct` > `0.2351` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2351
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=257)

- **FILTRO** `volumen_regimen` < `0.7553` → IC=-0.343 (n=68)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7553
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=205)

- **FILTRO** `volumen_spike_ratio` < `1.518` → IC=-0.186 (n=49)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.518
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=150)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.205 (n=76)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=197)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.381 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=174)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.300 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=163)

- **FILTRO** `dist_vwap_pct` > `0.3328` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3328
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=198)

- **FILTRO** `sigma_ewma_delta_pct` > `10.779` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.779
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=208)

- **FILTRO** `volumen_pendiente_norm` > `0.0559` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0559
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=121)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.261 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

- **FILTRO** `volumen_regimen` < `0.8417` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8417
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=68)

- **FILTRO** `volumen_spike_ratio` > `3.7984` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.7984
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=51)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.315 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=76)

- **FILTRO** `sigma_ewma_delta_pct` > `2.402` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.402
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=69)

- **FILTRO** `volumen_spike_ratio` > `1.5538` → IC=-0.329 (n=33)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5538
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=35)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.438 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=61)

- **FILTRO** `volumen_spike_ratio` > `2.7358` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.7358
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=49)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.350 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=67)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=57)

- **FILTRO** `dist_vwap_pct` > `0.1182` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1182
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=57)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=35)

- **FILTRO** `libro_liquidez` < `1258.6237` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 1258.6237
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=64)

- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.9583 (IC base=-0.156)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=76)

- **FILTRO** `volumen_spike_ratio` < `1.5614` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5614
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=51)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=66)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.167 (n=199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0057 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.131 (n=215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 15.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.141 (n=438)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.6667 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.4828` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.4828 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `0.6589` → IC=+0.151 (n=147)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6589 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` < `0.2366` → IC=+0.132 (n=373)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.2366 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.5344` → IC=+0.167 (n=148)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5344 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.1681` → IC=+0.175 (n=435)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.1681 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.252` → IC=+0.195 (n=152)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.252 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `2923.7123` → IC=+0.157 (n=330)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2923.7123 (IC base=+0.076)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6544` → IC=-0.239 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6544
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=135)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.187 (n=199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0024 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.173 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.154 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.1414` → IC=+0.211 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1414 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.257` → IC=+0.171 (n=71)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 10.257 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.879` → IC=+0.167 (n=175)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 4.879 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `0.6869` → IC=+0.177 (n=199)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6869 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.1828` → IC=+0.177 (n=193)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.1828 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.2594` → IC=+0.178 (n=169)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.2594 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.4468` → IC=+0.170 (n=192)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4468 (IC base=+0.152)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1478` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1478
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=135)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.159 (n=83)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.071)

- **PATRÓN** `libro_liquidez` > `1535.3678` → IC=+0.134 (n=151)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 1535.3678 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.2609` → IC=+0.139 (n=164)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.2609 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.19` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.19 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.218` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.218 (IC base=+0.052)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `dist_vwap_pct` > `0.2725` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2725
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=92)

- **FILTRO** `volumen_spike_ratio` > `1.8262` → IC=-0.125 (n=38)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.8262
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=39)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.288 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.281 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.250 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.6434` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6434 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` < `0.2189` → IC=+0.240 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2189 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.365` → IC=+0.294 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.365 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `1.0151` → IC=+0.274 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0151 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.2516` → IC=+0.291 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2516 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.339 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.1062` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1062 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.241 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.069)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.286)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.286)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `1.0148` → IC=+0.333 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0148 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.286)

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

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.286)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.286)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `1.0148` → IC=+0.333 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0148 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.286)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=1075)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2888.6575` → IC=+0.128 (n=495)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2888.6575 (IC base=+0.103)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=1075)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2888.6575` → IC=+0.128 (n=495)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2888.6575 (IC base=+0.103)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=163)

- **FILTRO** `libro_liquidez` < `2690.866` → IC=-0.239 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 2690.866
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=135)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=246)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=232)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=58)

- **FILTRO** `libro_liquidez` < `11939.3802` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 11939.3802
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=53)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4919.88` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_usd_total` < 4919.88
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2979)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=99)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=56)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=88)

- **FILTRO** `ballena_activa_n` > `124.0` → IC=-0.212 (n=57)

  - _Acción_: SKIP cuando `ballena_activa_n` > 124.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=29)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=119)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.128 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 13.0 (IC base=+0.036)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.131 (n=196)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.495 (IC base=+0.042)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=1094)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1048)

- **FILTRO** `liq_usd_total` < `12056.79` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `liq_usd_total` < 12056.79
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=692)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=367)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=348)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.157 (n=135)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=785)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=785)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=619)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=625)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=625)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=218)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=218)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=180)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=145)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=155)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=179)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=187)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=310)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=310)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=222)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.145 (n=74)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=163)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.123 (n=1548)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1653)

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
- **FILTRO** `py_entrada` < `0.5` → IC=-0.135 (n=209)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=110)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.150 (n=201)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.56 (IC base=+0.039)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.206 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=170)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.129 (n=130)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=76)

- **FILTRO** `restante_min` < `3.74` → IC=-0.150 (n=101)

  - _Acción_: SKIP cuando `restante_min` < 3.74
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=105)

- **FILTRO** `lag_apertura_s` > `75.52` → IC=-0.154 (n=102)

  - _Acción_: SKIP cuando `lag_apertura_s` > 75.52
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=104)

- **PATRÓN** `py_entrada` < `0.58` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.58 (IC base=+0.051)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.144 (n=209)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=73)

- **FILTRO** `profundidad_ratio` < `37.6` → IC=-0.208 (n=70)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.6
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=212)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=222)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.46 (IC base=-0.013)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.129 (n=227)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=135)

- **FILTRO** `restante_min` < `3.33` → IC=-0.194 (n=119)

  - _Acción_: SKIP cuando `restante_min` < 3.33
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=243)

- **FILTRO** `lag_apertura_s` > `98.43` → IC=-0.204 (n=123)

  - _Acción_: SKIP cuando `lag_apertura_s` > 98.43
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=239)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.139 (n=59)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=222)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.130 (n=214)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=115)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.195 (n=93)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=317)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.167 (n=4832)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=15632)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.165 (n=5280)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=15862)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.188 (n=890)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=2769)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.157 (n=882)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2902)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.171 (n=731)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=2318)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.173 (n=910)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=2795)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.183 (n=949)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=2891)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2233)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2597)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3337)

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

- **FILTRO** `hora_utc` < `8.0` → IC=-0.189 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=286)

- **FILTRO** `drift_20min_pct` |x|> `0.1551` → IC=-0.162 (n=137)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1551
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=266)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=388)

- **FILTRO** `libro_liquidez` < `2887.1026` → IC=-0.196 (n=100)

  - _Acción_: SKIP cuando `libro_liquidez` < 2887.1026
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=303)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=806)

- **FILTRO** `libro_liquidez` < `2028.3639` → IC=-0.163 (n=339)

  - _Acción_: SKIP cuando `libro_liquidez` < 2028.3639
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=690)

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
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=39)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=14228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=31613)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=10941)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=34900)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.232 (n=11382)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=34459)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.155 (n=15290)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=30551)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.236 (n=14087)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=44277)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.179 (n=14575)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=43789)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=2297)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5543)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=1884)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=5956)

- **FILTRO** `ibs_7min` < `0.7091` → IC=-0.249 (n=2587)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=5253)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.172 (n=1915)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5925)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.269 (n=2475)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=7667)

- **FILTRO** `ibs_7min` > `0.7778` → IC=-0.210 (n=2535)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=7607)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.130 (n=1867)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=5943)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.246 (n=1943)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=5867)

- **FILTRO** `ibs_7min` < `0.7371` → IC=-0.195 (n=1949)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7371
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5861)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.186 (n=1951)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=5859)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=1905)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=6062)

- **FILTRO** `ibs_7min` > `0.2661` → IC=-0.194 (n=1990)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2661
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5977)

- **FILTRO** `ballena_activa_n` > `147.0` → IC=-0.184 (n=1986)

  - _Acción_: SKIP cuando `ballena_activa_n` > 147.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=5981)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.162 (n=2116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=5358)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.319 (n=1789)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5685)

- **FILTRO** `ibs_7min` < `0.7005` → IC=-0.247 (n=2466)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7005
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=5008)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.223 (n=1641)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5833)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.247 (n=2432)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=8340)

- **FILTRO** `ibs_7min` > `0.7358` → IC=-0.174 (n=2691)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7358
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=8081)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=2454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=5067)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1875)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=5646)

- **FILTRO** `ibs_7min` < `0.7366` → IC=-0.186 (n=1880)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7366
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5641)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.189 (n=1835)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5686)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=1929)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=5861)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.179 (n=1947)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5843)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.178 (n=1932)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5858)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=1850)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=5828)

- **FILTRO** `ibs_7min` < `0.2368` → IC=-0.234 (n=1918)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2368
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=5760)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=2628)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=8499)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.280 (n=1824)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=5694)

- **FILTRO** `ibs_7min` < `0.2308` → IC=-0.223 (n=1872)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2308
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5646)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.202 (n=1791)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5727)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.207 (n=2568)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=7998)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=972)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1256)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.154 (n=50)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=625)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=363)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.146 (n=156)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=309)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=417)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=600)

- **FILTRO** `libro_liquidez` < `3312.3658` → IC=-0.151 (n=167)

  - _Acción_: SKIP cuando `libro_liquidez` < 3312.3658
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=501)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=320)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3979` → IC=+0.143 (n=992)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.3979 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.141 (n=457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.132 (n=370)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 4.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `442.4725` → IC=+0.158 (n=331)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 442.4725 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3779.4381` → IC=+0.131 (n=450)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3779.4381 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.152 (n=323)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 14.0 (IC base=+0.130)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4372` → IC=+0.158 (n=77)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.4372 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.226 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `2641.0058` → IC=+0.247 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2641.0058 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.204 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.146)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.133 (n=194)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 16.0 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.123 (n=237)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.04 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 10.0 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4153` → IC=+0.186 (n=135)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio` |x|> 0.4153 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.152 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 4.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.217 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `7230.8556` → IC=+0.134 (n=181)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 7230.8556 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 73.0 (IC base=+0.129)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.187 (n=177)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.189 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.151)

- **PATRÓN** `total_vol_5m` < `4970.298` → IC=+0.186 (n=119)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 4970.298 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `3405.7473` → IC=+0.158 (n=159)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3405.7473 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 28.0 (IC base=+0.151)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.121 (n=167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 13.0 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=117)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `3657.3836` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3657.3836 (IC base=+0.097)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.6961` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.6961
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=122)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.271 (n=282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=284)

- **FILTRO** `T_h` > `129.6273` → IC=-0.234 (n=141)

  - _Acción_: SKIP cuando `T_h` > 129.6273
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=425)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.130 (n=187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0043 (IC base=-0.091)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0044` → IC=-0.169 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.322 (n=43)

- **FILTRO** `T_h` > `88.6373` → IC=-0.357 (n=40)

  - _Acción_: SKIP cuando `T_h` > 88.6373
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=128)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.322 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=-0.041)

- **PATRÓN** `pct_vs_K` |x|≤ `1.73` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `pct_vs_K` |x|≤ 1.73 (IC base=-0.041)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.128 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `pct_vs_K` |x|> `8.3214` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.3214
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.190 (n=69)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=35)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.066)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0047` → IC=-0.208 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=387)

- **FILTRO** `T_h` > `70.6078` → IC=-0.165 (n=386)

  - _Acción_: SKIP cuando `T_h` > 70.6078
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=129)

- **FILTRO** `pct_vs_K` |x|> `2.1556` → IC=-0.379 (n=221)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.1556
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=222)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=136)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.305 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=82)

- **FILTRO** `pct_vs_K` |x|> `1.9536` → IC=-0.390 (n=80)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.9536
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=82)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

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
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.253 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=73)

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.276 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=97)

- **FILTRO** `sigma_h` > `0.0088` → IC=-0.329 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=103)

- **FILTRO** `T_h` > `54.8663` → IC=-0.274 (n=91)

  - _Acción_: SKIP cuando `T_h` > 54.8663
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=45)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` > `0.006` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0073` → IC=-0.235 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=97)

- **FILTRO** `T_h` > `113.0501` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `T_h` > 113.0501
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=65)

- **FILTRO** `sigma_h` > `0.0135` → IC=-0.344 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0135
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=61)

- **FILTRO** `sigma_h` < `0.0068` → IC=-0.292 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=69)

- **FILTRO** `T_h` > `34.5323` → IC=-0.371 (n=68)

  - _Acción_: SKIP cuando `T_h` > 34.5323
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1221` → IC=+0.461 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1221 (IC base=+0.335)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.381 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.335)

- **PATRÓN** `T_h` < `0.9804` → IC=+0.351 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9804 (IC base=+0.335)

- **PATRÓN** `T_h` > `0.4186` → IC=+0.369 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4186 (IC base=+0.335)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.335)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.351 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.335)

- **PATRÓN** `edge` > `0.096` → IC=+0.445 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.427 (n=67)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.440 (n=132)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.417)

- **PATRÓN** `T_h` < `1.014` → IC=+0.425 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.014 (IC base=+0.417)

- **PATRÓN** `T_h` > `1.4832` → IC=+0.441 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4832 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.3885` → IC=+0.465 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3885 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

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
- **PATRÓN** `edge` > `0.1885` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1885 (IC base=+0.429)

- **PATRÓN** `sigma_h` < `0.0161` → IC=+0.462 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0161 (IC base=+0.429)

- **PATRÓN** `T_h` > `0.6729` → IC=+0.457 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.6729 (IC base=+0.429)

- **PATRÓN** `dist_50` > `0.3288` → IC=+0.462 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3288 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.429)

- **PATRÓN** `edge` > `0.2005` → IC=+0.477 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.477 (n=128)
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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=261)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=346)

- **PATRÓN** `streak_estiramiento` < `0.4396` → IC=+0.152 (n=87)

  - _Acción_: Kelly boost +0.76€ cuando `streak_estiramiento` < 0.4396 (IC base=+0.025)

- **PATRÓN** `streak_estiramiento` < `0.5654` → IC=+0.177 (n=153)

  - _Acción_: Kelly boost +0.89€ cuando `streak_estiramiento` < 0.5654 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `2526.0042` → IC=+0.133 (n=126)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2526.0042 (IC base=+0.042)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=25)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `1831586.9` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `volumen_racha` > 1831586.9
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=66)

- **FILTRO** `streak_estiramiento` > `0.4782` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4782
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=61)

- **FILTRO** `ballena_activa_n` > `51.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 51.0
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=65)

- **PATRÓN** `volumen_racha` < `945898.4` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_racha` < 945898.4 (IC base=+0.028)

- **PATRÓN** `streak_estiramiento` < `0.4782` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `streak_estiramiento` < 0.4782 (IC base=+0.028)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.088)

- **PATRÓN** `streak_estiramiento` < `0.326` → IC=+0.188 (n=62)

  - _Acción_: Kelly boost +0.94€ cuando `streak_estiramiento` < 0.326 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.151 (n=104)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 46.0 (IC base=+0.088)

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
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=38)

- **FILTRO** `streak_estiramiento` > `1.0608` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.0608
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=32)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=26)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=655)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

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
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=865)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1321)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1002)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=1012)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3601)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1922)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.202 (n=959)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.232 (n=958)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.1644` → IC=+0.204 (n=2528)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1644 (IC base=+0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3457` → IC=+0.209 (n=2539)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3457 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.202 (n=2651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=2647)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.195)

- **PATRÓN** `ibs_15` > `0.5957` → IC=+0.269 (n=2872)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5957 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.1219` → IC=+0.190 (n=1344)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1219 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` < `0.3041` → IC=+0.182 (n=2190)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.3041 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.662` → IC=+0.271 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.662 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `5944.0797` → IC=+0.200 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5944.0797 (IC base=+0.195)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1162)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.240 (n=348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.267 (n=174)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.215)

- **PATRÓN** `delta_ratio_macro` |x|> `0.251` → IC=+0.250 (n=174)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.251 (IC base=+0.215)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.237 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_15` > `0.7176` → IC=+0.278 (n=521)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7176 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.2456` → IC=+0.246 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2456 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.288 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `16282.4193` → IC=+0.250 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16282.4193 (IC base=+0.215)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.513` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.513
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=667)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.184 (n=194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0034 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.158 (n=255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2356` → IC=+0.162 (n=193)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.2356 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1276` → IC=+0.158 (n=223)

  - _Acción_: Kelly boost +0.79€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1276 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.157 (n=269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 15.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=411)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.5749` → IC=+0.240 (n=579)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5749 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.149 (n=317)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1534 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.914` → IC=+0.277 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.914 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3532.094` → IC=+0.150 (n=518)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3532.094 (IC base=+0.143)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `19.46` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.46
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=237)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.153 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0054 (IC base=+0.135)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.171 (n=168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0095 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.2298` → IC=+0.162 (n=504)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2298 (IC base=+0.135)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0632` → IC=+0.144 (n=504)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio_macro` |x|> 0.0632 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3382` → IC=+0.161 (n=455)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3382 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.154 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.136 (n=462)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.9189` → IC=+0.312 (n=168)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9189 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1943` → IC=+0.149 (n=459)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1943 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.786` → IC=+0.193 (n=99)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 17.786 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=302)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.135)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.013)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.259 (n=600)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0133 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1651` → IC=+0.227 (n=591)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1651 (IC base=+0.220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1097` → IC=+0.224 (n=448)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1097 (IC base=+0.220)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0897` → IC=+0.258 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0897 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.235 (n=594)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.220)

- **PATRÓN** `ibs_15` > `0.5758` → IC=+0.301 (n=672)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5758 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.1996` → IC=+0.234 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1996 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.872` → IC=+0.262 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.872 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2940.5394` → IC=+0.282 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2940.5394 (IC base=+0.220)

- **PATRÓN** `ibs_15` < `0.1096` → IC=+0.161 (n=699)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` < 0.1096 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.367 (n=373)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.384 (n=187)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1122` → IC=+0.361 (n=373)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1122 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.385 (n=372)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1356` → IC=+0.395 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1356 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=563)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.395 (n=561)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.392 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.247` → IC=+0.373 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.247 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `3837.2318` → IC=+0.372 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3837.2318 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `434.0` → IC=+0.381 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 434.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.356 (n=200)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.357)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.374 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.357)

- **PATRÓN** `drift_15min` |x|≤ `0.5078` → IC=+0.356 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5078 (IC base=+0.357)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2147` → IC=+0.391 (n=135)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2147 (IC base=+0.357)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.389 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.357)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.357)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.384 (n=299)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.357)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.571` → IC=+0.365 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.571 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` < `25.57` → IC=+0.357 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 25.57 (IC base=+0.357)

- **PATRÓN** `libro_liquidez` > `15251.8586` → IC=+0.384 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15251.8586 (IC base=+0.357)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.405 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.357)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.364 (n=174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.383 (n=118)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.365)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.375 (n=174)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0901` → IC=+0.381 (n=233)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0901 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.389 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.419 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.409 (n=261)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1529` → IC=+0.368 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1529 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` < `0.2765` → IC=+0.367 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2765 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.939` → IC=+0.383 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.939 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.828` → IC=+0.364 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.828 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.373 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3893.6222` → IC=+0.392 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3893.6222 (IC base=+0.365)

- **PATRÓN** `ballena_activa_n` < `141.0` → IC=+0.371 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 141.0 (IC base=+0.365)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.217 (n=961)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2887)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.207 (n=1483)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1409` → IC=+0.190 (n=614)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio_macro` |x|> 0.1409 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.6335` → IC=+0.282 (n=921)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6335 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.201 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2619` → IC=+0.198 (n=776)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2619 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2231` → IC=+0.267 (n=1036)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2231 (IC base=-0.013)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3262` → IC=+0.253 (n=3043)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3262 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3514` → IC=+0.280 (n=3107)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3514 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.8624` → IC=+0.294 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8624 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.204 (n=535)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1606)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.230 (n=535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=1606)

- **FILTRO** `sigma_ewma_delta_pct` > `23.623` → IC=-0.261 (n=307)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.623
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=1834)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.200 (n=58)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=2083)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.174 (n=216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0027 (IC base=+0.090)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2081` → IC=+0.305 (n=126)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2081 (IC base=+0.090)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1422` → IC=+0.292 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1422 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.133 (n=317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.090)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.332 (n=277)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1012` → IC=+0.291 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1012 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` < `0.3651` → IC=+0.290 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3651 (IC base=+0.090)

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
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=598)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.159 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0058 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.163 (n=413)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0038 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1112` → IC=+0.184 (n=308)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1112 (IC base=+0.151)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1388` → IC=+0.155 (n=308)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.1388 (IC base=+0.151)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.195 (n=346)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.175 (n=321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.151)

- **PATRÓN** `ibs_15` > `0.6307` → IC=+0.254 (n=462)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6307 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.5656` → IC=+0.155 (n=82)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.5656 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1008` → IC=+0.153 (n=332)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1008 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.253 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=598)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `10899.0951` → IC=+0.167 (n=154)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 10899.0951 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.257 (n=356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.3488` → IC=+0.245 (n=938)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3488 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `0.7502` → IC=+0.252 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7502 (IC base=+0.242)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1543` → IC=+0.260 (n=710)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1543 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.248 (n=415)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.242)

- **PATRÓN** `ibs_15` < `0.366` → IC=+0.271 (n=1066)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.366 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.764` → IC=+0.298 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.764 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.581` → IC=+0.259 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.581 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.664` → IC=+0.244 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.664 (IC base=+0.242)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1722` → IC=-0.249 (n=301)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1722
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=586)

- **FILTRO** `drift_15min` |x|> `0.8773` → IC=-0.271 (n=221)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8773
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=666)

- **FILTRO** `sigma_ewma_delta_pct` > `6.662` → IC=-0.194 (n=217)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.662
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=670)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.252 (n=103)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=784)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.178)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.178)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.178)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.178)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.242 (n=483)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.288 (n=483)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.172` → IC=+0.245 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.172 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.248 (n=538)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=540)

- **FILTRO** `drift_15min` |x|> `1.2315` → IC=-0.264 (n=269)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2315
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=809)

- **FILTRO** `libro_liquidez` < `2986.2027` → IC=-0.211 (n=808)

  - _Acción_: SKIP cuando `libro_liquidez` < 2986.2027
  - _Potencial_: sin este filtro IC_bueno=-0.169 (n=270)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.201)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0662` → IC=+0.273 (n=677)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0662 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1103` → IC=+0.304 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1103 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=760)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `1.0395` → IC=+0.359 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0395 (IC base=-0.026)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.028)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.028)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.294 (n=814)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0534` → IC=+0.326 (n=309)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0534 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.301 (n=309)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2237` → IC=+0.308 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2237 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=967)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.322 (n=925)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.424` → IC=+0.325 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.424 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.358 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `12848.0159` → IC=+0.303 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12848.0159 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.308 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.317 (n=167)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.285)

- **PATRÓN** `drift_15min` |x|≤ `0.4172` → IC=+0.285 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4172 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2575` → IC=+0.311 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2575 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3852` → IC=+0.296 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3852 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.309 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.313 (n=501)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.332 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.364 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.284 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `16346.0348` → IC=+0.323 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16346.0348 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.304 (n=284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.294)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.299 (n=425)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.326 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.296 (n=283)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3006` → IC=+0.320 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3006 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.316 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.332 (n=426)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.436` → IC=+0.315 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.436 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.341 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0872` → IC=-0.256 (n=76)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0872
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=232)

- **FILTRO** `sigma_h` > `0.0042` → IC=-0.245 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=204)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.196 (n=67)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=136)

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
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=118)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.174 (n=44)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=134)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.297` → IC=-0.139 (n=34)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.297
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.296` → IC=-0.370 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.296
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `drift_15min` |x|> `0.1655` → IC=-0.235 (n=32)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.1655
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

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
- **PATRÓN** `T_h` > `81.9543` → IC=+0.213 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 81.9543 (IC base=+0.198)

- **PATRÓN** `ratio` < `0.9763` → IC=+0.436 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9763 (IC base=+0.198)

- **PATRÓN** `T_h` > `145.7372` → IC=+0.386 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7372 (IC base=+0.338)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.320 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.338)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.3918` → IC=+0.202 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.179)

- **PATRÓN** `ratio` < `0.972` → IC=+0.418 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.972 (IC base=+0.179)

- **PATRÓN** `T_h` > `107.4888` → IC=+0.301 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 107.4888 (IC base=+0.291)

- **PATRÓN** `ratio` > `1.0228` → IC=+0.332 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0228 (IC base=+0.291)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.249 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.231)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.407 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.231)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.350 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.326)

- **PATRÓN** `ratio` > `1.0112` → IC=+0.362 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0112 (IC base=+0.326)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.400)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5957 sube el IC de +0.195 a +0.269 en UPDOWN_GBM#15min (n=2872). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7176 sube el IC de +0.215 a +0.278 en UPDOWN_GBM#BTC#15min (n=521). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5749 sube el IC de +0.143 a +0.240 en UPDOWN_GBM#ETH#15min (n=579). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9189 sube el IC de +0.135 a +0.312 en UPDOWN_GBM#SOL#15min (n=168). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5758 sube el IC de +0.220 a +0.301 en UPDOWN_GBM#XRP#15min (n=672). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1096 sube el IC de +0.066 a +0.161 en UPDOWN_GBM#XRP#15min (n=699). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6335 sube el IC de -0.067 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=921). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3514 sube el IC de -0.013 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=3107). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.090 a +0.332 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=277). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.190 a +0.311 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6307 sube el IC de +0.151 a +0.254 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=462). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.366 sube el IC de +0.242 a +0.271 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1066). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.178 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.039 a +0.288 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=483). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.201 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=760). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.289 a +0.322 en UPDOWN_GBM_IBS_ALTO (n=925). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.285 a +0.313 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=501). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.294 a +0.332 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=426). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.362 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=561). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.357 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=299). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.365 a +0.409 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=261). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1660 | +0.088 | +181.85€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1660 | +0.088 | +181.85€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1289 | +0.092 | +154.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1289 | +0.092 | +154.81€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 268 | +0.067 | +11.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 268 | +0.067 | +11.32€ | 4 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 364 | +0.000 | +70.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 364 | +0.000 | +70.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 270 | -0.004 | +50.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 270 | -0.004 | +50.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 71 | +0.034 | +19.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 71 | +0.034 | +19.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 36012 | -0.084 | -4700.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1850 | -0.008 | -240.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 34162 | -0.088 | -4459.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4422 | -0.116 | -761.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4422 | -0.116 | -761.56€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1850 | -0.008 | -240.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1850 | -0.008 | -240.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4107 | -0.113 | -841.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4107 | -0.113 | -841.46€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9354 | +0.005 | -883.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9354 | +0.005 | -883.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9251 | -0.111 | -703.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9251 | -0.111 | -703.89€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7028 | -0.152 | -1268.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7028 | -0.152 | -1268.86€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 28740 | -0.018 | +3650.34€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 7420 | +0.003 | +1764.48€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 21320 | -0.026 | +1885.86€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 28740 | -0.018 | +3650.34€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 7420 | +0.003 | +1764.48€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 21320 | -0.026 | +1885.86€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 125113 | +0.114 | -5432.80€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 17005 | +0.182 | -515.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 538 | -0.037 | -65.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 99893 | +0.104 | -4569.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7677 | +0.103 | -282.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 16580 | +0.105 | -1098.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 57 | -0.144 | +12.20€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 16508 | +0.106 | -1098.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 24593 | +0.129 | -392.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4969 | +0.194 | -143.17€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 16561 | +0.117 | -143.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3021 | +0.087 | -82.76€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 16630 | +0.096 | -1260.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 66 | -0.103 | -3.51€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 16549 | +0.097 | -1245.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 26595 | +0.123 | -482.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7023 | +0.175 | -118.73€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 16766 | +0.106 | -301.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2794 | +0.101 | -53.91€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 24118 | +0.114 | -1329.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4832 | +0.190 | -271.63€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 441 | -0.001 | -11.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 16983 | +0.092 | -901.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1862 | +0.132 | -145.39€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 16597 | +0.103 | -869.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 58 | -0.050 | +9.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 16526 | +0.103 | -878.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 20031 | +0.194 | -1259.26€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 20031 | +0.194 | -1259.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4625 | +0.175 | -421.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4625 | +0.175 | -421.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2294 | +0.200 | -50.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2294 | +0.200 | -50.98€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4555 | +0.181 | -370.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4555 | +0.181 | -370.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3987 | +0.242 | -144.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3987 | +0.242 | -144.35€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4491 | +0.190 | -285.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4491 | +0.190 | -285.37€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 913 | +0.427 | -32.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 913 | +0.427 | -32.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 362 | +0.434 | -6.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 362 | +0.434 | -6.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 351 | +0.429 | -9.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 351 | +0.429 | -9.87€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 188 | +0.405 | -12.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 188 | +0.405 | -12.81€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 69676 | +0.200 | -5149.89€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 69676 | +0.200 | -5149.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 11984 | +0.184 | -1248.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 11984 | +0.184 | -1248.46€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 11222 | +0.224 | -389.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 11222 | +0.224 | -389.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 11960 | +0.178 | -1322.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 11960 | +0.178 | -1322.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 11291 | +0.220 | -435.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 11291 | +0.220 | -435.03€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 11549 | +0.201 | -784.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 11549 | +0.201 | -784.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 11670 | +0.195 | -969.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 11670 | +0.195 | -969.99€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 26584 | +0.117 | +219.94€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 26584 | +0.117 | +219.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 13206 | +0.121 | +191.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 13206 | +0.121 | +191.40€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 13378 | +0.114 | +28.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 13378 | +0.114 | +28.54€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1836 | +0.292 | -8.35€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1836 | +0.292 | -8.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 829 | +0.283 | -10.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 829 | +0.283 | -10.05€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 889 | +0.290 | -2.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 889 | +0.290 | -2.95€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 118 | +0.350 | +4.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 118 | +0.350 | +4.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 840 | +0.442 | +5.11€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 840 | +0.442 | +5.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 404 | +0.441 | +0.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 404 | +0.441 | +0.95€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 390 | +0.444 | +3.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 390 | +0.444 | +3.60€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1426 | +0.069 | -64.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 528 | +0.060 | -38.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 898 | +0.074 | -26.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 68 | +0.100 | +1.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 68 | +0.100 | +1.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1107 | +0.075 | -31.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 209 | +0.078 | -5.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 898 | +0.074 | -26.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 251 | +0.034 | -34.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 251 | +0.034 | -34.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 51511 | +0.100 | -1295.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4178 | +0.093 | +61.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 47333 | +0.101 | -1356.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 28485 | +0.105 | -291.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4178 | +0.093 | +61.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 24307 | +0.107 | -352.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 10346 | +0.110 | -17.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 10346 | +0.110 | -17.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 12680 | +0.080 | -986.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 12680 | +0.080 | -986.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 874 | +0.201 | -102.69€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 874 | +0.201 | -102.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 874 | +0.201 | -102.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 874 | +0.201 | -102.69€ | 2 | 4 |
| ✅ GBM_LATE_15M | 35764 | +0.090 | +17971.95€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 35764 | +0.090 | +17971.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6025 | +0.206 | +4714.19€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6025 | +0.206 | +4714.19€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 5322 | +0.179 | +3899.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5322 | +0.179 | +3899.88€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 6371 | +0.202 | +4871.65€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6371 | +0.202 | +4871.65€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 5026 | +0.038 | +1301.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5026 | +0.038 | +1301.82€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 5099 | -0.031 | +1076.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5099 | -0.031 | +1076.16€ | 3 | 13 |
| ✅ GBM_LATE_15M#XRP | 7921 | -0.036 | +2108.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7921 | -0.036 | +2108.26€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 38807 | +0.087 | +20684.63€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 38807 | +0.087 | +20684.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7537 | +0.009 | +3807.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7537 | +0.009 | +3807.42€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 8089 | +0.013 | +1753.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 8089 | +0.013 | +1753.32€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5450 | +0.270 | +5678.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5450 | +0.270 | +5678.80€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 6662 | +0.013 | +1521.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 6662 | +0.013 | +1521.08€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6305 | +0.037 | +2522.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6305 | +0.037 | +2522.91€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4764 | +0.293 | +5401.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4764 | +0.293 | +5401.10€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 28521 | +0.177 | +22480.10€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 28521 | +0.177 | +22480.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4326 | +0.218 | +3650.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4326 | +0.218 | +3650.57€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4493 | +0.151 | +3285.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4493 | +0.151 | +3285.54€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4538 | +0.218 | +3801.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4538 | +0.218 | +3801.75€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4795 | +0.139 | +3587.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4795 | +0.139 | +3587.60€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5350 | +0.125 | +3916.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5350 | +0.125 | +3916.50€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5019 | +0.218 | +4238.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5019 | +0.218 | +4238.14€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7679 | +0.140 | +3753.83€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7679 | +0.140 | +3753.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 342 | +0.142 | +200.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 342 | +0.142 | +200.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2367 | +0.149 | +1354.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2367 | +0.149 | +1354.35€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 376 | +0.140 | +173.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 376 | +0.140 | +173.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2360 | +0.153 | +1167.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2360 | +0.153 | +1167.15€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1696 | +0.108 | +616.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1696 | +0.108 | +616.51€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 538 | +0.135 | +242.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 538 | +0.135 | +242.32€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 36000 | +0.183 | +28083.85€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 36000 | +0.183 | +28083.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5739 | +0.233 | +5156.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5739 | +0.233 | +5156.32€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5563 | +0.149 | +3689.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5563 | +0.149 | +3689.38€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6046 | +0.230 | +5328.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6046 | +0.230 | +5328.02€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5853 | +0.139 | +4110.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5853 | +0.139 | +4110.60€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6376 | +0.124 | +4345.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6376 | +0.124 | +4345.83€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6423 | +0.221 | +5453.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6423 | +0.221 | +5453.70€ | 0 | 21 |
| ✅ GBM_LATE_5M | 9960 | +0.186 | +7122.55€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 9960 | +0.186 | +7122.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2197 | +0.177 | +1641.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2197 | +0.177 | +1641.75€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 1001 | +0.177 | +660.02€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1001 | +0.177 | +660.02€ | 0 | 16 |
| ✅ GBM_LATE_5M#ETH | 3072 | +0.189 | +2118.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3072 | +0.189 | +2118.97€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 1309 | +0.175 | +903.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1309 | +0.175 | +903.71€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 1462 | +0.183 | +984.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1462 | +0.183 | +984.11€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2759 | +0.069 | +970.57€ | 0 | 9 |
| ✅ GBM_LATE_60M#60min | 2759 | +0.069 | +970.57€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1039 | +0.086 | +378.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1039 | +0.086 | +378.91€ | 0 | 11 |
| ✅ GBM_LATE_60M#ETH | 871 | +0.069 | +359.10€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 871 | +0.069 | +359.10€ | 0 | 9 |
| ✅ GBM_LATE_60M#SOL | 849 | +0.048 | +232.56€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 849 | +0.048 | +232.56€ | 2 | 12 |
| 🚫 GBM_LATE_60M_FADE | 504 | -0.239 | -15.30€ | 10 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 504 | -0.239 | -15.30€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 191 | -0.231 | -9.54€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 191 | -0.231 | -9.54€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 176 | -0.219 | +0.69€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 176 | -0.219 | +0.69€ | 7 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 137 | -0.270 | -6.45€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 137 | -0.270 | -6.45€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1243 | +0.087 | +316.90€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1243 | +0.087 | +316.90€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 476 | +0.084 | +100.89€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 476 | +0.084 | +100.89€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 449 | +0.061 | +72.75€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 449 | +0.061 | +72.75€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 318 | +0.128 | +143.27€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 318 | +0.128 | +143.27€ | 2 | 14 |
| ✅ LATE_WINDOW_5MIN | 139 | +0.252 | +118.97€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 139 | +0.252 | +118.97€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 139 | +0.252 | +118.97€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 139 | +0.252 | +118.97€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 2971 | +0.100 | +755.78€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2971 | +0.100 | +755.78€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2971 | +0.100 | +755.78€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2971 | +0.100 | +755.78€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 446 | -0.069 | -32.31€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 446 | -0.069 | -32.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 127 | -0.027 | -0.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 127 | -0.027 | -0.72€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 70 | -0.097 | -8.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 70 | -0.097 | -8.98€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 168 | -0.029 | -5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 168 | -0.029 | -5.75€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 3184 | +0.020 | +81.63€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3184 | +0.020 | +81.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 155 | +0.022 | -2.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 155 | +0.022 | -2.00€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 553 | +0.028 | +38.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 553 | +0.028 | +38.57€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1144 | +0.028 | +29.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1144 | +0.028 | +29.27€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 733 | +0.013 | +2.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 733 | +0.013 | +2.00€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 396 | +0.015 | +18.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 396 | +0.015 | +18.87€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1505 | -0.041 | -25.42€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1505 | -0.041 | -25.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 427 | -0.034 | -11.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 427 | -0.034 | -11.00€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 501 | -0.017 | +4.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 501 | -0.017 | +4.01€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 577 | -0.067 | -18.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 577 | -0.067 | -18.43€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 5879 | -0.020 | +82.66€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2781 | -0.025 | +6.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 3098 | -0.015 | +76.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 167 | -0.003 | +7.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 81 | +0.042 | +11.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 86 | -0.045 | -3.67€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1480 | -0.009 | +38.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 703 | -0.013 | +7.14€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 777 | -0.004 | +31.51€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 649 | -0.025 | +5.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 327 | -0.038 | -6.49€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 322 | -0.012 | +12.28€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1207 | -0.034 | -30.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 553 | -0.051 | -38.65€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 654 | -0.020 | +7.97€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1149 | -0.013 | +39.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 553 | -0.013 | +24.12€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 596 | -0.013 | +15.67€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1227 | -0.024 | +21.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 564 | -0.025 | +8.27€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 663 | -0.023 | +12.89€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 41606 | -0.002 | +1995.52€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 41606 | -0.002 | +1995.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 7443 | +0.025 | +961.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 7443 | +0.025 | +961.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6133 | -0.033 | -102.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6133 | -0.033 | -102.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 7545 | +0.022 | +752.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 7545 | +0.022 | +752.03€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5957 | -0.050 | -172.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5957 | -0.050 | -172.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 7020 | -0.007 | +214.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 7020 | -0.007 | +214.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 7508 | +0.014 | +342.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 7508 | +0.014 | +342.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6288 | -0.059 | -145.77€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6288 | -0.059 | -145.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1220 | +0.001 | -13.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1220 | +0.001 | -13.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1569 | -0.076 | -33.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1569 | -0.076 | -33.06€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 52 | -0.074 | -3.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 52 | -0.074 | -3.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 737 | -0.122 | -33.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 737 | -0.122 | -33.42€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1854 | -0.078 | -36.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1854 | -0.078 | -36.96€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3358 | +0.004 | -2.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3358 | +0.004 | -2.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 138 | +0.000 | -1.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 138 | +0.000 | -1.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1322 | +0.005 | +5.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1322 | +0.005 | +5.17€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1389 | +0.007 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1389 | +0.007 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 104205 | -0.074 | +1776.68€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 104205 | -0.074 | +1776.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 17982 | -0.074 | +988.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 17982 | -0.074 | +988.50€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 15777 | -0.098 | -864.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 15777 | -0.098 | -864.50€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 18246 | -0.066 | +1048.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 18246 | -0.066 | +1048.41€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 15311 | -0.095 | -444.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 15311 | -0.095 | -444.32€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 18805 | -0.052 | +376.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 18805 | -0.052 | +376.57€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 18084 | -0.064 | +672.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 18084 | -0.064 | +672.01€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8496 | -0.032 | -178.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8496 | -0.032 | -178.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1946 | -0.044 | -21.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1946 | -0.044 | -21.20€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2552 | -0.027 | -48.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2552 | -0.027 | -48.96€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1134 | -0.051 | -25.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1134 | -0.051 | -25.82€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 860 | -0.025 | -29.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 860 | -0.025 | -29.39€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1457 | +0.123 | +586.95€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#5min | 1321 | +0.130 | +574.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 306 | +0.146 | +164.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 306 | +0.146 | +164.15€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 258 | +0.119 | +88.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 258 | +0.119 | +88.22€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 270 | +0.129 | +122.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 270 | +0.129 | +122.23€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 236 | +0.151 | +128.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 236 | +0.151 | +128.97€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 251 | +0.097 | +70.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 251 | +0.097 | +70.80€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1090 | -0.021 | -27.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1090 | -0.021 | -27.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 210 | -0.005 | +5.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 210 | -0.005 | +5.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 177 | -0.020 | -1.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 177 | -0.020 | -1.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 288 | -0.038 | -18.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 288 | -0.038 | -18.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 233 | +0.002 | +0.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 233 | +0.002 | +0.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 182 | -0.043 | -12.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 182 | -0.043 | -12.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 795 | -0.072 | -32.80€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 363 | -0.127 | -76.44€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 283 | -0.163 | -69.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 80 | +0.000 | -7.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 281 | -0.030 | +30.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 202 | -0.025 | +29.23€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 79 | -0.043 | +0.77€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 151 | -0.016 | +13.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 122 | -0.024 | +8.23€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 29 | +0.016 | +5.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 607 | -0.089 | -31.83€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 188 | -0.016 | -0.96€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 958 | -0.202 | -42.04€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 395 | -0.198 | -31.54€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 340 | -0.202 | -32.33€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 55 | -0.167 | +0.79€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 324 | -0.212 | -26.36€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 280 | -0.220 | -31.94€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 44 | -0.152 | +5.58€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 239 | -0.193 | +15.86€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 220 | -0.189 | +12.72€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 840 | -0.205 | -51.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 118 | -0.175 | +9.51€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 406 | +0.395 | +373.66€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 102 | +0.375 | +92.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 102 | +0.375 | +92.55€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 251 | +0.457 | +234.99€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 251 | +0.457 | +234.99€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 406 | +0.395 | +373.66€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 645 | +0.035 | +33.94€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 645 | +0.035 | +33.94€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 49 | +0.010 | -2.27€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 49 | +0.010 | -2.27€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 67 | -0.007 | -0.79€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 67 | -0.007 | -0.79€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 233 | +0.066 | +33.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 233 | +0.066 | +33.58€ | 3 | 5 |
| ✅ STREAK_FADE_5M | 3328 | -0.021 | -129.61€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3328 | -0.021 | -129.61€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 585 | -0.026 | -25.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 585 | -0.026 | -25.65€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 157 | -0.041 | -13.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 157 | -0.041 | -13.87€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1535 | -0.017 | -52.57€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1535 | -0.017 | -52.57€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 93 | -0.047 | -8.86€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 93 | -0.047 | -8.86€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 39 | -0.085 | -3.98€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 39 | -0.085 | -3.98€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 54 | -0.018 | -4.88€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 54 | -0.018 | -4.88€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10069 | +0.019 | +110.77€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10069 | +0.019 | +110.77€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2648 | +0.021 | +27.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2648 | +0.021 | +27.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2496 | +0.027 | +53.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2496 | +0.027 | +53.24€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2869 | +0.009 | -1.74€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2869 | +0.009 | -1.74€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2056 | +0.021 | +32.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2056 | +0.021 | +32.00€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9127 | +0.013 | -48.50€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 9127 | +0.013 | -48.50€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3620 | +0.018 | -5.23€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3620 | +0.018 | -5.23€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3551 | +0.011 | -28.46€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3551 | +0.011 | -28.46€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1956 | +0.008 | -14.81€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1956 | +0.008 | -14.81€ | 1 | 0 |
| ✅ UPDOWN_GBM | 65124 | +0.050 | +5533.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 16274 | +0.085 | +3678.72€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2154 | +0.006 | +11.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 42783 | +0.044 | +1789.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3695 | +0.007 | +58.15€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6694 | +0.087 | +1016.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1482 | +0.157 | +656.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5135 | +0.068 | +360.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 12773 | +0.052 | +1050.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2022 | +0.090 | +487.79€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 550 | +0.011 | +5.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 8461 | +0.056 | +511.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1660 | +0.005 | +44.05€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 80 | -0.085 | +1.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 7951 | +0.065 | +808.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1472 | +0.146 | +575.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6401 | +0.047 | +234.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 14228 | +0.040 | +847.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3759 | +0.059 | +511.34€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 544 | +0.007 | +8.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 8594 | +0.040 | +319.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1259 | +0.007 | +4.74€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 72 | -0.108 | +2.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 14283 | +0.027 | +604.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3850 | +0.036 | +357.34€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 533 | -0.001 | -0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 9060 | +0.028 | +244.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 776 | +0.010 | +9.36€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 64 | -0.151 | -6.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 9193 | +0.059 | +1208.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3689 | +0.104 | +1089.60€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 372 | +0.011 | +0.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5132 | +0.030 | +118.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 216 | -0.115 | -1.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 745 | +0.362 | +262.94€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 745 | +0.362 | +262.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 398 | +0.357 | +130.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 398 | +0.357 | +130.14€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 347 | +0.365 | +132.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 347 | +0.365 | +132.80€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 17628 | -0.025 | +4235.02€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 17628 | -0.025 | +4235.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1601 | -0.058 | +474.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1601 | -0.058 | +474.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3002 | -0.110 | +147.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3002 | -0.110 | +147.36€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 898 | +0.217 | +733.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 898 | +0.217 | +733.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2035 | +0.215 | +1306.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2035 | +0.215 | +1306.56€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5011 | -0.064 | +655.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5011 | -0.064 | +655.73€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5081 | -0.063 | +917.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5081 | -0.063 | +917.06€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 195 | +0.033 | +5.53€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 195 | +0.033 | +5.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 195 | +0.033 | +5.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 195 | +0.033 | +5.53€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1233 | +0.289 | +1025.18€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1233 | +0.289 | +1025.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 667 | +0.285 | +520.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 667 | +0.285 | +520.85€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 566 | +0.294 | +504.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 566 | +0.294 | +504.33€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 772 | -0.115 | -84.24€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 772 | -0.115 | -84.24€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 227 | -0.089 | -18.82€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 227 | -0.089 | -18.82€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 81 | -0.163 | -8.24€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 81 | -0.163 | -8.24€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 85 | -0.190 | -7.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 85 | -0.190 | -7.12€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 3109 | +0.305 | +1529.10€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1118 | +0.259 | +163.04€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1187 | +0.299 | +531.90€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 804 | +0.378 | +834.16€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.013 n=791 — no justifica filtro, seguir monitorizando
  - _Datos_: n=791 IC=+0.013 PNL=+36.93€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 658 celda(s) pasan gate riguroso completo de 2556 evaluadas (n>=40) y 3537 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.036 < 0.08 — monitorear
  - _Datos_: n=3846 IC=+0.036 PNL=+355.90€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1187/15 IC=+0.299 PNL=+531.90€ | BTC: n=1118/15 IC=+0.259 PNL=+163.04€ | SOL: n=804/15 IC=+0.378 PNL=+834.16€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.134 n=681/60 | contraria IC=+0.199 n=706 | gap=-0.065 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=408, boost estimado=+0.011. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1258/40 IC=+0.007 PNL=+5.25€ | BTC#60min: n=1659/40 IC=+0.006 PNL=+44.56€ | SOL#60min: n=775/40 IC=+0.011 PNL=+9.87€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=474381 | tras_1loss IC=+0.091 n=362693 | tras_2loss IC=+0.060 n=148218/40 | gap=-0.012 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.212 > 0.08 con n=599 PNL=+474.50€
  - _Datos_: n=599 IC=+0.212 PNL=+474.50€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.08 con n=637 PNL=+455.83€
  - _Datos_: n=637 IC=+0.206 PNL=+455.83€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.08 con n=55 PNL=+31.20€
  - _Datos_: n=55 IC=+0.184 PNL=+31.20€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=2540 PNL=+1417.84€
  - _Datos_: n=2540 IC=+0.334 PNL=+1417.84€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=515 IC=+0.074 PNL=+56.41€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=515 IC=+0.074 PNL=+56.41€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=71 IC=+0.199 PNL=+51.49€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=71 IC=+0.199 PNL=+51.49€

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
  - _Estado_: n=2476 IC=+0.009 PNL=+7.89€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2476 IC=+0.009 PNL=+7.89€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1216 IC=+0.004 PNL=+51.79€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1216 IC=+0.004 PNL=+51.79€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=791 IC=+0.013 PNL=+36.93€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=791 IC=+0.013 PNL=+36.93€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.195 > 0.1 con n=3826 PNL=+2628.25€
  - _Datos_: n=3826 IC=+0.195 PNL=+2628.25€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2022 IC=+0.090 PNL=+487.79€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2022 IC=+0.090 PNL=+487.79€

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
  - _Estado_: n=841 IC=+0.041 PNL=+84.82€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=841 IC=+0.041 PNL=+84.82€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=93 IC=+0.037 PNL=+3.65€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=93 IC=+0.037 PNL=+3.65€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.252 n=139) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=139 IC=+0.252 PNL=+118.97€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.131 > 0.02 con n=841 PNL=+366.51€
  - _Datos_: n=841 IC=+0.131 PNL=+366.51€

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
  - _Estado_: n=24743 IC=+0.072 PNL=+3611.60€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=24743 IC=+0.072 PNL=+3611.60€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.135 < -0.1 con n=382 PNL=+48.61€
  - _Datos_: n=382 IC=-0.135 PNL=+48.61€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2793 IC=+0.066 PNL=+342.90€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2793 IC=+0.066 PNL=+342.90€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=119 IC=-0.103 PNL=+4.34€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=119 IC=-0.103 PNL=+4.34€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.1 con n=656 PNL=+176.54€
  - _Datos_: n=656 IC=+0.120 PNL=+176.54€

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
  - _Estado_: n=26330 IC=-0.137 PNL=+1830.01€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=26330 IC=-0.137 PNL=+1830.01€

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
  - _Estado_: n=2658 IC=+0.138 PNL=+1568.95€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2658 IC=+0.138 PNL=+1568.95€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=6766 IC=+0.045 PNL=+494.64€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6766 IC=+0.045 PNL=+494.64€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.088 > 0.08 con n=2936 PNL=+1539.74€
  - _Datos_: n=2936 IC=+0.088 PNL=+1539.74€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.224 < -0.1 con n=2699 PNL=-193.18€
  - _Datos_: n=2699 IC=-0.224 PNL=-193.18€

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
  - _Estado_: n=56 IC=-0.017 PNL=+5.60€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=56 IC=-0.017 PNL=+5.60€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.098 n=1515) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1515 IC=+0.098 PNL=+329.16€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=518) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=518 IC=+0.411 PNL=+740.25€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=11976 IC=+0.184 PNL=-1249.85€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=11976 IC=+0.184 PNL=-1249.85€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.211 > 0.1 con n=195 PNL=+122.72€
  - _Datos_: n=195 IC=+0.211 PNL=+122.72€
