# Hipótesis automáticas — 2026-10-05 14:13 UTC
_Generado por shadow_postmortem.py sobre 760770 resoluciones (PNL=+92750.50€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=574)

- **PATRÓN** `py_entrada` > `0.51` → IC=+0.239 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.51 (IC base=+0.129)

- **PATRÓN** `n_total_lado` > `71.0` → IC=+0.215 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 71.0 (IC base=+0.129)

- **PATRÓN** `banda_hit_calibrado` > `0.7991` → IC=+0.265 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7991 (IC base=+0.129)

- **PATRÓN** `banda_z` > `9.249` → IC=+0.182 (n=212)

  - _Acción_: Kelly boost +0.91€ cuando `banda_z` > 9.249 (IC base=+0.129)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.702` → IC=+0.129 (n=567)

  - _Acción_: Kelly boost +0.65€ cuando `ballenas_wallet_edge_medio` > 0.702 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=671)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3077.5494` → IC=+0.131 (n=423)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3077.5494 (IC base=+0.129)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.219 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.135)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.194 (n=233)

  - _Acción_: Kelly boost +0.97€ cuando `n_total_lado` > 66.0 (IC base=+0.135)

- **PATRÓN** `banda_hit_calibrado` > `0.6177` → IC=+0.253 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6177 (IC base=+0.135)

- **PATRÓN** `banda_z` > `9.958` → IC=+0.196 (n=169)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 9.958 (IC base=+0.135)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.883` → IC=+0.137 (n=414)

  - _Acción_: Kelly boost +0.69€ cuando `ballenas_wallet_edge_medio` > 0.883 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=573)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.135)

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
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=93)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=93)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=106)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8094` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8094 (IC base=+0.125)

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

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.121 (n=93)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.5 (IC base=+0.000)

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
- **FILTRO** `restante_s_al_confirmar` < `144.05` → IC=-0.213 (n=8387)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.05
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=25165)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `132.48` → IC=-0.268 (n=1073)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.48
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3219)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `124.67` → IC=-0.302 (n=979)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.67
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=2938)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `164.89` → IC=-0.220 (n=2108)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 164.89
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6324)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.53` → IC=-0.314 (n=1627)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.53
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=4883)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.213 (n=16211)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=3879)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `5380.041` → IC=+0.171 (n=2521)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5380.041 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=14266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=17480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.229 (n=13360)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=6373)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7630.0373` → IC=+0.168 (n=2443)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7630.0373 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1845)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=2324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `16049.8465` → IC=+0.216 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.8465 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.201 (n=1671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1855)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2378)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `16003.8489` → IC=+0.212 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16003.8489 (IC base=+0.195)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.124 (n=1035)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.555 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `4587.7919` → IC=+0.123 (n=250)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 4587.7919 (IC base=+0.092)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=435)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.090)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.135 (n=942)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.44 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `5754.4405` → IC=+0.144 (n=234)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 5754.4405 (IC base=+0.090)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=3402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.356 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.232 (n=1522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.362 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.221)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=728)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.254 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=656)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2154.4479` → IC=+0.156 (n=367)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2154.4479 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.407 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.152 (n=1227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=654)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=809)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.181 (n=321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.372 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.219 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=14367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=12219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.228 (n=6121)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.178 (n=3198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3252)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.174)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.239 (n=1237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.234 (n=1395)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.333 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.232)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.188 (n=3154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=3181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.192 (n=1301)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.73 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.252 (n=2924)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.332 (n=1007)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=3254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=2793)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.191 (n=2458)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.196 (n=1174)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.436 (n=592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `2746.8442` → IC=+0.438 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2746.8442 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.435 (n=260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.443 (n=173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `14878.5401` → IC=+0.442 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14878.5401 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.447 (n=243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.466 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.434 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `3371.5411` → IC=+0.451 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3371.5411 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.413 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.420 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.419 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.409)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.203 (n=42750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.242 (n=18831)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.186 (n=7365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=5924)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.198 (n=8111)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=3814)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.268 (n=4362)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.180 (n=7776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=7781)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=3841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=2640)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=7089)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.204 (n=5689)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=2813)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=3045)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=3270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=6567)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.125 (n=6089)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=6338)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.48` → IC=+0.137 (n=6071)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.48 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=3286)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.127 (n=3016)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.16 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.141 (n=3166)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=3995)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.16` → IC=+0.144 (n=3016)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.16 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=3281)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.130 (n=3474)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.135 (n=3059)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.313 (n=930)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.289 (n=1306)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.379 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `4186.9259` → IC=+0.305 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4186.9259 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.292 (n=618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.334 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `3795.9101` → IC=+0.289 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3795.9101 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.295 (n=656)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1430.8899` → IC=+0.303 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1430.8899 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.355 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.349)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.367 (n=81)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.349)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.390 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.349)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.353 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.349)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.377 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.349)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.441 (n=252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.438 (n=287)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.459 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.442 (n=101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.451 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `2139.052` → IC=+0.457 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2139.052 (IC base=+0.442)

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
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=73)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=73)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.237 (n=55)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=38)

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
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=73)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=73)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.237 (n=55)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=38)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4857` → IC=+0.130 (n=10249)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4857 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9844` → IC=+0.243 (n=3416)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9844 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.3766` → IC=+0.254 (n=2668)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3766 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.031` → IC=+0.183 (n=3890)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.031 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2117` → IC=+0.251 (n=2866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2117 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6912` → IC=+0.256 (n=2560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6912 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.224 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `1.4663` → IC=+0.211 (n=7172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4663 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5661` → IC=+0.139 (n=12443)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.5661 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.7558` → IC=+0.203 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7558 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.1468` → IC=+0.179 (n=4142)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1468 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `1.1974` → IC=+0.179 (n=4556)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.1974 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2951` → IC=+0.225 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2951 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.5683` → IC=+0.200 (n=6973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5683 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.214 (n=7614)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 116.0 (IC base=+0.070)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.222 (n=761)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.185 (n=763)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.008 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3504` → IC=+0.185 (n=2283)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3504 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.192 (n=1105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.184 (n=1527)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 11.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.763` → IC=+0.296 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.763 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.226 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.180 (n=2158)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=2345)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2046.32` → IC=+0.187 (n=761)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2046.32 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.242 (n=1630)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0888` → IC=+0.264 (n=608)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0888 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0604` → IC=+0.284 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0604 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.49` → IC=+0.249 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.49 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.394` → IC=+0.236 (n=1907)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.394 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.155` → IC=+0.231 (n=1777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.155 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.257 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6087` → IC=+0.250 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6087 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.241 (n=794)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3531` → IC=+0.231 (n=1804)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3531 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.235 (n=1808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.979` → IC=+0.263 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.979 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.1888` → IC=+0.221 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1888 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.5452` → IC=+0.225 (n=1895)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5452 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.813` → IC=+0.259 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.813 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2501` → IC=+0.223 (n=1804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2501 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6183` → IC=+0.224 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6183 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.234 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.4169` → IC=+0.242 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4169 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.183 (n=604)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0026 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.162 (n=605)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=822)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.7219` → IC=+0.176 (n=1807)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7219 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1271` → IC=+0.154 (n=1622)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1271 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.356` → IC=+0.146 (n=289)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 11.356 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.302` → IC=+0.141 (n=1656)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.302 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.147 (n=1807)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.204 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `0.6209` → IC=+0.136 (n=1807)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6209 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0967` → IC=+0.171 (n=657)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0967 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4576` → IC=+0.148 (n=1696)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4576 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.7847` → IC=+0.144 (n=1130)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7847 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.169 (n=711)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 230.0 (IC base=+0.135)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.200 (n=2308)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.195 (n=2306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=2073)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.366` → IC=+0.258 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.366 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.196 (n=2021)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.3507` → IC=+0.194 (n=305)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3507 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `1.768` → IC=+0.198 (n=1980)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.768 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=2756)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2027.3432` → IC=+0.201 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2027.3432 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.221 (n=1789)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.1764` → IC=+0.224 (n=893)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1764 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=951)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.0649` → IC=+0.231 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0649 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.717` → IC=+0.245 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.717 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.253 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.7289` → IC=+0.214 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7289 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.225 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1825.6984` → IC=+0.213 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1825.6984 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.214 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.211)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=124)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=2746)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.154 (n=437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0036 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9602` → IC=+0.222 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9602 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.5163` → IC=+0.322 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5163 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.913` → IC=+0.173 (n=910)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 4.913 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.333 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8553 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.328 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1112` → IC=+0.331 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1112 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.356 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `1.8501` → IC=+0.321 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8501 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.326 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.0987` → IC=+0.163 (n=718)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.0987 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.2992` → IC=+0.194 (n=335)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.2992 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `0.8497` → IC=+0.155 (n=761)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8497 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.206 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.5312` → IC=+0.164 (n=971)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.5312 (IC base=+0.028)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.184 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=420)

- **FILTRO** `ibs_20min` < `0.314` → IC=-0.180 (n=123)

  - _Acción_: SKIP cuando `ibs_20min` < 0.314
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=371)

- **FILTRO** `ibs_20min` > `0.2308` → IC=-0.126 (n=2773)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2308
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=1366)

- **FILTRO** `sigma_ewma_delta_pct` > `8.797` → IC=-0.218 (n=435)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.797
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3704)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.200 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.9803` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9803 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.359` → IC=+0.134 (n=173)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.359 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.8994` → IC=+0.270 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8994 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `1.0815` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0815 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.1509` → IC=+0.286 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1509 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.1695` → IC=+0.290 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1695 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.284 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.040)

- **PATRÓN** `ibs_20min` < `0.2308` → IC=+0.136 (n=1366)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.2308 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.1755` → IC=+0.271 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1755 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.277 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.1613` → IC=+0.317 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1613 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.4232` → IC=+0.290 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4232 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.638` → IC=-0.174 (n=726)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.638
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2180)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.204 (n=722)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2184)

- **FILTRO** `ibs_20min` > `0.7669` → IC=-0.207 (n=1074)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7669
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=3228)

- **PATRÓN** `dist_vwap_pct` > `0.7626` → IC=+0.316 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7626 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2747` → IC=+0.312 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2747 (IC base=-0.068)

- **PATRÓN** `volumen_regimen` < `0.988` → IC=+0.297 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.988 (IC base=-0.068)

