# Hipótesis automáticas — 2026-10-08 13:56 UTC
_Generado por shadow_postmortem.py sobre 807535 resoluciones (PNL=+100287.04€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.209 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.120)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.200 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.120)

- **PATRÓN** `banda_hit_calibrado` > `0.6166` → IC=+0.236 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6166 (IC base=+0.120)

- **PATRÓN** `banda_z` > `8.976` → IC=+0.191 (n=228)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.976 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=721)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.120)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.229 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.124)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.207 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.124)

- **PATRÓN** `banda_hit_calibrado` > `0.8118` → IC=+0.259 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8118 (IC base=+0.124)

- **PATRÓN** `banda_z` > `9.568` → IC=+0.183 (n=184)

  - _Acción_: Kelly boost +0.91€ cuando `banda_z` > 9.568 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=623)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.124)

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
- **FILTRO** `restante_s_al_confirmar` < `144.04` → IC=-0.208 (n=8803)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.04
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=26409)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `131.25` → IC=-0.269 (n=1098)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.25
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3294)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `123.47` → IC=-0.305 (n=1022)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 123.47
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3068)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `165.19` → IC=-0.225 (n=2243)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 165.19
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=6731)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `130.87` → IC=-0.302 (n=1719)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.87
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=5159)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.207 (n=18307)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=3961)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `9526.5258` → IC=+0.183 (n=1763)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9526.5258 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.135 (n=15032)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=18458)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=13998)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=6507)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7522.082` → IC=+0.166 (n=2503)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 7522.082 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1914)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=1870)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2349)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `16090.8962` → IC=+0.211 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16090.8962 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.198 (n=1690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=1875)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=2405)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `16052.1822` → IC=+0.206 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16052.1822 (IC base=+0.193)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.122 (n=1063)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.555 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `4988.4492` → IC=+0.126 (n=228)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 4988.4492 (IC base=+0.087)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.090)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.138 (n=979)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.090)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=3563)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.364 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.231 (n=1586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.361 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=1839)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.222)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=760)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.250 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.134 (n=976)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `1324.629` → IC=+0.141 (n=847)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1324.629 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=842)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.409 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=1244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.289 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=818)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.147)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.181 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.376 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.223 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=15119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=12865)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.228 (n=6388)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=3552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=3364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.178 (n=3421)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.173)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=1544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.231 (n=1027)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.318 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.228)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=3483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=3331)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=3549)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.189 (n=1935)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.72 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=3052)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.331 (n=1063)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=3409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=2191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.189 (n=2593)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.71 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.198 (n=1215)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.430 (n=613)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=704)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `2776.9049` → IC=+0.433 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2776.9049 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.433 (n=268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.444 (n=178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `19769.7921` → IC=+0.444 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 19769.7921 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.440 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.434 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.427 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `3399.6895` → IC=+0.437 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3399.6895 (IC base=+0.427)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=45127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=19790)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.186 (n=7766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=6252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.199 (n=8612)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=4032)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.281 (n=2859)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.181 (n=8198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.177 (n=6242)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=8238)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=4066)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=2806)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=7487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.203 (n=5996)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=2936)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=3218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=3428)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=6939)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.125 (n=6446)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.2 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.137 (n=6771)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=8548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.45` → IC=+0.138 (n=6425)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.45 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=3447)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.122)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=3400)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=4234)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.122)

