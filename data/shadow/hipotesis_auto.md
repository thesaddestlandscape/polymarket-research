# Hipótesis automáticas — 2026-10-05 00:10 UTC
_Generado por shadow_postmortem.py sobre 751560 resoluciones (PNL=+91150.10€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=573)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.221 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.132)

- **PATRÓN** `n_total_lado` > `71.0` → IC=+0.215 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 71.0 (IC base=+0.132)

- **PATRÓN** `banda_hit_calibrado` > `0.8011` → IC=+0.264 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8011 (IC base=+0.132)

- **PATRÓN** `banda_z` > `9.189` → IC=+0.200 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.189 (IC base=+0.132)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.71` → IC=+0.133 (n=564)

  - _Acción_: Kelly boost +0.66€ cuando `ballenas_wallet_edge_medio` > 0.71 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.135 (n=425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 11.0 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=666)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `2353.6258` → IC=+0.138 (n=564)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2353.6258 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `8556.0995` → IC=+0.121 (n=233)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 8556.0995 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.226 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.197 (n=229)

  - _Acción_: Kelly boost +0.98€ cuando `n_total_lado` > 67.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.6183` → IC=+0.254 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6183 (IC base=+0.140)

- **PATRÓN** `banda_z` > `9.932` → IC=+0.212 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.932 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.141 (n=363)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 12.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=568)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4557.9578` → IC=+0.143 (n=228)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4557.9578 (IC base=+0.140)

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
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=92)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=105)

- **PATRÓN** `py_entrada` > `0.355` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.355 (IC base=+0.125)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=89)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=-0.004)

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
- **FILTRO** `restante_s_al_confirmar` < `144.16` → IC=-0.214 (n=8313)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.16
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=24946)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `131.73` → IC=-0.270 (n=1070)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.73
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=3213)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `124.32` → IC=-0.303 (n=974)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=2923)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `164.74` → IC=-0.222 (n=2086)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 164.74
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=6263)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.33` → IC=-0.318 (n=1613)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.33
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=4840)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.213 (n=16096)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=3860)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `5394.3105` → IC=+0.171 (n=2507)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5394.3105 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=14265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=17154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=13212)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=6338)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7631.7113` → IC=+0.168 (n=2427)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7631.7113 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.207 (n=1799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=1838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=2317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `16039.4185` → IC=+0.222 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16039.4185 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.201 (n=1663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1842)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2365)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `15950.0664` → IC=+0.207 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15950.0664 (IC base=+0.195)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.163 (n=395)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.61 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `4587.7919` → IC=+0.126 (n=249)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 4587.7919 (IC base=+0.093)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.089)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.134 (n=932)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.44 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.143 (n=233)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.089)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.153 (n=2861)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 15.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.356 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.231 (n=1513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.362 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.226 (n=1750)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=718)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.257 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=650)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2159.2967` → IC=+0.155 (n=363)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2159.2967 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.407 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=1223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=649)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=806)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.180 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.372 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `1192.3838` → IC=+0.151 (n=236)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1192.3838 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.225 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.204 (n=13498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=12046)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.235 (n=4504)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.177 (n=3176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3220)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.237 (n=1378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.235 (n=1362)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.336 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.233)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=3133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=3143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.192 (n=1289)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.73 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.252 (n=2905)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.332 (n=997)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=3233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=2759)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.190 (n=2437)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.71 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.195 (n=1170)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.73 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.435 (n=586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `3923.6329` → IC=+0.442 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3923.6329 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.435 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.442 (n=170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `14826.4554` → IC=+0.442 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14826.4554 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.447 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.466 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `3366.033` → IC=+0.451 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3366.033 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.406 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.407)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.410 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.407)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.418 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.407)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.418 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.407)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `6345.2155` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 6345.2155
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.203 (n=42452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.242 (n=18646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=7313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=5821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.198 (n=8018)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=3814)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.268 (n=4318)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=7271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=7698)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=3841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.272 (n=2609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=7039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.204 (n=5583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=2785)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=3045)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=3236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=6494)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.125 (n=6031)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=6243)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.49` → IC=+0.137 (n=6004)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.49 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=3251)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.127 (n=2988)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.16 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.140 (n=3114)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.133 (n=3444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.18` → IC=+0.143 (n=2984)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.18 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.185 (n=3243)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.130 (n=3425)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.135 (n=3025)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.312 (n=926)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.289 (n=1292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `4179.7331` → IC=+0.306 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4179.7331 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.292 (n=613)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.337 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `4308.5918` → IC=+0.295 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4308.5918 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.294 (n=650)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1429.9411` → IC=+0.301 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1429.9411 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.354 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.346)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.364 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.346)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.388 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.346)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.351 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.346)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.375 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.346)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.439 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.442 (n=293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.437 (n=285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.459 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.441 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.451 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=314)

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
- **FILTRO** `py_entrada` > `0.735` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=63)

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
- **FILTRO** `py_entrada` > `0.735` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=63)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4851` → IC=+0.130 (n=10138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4851 (IC base=+0.114)

- **PATRÓN** `ibs_20min` > `0.9845` → IC=+0.242 (n=3380)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9845 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2178` → IC=+0.256 (n=2252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2178 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.015` → IC=+0.185 (n=3853)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.015 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.2155` → IC=+0.252 (n=2839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2155 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.256 (n=2838)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.225 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `1.4663` → IC=+0.212 (n=7097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4663 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.5673` → IC=+0.138 (n=12281)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.5673 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.5813` → IC=+0.202 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5813 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.177 (n=4043)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `1.1978` → IC=+0.178 (n=4472)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.1978 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.224 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.4505` → IC=+0.198 (n=7672)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4505 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.213 (n=7470)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 116.0 (IC base=+0.069)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.222 (n=754)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.189 (n=753)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.008 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.3502` → IC=+0.185 (n=2260)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3502 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.192 (n=1105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.181 (n=1114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 8.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.274 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.225` → IC=+0.287 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.225 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.224 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.181 (n=2135)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=2318)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2042.9486` → IC=+0.186 (n=753)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2042.9486 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.242 (n=1603)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.265 (n=599)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0605` → IC=+0.283 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0605 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.484` → IC=+0.248 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.484 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.405` → IC=+0.236 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.405 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` < `0.0937` → IC=+0.231 (n=1579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0937 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.262 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.6131` → IC=+0.247 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6131 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=1966)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1601.2` → IC=+0.244 (n=1794)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1601.2 (IC base=+0.232)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.239 (n=787)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1074` → IC=+0.250 (n=785)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1074 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.235 (n=1792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.9796` → IC=+0.261 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9796 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.1896` → IC=+0.221 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1896 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.547` → IC=+0.224 (n=1873)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.547 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.786` → IC=+0.258 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.786 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.2524` → IC=+0.224 (n=1784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2524 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6184` → IC=+0.224 (n=1784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6184 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.236 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.4169` → IC=+0.242 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4169 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.184 (n=596)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0026 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0745` → IC=+0.165 (n=595)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0745 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=804)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.7231` → IC=+0.175 (n=1784)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.7231 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1271` → IC=+0.153 (n=1593)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1271 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.294` → IC=+0.140 (n=284)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 11.294 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.3` → IC=+0.142 (n=1637)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.3 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.147 (n=1784)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2044 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `0.852` → IC=+0.136 (n=1189)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.852 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.096` → IC=+0.169 (n=645)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.096 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4565` → IC=+0.147 (n=1673)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4565 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.7829` → IC=+0.145 (n=1115)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7829 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.171 (n=700)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 231.0 (IC base=+0.135)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.199 (n=2279)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0063 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=2286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=2039)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.261 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.345` → IC=+0.256 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.345 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.194 (n=1996)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.3511` → IC=+0.197 (n=302)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.3511 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.7676` → IC=+0.198 (n=1957)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.7676 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2726)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `1953.345` → IC=+0.198 (n=1033)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1953.345 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.220 (n=1764)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.1764` → IC=+0.221 (n=882)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1764 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=930)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.230 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.717` → IC=+0.242 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.717 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.348` → IC=+0.254 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.348 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7298` → IC=+0.216 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7298 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7563` → IC=+0.222 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7563 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.211 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=121)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=2707)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.156 (n=434)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0036 (IC base=+0.043)

- **PATRÓN** `ibs_20min` > `0.9616` → IC=+0.223 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9616 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.5192` → IC=+0.324 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5192 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.909` → IC=+0.177 (n=898)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 4.909 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.335 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.326 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.1123` → IC=+0.333 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1123 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.355 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `1.8701` → IC=+0.322 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8701 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.327 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.1007` → IC=+0.159 (n=708)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1007 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.3065` → IC=+0.196 (n=330)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3065 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.154 (n=744)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8504 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.203 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.5272` → IC=+0.164 (n=949)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.5272 (IC base=+0.026)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.184 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=420)

- **FILTRO** `ibs_20min` < `0.314` → IC=-0.180 (n=123)

  - _Acción_: SKIP cuando `ibs_20min` < 0.314
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=371)

- **FILTRO** `ibs_20min` > `0.2353` → IC=-0.126 (n=2740)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2353
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=1350)

- **FILTRO** `sigma_ewma_delta_pct` > `8.8` → IC=-0.216 (n=431)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.8
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=3659)

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

- **PATRÓN** `ibs_20min` < `0.2353` → IC=+0.135 (n=1350)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.2353 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.1758` → IC=+0.267 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1758 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.279 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.161` → IC=+0.312 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.161 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.4205` → IC=+0.292 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4205 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6379` → IC=-0.173 (n=717)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6379
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2155)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.201 (n=698)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2174)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.207 (n=1045)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=3203)

- **PATRÓN** `dist_vwap_pct` > `0.783` → IC=+0.323 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.783 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.279` → IC=+0.314 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.279 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` < `0.9898` → IC=+0.296 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9898 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.6476` → IC=+0.311 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6476 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1029` → IC=+0.303 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1029 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.4712` → IC=+0.298 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4712 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `2.1732` → IC=+0.306 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1732 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.8565` → IC=+0.285 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8565 (IC base=-0.014)

- **PATRÓN** `volumen_regimen` < `0.7206` → IC=+0.247 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7206 (IC base=-0.014)

- **PATRÓN** `volumen_regimen` > `1.0773` → IC=+0.275 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0773 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.0997` → IC=+0.264 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0997 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.144` → IC=+0.256 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.144 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.253 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.42 (IC base=-0.014)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.199 (n=4401)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0095 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.4717` → IC=+0.188 (n=11791)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4717 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.9855` → IC=+0.285 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9855 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.689` → IC=+0.157 (n=6011)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.689 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` < `1.1783` → IC=+0.247 (n=4812)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1783 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` > `0.6152` → IC=+0.253 (n=4814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6152 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` < `0.0807` → IC=+0.242 (n=7122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0807 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.2951` → IC=+0.260 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2951 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` > `2.6465` → IC=+0.256 (n=2591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6465 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.276 (n=7307)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.101)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.165 (n=4260)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.009 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.5472` → IC=+0.155 (n=11238)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5472 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.6863` → IC=+0.249 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6863 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.2367` → IC=+0.247 (n=3658)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2367 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` < `0.7075` → IC=+0.248 (n=1696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7075 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` > `1.1967` → IC=+0.258 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1967 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.303 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` < `1.5928` → IC=+0.277 (n=2343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5928 (IC base=+0.072)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.279 (n=5226)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.072)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2594` → IC=-0.160 (n=916)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2594
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=2750)