- **PATRÓN** `volumen_regimen` > `0.6476` → IC=+0.310 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6476 (IC base=-0.068)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.303 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` < `2.4802` → IC=+0.299 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4802 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.8591` → IC=+0.301 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8591 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.8345` → IC=+0.285 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8345 (IC base=-0.014)

- **PATRÓN** `volumen_regimen` < `0.722` → IC=+0.250 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.722 (IC base=-0.014)

- **PATRÓN** `volumen_regimen` > `1.0722` → IC=+0.276 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0722 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.099` → IC=+0.264 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.099 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.1485` → IC=+0.256 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1485 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` > `1.4218` → IC=+0.254 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4218 (IC base=-0.014)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.199 (n=4462)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.188 (n=11956)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4706 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.9745` → IC=+0.285 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9745 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.691` → IC=+0.155 (n=6085)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.691 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.1749` → IC=+0.247 (n=4880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1749 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.255 (n=4360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` < `0.1097` → IC=+0.243 (n=7585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1097 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2953` → IC=+0.255 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2953 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `1.4679` → IC=+0.242 (n=2627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4679 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.6456` → IC=+0.255 (n=2627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6456 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.276 (n=7437)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.164 (n=4314)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.009 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.157 (n=11386)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5455 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.6818` → IC=+0.252 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6818 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2353` → IC=+0.249 (n=3723)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2353 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `0.7077` → IC=+0.250 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7077 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.1967` → IC=+0.260 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1967 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.305 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.5928` → IC=+0.278 (n=2382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5928 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.280 (n=5300)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.073)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2584` → IC=-0.161 (n=928)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2584
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2790)

- **FILTRO** `ibs_20min` > `0.761` → IC=-0.177 (n=762)

  - _Acción_: SKIP cuando `ibs_20min` > 0.761
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2292)

- **FILTRO** `sigma_ewma_delta_pct` > `4.593` → IC=-0.175 (n=684)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.593
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2370)

- **PATRÓN** `ibs_20min` > `0.9093` → IC=+0.276 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9093 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.245` → IC=+0.203 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.245 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2277` → IC=+0.269 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2277 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4412` → IC=+0.215 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4412 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.2004` → IC=+0.228 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2004 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.228 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2235` → IC=+0.430 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2235 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.5496` → IC=+0.427 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5496 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.5328` → IC=+0.423 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5328 (IC base=-0.025)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.431 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=-0.025)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8657` → IC=+0.164 (n=896)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8657 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.1124` → IC=+0.194 (n=693)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1124 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.2024` → IC=+0.169 (n=1262)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2024 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6774` → IC=+0.180 (n=1128)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6774 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0752` → IC=+0.170 (n=1162)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.0752 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2745` → IC=+0.216 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2745 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4267` → IC=+0.196 (n=413)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4267 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.4378` → IC=+0.184 (n=413)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.4378 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.229 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 229.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1491` → IC=+0.226 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1491 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` > `0.6178` → IC=+0.228 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6178 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.300 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.233 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4386 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1744` → IC=+0.234 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1744 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.272 (n=2034)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.255 (n=2046)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=1822)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.786` → IC=+0.283 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.786 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.266 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `2.1822` → IC=+0.263 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1822 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `1948.2131` → IC=+0.270 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1948.2131 (IC base=+0.251)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.301 (n=1689)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.1791` → IC=+0.303 (n=743)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1791 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.319 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.359` → IC=+0.292 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.359 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `0.1` → IC=+0.288 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.7` → IC=+0.297 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.7 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` < `0.1953` → IC=+0.282 (n=1637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1953 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.1211` → IC=+0.291 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1211 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.7251` → IC=+0.298 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7251 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.6522` → IC=+0.294 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6522 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1941.6632` → IC=+0.299 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1941.6632 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.288 (n=1373)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.286)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7682` → IC=-0.183 (n=775)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7682
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=2328)

- **PATRÓN** `ibs_20min` > `0.9028` → IC=+0.171 (n=703)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.9028 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.3685` → IC=+0.226 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3685 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.0078` → IC=+0.244 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0078 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1702` → IC=+0.234 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1702 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.0816` → IC=+0.235 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0816 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4161` → IC=+0.255 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4161 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.256 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.122` → IC=+0.238 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.122 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.220 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1951 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.276 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.8479` → IC=+0.266 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8479 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.256 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7606` → IC=-0.186 (n=1423)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7606
  - _Potencial_: sin este filtro IC_bueno=+0.285 (n=1423)

- **FILTRO** `ibs_20min` > `0.6696` → IC=-0.243 (n=715)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6696
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2147)

- **FILTRO** `sigma_ewma_delta_pct` > `4.823` → IC=-0.203 (n=608)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.823
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=2254)

- **PATRÓN** `ibs_20min` > `0.7606` → IC=+0.285 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7606 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.2143` → IC=+0.319 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2143 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.692` → IC=+0.166 (n=447)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.692 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.312 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `0.6396` → IC=+0.305 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6396 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.303 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2759` → IC=+0.324 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2759 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.7975` → IC=+0.313 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7975 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.318 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.5692` → IC=+0.133 (n=1889)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5692 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.2679` → IC=+0.240 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2679 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.268 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.1889` → IC=+0.230 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1889 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.262 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4505` → IC=+0.249 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4505 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.261 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.021)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.331 (n=1453)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.305 (n=767)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.319 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2145` → IC=+0.319 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2145 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.776` → IC=+0.309 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.776 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.926` → IC=+0.286 (n=1832)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.926 (IC base=+0.286)

- **PATRÓN** `volumen_regimen` > `0.8619` → IC=+0.313 (n=1084)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8619 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.334 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `1.4345` → IC=+0.298 (n=1553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4345 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `2475.2192` → IC=+0.298 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2475.2192 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.322 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.317 (n=1148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.1886` → IC=+0.288 (n=758)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1886 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.291 (n=1636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.3725` → IC=+0.310 (n=1722)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3725 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.3053` → IC=+0.296 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3053 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.518` → IC=+0.298 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.518 (IC base=+0.285)

- **PATRÓN** `volumen_regimen` < `0.7176` → IC=+0.285 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7176 (IC base=+0.285)

- **PATRÓN** `volumen_regimen` > `1.2282` → IC=+0.316 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2282 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.332 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.294 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.1353` → IC=+0.283 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1353 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2634.017` → IC=+0.287 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2634.017 (IC base=+0.285)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.187 (n=3344)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0047 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.207 (n=3338)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3556` → IC=+0.185 (n=8812)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3556 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=10456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.5693` → IC=+0.226 (n=10014)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5693 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.1715` → IC=+0.199 (n=4340)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1715 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.462` → IC=+0.252 (n=2017)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.462 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.167 (n=6653)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2084 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6308` → IC=+0.163 (n=6653)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6308 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2955` → IC=+0.197 (n=1490)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2955 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.4517` → IC=+0.174 (n=3219)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4517 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.6126` → IC=+0.182 (n=3219)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6126 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `1988.8162` → IC=+0.177 (n=8945)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1988.8162 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.189 (n=8925)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 104.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.188 (n=6367)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0066 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.222 (n=3179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=3621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.4873` → IC=+0.230 (n=9533)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4873 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` < `0.1682` → IC=+0.168 (n=6616)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1682 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.32` → IC=+0.197 (n=1600)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.32 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.163 (n=6839)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1776 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.215 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.5613` → IC=+0.172 (n=3887)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5613 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.6155` → IC=+0.175 (n=2945)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6155 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.183 (n=8506)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 107.0 (IC base=+0.174)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.240 (n=564)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.203 (n=561)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3418` → IC=+0.220 (n=1682)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3418 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.203 (n=1680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.206 (n=1121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.9157` → IC=+0.286 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9157 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.276` → IC=+0.333 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.276 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.248 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4334` → IC=+0.197 (n=1573)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4334 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=1736)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2048.3196` → IC=+0.199 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.3196 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.247 (n=1119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.250 (n=1136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1012` → IC=+0.293 (n=559)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1012 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.250 (n=1220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.1026` → IC=+0.276 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1026 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.383` → IC=+0.242 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.383 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.221` → IC=+0.247 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.221 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.1618` → IC=+0.239 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1618 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.266 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4206` → IC=+0.262 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4206 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.6147` → IC=+0.241 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6147 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1835.25` → IC=+0.253 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1835.25 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.229 (n=503)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.0694` → IC=+0.198 (n=501)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0694 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=1505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.389` → IC=+0.223 (n=1502)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.389 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.1983` → IC=+0.212 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1983 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.528` → IC=+0.233 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.528 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.6924` → IC=+0.171 (n=661)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6924 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.0767` → IC=+0.160 (n=681)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.0767 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.193 (n=236)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.4144` → IC=+0.182 (n=488)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4144 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `11871.8913` → IC=+0.161 (n=1342)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11871.8913 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `434.0` → IC=+0.162 (n=1425)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 434.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1572)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.2972` → IC=+0.166 (n=1572)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2972 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.5923` → IC=+0.196 (n=1571)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5923 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1336` → IC=+0.169 (n=1552)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1336 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.901` → IC=+0.201 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.901 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.160 (n=1571)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2116 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.2288` → IC=+0.143 (n=1616)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.2288 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.147 (n=703)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4908` → IC=+0.152 (n=1459)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4908 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.7682` → IC=+0.143 (n=972)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7682 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.172 (n=464)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 208.0 (IC base=+0.141)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.228 (n=560)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2471` → IC=+0.220 (n=1121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2471 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.548` → IC=+0.276 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.548 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.205 (n=1417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2002` → IC=+0.205 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2002 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.7786` → IC=+0.205 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7786 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.7293` → IC=+0.211 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7293 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1998)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `1952.5984` → IC=+0.220 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1952.5984 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.242 (n=1256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1429` → IC=+0.262 (n=627)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1429 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.277 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.3506` → IC=+0.248 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3506 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.677` → IC=+0.256 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.677 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.259 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.7484` → IC=+0.236 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7484 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.7396` → IC=+0.232 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7396 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1939.9244` → IC=+0.225 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1939.9244 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.217 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.224)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.182 (n=1415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0064 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0789` → IC=+0.203 (n=536)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0789 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=1675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3388` → IC=+0.207 (n=1608)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3388 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1389` → IC=+0.188 (n=1054)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1389 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.210 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8563` → IC=+0.162 (n=1072)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8563 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.172 (n=674)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4355` → IC=+0.167 (n=526)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4355 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.529` → IC=+0.162 (n=525)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.529 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5128.1918` → IC=+0.197 (n=1072)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 5128.1918 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.155 (n=1548)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 152.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.159 (n=1677)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0071 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.3828` → IC=+0.147 (n=1677)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3828 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6686` → IC=+0.182 (n=1677)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.6686 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1469` → IC=+0.151 (n=1638)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1469 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.904` → IC=+0.162 (n=583)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.904 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8541` → IC=+0.159 (n=1118)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8541 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.181 (n=252)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.8208` → IC=+0.140 (n=1034)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8208 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.5391` → IC=+0.128 (n=517)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.5391 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `4321.6939` → IC=+0.162 (n=1118)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4321.6939 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.125 (n=1490)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 150.0 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.160 (n=831)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0099 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4479` → IC=+0.128 (n=1609)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4479 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.212 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `1.0387` → IC=+0.214 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0387 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.874` → IC=+0.261 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.874 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.2058` → IC=+0.138 (n=1828)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2058 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.647` → IC=+0.131 (n=1828)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.647 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1641` → IC=+0.135 (n=1841)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1641 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5458` → IC=+0.142 (n=778)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5458 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4822` → IC=+0.129 (n=589)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4822 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=1914)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2388.9978` → IC=+0.184 (n=1219)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2388.9978 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.149 (n=1439)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 46.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.158 (n=808)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0061 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1031` → IC=+0.179 (n=612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.1031 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=1852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5778` → IC=+0.217 (n=1835)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5778 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.7491` → IC=+0.125 (n=334)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.7491 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.198` → IC=+0.148 (n=1679)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.198 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.347` → IC=+0.128 (n=560)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 5.347 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.132 (n=1835)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1756 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2289` → IC=+0.157 (n=322)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2289 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4534` → IC=+0.139 (n=561)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4534 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `1.819` → IC=+0.125 (n=1122)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.819 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2744.0462` → IC=+0.185 (n=832)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2744.0462 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.128 (n=1639)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 52.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.230 (n=1718)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.1788` → IC=+0.219 (n=756)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1788 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=779)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.245 (n=1721)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.1986` → IC=+0.214 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1986 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.6` → IC=+0.243 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.6 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.1976` → IC=+0.211 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1976 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.216 (n=1716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.271 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.4732` → IC=+0.211 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4732 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.8125` → IC=+0.219 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8125 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.211 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2849.4481` → IC=+0.210 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2849.4481 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.227 (n=774)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.221 (n=797)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.243 (n=586)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.236 (n=859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.0213` → IC=+0.286 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0213 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `1.1572` → IC=+0.235 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1572 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.386` → IC=+0.252 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.386 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.6367` → IC=+0.225 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6367 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.272 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `2.2062` → IC=+0.208 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2062 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.4377` → IC=+0.214 (n=1612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4377 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2604.9815` → IC=+0.222 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2604.9815 (IC base=+0.215)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.195 (n=1159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0042 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.170 (n=877)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0084 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3398` → IC=+0.179 (n=2309)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3398 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.188 (n=2385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.341` → IC=+0.197 (n=2623)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.341 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.186 (n=421)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.7901 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.758` → IC=+0.194 (n=1142)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.758 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8708` → IC=+0.190 (n=1564)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8708 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.177 (n=782)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.2084 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1638` → IC=+0.173 (n=698)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1638 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4427` → IC=+0.180 (n=849)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4427 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.5338` → IC=+0.175 (n=850)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.5338 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=2990)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2726.8059` → IC=+0.170 (n=2343)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2726.8059 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.186 (n=2403)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 145.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.155 (n=900)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0036 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=2531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.195 (n=900)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.0714 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `0.6989` → IC=+0.123 (n=1074)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.6989 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.0756` → IC=+0.124 (n=1025)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0756 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` < `1.441` → IC=+0.145 (n=872)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.441 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2778.617` → IC=+0.128 (n=2406)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2778.617 (IC base=+0.108)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.129 (n=1145)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 29.0 (IC base=+0.108)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.208 (n=313)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.3302` → IC=+0.173 (n=711)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3302 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.190 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 8.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.6364` → IC=+0.208 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6364 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.287` → IC=+0.175 (n=247)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.287 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.203` → IC=+0.175 (n=306)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.203 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8832` → IC=+0.179 (n=474)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8832 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.157` → IC=+0.156 (n=742)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.157 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.2382` → IC=+0.160 (n=610)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.2382 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5207` → IC=+0.158 (n=620)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5207 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `10658.416` → IC=+0.156 (n=711)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 10658.416 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.206 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.208 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3449` → IC=+0.158 (n=847)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3449 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.147 (n=812)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 6.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=859)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6102` → IC=+0.181 (n=745)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.6102 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.3076` → IC=+0.154 (n=901)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.3076 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.14` → IC=+0.142 (n=770)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.14 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2185` → IC=+0.143 (n=847)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2185 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.063` → IC=+0.166 (n=384)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.063 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.194 (n=230)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1223` → IC=+0.159 (n=736)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1223 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.412` → IC=+0.146 (n=837)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.412 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=1096)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `11986.1084` → IC=+0.142 (n=756)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 11986.1084 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `355.0` → IC=+0.151 (n=814)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 355.0 (IC base=+0.140)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.241 (n=555)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.2071` → IC=+0.218 (n=555)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2071 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.6714` → IC=+0.252 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6714 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3604` → IC=+0.211 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3604 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.2068` → IC=+0.206 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2068 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.089` → IC=+0.221 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.089 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `0.8422` → IC=+0.211 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8422 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `1.1824` → IC=+0.220 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1824 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.1598` → IC=+0.233 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1598 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.4274` → IC=+0.225 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4274 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.4553` → IC=+0.232 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4553 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.131 (n=695)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0061 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.121 (n=708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 7.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.0866` → IC=+0.168 (n=263)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.0866 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.459` → IC=+0.149 (n=206)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.459 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `0.6885` → IC=+0.150 (n=347)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6885 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` > `0.2242` → IC=+0.143 (n=124)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2242 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `7726.703` → IC=+0.141 (n=525)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 7726.703 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.125 (n=334)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 42.0 (IC base=+0.104)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.475` → IC=-0.126 (n=268)

  - _Acción_: SKIP cuando `ibs_20min` > 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=521)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.172 (n=613)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0051 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.5405` → IC=+0.161 (n=612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.5405 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.277 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.947` → IC=+0.233 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.947 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.329` → IC=+0.218 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.329 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.0674` → IC=+0.176 (n=538)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0674 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `0.6528` → IC=+0.166 (n=612)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6528 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.174 (n=90)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `2.4855` → IC=+0.159 (n=590)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4855 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.1991` → IC=+0.174 (n=268)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.1991 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=648)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `3078.7088` → IC=+0.194 (n=204)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3078.7088 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.475` → IC=+0.146 (n=521)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.475 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.569` → IC=+0.124 (n=248)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.569 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `2864.9802` → IC=+0.153 (n=269)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2864.9802 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.124 (n=360)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 23.0 (IC base=+0.054)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.168 (n=191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0238 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.198 (n=127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0144 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.165 (n=168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.201 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.5556` → IC=+0.184 (n=172)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5556 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.24` → IC=+0.173 (n=105)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.24 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `1.115` → IC=+0.161 (n=213)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.115 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.181 (n=164)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `0.6843` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6843 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.2526` → IC=+0.181 (n=186)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.2526 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.182 (n=196)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.02 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `2503.9142` → IC=+0.174 (n=127)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2503.9142 (IC base=+0.152)

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
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.179 (n=4312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0046 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.211 (n=4313)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=13532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.9923` → IC=+0.310 (n=4311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9923 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1641` → IC=+0.186 (n=4938)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1641 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.397` → IC=+0.247 (n=3184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.397 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `0.8802` → IC=+0.171 (n=5774)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8802 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.196 (n=1756)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.6011` → IC=+0.195 (n=4168)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6011 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1973.596` → IC=+0.180 (n=11551)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1973.596 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.202 (n=10181)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.195 (n=5137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.1469` → IC=+0.194 (n=5121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1469 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=4364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.4528` → IC=+0.247 (n=10242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4528 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.1733` → IC=+0.165 (n=6848)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1733 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.095` → IC=+0.203 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.095 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.742` → IC=+0.184 (n=11217)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.742 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.163 (n=3475)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7056 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2895` → IC=+0.248 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2895 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `1.864` → IC=+0.190 (n=7242)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.864 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.206 (n=7099)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.184)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.251 (n=717)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.224 (n=719)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.356` → IC=+0.210 (n=2149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.356 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=1037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=1446)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.734` → IC=+0.358 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.734 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.264 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.5711` → IC=+0.215 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5711 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2046.45` → IC=+0.215 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2046.45 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.263 (n=1174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.262 (n=1761)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1253` → IC=+0.280 (n=775)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1253 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1588)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3579` → IC=+0.283 (n=1549)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3579 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.506` → IC=+0.264 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.506 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.293 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.622` → IC=+0.278 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.622 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=1928)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1970.84` → IC=+0.266 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1970.84 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.214 (n=698)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1801` → IC=+0.164 (n=1380)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1801 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=2168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.2861` → IC=+0.207 (n=2069)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2861 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1252` → IC=+0.191 (n=1182)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1252 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.762` → IC=+0.182 (n=347)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 11.762 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.23` → IC=+0.154 (n=1891)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.23 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.7032` → IC=+0.171 (n=911)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.7032 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0731` → IC=+0.155 (n=1831)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0731 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.272` → IC=+0.188 (n=296)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.272 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1465` → IC=+0.162 (n=1770)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1465 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5203` → IC=+0.157 (n=1797)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5203 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `277.0` → IC=+0.181 (n=861)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 277.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1724)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.3291` → IC=+0.158 (n=1724)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3291 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.148 (n=785)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6835` → IC=+0.194 (n=1724)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.6835 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1309` → IC=+0.165 (n=1566)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1309 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.553` → IC=+0.160 (n=292)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.553 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.158 (n=1724)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1913 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1542` → IC=+0.202 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1542 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4364` → IC=+0.154 (n=1624)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4364 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7759` → IC=+0.159 (n=1083)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7759 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `416.0` → IC=+0.144 (n=1346)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 416.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.251 (n=709)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=2232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=2149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.885` → IC=+0.294 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.885 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.2061` → IC=+0.226 (n=2138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2061 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.7692` → IC=+0.231 (n=1825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7692 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2534)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2026.8956` → IC=+0.241 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2026.8956 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.242 (n=1750)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.248 (n=874)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.259 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.234 (n=935)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0171` → IC=+0.301 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0171 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.987` → IC=+0.282 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.987 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3426` → IC=+0.296 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3426 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7441` → IC=+0.233 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7441 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1508` → IC=+0.241 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1508 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1941.8898` → IC=+0.243 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1941.8898 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.252 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.196 (n=976)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.424` → IC=+0.153 (n=2212)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.424 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2715` → IC=+0.189 (n=2211)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2715 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.5473` → IC=+0.163 (n=610)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.5473 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.166` → IC=+0.153 (n=909)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.166 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8735` → IC=+0.161 (n=1475)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8735 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.176 (n=588)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5247` → IC=+0.159 (n=947)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5247 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1799` → IC=+0.153 (n=976)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1799 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7336.8828` → IC=+0.233 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7336.8828 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.180 (n=698)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 70.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.167 (n=1193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0051 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4405` → IC=+0.143 (n=1786)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4405 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.133 (n=624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 5.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7338` → IC=+0.181 (n=1785)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.7338 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.145` → IC=+0.138 (n=1562)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.145 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.342` → IC=+0.173 (n=270)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.342 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8747` → IC=+0.141 (n=1191)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8747 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.229 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.2545` → IC=+0.134 (n=1505)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.2545 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4482` → IC=+0.141 (n=1710)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4482 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `5639.5091` → IC=+0.194 (n=809)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 5639.5091 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.133 (n=1708)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 167.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.135 (n=2221)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0056 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4565` → IC=+0.201 (n=2219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4565 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0319` → IC=+0.209 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0319 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.546` → IC=+0.248 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.546 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2331` → IC=+0.137 (n=2219)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2331 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1629` → IC=+0.128 (n=2284)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1629 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.1924` → IC=+0.137 (n=979)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.1924 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=1477)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2553.7156` → IC=+0.233 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2553.7156 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.142 (n=1338)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 41.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.178 (n=706)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0056 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1303` → IC=+0.165 (n=706)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1303 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.5077` → IC=+0.233 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5077 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.2163` → IC=+0.140 (n=1743)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2163 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.49` → IC=+0.131 (n=2041)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.49 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.6459` → IC=+0.166 (n=707)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6459 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2237` → IC=+0.187 (n=343)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2237 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `2.1606` → IC=+0.135 (n=1715)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1606 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2798.604` → IC=+0.197 (n=705)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2798.604 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.138 (n=1707)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 50.0 (IC base=+0.121)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.232 (n=2162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=2265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.220 (n=1563)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.262 (n=1938)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.2086` → IC=+0.233 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2086 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.765` → IC=+0.262 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.765 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.2397` → IC=+0.217 (n=2162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2397 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.6422` → IC=+0.221 (n=2162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6422 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2371` → IC=+0.243 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2371 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.5155` → IC=+0.249 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5155 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=2058)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2632.6162` → IC=+0.221 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2632.6162 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.218 (n=757)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.230 (n=1029)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.229 (n=1601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.4194` → IC=+0.262 (n=1997)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4194 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `1.1818` → IC=+0.215 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1818 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.2934` → IC=+0.216 (n=2113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2934 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.876` → IC=+0.256 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.876 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `1.227` → IC=+0.239 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.227 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.280 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.4297` → IC=+0.214 (n=2077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4297 (IC base=+0.214)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=3783)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.224 (n=1279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.3915` → IC=+0.194 (n=3367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3915 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=1418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.187 (n=1748)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 6.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.9409` → IC=+0.240 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9409 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.1683` → IC=+0.194 (n=1432)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1683 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.201` → IC=+0.210 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.201 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.7121` → IC=+0.190 (n=1163)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.7121 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` > `0.8944` → IC=+0.188 (n=1761)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.8944 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.1703` → IC=+0.212 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1703 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.4583` → IC=+0.191 (n=1258)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4583 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `1.8715` → IC=+0.187 (n=2516)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8715 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.191 (n=2838)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `3772.9492` → IC=+0.193 (n=2551)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3772.9492 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.222 (n=954)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.4847` → IC=+0.180 (n=2849)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.4847 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=1007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=1289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.1802` → IC=+0.189 (n=1254)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.1802 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.6442` → IC=+0.179 (n=530)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6442 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.2352` → IC=+0.157 (n=2532)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2352 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.208` → IC=+0.172 (n=2840)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.208 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.2566` → IC=+0.168 (n=2685)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2566 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.169 (n=2595)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.167 (n=595)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.5394` → IC=+0.169 (n=1238)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5394 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.8291` → IC=+0.175 (n=1875)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.8291 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=3783)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `12326.3521` → IC=+0.168 (n=950)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 12326.3521 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `200.0` → IC=+0.174 (n=2444)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 200.0 (IC base=+0.164)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.239 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.263 (n=175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.515` → IC=+0.233 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.515 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.7622` → IC=+0.217 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7622 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.3165` → IC=+0.221 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3165 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.039` → IC=+0.228 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.039 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.526` → IC=+0.213 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.526 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.221 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.5931` → IC=+0.221 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5931 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.8529` → IC=+0.224 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8529 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `12467.3842` → IC=+0.234 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12467.3842 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.229 (n=467)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3657` → IC=+0.163 (n=1059)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3657 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.197 (n=354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 4.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.1485` → IC=+0.179 (n=466)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1485 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.153 (n=480)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.6078 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6649` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6649 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.211` → IC=+0.150 (n=1073)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.211 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.38` → IC=+0.167 (n=1042)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.38 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.186 (n=706)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8812 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.180 (n=220)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.5397` → IC=+0.155 (n=1055)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5397 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.168 (n=703)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `11510.29` → IC=+0.162 (n=1059)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11510.29 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `699.0` → IC=+0.161 (n=1013)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 699.0 (IC base=+0.148)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.193 (n=223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.006 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.179 (n=303)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0099 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.581` → IC=+0.174 (n=669)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.581 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.233 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.456` → IC=+0.217 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.456 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2079` → IC=+0.209 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2079 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.6796` → IC=+0.167 (n=223)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.6796 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.2469` → IC=+0.171 (n=445)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.2469 (IC base=+0.166)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.220 (n=395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.1508` → IC=+0.213 (n=521)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1508 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=541)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.5256` → IC=+0.206 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5256 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.8854` → IC=+0.198 (n=395)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.8854 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.2036` → IC=+0.204 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2036 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.178` → IC=+0.201 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.178 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.0845` → IC=+0.198 (n=1043)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.0845 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` > `1.2448` → IC=+0.196 (n=396)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.2448 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.194 (n=1089)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.206 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `2.4777` → IC=+0.199 (n=1160)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.4777 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=1187)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.226 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.190 (n=945)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.174 (n=634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 10.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` < `0.7559` → IC=+0.170 (n=945)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7559 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.0897` → IC=+0.171 (n=945)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.0897 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.6046` → IC=+0.186 (n=205)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6046 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` < `0.3831` → IC=+0.167 (n=973)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.3831 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.153` → IC=+0.168 (n=1052)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 9.153 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.6432` → IC=+0.203 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6432 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `0.7259` → IC=+0.166 (n=844)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.7259 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.183 (n=399)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `2.1949` → IC=+0.180 (n=815)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.1949 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.7864` → IC=+0.167 (n=617)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.7864 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `7437.397` → IC=+0.179 (n=945)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7437.397 (IC base=+0.165)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.205 (n=296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.184 (n=441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 3.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.160 (n=442)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 14.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.259 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1981` → IC=+0.205 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1981 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.464` → IC=+0.212 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.464 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.721` → IC=+0.201 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.721 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `1.2801` → IC=+0.158 (n=147)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.2801 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.217 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.5383` → IC=+0.203 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5383 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.166 (n=531)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `3112.065` → IC=+0.186 (n=441)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3112.065 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.181 (n=374)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 49.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.196 (n=304)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.007 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3799` → IC=+0.221 (n=227)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3799 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.197 (n=232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 9.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.22` → IC=+0.237 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.22 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.8547` → IC=+0.217 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8547 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.401` → IC=+0.176 (n=177)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 2.401 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.203` → IC=+0.178 (n=327)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 5.203 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `0.7986` → IC=+0.184 (n=150)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.7986 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.221 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.6214` → IC=+0.196 (n=146)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.6214 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.2116` → IC=+0.191 (n=150)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.2116 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `3218.3001` → IC=+0.205 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3218.3001 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.219 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.175)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.154 (n=548)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0038 (IC base=+0.083)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.121 (n=566)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 16.0 (IC base=+0.083)

- **PATRÓN** `ibs_20min` > `0.4563` → IC=+0.156 (n=1154)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.4563 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.1412` → IC=+0.142 (n=643)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1412 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.471` → IC=+0.189 (n=268)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.471 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.183 (n=159)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.083)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.122 (n=368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0045 (IC base=+0.051)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.301 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` < `0.2024` → IC=+0.127 (n=513)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.2024 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.082` → IC=+0.134 (n=402)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.082 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.141` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.141 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.142 (n=414)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.5975 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` > `1.457` → IC=+0.129 (n=370)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.457 (IC base=+0.051)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.141 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0057 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.426` → IC=+0.173 (n=393)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.426 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.164 (n=215)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.573` → IC=+0.121 (n=233)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 3.573 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `2.5009` → IC=+0.127 (n=352)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.5009 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.123 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0036 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.294 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.1871` → IC=+0.127 (n=250)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.1871 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.069` → IC=+0.144 (n=220)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 7.069 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `0.8122` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.8122 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.0743` → IC=+0.145 (n=91)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0743 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `2.4864` → IC=+0.138 (n=205)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.4864 (IC base=+0.076)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.154 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=155)

- **FILTRO** `ibs_20min` > `0.7058` → IC=-0.211 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7058
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=133)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.152 (n=277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0047 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.131 (n=385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.6963` → IC=+0.213 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6963 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1209` → IC=+0.178 (n=212)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1209 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.674` → IC=+0.280 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.674 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.7889` → IC=+0.141 (n=218)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.7889 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `1146.9989` → IC=+0.156 (n=335)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1146.9989 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.7058` → IC=+0.152 (n=133)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.7058 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.7085` → IC=+0.133 (n=77)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.7085 (IC base=+0.007)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.240 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=145)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.263 (n=116)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.173 (n=255)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.7647 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` > `0.7192` → IC=+0.132 (n=104)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.7192 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.668` → IC=+0.134 (n=80)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 9.668 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.192 (n=76)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.051)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.169 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0086 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.263 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1153` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1153 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.1816` → IC=+0.161 (n=113)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1816 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.04` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.04 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `0.6561` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6561 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` > `0.9843` → IC=+0.130 (n=52)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.9843 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.0749` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0749 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` > `1.446` → IC=+0.221 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.446 (IC base=+0.054)

### GBM_LATE_60M_FADE
- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=233)

- **FILTRO** `volumen_regimen` < `0.7425` → IC=-0.359 (n=62)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7425
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=187)

- **FILTRO** `volumen_spike_ratio` > `2.9817` → IC=-0.189 (n=43)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.9817
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=132)

- **FILTRO** `volumen_spike_ratio` < `1.6074` → IC=-0.195 (n=57)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.6074
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=118)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.206 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=200)

- **FILTRO** `sigma_h` > `0.0056` → IC=-0.373 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=162)

- **FILTRO** `dist_vwap_pct` > `0.3146` → IC=-0.395 (n=36)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3146
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=179)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=185)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=104)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2353` → IC=-0.262 (n=40)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2353
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=41)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.292 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=68)

- **FILTRO** `volumen_regimen` > `0.8408` → IC=-0.375 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8408
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=68)

- **FILTRO** `volumen_spike_ratio` > `1.5874` → IC=-0.300 (n=28)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5874
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=29)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0026` → IC=-0.364 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=62)

- **FILTRO** `ibs_20min` < `0.5872` → IC=-0.466 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5872
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=55)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.357 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=61)

- **FILTRO** `ibs_20min` > `0.538` → IC=-0.354 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` > 0.538
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=41)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=33)

- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9583 (IC base=-0.167)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=70)

- **FILTRO** `volumen_spike_ratio` < `1.5474` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5474
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=46)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=60)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `dist_vwap_pct` < `0.219` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.219
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=21)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.169 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0057 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.128 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.6585` → IC=+0.142 (n=381)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6585 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.47` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.47 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6589` → IC=+0.136 (n=127)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6589 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `2.5067` → IC=+0.124 (n=280)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.5067 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.175 (n=340)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.156 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.855` → IC=+0.193 (n=112)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.855 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` < `2.6713` → IC=+0.123 (n=311)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.6713 (IC base=+0.080)

- **PATRÓN** `libro_liquidez` > `4049.975` → IC=+0.174 (n=176)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 4049.975 (IC base=+0.080)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6438` → IC=-0.269 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6438
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=114)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.186 (n=154)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0024 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.216 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.207 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1435 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.0856` → IC=+0.157 (n=176)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.0856 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.332` → IC=+0.176 (n=140)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 4.332 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.138` → IC=+0.149 (n=172)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.138 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.6733` → IC=+0.167 (n=154)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6733 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.1895` → IC=+0.195 (n=139)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1895 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.6881` → IC=+0.199 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6881 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.4563` → IC=+0.178 (n=141)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4563 (IC base=+0.149)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1654` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1654
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=101)

