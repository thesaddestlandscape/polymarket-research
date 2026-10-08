# Hipótesis automáticas — 2026-10-08 05:21 UTC
_Generado por shadow_postmortem.py sobre 802162 resoluciones (PNL=+99233.92€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.234 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.121)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.200 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.121)

- **PATRÓN** `banda_hit_calibrado` > `0.617` → IC=+0.241 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.617 (IC base=+0.121)

- **PATRÓN** `banda_z` > `9.018` → IC=+0.192 (n=225)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 9.018 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=713)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.121)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.230 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.207 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.6142` → IC=+0.229 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6142 (IC base=+0.125)

- **PATRÓN** `banda_z` > `9.588` → IC=+0.179 (n=182)

  - _Acción_: Kelly boost +0.90€ cuando `banda_z` > 9.588 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=615)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.125)

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
- **FILTRO** `restante_s_al_confirmar` < `143.83` → IC=-0.209 (n=8754)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.83
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=26265)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.76` → IC=-0.269 (n=1095)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.76
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=3288)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `123.5` → IC=-0.305 (n=1020)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 123.5
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3062)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `164.85` → IC=-0.224 (n=2226)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 164.85
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=6678)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `130.56` → IC=-0.303 (n=1708)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.56
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=5126)

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
- **PATRÓN** `py_entrada` > `0.685` → IC=+0.213 (n=16822)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.685 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=3951)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `9542.1065` → IC=+0.183 (n=1757)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9542.1065 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.135 (n=15032)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=18342)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=13923)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=6488)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7509.4511` → IC=+0.167 (n=2495)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7509.4511 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=1908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=1864)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=2343)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `16057.1675` → IC=+0.211 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16057.1675 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.198 (n=1685)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=1867)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=2397)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `16038.5479` → IC=+0.211 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16038.5479 (IC base=+0.193)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.122 (n=1061)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.555 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `4988.4492` → IC=+0.126 (n=228)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 4988.4492 (IC base=+0.087)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.091)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.138 (n=974)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.091)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.363 (n=1122)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.231 (n=1582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.360 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=1832)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.222)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=882)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=756)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.249 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.134 (n=972)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `1322.2406` → IC=+0.141 (n=844)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1322.2406 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=842)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.217 (n=1532)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.409 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=1244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=657)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.147)

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
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.121)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.224 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.121)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=15010)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=12756)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.228 (n=6362)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=3527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=3339)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=3404)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=1523)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.230 (n=1517)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.318 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.228)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=3459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=3307)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=2755)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=3040)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.331 (n=1060)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=3384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=2172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.190 (n=2577)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.71 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.197 (n=1211)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.430 (n=610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=701)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `2768.4308` → IC=+0.433 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2768.4308 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.433 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.444 (n=177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `19769.7921` → IC=+0.444 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 19769.7921 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.440 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.425 (n=266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.434 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.427 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `3391.3443` → IC=+0.436 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3391.3443 (IC base=+0.427)

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

- **FILTRO** `libro_liquidez` < `6345.2155` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 6345.2155
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.203 (n=44846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=19665)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=9091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=6190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.199 (n=8550)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=4032)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.269 (n=4589)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.181 (n=8141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=8183)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=4066)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=2785)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=7444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=2924)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=3218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=3406)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=6901)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.125 (n=6414)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.2 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.137 (n=6714)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=8501)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.45` → IC=+0.137 (n=6371)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.45 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=3430)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.126 (n=3180)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.141 (n=3368)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=4210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `3.09` → IC=+0.146 (n=3163)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.09 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=3471)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.131 (n=3676)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.134 (n=3226)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=1422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.290 (n=1402)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.379 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1546.3244` → IC=+0.292 (n=1338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1546.3244 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.291 (n=635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.353 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `3829.7681` → IC=+0.291 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3829.7681 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.291 (n=672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.385 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1446.6946` → IC=+0.301 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1446.6946 (IC base=+0.286)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.439 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.448 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.461 (n=100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.444)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.443 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` < `0.925` → IC=+0.455 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.925 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.444)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.445 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.444)

- **PATRÓN** `libro_liquidez` > `2138.537` → IC=+0.458 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2138.537 (IC base=+0.444)

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
- **PATRÓN** `drift_60min` |x|≤ `0.3703` → IC=+0.135 (n=9466)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.3703 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9825` → IC=+0.241 (n=3586)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9825 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2206` → IC=+0.254 (n=2461)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2206 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.427` → IC=+0.192 (n=2794)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.427 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.249 (n=2013)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8553 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.617` → IC=+0.254 (n=3019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.617 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.3019` → IC=+0.231 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3019 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.3274` → IC=+0.219 (n=3419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3274 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5634` → IC=+0.141 (n=13137)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5634 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.5751` → IC=+0.204 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5751 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.1501` → IC=+0.183 (n=4507)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1501 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` < `1.1973` → IC=+0.182 (n=4868)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.1973 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` > `1.054` → IC=+0.183 (n=2208)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.054 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2951` → IC=+0.232 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2951 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` > `1.4487` → IC=+0.203 (n=8335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4487 (IC base=+0.072)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.218 (n=8148)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.072)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.219 (n=801)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.187 (n=796)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0079 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.2801` → IC=+0.184 (n=2101)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.2801 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=1159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.185 (n=1597)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 11.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.277 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.783` → IC=+0.295 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.783 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.237 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.183 (n=2261)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2469)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `2075.97` → IC=+0.192 (n=796)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2075.97 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.245 (n=1726)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.088` → IC=+0.267 (n=645)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.088 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0613` → IC=+0.283 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0613 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.526` → IC=+0.251 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.526 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.403` → IC=+0.239 (n=2019)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.403 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0946` → IC=+0.236 (n=1699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0946 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2849` → IC=+0.263 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2849 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.6252` → IC=+0.255 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6252 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=2123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.235 (n=840)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.253 (n=840)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=1910)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.3232` → IC=+0.233 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3232 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1958` → IC=+0.221 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1958 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.3479` → IC=+0.222 (n=1802)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3479 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.672` → IC=+0.261 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.672 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `1.2476` → IC=+0.220 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2476 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.6192` → IC=+0.223 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6192 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.244 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7608` → IC=+0.220 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7608 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.4138` → IC=+0.237 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4138 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.178 (n=640)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0026 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.166 (n=638)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=730)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7206` → IC=+0.177 (n=1908)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7206 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1323` → IC=+0.156 (n=1750)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1323 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.291` → IC=+0.153 (n=306)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 11.291 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.303` → IC=+0.143 (n=1746)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.303 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1974` → IC=+0.147 (n=1908)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1974 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.6232` → IC=+0.138 (n=1908)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6232 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0967` → IC=+0.169 (n=693)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0967 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4507` → IC=+0.148 (n=1794)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4507 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7847` → IC=+0.145 (n=1196)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7847 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.174 (n=756)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 229.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.202 (n=2419)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=2544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=2167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.391` → IC=+0.256 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.391 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0965` → IC=+0.194 (n=2127)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0965 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.3469` → IC=+0.196 (n=317)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.3469 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.1521` → IC=+0.202 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1521 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=2887)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.225 (n=1430)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.1784` → IC=+0.228 (n=944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1784 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=1001)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.236 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.678` → IC=+0.257 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.678 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3459` → IC=+0.255 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3459 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.7162` → IC=+0.221 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7162 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.719` → IC=+0.225 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.719 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2053.68` → IC=+0.223 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2053.68 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.216 (n=1962)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.214)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=132)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=2889)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.146 (n=456)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0036 (IC base=+0.043)

- **PATRÓN** `ibs_20min` > `0.9584` → IC=+0.219 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9584 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.188` → IC=+0.319 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.188 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.981` → IC=+0.177 (n=952)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 4.981 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.324 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8553 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.344 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.337 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.352 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.21` → IC=+0.319 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.21 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.319 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.0982` → IC=+0.165 (n=756)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.0982 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.465` → IC=+0.196 (n=238)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.465 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `0.8486` → IC=+0.154 (n=808)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8486 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.211 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `1.5242` → IC=+0.167 (n=1035)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.5242 (IC base=+0.030)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.171 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=445)

- **FILTRO** `ibs_20min` < `0.3056` → IC=-0.189 (n=130)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3056
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=392)

- **FILTRO** `ibs_20min` > `0.2264` → IC=-0.127 (n=2925)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2264
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=1441)

- **FILTRO** `sigma_ewma_delta_pct` > `8.797` → IC=-0.224 (n=450)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.797
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=3916)

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

- **PATRÓN** `ibs_20min` < `0.2264` → IC=+0.140 (n=1441)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.2264 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.1817` → IC=+0.275 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1817 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.6941` → IC=+0.277 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6941 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.1613` → IC=+0.306 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1613 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.38` → IC=+0.294 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.38 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.641` → IC=-0.186 (n=760)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.641
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2292)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.212 (n=839)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2213)

- **FILTRO** `ibs_20min` > `0.7628` → IC=-0.207 (n=1134)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7628
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=3407)

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

- **PATRÓN** `dist_vwap_pct` > `0.817` → IC=+0.287 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.817 (IC base=-0.011)

- **PATRÓN** `volumen_regimen` > `1.0773` → IC=+0.279 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0773 (IC base=-0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.1016` → IC=+0.271 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1016 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` < `2.1667` → IC=+0.257 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1667 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` > `1.4259` → IC=+0.259 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4259 (IC base=-0.011)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.198 (n=4717)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0093 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4667` → IC=+0.186 (n=12641)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4667 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.6733` → IC=+0.284 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6733 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.69` → IC=+0.153 (n=6374)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.69 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.1748` → IC=+0.249 (n=5177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1748 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6894` → IC=+0.257 (n=4625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6894 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.261 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4647` → IC=+0.246 (n=2784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4647 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6372` → IC=+0.256 (n=2784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6372 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.277 (n=7903)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.167 (n=4571)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0089 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5422` → IC=+0.159 (n=12052)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5422 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.6832` → IC=+0.251 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6832 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.172` → IC=+0.254 (n=3855)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.172 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.8744` → IC=+0.251 (n=2777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8744 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1978` → IC=+0.260 (n=1388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1978 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.309 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5872` → IC=+0.281 (n=2563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5872 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.284 (n=5718)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2584` → IC=-0.169 (n=986)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2584
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=2964)

- **FILTRO** `ibs_20min` > `0.7548` → IC=-0.176 (n=813)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7548
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=2443)

- **FILTRO** `sigma_ewma_delta_pct` > `4.63` → IC=-0.177 (n=723)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.63
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2533)