- **FILTRO** `ibs_20min` > `0.761` → IC=-0.176 (n=751)

  - _Acción_: SKIP cuando `ibs_20min` > 0.761
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2258)

- **FILTRO** `sigma_ewma_delta_pct` > `4.581` → IC=-0.173 (n=677)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.581
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2332)

- **PATRÓN** `ibs_20min` > `0.9093` → IC=+0.277 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9093 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.223` → IC=+0.203 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.223 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2277` → IC=+0.274 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2277 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.208 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.230 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.230 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2289` → IC=+0.427 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2289 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.6507` → IC=+0.432 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6507 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` > `1.5457` → IC=+0.424 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5457 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.429 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8668` → IC=+0.165 (n=885)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8668 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.193 (n=689)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1122 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `1.0536` → IC=+0.167 (n=1095)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.0536 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `0.6774` → IC=+0.181 (n=1112)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6774 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.0746` → IC=+0.170 (n=1147)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.0746 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.219 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.4262` → IC=+0.200 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4262 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `2.4271` → IC=+0.187 (n=407)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4271 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.228 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 229.0 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.1458` → IC=+0.224 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1458 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `0.613` → IC=+0.225 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.613 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.219 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.294 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.4389` → IC=+0.231 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4389 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1737` → IC=+0.235 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1737 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.272 (n=2011)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.255 (n=1813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=1791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.778` → IC=+0.282 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.778 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.265 (n=1719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `1.6253` → IC=+0.258 (n=1921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6253 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=2381)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `1943.4584` → IC=+0.270 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1943.4584 (IC base=+0.251)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.301 (n=1668)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.1791` → IC=+0.300 (n=733)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1791 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.319 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.3571` → IC=+0.291 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3571 (IC base=+0.285)

- **PATRÓN** `ibs_20min` > `0.0997` → IC=+0.287 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0997 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.296 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.1951` → IC=+0.281 (n=1616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1951 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.1204` → IC=+0.290 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1204 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` < `1.7249` → IC=+0.298 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7249 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.6641` → IC=+0.294 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6641 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `1935.36` → IC=+0.302 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1935.36 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.286 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.285)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7715` → IC=-0.182 (n=762)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7715
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=2294)

- **PATRÓN** `ibs_20min` > `0.9035` → IC=+0.172 (n=691)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.9035 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.375` → IC=+0.231 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.375 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.0082` → IC=+0.250 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0082 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.1683` → IC=+0.237 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1683 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.0816` → IC=+0.247 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0816 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4132` → IC=+0.259 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4132 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.261 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.1235` → IC=+0.236 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1235 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1804` → IC=+0.221 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1804 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.270 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8412` → IC=+0.266 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8412 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.254 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7606` → IC=-0.183 (n=1400)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7606
  - _Potencial_: sin este filtro IC_bueno=+0.285 (n=1401)

- **FILTRO** `ibs_20min` > `0.6744` → IC=-0.241 (n=705)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6744
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=2117)

- **FILTRO** `sigma_ewma_delta_pct` > `4.823` → IC=-0.203 (n=601)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.823
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=2221)