- **PATRÓN** `lag_apertura_s` < `3.08` → IC=+0.146 (n=3188)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.08 (IC base=+0.122)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=3492)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.131 (n=3704)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.135 (n=3249)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=1430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.290 (n=1410)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.379 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1549.9598` → IC=+0.293 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1549.9598 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.292 (n=639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.354 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `3833.5712` → IC=+0.293 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3833.5712 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.291 (n=676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.385 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1447.4658` → IC=+0.300 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1447.4658 (IC base=+0.286)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.444 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.448 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.461 (n=100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.449 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `2133.31` → IC=+0.458 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2133.31 (IC base=+0.442)

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
- **PATRÓN** `drift_60min` |x|≤ `0.3703` → IC=+0.135 (n=9521)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.3703 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9828` → IC=+0.242 (n=3607)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9828 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2195` → IC=+0.253 (n=2478)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2195 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.434` → IC=+0.192 (n=2817)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.434 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.249 (n=2024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8546 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.617` → IC=+0.254 (n=3036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.617 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.3017` → IC=+0.231 (n=1095)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3017 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.3246` → IC=+0.218 (n=3439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3246 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5625` → IC=+0.142 (n=13240)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5625 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.5778` → IC=+0.203 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5778 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.1504` → IC=+0.184 (n=4568)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1504 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `1.196` → IC=+0.183 (n=4914)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.196 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.054` → IC=+0.183 (n=2229)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.054 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.230 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.4483` → IC=+0.203 (n=8416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4483 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.218 (n=8232)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.073)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.219 (n=801)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.188 (n=802)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0079 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.2816` → IC=+0.185 (n=2114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.2816 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=1159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.184 (n=1613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 11.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.278 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.782` → IC=+0.294 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.782 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.238 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.182 (n=2274)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=2484)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `2010.22` → IC=+0.187 (n=1089)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2010.22 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.244 (n=1742)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.088` → IC=+0.267 (n=651)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.088 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0604` → IC=+0.281 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0604 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.526` → IC=+0.250 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.526 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.403` → IC=+0.239 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.403 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0946` → IC=+0.236 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0946 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.257 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6222` → IC=+0.255 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6222 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=2144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.235 (n=847)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1083` → IC=+0.253 (n=847)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1083 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=1926)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.3226` → IC=+0.233 (n=1922)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3226 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1954` → IC=+0.220 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1954 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.3461` → IC=+0.222 (n=1820)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3461 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.672` → IC=+0.260 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.672 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `1.2468` → IC=+0.220 (n=1923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2468 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.6193` → IC=+0.224 (n=1922)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6193 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.245 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7583` → IC=+0.218 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7583 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.4073` → IC=+0.237 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4073 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.178 (n=641)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0026 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.166 (n=642)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=730)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7206` → IC=+0.177 (n=1923)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7206 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.132` → IC=+0.156 (n=1769)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.132 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.254` → IC=+0.155 (n=308)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.254 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.3` → IC=+0.143 (n=1762)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.3 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1967` → IC=+0.147 (n=1923)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1967 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.6233` → IC=+0.138 (n=1923)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6233 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0963` → IC=+0.168 (n=697)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.0963 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.449` → IC=+0.149 (n=1809)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.449 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7828` → IC=+0.145 (n=1208)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7828 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.175 (n=762)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 229.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.202 (n=2435)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=2564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=2187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.391` → IC=+0.256 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.391 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0965` → IC=+0.194 (n=2140)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0965 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.3469` → IC=+0.195 (n=319)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3469 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.1515` → IC=+0.201 (n=1562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1515 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=2904)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.226 (n=1442)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.1316` → IC=+0.232 (n=721)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1316 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=1007)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.238 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.678` → IC=+0.257 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.678 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.599` → IC=+0.216 (n=2351)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.599 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.257 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.7154` → IC=+0.220 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7154 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.7169` → IC=+0.226 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7169 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.217 (n=1984)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.215)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=132)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=2906)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.147 (n=457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0036 (IC base=+0.043)

- **PATRÓN** `ibs_20min` > `0.9581` → IC=+0.217 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9581 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.1871` → IC=+0.323 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1871 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.981` → IC=+0.176 (n=958)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 4.981 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8538` → IC=+0.325 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8538 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `1.2251` → IC=+0.345 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2251 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.337 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.353 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.2083` → IC=+0.320 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2083 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.319 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.0965` → IC=+0.165 (n=760)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.0965 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `0.3038` → IC=+0.191 (n=335)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.3038 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.155 (n=815)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8504 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.211 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.5242` → IC=+0.167 (n=1044)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.5242 (IC base=+0.032)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.171 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=445)

- **FILTRO** `ibs_20min` < `0.3056` → IC=-0.189 (n=130)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3056
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=392)

- **FILTRO** `ibs_20min` > `0.2258` → IC=-0.125 (n=2945)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2258
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=1454)

- **FILTRO** `sigma_ewma_delta_pct` > `8.79` → IC=-0.223 (n=452)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.79
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3947)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.196 (n=179)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.8 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.9797` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9797 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.366` → IC=+0.134 (n=181)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.366 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.5788` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5788 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `1.0454` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0454 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.0757` → IC=+0.289 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0757 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.289 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.274 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.040)

- **PATRÓN** `ibs_20min` < `0.2258` → IC=+0.142 (n=1454)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.2258 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.2588` → IC=+0.275 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2588 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.7007` → IC=+0.280 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7007 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.299 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.371` → IC=+0.295 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.371 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6431` → IC=-0.184 (n=767)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6431
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=2304)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.209 (n=857)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2214)

- **FILTRO** `ibs_20min` > `0.7628` → IC=-0.206 (n=1142)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7628
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=3430)

- **PATRÓN** `dist_vwap_pct` > `0.4642` → IC=+0.317 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4642 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2041` → IC=+0.316 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2041 (IC base=-0.073)

- **PATRÓN** `volumen_regimen` < `0.9898` → IC=+0.298 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9898 (IC base=-0.073)

- **PATRÓN** `volumen_regimen` > `0.6482` → IC=+0.313 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6482 (IC base=-0.073)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.304 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=-0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.300 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.4802` → IC=+0.301 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4802 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.4401` → IC=+0.301 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4401 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` > `0.8193` → IC=+0.286 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8193 (IC base=-0.011)

- **PATRÓN** `volumen_regimen` > `1.0773` → IC=+0.278 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0773 (IC base=-0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.274 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` < `2.1667` → IC=+0.256 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1667 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` > `1.4259` → IC=+0.259 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4259 (IC base=-0.011)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.198 (n=4757)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0093 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4648` → IC=+0.186 (n=12739)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4648 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.6701` → IC=+0.283 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6701 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.689` → IC=+0.153 (n=6423)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.689 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.1739` → IC=+0.248 (n=5219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1739 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6905` → IC=+0.256 (n=4662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6905 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.260 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4647` → IC=+0.245 (n=2805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4647 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6328` → IC=+0.256 (n=2804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6328 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.278 (n=7962)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.167 (n=4601)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0089 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.5406` → IC=+0.160 (n=12146)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.5406 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.6837` → IC=+0.251 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6837 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.1974` → IC=+0.261 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1974 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.307 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `1.5867` → IC=+0.281 (n=2592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5867 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.284 (n=5788)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.076)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2567` → IC=-0.172 (n=995)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2567
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=2986)

- **FILTRO** `ibs_20min` > `0.7546` → IC=-0.176 (n=820)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7546
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=2464)

- **FILTRO** `sigma_ewma_delta_pct` > `4.624` → IC=-0.179 (n=726)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.624
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2558)

- **PATRÓN** `ibs_20min` > `0.9061` → IC=+0.274 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9061 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.323` → IC=+0.201 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.323 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2278` → IC=+0.280 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2278 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.4427` → IC=+0.215 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4427 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `2.2222` → IC=+0.241 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2222 (IC base=+0.038)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.235 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.038)

- **PATRÓN** `ibs_20min` < `0.1593` → IC=+0.153 (n=822)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1593 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0751` → IC=+0.420 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0751 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.6397` → IC=+0.412 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6397 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5399` → IC=+0.410 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5399 (IC base=-0.023)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.405 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8632` → IC=+0.153 (n=960)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.8632 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1169` → IC=+0.193 (n=711)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1169 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.6783` → IC=+0.181 (n=1217)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6783 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2745` → IC=+0.217 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2745 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.199 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.4155` → IC=+0.188 (n=446)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4155 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `225.0` → IC=+0.231 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 225.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.1603` → IC=+0.227 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1603 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.232 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` < `0.0728` → IC=+0.223 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0728 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.294 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.5463` → IC=+0.237 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5463 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1737` → IC=+0.238 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1737 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.272 (n=2144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.259 (n=2153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.254 (n=1919)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.299` → IC=+0.286 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.299 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.1318` → IC=+0.265 (n=1950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1318 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.165` → IC=+0.262 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.165 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2534)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.304 (n=1809)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.1824` → IC=+0.306 (n=796)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1824 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.322 (n=604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.3636` → IC=+0.293 (n=1810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3636 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.672` → IC=+0.303 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.672 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.754` → IC=+0.288 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.754 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` < `0.1934` → IC=+0.285 (n=1763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1934 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` > `0.3376` → IC=+0.296 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3376 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` < `1.7103` → IC=+0.303 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7103 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `2.624` → IC=+0.290 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.624 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.288 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.288)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7614` → IC=-0.179 (n=827)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7614
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=2486)

- **PATRÓN** `ibs_20min` > `0.8995` → IC=+0.165 (n=762)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8995 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.2191` → IC=+0.215 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2191 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.0103` → IC=+0.233 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0103 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1688` → IC=+0.225 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1688 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.226 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4079` → IC=+0.256 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4079 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.282 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1262` → IC=+0.220 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1262 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.224 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1951 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.279 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.8479` → IC=+0.264 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8479 (IC base=-0.000)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.252 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7632` → IC=-0.190 (n=1517)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7632
  - _Potencial_: sin este filtro IC_bueno=+0.286 (n=1519)

- **FILTRO** `ibs_20min` > `0.6667` → IC=-0.246 (n=750)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=2315)

- **FILTRO** `sigma_ewma_delta_pct` > `8.654` → IC=-0.234 (n=352)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.654
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=2713)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.286 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `1.0133` → IC=+0.334 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0133 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.7` → IC=+0.167 (n=476)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.7 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` < `0.8552` → IC=+0.315 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8552 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` > `0.6341` → IC=+0.306 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6341 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.303 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.2759` → IC=+0.333 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2759 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.7981` → IC=+0.317 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7981 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` > `2.4083` → IC=+0.303 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4083 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.331 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.5625` → IC=+0.134 (n=2032)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5625 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.2709` → IC=+0.242 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2709 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.7031` → IC=+0.262 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7031 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.236 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.255 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4243` → IC=+0.255 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4243 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.266 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.025)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.335 (n=1511)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.309 (n=801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.324 (n=1694)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2128` → IC=+0.319 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2128 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.776` → IC=+0.313 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.776 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.947` → IC=+0.292 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.947 (IC base=+0.291)

- **PATRÓN** `volumen_regimen` > `0.8567` → IC=+0.315 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8567 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.339 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` > `1.4334` → IC=+0.303 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4334 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `2982.5368` → IC=+0.307 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2982.5368 (IC base=+0.291)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.328 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.321 (n=1202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.1867` → IC=+0.290 (n=794)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1867 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.294 (n=1713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` < `0.3675` → IC=+0.315 (n=1802)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3675 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.3086` → IC=+0.293 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3086 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.513` → IC=+0.301 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.513 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.038` → IC=+0.291 (n=2152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.038 (IC base=+0.290)

- **PATRÓN** `volumen_regimen` < `0.8905` → IC=+0.290 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8905 (IC base=+0.290)

- **PATRÓN** `volumen_regimen` > `1.2273` → IC=+0.321 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2273 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.338 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` < `2.4496` → IC=+0.291 (n=1631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4496 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` > `2.1346` → IC=+0.290 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1346 (IC base=+0.290)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.187 (n=3511)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0047 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.210 (n=3511)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3506` → IC=+0.186 (n=9254)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3506 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=10991)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.5652` → IC=+0.228 (n=10519)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5652 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.17` → IC=+0.200 (n=4444)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.17 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.48` → IC=+0.250 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.48 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.2034` → IC=+0.167 (n=6995)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2034 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.629` → IC=+0.161 (n=6995)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.629 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2947` → IC=+0.195 (n=1554)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2947 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.4516` → IC=+0.174 (n=3384)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4516 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.6045` → IC=+0.183 (n=3385)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6045 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `2499.8902` → IC=+0.177 (n=7011)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2499.8902 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.190 (n=9444)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 104.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.190 (n=6768)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0066 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0812` → IC=+0.223 (n=3383)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0812 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=3806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.4839` → IC=+0.234 (n=10143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4839 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.28` → IC=+0.201 (n=1682)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.28 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1821` → IC=+0.167 (n=7261)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1821 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2913` → IC=+0.222 (n=1486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2913 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `1.5573` → IC=+0.177 (n=4149)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.5573 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6102` → IC=+0.180 (n=3143)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.6102 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.188 (n=9104)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 106.0 (IC base=+0.178)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.233 (n=590)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.207 (n=588)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3383` → IC=+0.221 (n=1763)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3383 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=1868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.204 (n=1181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.9174` → IC=+0.286 (n=1176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9174 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.335` → IC=+0.330 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.335 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.259 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.8192` → IC=+0.192 (n=1103)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.8192 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.2347` → IC=+0.205 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2347 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1835)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2013.07` → IC=+0.202 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2013.07 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.250 (n=1203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.250 (n=1219)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0699` → IC=+0.305 (n=455)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0699 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.246 (n=1221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=685)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.3503` → IC=+0.261 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3503 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.234` → IC=+0.248 (n=1481)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.234 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.241 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.277 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4266` → IC=+0.255 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4266 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.631` → IC=+0.246 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.631 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=1506)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.224 (n=530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1651` → IC=+0.185 (n=1059)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1651 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.178 (n=1590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.3778` → IC=+0.223 (n=1587)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3778 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.1993` → IC=+0.212 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1993 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.506` → IC=+0.234 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.506 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.168 (n=699)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6892 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.196 (n=251)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4133` → IC=+0.180 (n=517)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4133 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.4789` → IC=+0.156 (n=516)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.4789 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `11985.6464` → IC=+0.157 (n=1418)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 11985.6464 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.171 (n=666)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 233.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.164 (n=1680)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2331` → IC=+0.176 (n=1478)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2331 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.5923` → IC=+0.200 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5923 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.777` → IC=+0.207 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.777 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.165 (n=1680)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.204 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.2284` → IC=+0.147 (n=1736)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.2284 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.148 (n=510)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.485` → IC=+0.154 (n=1565)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.485 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7682` → IC=+0.145 (n=1043)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7682 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.169 (n=496)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 207.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.232 (n=587)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.4069` → IC=+0.219 (n=1548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4069 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.557` → IC=+0.279 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.557 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.0958` → IC=+0.207 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0958 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.1269` → IC=+0.210 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1269 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.7659` → IC=+0.210 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7659 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.6883` → IC=+0.213 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6883 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=2092)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `1975.3784` → IC=+0.225 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1975.3784 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.245 (n=1337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.145` → IC=+0.267 (n=668)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.145 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.278 (n=517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.3493` → IC=+0.252 (n=1517)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3493 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.649` → IC=+0.263 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.649 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.265 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.716` → IC=+0.244 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.716 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.7161` → IC=+0.235 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7161 (IC base=+0.229)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.231 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.229)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.179 (n=1489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0064 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0779` → IC=+0.197 (n=566)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0779 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.3293` → IC=+0.204 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3293 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1389` → IC=+0.187 (n=1073)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1389 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.002` → IC=+0.202 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.002 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.158 (n=1129)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.856 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1014` → IC=+0.167 (n=706)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1014 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.4307` → IC=+0.160 (n=553)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4307 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.154 (n=553)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `5106.3215` → IC=+0.192 (n=1128)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 5106.3215 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.149 (n=1635)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 150.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.163 (n=1572)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0061 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.3834` → IC=+0.151 (n=1785)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3834 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.6687` → IC=+0.187 (n=1785)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6687 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.853` → IC=+0.164 (n=614)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.853 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8568` → IC=+0.164 (n=1190)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8568 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.193 (n=272)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.8112` → IC=+0.142 (n=1105)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.8112 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.135 (n=1656)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.42 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4540.0942` → IC=+0.169 (n=1190)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4540.0942 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.130 (n=1597)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 148.0 (IC base=+0.132)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.160 (n=872)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0098 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4413` → IC=+0.130 (n=1692)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4413 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=1968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.215 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1977` → IC=+0.185 (n=1162)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1977 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.935` → IC=+0.262 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.935 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.141 (n=1923)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2036 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.1641` → IC=+0.136 (n=1942)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1641 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.549` → IC=+0.141 (n=819)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.549 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4868` → IC=+0.133 (n=620)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4868 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2017)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2388.9978` → IC=+0.188 (n=1282)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2388.9978 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.148 (n=1520)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 45.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.143 (n=1712)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0091 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.1053` → IC=+0.180 (n=648)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.1053 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1963)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.5741` → IC=+0.222 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5741 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.362` → IC=+0.132 (n=588)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 5.362 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.591` → IC=+0.127 (n=1712)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 2.591 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.1845` → IC=+0.137 (n=1943)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.1845 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.164 (n=245)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.4517` → IC=+0.144 (n=596)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4517 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.8156` → IC=+0.130 (n=1191)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.8156 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2793.6768` → IC=+0.187 (n=881)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2793.6768 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.136 (n=1754)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 52.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.234 (n=1602)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2855` → IC=+0.221 (n=1196)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2855 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=1868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.216 (n=1214)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.248 (n=1795)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.1958` → IC=+0.215 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1958 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.2838` → IC=+0.212 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2838 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.6` → IC=+0.244 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.6 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `1.183` → IC=+0.215 (n=1794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.183 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.6232` → IC=+0.219 (n=1794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6232 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.271 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `2.4727` → IC=+0.215 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4727 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4264` → IC=+0.219 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4264 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2657.7026` → IC=+0.221 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2657.7026 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.230 (n=816)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.219)

- **PATRÓN** `sigma_h` > `0.0223` → IC=+0.222 (n=843)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0223 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.244 (n=619)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.237 (n=904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.02` → IC=+0.290 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.02 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `1.1598` → IC=+0.234 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1598 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.425` → IC=+0.248 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.425 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6367` → IC=+0.230 (n=1854)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6367 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.278 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `2.1966` → IC=+0.213 (n=1502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1966 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `1.4377` → IC=+0.220 (n=1707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4377 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `2631.9668` → IC=+0.228 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2631.9668 (IC base=+0.219)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.191 (n=1219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0041 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.167 (n=920)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0083 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3332` → IC=+0.178 (n=2427)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3332 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.204 (n=1364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.3274` → IC=+0.196 (n=2758)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3274 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.774` → IC=+0.184 (n=429)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.774 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.76` → IC=+0.192 (n=1182)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.76 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.8679` → IC=+0.185 (n=1652)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8679 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `1.2036` → IC=+0.177 (n=827)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.2036 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.1025` → IC=+0.176 (n=991)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1025 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.4378` → IC=+0.184 (n=893)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4378 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.522` → IC=+0.169 (n=893)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.522 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=2551)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.185 (n=2540)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 150.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.163 (n=951)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0036 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.3328` → IC=+0.123 (n=2499)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.3328 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=2683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.0731` → IC=+0.199 (n=947)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.0731 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.2213` → IC=+0.120 (n=2582)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.2213 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.126 (n=1086)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4373` → IC=+0.149 (n=920)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4373 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `5216.0045` → IC=+0.142 (n=1893)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 5216.0045 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.133 (n=925)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 21.0 (IC base=+0.114)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.201 (n=353)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1011` → IC=+0.201 (n=352)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1011 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.186 (n=733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.6268` → IC=+0.206 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6268 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.3081` → IC=+0.173 (n=249)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.3081 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.173 (n=337)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.865` → IC=+0.151 (n=849)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.865 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.0899` → IC=+0.167 (n=703)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.0899 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.0702` → IC=+0.156 (n=315)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0702 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.211` → IC=+0.161 (n=686)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.211 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.4162` → IC=+0.151 (n=780)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4162 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `14715.6452` → IC=+0.157 (n=532)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 14715.6452 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.201 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.204 (n=312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.2658` → IC=+0.165 (n=824)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2658 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.153 (n=842)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.147 (n=948)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.611` → IC=+0.184 (n=824)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.611 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.75` → IC=+0.148 (n=180)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.75 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.48` → IC=+0.148 (n=986)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.48 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.208` → IC=+0.148 (n=936)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.208 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `0.7022` → IC=+0.158 (n=836)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7022 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.197 (n=249)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.1137` → IC=+0.162 (n=814)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1137 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.4012` → IC=+0.149 (n=925)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4012 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=1212)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `287.0` → IC=+0.161 (n=795)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 287.0 (IC base=+0.146)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.232 (n=587)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.2048` → IC=+0.210 (n=585)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2048 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=922)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.251 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.3573` → IC=+0.205 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3573 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.2075` → IC=+0.199 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2075 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.05` → IC=+0.219 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.05 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `0.8392` → IC=+0.197 (n=585)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8392 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` > `1.1824` → IC=+0.219 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1824 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.16` → IC=+0.227 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.16 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `1.4188` → IC=+0.225 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4188 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.4505` → IC=+0.215 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4505 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.137 (n=742)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.006 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.096` → IC=+0.134 (n=282)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.096 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.0868` → IC=+0.164 (n=281)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.0868 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.411` → IC=+0.149 (n=220)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 6.411 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.6877` → IC=+0.155 (n=372)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6877 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.146 (n=272)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `7713.0144` → IC=+0.148 (n=561)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 7713.0144 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.136 (n=352)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 41.0 (IC base=+0.111)

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
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.179 (n=4556)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.213 (n=4560)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=14300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.4537` → IC=+0.224 (n=13665)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4537 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1648` → IC=+0.187 (n=5042)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1648 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.434` → IC=+0.246 (n=3363)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.434 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.2323` → IC=+0.166 (n=9163)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2323 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2894` → IC=+0.200 (n=1846)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2894 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.5988` → IC=+0.195 (n=4410)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5988 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2463.1153` → IC=+0.180 (n=9109)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2463.1153 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.203 (n=10862)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.196 (n=5452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.1464` → IC=+0.198 (n=5439)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1464 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=4629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.45` → IC=+0.251 (n=10883)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.45 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.107` → IC=+0.213 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.107 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.727` → IC=+0.188 (n=11925)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.727 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `1.0605` → IC=+0.162 (n=7361)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.0605 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.251 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.2632` → IC=+0.195 (n=5250)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.2632 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.210 (n=7586)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.253 (n=755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.227 (n=753)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=1088)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=1525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.777` → IC=+0.348 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.777 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.272 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.589` → IC=+0.225 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.589 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2320)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2008.5202` → IC=+0.218 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2008.5202 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.266 (n=1257)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.264 (n=1685)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.2042` → IC=+0.273 (n=1256)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2042 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=1708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.3579` → IC=+0.285 (n=1657)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3579 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.314` → IC=+0.267 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.314 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2846` → IC=+0.285 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2846 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `2.6325` → IC=+0.282 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6325 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=2074)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.260)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.203 (n=739)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1783` → IC=+0.166 (n=1467)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1783 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.2741` → IC=+0.206 (n=2199)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2741 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1309` → IC=+0.186 (n=1196)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1309 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.715` → IC=+0.171 (n=369)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.715 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.221` → IC=+0.153 (n=2011)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.221 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6277` → IC=+0.175 (n=734)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6277 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.190 (n=314)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1425` → IC=+0.159 (n=1885)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1425 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5231` → IC=+0.154 (n=1913)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5231 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `273.0` → IC=+0.182 (n=913)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 273.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1829)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2557` → IC=+0.165 (n=1608)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2557 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6836` → IC=+0.195 (n=1828)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6836 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1344` → IC=+0.166 (n=1694)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1344 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.518` → IC=+0.167 (n=310)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.518 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.315` → IC=+0.147 (n=1654)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.315 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.186` → IC=+0.159 (n=1828)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.186 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1542` → IC=+0.202 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1542 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.432` → IC=+0.154 (n=1726)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.432 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7751` → IC=+0.161 (n=1150)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7751 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `256.0` → IC=+0.147 (n=545)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 256.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.232 (n=2244)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2019)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.512` → IC=+0.306 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.512 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.2043` → IC=+0.226 (n=2271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2043 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.7627` → IC=+0.229 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7627 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2672)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.242 (n=1413)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1832` → IC=+0.255 (n=931)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1832 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.239 (n=764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0152` → IC=+0.304 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0152 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.987` → IC=+0.289 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.987 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3416` → IC=+0.297 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3416 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7145` → IC=+0.245 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7145 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.1269` → IC=+0.242 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1269 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.259 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.237)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=1031)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3325` → IC=+0.152 (n=2058)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3325 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2662` → IC=+0.191 (n=2338)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2662 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.139` → IC=+0.157 (n=1288)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.139 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.181` → IC=+0.151 (n=954)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.181 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8732` → IC=+0.162 (n=1559)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8732 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1662` → IC=+0.171 (n=615)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1662 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5248` → IC=+0.163 (n=1002)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5248 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1799` → IC=+0.150 (n=1032)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1799 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7316.6924` → IC=+0.234 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7316.6924 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.178 (n=753)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 70.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.196 (n=632)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0033 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.345` → IC=+0.146 (n=1661)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.345 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.137 (n=661)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.188 (n=1888)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.7333 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.332` → IC=+0.179 (n=384)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.332 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8747` → IC=+0.143 (n=1259)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8747 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2971` → IC=+0.235 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2971 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4416` → IC=+0.145 (n=1812)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4416 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `5601.6515` → IC=+0.196 (n=856)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 5601.6515 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.137 (n=1812)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 165.0 (IC base=+0.134)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.136 (n=2359)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0055 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.4521` → IC=+0.201 (n=2354)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4521 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `1.0154` → IC=+0.212 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0154 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.067` → IC=+0.256 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.067 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2342` → IC=+0.140 (n=2354)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2342 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1615` → IC=+0.130 (n=2429)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1615 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.1954` → IC=+0.140 (n=1039)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.1954 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2406)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2578.4685` → IC=+0.236 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2578.4685 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.148 (n=743)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 27.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.159 (n=1504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0077 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.1305` → IC=+0.171 (n=752)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1305 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.236 (n=1999)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.217` → IC=+0.143 (n=1899)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.217 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.271` → IC=+0.128 (n=310)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 9.271 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.468` → IC=+0.137 (n=2178)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.468 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.7137` → IC=+0.158 (n=992)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7137 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.223` → IC=+0.186 (n=367)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.223 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.1541` → IC=+0.143 (n=1835)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1541 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2828.6558` → IC=+0.204 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2828.6558 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.144 (n=1839)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 50.0 (IC base=+0.126)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.236 (n=2271)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=2378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.225 (n=1646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.266 (n=2036)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.2066` → IC=+0.236 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2066 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.765` → IC=+0.265 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.765 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.2332` → IC=+0.225 (n=2272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2332 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6415` → IC=+0.224 (n=2272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6415 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.243 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.5127` → IC=+0.246 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5127 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=2079)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `2664.8726` → IC=+0.231 (n=1514)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2664.8726 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.221 (n=800)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.233 (n=1087)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.231 (n=1697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.416` → IC=+0.267 (n=2109)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.416 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.95` → IC=+0.258 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.95 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.247 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.286 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.4316` → IC=+0.219 (n=2204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4316 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.210 (n=2135)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.218)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=4057)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.231 (n=1373)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.4977` → IC=+0.202 (n=4112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4977 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.194 (n=4327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 4.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.194 (n=1853)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.9401` → IC=+0.241 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9401 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.1705` → IC=+0.197 (n=1512)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1705 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.238` → IC=+0.217 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.238 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.202 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` > `1.2543` → IC=+0.196 (n=963)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.2543 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.1685` → IC=+0.218 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1685 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.197 (n=1351)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `1.8616` → IC=+0.197 (n=2701)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.8616 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=3080)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `3858.5308` → IC=+0.204 (n=2741)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3858.5308 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.221 (n=1021)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.4847` → IC=+0.188 (n=3055)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.4847 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=1043)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=1389)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.173` → IC=+0.196 (n=1344)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.173 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.6448` → IC=+0.180 (n=536)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6448 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.169` → IC=+0.179 (n=3048)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.169 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.2516` → IC=+0.177 (n=2872)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.2516 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.176 (n=2790)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.179 (n=1389)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.5396` → IC=+0.177 (n=1326)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.5396 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `1.825` → IC=+0.183 (n=2008)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.825 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=4057)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.186 (n=1338)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 37.0 (IC base=+0.172)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.239 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.260 (n=177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=529)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.5153` → IC=+0.235 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5153 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.7702` → IC=+0.215 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7702 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.1783` → IC=+0.215 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1783 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.039` → IC=+0.233 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.039 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.529` → IC=+0.214 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.529 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.221 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.8402` → IC=+0.227 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8402 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.232 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `12537.6672` → IC=+0.237 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12537.6672 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.228 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1125` → IC=+0.179 (n=468)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1125 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.198 (n=356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 4.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.144` → IC=+0.183 (n=468)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.144 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.6071` → IC=+0.153 (n=482)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6071 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6648` → IC=+0.176 (n=103)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.6648 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.3474` → IC=+0.152 (n=1161)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.3474 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.385` → IC=+0.166 (n=1047)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.385 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.188 (n=709)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8812 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2218` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2218 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.5397` → IC=+0.154 (n=1060)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5397 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.170 (n=706)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `11531.9522` → IC=+0.161 (n=1063)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11531.9522 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.160 (n=1019)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 701.0 (IC base=+0.148)

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
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.211 (n=1091)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.458` → IC=+0.208 (n=1240)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.458 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.201 (n=1283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.5182` → IC=+0.215 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5182 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.8799` → IC=+0.204 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8799 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.152` → IC=+0.206 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.152 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.7064` → IC=+0.204 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7064 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `1.2467` → IC=+0.206 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2467 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.198 (n=1142)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.211 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.424` → IC=+0.215 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.424 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.233 (n=331)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.4923` → IC=+0.195 (n=988)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4923 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.187 (n=388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 16.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.181 (n=666)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 10.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.7466` → IC=+0.178 (n=988)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7466 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.0837` → IC=+0.172 (n=987)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.0837 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.6317` → IC=+0.194 (n=194)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6317 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.748` → IC=+0.175 (n=1010)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 6.748 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.2516` → IC=+0.184 (n=988)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.2516 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.7236` → IC=+0.172 (n=882)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.7236 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.193 (n=415)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.1885` → IC=+0.186 (n=851)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.1885 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `7437.397` → IC=+0.187 (n=987)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7437.397 (IC base=+0.171)

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
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.154 (n=591)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0038 (IC base=+0.074)

- **PATRÓN** `ibs_20min` > `0.4255` → IC=+0.147 (n=1242)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.4255 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.1427` → IC=+0.140 (n=664)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1427 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.471` → IC=+0.181 (n=280)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.471 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.180 (n=173)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.074)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.143 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0029 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.1923` → IC=+0.263 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1923 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` < `0.1231` → IC=+0.132 (n=569)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1231 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.1466` → IC=+0.193 (n=135)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1466 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `2.5724` → IC=+0.139 (n=485)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5724 (IC base=+0.058)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.137 (n=455)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0057 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.139 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 18.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.5664` → IC=+0.193 (n=379)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.5664 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.161 (n=219)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.092)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.121 (n=249)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0045 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.0582` → IC=+0.293 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0582 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.2051` → IC=+0.129 (n=289)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.2051 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.179` → IC=+0.143 (n=253)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 7.179 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` < `2.5091` → IC=+0.137 (n=235)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5091 (IC base=+0.079)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.147 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0046 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.124 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.6839` → IC=+0.199 (n=363)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.6839 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.123` → IC=+0.174 (n=219)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.123 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.447` → IC=+0.274 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.447 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `1179.3386` → IC=+0.140 (n=359)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1179.3386 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.0162` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0162 (IC base=+0.013)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.243` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.243 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.4509` → IC=+0.129 (n=60)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4509 (IC base=+0.013)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.01` → IC=-0.202 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=168)

- **FILTRO** `ibs_20min` > `0.16` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` > 0.16
  - _Potencial_: sin este filtro IC_bueno=+0.270 (n=137)

- **PATRÓN** `ibs_20min` > `0.76` → IC=+0.172 (n=275)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.76 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7176` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.7176 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.042)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.175 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0081 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.16` → IC=+0.270 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.16 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.949` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.949 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `0.6578` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.6578 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` > `0.9765` → IC=+0.172 (n=62)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.9765 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.1474` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1474 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.18` → IC=+0.189 (n=101)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.18 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.4839` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4839 (IC base=+0.069)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.205 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.069)

- **PATRÓN** `libro_liquidez` > `774.2903` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 774.2903 (IC base=+0.069)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1826` → IC=-0.306 (n=65)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1826
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=196)

- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=247)

- **FILTRO** `volumen_regimen` < `0.7446` → IC=-0.336 (n=65)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7446
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=198)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.379 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=171)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.297 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=160)

- **FILTRO** `dist_vwap_pct` > `0.3287` → IC=-0.389 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3287
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=193)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=197)

- **FILTRO** `volumen_pendiente_norm` > `0.0718` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=122)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=66)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.233 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=59)

- **FILTRO** `volumen_spike_ratio` > `3.7991` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.7991
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=49)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.308 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=74)

- **FILTRO** `sigma_ewma_delta_pct` > `2.402` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.402
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=66)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=74)

- **FILTRO** `volumen_regimen` < `0.5547` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.5547
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=74)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0026` → IC=-0.370 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=66)

- **FILTRO** `ibs_20min` < `0.6002` → IC=-0.467 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6002
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=59)

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

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.9508 (IC base=-0.152)

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
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.174 (n=188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0057 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.128 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.6599` → IC=+0.136 (n=413)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.6599 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.4822` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.4822 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` < `0.8586` → IC=+0.122 (n=276)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.8586 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` < `1.5367` → IC=+0.162 (n=137)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5367 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.1558` → IC=+0.174 (n=403)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1558 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.339` → IC=+0.217 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.339 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.083)

- **PATRÓN** `libro_liquidez` > `1320.3512` → IC=+0.122 (n=458)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1320.3512 (IC base=+0.083)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6472` → IC=-0.267 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6472
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=126)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.229 (n=94)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.004 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.158 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.1381` → IC=+0.211 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1381 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.265` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 10.265 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.879` → IC=+0.177 (n=165)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 4.879 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.178 (n=206)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6226 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.1895` → IC=+0.184 (n=175)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1895 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.2899` → IC=+0.186 (n=154)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.2899 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.176 (n=174)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.156)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.0817` → IC=-0.141 (n=37)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0817
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=107)

- **PATRÓN** `volumen_spike_ratio` < `1.8069` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8069 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.2038` → IC=+0.158 (n=147)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.2038 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.061` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.061 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.071)

- **PATRÓN** `libro_liquidez` > `2391.6339` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2391.6339 (IC base=+0.071)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.1679` → IC=-0.207 (n=56)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1679
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=58)

- **FILTRO** `dist_vwap_pct` > `0.2725` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2725
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=92)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.286 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.262 (n=141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.248 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.6388` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6388 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` < `0.1413` → IC=+0.241 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1413 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.365` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.365 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `1.0151` → IC=+0.272 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0151 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.2519` → IC=+0.289 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2519 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.415` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.415 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1062` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1062 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.237 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.069)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4923` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4923 (IC base=+0.291)

- **PATRÓN** `elapsed_s` > `189.2` → IC=+0.363 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 189.2 (IC base=+0.291)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.367 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.291)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.291)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3408` → IC=+0.236 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3408 (IC base=+0.210)

- **PATRÓN** `elapsed_s` > `184.2` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.2 (IC base=+0.210)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.210)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.278 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.210)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `1814.0` → IC=+0.274 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1814.0 (IC base=+0.210)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4923` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4923 (IC base=+0.291)

- **PATRÓN** `elapsed_s` > `189.2` → IC=+0.363 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 189.2 (IC base=+0.291)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.367 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.291)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.291)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3408` → IC=+0.236 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3408 (IC base=+0.210)

- **PATRÓN** `elapsed_s` > `184.2` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.2 (IC base=+0.210)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.210)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.278 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.210)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `1814.0` → IC=+0.274 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1814.0 (IC base=+0.210)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=1020)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2869.517` → IC=+0.129 (n=475)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2869.517 (IC base=+0.101)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=1020)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2869.517` → IC=+0.129 (n=475)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2869.517 (IC base=+0.101)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=156)