- **FILTRO** `libro_liquidez` < `1506.2493` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `libro_liquidez` < 1506.2493
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=122)

- **FILTRO** `ibs_20min` > `0.1832` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1832
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=121)

- **PATRÓN** `volumen_spike_ratio` < `1.8267` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8267 (IC base=+0.049)

- **PATRÓN** `libro_liquidez` > `1506.2493` → IC=+0.129 (n=122)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1506.2493 (IC base=+0.049)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.136 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 12.0 (IC base=+0.060)

- **PATRÓN** `ibs_20min` < `0.1832` → IC=+0.159 (n=121)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1832 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.6541` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6541 (IC base=+0.060)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.0968` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0968
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=34)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.268 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.248 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.227 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` < `0.7358` → IC=+0.231 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7358 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.9298` → IC=+0.237 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9298 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.6339` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6339 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.1348` → IC=+0.227 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1348 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.379` → IC=+0.279 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.379 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.280 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.089` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.089 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.1536` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1536 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.229 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.0968` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0968 (IC base=-0.038)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.285)

- **PATRÓN** `elapsed_s` > `193.1` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.1 (IC base=+0.285)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.8028` → IC=+0.364 (n=42)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8028 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.285)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3438` → IC=+0.250 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3438 (IC base=+0.214)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.214)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.214)