- **PATRÓN** `ibs_20min` > `0.7606` → IC=+0.285 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7606 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` > `0.2166` → IC=+0.318 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2166 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.69` → IC=+0.171 (n=442)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.69 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` < `0.8605` → IC=+0.311 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8605 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.303 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.300 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.317 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `1.4314` → IC=+0.322 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4314 (IC base=+0.051)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.323 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.051)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.133 (n=1866)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5714 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.2679` → IC=+0.239 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2679 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.271 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7056 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.1889` → IC=+0.228 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1889 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.261 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.248 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.259 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.021)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.330 (n=1442)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.285)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.305 (n=757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` > `0.6494` → IC=+0.318 (n=1614)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6494 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2152` → IC=+0.319 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2152 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.765` → IC=+0.310 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.765 (IC base=+0.285)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.299 (n=1614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.333 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.297 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2474.2976` → IC=+0.296 (n=1442)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2474.2976 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.322 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.315 (n=1139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.1892` → IC=+0.285 (n=751)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1892 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.288 (n=1708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.309 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.3081` → IC=+0.295 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3081 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.518` → IC=+0.298 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.518 (IC base=+0.284)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.314 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.2336` → IC=+0.331 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2336 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.294 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.1375` → IC=+0.281 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1375 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2430.3904` → IC=+0.289 (n=1524)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2430.3904 (IC base=+0.284)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.188 (n=3314)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0047 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.205 (n=3305)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3561` → IC=+0.185 (n=8721)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3561 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=10364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.226 (n=9912)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.1725` → IC=+0.198 (n=4313)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1725 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.446` → IC=+0.252 (n=2001)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.446 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.2091` → IC=+0.167 (n=6583)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2091 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6308` → IC=+0.164 (n=6583)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6308 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2956` → IC=+0.199 (n=1475)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2956 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.5654` → IC=+0.173 (n=4204)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5654 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.6126` → IC=+0.183 (n=3185)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6126 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `1829.4248` → IC=+0.176 (n=9910)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1829.4248 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.189 (n=8827)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 105.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.187 (n=6276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0066 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.221 (n=3136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=3621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.4876` → IC=+0.229 (n=9407)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4876 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` < `0.1688` → IC=+0.167 (n=6503)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1688 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.319` → IC=+0.195 (n=1577)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.319 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1784` → IC=+0.162 (n=6746)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1784 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2918` → IC=+0.214 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2918 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.5586` → IC=+0.172 (n=3832)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5586 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6172` → IC=+0.174 (n=2903)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6172 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.181 (n=8378)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 107.0 (IC base=+0.173)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.242 (n=557)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.206 (n=555)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3412` → IC=+0.221 (n=1666)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3412 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.203 (n=1667)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.202 (n=1211)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.9142` → IC=+0.285 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9142 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.249` → IC=+0.332 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.249 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.245 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.198 (n=1559)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1719)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2044.4902` → IC=+0.202 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2044.4902 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.248 (n=1105)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.249 (n=1119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1009` → IC=+0.292 (n=552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1009 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=1123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=627)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.262 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.392` → IC=+0.245 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.392 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.224` → IC=+0.246 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.224 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.238 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2915` → IC=+0.265 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2915 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4215` → IC=+0.263 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4215 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.6218` → IC=+0.238 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6218 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1596.68` → IC=+0.256 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1596.68 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.227 (n=499)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.0691` → IC=+0.199 (n=496)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0691 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.182 (n=1493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.394` → IC=+0.225 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.394 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.2016` → IC=+0.211 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2016 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.528` → IC=+0.232 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.528 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.6924` → IC=+0.170 (n=655)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6924 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.0768` → IC=+0.160 (n=674)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.0768 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.196 (n=235)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.414` → IC=+0.187 (n=483)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.414 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.4971` → IC=+0.158 (n=483)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4971 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `11874.9267` → IC=+0.160 (n=1328)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11874.9267 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `434.0` → IC=+0.162 (n=1410)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 434.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1548)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.2954` → IC=+0.165 (n=1548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2954 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=754)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=725)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.5923` → IC=+0.196 (n=1548)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5923 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.169 (n=1523)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.883` → IC=+0.197 (n=305)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.883 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2129` → IC=+0.161 (n=1548)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2129 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.2279` → IC=+0.143 (n=1592)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.2279 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0699` → IC=+0.147 (n=693)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0699 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4718` → IC=+0.151 (n=1436)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4718 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.763` → IC=+0.140 (n=957)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.763 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.173 (n=451)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 208.0 (IC base=+0.141)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.227 (n=555)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.2456` → IC=+0.219 (n=1109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2456 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.514` → IC=+0.276 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.514 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` < `0.0964` → IC=+0.203 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0964 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.1273` → IC=+0.205 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1273 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.7296` → IC=+0.212 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7296 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1978)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `1947.8684` → IC=+0.214 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1947.8684 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.240 (n=1239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1429` → IC=+0.259 (n=621)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1429 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.277 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.3506` → IC=+0.246 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3506 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.666` → IC=+0.255 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.666 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.260 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.7477` → IC=+0.236 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7477 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.1707` → IC=+0.226 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1707 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1934.3468` → IC=+0.224 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1934.3468 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.215 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.222)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.184 (n=1398)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0064 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0791` → IC=+0.201 (n=530)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0791 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3409` → IC=+0.205 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3409 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1409` → IC=+0.186 (n=1046)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1409 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.216 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.0413` → IC=+0.158 (n=1398)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0413 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1022` → IC=+0.172 (n=665)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1022 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4307` → IC=+0.167 (n=520)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4307 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.5288` → IC=+0.164 (n=519)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5288 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5174.4297` → IC=+0.196 (n=1059)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 5174.4297 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.155 (n=1527)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 152.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.156 (n=1651)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0071 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.381` → IC=+0.146 (n=1651)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.381 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.180 (n=1651)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6667 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1478` → IC=+0.148 (n=1608)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1478 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.904` → IC=+0.164 (n=573)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.904 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8555` → IC=+0.155 (n=1101)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8555 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.181 (n=246)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.8192` → IC=+0.138 (n=1018)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8192 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5424` → IC=+0.126 (n=509)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.5424 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `4266.2624` → IC=+0.159 (n=1101)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4266.2624 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.122 (n=1468)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 151.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.158 (n=820)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.01 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4487` → IC=+0.128 (n=1591)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4487 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.5045` → IC=+0.214 (n=1808)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5045 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `1.0603` → IC=+0.214 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0603 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.911` → IC=+0.262 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.911 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.2085` → IC=+0.138 (n=1807)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2085 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `0.6472` → IC=+0.132 (n=1807)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6472 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.1633` → IC=+0.134 (n=1818)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1633 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.129 (n=753)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.5436` → IC=+0.143 (n=769)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5436 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4749` → IC=+0.130 (n=582)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4749 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=1889)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2388.4402` → IC=+0.183 (n=1205)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2388.4402 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.148 (n=1416)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 46.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.158 (n=798)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0061 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.103` → IC=+0.177 (n=605)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.103 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=1836)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5789` → IC=+0.216 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5789 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.7586` → IC=+0.124 (n=333)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.7586 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.1986` → IC=+0.147 (n=1654)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1986 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.439` → IC=+0.127 (n=745)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 3.439 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.6382` → IC=+0.153 (n=606)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6382 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2277` → IC=+0.152 (n=317)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2277 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4523` → IC=+0.137 (n=554)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4523 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `1.8156` → IC=+0.125 (n=1107)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.8156 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `3058.0546` → IC=+0.190 (n=605)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3058.0546 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.127 (n=1615)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 52.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.229 (n=1701)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.2883` → IC=+0.216 (n=1134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2883 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.208 (n=1775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=767)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.244 (n=1706)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.2055` → IC=+0.213 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2055 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.2961` → IC=+0.205 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2961 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.588` → IC=+0.245 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.588 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.1979` → IC=+0.212 (n=1701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1979 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.6251` → IC=+0.217 (n=1701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6251 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.269 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.4773` → IC=+0.210 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4773 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4242` → IC=+0.213 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4242 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2466.5198` → IC=+0.208 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2466.5198 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.228 (n=765)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.219 (n=788)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.242 (n=580)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.236 (n=859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.02` → IC=+0.288 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.02 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `1.1734` → IC=+0.232 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1734 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.365` → IC=+0.252 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.365 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.6364` → IC=+0.225 (n=1736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6364 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.271 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.214 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2408.9706` → IC=+0.220 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2408.9706 (IC base=+0.214)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.195 (n=1145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0042 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.171 (n=864)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0084 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3399` → IC=+0.178 (n=2281)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3399 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.187 (n=2372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.3438` → IC=+0.196 (n=2592)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3438 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.7944` → IC=+0.187 (n=417)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.7944 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.743` → IC=+0.194 (n=1131)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.743 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8717` → IC=+0.191 (n=1543)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8717 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `1.2092` → IC=+0.175 (n=771)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.2092 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` < `0.0752` → IC=+0.170 (n=2299)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.0752 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1633` → IC=+0.174 (n=692)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1633 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4385` → IC=+0.182 (n=839)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4385 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.539` → IC=+0.177 (n=839)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.539 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=2950)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2701.397` → IC=+0.170 (n=2316)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2701.397 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.186 (n=2373)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 144.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.155 (n=889)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0037 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.194 (n=887)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.0714 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.145 (n=860)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2760.1991` → IC=+0.126 (n=2373)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2760.1991 (IC base=+0.106)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.126 (n=874)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 20.0 (IC base=+0.106)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.202 (n=307)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3292` → IC=+0.168 (n=696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3292 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.187 (n=647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.6381` → IC=+0.206 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6381 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.2873` → IC=+0.172 (n=245)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.2873 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.203` → IC=+0.173 (n=301)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.203 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.971` → IC=+0.148 (n=732)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.971 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8855` → IC=+0.178 (n=464)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8855 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.1564` → IC=+0.152 (n=725)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1564 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.2348` → IC=+0.156 (n=597)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.2348 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.5183` → IC=+0.156 (n=606)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5183 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `10600.6989` → IC=+0.158 (n=696)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 10600.6989 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.200 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 152.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.206 (n=277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3447` → IC=+0.159 (n=829)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3447 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.144 (n=835)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.611` → IC=+0.181 (n=729)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.611 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1812` → IC=+0.156 (n=812)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1812 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.088` → IC=+0.145 (n=756)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.088 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2185` → IC=+0.145 (n=829)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2185 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.6958` → IC=+0.154 (n=740)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6958 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1598` → IC=+0.193 (n=223)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1598 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1209` → IC=+0.158 (n=721)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1209 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4081` → IC=+0.148 (n=819)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4081 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=1073)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `11929.6805` → IC=+0.141 (n=740)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 11929.6805 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `294.0` → IC=+0.156 (n=701)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 294.0 (IC base=+0.140)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.241 (n=547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.3973` → IC=+0.210 (n=819)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3973 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=861)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.67` → IC=+0.252 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.67 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.361` → IC=+0.211 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.361 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.2089` → IC=+0.208 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2089 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.057` → IC=+0.218 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.057 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `0.8422` → IC=+0.213 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8422 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `1.1822` → IC=+0.220 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1822 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.232 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.4253` → IC=+0.232 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4253 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `2.1126` → IC=+0.229 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1126 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.123 (n=680)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0061 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.127 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 11.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.0868` → IC=+0.156 (n=257)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.0868 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `0.6885` → IC=+0.142 (n=339)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6885 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.137 (n=122)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `3957.4133` → IC=+0.125 (n=688)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 3957.4133 (IC base=+0.098)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4756` → IC=-0.124 (n=267)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4756
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=520)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.171 (n=611)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0051 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.5405` → IC=+0.160 (n=610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5405 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.947` → IC=+0.233 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.947 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.339` → IC=+0.216 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.339 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `1.0674` → IC=+0.175 (n=537)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0674 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.6528` → IC=+0.165 (n=610)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6528 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.4932` → IC=+0.158 (n=589)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4932 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.1991` → IC=+0.173 (n=267)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1991 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.162 (n=646)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `3078.7088` → IC=+0.194 (n=204)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3078.7088 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.4756` → IC=+0.144 (n=520)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.4756 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.569` → IC=+0.124 (n=248)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.569 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `2864.9802` → IC=+0.152 (n=268)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2864.9802 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.124 (n=360)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 23.0 (IC base=+0.053)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.172 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0238 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.198 (n=127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0144 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.169 (n=167)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.209 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.5556` → IC=+0.188 (n=171)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5556 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.2434` → IC=+0.173 (n=105)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.2434 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `1.115` → IC=+0.164 (n=212)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 1.115 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.737` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 7.737 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.181 (n=164)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `1.111` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.111 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.2526` → IC=+0.181 (n=186)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.2526 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.185 (n=195)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `2503.9142` → IC=+0.174 (n=127)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2503.9142 (IC base=+0.155)

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
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.179 (n=4262)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0046 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.210 (n=4263)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=13404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.9934` → IC=+0.309 (n=4261)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9934 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.9047` → IC=+0.200 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9047 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.395` → IC=+0.249 (n=3147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.395 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `0.8808` → IC=+0.173 (n=5708)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8808 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2899` → IC=+0.201 (n=1736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2899 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.5958` → IC=+0.196 (n=4121)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5958 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1815.2984` → IC=+0.181 (n=12783)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1815.2984 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.202 (n=10045)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.195 (n=5053)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0053 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1466` → IC=+0.192 (n=5052)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1466 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=4364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.4529` → IC=+0.246 (n=10102)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4529 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2428` → IC=+0.162 (n=7101)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2428 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.069` → IC=+0.202 (n=1609)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.069 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.734` → IC=+0.183 (n=11077)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.734 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.162 (n=3429)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7056 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2897` → IC=+0.248 (n=1520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2897 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `1.8642` → IC=+0.189 (n=7140)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8642 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.204 (n=6981)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.250 (n=710)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.226 (n=712)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.3555` → IC=+0.210 (n=2126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3555 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=1037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=1418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.328 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.357 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.267 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.5769` → IC=+0.215 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5769 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2043.02` → IC=+0.217 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2043.02 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.263 (n=1157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.262 (n=1732)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1247` → IC=+0.280 (n=762)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1247 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.359` → IC=+0.282 (n=1524)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.359 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.506` → IC=+0.264 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.506 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.291 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.6325` → IC=+0.275 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6325 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=1898)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1596.72` → IC=+0.269 (n=1732)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1596.72 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.212 (n=682)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1797` → IC=+0.165 (n=1364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1797 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=2146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.2889` → IC=+0.207 (n=2045)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2889 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1263` → IC=+0.190 (n=1176)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1263 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.762` → IC=+0.185 (n=344)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 11.762 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.227` → IC=+0.152 (n=1871)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.227 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.6272` → IC=+0.170 (n=682)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6272 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2717` → IC=+0.195 (n=293)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2717 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1425` → IC=+0.161 (n=1750)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1425 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5175` → IC=+0.156 (n=1776)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5175 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `277.0` → IC=+0.178 (n=851)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 277.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1707)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.3284` → IC=+0.157 (n=1705)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3284 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.149 (n=770)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6835` → IC=+0.193 (n=1705)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.6835 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1316` → IC=+0.164 (n=1544)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1316 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.518` → IC=+0.157 (n=287)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.518 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.327` → IC=+0.144 (n=1548)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.327 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.157 (n=1705)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1917 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1535` → IC=+0.201 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1535 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.153 (n=1606)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.158 (n=1071)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `415.0` → IC=+0.142 (n=1329)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 415.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.250 (n=699)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=2101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=2114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.85` → IC=+0.295 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.85 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.2057` → IC=+0.225 (n=2109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2057 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.7675` → IC=+0.232 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7675 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2503)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1953.02` → IC=+0.235 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1953.02 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.241 (n=1726)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.1782` → IC=+0.247 (n=863)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1782 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.259 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.233 (n=915)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0148` → IC=+0.301 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0148 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.943` → IC=+0.281 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.943 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3428` → IC=+0.297 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3428 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.233 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.154` → IC=+0.241 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.154 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1937.383` → IC=+0.241 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1937.383 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.233 (n=1778)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.198 (n=962)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.4298` → IC=+0.154 (n=2184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4298 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=2285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.2739` → IC=+0.190 (n=2184)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2739 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.5525` → IC=+0.165 (n=606)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.5525 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.19` → IC=+0.156 (n=897)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 4.19 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8748` → IC=+0.165 (n=1456)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8748 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1655` → IC=+0.183 (n=579)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1655 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5223` → IC=+0.161 (n=936)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5223 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.1748` → IC=+0.156 (n=964)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1748 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7348.7335` → IC=+0.233 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7348.7335 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.180 (n=691)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 70.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.165 (n=1173)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0051 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3487` → IC=+0.139 (n=1546)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.3487 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.5987` → IC=+0.196 (n=1546)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5987 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1468` → IC=+0.134 (n=1529)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1468 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.298` → IC=+0.164 (n=266)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.298 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8747` → IC=+0.139 (n=1172)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8747 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2976` → IC=+0.229 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2976 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `2.2502` → IC=+0.132 (n=1480)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.2502 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4458` → IC=+0.140 (n=1682)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4458 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `8890.8006` → IC=+0.202 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8890.8006 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `168.0` → IC=+0.131 (n=1685)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 168.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.135 (n=2196)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0056 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.5596` → IC=+0.129 (n=2193)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.5596 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.200 (n=2194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4615 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0427` → IC=+0.212 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0427 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.567` → IC=+0.246 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.567 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2342` → IC=+0.138 (n=2193)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2342 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1615` → IC=+0.128 (n=2261)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1615 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.1865` → IC=+0.134 (n=969)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.1865 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2232)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2551.935` → IC=+0.235 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2551.935 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.146 (n=659)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 27.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.181 (n=698)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0057 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1303` → IC=+0.163 (n=696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1303 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5128` → IC=+0.234 (n=1837)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5128 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.217` → IC=+0.138 (n=1709)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.217 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.486` → IC=+0.131 (n=2011)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.486 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.645` → IC=+0.166 (n=696)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.645 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2227` → IC=+0.178 (n=337)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2227 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.1605` → IC=+0.134 (n=1690)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1605 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2793.9248` → IC=+0.193 (n=696)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2793.9248 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.135 (n=1677)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 50.0 (IC base=+0.119)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.230 (n=2142)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.218 (n=1539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.261 (n=1919)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.2117` → IC=+0.232 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2117 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.305` → IC=+0.275 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.305 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.2397` → IC=+0.217 (n=2142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2397 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.6415` → IC=+0.221 (n=2142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6415 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2367` → IC=+0.243 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2367 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.5119` → IC=+0.246 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5119 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=2051)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2350.077` → IC=+0.216 (n=2142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2350.077 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.219 (n=748)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.231 (n=1016)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.229 (n=1594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.4198` → IC=+0.262 (n=1972)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4198 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `1.2049` → IC=+0.218 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2049 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.2952` → IC=+0.215 (n=2077)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2952 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.857` → IC=+0.255 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.857 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.2299` → IC=+0.240 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2299 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.279 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.4288` → IC=+0.212 (n=2050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4288 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2416.2064` → IC=+0.216 (n=2002)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2416.2064 (IC base=+0.213)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.164 (n=3743)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.226 (n=1249)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.5013` → IC=+0.193 (n=3738)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.5013 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=1418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.183 (n=1691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.240 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.1696` → IC=+0.192 (n=1417)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1696 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.244` → IC=+0.211 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.244 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7121` → IC=+0.186 (n=1139)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.7121 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.8968` → IC=+0.187 (n=1722)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.8968 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.1692` → IC=+0.209 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1692 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.4557` → IC=+0.192 (n=1231)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4557 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.8658` → IC=+0.186 (n=2459)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8658 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=2794)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2926.5639` → IC=+0.190 (n=3339)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2926.5639 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.221 (n=943)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.4846` → IC=+0.179 (n=2819)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.4846 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=1007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=1267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.1825` → IC=+0.187 (n=1241)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.1825 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.6554` → IC=+0.180 (n=529)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6554 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.2354` → IC=+0.156 (n=2495)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.2354 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.214` → IC=+0.171 (n=2812)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.214 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.2586` → IC=+0.167 (n=2655)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2586 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.168 (n=2569)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.166 (n=587)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.5388` → IC=+0.171 (n=1225)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5388 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.8277` → IC=+0.173 (n=1856)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8277 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=3743)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `12360.4208` → IC=+0.169 (n=940)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 12360.4208 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `205.0` → IC=+0.172 (n=2416)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 205.0 (IC base=+0.163)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.236 (n=346)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.0805` → IC=+0.266 (n=173)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0805 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.215 (n=237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.516` → IC=+0.231 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.516 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.7635` → IC=+0.213 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7635 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.3179` → IC=+0.217 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3179 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.039` → IC=+0.226 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.039 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.529` → IC=+0.212 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.529 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.219 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.596` → IC=+0.219 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.596 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.231 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `12550.0528` → IC=+0.235 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12550.0528 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.229 (n=467)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.366` → IC=+0.164 (n=1057)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.366 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.181 (n=406)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.1485` → IC=+0.181 (n=465)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1485 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.153 (n=479)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6084 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6653` → IC=+0.180 (n=101)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6653 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.2114` → IC=+0.151 (n=1071)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2114 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.385` → IC=+0.168 (n=1039)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.385 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.187 (n=705)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8812 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.180 (n=220)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.5397` → IC=+0.156 (n=1053)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.5397 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.168 (n=702)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11518.9437` → IC=+0.162 (n=1056)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11518.9437 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `698.0` → IC=+0.160 (n=1011)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 698.0 (IC base=+0.149)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.188 (n=213)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.006 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.180 (n=289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.01 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.587` → IC=+0.173 (n=637)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.587 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.242 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.56` → IC=+0.231 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.56 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2079` → IC=+0.204 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2079 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.6711` → IC=+0.173 (n=212)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.6711 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.8234` → IC=+0.171 (n=567)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8234 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2429.8516` → IC=+0.204 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2429.8516 (IC base=+0.166)

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

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.237)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.219 (n=393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.1515` → IC=+0.212 (n=519)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1515 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.194 (n=537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` < `0.5305` → IC=+0.204 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5305 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.8854` → IC=+0.196 (n=393)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.8854 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.2066` → IC=+0.201 (n=985)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2066 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.178` → IC=+0.200 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.178 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `1.0851` → IC=+0.196 (n=1037)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 1.0851 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` > `1.2457` → IC=+0.194 (n=393)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 1.2457 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.107` → IC=+0.192 (n=1083)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.107 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.205 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `2.4777` → IC=+0.198 (n=1155)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.4777 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=1184)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.192)

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
- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.173 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0107 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.168 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 3.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.9296` → IC=+0.236 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9296 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.2874` → IC=+0.202 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2874 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.547` → IC=+0.206 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.547 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.721` → IC=+0.184 (n=175)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.721 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1616` → IC=+0.212 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1616 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1817` → IC=+0.144 (n=338)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1817 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.8229` → IC=+0.167 (n=256)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8229 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.148 (n=472)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `3007.5542` → IC=+0.167 (n=397)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3007.5542 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.158 (n=381)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 59.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.188 (n=312)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0066 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.3887` → IC=+0.206 (n=209)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3887 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.172 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 16.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.194 (n=217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 10.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` < `0.1081` → IC=+0.229 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1081 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.5969` → IC=+0.214 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5969 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.423` → IC=+0.171 (n=162)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 2.423 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.281` → IC=+0.168 (n=302)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 5.281 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `1.4149` → IC=+0.170 (n=313)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.4149 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `1.1845` → IC=+0.167 (n=142)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.1845 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.219 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.611` → IC=+0.191 (n=134)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.611 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.1939` → IC=+0.179 (n=138)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.1939 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3140.095` → IC=+0.201 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3140.095 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.217 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.165)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.156 (n=539)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.083)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.121 (n=566)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 16.0 (IC base=+0.083)

- **PATRÓN** `ibs_20min` > `0.4597` → IC=+0.157 (n=1133)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.4597 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.1412` → IC=+0.141 (n=635)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1412 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.465` → IC=+0.189 (n=262)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.465 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.179 (n=157)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.083)

- **PATRÓN** `libro_liquidez` > `1360.1033` → IC=+0.122 (n=739)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1360.1033 (IC base=+0.083)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.121 (n=238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0032 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.2261` → IC=+0.257 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2261 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` < `0.111` → IC=+0.138 (n=459)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.111 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.082` → IC=+0.143 (n=387)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.082 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.1418` → IC=+0.181 (n=111)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1418 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` < `2.6098` → IC=+0.153 (n=399)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.6098 (IC base=+0.052)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.141 (n=418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0057 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.4301` → IC=+0.176 (n=387)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.4301 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1239` → IC=+0.164 (n=212)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1239 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `2.4916` → IC=+0.129 (n=346)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.4916 (IC base=+0.099)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.124 (n=163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0035 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.298 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.069` → IC=+0.140 (n=209)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.069 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.92` → IC=+0.157 (n=211)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.92 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `1.151` → IC=+0.124 (n=219)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.151 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` > `0.6803` → IC=+0.124 (n=195)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6803 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.0743` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0743 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` < `2.5035` → IC=+0.151 (n=196)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.5035 (IC base=+0.079)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.154 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=151)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.154 (n=270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0047 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.7033` → IC=+0.216 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7033 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.1226` → IC=+0.174 (n=210)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1226 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.674` → IC=+0.276 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.674 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `0.8141` → IC=+0.130 (n=249)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.8141 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `1.7915` → IC=+0.143 (n=214)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.7915 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `1135.9488` → IC=+0.160 (n=330)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1135.9488 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.7058` → IC=+0.144 (n=130)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.7058 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.003)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.235 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=142)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.281 (n=112)

- **PATRÓN** `ibs_20min` > `0.7692` → IC=+0.169 (n=249)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.7692 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.736` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.736 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.631` → IC=+0.142 (n=79)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.631 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2448` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2448 (IC base=+0.049)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.177 (n=125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0086 (IC base=+0.060)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.281 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` < `0.1829` → IC=+0.176 (n=109)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1829 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.949` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.949 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.6377` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6377 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` > `0.9765` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.9765 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` < `2.1886` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1886 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `1.8705` → IC=+0.214 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8705 (IC base=+0.060)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.05 (IC base=+0.060)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.300 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=185)

- **FILTRO** `dist_vwap_pct` > `0.2381` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=228)

- **FILTRO** `volumen_regimen` < `0.7363` → IC=-0.355 (n=60)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7363
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=183)

- **FILTRO** `sigma_h` > `0.0057` → IC=-0.368 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=160)

- **FILTRO** `dist_vwap_pct` > `0.3287` → IC=-0.389 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3287
  - _Potencial_: sin este filtro IC_bueno=-0.249 (n=177)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=181)

- **FILTRO** `volumen_pendiente_norm` > `0.0549` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0549
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=100)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2353` → IC=-0.262 (n=40)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2353
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=40)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=66)

- **FILTRO** `volumen_regimen` > `0.8507` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8507
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=66)

- **FILTRO** `volumen_spike_ratio` > `1.5874` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5874
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=28)

- **FILTRO** `libro_liquidez` < `3685.6992` → IC=-0.233 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 3685.6992
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=59)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0023` → IC=-0.357 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0023
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=60)