- **PATRÓN** `ibs_20min` > `0.9077` → IC=+0.275 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9077 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.323` → IC=+0.202 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.323 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2276` → IC=+0.280 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2276 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.216 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `2.2071` → IC=+0.238 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2071 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.232 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.1607` → IC=+0.151 (n=815)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1607 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0743` → IC=+0.417 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0743 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.2235` → IC=+0.424 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2235 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.6397` → IC=+0.420 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6397 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5399` → IC=+0.418 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5399 (IC base=-0.023)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.412 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8619` → IC=+0.153 (n=952)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.8619 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.1169` → IC=+0.194 (n=707)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1169 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` > `0.6779` → IC=+0.183 (n=1207)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6779 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.220 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.206 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` > `2.4223` → IC=+0.187 (n=442)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4223 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `226.0` → IC=+0.233 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 226.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.1603` → IC=+0.228 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1603 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.232 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0734` → IC=+0.222 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0734 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.300 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5482` → IC=+0.233 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5482 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1744` → IC=+0.238 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1744 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.278 (n=1907)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.258 (n=2139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.254 (n=1903)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.781` → IC=+0.283 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.781 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.266 (n=1832)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.1656` → IC=+0.262 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1656 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.263 (n=2521)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.304 (n=1795)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1822` → IC=+0.306 (n=790)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1822 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.322 (n=604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.3631` → IC=+0.292 (n=1795)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3631 (IC base=+0.287)

- **PATRÓN** `ibs_20min` > `0.1` → IC=+0.287 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.684` → IC=+0.302 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.684 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.1935` → IC=+0.284 (n=1748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1935 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.339` → IC=+0.295 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.339 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.7149` → IC=+0.304 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7149 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.6195` → IC=+0.290 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6195 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.287 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.287)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7614` → IC=-0.180 (n=821)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7614
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=2467)

- **PATRÓN** `ibs_20min` > `0.8995` → IC=+0.165 (n=755)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8995 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.219` → IC=+0.219 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.219 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.0103` → IC=+0.235 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0103 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1688` → IC=+0.226 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1688 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.231 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4092` → IC=+0.259 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4092 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.245 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1255` → IC=+0.222 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1255 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.224 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1951 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.297` → IC=+0.288 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.297 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.8479` → IC=+0.264 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8479 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.5231` → IC=+0.237 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5231 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.254 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7636` → IC=-0.187 (n=1507)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7636
  - _Potencial_: sin este filtro IC_bueno=+0.286 (n=1507)

- **FILTRO** `ibs_20min` > `0.6667` → IC=-0.245 (n=748)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2292)

- **FILTRO** `sigma_ewma_delta_pct` > `8.667` → IC=-0.236 (n=350)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.667
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=2690)