- **FILTRO** `libro_liquidez` < `10545.7403` → IC=-0.178 (n=113)

  - _Acción_: SKIP cuando `libro_liquidez` < 10545.7403
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=59)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=246)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=232)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=54)

- **FILTRO** `hora_utc` < `3.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=58)

- **FILTRO** `libro_liquidez` < `10893.2451` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 10893.2451
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=56)

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
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2858)

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
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=114)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.130 (n=98)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 13.0 (IC base=+0.048)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.132 (n=180)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.495 (IC base=+0.036)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=1064)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1018)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=657)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=355)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=336)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.146 (n=125)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.495 (IC base=+0.017)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=777)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=777)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=611)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=589)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=589)

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
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=146)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=170)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=170)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=303)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=303)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=212)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.125 (n=1402)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1494)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.139 (n=624)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.47 (IC base=+0.018)

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
- **FILTRO** `py_entrada` < `0.5` → IC=-0.144 (n=186)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=98)

- **PATRÓN** `py_entrada` < `0.48` → IC=+0.128 (n=119)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.48 (IC base=+0.016)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.222 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.050)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.56` → IC=-0.126 (n=137)

  - _Acción_: SKIP cuando `py_entrada` < 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=47)

- **FILTRO** `restante_min` < `8.94` → IC=-0.167 (n=46)

  - _Acción_: SKIP cuando `restante_min` < 8.94
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=138)