- **FILTRO** `ibs_20min` < `0.7738` → IC=-0.402 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7738
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.342 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=62)

- **FILTRO** `dist_vwap_pct` > `0.1182` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1182
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=52)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=32)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=-0.179)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=68)

- **FILTRO** `ibs_20min` < `0.2444` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2444
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=57)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=58)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.178 (n=169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0057 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.128 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.6508` → IC=+0.145 (n=370)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6508 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.4822` → IC=+0.204 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4822 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.6625` → IC=+0.130 (n=125)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.6625 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.5157` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5157 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.1558` → IC=+0.175 (n=333)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1558 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.957` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `3965.7979` → IC=+0.172 (n=172)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3965.7979 (IC base=+0.079)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6382` → IC=-0.263 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6382
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=110)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.178 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0024 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.216 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.206 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1435 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.0797` → IC=+0.151 (n=170)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.0797 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.332` → IC=+0.174 (n=136)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 4.332 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1443` → IC=+0.147 (n=168)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1443 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6691` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6691 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.1846` → IC=+0.201 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1846 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.2913` → IC=+0.197 (n=120)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2913 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4563` → IC=+0.174 (n=136)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.4563 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3936.7645` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3936.7645 (IC base=+0.144)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1659` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1659
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=96)

- **FILTRO** `libro_liquidez` < `1457.1387` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 1457.1387
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=117)

- **FILTRO** `ibs_20min` > `0.1906` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1906
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=119)