- **PATRÓN** `drift_15min` |x|≤ `1.4068` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4068 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.8756` → IC=+0.267 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8756 (IC base=+0.214)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `1814.0` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1814.0 (IC base=+0.214)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.285)

- **PATRÓN** `elapsed_s` > `193.1` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.1 (IC base=+0.285)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.8028` → IC=+0.364 (n=42)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8028 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.285)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3438` → IC=+0.250 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3438 (IC base=+0.214)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.214)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.214)

- **PATRÓN** `drift_15min` |x|≤ `1.4068` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4068 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.8756` → IC=+0.267 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8756 (IC base=+0.214)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `1814.0` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1814.0 (IC base=+0.214)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.126 (n=974)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2940.6954` → IC=+0.155 (n=337)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2940.6954 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.101)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.126 (n=974)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2940.6954` → IC=+0.155 (n=337)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2940.6954 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.101)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=148)

- **FILTRO** `libro_liquidez` < `9884.3291` → IC=-0.182 (n=108)

  - _Acción_: SKIP cuando `libro_liquidez` < 9884.3291
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=56)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=234)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=220)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=47)

- **FILTRO** `libro_liquidez` < `10724.0239` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 10724.0239
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=51)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

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
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=2587)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=95)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=52)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=95)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=103)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.129 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 15.0 (IC base=+0.056)

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

- **PATRÓN** `liq_usd_total` > `118339.59` → IC=+0.149 (n=95)

  - _Acción_: Kelly boost +0.75€ cuando `liq_usd_total` > 118339.59 (IC base=+0.047)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.141 (n=168)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.047)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=1005)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=959)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=599)

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
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=311)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=113)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.026)

- **PATRÓN** `libro_liquidez` > `3946.3264` → IC=+0.132 (n=112)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3946.3264 (IC base=+0.026)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=758)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=758)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.131 (n=242)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=596)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=509)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=509)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=210)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=210)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=172)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=137)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=128)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=152)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=123)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=136)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=291)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=291)