- **FILTRO** `lag_apertura_s` > `369.74` → IC=-0.160 (n=45)

  - _Acción_: SKIP cuando `lag_apertura_s` > 369.74
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=139)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.155 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=101)

- **FILTRO** `restante_min` < `3.7` → IC=-0.132 (n=93)

  - _Acción_: SKIP cuando `restante_min` < 3.7
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=93)

- **FILTRO** `lag_apertura_s` > `79.45` → IC=-0.138 (n=92)

  - _Acción_: SKIP cuando `lag_apertura_s` > 79.45
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=94)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.149 (n=192)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=66)

- **FILTRO** `profundidad_ratio` < `36.4` → IC=-0.197 (n=64)

  - _Acción_: SKIP cuando `profundidad_ratio` < 36.4
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=194)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.229 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=192)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.46 (IC base=-0.013)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.130 (n=209)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=120)

- **FILTRO** `restante_min` < `3.32` → IC=-0.182 (n=108)

  - _Acción_: SKIP cuando `restante_min` < 3.32
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=221)

- **FILTRO** `lag_apertura_s` > `99.42` → IC=-0.190 (n=111)

  - _Acción_: SKIP cuando `lag_apertura_s` > 99.42
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=218)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=197)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.124 (n=91)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.5 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.131 (n=201)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=105)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.126 (n=105)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=-0.042)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.196 (n=90)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=291)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.170 (n=4626)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=15005)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.166 (n=5047)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=15330)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.194 (n=848)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=2646)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.151 (n=855)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=2800)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.121 (n=1694)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.174 (n=707)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2235)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.177 (n=881)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=2666)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=918)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=2777)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.163 (n=843)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=2658)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2554)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=3294)

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
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=310)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=381)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `2022.006` → IC=-0.165 (n=338)

  - _Acción_: SKIP cuando `libro_liquidez` < 2022.006
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=688)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=13680)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=30437)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=10434)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=33683)