- **PATRÓN** `ibs_20min` < `0.1906` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1906 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.489` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.489 (IC base=+0.058)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.0941` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0941
  - _Potencial_: sin este filtro IC_bueno=+0.235 (n=32)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.279 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.246 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7333 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.92` → IC=+0.235 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.92 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.6243` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6243 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` < `0.1413` → IC=+0.225 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1413 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.025` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.025 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.278 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.089` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.089 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.357 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.223 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.818` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.818 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.0941` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0941 (IC base=-0.029)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4522` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4522 (IC base=+0.281)

- **PATRÓN** `elapsed_s` > `193.1` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.1 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.8028` → IC=+0.360 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8028 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.281)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.226)

- **PATRÓN** `elapsed_s` > `177.0` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 177.0 (IC base=+0.226)

- **PATRÓN** `elapsed_s` < `177.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 177.0 (IC base=+0.226)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.318 (n=31)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `1457.0` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1457.0 (IC base=+0.226)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4522` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4522 (IC base=+0.281)

- **PATRÓN** `elapsed_s` > `193.1` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.1 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.8028` → IC=+0.360 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8028 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.281)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.226)

- **PATRÓN** `elapsed_s` > `177.0` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 177.0 (IC base=+0.226)

- **PATRÓN** `elapsed_s` < `177.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 177.0 (IC base=+0.226)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.318 (n=31)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `1457.0` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1457.0 (IC base=+0.226)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=960)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2928.7278` → IC=+0.155 (n=331)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2928.7278 (IC base=+0.105)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=960)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2928.7278` → IC=+0.155 (n=331)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2928.7278 (IC base=+0.105)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=148)

- **FILTRO** `libro_liquidez` < `9884.3291` → IC=-0.182 (n=108)

  - _Acción_: SKIP cuando `libro_liquidez` < 9884.3291
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=56)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=231)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=217)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=47)

- **FILTRO** `libro_liquidez` < `10724.0239` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 10724.0239
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=51)

- **FILTRO** `liq_n` < `5.0` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `liq_n` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=23)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=96)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2533)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=95)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=52)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=84)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=95)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=100)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=162)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.056)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=996)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=950)

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
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=587)

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
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=298)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.161 (n=110)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.495 (IC base=+0.029)

- **PATRÓN** `libro_liquidez` > `3909.4956` → IC=+0.142 (n=107)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3909.4956 (IC base=+0.029)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=755)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=755)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.131 (n=242)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=593)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=497)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=497)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=207)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=207)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=169)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=134)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=123)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=147)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=119)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=132)

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
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=181)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.124 (n=1086)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1116)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.517` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.517
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=10)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.121 (n=151)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=58)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.150 (n=78)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=210)

- **PATRÓN** `py_entrada` > `0.52` → IC=+0.167 (n=58)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.52 (IC base=-0.040)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.225 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.047)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=119)

- **FILTRO** `restante_min` < `10.16` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `restante_min` < 10.16
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=96)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.152 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=99)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.189 (n=43)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=107)

- **FILTRO** `restante_min` < `3.99` → IC=-0.127 (n=108)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **FILTRO** `lag_apertura_s` > `60.75` → IC=-0.132 (n=112)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.75
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=38)

- **PATRÓN** `py_entrada` < `0.57` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.57 (IC base=+0.071)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.144 (n=144)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=50)

- **FILTRO** `profundidad_ratio` < `54.9` → IC=-0.212 (n=64)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.9
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=130)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=166)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.150 (n=158)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=92)

- **FILTRO** `restante_min` < `3.43` → IC=-0.226 (n=82)

  - _Acción_: SKIP cuando `restante_min` < 3.43
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=168)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.172 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=194)

- **FILTRO** `lag_apertura_s` > `92.29` → IC=-0.209 (n=84)

  - _Acción_: SKIP cuando `lag_apertura_s` > 92.29
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=166)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.46 (IC base=+0.033)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=148)

- **PATRÓN** `lag_apertura_s` < `90.78` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 90.78 (IC base=-0.011)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.45` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.45 (IC base=+0.007)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.156 (n=155)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=86)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.148 (n=86)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` > 0.5 (IC base=-0.047)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.222 (n=77)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=219)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.162 (n=4510)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=13729)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.165 (n=4549)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=14305)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.192 (n=796)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2438)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.149 (n=790)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=2580)

- **PATRÓN** `libro_liquidez` > `1811.12` → IC=+0.131 (n=1100)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1811.12 (IC base=+0.036)

- **PATRÓN** `libro_liquidez` > `1581.1195` → IC=+0.145 (n=1146)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1581.1195 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.173 (n=817)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2460)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.195 (n=798)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2619)

- **PATRÓN** `libro_liquidez` > `1811.2984` → IC=+0.129 (n=1115)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1811.2984 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.166 (n=777)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=2450)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2452)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3192)

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

- **FILTRO** `libro_liquidez` < `1955.8572` → IC=-0.173 (n=328)

  - _Acción_: SKIP cuando `libro_liquidez` < 1955.8572
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=668)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.144 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.037)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=12657)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=28440)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=9631)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=31466)

- **FILTRO** `ibs_7min` < `0.2625` → IC=-0.234 (n=10274)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2625
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=30823)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=13862)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=27235)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.236 (n=12684)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=39435)

- **FILTRO** `ibs_7min` > `0.2903` → IC=-0.180 (n=13020)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2903
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=39099)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.140 (n=2060)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=4930)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=1664)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=5326)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.250 (n=2301)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4689)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.184 (n=1548)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=5442)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.266 (n=2211)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=6801)

- **FILTRO** `ibs_7min` > `0.7875` → IC=-0.210 (n=2252)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7875
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=6760)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=1661)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5364)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.249 (n=1721)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=5304)

- **FILTRO** `ibs_7min` < `0.7429` → IC=-0.197 (n=1756)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=5269)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.179 (n=1753)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=5272)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.266 (n=1694)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=5460)

- **FILTRO** `ibs_7min` > `0.2662` → IC=-0.195 (n=1788)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2662
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5366)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.189 (n=1782)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=5372)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.163 (n=1634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=4999)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=1571)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5062)

- **FILTRO** `ibs_7min` < `0.7037` → IC=-0.246 (n=2188)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7037
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=4445)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.215 (n=1521)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5112)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.243 (n=2200)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=7416)

- **FILTRO** `ibs_7min` > `0.741` → IC=-0.172 (n=2402)

  - _Acción_: SKIP cuando `ibs_7min` > 0.741
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=7214)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=2172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=4588)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.237 (n=2005)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4755)

- **FILTRO** `ibs_7min` < `0.7413` → IC=-0.186 (n=1690)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7413
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=5070)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.182 (n=1688)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5072)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.266 (n=1722)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=5229)

- **FILTRO** `ibs_7min` > `0.2753` → IC=-0.180 (n=1737)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2753
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5214)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.185 (n=1699)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=5252)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.262 (n=1741)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=5223)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.232 (n=1709)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=5255)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=2372)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=7572)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.275 (n=1593)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=5132)

- **FILTRO** `ibs_7min` < `0.255` → IC=-0.223 (n=1681)

  - _Acción_: SKIP cuando `ibs_7min` < 0.255
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=5044)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.200 (n=1666)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=5059)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.206 (n=2356)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=7086)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1232)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=613)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

- **FILTRO** `libro_liquidez` < `7920.2009` → IC=-0.129 (n=346)

  - _Acción_: SKIP cuando `libro_liquidez` < 7920.2009
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=703)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=342)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.138 (n=150)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=294)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=396)

- **FILTRO** `libro_liquidez` < `3304.2295` → IC=-0.154 (n=163)

  - _Acción_: SKIP cuando `libro_liquidez` < 3304.2295
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=489)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.136 (n=907)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.141 (n=416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 14.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `442.2457` → IC=+0.148 (n=302)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 442.2457 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.130 (n=774)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 53.0 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.438` → IC=+0.171 (n=71)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.438 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.226 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.139 (n=225)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.04 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2596.4012` → IC=+0.212 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2596.4012 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.173 (n=96)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 12.0 (IC base=+0.139)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 8.0 (IC base=+0.107)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.188 (n=123)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.203 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.115)

- **PATRÓN** `total_vol_5m` < `385.7846` → IC=+0.211 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 385.7846 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 73.0 (IC base=+0.115)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.175 (n=164)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.145)

- **PATRÓN** `total_vol_5m` < `8043.774` → IC=+0.169 (n=164)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 8043.774 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3323.3564` → IC=+0.144 (n=147)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3323.3564 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 28.0 (IC base=+0.145)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4006` → IC=+0.144 (n=158)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4006 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.120 (n=156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 13.0 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3599.4239` → IC=+0.171 (n=80)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3599.4239 (IC base=+0.102)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.75` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.75
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=114)

- **FILTRO** `sigma_h` > `0.0044` → IC=-0.236 (n=339)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=168)

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
- **FILTRO** `sigma_h` > `0.0081` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0081
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `pct_vs_K` |x|> `8.662` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.662
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=34)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.200 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=24)

- **FILTRO** `T_h` < `87.1706` → IC=-0.167 (n=46)

  - _Acción_: SKIP cuando `T_h` < 87.1706
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=46)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `3.7555` → IC=-0.246 (n=116)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7555
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=350)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.306 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=307)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.316 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=307)

- **FILTRO** `T_h` > `57.7978` → IC=-0.314 (n=305)

  - _Acción_: SKIP cuando `T_h` > 57.7978
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=103)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `87.6765` → IC=-0.149 (n=109)

  - _Acción_: SKIP cuando `T_h` > 87.6765
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=54)

- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.381 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=123)

- **FILTRO** `sigma_h` > `0.0057` → IC=-0.316 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=76)

- **FILTRO** `T_h` > `143.1632` → IC=-0.308 (n=50)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=100)

- **FILTRO** `T_h` < `95.9199` → IC=-0.324 (n=49)

  - _Acción_: SKIP cuando `T_h` < 95.9199
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=101)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

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

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
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

- **PATRÓN** `edge` > `0.096` → IC=+0.454 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.421)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.434 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.421)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.449 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.421)

- **PATRÓN** `T_h` < `0.608` → IC=+0.432 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.608 (IC base=+0.421)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.450 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.421)

- **PATRÓN** `dist_50` > `0.3938` → IC=+0.483 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3938 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.475 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.421)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1078` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1078 (IC base=+0.422)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.409 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.422)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.455 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.422)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.422)

- **PATRÓN** `dist_50` > `0.4166` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4166 (IC base=+0.422)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.413 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.422)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.422)

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

- **PATRÓN** `edge` > `0.1155` → IC=+0.471 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1155 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.487 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0114 (IC base=+0.464)

- **PATRÓN** `T_h` > `0.8021` → IC=+0.465 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8021 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.4578` → IC=+0.491 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4578 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.469 (n=125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.464)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=239)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=332)