- **PATRÓN** `ibs_20min` > `0.7636` → IC=+0.286 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7636 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `1.0156` → IC=+0.337 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0156 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.734` → IC=+0.168 (n=474)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.734 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8566` → IC=+0.315 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8566 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.6339` → IC=+0.307 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6339 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.304 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.333 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.8034` → IC=+0.317 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8034 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `2.4149` → IC=+0.302 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4149 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.331 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.5625` → IC=+0.133 (n=2012)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5625 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.2679` → IC=+0.239 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2679 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `0.7014` → IC=+0.261 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7014 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.233 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.254 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.251 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.264 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.023)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.334 (n=1501)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.309 (n=792)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.323 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2129` → IC=+0.320 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2129 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.776` → IC=+0.313 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.776 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.947` → IC=+0.291 (n=1900)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.947 (IC base=+0.290)

- **PATRÓN** `volumen_regimen` > `0.8578` → IC=+0.315 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8578 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.338 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` > `1.4333` → IC=+0.302 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4333 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `2663.9798` → IC=+0.307 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2663.9798 (IC base=+0.290)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.327 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.321 (n=1195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.187` → IC=+0.290 (n=789)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.187 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.297 (n=899)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.289)

- **PATRÓN** `ibs_20min` < `0.3676` → IC=+0.315 (n=1792)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3676 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.3086` → IC=+0.293 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3086 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.512` → IC=+0.302 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.512 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.01` → IC=+0.290 (n=2137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.01 (IC base=+0.289)

- **PATRÓN** `volumen_regimen` > `1.2282` → IC=+0.320 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2282 (IC base=+0.289)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.337 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` < `1.4206` → IC=+0.299 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4206 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` > `2.1367` → IC=+0.288 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1367 (IC base=+0.289)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.189 (n=3501)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0047 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.209 (n=3488)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3504` → IC=+0.186 (n=9196)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3504 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=10902)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.5668` → IC=+0.228 (n=10449)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5668 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.1712` → IC=+0.200 (n=4433)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1712 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.483` → IC=+0.251 (n=2104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.483 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.2054` → IC=+0.168 (n=6949)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2054 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` > `0.6287` → IC=+0.162 (n=6949)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6287 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2951` → IC=+0.197 (n=1544)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2951 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.4519` → IC=+0.175 (n=3362)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4519 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.6063` → IC=+0.183 (n=3362)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6063 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `2009.99` → IC=+0.180 (n=9335)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2009.99 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.190 (n=9380)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 104.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.190 (n=6711)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0065 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0808` → IC=+0.223 (n=3350)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0808 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=3806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.4839` → IC=+0.234 (n=10051)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4839 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.3` → IC=+0.201 (n=1674)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.3 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1822` → IC=+0.166 (n=7198)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1822 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.224 (n=1471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `1.5576` → IC=+0.176 (n=4111)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.5576 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.613` → IC=+0.180 (n=3113)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.613 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.188 (n=9011)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 106.0 (IC base=+0.178)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.233 (n=587)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.206 (n=586)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3383` → IC=+0.220 (n=1753)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3383 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=1855)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.204 (n=1169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.335` → IC=+0.329 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.335 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.258 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.2345` → IC=+0.207 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2345 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1824)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2009.99` → IC=+0.201 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.99 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0041` → IC=+0.250 (n=1349)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0041 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.0702` → IC=+0.304 (n=452)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0702 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.249 (n=1291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.244 (n=1247)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.263 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.224` → IC=+0.249 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.224 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` < `0.099` → IC=+0.242 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.099 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.280 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` < `1.4252` → IC=+0.257 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4252 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.245 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.243)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.226 (n=527)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.1649` → IC=+0.185 (n=1050)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1649 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=1575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.3865` → IC=+0.223 (n=1574)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3865 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.1998` → IC=+0.213 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1998 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.523` → IC=+0.232 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.523 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.6895` → IC=+0.171 (n=693)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6895 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.0753` → IC=+0.159 (n=714)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.0753 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.197 (n=249)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.4139` → IC=+0.185 (n=512)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4139 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `11955.6489` → IC=+0.160 (n=1406)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11955.6489 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.174 (n=658)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 233.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1666)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2309` → IC=+0.175 (n=1464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2309 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.5923` → IC=+0.201 (n=1664)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5923 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1393` → IC=+0.171 (n=1669)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1393 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.828` → IC=+0.209 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.828 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2077` → IC=+0.164 (n=1663)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2077 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.2288` → IC=+0.146 (n=1717)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.2288 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.150 (n=506)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4919` → IC=+0.153 (n=1549)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4919 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.77` → IC=+0.145 (n=1032)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.77 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.169 (n=493)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 207.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.230 (n=583)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.406` → IC=+0.218 (n=1539)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.406 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.557` → IC=+0.277 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.557 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` < `0.0964` → IC=+0.206 (n=1480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0964 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.1273` → IC=+0.209 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1273 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.7659` → IC=+0.209 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7659 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.6894` → IC=+0.213 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6894 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=2081)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `1972.2784` → IC=+0.225 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1972.2784 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.244 (n=1323)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1448` → IC=+0.267 (n=662)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1448 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.278 (n=517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.3478` → IC=+0.251 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3478 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.671` → IC=+0.262 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.671 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.3494` → IC=+0.264 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3494 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.7186` → IC=+0.245 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7186 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.7161` → IC=+0.234 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7161 (IC base=+0.229)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.229 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.229)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.181 (n=1482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0064 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.200 (n=561)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=1751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.3311` → IC=+0.205 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3311 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.141` → IC=+0.188 (n=1069)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.141 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.002` → IC=+0.205 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.002 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.158 (n=1121)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.856 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1014` → IC=+0.170 (n=700)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1014 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4335` → IC=+0.164 (n=549)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4335 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5111` → IC=+0.157 (n=549)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.5111 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5095.3746` → IC=+0.194 (n=1120)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 5095.3746 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.151 (n=1622)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 150.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.162 (n=1558)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0061 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3811` → IC=+0.150 (n=1768)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3811 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6687` → IC=+0.186 (n=1768)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6687 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.868` → IC=+0.162 (n=608)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.868 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8568` → IC=+0.162 (n=1179)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8568 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.192 (n=271)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.8129` → IC=+0.141 (n=1094)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8129 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.5407` → IC=+0.138 (n=547)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5407 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `4511.3976` → IC=+0.167 (n=1179)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4511.3976 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.134 (n=1063)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 97.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.159 (n=867)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0098 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4402` → IC=+0.130 (n=1683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4402 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=1954)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.215 (n=1919)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1984` → IC=+0.185 (n=1162)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1984 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.935` → IC=+0.263 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.935 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.142 (n=1912)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2036 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.1645` → IC=+0.138 (n=1933)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.1645 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.5508` → IC=+0.141 (n=814)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5508 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.1636` → IC=+0.134 (n=839)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.1636 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=2006)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2388.5554` → IC=+0.188 (n=1275)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2388.5554 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.149 (n=1509)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 45.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.160 (n=850)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.006 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1048` → IC=+0.182 (n=643)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1048 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=1941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.5741` → IC=+0.221 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5741 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.7428` → IC=+0.124 (n=336)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.7428 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.372` → IC=+0.134 (n=585)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 5.372 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.18` → IC=+0.136 (n=1927)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.18 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.160 (n=242)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.4523` → IC=+0.141 (n=591)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4523 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2783.1673` → IC=+0.185 (n=874)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2783.1673 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.133 (n=1735)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 52.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.234 (n=1593)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2846` → IC=+0.221 (n=1190)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2846 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=1854)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.216 (n=1202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.249 (n=1784)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.1969` → IC=+0.215 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1969 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.2845` → IC=+0.212 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2845 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.596` → IC=+0.245 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.596 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `1.1848` → IC=+0.216 (n=1783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1848 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.220 (n=1783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6237 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.271 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `2.4727` → IC=+0.215 (n=1731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4727 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.8094` → IC=+0.225 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8094 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2649.2154` → IC=+0.221 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2649.2154 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.230 (n=810)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0223` → IC=+0.224 (n=837)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0223 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0901` → IC=+0.242 (n=614)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0901 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.237 (n=904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.0196` → IC=+0.291 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0196 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `1.1683` → IC=+0.232 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1683 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.402` → IC=+0.249 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.402 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6367` → IC=+0.231 (n=1841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6367 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.278 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `2.199` → IC=+0.212 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.199 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.4384` → IC=+0.219 (n=1693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4384 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2627.8785` → IC=+0.228 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2627.8785 (IC base=+0.220)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.192 (n=1216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0041 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3327` → IC=+0.178 (n=2419)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3327 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.204 (n=1364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.3277` → IC=+0.196 (n=2749)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3277 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.7767` → IC=+0.184 (n=428)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.7767 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.768` → IC=+0.192 (n=1178)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.768 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.869` → IC=+0.185 (n=1647)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.869 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.2045` → IC=+0.176 (n=823)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.2045 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1028` → IC=+0.175 (n=987)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1028 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.185 (n=890)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.5236` → IC=+0.169 (n=890)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5236 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=2540)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2800.762` → IC=+0.167 (n=2456)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2800.762 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.185 (n=2528)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 149.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.161 (n=942)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0036 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=2666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.0757` → IC=+0.198 (n=942)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.0757 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2044` → IC=+0.123 (n=2569)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.2044 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.2216` → IC=+0.120 (n=2570)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.2216 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.128 (n=1082)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4381` → IC=+0.149 (n=915)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4381 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2839.1196` → IC=+0.134 (n=2524)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2839.1196 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.134 (n=923)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 21.0 (IC base=+0.114)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.201 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1007` → IC=+0.201 (n=349)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1007 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=729)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.6275` → IC=+0.206 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6275 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.172 (n=248)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.203` → IC=+0.176 (n=334)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.203 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.8817` → IC=+0.176 (n=529)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8817 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.155 (n=314)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.22` → IC=+0.162 (n=682)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.22 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.4164` → IC=+0.152 (n=774)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4164 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `14720.7097` → IC=+0.157 (n=528)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 14720.7097 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.203 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.204 (n=309)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2654` → IC=+0.164 (n=817)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2654 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.153 (n=832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.148 (n=936)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.186 (n=816)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6112 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.765` → IC=+0.148 (n=177)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.765 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.506` → IC=+0.149 (n=979)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.506 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.208` → IC=+0.148 (n=927)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.208 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.7005` → IC=+0.158 (n=828)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7005 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.203 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.1142` → IC=+0.161 (n=806)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1142 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.4038` → IC=+0.151 (n=916)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4038 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=1200)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.161 (n=788)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 288.0 (IC base=+0.147)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.233 (n=586)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.2048` → IC=+0.211 (n=583)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2048 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=918)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.252 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.3578` → IC=+0.204 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3578 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` < `0.2092` → IC=+0.201 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2092 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.057` → IC=+0.217 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.057 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.8392` → IC=+0.197 (n=583)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8392 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` > `1.1833` → IC=+0.221 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1833 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.227 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.231 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.4553` → IC=+0.217 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4553 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.137 (n=737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.006 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.134 (n=279)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.0876` → IC=+0.167 (n=280)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.0876 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.411` → IC=+0.154 (n=218)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 6.411 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.6874` → IC=+0.162 (n=368)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6874 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.424` → IC=+0.145 (n=271)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.424 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `4111.5445` → IC=+0.137 (n=748)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 4111.5445 (IC base=+0.112)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.135 (n=349)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 41.0 (IC base=+0.112)

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
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.180 (n=4530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.212 (n=4527)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=14183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.9891` → IC=+0.310 (n=4527)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9891 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.165` → IC=+0.187 (n=5035)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.165 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.428` → IC=+0.246 (n=3330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.428 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.2331` → IC=+0.167 (n=9102)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2331 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2895` → IC=+0.201 (n=1836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2895 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.5996` → IC=+0.196 (n=4381)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5996 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2452.9003` → IC=+0.180 (n=9051)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2452.9003 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.204 (n=10781)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.196 (n=5401)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0052 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.1463` → IC=+0.198 (n=5401)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1463 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=4629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.4512` → IC=+0.250 (n=10797)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4512 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.1749` → IC=+0.169 (n=7337)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1749 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.11` → IC=+0.213 (n=1729)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.11 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.73` → IC=+0.187 (n=11830)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.73 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `1.0604` → IC=+0.161 (n=7310)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0604 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.252 (n=1644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.2653` → IC=+0.194 (n=5209)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.2653 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.210 (n=7500)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.253 (n=750)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.226 (n=750)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=1088)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=1510)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.330 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.777` → IC=+0.349 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.777 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.271 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.5862` → IC=+0.227 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5862 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2006.13` → IC=+0.216 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2006.13 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.265 (n=1246)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.263 (n=1865)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.2028` → IC=+0.274 (n=1243)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2028 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.3594` → IC=+0.285 (n=1641)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3594 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.493` → IC=+0.266 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.493 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2858` → IC=+0.291 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2858 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `2.6332` → IC=+0.283 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6332 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2053)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.260)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.204 (n=738)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1785` → IC=+0.165 (n=1456)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1785 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2754` → IC=+0.206 (n=2183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2754 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1308` → IC=+0.187 (n=1192)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1308 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.715` → IC=+0.173 (n=365)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.715 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.23` → IC=+0.154 (n=1998)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.23 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6273` → IC=+0.175 (n=728)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6273 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.191 (n=312)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1442` → IC=+0.160 (n=1870)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1442 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5235` → IC=+0.153 (n=1899)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5235 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `248.0` → IC=+0.186 (n=692)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 248.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1815)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2551` → IC=+0.164 (n=1597)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2551 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6835` → IC=+0.195 (n=1815)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6835 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1343` → IC=+0.166 (n=1677)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1343 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.539` → IC=+0.169 (n=309)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.539 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.1888` → IC=+0.158 (n=1815)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1888 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1542` → IC=+0.202 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1542 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.154 (n=1713)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7751` → IC=+0.160 (n=1142)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7751 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `348.0` → IC=+0.146 (n=1086)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 348.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.232 (n=2229)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=1999)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.503` → IC=+0.306 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.503 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.204` → IC=+0.225 (n=2256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.204 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.7627` → IC=+0.230 (n=1920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7627 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2655)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1982.1984` → IC=+0.234 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1982.1984 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.243 (n=1401)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.1813` → IC=+0.255 (n=924)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1813 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.238 (n=762)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0146` → IC=+0.302 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0146 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.96` → IC=+0.287 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.96 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.3416` → IC=+0.296 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3416 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.7145` → IC=+0.244 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7145 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.128` → IC=+0.240 (n=1316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.128 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.258 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.236)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=1029)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3325` → IC=+0.152 (n=2044)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3325 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=2420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.2672` → IC=+0.191 (n=2322)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2672 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1397` → IC=+0.157 (n=1288)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1397 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.171` → IC=+0.152 (n=947)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.171 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8732` → IC=+0.162 (n=1549)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8732 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1662` → IC=+0.175 (n=611)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1662 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5247` → IC=+0.164 (n=995)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5247 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.1809` → IC=+0.150 (n=1025)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1809 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7316.6924` → IC=+0.236 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7316.6924 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.180 (n=743)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 70.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.195 (n=631)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0033 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.3439` → IC=+0.146 (n=1652)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3439 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.136 (n=660)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7338` → IC=+0.187 (n=1878)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.7338 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.337` → IC=+0.179 (n=381)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.337 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8747` → IC=+0.143 (n=1253)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8747 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.234 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4416` → IC=+0.145 (n=1802)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4416 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `5639.5091` → IC=+0.197 (n=852)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 5639.5091 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.136 (n=1801)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 165.0 (IC base=+0.133)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.137 (n=2341)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0055 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.4524` → IC=+0.202 (n=2340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4524 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `1.0156` → IC=+0.212 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0156 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.051` → IC=+0.258 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.051 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.2342` → IC=+0.140 (n=2340)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2342 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.130 (n=2414)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.131 (n=310)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.1972` → IC=+0.142 (n=1033)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.1972 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=2392)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2571.2845` → IC=+0.237 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2571.2845 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.149 (n=734)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 27.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.158 (n=1492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0077 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1305` → IC=+0.171 (n=746)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1305 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.235 (n=1978)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.2159` → IC=+0.141 (n=1872)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2159 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.133 (n=306)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.486` → IC=+0.136 (n=2159)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.486 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.7132` → IC=+0.158 (n=984)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7132 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.182 (n=363)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `2.1548` → IC=+0.142 (n=1819)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1548 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2815.4542` → IC=+0.203 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2815.4542 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.142 (n=1819)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 50.0 (IC base=+0.124)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.235 (n=2258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=2360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.224 (n=1630)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.267 (n=2021)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.2066` → IC=+0.235 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2066 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.623` → IC=+0.259 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.623 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.2332` → IC=+0.224 (n=2258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2332 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6415` → IC=+0.224 (n=2258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6415 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.246 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.5125` → IC=+0.246 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5125 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=2079)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `2662.6144` → IC=+0.230 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2662.6144 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.222 (n=797)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.233 (n=1079)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.232 (n=1688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.4167` → IC=+0.266 (n=2097)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4167 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.897` → IC=+0.254 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.897 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.248 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.287 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.4316` → IC=+0.219 (n=2188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4316 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.211 (n=2116)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.218)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.172 (n=4029)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.230 (n=1364)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.3903` → IC=+0.200 (n=3593)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3903 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=1508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.194 (n=1846)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `0.9399` → IC=+0.242 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9399 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.1709` → IC=+0.198 (n=1505)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1709 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.247` → IC=+0.216 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.247 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.201 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` > `1.2573` → IC=+0.199 (n=958)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 1.2573 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.1688` → IC=+0.220 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1688 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `1.4563` → IC=+0.197 (n=1341)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4563 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `1.8658` → IC=+0.196 (n=2681)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.8658 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=3063)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `3858.5308` → IC=+0.203 (n=2722)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3858.5308 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.221 (n=1015)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.4847` → IC=+0.187 (n=3034)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.4847 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=1043)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.190 (n=1380)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.1747` → IC=+0.193 (n=1335)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1747 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.6442` → IC=+0.180 (n=536)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6442 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.181` → IC=+0.178 (n=3027)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.181 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.2534` → IC=+0.176 (n=2866)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.2534 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.175 (n=2769)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.178 (n=1380)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5399` → IC=+0.175 (n=1317)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.5399 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.181 (n=1995)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=4029)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.184 (n=1006)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 25.0 (IC base=+0.171)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.239 (n=355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.211)

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

- **PATRÓN** `volumen_regimen` > `0.5963` → IC=+0.221 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5963 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.232 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `12537.6672` → IC=+0.237 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12537.6672 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.228 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1116` → IC=+0.178 (n=467)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1116 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.198 (n=356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 4.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.144` → IC=+0.182 (n=467)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.144 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.6071` → IC=+0.153 (n=482)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6071 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6649` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6649 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.211` → IC=+0.150 (n=1077)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.211 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.385` → IC=+0.166 (n=1045)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.385 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8817` → IC=+0.187 (n=708)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8817 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2218` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2218 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.5397` → IC=+0.154 (n=1058)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5397 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.169 (n=705)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `11518.9437` → IC=+0.161 (n=1062)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11518.9437 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `700.0` → IC=+0.160 (n=1016)

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
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.211 (n=1090)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.458` → IC=+0.207 (n=1239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.458 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.201 (n=1282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.5174` → IC=+0.215 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5174 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.8799` → IC=+0.204 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8799 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.148` → IC=+0.206 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.148 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.204 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `1.2467` → IC=+0.206 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2467 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.198 (n=1141)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.1655` → IC=+0.210 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1655 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.424` → IC=+0.215 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.424 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.234 (n=329)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.195 (n=986)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.187 (n=388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 16.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.182 (n=664)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 10.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.7466` → IC=+0.178 (n=986)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7466 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.0817` → IC=+0.173 (n=986)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.0817 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.6317` → IC=+0.194 (n=194)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6317 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.168` → IC=+0.174 (n=1098)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 9.168 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.2516` → IC=+0.184 (n=986)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.2516 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.7236` → IC=+0.172 (n=881)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.7236 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.193 (n=415)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.1859` → IC=+0.185 (n=849)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.1859 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `7438.5832` → IC=+0.186 (n=986)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7438.5832 (IC base=+0.171)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.217 (n=358)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.3032` → IC=+0.181 (n=358)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3032 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.195 (n=549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 3.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.245 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.1937` → IC=+0.210 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1937 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.547` → IC=+0.220 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.547 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `0.6938` → IC=+0.210 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6938 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.225 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `1.468` → IC=+0.187 (n=522)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.468 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=644)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.02 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `3413.2842` → IC=+0.222 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3413.2842 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.190 (n=463)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 48.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.213 (n=134)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.211 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.3725` → IC=+0.236 (n=267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3725 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.216 (n=269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.1849` → IC=+0.242 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1849 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.7721` → IC=+0.227 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7721 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.053` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.053 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.987` → IC=+0.190 (n=346)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.987 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.7658` → IC=+0.197 (n=176)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.7658 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` > `0.6811` → IC=+0.186 (n=399)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6811 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.222 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.631` → IC=+0.188 (n=171)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.631 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.2075` → IC=+0.202 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2075 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `3873.4593` → IC=+0.198 (n=266)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3873.4593 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.223 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.185)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.155 (n=586)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0038 (IC base=+0.076)

- **PATRÓN** `ibs_20min` > `0.4284` → IC=+0.148 (n=1235)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.4284 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.1412` → IC=+0.140 (n=665)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1412 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.471` → IC=+0.180 (n=279)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.471 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.182 (n=171)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.076)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.139 (n=206)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0029 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.1926` → IC=+0.258 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1926 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` < `0.1228` → IC=+0.132 (n=561)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1228 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.169` → IC=+0.130 (n=466)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 4.169 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.1467` → IC=+0.196 (n=133)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1467 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `2.581` → IC=+0.138 (n=479)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.581 (IC base=+0.058)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.137 (n=453)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0057 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.122 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 8.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.5692` → IC=+0.194 (n=377)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.5692 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1286` → IC=+0.161 (n=219)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1286 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.517` → IC=+0.122 (n=247)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 3.517 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `2.4916` → IC=+0.123 (n=380)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4916 (IC base=+0.093)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.122 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0045 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.0582` → IC=+0.291 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0582 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.2024` → IC=+0.130 (n=287)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.2024 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.157` → IC=+0.144 (n=251)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 7.157 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` < `2.5247` → IC=+0.136 (n=234)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.5247 (IC base=+0.080)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.7006` → IC=-0.186 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7006
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=150)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.147 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0046 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.127 (n=408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.6845` → IC=+0.200 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6845 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1226` → IC=+0.171 (n=220)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1226 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.373` → IC=+0.274 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.373 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `1179.0901` → IC=+0.141 (n=357)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1179.0901 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.1031` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1031 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.3422` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.3422 (IC base=+0.013)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.01` → IC=-0.202 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=166)

- **FILTRO** `ibs_20min` > `0.1667` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1667
  - _Potencial_: sin este filtro IC_bueno=+0.261 (n=136)

- **PATRÓN** `ibs_20min` > `0.7609` → IC=+0.173 (n=273)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.7609 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `0.7176` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.7176 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2448` → IC=+0.187 (n=81)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2448 (IC base=+0.043)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.190 (n=111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0061 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.261 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1667 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.1905` → IC=+0.155 (n=137)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1905 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.949` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.949 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.6561` → IC=+0.129 (n=60)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.6561 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` > `1.0544` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0544 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.0818` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0818 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `2.18` → IC=+0.186 (n=100)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.18 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` > `2.5569` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5569 (IC base=+0.065)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.200 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `774.2903` → IC=+0.171 (n=80)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 774.2903 (IC base=+0.065)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1828` → IC=-0.303 (n=64)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1828
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=196)

- **FILTRO** `dist_vwap_pct` > `0.2351` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2351
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=246)

- **FILTRO** `volumen_regimen` < `0.7446` → IC=-0.336 (n=65)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7446
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=197)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.379 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=170)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.297 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=159)