- **FILTRO** `ibs_7min` < `0.2545` → IC=-0.234 (n=11029)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2545
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=33088)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.155 (n=14805)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=29312)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.236 (n=13491)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=42680)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.178 (n=14017)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=42154)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=2215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=5284)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=1799)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=5700)

- **FILTRO** `ibs_7min` < `0.7078` → IC=-0.251 (n=2474)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7078
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=5025)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.190 (n=1584)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5915)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.268 (n=2372)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=7391)

- **FILTRO** `ibs_7min` > `0.7778` → IC=-0.210 (n=2440)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=7323)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.132 (n=1796)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=5742)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.247 (n=1866)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=5672)

- **FILTRO** `ibs_7min` < `0.7391` → IC=-0.197 (n=1884)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7391
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5654)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.183 (n=1884)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=5654)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=1822)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5844)

- **FILTRO** `ibs_7min` > `0.2648` → IC=-0.191 (n=1916)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2648
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5750)

- **FILTRO** `ballena_activa_n` > `148.0` → IC=-0.189 (n=1904)

  - _Acción_: SKIP cuando `ballena_activa_n` > 148.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5762)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.163 (n=2033)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=5134)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=1703)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5464)

- **FILTRO** `ibs_7min` < `0.703` → IC=-0.247 (n=2364)

  - _Acción_: SKIP cuando `ibs_7min` < 0.703
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=4803)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.220 (n=1598)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5569)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.244 (n=2335)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=8036)

- **FILTRO** `ibs_7min` > `0.7342` → IC=-0.172 (n=2591)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=7780)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=2358)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=4897)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.241 (n=2163)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=5092)

- **FILTRO** `ibs_7min` < `0.7381` → IC=-0.185 (n=1813)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7381
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5442)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.186 (n=1783)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5472)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.270 (n=1834)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=5650)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.180 (n=1869)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5615)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.183 (n=1797)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5687)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.272 (n=1753)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5674)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.233 (n=1849)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=5578)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.174 (n=2667)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=8043)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.281 (n=1737)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=5494)

- **FILTRO** `ibs_7min` < `0.24` → IC=-0.225 (n=1805)

  - _Acción_: SKIP cuando `ibs_7min` < 0.24
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5426)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.203 (n=1755)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5476)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.207 (n=2469)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=7708)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.153 (n=295)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=964)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1244)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=49)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=617)

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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=359)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.143 (n=155)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=306)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=413)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=596)

- **FILTRO** `libro_liquidez` < `3306.2556` → IC=-0.155 (n=166)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.2556
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=498)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=262)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.142 (n=967)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.140 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.130 (n=360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 4.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `443.866` → IC=+0.159 (n=323)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 443.866 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `4352.1298` → IC=+0.131 (n=323)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 4352.1298 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.148 (n=316)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 14.0 (IC base=+0.128)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4374` → IC=+0.162 (n=75)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4374 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.234 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2661.4728` → IC=+0.240 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2661.4728 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.205 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.148)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 10.0 (IC base=+0.107)

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
- **PATRÓN** `delta_ratio` |x|> `0.4337` → IC=+0.237 (n=78)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4337 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.233 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.154)

- **PATRÓN** `total_vol_5m` < `8043.774` → IC=+0.172 (n=172)

  - _Acción_: Kelly boost +0.86€ cuando `total_vol_5m` < 8043.774 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 28.0 (IC base=+0.154)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4006` → IC=+0.141 (n=168)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.4006 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.125 (n=166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 13.0 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=115)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3657.1308` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3657.1308 (IC base=+0.100)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.6961` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.6961
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=122)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.273 (n=271)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=272)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0049` → IC=-0.234 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0049
  - _Potencial_: sin este filtro IC_bueno=+0.264 (n=53)

- **FILTRO** `T_h` > `88.6373` → IC=-0.378 (n=39)

  - _Acción_: SKIP cuando `T_h` > 88.6373
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=121)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.264 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.068)

- **PATRÓN** `pct_vs_K` |x|≤ `1.73` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `pct_vs_K` |x|≤ 1.73 (IC base=-0.068)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `8.3214` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.3214
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.176 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=33)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.193 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=124)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.317 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=322)

- **FILTRO** `pct_vs_K` |x|> `3.4531` → IC=-0.445 (n=107)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4531
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=322)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `79.3043` → IC=-0.152 (n=113)

  - _Acción_: SKIP cuando `T_h` > 79.3043
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=57)

- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.384 (n=41)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=129)

- **FILTRO** `T_h` > `73.6519` → IC=-0.292 (n=118)

  - _Acción_: SKIP cuando `T_h` > 73.6519
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=40)

- **FILTRO** `pct_vs_K` |x|> `2.8429` → IC=-0.424 (n=51)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8429
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=107)

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
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.272 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=47)

- **FILTRO** `T_h` > `135.9851` → IC=-0.250 (n=34)

  - _Acción_: SKIP cuando `T_h` > 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=103)

- **FILTRO** `pct_vs_K` |x|> `3.3525` → IC=-0.457 (n=44)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3525
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=86)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.008` → IC=-0.188 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=92)

- **FILTRO** `T_h` > `113.7599` → IC=-0.177 (n=60)

  - _Acción_: SKIP cuando `T_h` > 113.7599
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=62)

- **FILTRO** `T_h` > `37.9805` → IC=-0.381 (n=65)

  - _Acción_: SKIP cuando `T_h` > 37.9805
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=22)

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

- **PATRÓN** `edge` > `0.095` → IC=+0.458 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.095 (IC base=+0.424)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.453 (n=126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.424)

- **PATRÓN** `T_h` < `1.014` → IC=+0.430 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.014 (IC base=+0.424)

- **PATRÓN** `T_h` > `1.3596` → IC=+0.454 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.3596 (IC base=+0.424)

- **PATRÓN** `dist_50` > `0.3938` → IC=+0.479 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3938 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.424)

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

- **PATRÓN** `sigma_h` < `0.0161` → IC=+0.461 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0161 (IC base=+0.441)

- **PATRÓN** `T_h` > `0.801` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.801 (IC base=+0.441)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.460 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.441)

- **PATRÓN** `edge` > `0.114` → IC=+0.474 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.114 (IC base=+0.467)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.484 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.467)

- **PATRÓN** `T_h` > `0.77` → IC=+0.469 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.77 (IC base=+0.467)

- **PATRÓN** `dist_50` > `0.4568` → IC=+0.492 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4568 (IC base=+0.467)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.467)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=256)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=341)

- **PATRÓN** `streak_estiramiento` < `0.4547` → IC=+0.125 (n=86)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.4547 (IC base=+0.020)

- **PATRÓN** `streak_estiramiento` < `0.5687` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.5687 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `2505.47` → IC=+0.127 (n=124)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2505.47 (IC base=+0.038)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=25)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.479` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.479
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=58)

- **FILTRO** `ballena_activa_n` > `51.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 51.0
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=62)

- **PATRÓN** `volumen_racha` < `982893.6` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_racha` < 982893.6 (IC base=+0.018)

- **PATRÓN** `streak_estiramiento` < `0.4177` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.4177 (IC base=+0.018)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.136 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 10.0 (IC base=+0.079)

- **PATRÓN** `streak_estiramiento` < `0.3368` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.3368 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.144 (n=102)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 47.0 (IC base=+0.079)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=600)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=827)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1320)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=971)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=980)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3514)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1864)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.201 (n=873)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.231 (n=872)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.1604` → IC=+0.202 (n=2303)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1604 (IC base=+0.193)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2233` → IC=+0.196 (n=874)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.2233 (IC base=+0.193)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1312` → IC=+0.213 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1312 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.202 (n=2419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=2710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_15` > `0.6032` → IC=+0.269 (n=2616)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6032 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.1201` → IC=+0.194 (n=1241)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1201 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.899` → IC=+0.271 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.899 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `6925.4045` → IC=+0.198 (n=872)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6925.4045 (IC base=+0.193)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=1111)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.225 (n=500)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.275 (n=167)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.214)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1462` → IC=+0.237 (n=333)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1462 (IC base=+0.214)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.245 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `ibs_15` > `0.7143` → IC=+0.279 (n=500)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7143 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.1369` → IC=+0.247 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1369 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.267 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `16201.6469` → IC=+0.246 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16201.6469 (IC base=+0.214)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.513` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.513
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=642)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.5728` → IC=-0.161 (n=184)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5728
  - _Potencial_: sin este filtro IC_bueno=+0.232 (n=553)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.168 (n=185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0034 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.150 (n=244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2368` → IC=+0.154 (n=186)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.2368 (IC base=+0.133)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.128` → IC=+0.149 (n=212)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.128 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.137 (n=579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.5728` → IC=+0.232 (n=553)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5728 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.1536` → IC=+0.139 (n=297)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1536 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.901` → IC=+0.259 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.901 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `3507.1457` → IC=+0.139 (n=494)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3507.1457 (IC base=+0.133)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `20.507` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.507
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=224)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.152 (n=185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0055 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.211 (n=140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1804` → IC=+0.194 (n=370)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1804 (IC base=+0.148)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0629` → IC=+0.159 (n=420)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.0629 (IC base=+0.148)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3429` → IC=+0.176 (n=372)

  - _Acción_: Kelly boost +0.88€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3429 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.167 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.9296` → IC=+0.352 (n=140)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9296 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1845` → IC=+0.155 (n=375)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1845 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.221 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=269)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2568.7783` → IC=+0.149 (n=420)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2568.7783 (IC base=+0.148)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.027)

- **PATRÓN** `libro_liquidez` > `3350.0472` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3350.0472 (IC base=+0.027)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.258 (n=556)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0805` → IC=+0.218 (n=275)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0805 (IC base=+0.215)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0442` → IC=+0.218 (n=623)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0442 (IC base=+0.215)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.268 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.229 (n=552)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.215)

- **PATRÓN** `ibs_15` > `0.5849` → IC=+0.295 (n=622)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5849 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.1332` → IC=+0.224 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1332 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.758` → IC=+0.250 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.758 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.489` → IC=+0.215 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.489 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2968.5394` → IC=+0.305 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2968.5394 (IC base=+0.215)

- **PATRÓN** `ibs_15` < `0.1091` → IC=+0.158 (n=667)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1091 (IC base=+0.069)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.364 (n=358)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.359)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.379 (n=179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.359)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.359 (n=359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.359)

- **PATRÓN** `drift_15min` |x|≤ `0.4034` → IC=+0.362 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4034 (IC base=+0.359)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.383 (n=357)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.359)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.391 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.359)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.375 (n=542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.359)

- **PATRÓN** `ibs_15` > `0.8305` → IC=+0.407 (n=480)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8305 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` > `0.4131` → IC=+0.388 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4131 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.231` → IC=+0.372 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.231 (IC base=+0.359)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `3823.0046` → IC=+0.371 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3823.0046 (IC base=+0.359)

- **PATRÓN** `ballena_activa_n` < `440.0` → IC=+0.378 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 440.0 (IC base=+0.359)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.360 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.358)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.369 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.358)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.359 (n=97)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.358)

- **PATRÓN** `drift_15min` |x|≤ `0.5086` → IC=+0.362 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5086 (IC base=+0.358)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1524` → IC=+0.382 (n=193)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1524 (IC base=+0.358)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.394 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.358)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.358)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.387 (n=290)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.398 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.495` → IC=+0.363 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.495 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` < `25.57` → IC=+0.358 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 25.57 (IC base=+0.358)