- **FILTRO** `libro_liquidez` < `553.2637` → IC=-0.136 (n=105)

  - _Acción_: SKIP cuando `libro_liquidez` < 553.2637
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=216)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=184)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.145 (n=658)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1625)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.517` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.517
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=10)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.123 (n=136)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=82)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.221 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.041)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=124)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=102)

- **FILTRO** `lag_apertura_s` > `274.09` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `lag_apertura_s` > 274.09
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=98)

- **FILTRO** `profundidad_ratio` < `30.6` → IC=-0.126 (n=97)

  - _Acción_: SKIP cuando `profundidad_ratio` < 30.6
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=51)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `restante_min` < `3.99` → IC=-0.125 (n=110)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=43)

- **FILTRO** `lag_apertura_s` > `60.75` → IC=-0.129 (n=114)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.75
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=39)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.143 (n=152)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=51)

- **FILTRO** `profundidad_ratio` < `54.8` → IC=-0.206 (n=66)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.8
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=137)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=170)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.139 (n=164)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=95)

- **FILTRO** `restante_min` < `3.43` → IC=-0.224 (n=85)

  - _Acción_: SKIP cuando `restante_min` < 3.43
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=174)

- **FILTRO** `lag_apertura_s` > `92.29` → IC=-0.200 (n=88)

  - _Acción_: SKIP cuando `lag_apertura_s` > 92.29
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=171)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.46 (IC base=+0.033)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=154)

- **PATRÓN** `lag_apertura_s` < `93.77` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `lag_apertura_s` < 93.77 (IC base=-0.013)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.49` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.49 (IC base=+0.002)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.140 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=89)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.5 (IC base=-0.034)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.216 (n=79)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=229)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7798)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.162 (n=4572)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=13893)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.164 (n=4763)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=14340)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.189 (n=806)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2467)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.150 (n=796)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=2619)

- **PATRÓN** `libro_liquidez` > `1815.5348` → IC=+0.131 (n=1113)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1815.5348 (IC base=+0.036)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.173 (n=829)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2495)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.193 (n=803)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2659)

- **PATRÓN** `libro_liquidez` > `1816.56` → IC=+0.129 (n=1131)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1816.56 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.166 (n=783)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=2488)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2467)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3207)

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

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=284)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1959.6157` → IC=-0.171 (n=329)

  - _Acción_: SKIP cuando `libro_liquidez` < 1959.6157
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=669)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=231)

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

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.043)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=12905)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=28669)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=9762)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=31812)

- **FILTRO** `ibs_7min` < `0.2614` → IC=-0.235 (n=10391)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2614
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=31183)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=14019)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=27555)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.236 (n=12809)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=39981)

- **FILTRO** `ibs_7min` > `0.2897` → IC=-0.179 (n=13196)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2897
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=39594)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.142 (n=2099)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=4972)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.235 (n=3488)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=3583)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.252 (n=2331)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=4740)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.185 (n=1555)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5516)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.267 (n=2232)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=6908)

- **FILTRO** `ibs_7min` > `0.7857` → IC=-0.211 (n=2280)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7857
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=6860)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=1691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5419)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.250 (n=1744)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=5366)

- **FILTRO** `ibs_7min` < `0.7425` → IC=-0.198 (n=1777)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7425
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=5333)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.179 (n=1760)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=5350)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.267 (n=1713)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=5524)

- **FILTRO** `ibs_7min` > `0.2659` → IC=-0.194 (n=1809)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2659
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5428)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.190 (n=1802)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=5435)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.162 (n=1911)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=4805)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=1594)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5122)

- **FILTRO** `ibs_7min` < `0.7034` → IC=-0.247 (n=2213)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7034
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4503)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.216 (n=1532)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5184)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.243 (n=2221)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=7516)

- **FILTRO** `ibs_7min` > `0.7402` → IC=-0.172 (n=2434)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7402
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=7303)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=2213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=4627)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.238 (n=2031)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4809)

- **FILTRO** `ibs_7min` < `0.7406` → IC=-0.187 (n=1709)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7406
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5131)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.182 (n=1704)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5136)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.267 (n=1742)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=5296)

- **FILTRO** `ibs_7min` > `0.2759` → IC=-0.182 (n=1757)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5281)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.185 (n=1720)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5318)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.271 (n=1632)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=5408)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.232 (n=1730)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=5310)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.182 (n=2392)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=7680)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.276 (n=1617)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=5180)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.223 (n=1687)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=5110)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.201 (n=1678)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=5119)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.205 (n=2375)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=7191)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1241)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=615)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

- **FILTRO** `libro_liquidez` < `7920.2009` → IC=-0.129 (n=346)

  - _Acción_: SKIP cuando `libro_liquidez` < 7920.2009
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=705)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=345)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.134 (n=151)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=296)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=399)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=588)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.135 (n=919)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.141 (n=416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 14.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `442.3859` → IC=+0.146 (n=306)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 442.3859 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.130 (n=787)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 53.0 (IC base=+0.122)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.438` → IC=+0.162 (n=72)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.438 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.226 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2500.1426` → IC=+0.200 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2500.1426 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 11.0 (IC base=+0.140)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 8.0 (IC base=+0.108)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.177 (n=125)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.203 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.112)

- **PATRÓN** `total_vol_5m` < `385.7846` → IC=+0.202 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 385.7846 (IC base=+0.112)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.182 (n=83)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 73.0 (IC base=+0.112)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.177 (n=165)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.188 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 6.0 (IC base=+0.144)

- **PATRÓN** `total_vol_5m` < `8043.774` → IC=+0.167 (n=166)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 8043.774 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 28.0 (IC base=+0.144)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3602.5746` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3602.5746 (IC base=+0.100)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.6961` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.6961
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=122)

- **FILTRO** `sigma_h` > `0.0044` → IC=-0.236 (n=339)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=175)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0051` → IC=-0.248 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0051
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=51)

- **FILTRO** `T_h` > `89.1097` → IC=-0.397 (n=37)

  - _Acción_: SKIP cuando `T_h` > 89.1097
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=115)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.255 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=-0.078)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7678` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `pct_vs_K` |x|≤ 1.7678 (IC base=-0.078)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.128 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `pct_vs_K` |x|> `8.3214` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.3214
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.198 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=31)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `72.5264` → IC=-0.152 (n=354)

  - _Acción_: SKIP cuando `T_h` > 72.5264
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=119)

- **FILTRO** `pct_vs_K` |x|> `3.7664` → IC=-0.258 (n=118)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7664
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=355)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.308 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.255 (n=308)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.317 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=308)

- **FILTRO** `T_h` > `57.7978` → IC=-0.312 (n=307)

  - _Acción_: SKIP cuando `T_h` > 57.7978
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=103)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0042` → IC=-0.159 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=124)

- **FILTRO** `T_h` > `87.6765` → IC=-0.149 (n=109)

  - _Acción_: SKIP cuando `T_h` > 87.6765
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=54)

- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.381 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=123)

- **FILTRO** `T_h` > `143.1632` → IC=-0.308 (n=50)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=100)

- **FILTRO** `T_h` < `95.9199` → IC=-0.324 (n=49)

  - _Acción_: SKIP cuando `T_h` < 95.9199
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=101)

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
- **FILTRO** `T_h` > `135.986` → IC=-0.288 (n=31)

  - _Acción_: SKIP cuando `T_h` > 135.986
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=99)

- **FILTRO** `pct_vs_K` |x|> `3.4756` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4756
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=100)

- **FILTRO** `sigma_h` > `0.0089` → IC=-0.344 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=94)

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.318 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=93)

- **FILTRO** `T_h` > `57.2342` → IC=-0.312 (n=83)

  - _Acción_: SKIP cuando `T_h` > 57.2342
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=41)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `T_h` > `135.1308` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `T_h` > 135.1308
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=88)

- **FILTRO** `pct_vs_K` |x|> `3.7818` → IC=-0.256 (n=39)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7818
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=77)

- **FILTRO** `sigma_h` > `0.0108` → IC=-0.357 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0108
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=42)

- **FILTRO** `T_h` > `41.2311` → IC=-0.373 (n=61)

  - _Acción_: SKIP cuando `T_h` > 41.2311
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1255` → IC=+0.470 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1255 (IC base=+0.350)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.378 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.350)

- **PATRÓN** `T_h` > `1.2173` → IC=+0.423 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2173 (IC base=+0.350)

- **PATRÓN** `dist_50` > `0.4086` → IC=+0.460 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4086 (IC base=+0.350)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.371 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.350)

- **PATRÓN** `edge` > `0.096` → IC=+0.455 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.422)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.439 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.422)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.449 (n=116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.422)

- **PATRÓN** `T_h` < `0.6208` → IC=+0.435 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6208 (IC base=+0.422)

- **PATRÓN** `T_h` > `1.48` → IC=+0.450 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.48 (IC base=+0.422)

- **PATRÓN** `dist_50` > `0.3938` → IC=+0.483 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3938 (IC base=+0.422)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.476 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.422)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1026` → IC=+0.454 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1026 (IC base=+0.424)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.409 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.424)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.457 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.424)

- **PATRÓN** `T_h` < `1.0313` → IC=+0.452 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0313 (IC base=+0.424)

- **PATRÓN** `T_h` > `0.5167` → IC=+0.407 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5167 (IC base=+0.424)

- **PATRÓN** `dist_50` > `0.4122` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4122 (IC base=+0.424)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.413 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.424)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1992` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1992 (IC base=+0.438)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.470 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.438)

- **PATRÓN** `T_h` > `0.7758` → IC=+0.454 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7758 (IC base=+0.438)

- **PATRÓN** `dist_50` > `0.3553` → IC=+0.457 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3553 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.438)

- **PATRÓN** `edge` > `0.1155` → IC=+0.472 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1155 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.487 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.464)

- **PATRÓN** `T_h` > `0.8021` → IC=+0.466 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8021 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.4572` → IC=+0.491 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4572 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.469 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.464)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=244)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=333)

- **PATRÓN** `streak_estiramiento` < `0.4493` → IC=+0.187 (n=97)

  - _Acción_: Kelly boost +0.93€ cuando `streak_estiramiento` < 0.4493 (IC base=+0.034)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=25)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=53)

- **FILTRO** `volumen_racha` > `945898.4` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `volumen_racha` > 945898.4
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=37)

- **FILTRO** `streak_estiramiento` > `0.4177` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4177
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=45)