- **FILTRO** `dist_vwap_pct` > `0.3328` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3328
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=193)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=196)

- **FILTRO** `volumen_pendiente_norm` > `0.0718` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=121)

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
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=73)

- **FILTRO** `sigma_ewma_delta_pct` > `2.482` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.482
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=65)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=73)

- **FILTRO** `volumen_regimen` < `0.5547` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.5547
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=73)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0026` → IC=-0.370 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=66)

- **FILTRO** `ibs_20min` < `0.6002` → IC=-0.467 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6002
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=59)

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
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.174 (n=185)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0057 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.128 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.6592` → IC=+0.139 (n=408)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.6592 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.4828` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.4828 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `1.5367` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5367 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.1558` → IC=+0.169 (n=397)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1558 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.348` → IC=+0.209 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.348 (IC base=+0.080)

- **PATRÓN** `libro_liquidez` > `2762.0501` → IC=+0.152 (n=300)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2762.0501 (IC base=+0.080)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6472` → IC=-0.267 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6472
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=124)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.189 (n=181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0024 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.158 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.1361` → IC=+0.206 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1361 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.925` → IC=+0.175 (n=161)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 4.925 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.627` → IC=+0.176 (n=202)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.627 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.1907` → IC=+0.182 (n=171)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1907 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.2815` → IC=+0.184 (n=150)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.2815 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.5807` → IC=+0.165 (n=153)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.5807 (IC base=+0.153)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1606` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1606
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=113)

- **PATRÓN** `volumen_spike_ratio` < `1.378` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.378 (IC base=+0.048)

- **PATRÓN** `libro_liquidez` > `1532.5809` → IC=+0.122 (n=133)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1532.5809 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.1906` → IC=+0.151 (n=144)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.1906 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.8233` → IC=+0.125 (n=110)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.8233 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.218` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.218 (IC base=+0.068)

- **PATRÓN** `libro_liquidez` > `1982.4493` → IC=+0.136 (n=75)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1982.4493 (IC base=+0.068)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.1679` → IC=-0.207 (n=56)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1679
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=57)

- **FILTRO** `dist_vwap_pct` > `0.2725` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2725
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=91)

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

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.1575` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_pendiente_norm` > 0.1575 (IC base=-0.074)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=1012)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2861.976` → IC=+0.131 (n=472)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2861.976 (IC base=+0.101)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=1012)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2861.976` → IC=+0.131 (n=472)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2861.976 (IC base=+0.101)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=121)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=153)

- **FILTRO** `libro_liquidez` < `2625.3641` → IC=-0.273 (n=42)

  - _Acción_: SKIP cuando `libro_liquidez` < 2625.3641
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=127)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=246)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=232)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=52)

- **FILTRO** `hora_utc` < `3.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=56)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2818)

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
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=109)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.132 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 13.0 (IC base=+0.046)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.130 (n=179)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.495 (IC base=+0.037)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1055)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1009)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=645)

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
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=775)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=775)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=609)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=580)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=580)

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
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=145)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=169)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=165)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=303)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=303)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=209)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.127 (n=1348)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1433)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.144 (n=614)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.47 (IC base=+0.020)

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
- **FILTRO** `py_entrada` < `0.5` → IC=-0.139 (n=178)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=92)