- **PATRÓN** `streak_estiramiento` < `0.5782` → IC=+0.149 (n=146)

  - _Acción_: Kelly boost +0.74€ cuando `streak_estiramiento` < 0.5782 (IC base=+0.032)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=24)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=50)

- **FILTRO** `volumen_racha` > `2314731.8` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_racha` > 2314731.8
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=53)

- **FILTRO** `streak_estiramiento` > `0.4315` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4315
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=43)

- **PATRÓN** `streak_estiramiento` < `0.4315` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.4315 (IC base=-0.014)

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
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=544)

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
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=766)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=915)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=906)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3386)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1760)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.210 (n=747)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.240 (n=747)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0507` → IC=+0.214 (n=747)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0507 (IC base=+0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2215` → IC=+0.214 (n=747)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2215 (IC base=+0.203)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1289` → IC=+0.233 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1289 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=2091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=2312)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `ibs_15` > `0.6192` → IC=+0.282 (n=2240)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6192 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.203 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.899` → IC=+0.283 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.899 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2938.6554` → IC=+0.208 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2938.6554 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.221 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.203)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=957)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.229 (n=463)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.283 (n=155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.217)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.256 (n=154)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.217)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.217)

- **PATRÓN** `ibs_15` > `0.7141` → IC=+0.279 (n=463)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7141 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.2515` → IC=+0.252 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2515 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.367` → IC=+0.270 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.367 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `16113.4131` → IC=+0.258 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16113.4131 (IC base=+0.217)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.756` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.756
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=570)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.192 (n=167)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.164 (n=221)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2368` → IC=+0.175 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.2368 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1226` → IC=+0.165 (n=189)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1226 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.160 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.149 (n=525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5797` → IC=+0.238 (n=501)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5797 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2752` → IC=+0.157 (n=462)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2752 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.546` → IC=+0.232 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.546 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3447.0107` → IC=+0.159 (n=447)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3447.0107 (IC base=+0.146)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.292 (n=94)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.1521` → IC=+0.216 (n=248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1521 (IC base=+0.190)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.201 (n=252)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=+0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3526` → IC=+0.238 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3526 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.191 (n=289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 17.0 (IC base=+0.190)

- **PATRÓN** `ibs_15` > `0.587` → IC=+0.278 (n=282)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.587 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.1286` → IC=+0.212 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1286 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.265` → IC=+0.361 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.265 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=299)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `3075.9018` → IC=+0.285 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3075.9018 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.217 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.190)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.005)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.249 (n=504)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.0815` → IC=+0.221 (n=249)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0815 (IC base=+0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.063` → IC=+0.213 (n=504)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.063 (IC base=+0.211)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0888` → IC=+0.266 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0888 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_15` > `0.5854` → IC=+0.295 (n=564)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5854 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1365` → IC=+0.216 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1365 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.5513` → IC=+0.211 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5513 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.363` → IC=+0.237 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.363 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.356` → IC=+0.215 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.356 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.210 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2924.6824` → IC=+0.284 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2924.6824 (IC base=+0.211)

- **PATRÓN** `ibs_15` < `0.1143` → IC=+0.150 (n=612)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1143 (IC base=+0.062)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.369 (n=342)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.358)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.366 (n=512)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.358)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.361 (n=343)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.358)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1503` → IC=+0.383 (n=341)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1503 (IC base=+0.358)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.390 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.358)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.401 (n=250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.358)

- **PATRÓN** `ibs_15` > `0.7856` → IC=+0.397 (n=512)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7856 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.384 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.259` → IC=+0.368 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.259 (IC base=+0.358)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.363 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.358)

- **PATRÓN** `libro_liquidez` > `3820.3005` → IC=+0.374 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3820.3005 (IC base=+0.358)

- **PATRÓN** `ballena_activa_n` < `444.0` → IC=+0.378 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 444.0 (IC base=+0.358)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.367 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.366 (n=251)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.375 (n=94)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.362)

- **PATRÓN** `drift_15min` |x|≤ `0.5105` → IC=+0.363 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5105 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1537` → IC=+0.378 (n=187)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1537 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.391 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.380 (n=282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8038` → IC=+0.394 (n=281)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8038 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3935` → IC=+0.395 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3935 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.859` → IC=+0.367 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.859 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` < `25.861` → IC=+0.361 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 25.861 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `16049.8465` → IC=+0.385 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.8465 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `500.0` → IC=+0.413 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 500.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.356 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.352)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.369 (n=105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.352)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.366 (n=155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.352)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.371 (n=208)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.352)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.379 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.352)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.412 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.352)

- **PATRÓN** `ibs_15` > `0.7485` → IC=+0.401 (n=231)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7485 (IC base=+0.352)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.375 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.352)

- **PATRÓN** `dist_vwap_pct` < `0.2936` → IC=+0.353 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2936 (IC base=+0.352)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.031` → IC=+0.368 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.031 (IC base=+0.352)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.354 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.352)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.358 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.352)

- **PATRÓN** `libro_liquidez` > `4204.0039` → IC=+0.373 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4204.0039 (IC base=+0.352)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.360 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.352)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.222 (n=831)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=2496)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.202 (n=1200)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2127)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1365` → IC=+0.241 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1365 (IC base=-0.063)

- **PATRÓN** `ibs_15` > `0.6389` → IC=+0.278 (n=807)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6389 (IC base=-0.063)

- **PATRÓN** `dist_vwap_pct` < `0.4165` → IC=+0.201 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4165 (IC base=-0.063)

- **PATRÓN** `delta_ratio_macro` |x|> `0.125` → IC=+0.248 (n=1674)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.125 (IC base=-0.022)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3157` → IC=+0.244 (n=2448)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3157 (IC base=-0.022)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.273 (n=2513)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.022)

- **PATRÓN** `dist_vwap_pct` > `0.8663` → IC=+0.293 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8663 (IC base=-0.022)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.241 (n=2178)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=-0.022)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.211 (n=486)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1461)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.230 (n=486)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1461)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.205 (n=1238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=709)

- **FILTRO** `sigma_ewma_delta_pct` > `23.756` → IC=-0.263 (n=276)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.756
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1671)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.174 (n=191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0027 (IC base=+0.089)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.302 (n=109)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.089)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.317 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.125 (n=390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 12.0 (IC base=+0.089)

- **PATRÓN** `ibs_15` > `0.7503` → IC=+0.331 (n=240)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7503 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.294 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.3585` → IC=+0.288 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3585 (IC base=+0.089)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0923` → IC=+0.176 (n=35)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.0923 (IC base=-0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.194)

- **PATRÓN** `ibs_15` < `0.5472` → IC=+0.311 (n=35)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.5472 (IC base=-0.194)

- **PATRÓN** `dist_vwap_pct` < `0.0651` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0651 (IC base=-0.194)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=-0.194)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=505)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.166 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.168 (n=350)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0038 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1119` → IC=+0.201 (n=262)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1119 (IC base=+0.157)

- **PATRÓN** `drift_15min` |x|≤ `0.4072` → IC=+0.162 (n=131)

  - _Acción_: Kelly boost +0.81€ cuando `drift_15min` |x|≤ 0.4072 (IC base=+0.157)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.157 (n=392)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.157)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2883` → IC=+0.215 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2883 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.180 (n=282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 11.0 (IC base=+0.157)

- **PATRÓN** `ibs_15` > `0.6526` → IC=+0.259 (n=392)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6526 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` < `0.2696` → IC=+0.171 (n=363)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2696 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.212 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=505)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `9553.1781` → IC=+0.172 (n=178)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 9553.1781 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.240 (n=930)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.4422` → IC=+0.234 (n=930)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4422 (IC base=+0.233)

- **PATRÓN** `drift_15min` |x|≤ `0.766` → IC=+0.243 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.766 (IC base=+0.233)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2084` → IC=+0.257 (n=422)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2084 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.234 (n=629)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.233)

- **PATRÓN** `ibs_15` < `0.3647` → IC=+0.265 (n=930)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3647 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.7436` → IC=+0.306 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7436 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.226` → IC=+0.264 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.226 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.472` → IC=+0.236 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.472 (IC base=+0.233)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.203 (n=584)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=196)

- **FILTRO** `drift_60min` |x|> `0.167` → IC=-0.242 (n=265)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.167
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=515)

- **FILTRO** `drift_15min` |x|> `0.8825` → IC=-0.270 (n=194)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8825
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=586)

- **FILTRO** `sigma_ewma_delta_pct` > `6.662` → IC=-0.175 (n=189)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.662
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=591)

- **FILTRO** `sigma_ewma_delta_pct` > `18.298` → IC=-0.139 (n=411)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.298
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=3300)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.159 (n=42)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.175)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.229 (n=57)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=-0.175)

- **PATRÓN** `dist_vwap_pct` > `0.3016` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.3016 (IC base=-0.175)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.175)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.175)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0786` → IC=+0.228 (n=366)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0786 (IC base=-0.041)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1879` → IC=+0.228 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1879 (IC base=-0.041)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.270 (n=411)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.6614` → IC=+0.226 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6614 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.1715` → IC=+0.230 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1715 (IC base=-0.041)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0194` → IC=-0.262 (n=468)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0194
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=470)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.253 (n=285)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=653)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.200)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.200)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1056` → IC=+0.269 (n=423)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1056 (IC base=-0.032)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1703` → IC=+0.302 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1703 (IC base=-0.032)

- **PATRÓN** `ibs_15` < `0.3273` → IC=+0.294 (n=634)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3273 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` > `0.827` → IC=+0.354 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.827 (IC base=-0.032)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.8434` → IC=-0.167 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8434
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.031)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.8434` → IC=-0.167 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8434
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.031)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.301 (n=551)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.291 (n=826)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0029 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.332 (n=277)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2411` → IC=+0.305 (n=275)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2411 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.221` → IC=+0.316 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.221 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.312 (n=864)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.326 (n=826)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.4357` → IC=+0.336 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4357 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.344 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `12848.0159` → IC=+0.306 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12848.0159 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.297 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.337 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2575` → IC=+0.309 (n=150)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2575 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4004` → IC=+0.306 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4004 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8305` → IC=+0.317 (n=451)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8305 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.347 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.358 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `16196.8854` → IC=+0.330 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16196.8854 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.302 (n=251)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.295)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.298 (n=375)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0518` → IC=+0.320 (n=126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0518 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2883` → IC=+0.317 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2883 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.336 (n=375)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2788` → IC=+0.311 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2788 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.564` → IC=+0.321 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.564 (IC base=+0.295)

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
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=131)

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

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.214 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

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
- **PATRÓN** `T_h` > `80.0063` → IC=+0.232 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 80.0063 (IC base=+0.215)

- **PATRÓN** `ratio` < `0.9753` → IC=+0.472 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9753 (IC base=+0.215)