- **PATRÓN** `streak_estiramiento` < `0.359` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `streak_estiramiento` < 0.359 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.126 (n=97)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 48.0 (IC base=+0.065)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=88)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=94)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=557)

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

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=775)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=923)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=921)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3410)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1774)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.210 (n=763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.239 (n=763)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.1591` → IC=+0.208 (n=2015)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1591 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2213` → IC=+0.214 (n=763)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2213 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1293` → IC=+0.232 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1293 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.208 (n=2125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=2376)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.617` → IC=+0.279 (n=2288)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.617 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1194` → IC=+0.202 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1194 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.463` → IC=+0.191 (n=1967)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.463 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.921` → IC=+0.286 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.921 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `7478.5102` → IC=+0.207 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7478.5102 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.217 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.202)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=982)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.228 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.274 (n=157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.216)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2017` → IC=+0.243 (n=212)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2017 (IC base=+0.216)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.264 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.242 (n=436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.216)

- **PATRÓN** `ibs_15` > `0.7112` → IC=+0.279 (n=468)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7112 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.250 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.724` → IC=+0.286 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.724 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `16193.642` → IC=+0.247 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16193.642 (IC base=+0.216)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.693` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.693
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=583)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.192 (n=170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0674` → IC=+0.165 (n=225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0674 (IC base=+0.148)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2358` → IC=+0.180 (n=170)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.2358 (IC base=+0.148)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1229` → IC=+0.172 (n=193)

  - _Acción_: Kelly boost +0.86€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1229 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.162 (n=365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.148 (n=510)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 16.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.5797` → IC=+0.242 (n=510)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5797 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.2696` → IC=+0.158 (n=471)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2696 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.851` → IC=+0.258 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.851 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `3459.7073` → IC=+0.161 (n=455)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3459.7073 (IC base=+0.148)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `20.944` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.944
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=183)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.275 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1543` → IC=+0.214 (n=264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1543 (IC base=+0.182)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0747` → IC=+0.191 (n=267)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.0747 (IC base=+0.182)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3526` → IC=+0.228 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3526 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.201 (n=209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.186 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 4.0 (IC base=+0.182)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.274 (n=299)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.1289` → IC=+0.195 (n=175)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1289 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.3286` → IC=+0.190 (n=288)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.3286 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.263` → IC=+0.366 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.263 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=198)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2456.3522` → IC=+0.208 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2456.3522 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.213 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.182)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `16.21` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 16.21 (IC base=+0.005)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.251 (n=512)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.214 (n=253)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0429` → IC=+0.215 (n=573)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0429 (IC base=+0.211)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.270 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.240 (n=286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_15` > `0.5833` → IC=+0.292 (n=575)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5833 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1342` → IC=+0.218 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1342 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.5506` → IC=+0.211 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5506 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.471` → IC=+0.239 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.471 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.374` → IC=+0.214 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.374 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2938.7445` → IC=+0.288 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2938.7445 (IC base=+0.211)

- **PATRÓN** `ibs_15` < `0.1143` → IC=+0.152 (n=624)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.76€ cuando `ibs_15` < 0.1143 (IC base=+0.064)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.370 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.367 (n=517)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.362 (n=345)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.382 (n=344)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1326` → IC=+0.391 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1326 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.401 (n=250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.7863` → IC=+0.398 (n=517)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7863 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.378 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.259` → IC=+0.369 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.259 (IC base=+0.360)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `3820.3005` → IC=+0.375 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3820.3005 (IC base=+0.360)

- **PATRÓN** `ballena_activa_n` < `444.0` → IC=+0.379 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 444.0 (IC base=+0.360)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.368 (n=248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.366 (n=252)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.375 (n=94)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.362)

- **PATRÓN** `drift_15min` |x|≤ `0.5105` → IC=+0.363 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5105 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.370 (n=282)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.13` → IC=+0.391 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.13 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.381 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8038` → IC=+0.394 (n=282)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8038 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3959` → IC=+0.406 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3959 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.369 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` < `26.174` → IC=+0.361 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 26.174 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `16049.8465` → IC=+0.385 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.8465 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `500.0` → IC=+0.413 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 500.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.358 (n=104)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.381 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.354)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.369 (n=158)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.354)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.374 (n=212)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.354)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.381 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.354)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.412 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.354)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.403 (n=236)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` > `0.4534` → IC=+0.377 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4534 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` < `0.2936` → IC=+0.356 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2936 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.854` → IC=+0.379 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.854 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.356 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.354)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.361 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.354)

- **PATRÓN** `libro_liquidez` > `4204.0039` → IC=+0.377 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4204.0039 (IC base=+0.354)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.363 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.354)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.222 (n=847)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=2543)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.201 (n=1233)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2157)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1365` → IC=+0.246 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1365 (IC base=-0.063)

- **PATRÓN** `ibs_15` > `0.6389` → IC=+0.279 (n=818)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6389 (IC base=-0.063)

- **PATRÓN** `dist_vwap_pct` > `0.1081` → IC=+0.195 (n=474)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1081 (IC base=-0.063)

- **PATRÓN** `dist_vwap_pct` < `0.4129` → IC=+0.202 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4129 (IC base=-0.063)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1258` → IC=+0.252 (n=1726)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1258 (IC base=-0.019)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3162` → IC=+0.246 (n=2527)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3162 (IC base=-0.019)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.275 (n=2592)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.019)

- **PATRÓN** `dist_vwap_pct` > `0.8588` → IC=+0.295 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8588 (IC base=-0.019)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.245 (n=2254)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=-0.019)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0471` → IC=-0.214 (n=1318)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0471
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=652)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.230 (n=491)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=1479)

- **FILTRO** `sigma_ewma_delta_pct` > `23.719` → IC=-0.262 (n=280)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.719
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=1690)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.179 (n=194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0027 (IC base=+0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.304 (n=110)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.325 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.123 (n=393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 12.0 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.7503` → IC=+0.328 (n=242)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7503 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.1012` → IC=+0.294 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1012 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.5105` → IC=+0.294 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5105 (IC base=+0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0802` → IC=+0.214 (n=40)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0802 (IC base=-0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1778` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1778 (IC base=-0.192)

- **PATRÓN** `ibs_15` < `0.5567` → IC=+0.329 (n=39)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.5567 (IC base=-0.192)

- **PATRÓN** `dist_vwap_pct` < `0.0415` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0415 (IC base=-0.192)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.438 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.192)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.169 (n=517)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.165 (n=401)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0064 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.169 (n=358)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0038 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.158` → IC=+0.184 (n=353)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.158 (IC base=+0.159)

- **PATRÓN** `drift_15min` |x|≤ `0.4132` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `drift_15min` |x|≤ 0.4132 (IC base=+0.159)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.160 (n=401)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.159)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.216 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.182 (n=284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 11.0 (IC base=+0.159)

- **PATRÓN** `ibs_15` > `0.6515` → IC=+0.264 (n=401)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6515 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` < `0.2663` → IC=+0.173 (n=371)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2663 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.220 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=517)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `9459.3828` → IC=+0.169 (n=182)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 9459.3828 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.242 (n=949)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.3518` → IC=+0.238 (n=835)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3518 (IC base=+0.235)

- **PATRÓN** `drift_15min` |x|≤ `0.7654` → IC=+0.245 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7654 (IC base=+0.235)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2091` → IC=+0.260 (n=431)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2091 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=840)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.235)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.268 (n=949)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.7312` → IC=+0.295 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7312 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.205` → IC=+0.259 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.205 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.476` → IC=+0.240 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.476 (IC base=+0.235)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.204 (n=596)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=200)

- **FILTRO** `drift_60min` |x|> `0.1682` → IC=-0.243 (n=270)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=526)

- **FILTRO** `drift_15min` |x|> `0.8847` → IC=-0.265 (n=198)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8847
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=598)

- **FILTRO** `sigma_ewma_delta_pct` > `18.332` → IC=-0.142 (n=414)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.332
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3338)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.167 (n=43)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.175)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.233 (n=58)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=-0.175)

- **PATRÓN** `dist_vwap_pct` > `0.2865` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2865 (IC base=-0.175)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.175)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.175)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0786` → IC=+0.233 (n=376)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0786 (IC base=-0.040)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1879` → IC=+0.227 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1879 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.271 (n=421)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.6434` → IC=+0.227 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6434 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.172` → IC=+0.232 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.172 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0194` → IC=-0.261 (n=475)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0194
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=477)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.253 (n=297)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=655)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.200)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.200)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1058` → IC=+0.271 (n=434)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1058 (IC base=-0.031)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1709` → IC=+0.302 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1709 (IC base=-0.031)

- **PATRÓN** `ibs_15` < `0.3256` → IC=+0.292 (n=651)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3256 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.8075` → IC=+0.350 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8075 (IC base=-0.031)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.8434` → IC=-0.167 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8434
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.034)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.8434` → IC=-0.167 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8434
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.034)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.302 (n=558)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.293)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.293 (n=748)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.330 (n=280)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2402` → IC=+0.304 (n=279)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2402 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.221` → IC=+0.318 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.221 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.312 (n=872)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8395` → IC=+0.326 (n=837)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8395 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.4333` → IC=+0.338 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4333 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.347 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `12836.5354` → IC=+0.306 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12836.5354 (IC base=+0.293)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.296 (n=400)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.331 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2556` → IC=+0.312 (n=152)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2556 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.109` → IC=+0.315 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.109 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8305` → IC=+0.316 (n=455)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8305 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.347 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.360 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `16217.9862` → IC=+0.331 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16217.9862 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.305 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.298)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.302 (n=382)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.0518` → IC=+0.323 (n=128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0518 (IC base=+0.298)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2883` → IC=+0.321 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2883 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.325 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.298)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.339 (n=382)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` > `0.4406` → IC=+0.311 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4406 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.221` → IC=+0.327 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.221 (IC base=+0.298)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0876` → IC=-0.253 (n=75)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0876
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=226)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.260 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=199)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.197 (n=64)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=132)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2665` → IC=-0.156 (n=30)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2665
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0775` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0775
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.214 (n=33)
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
- **PATRÓN** `T_h` > `80.0063` → IC=+0.234 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 80.0063 (IC base=+0.218)

- **PATRÓN** `ratio` < `0.9763` → IC=+0.472 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9763 (IC base=+0.218)

- **PATRÓN** `T_h` > `145.7546` → IC=+0.392 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7546 (IC base=+0.334)

- **PATRÓN** `ratio` > `1.01` → IC=+0.318 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.01 (IC base=+0.334)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `126.1277` → IC=+0.248 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 126.1277 (IC base=+0.200)

- **PATRÓN** `ratio` < `0.973` → IC=+0.457 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.200)

- **PATRÓN** `T_h` > `104.0063` → IC=+0.293 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 104.0063 (IC base=+0.286)

- **PATRÓN** `ratio` > `1.0479` → IC=+0.399 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0479 (IC base=+0.286)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `82.5234` → IC=+0.270 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 82.5234 (IC base=+0.250)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.432 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.250)