- **PATRÓN** `py_entrada` < `0.48` → IC=+0.125 (n=118)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.48 (IC base=+0.018)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.229 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.052)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `restante_min` < `8.84` → IC=-0.174 (n=44)

  - _Acción_: SKIP cuando `restante_min` < 8.84
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=135)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=126)

- **FILTRO** `lag_apertura_s` > `369.74` → IC=-0.174 (n=44)

  - _Acción_: SKIP cuando `lag_apertura_s` > 369.74
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=135)

- **FILTRO** `profundidad_ratio` < `22.8` → IC=-0.137 (n=89)

  - _Acción_: SKIP cuando `profundidad_ratio` < 22.8
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=90)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.159 (n=83)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=101)

- **FILTRO** `restante_min` < `3.7` → IC=-0.128 (n=92)

  - _Acción_: SKIP cuando `restante_min` < 3.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=92)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.152 (n=185)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=64)

- **FILTRO** `profundidad_ratio` < `37.3` → IC=-0.203 (n=62)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.3
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=187)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.229 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=188)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.46 (IC base=-0.013)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.131 (n=201)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=114)

- **FILTRO** `restante_min` < `3.34` → IC=-0.195 (n=103)

  - _Acción_: SKIP cuando `restante_min` < 3.34
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=212)

- **FILTRO** `lag_apertura_s` > `97.61` → IC=-0.206 (n=107)

  - _Acción_: SKIP cuando `lag_apertura_s` > 97.61
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=208)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.130 (n=52)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=189)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.126 (n=89)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.5 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.141 (n=193)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.137 (n=100)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.137 (n=100)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` > 0.5 (IC base=-0.046)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.197 (n=87)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=280)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.170 (n=4595)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=14899)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.166 (n=5011)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=15211)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.195 (n=840)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=2630)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.151 (n=849)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=2777)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.121 (n=1677)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.174 (n=701)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2220)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.177 (n=875)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=2645)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.183 (n=911)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=2758)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.163 (n=835)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=2636)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2542)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3282)

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
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=306)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=377)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `2015.008` → IC=-0.164 (n=337)

  - _Acción_: SKIP cuando `libro_liquidez` < 2015.008
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=686)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=13594)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=30226)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=10348)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=33472)

- **FILTRO** `ibs_7min` < `0.2556` → IC=-0.233 (n=10953)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2556
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=32867)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.155 (n=14711)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=29109)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.236 (n=13418)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=42348)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.178 (n=13925)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=41841)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.144 (n=2204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=5249)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.235 (n=3685)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=3768)

- **FILTRO** `ibs_7min` < `0.7089` → IC=-0.251 (n=2458)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7089
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=4995)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.189 (n=1580)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5873)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.269 (n=2356)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=7329)

- **FILTRO** `ibs_7min` > `0.7778` → IC=-0.211 (n=2421)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=7264)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=1789)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=5696)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.247 (n=1853)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=5632)

- **FILTRO** `ibs_7min` < `0.7392` → IC=-0.197 (n=1870)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7392
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5615)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.183 (n=1862)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=5623)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=1813)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=5804)

- **FILTRO** `ibs_7min` > `0.2651` → IC=-0.191 (n=1904)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2651
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5713)

- **FILTRO** `ballena_activa_n` > `148.0` → IC=-0.190 (n=1896)

  - _Acción_: SKIP cuando `ballena_activa_n` > 148.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5721)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.165 (n=1771)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=5345)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=1688)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5428)

- **FILTRO** `ibs_7min` < `0.7032` → IC=-0.246 (n=2348)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7032
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4768)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.219 (n=1588)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5528)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.244 (n=2321)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=7976)

- **FILTRO** `ibs_7min` > `0.7341` → IC=-0.172 (n=2574)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7341
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=7723)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=2342)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4859)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.240 (n=2142)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5059)

- **FILTRO** `ibs_7min` < `0.7398` → IC=-0.185 (n=1800)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7398
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5401)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.186 (n=1771)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5430)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.270 (n=1824)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=5611)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.181 (n=1858)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5577)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.183 (n=1789)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5646)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.271 (n=1738)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=5645)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.233 (n=1837)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5546)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.174 (n=2654)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=7977)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.280 (n=1723)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=5459)

- **FILTRO** `ibs_7min` < `0.24` → IC=-0.225 (n=1791)

  - _Acción_: SKIP cuando `ibs_7min` < 0.24
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5391)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.202 (n=1748)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5434)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.205 (n=2459)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=7642)

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

- **FILTRO** `libro_liquidez` < `3306.2556` → IC=-0.155 (n=166)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.2556
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=498)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=256)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.141 (n=962)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.140 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.130 (n=360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 4.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `442.4725` → IC=+0.159 (n=321)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 442.4725 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `4345.4042` → IC=+0.129 (n=321)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 4345.4042 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.149 (n=314)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 14.0 (IC base=+0.128)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4374` → IC=+0.162 (n=75)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4374 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.234 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `2641.0058` → IC=+0.253 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2641.0058 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.202 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.149)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 10.0 (IC base=+0.107)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4144` → IC=+0.184 (n=131)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.4144 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.219 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `7275.4252` → IC=+0.133 (n=175)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 7275.4252 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 73.0 (IC base=+0.124)

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
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.135 (n=165)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.124 (n=163)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 13.0 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=114)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `3635.4092` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3635.4092 (IC base=+0.099)

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
- **FILTRO** `sigma_h` > `0.0081` → IC=-0.206 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0081
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=50)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0048` → IC=-0.188 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.137 (n=370)

- **FILTRO** `T_h` < `87.9844` → IC=-0.159 (n=162)

  - _Acción_: SKIP cuando `T_h` < 87.9844
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=331)

- **FILTRO** `sigma_h` > `0.0089` → IC=-0.315 (n=106)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=323)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.317 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=322)

- **FILTRO** `T_h` > `56.6209` → IC=-0.305 (n=321)

  - _Acción_: SKIP cuando `T_h` > 56.6209
  - _Potencial_: sin este filtro IC_bueno=-0.127 (n=108)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.384 (n=41)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=129)

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
- **FILTRO** `sigma_h` < `0.0049` → IC=-0.266 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=92)

- **FILTRO** `T_h` < `87.9918` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `T_h` < 87.9918
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=92)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=255)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=341)

- **PATRÓN** `streak_estiramiento` < `0.4511` → IC=+0.121 (n=85)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.4511 (IC base=+0.022)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=589)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=822)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=964)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=973)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3500)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1856)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.198 (n=863)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0043 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.230 (n=861)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.202 (n=2275)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.194)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2233` → IC=+0.197 (n=863)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio_macro` |x|> 0.2233 (IC base=+0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1312` → IC=+0.216 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1312 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.203 (n=2384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.196 (n=2666)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `ibs_15` > `0.6047` → IC=+0.268 (n=2584)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6047 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.1201` → IC=+0.194 (n=1238)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1201 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.887` → IC=+0.268 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.887 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `6960.2205` → IC=+0.201 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6960.2205 (IC base=+0.194)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=1096)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.229 (n=437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.274 (n=166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.215)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1442` → IC=+0.238 (n=330)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1442 (IC base=+0.215)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1075` → IC=+0.254 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1075 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_15` > `0.7143` → IC=+0.279 (n=496)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7143 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.246 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.268 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `16201.6469` → IC=+0.250 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16201.6469 (IC base=+0.215)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.513` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.513
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=636)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.165 (n=183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0034 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.067` → IC=+0.147 (n=242)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.067 (IC base=+0.134)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2372` → IC=+0.160 (n=183)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.2372 (IC base=+0.134)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.151 (n=210)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.138 (n=573)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.134)

- **PATRÓN** `ibs_15` > `0.5749` → IC=+0.230 (n=549)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5749 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.1542` → IC=+0.136 (n=295)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1542 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1542` → IC=+0.134 (n=438)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1542 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.901` → IC=+0.259 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.901 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `7693.0802` → IC=+0.145 (n=249)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 7693.0802 (IC base=+0.134)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `20.51` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.51
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=220)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.239 (n=136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1772` → IC=+0.194 (n=361)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1772 (IC base=+0.154)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0624` → IC=+0.166 (n=408)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio_macro` |x|> 0.0624 (IC base=+0.154)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3438` → IC=+0.182 (n=360)

  - _Acción_: Kelly boost +0.91€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3438 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.172 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.155 (n=424)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 17.0 (IC base=+0.154)

- **PATRÓN** `ibs_15` > `0.9322` → IC=+0.362 (n=136)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9322 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.33` → IC=+0.169 (n=418)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.33 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.221 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=260)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2554.4704` → IC=+0.156 (n=408)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2554.4704 (IC base=+0.154)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.407` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.407 (IC base=+0.018)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.256 (n=552)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.219 (n=272)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.214)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0442` → IC=+0.217 (n=619)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0442 (IC base=+0.214)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0894` → IC=+0.261 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0894 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.228 (n=546)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.214)

- **PATRÓN** `ibs_15` > `0.5849` → IC=+0.293 (n=618)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5849 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.1329` → IC=+0.224 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1329 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.77` → IC=+0.248 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.77 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2964.7894` → IC=+0.298 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2964.7894 (IC base=+0.214)

- **PATRÓN** `ibs_15` < `0.1089` → IC=+0.158 (n=661)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1089 (IC base=+0.070)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.363 (n=357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.359)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.379 (n=179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.359)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.359 (n=359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.359)

- **PATRÓN** `drift_15min` |x|≤ `0.4043` → IC=+0.362 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4043 (IC base=+0.359)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.383 (n=356)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.359)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1362` → IC=+0.390 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1362 (IC base=+0.359)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.374 (n=540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.359)

- **PATRÓN** `ibs_15` > `0.8305` → IC=+0.406 (n=478)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8305 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.388 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.247` → IC=+0.372 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.247 (IC base=+0.359)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `3836.614` → IC=+0.371 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3836.614 (IC base=+0.359)