- **PATRÓN** `libro_liquidez` > `15215.7199` → IC=+0.388 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15215.7199 (IC base=+0.358)

- **PATRÓN** `ballena_activa_n` < `499.0` → IC=+0.407 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 499.0 (IC base=+0.358)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.357 (n=110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.358)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.377 (n=112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.358)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.368 (n=165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.358)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0901` → IC=+0.374 (n=221)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0901 (IC base=+0.358)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.382 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.358)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.416 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.358)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.404 (n=247)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` > `0.4406` → IC=+0.365 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4406 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` < `0.2769` → IC=+0.360 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2769 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.861` → IC=+0.387 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.861 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.356 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.358)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.358)

- **PATRÓN** `libro_liquidez` > `4286.2041` → IC=+0.382 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4286.2041 (IC base=+0.358)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.364 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 145.0 (IC base=+0.358)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.223 (n=915)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2749)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.208 (n=1378)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2286)

- **FILTRO** `libro_liquidez` < `4072.8167` → IC=-0.147 (n=2418)

  - _Acción_: SKIP cuando `libro_liquidez` < 4072.8167
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=1246)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.186 (n=588)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=-0.069)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.221 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.069)

- **PATRÓN** `ibs_15` > `0.6335` → IC=+0.277 (n=882)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6335 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.200 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2612` → IC=+0.193 (n=743)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.2612 (IC base=-0.069)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2227` → IC=+0.268 (n=975)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2227 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3508` → IC=+0.283 (n=2923)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3508 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.8606` → IC=+0.295 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8606 (IC base=-0.013)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.253 (n=2544)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.210 (n=518)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1557)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.229 (n=518)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=1557)

- **FILTRO** `sigma_ewma_delta_pct` > `23.641` → IC=-0.263 (n=297)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.641
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=1778)

- **FILTRO** `libro_liquidez` < `16308.7525` → IC=-0.197 (n=1369)

  - _Acción_: SKIP cuando `libro_liquidez` < 16308.7525
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=706)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.175 (n=207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0027 (IC base=+0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1979` → IC=+0.302 (n=119)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1979 (IC base=+0.087)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.305 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.087)

- **PATRÓN** `ibs_15` > `0.7533` → IC=+0.330 (n=263)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7533 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.0996` → IC=+0.295 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0996 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.4912` → IC=+0.294 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4912 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.533` → IC=+0.127 (n=306)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 8.533 (IC base=+0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.231 (n=50)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1833` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1833 (IC base=-0.190)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.308 (n=50)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.190)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.190)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.414 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.190)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=568)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.150 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.160 (n=392)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0038 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.175 (n=293)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1103 (IC base=+0.144)

- **PATRÓN** `drift_15min` |x|≤ `0.4046` → IC=+0.144 (n=147)

  - _Acción_: Kelly boost +0.72€ cuando `drift_15min` |x|≤ 0.4046 (IC base=+0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.154 (n=293)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.190 (n=327)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.248 (n=439)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.5931` → IC=+0.151 (n=81)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.5931 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.145 (n=319)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.508` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.508 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=568)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `11031.3332` → IC=+0.178 (n=147)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 11031.3332 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.249 (n=684)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.3488` → IC=+0.242 (n=903)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3488 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.757` → IC=+0.254 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.757 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2128` → IC=+0.265 (n=465)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2128 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.268 (n=343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.3647` → IC=+0.271 (n=1026)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3647 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.7568` → IC=+0.300 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7568 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.34` → IC=+0.262 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.34 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.558` → IC=+0.244 (n=1073)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.558 (IC base=+0.241)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1711` → IC=-0.248 (n=288)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1711
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=560)

- **FILTRO** `drift_15min` |x|> `0.8847` → IC=-0.279 (n=211)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8847
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=637)

- **FILTRO** `sigma_ewma_delta_pct` > `6.672` → IC=-0.182 (n=209)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.672
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=639)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.256 (n=84)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=764)

- **FILTRO** `sigma_ewma_delta_pct` > `18.292` → IC=-0.143 (n=441)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.292
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3538)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.179)

- **PATRÓN** `ibs_15` > `0.9167` → IC=+0.340 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9167 (IC base=-0.179)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.179)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.179)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0787` → IC=+0.244 (n=409)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0787 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.3462` → IC=+0.287 (n=458)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3462 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.1715` → IC=+0.250 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1715 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.242 (n=370)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=658)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.201)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1482` → IC=+0.279 (n=328)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1482 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1097` → IC=+0.302 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1097 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=720)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7968` → IC=+0.353 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7968 (IC base=-0.026)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.032)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.032)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.290 (n=783)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.326 (n=297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.299 (n=296)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.224` → IC=+0.305 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.224 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.306 (n=931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8395` → IC=+0.319 (n=889)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8395 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.424` → IC=+0.328 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.424 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.353 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `12909.8374` → IC=+0.305 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12909.8374 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.311 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.329 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.285)

- **PATRÓN** `drift_15min` |x|≤ `0.4183` → IC=+0.286 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4183 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.310 (n=161)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2304` → IC=+0.291 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2304 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.308 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.314 (n=483)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.334 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.865` → IC=+0.361 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.865 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.284 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `16334.7136` → IC=+0.328 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16334.7136 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.295 (n=271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.294 (n=406)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.319 (n=136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.288 (n=272)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3023` → IC=+0.311 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3023 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.311 (n=364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.328 (n=406)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.4372` → IC=+0.313 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4372 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.99` → IC=+0.333 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.99 (IC base=+0.288)

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

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.175 (n=115)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=345)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.296` → IC=-0.370 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.296
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

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
- **PATRÓN** `T_h` > `81.9543` → IC=+0.228 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 81.9543 (IC base=+0.210)

- **PATRÓN** `ratio` < `0.9763` → IC=+0.456 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9763 (IC base=+0.210)

- **PATRÓN** `T_h` > `145.7504` → IC=+0.390 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7504 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0095` → IC=+0.319 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0095 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.3918` → IC=+0.218 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.190)

- **PATRÓN** `ratio` < `0.972` → IC=+0.429 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.972 (IC base=+0.190)

- **PATRÓN** `T_h` > `108.3228` → IC=+0.298 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 108.3228 (IC base=+0.289)

- **PATRÓN** `ratio` > `1.0479` → IC=+0.404 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0479 (IC base=+0.289)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.262 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.245)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.428 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.245)