- **PATRÓN** `T_h` > `145.7688` → IC=+0.394 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7688 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.012` → IC=+0.323 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.012 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `127.068` → IC=+0.243 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 127.068 (IC base=+0.196)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.469 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.196)

- **PATRÓN** `T_h` > `104.0063` → IC=+0.295 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 104.0063 (IC base=+0.290)

- **PATRÓN** `ratio` > `1.0479` → IC=+0.396 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0479 (IC base=+0.290)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.268 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.248)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.432 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.248)

- **PATRÓN** `T_h` > `111.9558` → IC=+0.344 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9558 (IC base=+0.323)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.356 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.323)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1131` → IC=+0.457 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1131 (IC base=+0.401)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6192 sube el IC de +0.203 a +0.282 en UPDOWN_GBM#15min (n=2240). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7141 sube el IC de +0.217 a +0.279 en UPDOWN_GBM#BTC#15min (n=463). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5797 sube el IC de +0.146 a +0.238 en UPDOWN_GBM#ETH#15min (n=501). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.587 sube el IC de +0.190 a +0.278 en UPDOWN_GBM#SOL#15min (n=282). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5854 sube el IC de +0.211 a +0.295 en UPDOWN_GBM#XRP#15min (n=564). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6389 sube el IC de -0.063 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=807). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.022 a +0.273 en UPDOWN_GBM_15M_TARDIO (n=2513). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7503 sube el IC de +0.089 a +0.331 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=240). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.5472 sube el IC de -0.194 a +0.311 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=35). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6526 sube el IC de +0.157 a +0.259 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=392). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3647 sube el IC de +0.233 a +0.265 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=930). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de -0.175 a +0.229 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=57). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.041 a +0.270 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=411). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.200 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3273 sube el IC de -0.032 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=634). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.291 a +0.326 en UPDOWN_GBM_IBS_ALTO (n=826). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8305 sube el IC de +0.288 a +0.317 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=451). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.295 a +0.336 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=375). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7856 sube el IC de +0.358 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=512). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8038 sube el IC de +0.362 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=281). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7485 sube el IC de +0.352 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=231). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1526 | +0.098 | +196.49€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1526 | +0.098 | +196.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1160 | +0.105 | +169.58€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1160 | +0.105 | +169.58€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 263 | +0.066 | +11.20€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 263 | +0.066 | +11.20€ | 6 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 144 | +0.007 | +24.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 144 | +0.007 | +24.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 120 | +0.008 | +20.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 120 | +0.008 | +20.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 33259 | -0.087 | -4395.93€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1701 | -0.016 | -215.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 31558 | -0.091 | -4180.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4283 | -0.119 | -737.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4283 | -0.119 | -737.61€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1701 | -0.016 | -215.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1701 | -0.016 | -215.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3897 | -0.112 | -873.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3897 | -0.112 | -873.60€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8576 | -0.001 | -770.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8576 | -0.001 | -770.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8349 | -0.106 | -582.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8349 | -0.106 | -582.66€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6453 | -0.160 | -1215.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6453 | -0.160 | -1215.79€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 25016 | -0.020 | +3739.12€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6473 | +0.002 | +1780.11€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 18543 | -0.028 | +1959.01€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 25016 | -0.020 | +3739.12€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6473 | +0.002 | +1780.11€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 18543 | -0.028 | +1959.01€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 113774 | +0.113 | -5158.62€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 16058 | +0.183 | -479.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 482 | -0.052 | -60.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 90138 | +0.102 | -4346.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7096 | +0.104 | -271.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 14969 | +0.102 | -1086.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 52 | -0.130 | +12.55€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 14902 | +0.103 | -1087.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 22600 | +0.130 | -358.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4834 | +0.198 | -122.79€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 14949 | +0.116 | -146.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2775 | +0.091 | -66.24€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 15016 | +0.093 | -1244.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 60 | -0.113 | -5.60€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 14941 | +0.094 | -1227.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 24171 | +0.124 | -425.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6468 | +0.176 | -101.26€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 15113 | +0.107 | -257.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2578 | +0.100 | -58.61€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 22030 | +0.115 | -1202.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4590 | +0.188 | -272.71€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 385 | -0.014 | -7.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 15312 | +0.094 | -775.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1743 | +0.130 | -147.13€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 14988 | +0.101 | -841.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 54 | -0.036 | +10.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 14921 | +0.102 | -851.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 18189 | +0.194 | -1139.69€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 18189 | +0.194 | -1139.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4229 | +0.174 | -393.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4229 | +0.174 | -393.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1925 | +0.203 | -25.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1925 | +0.203 | -25.49€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4169 | +0.181 | -340.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4169 | +0.181 | -340.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3674 | +0.242 | -124.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3674 | +0.242 | -124.26€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4113 | +0.188 | -270.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4113 | +0.188 | -270.26€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 850 | +0.430 | -24.53€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 850 | +0.430 | -24.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 337 | +0.435 | -5.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 337 | +0.435 | -5.57€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 321 | +0.435 | -4.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 321 | +0.435 | -4.82€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 180 | +0.407 | -11.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 180 | +0.407 | -11.70€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 63020 | +0.199 | -4708.72€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 63020 | +0.199 | -4708.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10846 | +0.183 | -1155.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10846 | +0.183 | -1155.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 10129 | +0.224 | -349.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 10129 | +0.224 | -349.92€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10845 | +0.176 | -1225.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10845 | +0.176 | -1225.14€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10191 | +0.220 | -379.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10191 | +0.220 | -379.24€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10437 | +0.203 | -691.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10437 | +0.203 | -691.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10572 | +0.193 | -908.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10572 | +0.193 | -908.14€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 23949 | +0.116 | +145.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 23949 | +0.116 | +145.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 11892 | +0.120 | +134.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 11892 | +0.120 | +134.13€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 12057 | +0.113 | +10.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 12057 | +0.113 | +10.89€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1722 | +0.289 | -22.59€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1722 | +0.289 | -22.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 777 | +0.281 | -15.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 777 | +0.281 | -15.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 830 | +0.287 | -10.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 830 | +0.287 | -10.70€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 115 | +0.346 | +3.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 115 | +0.346 | +3.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 775 | +0.438 | -0.94€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 775 | +0.438 | -0.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 372 | +0.436 | -3.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 372 | +0.436 | -3.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 357 | +0.442 | +1.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 357 | +0.442 | +1.53€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1317 | +0.072 | -56.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 475 | +0.060 | -36.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 842 | +0.078 | -20.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1032 | +0.077 | -27.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 190 | +0.073 | -7.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 842 | +0.078 | -20.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 219 | +0.034 | -31.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 219 | +0.034 | -31.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 45760 | +0.100 | -1211.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3716 | +0.090 | +38.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 42044 | +0.100 | -1250.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 25403 | +0.104 | -304.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3716 | +0.090 | +38.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 21687 | +0.106 | -342.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 9016 | +0.109 | -26.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 9016 | +0.109 | -26.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 11341 | +0.081 | -881.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 11341 | +0.081 | -881.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 866 | +0.206 | -101.64€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 866 | +0.206 | -101.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 866 | +0.206 | -101.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 866 | +0.206 | -101.64€ | 1 | 4 |
| ✅ GBM_LATE_15M | 32124 | +0.088 | +15945.58€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 32124 | +0.088 | +15945.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5403 | +0.203 | +4154.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5403 | +0.203 | +4154.54€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 4756 | +0.177 | +3416.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4756 | +0.177 | +3416.44€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 5709 | +0.199 | +4280.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5709 | +0.199 | +4280.95€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 4552 | +0.033 | +1157.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4552 | +0.033 | +1157.83€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4584 | -0.031 | +1011.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4584 | -0.031 | +1011.33€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 7120 | -0.035 | +1924.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7120 | -0.035 | +1924.49€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 34622 | +0.087 | +18445.32€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 34622 | +0.087 | +18445.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6675 | +0.012 | +3458.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6675 | +0.012 | +3458.10€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7181 | +0.014 | +1531.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7181 | +0.014 | +1531.51€ | 0 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4899 | +0.267 | +5019.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4899 | +0.267 | +5019.20€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5819 | +0.010 | +1296.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5819 | +0.010 | +1296.13€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5623 | +0.036 | +2269.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5623 | +0.036 | +2269.19€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4425 | +0.284 | +4871.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4425 | +0.284 | +4871.19€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 25754 | +0.173 | +19964.36€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 25754 | +0.173 | +19964.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3890 | +0.217 | +3259.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3890 | +0.217 | +3259.68€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4045 | +0.150 | +2944.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4045 | +0.150 | +2944.78€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4094 | +0.212 | +3330.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4094 | +0.212 | +3330.87€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4319 | +0.137 | +3180.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4319 | +0.137 | +3180.54€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4826 | +0.123 | +3523.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4826 | +0.123 | +3523.02€ | 0 | 28 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4580 | +0.210 | +3725.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4580 | +0.210 | +3725.47€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6997 | +0.137 | +3291.76€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6997 | +0.137 | +3291.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 339 | +0.142 | +189.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 339 | +0.142 | +189.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2031 | +0.144 | +1094.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2031 | +0.144 | +1094.14€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2117 | +0.152 | +1029.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2117 | +0.152 | +1029.13€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1600 | +0.106 | +566.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1600 | +0.106 | +566.90€ | 1 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 535 | +0.135 | +236.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 535 | +0.135 | +236.68€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 32349 | +0.179 | +24895.50€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 32349 | +0.179 | +24895.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5143 | +0.230 | +4561.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5143 | +0.230 | +4561.89€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4999 | +0.148 | +3262.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4999 | +0.148 | +3262.70€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5409 | +0.227 | +4682.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5409 | +0.227 | +4682.91€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5252 | +0.136 | +3669.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5252 | +0.136 | +3669.04€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5704 | +0.122 | +3941.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5704 | +0.122 | +3941.40€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5842 | +0.213 | +4777.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5842 | +0.213 | +4777.56€ | 0 | 23 |
| ✅ GBM_LATE_5M | 8741 | +0.174 | +5843.94€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 8741 | +0.174 | +5843.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2098 | +0.169 | +1523.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2098 | +0.169 | +1523.13€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2829 | +0.180 | +1867.24€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2829 | +0.180 | +1867.24€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 945 | +0.151 | +551.95€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 945 | +0.151 | +551.95€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1112 | +0.148 | +582.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1112 | +0.148 | +582.60€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2345 | +0.074 | +873.74€ | 0 | 13 |
| ✅ GBM_LATE_60M#60min | 2345 | +0.074 | +873.74€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 880 | +0.092 | +328.68€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 880 | +0.092 | +328.68€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 739 | +0.073 | +329.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 739 | +0.073 | +329.25€ | 1 | 11 |
| ✅ GBM_LATE_60M#SOL | 726 | +0.052 | +215.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 726 | +0.052 | +215.81€ | 2 | 14 |
| 🚫 GBM_LATE_60M_FADE | 454 | -0.239 | -10.92€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 454 | -0.239 | -10.92€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 167 | -0.216 | -5.32€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 167 | -0.216 | -5.32€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 158 | -0.231 | -0.89€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 158 | -0.231 | -0.89€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 129 | -0.271 | -4.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 129 | -0.271 | -4.71€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 997 | +0.087 | +258.53€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 997 | +0.087 | +258.53€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 369 | +0.080 | +79.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 369 | +0.080 | +79.70€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 334 | +0.051 | +37.84€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 334 | +0.051 | +37.84€ | 3 | 2 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 294 | +0.135 | +140.98€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 294 | +0.135 | +140.98€ | 1 | 14 |
| ✅ LATE_WINDOW_5MIN | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2688 | +0.102 | +704.32€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2688 | +0.102 | +704.32€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2688 | +0.102 | +704.32€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2688 | +0.102 | +704.32€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 416 | -0.072 | -32.64€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 416 | -0.072 | -32.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 112 | -0.035 | -2.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 112 | -0.035 | -2.26€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 155 | -0.029 | -5.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 155 | -0.029 | -5.55€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2734 | +0.023 | +74.64€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2734 | +0.023 | +74.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 136 | +0.029 | -1.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 136 | +0.029 | -1.24€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 398 | +0.035 | +34.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 398 | +0.035 | +34.72€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1045 | +0.031 | +30.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1045 | +0.031 | +30.61€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 627 | +0.015 | +2.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 627 | +0.015 | +2.43€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 327 | +0.020 | +14.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 327 | +0.020 | +14.25€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1347 | -0.044 | -28.02€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1347 | -0.044 | -28.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 384 | -0.042 | -13.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 384 | -0.042 | -13.31€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 446 | -0.025 | +0.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 446 | -0.025 | +0.16€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 517 | -0.063 | -14.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 517 | -0.063 | -14.86€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 4279 | -0.017 | +105.23€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2026 | -0.018 | +39.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2253 | -0.015 | +65.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 120 | -0.008 | +2.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 62 | +0.047 | +9.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 58 | -0.067 | -7.01€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1050 | +0.000 | +49.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 497 | -0.007 | +12.92€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 553 | +0.006 | +36.46€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 485 | -0.018 | +14.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 239 | -0.023 | +4.25€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 246 | -0.012 | +9.90€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 872 | -0.030 | -10.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 397 | -0.041 | -17.18€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 475 | -0.020 | +6.22€ | 4 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 844 | -0.020 | +19.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 410 | -0.022 | +12.23€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 434 | -0.018 | +7.07€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 908 | -0.020 | +30.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 421 | -0.013 | +17.77€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 487 | -0.026 | +12.95€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 37093 | -0.004 | +1761.41€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 37093 | -0.004 | +1761.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6604 | +0.024 | +875.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6604 | +0.024 | +875.08€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5563 | -0.032 | -84.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5563 | -0.032 | -84.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6694 | +0.019 | +661.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6694 | +0.019 | +661.62€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5349 | -0.053 | -162.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5349 | -0.053 | -162.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6251 | -0.009 | +201.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6251 | -0.009 | +201.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6632 | +0.012 | +270.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6632 | +0.012 | +270.25€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6135 | -0.059 | -146.73€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6135 | -0.059 | -146.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1501 | -0.079 | -34.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1501 | -0.079 | -34.90€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 704 | -0.126 | -34.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 704 | -0.126 | -34.31€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1813 | -0.076 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1813 | -0.076 | -32.29€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 855 | -0.016 | -25.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 855 | -0.016 | -25.54€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3348 | +0.004 | -2.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3348 | +0.004 | -2.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 190 | +0.016 | +0.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 190 | +0.016 | +0.21€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1317 | +0.006 | +6.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1317 | +0.006 | +6.68€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 93216 | -0.073 | +1736.80€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 93216 | -0.073 | +1736.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 16002 | -0.074 | +917.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 16002 | -0.074 | +917.21€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 14179 | -0.098 | -759.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 14179 | -0.098 | -759.34€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 16249 | -0.066 | +905.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 16249 | -0.066 | +905.59€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 13711 | -0.094 | -378.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 13711 | -0.094 | -378.19€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 16908 | -0.051 | +339.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 16908 | -0.051 | +339.80€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 16167 | -0.063 | +711.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 16167 | -0.063 | +711.73€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8017 | -0.030 | -143.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8017 | -0.030 | -143.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1907 | -0.041 | -15.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1907 | -0.041 | -15.32€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2238 | -0.024 | -28.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2238 | -0.024 | -28.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1097 | -0.048 | -21.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1097 | -0.048 | -21.52€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 771 | -0.023 | -25.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 771 | -0.023 | -25.39€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1343 | +0.116 | +500.07€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1207 | +0.123 | +487.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 283 | +0.139 | +143.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 283 | +0.139 | +143.26€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 227 | +0.107 | +63.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 227 | +0.107 | +63.54€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 245 | +0.115 | +98.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 245 | +0.115 | +98.12€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 218 | +0.145 | +113.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 218 | +0.145 | +113.48€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 234 | +0.102 | +69.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 234 | +0.102 | +69.07€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 873 | -0.017 | -19.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 873 | -0.017 | -19.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 170 | +0.006 | +8.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 170 | +0.006 | +8.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 127 | -0.012 | -1.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 127 | -0.012 | -1.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 236 | -0.038 | -18.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 236 | -0.038 | -18.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 192 | +0.010 | +3.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 192 | +0.010 | +3.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 148 | -0.047 | -12.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 148 | -0.047 | -12.36€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 725 | -0.093 | -67.24€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 330 | -0.148 | -79.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 259 | -0.190 | -74.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 71 | +0.007 | -4.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 257 | -0.048 | -1.17€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 186 | -0.053 | -4.01€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 71 | -0.034 | +2.83€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 138 | -0.043 | +13.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 110 | -0.062 | +7.10€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 28 | +0.033 | +5.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 555 | -0.119 | -71.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 170 | -0.006 | +3.87€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 874 | -0.201 | -49.54€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 363 | -0.193 | -31.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 313 | -0.195 | -31.77€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 50 | -0.173 | +0.17€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 295 | -0.217 | -31.22€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 254 | -0.227 | -37.06€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 41 | -0.151 | +5.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 216 | -0.188 | +13.28€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 198 | -0.185 | +9.63€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 18 | -0.180 | +3.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 765 | -0.204 | -59.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 109 | -0.176 | +9.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 356 | +0.402 | +290.97€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 91 | +0.371 | +75.92€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 91 | +0.371 | +75.92€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 225 | +0.460 | +216.29€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 225 | +0.460 | +216.29€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 356 | +0.402 | +290.97€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 609 | +0.025 | +14.66€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 609 | +0.025 | +14.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 44 | +0.043 | +0.25€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 44 | +0.043 | +0.25€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 64 | -0.015 | -2.20€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 64 | -0.015 | -2.20€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 206 | +0.038 | +14.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 206 | +0.038 | +14.31€ | 3 | 2 |
| ✅ STREAK_FADE_5M | 3064 | -0.022 | -123.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3064 | -0.022 | -123.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 905 | -0.021 | -32.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 905 | -0.021 | -32.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 579 | -0.027 | -25.73€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 579 | -0.027 | -25.73€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1424 | -0.018 | -51.31€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1424 | -0.018 | -51.31€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 85 | -0.052 | -8.44€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 85 | -0.052 | -8.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9589 | +0.019 | +105.73€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9589 | +0.019 | +105.73€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2628 | +0.021 | +27.28€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2628 | +0.021 | +27.28€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2237 | +0.028 | +50.74€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2237 | +0.028 | +50.74€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2861 | +0.010 | -0.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2861 | +0.010 | -0.81€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1863 | +0.021 | +28.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1863 | +0.021 | +28.53€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8633 | +0.012 | -49.93€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8633 | +0.012 | -49.93€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3405 | +0.015 | -12.70€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3405 | +0.015 | -12.70€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3434 | +0.012 | -22.86€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3434 | +0.012 | -22.86€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1794 | +0.007 | -14.37€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1794 | +0.007 | -14.37€ | 1 | 0 |
| ✅ UPDOWN_GBM | 54442 | +0.043 | +4093.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 13635 | +0.077 | +2859.75€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1811 | +0.006 | +10.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 35633 | +0.036 | +1186.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3168 | +0.005 | +40.81€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 5547 | +0.081 | +754.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1072 | +0.157 | +479.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4442 | +0.063 | +275.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 10501 | +0.049 | +832.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1751 | +0.089 | +403.34€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 486 | +0.012 | +5.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 6754 | +0.051 | +385.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1437 | +0.006 | +38.23€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 73 | -0.087 | +0.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 6450 | +0.053 | +515.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1048 | +0.137 | +378.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 5374 | +0.036 | +138.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 11962 | +0.033 | +643.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3331 | +0.053 | +445.51€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 479 | +0.007 | +8.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 7011 | +0.031 | +189.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1077 | +0.002 | -2.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 64 | -0.121 | +2.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 12123 | +0.022 | +435.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3235 | +0.031 | +281.12€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 469 | -0.001 | -0.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 7709 | +0.022 | +154.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 654 | +0.008 | +5.36€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 56 | -0.155 | -4.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 7857 | +0.050 | +913.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3198 | +0.097 | +872.31€ | 0 | 13 |
| ✅ UPDOWN_GBM#XRP#240min | 316 | +0.006 | -1.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4343 | +0.018 | +42.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 193 | -0.120 | -2.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 682 | +0.358 | +238.24€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 682 | +0.358 | +238.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 374 | +0.362 | +127.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 374 | +0.362 | +127.87€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 308 | +0.352 | +110.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 308 | +0.352 | +110.37€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 15269 | -0.031 | +3479.66€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 15269 | -0.031 | +3479.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1167 | -0.059 | +384.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1167 | -0.059 | +384.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2709 | -0.114 | +111.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2709 | -0.114 | +111.18€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 643 | +0.198 | +476.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 643 | +0.198 | +476.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1761 | +0.210 | +1112.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1761 | +0.210 | +1112.43€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4491 | -0.064 | +608.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4491 | -0.064 | +608.05€ | 5 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4498 | -0.067 | +787.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4498 | -0.067 | +787.04€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 173 | +0.026 | +6.12€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 173 | +0.026 | +6.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 173 | +0.026 | +6.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 173 | +0.026 | +6.12€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1101 | +0.291 | +903.91€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1101 | +0.291 | +903.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 601 | +0.288 | +460.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 601 | +0.288 | +460.37€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 500 | +0.295 | +443.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 500 | +0.295 | +443.54€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 757 | -0.114 | -85.13€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 757 | -0.114 | -85.13€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 224 | -0.088 | -18.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 224 | -0.088 | -18.30€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 73 | -0.167 | -9.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 73 | -0.167 | -9.78€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 81 | -0.187 | -7.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 81 | -0.187 | -7.00€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2863 | +0.307 | +1417.52€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1010 | +0.261 | +151.82€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1094 | +0.300 | +483.95€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 759 | +0.378 | +781.76€ | 0 | 1 |