- **PATRÓN** `ballena_activa_n` < `441.0` → IC=+0.378 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 441.0 (IC base=+0.359)

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
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.355 (n=164)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.357)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.377 (n=112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.357)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.368 (n=165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.357)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.374 (n=221)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.357)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2986` → IC=+0.381 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2986 (IC base=+0.357)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.416 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.357)

- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.403 (n=246)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.357)

- **PATRÓN** `dist_vwap_pct` > `0.4406` → IC=+0.365 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4406 (IC base=+0.357)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.359 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.377 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.356 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.357)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.357)

- **PATRÓN** `libro_liquidez` > `4286.2041` → IC=+0.381 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4286.2041 (IC base=+0.357)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.363 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 145.0 (IC base=+0.357)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.225 (n=909)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2730)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.208 (n=1367)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2272)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1406` → IC=+0.185 (n=583)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.1406 (IC base=-0.068)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.228 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.068)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.277 (n=876)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1071` → IC=+0.199 (n=489)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1071 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2614` → IC=+0.195 (n=736)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2614 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1312` → IC=+0.261 (n=1923)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1312 (IC base=-0.014)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3241` → IC=+0.253 (n=2823)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3241 (IC base=-0.014)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.282 (n=2885)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.014)

- **PATRÓN** `dist_vwap_pct` > `0.8548` → IC=+0.297 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8548 (IC base=-0.014)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.252 (n=2521)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=-0.014)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.208 (n=515)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1547)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.229 (n=515)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=1547)

- **FILTRO** `sigma_ewma_delta_pct` > `23.641` → IC=-0.261 (n=295)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.641
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=1767)

- **FILTRO** `libro_liquidez` < `16304.1531` → IC=-0.197 (n=1360)

  - _Acción_: SKIP cuando `libro_liquidez` < 16304.1531
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=702)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.178 (n=206)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0027 (IC base=+0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1417` → IC=+0.290 (n=174)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1417 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.314 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.120 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 12.0 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.7503` → IC=+0.329 (n=261)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7503 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.0996` → IC=+0.294 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0996 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.4928` → IC=+0.295 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4928 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.533` → IC=+0.126 (n=303)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 8.533 (IC base=+0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.226 (n=49)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.190)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.304 (n=49)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.190)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.190)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.414 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.190)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=563)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.152 (n=383)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0057 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.159 (n=435)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0033 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1111` → IC=+0.183 (n=291)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1111 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1409` → IC=+0.154 (n=290)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.1409 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.193 (n=324)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.172 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.6395` → IC=+0.248 (n=435)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6395 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.5943` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.5943 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.266` → IC=+0.153 (n=413)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.266 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=563)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `11133.475` → IC=+0.173 (n=145)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 11133.475 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.253 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.3441` → IC=+0.240 (n=893)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3441 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `0.7547` → IC=+0.251 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7547 (IC base=+0.239)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2117` → IC=+0.265 (n=461)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2117 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.268 (n=343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.239)

- **PATRÓN** `ibs_15` < `0.3647` → IC=+0.270 (n=1015)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3647 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.7509` → IC=+0.305 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7509 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.34` → IC=+0.260 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.34 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.558` → IC=+0.244 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.558 (IC base=+0.239)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.171` → IC=-0.246 (n=286)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.171
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=557)

- **FILTRO** `drift_15min` |x|> `0.8825` → IC=-0.278 (n=210)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8825
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=633)

- **FILTRO** `sigma_ewma_delta_pct` > `6.672` → IC=-0.184 (n=207)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.672
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=636)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.256 (n=84)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=759)