- **PATRÓN** `T_h` > `111.9668` → IC=+0.345 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9668 (IC base=+0.322)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.360 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.322)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.401)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6032 sube el IC de +0.193 a +0.269 en UPDOWN_GBM#15min (n=2616). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7143 sube el IC de +0.214 a +0.279 en UPDOWN_GBM#BTC#15min (n=500). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5728 sube el IC de +0.133 a +0.232 en UPDOWN_GBM#ETH#15min (n=553). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9296 sube el IC de +0.148 a +0.352 en UPDOWN_GBM#SOL#15min (n=140). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5849 sube el IC de +0.215 a +0.295 en UPDOWN_GBM#XRP#15min (n=622). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1091 sube el IC de +0.069 a +0.158 en UPDOWN_GBM#XRP#15min (n=667). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6335 sube el IC de -0.069 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=882). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3508 sube el IC de -0.013 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=2923). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.087 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=263). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.190 a +0.308 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=50). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6341 sube el IC de +0.144 a +0.248 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=439). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3647 sube el IC de +0.241 a +0.271 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1026). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9167 sube el IC de -0.179 a +0.340 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3462 sube el IC de -0.038 a +0.287 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=458). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.201 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=720). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8395 sube el IC de +0.287 a +0.319 en UPDOWN_GBM_IBS_ALTO (n=889). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.285 a +0.314 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=483). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.288 a +0.328 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=406). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8305 sube el IC de +0.359 a +0.407 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=480). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.358 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=290). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.358 a +0.404 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=247). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1612 | +0.090 | +178.45€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1612 | +0.090 | +178.45€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1241 | +0.095 | +151.41€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1241 | +0.095 | +151.41€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 268 | +0.067 | +11.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 268 | +0.067 | +11.32€ | 6 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 313 | +0.008 | +62.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 313 | +0.008 | +62.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 246 | +0.012 | +54.28€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 246 | +0.012 | +54.28€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 45 | +0.011 | +5.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 45 | +0.011 | +5.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 35212 | -0.084 | -4610.75€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1768 | -0.015 | -226.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 33444 | -0.087 | -4384.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4392 | -0.117 | -759.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4392 | -0.117 | -759.74€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1768 | -0.015 | -226.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1768 | -0.015 | -226.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4090 | -0.113 | -839.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4090 | -0.113 | -839.13€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9110 | +0.008 | -854.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9110 | +0.008 | -854.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8974 | -0.108 | -668.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8974 | -0.108 | -668.96€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6878 | -0.152 | -1262.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6878 | -0.152 | -1262.37€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 27418 | -0.019 | +3714.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 7090 | +0.002 | +1770.17€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 20328 | -0.027 | +1944.69€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 27418 | -0.019 | +3714.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 7090 | +0.002 | +1770.17€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 20328 | -0.027 | +1944.69€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 121037 | +0.114 | -5299.01€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 16650 | +0.182 | -511.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 518 | -0.042 | -62.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 96401 | +0.103 | -4456.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7468 | +0.104 | -269.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 16005 | +0.104 | -1087.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 56 | -0.155 | +9.14€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 15934 | +0.105 | -1085.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 23869 | +0.128 | -418.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4910 | +0.195 | -151.87€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 15984 | +0.116 | -166.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2933 | +0.089 | -77.31€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 16052 | +0.095 | -1226.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 63 | -0.100 | -2.83€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 15974 | +0.097 | -1212.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 25711 | +0.124 | -442.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6815 | +0.175 | -108.13€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 16170 | +0.106 | -270.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2714 | +0.101 | -54.72€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 23378 | +0.114 | -1268.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4749 | +0.190 | -268.11€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 421 | -0.006 | -8.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 16387 | +0.093 | -854.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1821 | +0.133 | -137.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 16022 | +0.102 | -856.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 57 | -0.042 | +10.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 15952 | +0.103 | -866.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 19328 | +0.194 | -1225.01€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 19328 | +0.194 | -1225.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4474 | +0.173 | -421.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4474 | +0.173 | -421.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2154 | +0.201 | -40.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2154 | +0.201 | -40.08€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4404 | +0.182 | -354.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4404 | +0.182 | -354.51€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3870 | +0.241 | -142.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3870 | +0.241 | -142.21€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4347 | +0.189 | -280.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4347 | +0.189 | -280.09€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 892 | +0.426 | -32.30€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 892 | +0.426 | -32.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 350 | +0.435 | -6.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 350 | +0.435 | -6.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 343 | +0.427 | -10.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 343 | +0.427 | -10.89€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 187 | +0.405 | -12.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 187 | +0.405 | -12.95€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 67230 | +0.200 | -4991.87€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 67230 | +0.200 | -4991.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 11566 | +0.183 | -1219.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 11566 | +0.183 | -1219.15€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 10829 | +0.224 | -383.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 10829 | +0.224 | -383.18€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 11544 | +0.177 | -1285.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 11544 | +0.177 | -1285.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10890 | +0.221 | -404.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10890 | +0.221 | -404.04€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 11138 | +0.202 | -741.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 11138 | +0.202 | -741.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 11263 | +0.193 | -958.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 11263 | +0.193 | -958.78€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 25645 | +0.118 | +249.04€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 25645 | +0.118 | +249.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 12737 | +0.122 | +195.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 12737 | +0.122 | +195.85€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 12908 | +0.115 | +53.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 12908 | +0.115 | +53.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1791 | +0.289 | -23.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1791 | +0.289 | -23.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 809 | +0.281 | -16.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 809 | +0.281 | -16.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 864 | +0.286 | -11.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 864 | +0.286 | -11.26€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 118 | +0.350 | +4.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 118 | +0.350 | +4.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 812 | +0.440 | +1.39€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 812 | +0.440 | +1.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 392 | +0.439 | -0.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 392 | +0.439 | -0.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 374 | +0.442 | +1.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 374 | +0.442 | +1.53€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1392 | +0.067 | -70.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 511 | +0.056 | -42.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 881 | +0.073 | -28.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1087 | +0.073 | -36.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 206 | +0.072 | -7.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 881 | +0.073 | -28.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 239 | +0.027 | -36.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 239 | +0.027 | -36.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 49464 | +0.100 | -1265.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4018 | +0.092 | +57.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 45446 | +0.100 | -1322.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 27397 | +0.104 | -294.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4018 | +0.092 | +57.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 23379 | +0.107 | -351.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 9870 | +0.109 | -22.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 9870 | +0.109 | -22.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 12197 | +0.081 | -948.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 12197 | +0.081 | -948.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 871 | +0.203 | -101.16€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 871 | +0.203 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 871 | +0.203 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 871 | +0.203 | -101.16€ | 2 | 4 |
| ✅ GBM_LATE_15M | 34477 | +0.090 | +17269.85€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 34477 | +0.090 | +17269.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5800 | +0.205 | +4521.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5800 | +0.205 | +4521.47€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 5125 | +0.178 | +3719.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5125 | +0.178 | +3719.02€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 6124 | +0.202 | +4670.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6124 | +0.202 | +4670.69€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 4864 | +0.036 | +1229.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4864 | +0.036 | +1229.87€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4921 | -0.029 | +1079.36€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4921 | -0.029 | +1079.36€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 7643 | -0.036 | +2049.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7643 | -0.036 | +2049.44€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 37412 | +0.087 | +19920.64€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 37412 | +0.087 | +19920.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7265 | +0.011 | +3703.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7265 | +0.011 | +3703.31€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7763 | +0.013 | +1657.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7763 | +0.013 | +1657.85€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5268 | +0.269 | +5463.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5268 | +0.269 | +5463.37€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 6358 | +0.012 | +1424.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 6358 | +0.012 | +1424.68€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6101 | +0.036 | +2436.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6101 | +0.036 | +2436.15€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4657 | +0.290 | +5235.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4657 | +0.290 | +5235.28€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 27542 | +0.176 | +21659.14€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 27542 | +0.176 | +21659.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4169 | +0.218 | +3511.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4169 | +0.218 | +3511.86€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4355 | +0.151 | +3192.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4355 | +0.151 | +3192.51€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4367 | +0.218 | +3652.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4367 | +0.218 | +3652.55€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4635 | +0.138 | +3425.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4635 | +0.138 | +3425.80€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5153 | +0.127 | +3820.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5153 | +0.127 | +3820.51€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4863 | +0.215 | +4055.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4863 | +0.215 | +4055.91€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7461 | +0.140 | +3608.34€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7461 | +0.140 | +3608.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 341 | +0.141 | +188.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 341 | +0.141 | +188.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2310 | +0.148 | +1300.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2310 | +0.148 | +1300.58€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2291 | +0.154 | +1124.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2291 | +0.154 | +1124.66€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1607 | +0.108 | +579.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1607 | +0.108 | +579.43€ | 1 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 537 | +0.135 | +240.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 537 | +0.135 | +240.44€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 34699 | +0.182 | +27021.72€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 34699 | +0.182 | +27021.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5522 | +0.233 | +4945.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5522 | +0.233 | +4945.21€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5368 | +0.148 | +3548.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5368 | +0.148 | +3548.81€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5811 | +0.229 | +5108.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5811 | +0.229 | +5108.21€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5633 | +0.137 | +3919.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5633 | +0.137 | +3919.87€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6143 | +0.126 | +4279.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6143 | +0.126 | +4279.64€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6222 | +0.218 | +5219.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6222 | +0.218 | +5219.98€ | 0 | 21 |
| ✅ GBM_LATE_5M | 9554 | +0.183 | +6718.65€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 9554 | +0.183 | +6718.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 882 | +0.234 | +789.82€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 882 | +0.234 | +789.82€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2122 | +0.170 | +1532.70€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2122 | +0.170 | +1532.70€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 992 | +0.176 | +650.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 992 | +0.176 | +650.38€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 2968 | +0.186 | +2020.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2968 | +0.186 | +2020.52€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 1250 | +0.178 | +871.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1250 | +0.178 | +871.81€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1340 | +0.175 | +853.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1340 | +0.175 | +853.42€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2608 | +0.069 | +937.43€ | 0 | 10 |
| ✅ GBM_LATE_60M#60min | 2608 | +0.069 | +937.43€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 982 | +0.087 | +355.46€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 982 | +0.087 | +355.46€ | 0 | 10 |
| ✅ GBM_LATE_60M#ETH | 814 | +0.067 | +351.41€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 814 | +0.067 | +351.41€ | 0 | 10 |
| ✅ GBM_LATE_60M#SOL | 812 | +0.049 | +230.57€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 812 | +0.049 | +230.57€ | 2 | 13 |
| 🚫 GBM_LATE_60M_FADE | 490 | -0.240 | -15.90€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 490 | -0.240 | -15.90€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 185 | -0.233 | -11.64€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 185 | -0.233 | -11.64€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 171 | -0.217 | +1.92€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 171 | -0.217 | +1.92€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 134 | -0.272 | -6.17€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 134 | -0.272 | -6.17€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1160 | +0.087 | +303.73€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1160 | +0.087 | +303.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 441 | +0.082 | +95.28€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 441 | +0.082 | +95.28€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 403 | +0.060 | +66.14€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 403 | +0.060 | +66.14€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 316 | +0.126 | +142.30€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 316 | +0.126 | +142.30€ | 2 | 14 |
| ✅ LATE_WINDOW_5MIN | 132 | +0.254 | +113.28€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 132 | +0.254 | +113.28€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 132 | +0.254 | +113.28€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 132 | +0.254 | +113.28€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 2847 | +0.101 | +732.77€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2847 | +0.101 | +732.77€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2847 | +0.101 | +732.77€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2847 | +0.101 | +732.77€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 439 | -0.069 | -32.39€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 439 | -0.069 | -32.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 123 | -0.028 | -1.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 123 | -0.028 | -1.03€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 167 | -0.033 | -6.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 167 | -0.033 | -6.54€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 3062 | +0.018 | +67.34€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3062 | +0.018 | +67.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 150 | +0.033 | -0.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 150 | +0.033 | -0.41€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 514 | +0.021 | +31.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 514 | +0.021 | +31.22€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1113 | +0.028 | +29.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1113 | +0.028 | +29.08€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 698 | +0.011 | +0.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 698 | +0.011 | +0.43€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 384 | +0.010 | +12.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 384 | +0.010 | +12.12€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1461 | -0.039 | -22.57€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1461 | -0.039 | -22.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 417 | -0.035 | -11.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 417 | -0.035 | -11.10€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 484 | -0.014 | +5.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 484 | -0.014 | +5.04€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 560 | -0.064 | -16.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 560 | -0.064 | -16.52€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 5303 | -0.017 | +106.34€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2504 | -0.022 | +16.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2799 | -0.012 | +89.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 148 | -0.007 | +4.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 72 | +0.027 | +7.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 76 | -0.038 | -3.61€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1335 | -0.008 | +35.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 631 | -0.015 | +1.38€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 704 | -0.001 | +33.89€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 586 | -0.022 | +12.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 294 | -0.034 | -2.31€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 292 | -0.010 | +14.36€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1085 | -0.035 | -26.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 496 | -0.052 | -34.13€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 589 | -0.019 | +8.12€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1039 | -0.011 | +37.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 501 | -0.009 | +25.55€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 538 | -0.013 | +12.20€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1110 | -0.015 | +42.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 510 | -0.016 | +18.47€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 600 | -0.015 | +24.42€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 40008 | -0.002 | +1933.56€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 40008 | -0.002 | +1933.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 7149 | +0.024 | +944.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 7149 | +0.024 | +944.54€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5927 | -0.032 | -94.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5927 | -0.032 | -94.68€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 7242 | +0.021 | +717.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 7242 | +0.021 | +717.06€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5745 | -0.049 | -144.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5745 | -0.049 | -144.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6749 | -0.007 | +202.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6749 | -0.007 | +202.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 7196 | +0.013 | +308.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 7196 | +0.013 | +308.28€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6237 | -0.058 | -141.45€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6237 | -0.058 | -141.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1220 | +0.001 | -13.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1220 | +0.001 | -13.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1538 | -0.075 | -30.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1538 | -0.075 | -30.43€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 50 | -0.077 | -3.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 50 | -0.077 | -3.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 730 | -0.122 | -32.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 730 | -0.122 | -32.16€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1843 | -0.078 | -36.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1843 | -0.078 | -36.50€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 100288 | -0.074 | +1665.53€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 100288 | -0.074 | +1665.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 17262 | -0.075 | +883.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 17262 | -0.075 | +883.06€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 15204 | -0.098 | -830.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 15204 | -0.098 | -830.80€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 17538 | -0.065 | +1049.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 17538 | -0.065 | +1049.84€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 14739 | -0.095 | -459.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 14739 | -0.095 | -459.01€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 18137 | -0.052 | +359.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 18137 | -0.052 | +359.72€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 17408 | -0.064 | +662.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 17408 | -0.064 | +662.70€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8102 | -0.032 | -159.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8102 | -0.032 | -159.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1925 | -0.043 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1925 | -0.043 | -18.91€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2245 | -0.026 | -31.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2245 | -0.026 | -31.96€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1126 | -0.051 | -24.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1126 | -0.051 | -24.99€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 802 | -0.029 | -30.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 802 | -0.029 | -30.75€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1425 | +0.122 | +565.02€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#5min | 1289 | +0.128 | +552.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 299 | +0.148 | +162.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 299 | +0.148 | +162.59€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 250 | +0.107 | +73.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 250 | +0.107 | +73.58€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 263 | +0.126 | +116.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 263 | +0.126 | +116.34€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 229 | +0.154 | +127.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 229 | +0.154 | +127.17€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 248 | +0.100 | +72.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 248 | +0.100 | +72.74€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1021 | -0.013 | -9.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1021 | -0.013 | -9.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 201 | -0.007 | +4.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 201 | -0.007 | +4.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 157 | +0.009 | +9.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 157 | +0.009 | +9.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 269 | -0.024 | -10.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 269 | -0.024 | -10.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 226 | +0.009 | +2.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 226 | +0.009 | +2.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 168 | -0.053 | -15.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 168 | -0.053 | -15.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 772 | -0.087 | -71.70€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 353 | -0.139 | -82.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 273 | -0.180 | -75.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 80 | +0.000 | -7.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 273 | -0.045 | -1.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 194 | -0.046 | -2.35€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 79 | -0.043 | +0.77€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 146 | -0.034 | +12.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 117 | -0.046 | +7.34€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 29 | +0.016 | +5.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 584 | -0.109 | -70.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 188 | -0.016 | -0.96€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 922 | -0.202 | -55.47€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 383 | -0.196 | -33.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 328 | -0.200 | -34.63€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 55 | -0.167 | +0.79€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 311 | -0.216 | -32.10€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 267 | -0.225 | -37.68€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 44 | -0.152 | +5.58€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 228 | -0.191 | +10.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 209 | -0.187 | +7.33€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 804 | -0.206 | -64.98€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 118 | -0.175 | +9.51€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 389 | +0.400 | +336.92€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 45 | +0.096 | +25.91€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 45 | +0.096 | +25.91€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 98 | +0.370 | +76.40€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 98 | +0.370 | +76.40€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 246 | +0.464 | +234.61€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 246 | +0.464 | +234.61€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 389 | +0.400 | +336.92€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 635 | +0.031 | +24.86€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 635 | +0.031 | +24.86€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 48 | +0.020 | -1.12€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 48 | +0.020 | -1.12€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 66 | -0.015 | -2.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 66 | -0.015 | -2.23€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 226 | +0.057 | +25.91€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 226 | +0.057 | +25.91€ | 2 | 5 |
| ✅ STREAK_FADE_5M | 3215 | -0.021 | -125.74€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3215 | -0.021 | -125.74€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 994 | -0.023 | -36.46€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 994 | -0.023 | -36.46€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 585 | -0.026 | -25.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 585 | -0.026 | -25.65€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1480 | -0.015 | -49.22€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1480 | -0.015 | -49.22€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 91 | -0.059 | -9.78€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 91 | -0.059 | -9.78€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 53 | -0.027 | -5.34€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 53 | -0.027 | -5.34€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 9896 | +0.019 | +102.61€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9896 | +0.019 | +102.61€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2641 | +0.021 | +28.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2641 | +0.021 | +28.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2399 | +0.025 | +45.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2399 | +0.025 | +45.38€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2863 | +0.009 | -1.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2863 | +0.009 | -1.83€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1993 | +0.021 | +30.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1993 | +0.021 | +30.24€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8950 | +0.013 | -42.53€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8950 | +0.013 | -42.53€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3533 | +0.018 | -4.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3533 | +0.018 | -4.78€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3519 | +0.011 | -25.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3519 | +0.011 | -25.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1898 | +0.009 | -11.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1898 | +0.009 | -11.96€ | 1 | 0 |
| ✅ UPDOWN_GBM | 61706 | +0.049 | +5037.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 15343 | +0.084 | +3366.69€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2043 | +0.005 | +7.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 40595 | +0.042 | +1608.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3516 | +0.006 | +57.28€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6386 | +0.084 | +911.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1346 | +0.157 | +584.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 67 | -0.022 | -2.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4973 | +0.066 | +329.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 11973 | +0.051 | +982.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1933 | +0.092 | +463.36€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 528 | +0.011 | +5.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 7846 | +0.055 | +468.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1589 | +0.005 | +42.65€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 77 | -0.082 | +2.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 7505 | +0.062 | +723.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1329 | +0.148 | +518.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 64 | +0.000 | -2.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6112 | +0.044 | +207.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 13441 | +0.038 | +753.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3623 | +0.056 | +458.91€ | 1 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 521 | +0.007 | +8.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 8031 | +0.038 | +282.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1197 | +0.005 | +1.00€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 69 | -0.106 | +3.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 13634 | +0.027 | +565.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3618 | +0.037 | +337.48€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 511 | -0.001 | -0.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 8714 | +0.026 | +220.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 730 | +0.014 | +13.62€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#daily | 61 | -0.151 | -5.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 8765 | +0.057 | +1102.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3494 | +0.103 | +1004.16€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 352 | +0.006 | -1.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4919 | +0.028 | +100.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 207 | -0.112 | +0.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 715 | +0.359 | +247.69€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 715 | +0.359 | +247.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 386 | +0.358 | +126.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 386 | +0.358 | +126.47€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 329 | +0.358 | +121.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 329 | +0.358 | +121.22€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 16816 | -0.025 | +4068.84€ | 3 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 16816 | -0.025 | +4068.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1442 | -0.052 | +484.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1442 | -0.052 | +484.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2901 | -0.111 | +137.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2901 | -0.111 | +137.85€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 820 | +0.218 | +673.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 820 | +0.218 | +673.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1952 | +0.212 | +1223.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1952 | +0.212 | +1223.24€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4827 | -0.063 | +645.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4827 | -0.063 | +645.52€ | 5 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4874 | -0.063 | +904.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4874 | -0.063 | +904.72€ | 1 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 187 | +0.034 | +6.83€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 187 | +0.034 | +6.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 187 | +0.034 | +6.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 187 | +0.034 | +6.83€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1185 | +0.287 | +967.99€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1185 | +0.287 | +967.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 644 | +0.285 | +505.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 644 | +0.285 | +505.59€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 541 | +0.288 | +462.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 541 | +0.288 | +462.41€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 766 | -0.115 | -84.11€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 766 | -0.115 | -84.11€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 224 | -0.088 | -18.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 224 | -0.088 | -18.30€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 80 | -0.159 | -7.73€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 80 | -0.159 | -7.73€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 83 | -0.194 | -8.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 83 | -0.194 | -8.02€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 3015 | +0.306 | +1479.60€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1079 | +0.260 | +156.25€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1150 | +0.299 | +509.92€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 786 | +0.378 | +813.42€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.011 n=751 — no justifica filtro, seguir monitorizando
  - _Datos_: n=751 IC=+0.011 PNL=+31.25€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 649 celda(s) pasan gate riguroso completo de 2512 evaluadas (n>=40) y 3494 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.036 < 0.08 — monitorear
  - _Datos_: n=3613 IC=+0.036 PNL=+334.65€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1150/15 IC=+0.299 PNL=+509.92€ | BTC: n=1079/15 IC=+0.260 PNL=+156.25€ | SOL: n=786/15 IC=+0.378 PNL=+813.42€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.137 n=620/60 | contraria IC=+0.200 n=631 | gap=-0.063 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=396, boost estimado=+0.012. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1195/40 IC=+0.005 PNL=+0.99€ | BTC#60min: n=1587/40 IC=+0.005 PNL=+42.62€ | SOL#60min: n=729/40 IC=+0.013 PNL=+12.36€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=456918 | tras_1loss IC=+0.090 n=349682 | tras_2loss IC=+0.059 n=143190/40 | gap=-0.011 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.215 > 0.08 con n=539 PNL=+437.71€
  - _Datos_: n=539 IC=+0.215 PNL=+437.71€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.08 con n=591 PNL=+434.37€
  - _Datos_: n=591 IC=+0.210 PNL=+434.37€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.185 > 0.08 con n=52 PNL=+29.44€
  - _Datos_: n=52 IC=+0.185 PNL=+29.44€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=2461 PNL=+1348.92€
  - _Datos_: n=2461 IC=+0.332 PNL=+1348.92€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=491 IC=+0.074 PNL=+54.54€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=491 IC=+0.074 PNL=+54.54€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=69 IC=+0.190 PNL=+47.57€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=69 IC=+0.190 PNL=+47.57€

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
  - _Estado_: n=2349 IC=+0.006 PNL=+0.47€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2349 IC=+0.006 PNL=+0.47€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1162 IC=+0.008 PNL=+55.51€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1162 IC=+0.008 PNL=+55.51€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=751 IC=+0.011 PNL=+31.25€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=751 IC=+0.011 PNL=+31.25€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.193 > 0.1 con n=3483 PNL=+2363.91€
  - _Datos_: n=3483 IC=+0.193 PNL=+2363.91€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1930 IC=+0.092 PNL=+463.52€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1930 IC=+0.092 PNL=+463.52€

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
  - _Estado_: n=805 IC=+0.034 PNL=+70.88€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=805 IC=+0.034 PNL=+70.88€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=87 IC=+0.051 PNL=+4.69€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=87 IC=+0.051 PNL=+4.69€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.254 n=132) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=132 IC=+0.254 PNL=+113.28€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.129 > 0.02 con n=822 PNL=+349.40€
  - _Datos_: n=822 IC=+0.129 PNL=+349.40€

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
  - _Estado_: n=23139 IC=+0.070 PNL=+3245.40€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=23139 IC=+0.070 PNL=+3245.40€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.131 < -0.1 con n=364 PNL=+49.81€
  - _Datos_: n=364 IC=-0.131 PNL=+49.81€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2662 IC=+0.069 PNL=+329.88€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2662 IC=+0.069 PNL=+329.88€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=113 IC=-0.109 PNL=+4.62€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=113 IC=-0.109 PNL=+4.62€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.1 con n=628 PNL=+167.02€
  - _Datos_: n=628 IC=+0.119 PNL=+167.02€

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
  - _Estado_: n=25095 IC=-0.138 PNL=+1661.17€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=25095 IC=-0.138 PNL=+1661.17€

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
  - _Estado_: n=2559 IC=+0.137 PNL=+1489.36€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2559 IC=+0.137 PNL=+1489.36€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=6415 IC=+0.044 PNL=+435.81€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6415 IC=+0.044 PNL=+435.81€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.088 > 0.08 con n=2829 PNL=+1481.44€
  - _Datos_: n=2829 IC=+0.088 PNL=+1481.44€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.226 < -0.1 con n=2575 PNL=-198.03€
  - _Datos_: n=2575 IC=-0.226 PNL=-198.03€

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
  - _Estado_: n=53 IC=-0.009 PNL=+6.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=53 IC=-0.009 PNL=+6.32€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1450) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1450 IC=+0.101 PNL=+327.85€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=508) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=508 IC=+0.410 PNL=+720.85€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=11558 IC=+0.184 PNL=-1216.40€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=11558 IC=+0.184 PNL=-1216.40€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.1 con n=184 PNL=+114.46€
  - _Datos_: n=184 IC=+0.210 PNL=+114.46€