- **PATRÓN** `T_h` > `111.9558` → IC=+0.344 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9558 (IC base=+0.319)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.355 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.319)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1131` → IC=+0.457 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1131 (IC base=+0.401)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.617 sube el IC de +0.202 a +0.279 en UPDOWN_GBM#15min (n=2288). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7112 sube el IC de +0.216 a +0.279 en UPDOWN_GBM#BTC#15min (n=468). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5797 sube el IC de +0.148 a +0.242 en UPDOWN_GBM#ETH#15min (n=510). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de +0.182 a +0.274 en UPDOWN_GBM#SOL#15min (n=299). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5833 sube el IC de +0.211 a +0.292 en UPDOWN_GBM#XRP#15min (n=575). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1143 sube el IC de +0.064 a +0.152 en UPDOWN_GBM#XRP#15min (n=624). Ya aplicado como kelly_boost=+0.76€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6389 sube el IC de -0.063 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=818). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.019 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=2592). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7503 sube el IC de +0.088 a +0.328 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=242). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.5567 sube el IC de -0.192 a +0.329 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=39). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6515 sube el IC de +0.159 a +0.264 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=401). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3605 sube el IC de +0.235 a +0.268 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=949). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de -0.175 a +0.233 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=58). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.040 a +0.271 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=421). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.200 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3256 sube el IC de -0.031 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=651). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8395 sube el IC de +0.293 a +0.326 en UPDOWN_GBM_IBS_ALTO (n=837). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8305 sube el IC de +0.288 a +0.316 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=455). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.298 a +0.339 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=382). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7863 sube el IC de +0.360 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=517). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8038 sube el IC de +0.362 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=282). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.354 a +0.403 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=236). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1532 | +0.096 | +186.77€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1532 | +0.096 | +186.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1165 | +0.102 | +159.38€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1165 | +0.102 | +159.38€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 264 | +0.068 | +11.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 264 | +0.068 | +11.68€ | 6 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 164 | +0.030 | +38.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 164 | +0.030 | +38.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 138 | +0.036 | +35.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 138 | +0.036 | +35.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 33552 | -0.086 | -4432.97€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1711 | -0.015 | -216.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 31841 | -0.089 | -4216.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4292 | -0.117 | -735.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4292 | -0.117 | -735.79€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1711 | -0.015 | -216.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1711 | -0.015 | -216.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3917 | -0.112 | -878.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3917 | -0.112 | -878.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8690 | -0.001 | -806.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8690 | -0.001 | -806.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8432 | -0.104 | -572.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8432 | -0.104 | -572.88€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6510 | -0.157 | -1222.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6510 | -0.157 | -1222.76€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 25412 | -0.020 | +3804.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6577 | +0.002 | +1774.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 18835 | -0.028 | +2030.00€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 25412 | -0.020 | +3804.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6577 | +0.002 | +1774.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 18835 | -0.028 | +2030.00€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 114965 | +0.114 | -5095.78€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 16164 | +0.183 | -478.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 487 | -0.050 | -61.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 91158 | +0.103 | -4288.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7156 | +0.104 | -267.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 15139 | +0.103 | -1064.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 53 | -0.136 | +12.04€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 15071 | +0.104 | -1064.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 22815 | +0.130 | -352.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4854 | +0.198 | -126.34€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 15118 | +0.117 | -135.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2801 | +0.091 | -68.39€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 15186 | +0.093 | -1235.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 61 | -0.119 | -6.11€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 15110 | +0.095 | -1218.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 24419 | +0.125 | -408.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6525 | +0.176 | -103.41€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 15283 | +0.107 | -243.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2599 | +0.100 | -53.21€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 22250 | +0.115 | -1200.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4616 | +0.189 | -263.99€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 390 | -0.013 | -7.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 15488 | +0.094 | -783.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1756 | +0.130 | -146.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 15156 | +0.102 | -834.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 55 | -0.044 | +9.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 15088 | +0.102 | -844.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 18362 | +0.194 | -1148.01€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 18362 | +0.194 | -1148.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4268 | +0.175 | -395.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4268 | +0.175 | -395.10€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1958 | +0.203 | -26.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1958 | +0.203 | -26.98€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4207 | +0.181 | -341.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4207 | +0.181 | -341.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3703 | +0.242 | -129.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3703 | +0.242 | -129.64€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4147 | +0.189 | -268.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4147 | +0.189 | -268.42€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 860 | +0.430 | -23.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 860 | +0.430 | -23.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 340 | +0.436 | -5.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 340 | +0.436 | -5.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 324 | +0.436 | -4.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 324 | +0.436 | -4.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 184 | +0.409 | -11.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 184 | +0.409 | -11.13€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 63694 | +0.200 | -4734.09€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 63694 | +0.200 | -4734.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10958 | +0.183 | -1163.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10958 | +0.183 | -1163.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 10240 | +0.225 | -346.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 10240 | +0.225 | -346.84€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10958 | +0.176 | -1233.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10958 | +0.176 | -1233.32€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10301 | +0.221 | -378.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10301 | +0.221 | -378.32€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10551 | +0.203 | -696.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10551 | +0.203 | -696.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10686 | +0.193 | -915.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10686 | +0.193 | -915.75€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 24226 | +0.116 | +155.29€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 24226 | +0.116 | +155.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 12030 | +0.120 | +143.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 12030 | +0.120 | +143.77€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 12196 | +0.113 | +11.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 12196 | +0.113 | +11.51€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1736 | +0.289 | -21.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1736 | +0.289 | -21.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 783 | +0.280 | -16.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 783 | +0.280 | -16.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 836 | +0.288 | -9.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 836 | +0.288 | -9.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 117 | +0.349 | +4.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 117 | +0.349 | +4.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 779 | +0.439 | -0.58€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 779 | +0.439 | -0.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 374 | +0.436 | -2.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 374 | +0.436 | -2.83€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 359 | +0.442 | +1.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 359 | +0.442 | +1.70€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1330 | +0.072 | -55.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 480 | +0.058 | -38.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 850 | +0.080 | -17.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1042 | +0.079 | -25.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 192 | +0.072 | -7.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 850 | +0.080 | -17.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 222 | +0.031 | -32.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 222 | +0.031 | -32.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 46351 | +0.100 | -1202.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3765 | +0.091 | +45.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 42586 | +0.101 | -1248.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 25726 | +0.104 | -294.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3765 | +0.091 | +45.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 21961 | +0.107 | -340.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 9147 | +0.110 | -20.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 9147 | +0.110 | -20.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 11478 | +0.082 | -887.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 11478 | +0.082 | -887.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 866 | +0.206 | -101.64€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 866 | +0.206 | -101.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 866 | +0.206 | -101.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 866 | +0.206 | -101.64€ | 3 | 4 |
| ✅ GBM_LATE_15M | 32515 | +0.088 | +16134.20€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 32515 | +0.088 | +16134.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5472 | +0.203 | +4210.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5472 | +0.203 | +4210.26€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 4813 | +0.177 | +3455.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4813 | +0.177 | +3455.26€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 5776 | +0.200 | +4354.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5776 | +0.200 | +4354.90€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4613 | +0.033 | +1166.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4613 | +0.033 | +1166.83€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4633 | -0.031 | +1013.31€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4633 | -0.031 | +1013.31€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 7208 | -0.036 | +1933.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7208 | -0.036 | +1933.63€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 35082 | +0.087 | +18658.65€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 35082 | +0.087 | +18658.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6772 | +0.012 | +3498.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6772 | +0.012 | +3498.61€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7268 | +0.014 | +1551.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7268 | +0.014 | +1551.44€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4958 | +0.267 | +5089.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4958 | +0.267 | +5089.52€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5913 | +0.010 | +1304.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5913 | +0.010 | +1304.91€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5708 | +0.035 | +2286.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5708 | +0.035 | +2286.24€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4463 | +0.285 | +4927.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4463 | +0.285 | +4927.92€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 26060 | +0.174 | +20217.27€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 26060 | +0.174 | +20217.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3933 | +0.217 | +3300.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3933 | +0.217 | +3300.55€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4096 | +0.150 | +2972.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4096 | +0.150 | +2972.80€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4139 | +0.214 | +3389.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4139 | +0.214 | +3389.82€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4378 | +0.138 | +3222.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4378 | +0.138 | +3222.86€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4883 | +0.123 | +3550.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4883 | +0.123 | +3550.75€ | 0 | 27 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4631 | +0.211 | +3780.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4631 | +0.211 | +3780.49€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7088 | +0.138 | +3357.46€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7088 | +0.138 | +3357.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 340 | +0.140 | +187.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 340 | +0.140 | +187.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2075 | +0.144 | +1122.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2075 | +0.144 | +1122.59€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2158 | +0.154 | +1063.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2158 | +0.154 | +1063.21€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1604 | +0.107 | +574.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1604 | +0.107 | +574.16€ | 1 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 536 | +0.134 | +234.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 536 | +0.134 | +234.64€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 32755 | +0.180 | +25232.83€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 32755 | +0.180 | +25232.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5211 | +0.230 | +4617.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5211 | +0.230 | +4617.96€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5056 | +0.148 | +3318.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5056 | +0.148 | +3318.54€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5476 | +0.227 | +4757.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5476 | +0.227 | +4757.40€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5327 | +0.135 | +3703.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5327 | +0.135 | +3703.90€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5778 | +0.123 | +3983.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5778 | +0.123 | +3983.56€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5907 | +0.214 | +4851.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5907 | +0.214 | +4851.48€ | 0 | 22 |
| ✅ GBM_LATE_5M | 8899 | +0.176 | +5987.69€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 8899 | +0.176 | +5987.69€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2109 | +0.169 | +1524.69€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2109 | +0.169 | +1524.69€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 965 | +0.172 | +617.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 965 | +0.172 | +617.83€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 2837 | +0.180 | +1870.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2837 | +0.180 | +1870.40€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 1041 | +0.165 | +662.77€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1041 | +0.165 | +662.77€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1112 | +0.148 | +582.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1112 | +0.148 | +582.60€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2393 | +0.073 | +902.48€ | 0 | 13 |
| ✅ GBM_LATE_60M#60min | 2393 | +0.073 | +902.48€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 900 | +0.090 | +340.11€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 900 | +0.090 | +340.11€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 752 | +0.074 | +350.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 752 | +0.074 | +350.02€ | 2 | 10 |
| ✅ GBM_LATE_60M#SOL | 741 | +0.052 | +212.35€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 741 | +0.052 | +212.35€ | 2 | 13 |
| 🚫 GBM_LATE_60M_FADE | 464 | -0.236 | -9.91€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 464 | -0.236 | -9.91€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 171 | -0.217 | -5.91€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 171 | -0.217 | -5.91€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 162 | -0.226 | +0.64€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 162 | -0.226 | +0.64€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 131 | -0.267 | -4.64€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 131 | -0.267 | -4.64€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1022 | +0.087 | +262.77€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1022 | +0.087 | +262.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 380 | +0.079 | +80.98€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 380 | +0.079 | +80.98€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 344 | +0.055 | +43.20€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 344 | +0.055 | +43.20€ | 3 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 298 | +0.133 | +138.59€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 298 | +0.133 | +138.59€ | 1 | 14 |
| ✅ LATE_WINDOW_5MIN | 124 | +0.254 | +105.60€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 124 | +0.254 | +105.60€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 124 | +0.254 | +105.60€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 124 | +0.254 | +105.60€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 2734 | +0.103 | +722.35€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2734 | +0.103 | +722.35€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2734 | +0.103 | +722.35€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2734 | +0.103 | +722.35€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 419 | -0.070 | -32.11€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 419 | -0.070 | -32.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 114 | -0.035 | -2.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 114 | -0.035 | -2.25€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 156 | -0.025 | -5.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 156 | -0.025 | -5.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2788 | +0.022 | +74.04€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2788 | +0.022 | +74.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 139 | +0.039 | +0.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 139 | +0.039 | +0.87€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 415 | +0.028 | +31.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 415 | +0.028 | +31.81€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1054 | +0.030 | +30.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1054 | +0.030 | +30.10€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 639 | +0.016 | +3.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 639 | +0.016 | +3.31€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 340 | +0.018 | +14.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 340 | +0.018 | +14.06€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1362 | -0.045 | -30.28€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1362 | -0.045 | -30.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 392 | -0.043 | -14.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 392 | -0.043 | -14.26€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 450 | -0.026 | -0.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 450 | -0.026 | -0.80€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 520 | -0.063 | -15.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 520 | -0.063 | -15.22€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 4419 | -0.015 | +122.86€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2098 | -0.017 | +50.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2321 | -0.014 | +72.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 123 | -0.012 | +2.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 63 | +0.054 | +11.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 60 | -0.081 | -9.15€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1087 | -0.002 | +43.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 516 | -0.006 | +15.86€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 571 | +0.001 | +27.84€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 500 | -0.018 | +15.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 248 | -0.024 | +4.08€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 252 | -0.012 | +11.70€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 899 | -0.032 | -13.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 413 | -0.047 | -22.34€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 486 | -0.018 | +9.23€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 870 | -0.018 | +23.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 424 | -0.019 | +14.34€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 446 | -0.018 | +9.06€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 940 | -0.011 | +51.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 434 | -0.005 | +27.12€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 506 | -0.016 | +23.89€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 37568 | -0.004 | +1764.74€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 37568 | -0.004 | +1764.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6688 | +0.024 | +889.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6688 | +0.024 | +889.58€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5622 | -0.032 | -98.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5622 | -0.032 | -98.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6786 | +0.019 | +670.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6786 | +0.019 | +670.85€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5414 | -0.052 | -161.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5414 | -0.052 | -161.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6332 | -0.009 | +197.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6332 | -0.009 | +197.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6726 | +0.012 | +267.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6726 | +0.012 | +267.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6150 | -0.059 | -144.63€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6150 | -0.059 | -144.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1218 | +0.001 | -13.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1218 | +0.001 | -13.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1513 | -0.077 | -32.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1513 | -0.077 | -32.33€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 704 | -0.126 | -34.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 704 | -0.126 | -34.31€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1815 | -0.077 | -33.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1815 | -0.077 | -33.31€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 855 | -0.016 | -25.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 855 | -0.016 | -25.54€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3349 | +0.004 | -1.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3349 | +0.004 | -1.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 191 | +0.018 | +1.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 191 | +0.018 | +1.53€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1317 | +0.006 | +6.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1317 | +0.006 | +6.68€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 94364 | -0.073 | +1701.42€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 94364 | -0.073 | +1701.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 16211 | -0.073 | +907.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 16211 | -0.073 | +907.54€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 14347 | -0.098 | -778.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 14347 | -0.098 | -778.83€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 16453 | -0.066 | +909.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 16453 | -0.066 | +909.78€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 13878 | -0.095 | -406.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 13878 | -0.095 | -406.19€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 17112 | -0.052 | +351.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 17112 | -0.052 | +351.80€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 16363 | -0.063 | +717.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 16363 | -0.063 | +717.31€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8043 | -0.030 | -146.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8043 | -0.030 | -146.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1918 | -0.042 | -17.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1918 | -0.042 | -17.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2240 | -0.025 | -29.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2240 | -0.025 | -29.41€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1104 | -0.048 | -21.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1104 | -0.048 | -21.91€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 777 | -0.022 | -25.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 777 | -0.022 | -25.30€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1359 | +0.116 | +502.19€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1223 | +0.122 | +489.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 287 | +0.140 | +146.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 287 | +0.140 | +146.99€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 230 | +0.108 | +65.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 230 | +0.108 | +65.18€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 248 | +0.112 | +95.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 248 | +0.112 | +95.11€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 220 | +0.144 | +113.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 220 | +0.144 | +113.40€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 238 | +0.100 | +68.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 238 | +0.100 | +68.91€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 897 | -0.017 | -21.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 897 | -0.017 | -21.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 178 | +0.000 | +5.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 178 | +0.000 | +5.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 129 | -0.004 | +0.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 129 | -0.004 | +0.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 239 | -0.039 | -18.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 239 | -0.039 | -18.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 195 | +0.008 | +2.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 195 | +0.008 | +2.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 156 | -0.044 | -11.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 156 | -0.044 | -11.19€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 743 | -0.093 | -72.07€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 339 | -0.145 | -81.34€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 259 | -0.190 | -74.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 80 | +0.000 | -7.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 265 | -0.051 | -3.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 186 | -0.053 | -4.01€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 79 | -0.043 | +0.77€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 139 | -0.046 | +12.51€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 110 | -0.062 | +7.10€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 29 | +0.016 | +5.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 555 | -0.119 | -71.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 188 | -0.016 | -0.96€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 883 | -0.201 | -49.70€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 368 | -0.192 | -30.98€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 313 | -0.195 | -31.77€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 55 | -0.167 | +0.79€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 298 | -0.217 | -31.49€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 254 | -0.227 | -37.06€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 44 | -0.152 | +5.58€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 217 | -0.190 | +12.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 198 | -0.185 | +9.63€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 765 | -0.204 | -59.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 118 | -0.175 | +9.51€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 361 | +0.404 | +296.37€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 93 | +0.374 | +76.65€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 93 | +0.374 | +76.65€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 228 | +0.461 | +220.97€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 228 | +0.461 | +220.97€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 361 | +0.404 | +296.37€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 615 | +0.027 | +15.84€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 615 | +0.027 | +15.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 46 | +0.042 | -0.04€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 46 | +0.042 | -0.04€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 65 | -0.007 | -1.72€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 65 | -0.007 | -1.72€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 209 | +0.040 | +15.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 209 | +0.040 | +15.29€ | 3 | 2 |
| ✅ STREAK_FADE_5M | 3079 | -0.021 | -121.33€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3079 | -0.021 | -121.33€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 907 | -0.020 | -31.15€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 907 | -0.020 | -31.15€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 579 | -0.027 | -25.73€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 579 | -0.027 | -25.73€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1437 | -0.017 | -50.04€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1437 | -0.017 | -50.04€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 85 | -0.052 | -8.44€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 85 | -0.052 | -8.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9639 | +0.019 | +104.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9639 | +0.019 | +104.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2629 | +0.021 | +27.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2629 | +0.021 | +27.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2263 | +0.027 | +47.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2263 | +0.027 | +47.45€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2861 | +0.010 | -0.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2861 | +0.010 | -0.81€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1886 | +0.021 | +29.75€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1886 | +0.021 | +29.75€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8689 | +0.013 | -44.43€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8689 | +0.013 | -44.43€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3429 | +0.017 | -9.49€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3429 | +0.017 | -9.49€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3452 | +0.012 | -22.35€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3452 | +0.012 | -22.35€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1808 | +0.008 | -12.60€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1808 | +0.008 | -12.60€ | 1 | 0 |
| ✅ UPDOWN_GBM | 55658 | +0.044 | +4233.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 13915 | +0.079 | +2941.09€ | 0 | 13 |
| ✅ UPDOWN_GBM#240min | 1842 | +0.005 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 36483 | +0.037 | +1241.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3223 | +0.006 | +46.40€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 5695 | +0.082 | +780.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1116 | +0.157 | +492.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 36 | -0.026 | -1.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4543 | +0.064 | +289.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 10749 | +0.050 | +859.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1787 | +0.089 | +408.65€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 492 | +0.012 | +5.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 6935 | +0.053 | +404.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1462 | +0.005 | +40.79€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 73 | -0.087 | +0.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 6614 | +0.053 | +538.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1088 | +0.140 | +400.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 33 | -0.014 | -2.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 5493 | +0.036 | +140.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 12205 | +0.034 | +669.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3383 | +0.056 | +457.11€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 485 | +0.007 | +8.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 7179 | +0.032 | +201.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1094 | +0.005 | -0.16€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 64 | -0.121 | +2.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 12381 | +0.022 | +447.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3292 | +0.032 | +288.18€ | 0 | 13 |
| ✅ UPDOWN_GBM#SOL#240min | 475 | -0.001 | -0.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 7891 | +0.022 | +158.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 667 | +0.008 | +5.78€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 56 | -0.155 | -4.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 8012 | +0.051 | +940.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3249 | +0.099 | +894.48€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 321 | +0.005 | -1.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4442 | +0.019 | +47.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 193 | -0.120 | -2.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 689 | +0.360 | +241.77€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 689 | +0.360 | +241.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 375 | +0.362 | +128.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 375 | +0.362 | +128.07€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 314 | +0.354 | +113.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 314 | +0.354 | +113.70€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 15531 | -0.029 | +3589.17€ | 2 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 15531 | -0.029 | +3589.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1215 | -0.056 | +399.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1215 | -0.056 | +399.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2742 | -0.113 | +122.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2742 | -0.113 | +122.06€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 670 | +0.205 | +516.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 670 | +0.205 | +516.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1799 | +0.212 | +1142.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1799 | +0.212 | +1142.16€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4548 | -0.064 | +607.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4548 | -0.064 | +607.90€ | 4 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4557 | -0.066 | +800.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4557 | -0.066 | +800.70€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 176 | +0.028 | +6.95€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 176 | +0.028 | +6.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 176 | +0.028 | +6.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 176 | +0.028 | +6.95€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1115 | +0.293 | +919.00€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1115 | +0.293 | +919.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 606 | +0.288 | +465.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 606 | +0.288 | +465.31€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 509 | +0.298 | +453.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 509 | +0.298 | +453.70€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 758 | -0.115 | -85.64€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 758 | -0.115 | -85.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 224 | -0.088 | -18.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 224 | -0.088 | -18.30€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 73 | -0.167 | -9.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 73 | -0.167 | -9.78€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 82 | -0.191 | -7.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 82 | -0.191 | -7.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2889 | +0.306 | +1418.94€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1024 | +0.259 | +154.07€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1106 | +0.298 | +483.12€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 759 | +0.378 | +781.76€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.020 n=688 — no justifica filtro, seguir monitorizando
  - _Datos_: n=688 IC=+0.020 PNL=+31.27€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 616 celda(s) pasan gate riguroso completo de 2444 evaluadas (n>=40) y 3420 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.032 < 0.08 — monitorear
  - _Datos_: n=3286 IC=+0.032 PNL=+284.29€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1106/15 IC=+0.298 PNL=+483.12€ | BTC: n=1024/15 IC=+0.259 PNL=+154.07€ | SOL: n=759/15 IC=+0.378 PNL=+781.76€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.129 n=531/60 | contraria IC=+0.187 n=538 | gap=-0.059 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=374, boost estimado=+0.008. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1093/40 IC=+0.004 PNL=-0.63€ | BTC#60min: n=1460/40 IC=+0.005 PNL=+40.80€ | SOL#60min: n=666/40 IC=+0.007 PNL=+5.28€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=429822 | tras_1loss IC=+0.088 n=329983 | tras_2loss IC=+0.057 n=135907/40 | gap=-0.008 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.08 con n=463 PNL=+362.92€
  - _Datos_: n=463 IC=+0.210 PNL=+362.92€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.217 > 0.08 con n=524 PNL=+395.79€
  - _Datos_: n=524 IC=+0.217 PNL=+395.79€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.226 > 0.08 con n=49 PNL=+34.92€
  - _Datos_: n=49 IC=+0.226 PNL=+34.92€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.330 > 0.1 con n=2357 PNL=+1280.20€
  - _Datos_: n=2357 IC=+0.330 PNL=+1280.20€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=437 IC=+0.076 PNL=+51.65€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=437 IC=+0.076 PNL=+51.65€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=65 IC=+0.172 PNL=+39.69€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=65 IC=+0.172 PNL=+39.69€

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
  - _Estado_: n=2184 IC=+0.010 PNL=+8.19€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2184 IC=+0.010 PNL=+8.19€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1035 IC=-0.003 PNL=+37.26€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1035 IC=-0.003 PNL=+37.26€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=688 IC=+0.020 PNL=+31.27€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=688 IC=+0.020 PNL=+31.27€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.201 > 0.1 con n=3040 PNL=+2143.22€
  - _Datos_: n=3040 IC=+0.201 PNL=+2143.22€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1782 IC=+0.089 PNL=+408.00€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1782 IC=+0.089 PNL=+408.00€

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
  - _Estado_: n=732 IC=+0.025 PNL=+58.96€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=732 IC=+0.025 PNL=+58.96€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=77 IC=+0.057 PNL=+4.75€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=77 IC=+0.057 PNL=+4.75€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.252 n=123) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=123 IC=+0.252 PNL=+103.60€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.02 con n=780 PNL=+302.89€
  - _Datos_: n=780 IC=+0.120 PNL=+302.89€

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
  - _Estado_: n=20704 IC=+0.070 PNL=+2892.84€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=20704 IC=+0.070 PNL=+2892.84€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.148 < -0.1 con n=328 PNL=+33.46€
  - _Datos_: n=328 IC=-0.148 PNL=+33.46€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2483 IC=+0.064 PNL=+287.82€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2483 IC=+0.064 PNL=+287.82€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=104 IC=-0.132 PNL=+0.42€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=104 IC=-0.132 PNL=+0.42€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.1 con n=588 PNL=+153.11€
  - _Datos_: n=588 IC=+0.119 PNL=+153.11€

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
  - _Estado_: n=23527 IC=-0.136 PNL=+1679.07€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=23527 IC=-0.136 PNL=+1679.07€

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
  - _Estado_: n=2406 IC=+0.135 PNL=+1385.05€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2406 IC=+0.135 PNL=+1385.05€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=5797 IC=+0.038 PNL=+345.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5797 IC=+0.038 PNL=+345.74€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.089 > 0.08 con n=2670 PNL=+1419.94€
  - _Datos_: n=2670 IC=+0.089 PNL=+1419.94€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.228 < -0.1 con n=2381 PNL=-198.56€
  - _Datos_: n=2381 IC=-0.228 PNL=-198.56€

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
  - _Estado_: n=49 IC=-0.010 PNL=+3.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=49 IC=-0.010 PNL=+3.83€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1392) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1392 IC=+0.101 PNL=+316.87€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.408 n=490) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=490 IC=+0.408 PNL=+690.08€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=10951 IC=+0.183 PNL=-1164.81€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=10951 IC=+0.183 PNL=-1164.81€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.1 con n=174 PNL=+108.08€
  - _Datos_: n=174 IC=+0.210 PNL=+108.08€