- **FILTRO** `sigma_ewma_delta_pct` > `18.28` → IC=-0.146 (n=439)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.28
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3516)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.174 (n=44)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.179)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.238 (n=59)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=-0.179)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.179)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.179)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.179)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0787` → IC=+0.243 (n=407)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0787 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.287 (n=458)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.171` → IC=+0.248 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.171 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1258` → IC=-0.227 (n=510)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1258
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=512)

- **FILTRO** `sigma_h` > `0.0192` → IC=-0.254 (n=510)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0192
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=512)

- **FILTRO** `drift_60min` |x|> `0.1534` → IC=-0.204 (n=255)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1534
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=767)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.202)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1492` → IC=+0.285 (n=323)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1492 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1101` → IC=+0.307 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1101 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.296 (n=714)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7904` → IC=+0.354 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7904 (IC base=-0.026)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `dist_vwap_pct` > `0.1515` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1515 (IC base=+0.033)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1515` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1515 (IC base=+0.033)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.289 (n=777)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.288 (n=789)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.326 (n=296)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.292 (n=589)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.224` → IC=+0.308 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.224 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.322 (n=883)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.327 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.352 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `12848.0159` → IC=+0.309 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12848.0159 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.309 (n=160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.327 (n=160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2454` → IC=+0.309 (n=160)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2454 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.297 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.309 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8279` → IC=+0.315 (n=480)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8279 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2565` → IC=+0.333 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2565 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.360 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.285 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16334.7136` → IC=+0.333 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16334.7136 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.294 (n=270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.296 (n=404)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.318 (n=135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.290 (n=269)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3023` → IC=+0.309 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3023 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.304 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.330 (n=404)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2788` → IC=+0.310 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2788 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.656` → IC=+0.335 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.656 (IC base=+0.289)

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

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.202 (n=65)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.137 (n=133)

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
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6047 sube el IC de +0.194 a +0.268 en UPDOWN_GBM#15min (n=2584). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7143 sube el IC de +0.215 a +0.279 en UPDOWN_GBM#BTC#15min (n=496). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5749 sube el IC de +0.134 a +0.230 en UPDOWN_GBM#ETH#15min (n=549). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9322 sube el IC de +0.154 a +0.362 en UPDOWN_GBM#SOL#15min (n=136). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5849 sube el IC de +0.214 a +0.293 en UPDOWN_GBM#XRP#15min (n=618). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1089 sube el IC de +0.070 a +0.158 en UPDOWN_GBM#XRP#15min (n=661). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.068 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=876). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.014 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=2885). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7503 sube el IC de +0.088 a +0.329 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=261). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.190 a +0.304 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=49). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6395 sube el IC de +0.146 a +0.248 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=435). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3647 sube el IC de +0.239 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1015). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de -0.179 a +0.238 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=59). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.040 a +0.287 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=458). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.202 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.296 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=714). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.288 a +0.322 en UPDOWN_GBM_IBS_ALTO (n=883). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8279 sube el IC de +0.286 a +0.315 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=480). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.289 a +0.330 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=404). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8305 sube el IC de +0.359 a +0.406 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=478). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.358 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=290). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.357 a +0.403 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=246). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1600 | +0.090 | +175.71€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1600 | +0.090 | +175.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1229 | +0.095 | +148.67€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1229 | +0.095 | +148.67€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 268 | +0.067 | +11.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 268 | +0.067 | +11.32€ | 6 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 300 | +0.007 | +57.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 300 | +0.007 | +57.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 240 | +0.012 | +52.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 240 | +0.012 | +52.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 38 | +0.000 | +2.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 38 | +0.000 | +2.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 35019 | -0.084 | -4643.61€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1759 | -0.013 | -223.33€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 33260 | -0.087 | -4420.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4383 | -0.118 | -760.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4383 | -0.118 | -760.59€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1759 | -0.013 | -223.33€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1759 | -0.013 | -223.33€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4082 | -0.114 | -906.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4082 | -0.114 | -906.86€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9057 | +0.007 | -846.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9057 | +0.007 | -846.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8904 | -0.107 | -643.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8904 | -0.107 | -643.51€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6834 | -0.152 | -1263.18€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6834 | -0.152 | -1263.18€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 27184 | -0.019 | +3730.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 7029 | +0.002 | +1775.55€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 20155 | -0.027 | +1954.66€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 27184 | -0.019 | +3730.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 7029 | +0.002 | +1775.55€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 20155 | -0.027 | +1954.66€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 120317 | +0.114 | -5288.88€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 16595 | +0.183 | -492.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 515 | -0.043 | -62.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 95770 | +0.103 | -4460.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7437 | +0.104 | -273.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 15902 | +0.103 | -1089.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 56 | -0.155 | +9.14€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 15831 | +0.105 | -1086.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 23738 | +0.128 | -410.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4896 | +0.196 | -144.03€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 15880 | +0.116 | -167.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2920 | +0.089 | -77.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 15949 | +0.095 | -1228.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 63 | -0.100 | -2.83€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 15871 | +0.096 | -1214.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 25560 | +0.124 | -440.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6784 | +0.175 | -101.56€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 16062 | +0.107 | -273.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2702 | +0.101 | -56.90€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 23249 | +0.114 | -1267.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4739 | +0.190 | -263.94€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 418 | -0.007 | -8.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 16277 | +0.093 | -855.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1815 | +0.132 | -139.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 15919 | +0.102 | -853.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 57 | -0.042 | +10.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 15849 | +0.103 | -863.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 19219 | +0.194 | -1210.03€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 19219 | +0.194 | -1210.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4449 | +0.174 | -416.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4449 | +0.174 | -416.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2131 | +0.201 | -37.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2131 | +0.201 | -37.59€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4380 | +0.182 | -351.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4380 | +0.182 | -351.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3858 | +0.241 | -140.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3858 | +0.241 | -140.34€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4322 | +0.189 | -278.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4322 | +0.189 | -278.27€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 889 | +0.426 | -32.62€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 889 | +0.426 | -32.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 349 | +0.434 | -6.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 349 | +0.434 | -6.17€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 341 | +0.427 | -11.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 341 | +0.427 | -11.06€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 187 | +0.405 | -12.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 187 | +0.405 | -12.95€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 66822 | +0.199 | -4979.96€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 66822 | +0.199 | -4979.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 11497 | +0.183 | -1214.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 11497 | +0.183 | -1214.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 10760 | +0.224 | -381.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 10760 | +0.224 | -381.44€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 11473 | +0.177 | -1279.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 11473 | +0.177 | -1279.07€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10827 | +0.220 | -407.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10827 | +0.220 | -407.28€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 11074 | +0.202 | -742.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 11074 | +0.202 | -742.83€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 11191 | +0.193 | -954.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 11191 | +0.193 | -954.61€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 25473 | +0.118 | +248.11€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 25473 | +0.118 | +248.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 12651 | +0.121 | +193.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 12651 | +0.121 | +193.62€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 12822 | +0.115 | +54.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 12822 | +0.115 | +54.48€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1783 | +0.288 | -24.66€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1783 | +0.288 | -24.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 805 | +0.279 | -18.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 805 | +0.279 | -18.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 860 | +0.286 | -10.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 860 | +0.286 | -10.78€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 118 | +0.350 | +4.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 118 | +0.350 | +4.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 806 | +0.441 | +2.77€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 806 | +0.441 | +2.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 389 | +0.439 | -1.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 389 | +0.439 | -1.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 371 | +0.444 | +3.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 371 | +0.444 | +3.28€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1385 | +0.068 | -67.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 508 | +0.057 | -41.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 877 | +0.074 | -25.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1082 | +0.074 | -34.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 205 | +0.070 | -8.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 877 | +0.074 | -25.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 237 | +0.031 | -34.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 237 | +0.031 | -34.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 49100 | +0.100 | -1269.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3986 | +0.092 | +55.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 45114 | +0.100 | -1325.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 27203 | +0.104 | -303.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3986 | +0.092 | +55.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 23217 | +0.106 | -358.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 9781 | +0.109 | -20.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 9781 | +0.109 | -20.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 12116 | +0.081 | -946.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 12116 | +0.081 | -946.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 871 | +0.203 | -101.16€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 871 | +0.203 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 871 | +0.203 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 871 | +0.203 | -101.16€ | 2 | 4 |
| ✅ GBM_LATE_15M | 34241 | +0.089 | +17093.24€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 34241 | +0.089 | +17093.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5756 | +0.205 | +4491.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5756 | +0.205 | +4491.15€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 5086 | +0.178 | +3669.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5086 | +0.178 | +3669.99€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 6082 | +0.201 | +4628.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6082 | +0.201 | +4628.32€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 4836 | +0.035 | +1225.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4836 | +0.035 | +1225.85€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4888 | -0.030 | +1059.06€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4888 | -0.030 | +1059.06€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 7593 | -0.036 | +2018.86€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7593 | -0.036 | +2018.86€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 37126 | +0.087 | +19725.75€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 37126 | +0.087 | +19725.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7206 | +0.011 | +3673.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7206 | +0.011 | +3673.10€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7701 | +0.013 | +1643.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7701 | +0.013 | +1643.02€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5232 | +0.269 | +5416.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5232 | +0.269 | +5416.76€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 6305 | +0.012 | +1400.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 6305 | +0.012 | +1400.18€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6054 | +0.036 | +2402.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6054 | +0.036 | +2402.30€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4628 | +0.290 | +5190.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4628 | +0.290 | +5190.39€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 27330 | +0.176 | +21487.87€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 27330 | +0.176 | +21487.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4135 | +0.218 | +3489.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4135 | +0.218 | +3489.14€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4315 | +0.152 | +3167.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4315 | +0.152 | +3167.94€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4335 | +0.217 | +3617.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4335 | +0.217 | +3617.67€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4597 | +0.138 | +3407.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4597 | +0.138 | +3407.16€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5117 | +0.127 | +3772.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5117 | +0.127 | +3772.98€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4831 | +0.215 | +4032.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4831 | +0.215 | +4032.99€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7431 | +0.140 | +3601.66€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7431 | +0.140 | +3601.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 341 | +0.141 | +188.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 341 | +0.141 | +188.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2291 | +0.148 | +1293.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2291 | +0.148 | +1293.93€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2280 | +0.154 | +1124.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2280 | +0.154 | +1124.63€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1607 | +0.108 | +579.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1607 | +0.108 | +579.43€ | 1 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 537 | +0.135 | +240.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 537 | +0.135 | +240.44€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 34460 | +0.182 | +26810.96€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 34460 | +0.182 | +26810.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5480 | +0.233 | +4910.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5480 | +0.233 | +4910.81€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5329 | +0.148 | +3509.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5329 | +0.148 | +3509.11€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5770 | +0.229 | +5063.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5770 | +0.229 | +5063.80€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5599 | +0.137 | +3906.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5599 | +0.137 | +3906.50€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6099 | +0.126 | +4237.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6099 | +0.126 | +4237.24€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6183 | +0.218 | +5183.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6183 | +0.218 | +5183.49€ | 0 | 21 |
| ✅ GBM_LATE_5M | 9487 | +0.183 | +6630.33€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 9487 | +0.183 | +6630.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 842 | +0.230 | +739.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 842 | +0.230 | +739.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2120 | +0.169 | +1531.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2120 | +0.169 | +1531.92€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 992 | +0.176 | +650.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 992 | +0.176 | +650.38€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 2965 | +0.186 | +2015.03€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2965 | +0.186 | +2015.03€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 1247 | +0.177 | +858.31€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1247 | +0.177 | +858.31€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1321 | +0.174 | +835.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1321 | +0.174 | +835.55€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2591 | +0.070 | +918.94€ | 0 | 11 |
| ✅ GBM_LATE_60M#60min | 2591 | +0.070 | +918.94€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 977 | +0.088 | +352.93€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 977 | +0.088 | +352.93€ | 0 | 12 |
| ✅ GBM_LATE_60M#ETH | 807 | +0.069 | +348.88€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 807 | +0.069 | +348.88€ | 1 | 9 |
| ✅ GBM_LATE_60M#SOL | 807 | +0.049 | +217.13€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 807 | +0.049 | +217.13€ | 2 | 14 |
| 🚫 GBM_LATE_60M_FADE | 488 | -0.239 | -14.88€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 488 | -0.239 | -14.88€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 184 | -0.231 | -11.13€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 184 | -0.231 | -11.13€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 171 | -0.217 | +1.92€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 171 | -0.217 | +1.92€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 133 | -0.270 | -5.66€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 133 | -0.270 | -5.66€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1144 | +0.086 | +284.43€ | 0 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1144 | +0.086 | +284.43€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 434 | +0.080 | +91.23€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 434 | +0.080 | +91.23€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 395 | +0.059 | +63.01€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 395 | +0.059 | +63.01€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 315 | +0.125 | +130.20€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 315 | +0.125 | +130.20€ | 2 | 15 |
| ✅ LATE_WINDOW_5MIN | 132 | +0.254 | +113.28€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 132 | +0.254 | +113.28€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 132 | +0.254 | +113.28€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 132 | +0.254 | +113.28€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 2829 | +0.102 | +730.42€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2829 | +0.102 | +730.42€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2829 | +0.102 | +730.42€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2829 | +0.102 | +730.42€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 436 | -0.069 | -32.07€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 436 | -0.069 | -32.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 121 | -0.029 | -1.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 121 | -0.029 | -1.21€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 166 | -0.030 | -6.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 166 | -0.030 | -6.03€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 3022 | +0.019 | +69.63€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3022 | +0.019 | +69.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 145 | +0.031 | -2.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 145 | +0.031 | -2.10€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 500 | +0.022 | +31.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 500 | +0.022 | +31.45€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1104 | +0.030 | +30.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1104 | +0.030 | +30.70€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 686 | +0.015 | +2.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 686 | +0.015 | +2.56€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 384 | +0.010 | +12.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 384 | +0.010 | +12.12€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1450 | -0.040 | -23.43€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1450 | -0.040 | -23.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 414 | -0.036 | -11.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 414 | -0.036 | -11.72€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 479 | -0.013 | +5.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 479 | -0.013 | +5.59€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 557 | -0.065 | -17.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 557 | -0.065 | -17.31€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 5157 | -0.016 | +120.65€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2433 | -0.020 | +28.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2724 | -0.012 | +92.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 141 | -0.004 | +4.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 70 | +0.042 | +10.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 71 | -0.048 | -5.81€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1295 | -0.004 | +45.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 610 | -0.013 | +4.43€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 685 | +0.004 | +40.66€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 579 | -0.021 | +12.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 289 | -0.033 | -1.49€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 290 | -0.010 | +13.81€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1056 | -0.033 | -22.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 483 | -0.051 | -32.44€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 573 | -0.018 | +10.12€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1011 | -0.010 | +40.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 488 | -0.004 | +30.03€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 523 | -0.016 | +10.10€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1075 | -0.015 | +41.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 493 | -0.015 | +17.97€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 582 | -0.015 | +23.12€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 39716 | -0.003 | +1890.16€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 39716 | -0.003 | +1890.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 7096 | +0.024 | +932.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 7096 | +0.024 | +932.47€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5892 | -0.032 | -93.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5892 | -0.032 | -93.89€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 7189 | +0.021 | +710.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 7189 | +0.021 | +710.31€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5703 | -0.050 | -145.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5703 | -0.050 | -145.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6696 | -0.008 | +200.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6696 | -0.008 | +200.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 7140 | +0.013 | +286.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 7140 | +0.013 | +286.59€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6225 | -0.059 | -143.60€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6225 | -0.059 | -143.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1220 | +0.001 | -13.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1220 | +0.001 | -13.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1533 | -0.076 | -31.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1533 | -0.076 | -31.41€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 50 | -0.077 | -3.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 50 | -0.077 | -3.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 726 | -0.124 | -33.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 726 | -0.124 | -33.70€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1840 | -0.078 | -36.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1840 | -0.078 | -36.12€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 99586 | -0.073 | +1720.94€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 99586 | -0.073 | +1720.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 17138 | -0.074 | +883.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 17138 | -0.074 | +883.30€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 15102 | -0.099 | -832.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 15102 | -0.099 | -832.30€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 17413 | -0.065 | +1061.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 17413 | -0.065 | +1061.04€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 14636 | -0.095 | -452.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 14636 | -0.095 | -452.79€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 18014 | -0.052 | +374.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 18014 | -0.052 | +374.98€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 17283 | -0.064 | +686.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 17283 | -0.064 | +686.72€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8092 | -0.032 | -158.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8092 | -0.032 | -158.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1923 | -0.042 | -17.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1923 | -0.042 | -17.89€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2245 | -0.026 | -31.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2245 | -0.026 | -31.96€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1124 | -0.051 | -24.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1124 | -0.051 | -24.99€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 796 | -0.029 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 796 | -0.029 | -30.79€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1418 | +0.121 | +559.31€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#5min | 1282 | +0.128 | +546.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 297 | +0.149 | +162.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 297 | +0.149 | +162.63€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 250 | +0.107 | +73.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 250 | +0.107 | +73.58€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 261 | +0.124 | +112.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 261 | +0.124 | +112.46€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 229 | +0.154 | +127.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 229 | +0.154 | +127.17€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 245 | +0.099 | +70.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 245 | +0.099 | +70.88€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1015 | -0.011 | -5.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1015 | -0.011 | -5.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 198 | +0.000 | +8.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 198 | +0.000 | +8.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 157 | +0.009 | +9.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 157 | +0.009 | +9.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 268 | -0.026 | -12.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 268 | -0.026 | -12.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 224 | +0.013 | +4.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 224 | +0.013 | +4.87€ | 0 | 0 |
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
| 🚫 PRICE_TARGET_GBM_FADE | 922 | -0.202 | -55.47€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 383 | -0.196 | -33.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 328 | -0.200 | -34.63€ | 2 | 0 |
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
| ✅ STREAK_FADE_15M | 634 | +0.031 | +25.37€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 634 | +0.031 | +25.37€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 47 | +0.031 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 47 | +0.031 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 66 | -0.015 | -2.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 66 | -0.015 | -2.23€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 226 | +0.057 | +25.91€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 226 | +0.057 | +25.91€ | 2 | 4 |
| ✅ STREAK_FADE_5M | 3178 | -0.021 | -124.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3178 | -0.021 | -124.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 968 | -0.023 | -35.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 968 | -0.023 | -35.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 585 | -0.026 | -25.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 585 | -0.026 | -25.65€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1469 | -0.016 | -49.53€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1469 | -0.016 | -49.53€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 91 | -0.059 | -9.78€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 91 | -0.059 | -9.78€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 53 | -0.027 | -5.34€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 53 | -0.027 | -5.34€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 9863 | +0.019 | +102.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9863 | +0.019 | +102.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2640 | +0.021 | +28.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2640 | +0.021 | +28.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2383 | +0.025 | +45.51€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2383 | +0.025 | +45.51€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2861 | +0.010 | -0.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2861 | +0.010 | -0.81€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1979 | +0.020 | +29.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1979 | +0.020 | +29.37€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8926 | +0.013 | -45.00€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8926 | +0.013 | -45.00€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3519 | +0.018 | -5.47€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3519 | +0.018 | -5.47€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3517 | +0.011 | -24.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3517 | +0.011 | -24.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1890 | +0.007 | -14.81€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1890 | +0.007 | -14.81€ | 1 | 0 |
| ✅ UPDOWN_GBM | 61184 | +0.048 | +4952.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 15178 | +0.083 | +3309.63€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2020 | +0.004 | +6.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 40292 | +0.042 | +1584.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3485 | +0.006 | +53.15€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6329 | +0.084 | +897.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1321 | +0.156 | +572.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 63 | -0.023 | -2.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4945 | +0.066 | +327.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 11854 | +0.051 | +959.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1914 | +0.091 | +447.34€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 524 | +0.011 | +5.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 7763 | +0.055 | +461.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1576 | +0.004 | +42.47€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 77 | -0.082 | +2.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 7449 | +0.062 | +704.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1304 | +0.145 | +500.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 60 | +0.000 | -2.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6085 | +0.044 | +206.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 13329 | +0.037 | +739.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3593 | +0.056 | +454.37€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 517 | +0.007 | +8.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 7965 | +0.037 | +272.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1185 | +0.005 | +1.01€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 69 | -0.106 | +3.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 13523 | +0.026 | +556.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3580 | +0.036 | +337.68€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 507 | -0.001 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 8651 | +0.026 | +214.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 724 | +0.012 | +9.66€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 61 | -0.151 | -5.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 8698 | +0.058 | +1098.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3466 | +0.104 | +997.65€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 349 | +0.004 | -2.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4883 | +0.029 | +102.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 207 | -0.112 | +0.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 713 | +0.359 | +245.74€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 713 | +0.359 | +245.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 386 | +0.358 | +126.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 386 | +0.358 | +126.47€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 327 | +0.357 | +119.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 327 | +0.357 | +119.27€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 16677 | -0.026 | +3972.06€ | 2 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 16677 | -0.026 | +3972.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1418 | -0.053 | +479.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1418 | -0.053 | +479.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2882 | -0.111 | +131.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2882 | -0.111 | +131.77€ | 4 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 804 | +0.215 | +650.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 804 | +0.215 | +650.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1933 | +0.212 | +1209.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1933 | +0.212 | +1209.63€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4798 | -0.064 | +621.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4798 | -0.064 | +621.05€ | 5 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4842 | -0.063 | +879.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4842 | -0.063 | +879.99€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 182 | +0.033 | +7.26€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 182 | +0.033 | +7.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 182 | +0.033 | +7.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 182 | +0.033 | +7.26€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1177 | +0.288 | +954.66€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1177 | +0.288 | +954.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 639 | +0.286 | +493.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 639 | +0.286 | +493.49€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 538 | +0.289 | +461.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 538 | +0.289 | +461.17€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 765 | -0.115 | -85.82€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 765 | -0.115 | -85.82€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 224 | -0.088 | -18.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 224 | -0.088 | -18.30€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 79 | -0.167 | -9.44€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 79 | -0.167 | -9.44€ | 2 | 0 |
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
  - _Estado_: 645 celda(s) pasan gate riguroso completo de 2498 evaluadas (n>=40) y 3483 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.036 < 0.08 — monitorear
  - _Datos_: n=3574 IC=+0.036 PNL=+338.86€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.136 n=616/60 | contraria IC=+0.198 n=624 | gap=-0.062 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=393, boost estimado=+0.011. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1183/40 IC=+0.005 PNL=+1.00€ | BTC#60min: n=1574/40 IC=+0.004 PNL=+42.49€ | SOL#60min: n=723/40 IC=+0.012 PNL=+9.14€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=453827 | tras_1loss IC=+0.090 n=347428 | tras_2loss IC=+0.059 n=142329/40 | gap=-0.011 (umbral 0.05)

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
  - _Estado_: n=2333 IC=+0.006 PNL=+1.92€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2333 IC=+0.006 PNL=+1.92€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1147 IC=+0.006 PNL=+50.72€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1147 IC=+0.006 PNL=+50.72€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.195 > 0.1 con n=3441 PNL=+2342.35€
  - _Datos_: n=3441 IC=+0.195 PNL=+2342.35€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1910 IC=+0.091 PNL=+448.31€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1910 IC=+0.091 PNL=+448.31€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.250 n=130) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=130 IC=+0.250 PNL=+109.36€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.02 con n=816 PNL=+341.58€
  - _Datos_: n=816 IC=+0.127 PNL=+341.58€

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
  - _Estado_: n=22962 IC=+0.070 PNL=+3210.40€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=22962 IC=+0.070 PNL=+3210.40€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.135 < -0.1 con n=362 PNL=+48.28€
  - _Datos_: n=362 IC=-0.135 PNL=+48.28€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2639 IC=+0.070 PNL=+333.23€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2639 IC=+0.070 PNL=+333.23€

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
  - _Estado_: n=24879 IC=-0.137 PNL=+1687.27€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=24879 IC=-0.137 PNL=+1687.27€

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
  - _Estado_: n=2540 IC=+0.137 PNL=+1487.87€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2540 IC=+0.137 PNL=+1487.87€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=6296 IC=+0.044 PNL=+431.93€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6296 IC=+0.044 PNL=+431.93€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.089 > 0.08 con n=2789 PNL=+1465.84€
  - _Datos_: n=2789 IC=+0.089 PNL=+1465.84€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.227 < -0.1 con n=2548 PNL=-214.06€
  - _Datos_: n=2548 IC=-0.227 PNL=-214.06€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1440) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1440 IC=+0.101 PNL=+325.85€

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
  - _Estado_: n=11489 IC=+0.183 PNL=-1216.16€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=11489 IC=+0.183 PNL=-1216.16€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.1 con n=184 PNL=+114.46€
  - _Datos_: n=184 IC=+0.210 PNL=+114.46€
