# Hipótesis automáticas — 2026-10-03 12:44 UTC
_Generado por shadow_postmortem.py sobre 729130 resoluciones (PNL=+87694.21€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=573)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.222 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.131)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.218 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.131)

- **PATRÓN** `banda_hit_calibrado` > `0.8026` → IC=+0.258 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8026 (IC base=+0.131)

- **PATRÓN** `banda_z` > `9.249` → IC=+0.197 (n=206)

  - _Acción_: Kelly boost +0.99€ cuando `banda_z` > 9.249 (IC base=+0.131)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.723` → IC=+0.132 (n=553)

  - _Acción_: Kelly boost +0.66€ cuando `ballenas_wallet_edge_medio` > 0.723 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.132 (n=419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 11.0 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=651)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4869.7265` → IC=+0.149 (n=206)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4869.7265 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `8556.0995` → IC=+0.121 (n=233)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 8556.0995 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.229 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.202 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 68.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.7991` → IC=+0.266 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7991 (IC base=+0.140)

- **PATRÓN** `banda_z` > `9.958` → IC=+0.208 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.958 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=556)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.140)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.355` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.229 (n=105)

- **FILTRO** `banda_hit_calibrado` < `0.8019` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8019
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=94)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=113)

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

- **PATRÓN** `py_entrada` > `0.355` → IC=+0.229 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.355 (IC base=+0.120)

- **PATRÓN** `banda_hit_calibrado` > `0.8019` → IC=+0.250 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8019 (IC base=+0.120)

- **PATRÓN** `banda_z` > `6.043` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `banda_z` > 6.043 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.128 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.178 (n=113)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `1207.4096` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1207.4096 (IC base=+0.120)

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
- **FILTRO** `restante_s_al_confirmar` < `144.5` → IC=-0.219 (n=8128)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.5
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=24384)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `132.95` → IC=-0.268 (n=1052)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.95
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=3156)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `124.8` → IC=-0.311 (n=962)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.8
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2887)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.14` → IC=-0.218 (n=2019)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.14
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=6059)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.65` → IC=-0.327 (n=1577)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.65
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=4733)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.212 (n=15784)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=3808)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `5446.5896` → IC=+0.171 (n=2468)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5446.5896 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=13727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=16845)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=12900)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=6247)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7654.6247` → IC=+0.168 (n=2389)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7654.6247 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.207 (n=1782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1824)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=2296)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `16049.8465` → IC=+0.221 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.8465 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.202 (n=1643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1830)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2345)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `15980.1695` → IC=+0.210 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15980.1695 (IC base=+0.196)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=391)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.129 (n=246)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 4624.034 (IC base=+0.091)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.095)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=914)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.148 (n=231)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.095)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.354 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.231 (n=1474)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.364 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.226 (n=1707)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.221)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=814)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=703)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.259 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=893)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `1317.494` → IC=+0.146 (n=780)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1317.494 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.406 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=1205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=647)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=799)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.226 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=13799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=11761)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.226 (n=5881)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=3264)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3096)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.181 (n=3134)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.174)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.245 (n=614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.235 (n=1289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.235)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.340 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.235)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=3218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=3072)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=2568)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=2830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.330 (n=955)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=3136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=2022)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.193 (n=2376)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.196 (n=1138)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `11651.323` → IC=+0.457 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11651.323 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.448 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.456 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `14760.7483` → IC=+0.446 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14760.7483 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.445 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.465 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `3371.5411` → IC=+0.449 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3371.5411 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.422 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.411)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.409 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.411)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.417 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.411)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.413 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.411)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `4.0` → IC=-0.300 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=41053)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=18011)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.183 (n=7060)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.184 (n=5706)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.195 (n=7766)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=3650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.266 (n=4184)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=7480)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.174 (n=5728)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 12.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=7491)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=3692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.268 (n=2502)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=2690)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=2931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.242 (n=3132)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=6294)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=6045)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.49` → IC=+0.137 (n=5826)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.49 (IC base=+0.115)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=3165)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.141 (n=3010)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=3847)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.2` → IC=+0.143 (n=2901)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.2 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.182 (n=3129)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.38 (IC base=+0.112)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.128 (n=3321)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` > 4.96 (IC base=+0.112)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.133 (n=2946)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.112)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=1343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.288 (n=1269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `4187.1233` → IC=+0.304 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4187.1233 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.291 (n=595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.331 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `3795.9272` → IC=+0.292 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3795.9272 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=639)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.390 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1716.9381` → IC=+0.309 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1716.9381 (IC base=+0.287)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.439 (n=503)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.439 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.440 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.439 (n=276)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.456 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.440 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.925` → IC=+0.456 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.925 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `1965.9066` → IC=+0.458 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1965.9066 (IC base=+0.442)

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
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=60)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1366.4094` → IC=+0.287 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1366.4094 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.735` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=60)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1366.4094` → IC=+0.287 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1366.4094 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4919` → IC=+0.130 (n=9832)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4919 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.243 (n=3280)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2214` → IC=+0.255 (n=2207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2214 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.401` → IC=+0.192 (n=2573)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.401 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.250 (n=2748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6157` → IC=+0.252 (n=2748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6157 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.3011` → IC=+0.228 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3011 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `1.4606` → IC=+0.211 (n=6864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4606 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5683` → IC=+0.137 (n=11938)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5683 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.5968` → IC=+0.202 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5968 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.1525` → IC=+0.176 (n=3968)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1525 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `1.1942` → IC=+0.177 (n=4327)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.1942 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` > `0.863` → IC=+0.176 (n=2884)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.863 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.1663` → IC=+0.220 (n=2080)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1663 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.2719` → IC=+0.196 (n=6518)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2719 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.4458` → IC=+0.199 (n=7408)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4458 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `120.0` → IC=+0.212 (n=7209)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 120.0 (IC base=+0.069)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.214 (n=736)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.188 (n=729)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0081 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3519` → IC=+0.183 (n=2188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3519 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.192 (n=1056)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.184 (n=1470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 11.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.278 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.713` → IC=+0.296 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.713 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.220 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.4332` → IC=+0.180 (n=2064)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4332 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=2243)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2038.742` → IC=+0.185 (n=729)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2038.742 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.235 (n=1160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.243 (n=1553)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.273 (n=579)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.251 (n=1188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.062` → IC=+0.286 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.062 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.484` → IC=+0.244 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.484 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.39` → IC=+0.241 (n=1811)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.39 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.232 (n=1442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.262 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.5704` → IC=+0.244 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5704 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=1903)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1587.18` → IC=+0.246 (n=1734)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1587.18 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.238 (n=766)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.3568` → IC=+0.227 (n=1735)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3568 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.231 (n=1737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.979` → IC=+0.259 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.979 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.3532` → IC=+0.219 (n=1612)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3532 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.762` → IC=+0.254 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.762 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `1.2505` → IC=+0.220 (n=1735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2505 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.6912` → IC=+0.220 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6912 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.238 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4014` → IC=+0.217 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4014 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.3925` → IC=+0.239 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3925 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `11121.9309` → IC=+0.220 (n=1734)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11121.9309 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.168 (n=1169)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.163 (n=586)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7206` → IC=+0.174 (n=1751)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.7206 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1289` → IC=+0.154 (n=1579)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1289 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.292` → IC=+0.138 (n=280)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 11.292 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.3` → IC=+0.144 (n=1612)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.3 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.147 (n=1751)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2035 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.8505` → IC=+0.138 (n=1167)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.8505 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.172 (n=468)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.442` → IC=+0.149 (n=1640)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.442 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7721` → IC=+0.147 (n=1093)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7721 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `14180.1472` → IC=+0.142 (n=1167)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 14180.1472 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.172 (n=689)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 231.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.199 (n=2208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=2327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=1485)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.319` → IC=+0.260 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.319 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.193 (n=1935)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.3478` → IC=+0.201 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3478 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.7627` → IC=+0.199 (n=1893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7627 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=2634)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `1944.22` → IC=+0.192 (n=1001)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 1944.22 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.219 (n=1711)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.1319` → IC=+0.218 (n=648)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1319 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=915)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.231 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.686` → IC=+0.237 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.686 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3464` → IC=+0.252 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3464 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.7245` → IC=+0.216 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7245 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.7414` → IC=+0.221 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7414 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `1934.3468` → IC=+0.213 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1934.3468 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.209 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.209)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=120)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=2638)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.153 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0037 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9556` → IC=+0.219 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9556 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1966` → IC=+0.329 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1966 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.896` → IC=+0.171 (n=871)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 4.896 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.332 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8546 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.211` → IC=+0.319 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.211 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.3004` → IC=+0.345 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3004 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.349 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `1.8416` → IC=+0.326 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8416 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.329 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.1023` → IC=+0.156 (n=690)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1023 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.3307` → IC=+0.198 (n=319)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3307 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.844` → IC=+0.150 (n=715)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.844 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.1643` → IC=+0.143 (n=357)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1643 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.194 (n=142)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.5154` → IC=+0.163 (n=910)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.5154 (IC base=+0.022)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=401)

- **FILTRO** `ibs_20min` < `0.3111` → IC=-0.183 (n=118)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3111
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=354)

- **FILTRO** `ibs_20min` > `0.2391` → IC=-0.125 (n=2658)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2391
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=1313)

- **FILTRO** `sigma_ewma_delta_pct` > `8.769` → IC=-0.214 (n=418)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.769
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=3553)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.205 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `1.695` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.695 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.332` → IC=+0.131 (n=166)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 2.332 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `1.0815` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0815 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.289 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.280 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.2391` → IC=+0.131 (n=1313)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2391 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.7032` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7032 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.6948` → IC=+0.271 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6948 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.308 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.3699` → IC=+0.288 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3699 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6494` → IC=-0.180 (n=691)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6494
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2088)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.206 (n=657)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2122)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.210 (n=1014)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=3106)

- **PATRÓN** `dist_vwap_pct` > `0.8005` → IC=+0.317 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8005 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2116` → IC=+0.315 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2116 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.6304` → IC=+0.310 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6304 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.297 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.303 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.4513` → IC=+0.299 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4513 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.8321` → IC=+0.306 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8321 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.5572` → IC=+0.279 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5572 (IC base=-0.016)

- **PATRÓN** `volumen_regimen` < `0.7234` → IC=+0.253 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7234 (IC base=-0.016)

- **PATRÓN** `volumen_regimen` > `1.0773` → IC=+0.271 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0773 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.268 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` < `2.1373` → IC=+0.260 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1373 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` > `1.4191` → IC=+0.252 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4191 (IC base=-0.016)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.200 (n=4255)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4716` → IC=+0.188 (n=11397)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4716 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `1.0112` → IC=+0.289 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0112 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.672` → IC=+0.158 (n=5833)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.672 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.1783` → IC=+0.245 (n=4649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1783 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.6916` → IC=+0.254 (n=4153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6916 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.266 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.6341` → IC=+0.255 (n=2500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6341 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.275 (n=7033)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.167 (n=4123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0091 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5457` → IC=+0.157 (n=10879)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5457 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7031` → IC=+0.251 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7031 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2443` → IC=+0.249 (n=3579)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2443 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7061` → IC=+0.248 (n=1640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7061 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1967` → IC=+0.261 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1967 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.304 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5872` → IC=+0.276 (n=2256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5872 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.279 (n=5008)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2587` → IC=-0.160 (n=884)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2587
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2655)

- **FILTRO** `ibs_20min` > `0.7575` → IC=-0.169 (n=723)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7575
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2172)

- **FILTRO** `sigma_ewma_delta_pct` > `4.561` → IC=-0.175 (n=653)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.561
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2242)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.278 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.21` → IC=+0.201 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.21 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2262` → IC=+0.277 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2262 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.202 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.1788` → IC=+0.237 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1788 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.233 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.0998` → IC=+0.434 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0998 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.5483` → IC=+0.446 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5483 (IC base=-0.025)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.436 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=-0.025)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8651` → IC=+0.164 (n=855)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8651 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.3011` → IC=+0.193 (n=461)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.3011 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.6746` → IC=+0.176 (n=1072)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6746 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.223 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.199 (n=393)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.4118` → IC=+0.186 (n=393)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4118 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.222 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 231.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1504` → IC=+0.225 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1504 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.6093` → IC=+0.227 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6093 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0722` → IC=+0.223 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0722 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2677` → IC=+0.278 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2677 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.4375` → IC=+0.226 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4375 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1657` → IC=+0.232 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1657 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.276 (n=1745)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.254 (n=1961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.251 (n=1746)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.173` → IC=+0.284 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.173 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.099` → IC=+0.265 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.099 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.1777` → IC=+0.265 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1777 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2304)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `2007.4196` → IC=+0.272 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2007.4196 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.301 (n=1615)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.184` → IC=+0.299 (n=711)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.184 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.318 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.3563` → IC=+0.292 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3563 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `0.0991` → IC=+0.287 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0991 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.685` → IC=+0.292 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.685 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.1191` → IC=+0.292 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1191 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.5716` → IC=+0.299 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5716 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.6522` → IC=+0.294 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6522 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1927.08` → IC=+0.305 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1927.08 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.288 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.286)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7715` → IC=-0.186 (n=737)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7715
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=2212)

- **PATRÓN** `ibs_20min` > `0.9046` → IC=+0.177 (n=661)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9046 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.4017` → IC=+0.230 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4017 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` < `1.009` → IC=+0.248 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.009 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.0816` → IC=+0.254 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0816 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4046` → IC=+0.267 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4046 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.258 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.1374` → IC=+0.231 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1374 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` < `1.1677` → IC=+0.217 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1677 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.8268` → IC=+0.268 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8268 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.472` → IC=+0.236 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.472 (IC base=-0.006)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.254 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7586` → IC=-0.184 (n=1349)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7586
  - _Potencial_: sin este filtro IC_bueno=+0.284 (n=1352)

- **FILTRO** `ibs_20min` > `0.675` → IC=-0.240 (n=678)

  - _Acción_: SKIP cuando `ibs_20min` > 0.675
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=2035)

- **FILTRO** `sigma_ewma_delta_pct` > `4.792` → IC=-0.200 (n=578)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.792
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=2135)

- **PATRÓN** `ibs_20min` > `0.7586` → IC=+0.284 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7586 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `1.0764` → IC=+0.332 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0764 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.69` → IC=+0.171 (n=429)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.69 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8573` → IC=+0.308 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8573 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.302 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.0982` → IC=+0.299 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0982 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.294 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.4185` → IC=+0.324 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4185 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.323 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.132 (n=1794)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5714 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.2039` → IC=+0.242 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2039 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.267 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.1879` → IC=+0.224 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1879 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.0947` → IC=+0.226 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0947 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.0684` → IC=+0.248 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0684 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.4082` → IC=+0.247 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4082 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.257 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.020)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.327 (n=1415)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.283)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.303 (n=744)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` > `0.6454` → IC=+0.315 (n=1583)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6454 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2152` → IC=+0.316 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2152 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.76` → IC=+0.309 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.76 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` > `0.6276` → IC=+0.296 (n=1583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6276 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.328 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `1.4333` → IC=+0.294 (n=1512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4333 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2474.544` → IC=+0.295 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2474.544 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.321 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.315 (n=1116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.1961` → IC=+0.288 (n=737)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1961 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.288 (n=1593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.3774` → IC=+0.309 (n=1675)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3774 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.3173` → IC=+0.296 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3173 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` < `0.2319` → IC=+0.283 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2319 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.54` → IC=+0.298 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.54 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` < `0.642` → IC=+0.284 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.642 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.316 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.340 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.292 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.1363` → IC=+0.280 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1363 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2430.526` → IC=+0.288 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2430.526 (IC base=+0.283)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.182 (n=3200)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0048 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.206 (n=3203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.3623` → IC=+0.182 (n=8448)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3623 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=10008)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.225 (n=9599)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1738` → IC=+0.196 (n=4128)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1738 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.405` → IC=+0.255 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.405 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.166 (n=6391)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2068 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6287` → IC=+0.162 (n=6391)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6287 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.199 (n=1421)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.5586` → IC=+0.171 (n=4068)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5586 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.5988` → IC=+0.181 (n=3082)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.5988 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `1976.62` → IC=+0.175 (n=8575)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1976.62 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.188 (n=8523)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 107.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.186 (n=6139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.0816` → IC=+0.216 (n=3067)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0816 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=3504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.4877` → IC=+0.229 (n=9194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4877 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.1729` → IC=+0.166 (n=6424)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1729 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.319` → IC=+0.196 (n=1544)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.319 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1777` → IC=+0.160 (n=6602)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1777 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.215 (n=1334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.5538` → IC=+0.172 (n=3741)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5538 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5977` → IC=+0.172 (n=2833)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5977 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.180 (n=8161)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 108.0 (IC base=+0.172)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.236 (n=539)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.207 (n=540)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.3413` → IC=+0.218 (n=1606)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3413 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=1693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=1083)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.9126` → IC=+0.287 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9126 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.249` → IC=+0.331 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.249 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.245 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `1.4317` → IC=+0.196 (n=1500)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4317 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1655)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `2039.0` → IC=+0.199 (n=536)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2039.0 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.251 (n=1075)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.249 (n=1096)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.0705` → IC=+0.309 (n=407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0705 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.250 (n=1090)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.3503` → IC=+0.263 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3503 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.213` → IC=+0.249 (n=1321)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.213 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.263 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4163` → IC=+0.267 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4163 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1585.6447` → IC=+0.255 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1585.6447 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.232 (n=486)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.0712` → IC=+0.194 (n=482)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0712 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.177 (n=1444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.3884` → IC=+0.222 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3884 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.2011` → IC=+0.205 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2011 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.523` → IC=+0.227 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.523 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.688` → IC=+0.170 (n=635)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.688 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.201 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4117` → IC=+0.177 (n=469)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4117 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.4806` → IC=+0.156 (n=469)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.4806 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `11952.667` → IC=+0.157 (n=1290)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 11952.667 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.165 (n=601)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 235.0 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.162 (n=1526)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.2319` → IC=+0.174 (n=1343)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2319 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=722)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.591` → IC=+0.195 (n=1526)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.591 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1346` → IC=+0.168 (n=1512)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1346 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.882` → IC=+0.196 (n=301)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.882 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2126` → IC=+0.160 (n=1526)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2126 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0696` → IC=+0.148 (n=682)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0696 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4573` → IC=+0.150 (n=1414)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4573 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.752` → IC=+0.141 (n=943)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.752 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.173 (n=445)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 208.0 (IC base=+0.141)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.226 (n=727)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.2513` → IC=+0.217 (n=1070)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2513 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.464` → IC=+0.281 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.464 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.1277` → IC=+0.208 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1277 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.7137` → IC=+0.217 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7137 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1903)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2007.5584` → IC=+0.211 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2007.5584 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.237 (n=1210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.1015` → IC=+0.261 (n=459)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1015 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.273 (n=470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.3509` → IC=+0.246 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3509 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.651` → IC=+0.252 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.651 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3508` → IC=+0.259 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3508 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.7398` → IC=+0.236 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7398 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.743` → IC=+0.227 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.743 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1930.3184` → IC=+0.225 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1930.3184 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.212 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.221)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.185 (n=1360)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0065 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.4235` → IC=+0.166 (n=1546)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4235 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=1611)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.34` → IC=+0.204 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.34 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1491` → IC=+0.186 (n=1007)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1491 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.946` → IC=+0.227 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.946 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.163 (n=1032)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.856 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1013` → IC=+0.181 (n=646)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1013 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4269` → IC=+0.167 (n=505)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4269 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.164 (n=504)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5139.067` → IC=+0.192 (n=1030)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 5139.067 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.155 (n=1484)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 154.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.154 (n=1614)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3873` → IC=+0.145 (n=1614)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3873 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6652` → IC=+0.178 (n=1614)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6652 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.1542` → IC=+0.144 (n=1582)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1542 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.868` → IC=+0.166 (n=560)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.868 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.8555` → IC=+0.152 (n=1076)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8555 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.180 (n=239)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8021` → IC=+0.138 (n=993)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8021 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.4191` → IC=+0.126 (n=1488)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4191 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `4253.4042` → IC=+0.157 (n=1076)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4253.4042 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.124 (n=1260)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 127.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.164 (n=796)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0101 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.585` → IC=+0.125 (n=1752)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.585 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.210 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0815` → IC=+0.216 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0815 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.866` → IC=+0.261 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.866 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2106` → IC=+0.136 (n=1752)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2106 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6466` → IC=+0.131 (n=1752)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6466 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1613` → IC=+0.132 (n=1763)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1613 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.126 (n=725)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.5369` → IC=+0.145 (n=745)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.5369 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=1833)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2897.5388` → IC=+0.200 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2897.5388 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.144 (n=1390)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 47.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.160 (n=784)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0062 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.105` → IC=+0.173 (n=591)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.105 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1790)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5773` → IC=+0.216 (n=1772)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5773 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.1996` → IC=+0.148 (n=1638)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1996 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.335` → IC=+0.133 (n=540)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 5.335 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6381` → IC=+0.151 (n=592)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6381 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.226` → IC=+0.161 (n=308)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.226 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.446` → IC=+0.142 (n=540)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.446 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.4154` → IC=+0.126 (n=540)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4154 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2744.0462` → IC=+0.181 (n=804)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2744.0462 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.126 (n=1570)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 52.0 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.230 (n=1475)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2933` → IC=+0.213 (n=1102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2933 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.245 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.209` → IC=+0.214 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.209 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.602` → IC=+0.248 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.602 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.1926` → IC=+0.211 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1926 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.217 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2779` → IC=+0.270 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2779 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.4665` → IC=+0.212 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4665 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.8022` → IC=+0.217 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8022 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.211 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2466.2754` → IC=+0.208 (n=1475)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2466.2754 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.225 (n=744)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0175` → IC=+0.216 (n=1127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0175 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.235 (n=564)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.4305` → IC=+0.243 (n=1690)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4305 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `1.2084` → IC=+0.226 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2084 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.374` → IC=+0.252 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.374 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.1727` → IC=+0.212 (n=1690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1727 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.703` → IC=+0.221 (n=1510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.703 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.275 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `2.1914` → IC=+0.205 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1914 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4348` → IC=+0.211 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4348 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2404.3655` → IC=+0.218 (n=1510)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2404.3655 (IC base=+0.212)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.192 (n=1113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0042 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.171 (n=843)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0085 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3469` → IC=+0.178 (n=2225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3469 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=1249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.4951` → IC=+0.204 (n=2258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4951 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.8094` → IC=+0.188 (n=402)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.8094 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.737` → IC=+0.192 (n=1107)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.737 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.871` → IC=+0.188 (n=1500)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.871 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.177 (n=751)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.2084 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1627` → IC=+0.178 (n=672)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1627 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4373` → IC=+0.183 (n=818)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4373 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.8202` → IC=+0.174 (n=1634)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8202 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=2870)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2687.8872` → IC=+0.170 (n=2258)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2687.8872 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.187 (n=2307)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 142.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.137 (n=1733)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0056 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.0699` → IC=+0.191 (n=866)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0699 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.0749` → IC=+0.124 (n=984)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0749 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `1.4404` → IC=+0.144 (n=840)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4404 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2751.2995` → IC=+0.124 (n=2320)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2751.2995 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.126 (n=1098)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 28.0 (IC base=+0.107)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.181 (n=296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0029 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.3342` → IC=+0.163 (n=671)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3342 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.179 (n=622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.6393` → IC=+0.206 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6393 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.299` → IC=+0.161 (n=231)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.299 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.181` → IC=+0.162 (n=294)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.181 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.952` → IC=+0.142 (n=702)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.952 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.892` → IC=+0.171 (n=448)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.892 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.1557` → IC=+0.145 (n=699)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.1557 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.143 (n=267)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.211` → IC=+0.152 (n=575)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.211 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.5112` → IC=+0.147 (n=584)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5112 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `10893.2461` → IC=+0.151 (n=671)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 10893.2461 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.193 (n=285)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 152.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.208 (n=272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3463` → IC=+0.160 (n=813)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3463 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.147 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.144 (n=823)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6119` → IC=+0.179 (n=715)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6119 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1832` → IC=+0.155 (n=804)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1832 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.074` → IC=+0.146 (n=743)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.074 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2204` → IC=+0.144 (n=813)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2204 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.154 (n=726)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.693 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.200 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1142` → IC=+0.156 (n=707)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1142 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4081` → IC=+0.147 (n=803)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4081 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `12071.9003` → IC=+0.143 (n=726)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 12071.9003 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `294.0` → IC=+0.154 (n=688)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 294.0 (IC base=+0.140)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.252 (n=530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.4057` → IC=+0.220 (n=794)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4057 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.3605` → IC=+0.242 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3605 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.1422` → IC=+0.214 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1422 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.2147` → IC=+0.210 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2147 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.334` → IC=+0.229 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.334 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.8407` → IC=+0.216 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8407 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `1.1816` → IC=+0.230 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1816 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.1552` → IC=+0.242 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1552 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.4188` → IC=+0.239 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4188 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.4384` → IC=+0.245 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4384 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.123 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 11.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.0876` → IC=+0.149 (n=249)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.0876 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6868` → IC=+0.138 (n=327)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6868 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `7918.7339` → IC=+0.134 (n=495)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 7918.7339 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.169 (n=533)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0059 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.5425` → IC=+0.154 (n=596)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.5425 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.188 (n=546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.9831` → IC=+0.241 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9831 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.339` → IC=+0.206 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.339 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.0671` → IC=+0.174 (n=525)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.0671 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.6526` → IC=+0.161 (n=596)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6526 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.17` → IC=+0.169 (n=164)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.17 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4797` → IC=+0.154 (n=574)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4797 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.1908` → IC=+0.169 (n=261)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.1908 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.159 (n=631)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `3082.2108` → IC=+0.192 (n=199)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3082.2108 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.4722` → IC=+0.152 (n=507)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.4722 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` < `1.5684` → IC=+0.138 (n=241)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5684 (IC base=+0.062)

- **PATRÓN** `libro_liquidez` > `2427.8353` → IC=+0.130 (n=384)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2427.8353 (IC base=+0.062)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.131 (n=350)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 22.0 (IC base=+0.062)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0239` → IC=+0.167 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0239 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.186 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.007 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2478` → IC=+0.174 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2478 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.192 (n=102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 8.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.190 (n=169)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.56 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.2468` → IC=+0.173 (n=105)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.2468 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `1.1352` → IC=+0.162 (n=211)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 1.1352 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.738` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 7.738 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.385` → IC=+0.179 (n=163)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 3.385 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.175 (n=189)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6182 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.2537` → IC=+0.181 (n=186)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.2537 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=194)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2504.6528` → IC=+0.172 (n=126)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2504.6528 (IC base=+0.153)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.177 (n=4155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0047 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.209 (n=4138)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=12980)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.9919` → IC=+0.309 (n=4140)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9919 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.9235` → IC=+0.202 (n=1694)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9235 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.367` → IC=+0.250 (n=3071)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.367 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `0.8796` → IC=+0.171 (n=5552)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8796 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.200 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.5776` → IC=+0.197 (n=3999)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5776 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `1806.8` → IC=+0.179 (n=12413)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1806.8 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.202 (n=9712)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.191 (n=7453)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1503` → IC=+0.192 (n=4917)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1503 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=4187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.4528` → IC=+0.246 (n=9832)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4528 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.248` → IC=+0.163 (n=6980)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.248 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.051` → IC=+0.203 (n=1569)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.051 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.732` → IC=+0.183 (n=10788)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.732 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.162 (n=3340)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7044 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.244 (n=1473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.8549` → IC=+0.188 (n=6936)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8549 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.204 (n=6716)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.240 (n=693)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.230 (n=686)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.3586` → IC=+0.208 (n=2056)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3586 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=989)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=1390)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.330 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.358 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.260 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.2327` → IC=+0.218 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2327 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2092)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2038.92` → IC=+0.217 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2038.92 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.230 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.263 (n=1120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.264 (n=1684)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1255` → IC=+0.283 (n=741)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1255 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=1514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3594` → IC=+0.285 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3594 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.508` → IC=+0.260 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.508 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.444` → IC=+0.259 (n=1762)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.444 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.291 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.5472` → IC=+0.258 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5472 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.6156` → IC=+0.275 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6156 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1585.6447` → IC=+0.270 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1585.6447 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.204 (n=671)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.161 (n=878)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2087)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.2876` → IC=+0.203 (n=1993)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2876 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1264` → IC=+0.182 (n=1124)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1264 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.74` → IC=+0.178 (n=436)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.74 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.182` → IC=+0.150 (n=1820)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.182 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.7005` → IC=+0.168 (n=877)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.7005 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2686` → IC=+0.196 (n=284)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2686 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.1285` → IC=+0.158 (n=1704)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1285 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.5091` → IC=+0.151 (n=1730)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.5091 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `11444.8195` → IC=+0.153 (n=1781)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 11444.8195 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `278.0` → IC=+0.172 (n=832)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 278.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=1677)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.331` → IC=+0.159 (n=1675)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.331 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.2937` → IC=+0.238 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2937 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.164 (n=1529)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1327 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.5` → IC=+0.152 (n=280)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 11.5 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.303` → IC=+0.147 (n=1524)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.303 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.1895` → IC=+0.160 (n=1675)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1895 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1514` → IC=+0.199 (n=446)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1514 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4127` → IC=+0.155 (n=1576)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4127 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7588` → IC=+0.160 (n=1050)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7588 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `348.0` → IC=+0.147 (n=994)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 348.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.257 (n=680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=1829)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.371` → IC=+0.302 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.371 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.2057` → IC=+0.223 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2057 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.7675` → IC=+0.231 (n=1744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7675 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1943.98` → IC=+0.229 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1943.98 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.240 (n=1675)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.233 (n=1702)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.1832` → IC=+0.242 (n=838)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1832 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.259 (n=720)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.233 (n=903)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0148` → IC=+0.301 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0148 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.902` → IC=+0.278 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.902 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3408` → IC=+0.293 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3408 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7297` → IC=+0.236 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7297 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.1492` → IC=+0.238 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1492 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1928.6248` → IC=+0.244 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1928.6248 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.233 (n=1704)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.200 (n=709)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4358` → IC=+0.153 (n=2123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4358 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2719` → IC=+0.189 (n=2123)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2719 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3629` → IC=+0.161 (n=818)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3629 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.523` → IC=+0.168 (n=344)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.523 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.162 (n=1416)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8725 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.196 (n=284)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5199` → IC=+0.159 (n=909)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5199 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1631` → IC=+0.155 (n=936)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1631 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7528.5122` → IC=+0.231 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7528.5122 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.177 (n=666)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 71.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.166 (n=1142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0052 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4454` → IC=+0.140 (n=1709)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4454 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.5985` → IC=+0.193 (n=1505)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5985 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1544` → IC=+0.130 (n=1499)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1544 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.292` → IC=+0.164 (n=257)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.292 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8727` → IC=+0.137 (n=1140)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8727 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.216 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.140 (n=1636)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `9330.5523` → IC=+0.201 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9330.5523 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.128 (n=1640)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 169.0 (IC base=+0.127)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.143 (n=1417)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0081 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.5742` → IC=+0.128 (n=2125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.5742 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.202 (n=2125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4615 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0673` → IC=+0.211 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0673 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.546` → IC=+0.244 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.546 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.8902` → IC=+0.148 (n=1417)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8902 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1604` → IC=+0.128 (n=2190)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1604 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8314` → IC=+0.125 (n=1379)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.8314 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.4546` → IC=+0.127 (n=2067)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4546 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2162)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2549.1679` → IC=+0.234 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2549.1679 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.145 (n=1299)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 42.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.182 (n=677)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0058 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1356` → IC=+0.159 (n=675)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1356 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=2089)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5065` → IC=+0.233 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5065 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.138 (n=1687)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.468` → IC=+0.128 (n=1951)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.468 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.645` → IC=+0.163 (n=675)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.645 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2195` → IC=+0.189 (n=319)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2195 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `2.1459` → IC=+0.133 (n=1635)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.1459 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2798.604` → IC=+0.191 (n=675)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2798.604 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.133 (n=1613)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 50.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.230 (n=2087)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.216 (n=1512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.263 (n=1872)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.2137` → IC=+0.233 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2137 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.264` → IC=+0.277 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.264 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.0569` → IC=+0.216 (n=1837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0569 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.221 (n=2087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6398 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2864` → IC=+0.242 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2864 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.4984` → IC=+0.240 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4984 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=2021)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2464.3002` → IC=+0.218 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2464.3002 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.219 (n=731)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.228 (n=991)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0228 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.226 (n=1540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.261 (n=1922)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `1.2288` → IC=+0.216 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2288 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.2205` → IC=+0.216 (n=1941)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2205 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.857` → IC=+0.258 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.857 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `1.232` → IC=+0.237 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.232 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2796` → IC=+0.283 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2796 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `2.1732` → IC=+0.205 (n=1755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1732 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4282` → IC=+0.210 (n=1995)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4282 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2413.7909` → IC=+0.214 (n=1952)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2413.7909 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.202 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.211)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=3687)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.221 (n=1224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.5067` → IC=+0.191 (n=3664)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.5067 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=1368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.183 (n=1674)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.239 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1719` → IC=+0.190 (n=1353)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1719 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.4505` → IC=+0.179 (n=2409)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.4505 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.22` → IC=+0.213 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.22 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7103` → IC=+0.186 (n=1107)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.7103 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.8942` → IC=+0.183 (n=1676)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.8942 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.1682` → IC=+0.208 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1682 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.4541` → IC=+0.190 (n=1207)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4541 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.185 (n=2411)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=2730)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `2523.2108` → IC=+0.186 (n=3663)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2523.2108 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.215 (n=926)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.4893` → IC=+0.176 (n=2777)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.4893 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=1258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` < `0.1825` → IC=+0.185 (n=1222)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1825 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.6649` → IC=+0.183 (n=518)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6649 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` < `0.2383` → IC=+0.153 (n=2466)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2383 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.211` → IC=+0.169 (n=2771)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.211 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `1.2581` → IC=+0.165 (n=2613)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2581 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.166 (n=2537)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.222` → IC=+0.162 (n=574)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.222 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.5352` → IC=+0.169 (n=1208)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5352 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `1.8237` → IC=+0.171 (n=1828)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8237 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=3687)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `5324.87` → IC=+0.166 (n=2481)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5324.87 (IC base=+0.160)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.166 (n=1809)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 86.0 (IC base=+0.160)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.232 (n=445)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.266 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.220 (n=234)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.516` → IC=+0.230 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.516 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.7629` → IC=+0.207 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7629 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.3288` → IC=+0.214 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3288 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.979` → IC=+0.222 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.979 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.554` → IC=+0.209 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.554 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.213 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2212 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.8386` → IC=+0.226 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8386 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.225 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `12591.1219` → IC=+0.238 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12591.1219 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.225 (n=463)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.3661` → IC=+0.162 (n=1050)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3661 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.196 (n=350)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 4.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.183 (n=462)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1435 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.151 (n=476)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6084 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6676` → IC=+0.193 (n=99)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6676 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.162` → IC=+0.150 (n=1032)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.162 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.372` → IC=+0.167 (n=1032)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.372 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.187 (n=700)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8812 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.177 (n=218)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.5395` → IC=+0.155 (n=1046)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.5395 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.164 (n=697)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `12148.8643` → IC=+0.159 (n=938)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12148.8643 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `699.0` → IC=+0.158 (n=1005)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 699.0 (IC base=+0.147)

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

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.237)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.216 (n=392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.1517` → IC=+0.210 (n=516)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1517 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.193 (n=536)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.5225` → IC=+0.203 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5225 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `0.8847` → IC=+0.195 (n=391)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.8847 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` < `0.2066` → IC=+0.200 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2066 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.152` → IC=+0.199 (n=1056)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 4.152 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `1.0845` → IC=+0.195 (n=1033)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.0845 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` > `1.2448` → IC=+0.193 (n=392)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 1.2448 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.192 (n=1078)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.201 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `2.4736` → IC=+0.197 (n=1150)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.4736 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=1180)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.221 (n=317)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.189 (n=944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.174 (n=634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 10.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.7559` → IC=+0.169 (n=944)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7559 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.0908` → IC=+0.170 (n=944)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.0908 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.6069` → IC=+0.184 (n=204)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6069 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.2152` → IC=+0.165 (n=873)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.2152 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.718` → IC=+0.168 (n=966)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.718 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.6432` → IC=+0.203 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6432 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.7259` → IC=+0.165 (n=843)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.7259 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.183 (n=399)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.1949` → IC=+0.180 (n=814)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.1949 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.7855` → IC=+0.166 (n=617)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.7855 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `7438.5832` → IC=+0.179 (n=944)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7438.5832 (IC base=+0.164)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.163 (n=327)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0111 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.162 (n=365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 3.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=377)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.250 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.2206` → IC=+0.194 (n=246)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.2206 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.097` → IC=+0.227 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.097 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.7119` → IC=+0.187 (n=164)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.7119 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `1.282` → IC=+0.135 (n=124)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.282 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.227 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `2.4251` → IC=+0.189 (n=120)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4251 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=439)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2974.6892` → IC=+0.162 (n=371)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2974.6892 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.156 (n=309)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 51.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.192 (n=300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0067 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.6689` → IC=+0.179 (n=300)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.6689 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.164 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 16.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.2667` → IC=+0.224 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2667 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.631` → IC=+0.225 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.631 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.639` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.639 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.281` → IC=+0.164 (n=290)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 5.281 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.3839` → IC=+0.169 (n=300)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.3839 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.219 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.6095` → IC=+0.179 (n=129)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.6095 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `2.1939` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1939 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3170.0512` → IC=+0.195 (n=300)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3170.0512 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.216 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.161)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.171 (n=517)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0039 (IC base=+0.081)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.121 (n=534)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 16.0 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.6473` → IC=+0.181 (n=967)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.6473 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1434` → IC=+0.145 (n=586)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1434 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.45` → IC=+0.190 (n=253)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.45 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.191 (n=147)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.2302` → IC=+0.260 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2302 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` < `0.201` → IC=+0.135 (n=475)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.201 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.09` → IC=+0.149 (n=360)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.09 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.1401` → IC=+0.202 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1401 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `2.5523` → IC=+0.152 (n=369)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.5523 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` > `1.4507` → IC=+0.143 (n=329)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4507 (IC base=+0.051)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.140 (n=404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0058 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.120 (n=409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.4419` → IC=+0.169 (n=373)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.4419 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.165 (n=198)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `2.4916` → IC=+0.126 (n=332)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.4916 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.124 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0053 (IC base=+0.089)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.202 (n=65)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.2737` → IC=+0.268 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2737 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.0689` → IC=+0.142 (n=205)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.0689 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.876` → IC=+0.178 (n=197)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.876 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `1.151` → IC=+0.134 (n=203)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.151 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `0.8122` → IC=+0.142 (n=135)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.8122 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.188 (n=78)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `2.412` → IC=+0.167 (n=181)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.412 (IC base=+0.089)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.7143` → IC=-0.127 (n=156)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=+0.220 (n=319)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=162)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.144 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0048 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.220 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7143 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.175 (n=195)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.674` → IC=+0.279 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.674 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.206 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.7834` → IC=+0.149 (n=203)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7834 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `1135.9488` → IC=+0.154 (n=316)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1135.9488 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.7058` → IC=+0.143 (n=127)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.7058 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.003)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.011` → IC=-0.256 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=131)

- **FILTRO** `ibs_20min` > `0.1176` → IC=-0.261 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1176
  - _Potencial_: sin este filtro IC_bueno=+0.302 (n=89)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.178 (n=237)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7647 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.58` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 9.58 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.210 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.052)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.139 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.011 (IC base=+0.040)

- **PATRÓN** `ibs_20min` < `0.1176` → IC=+0.302 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1176 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.93` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.93 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `0.5953` → IC=+0.128 (n=100)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.5953 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.1332` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1332 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.0771` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.0771 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.7925` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7925 (IC base=+0.040)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.06 (IC base=+0.040)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.300 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=183)

- **FILTRO** `dist_vwap_pct` > `0.2402` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2402
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=226)

- **FILTRO** `volumen_regimen` < `0.7363` → IC=-0.355 (n=60)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7363
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=181)

- **FILTRO** `sigma_h` > `0.0057` → IC=-0.365 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=152)

- **FILTRO** `ibs_20min` > `0.92` → IC=-0.327 (n=50)

  - _Acción_: SKIP cuando `ibs_20min` > 0.92
  - _Potencial_: sin este filtro IC_bueno=-0.253 (n=152)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.253 (n=180)

- **FILTRO** `volumen_pendiente_norm` > `0.0718` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=97)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.238 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=40)

- **FILTRO** `volumen_regimen` < `1.2353` → IC=-0.262 (n=40)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2353
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=40)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=64)

- **FILTRO** `sigma_ewma_delta_pct` > `2.55` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.55
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=55)

- **FILTRO** `volumen_regimen` > `0.8507` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8507
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=64)

- **FILTRO** `libro_liquidez` < `3685.6992` → IC=-0.233 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 3685.6992
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=57)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0023` → IC=-0.357 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0023
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=60)

- **FILTRO** `ibs_20min` < `0.5857` → IC=-0.464 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5857
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=53)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.350 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=55)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=53)

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=49)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=-0.179)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=66)

- **FILTRO** `ibs_20min` < `0.125` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.125
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=63)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **FILTRO** `dist_vwap_pct` < `0.219` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.219
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=20)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=22)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.179 (n=157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0059 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.126 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 15.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.6472` → IC=+0.143 (n=345)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6472 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.4941` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.4941 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.7233` → IC=+0.123 (n=152)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.7233 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `1.8098` → IC=+0.127 (n=164)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8098 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.138 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 14.0 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.1558` → IC=+0.180 (n=317)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1558 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.636` → IC=+0.214 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.636 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` < `2.6627` → IC=+0.134 (n=285)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.6627 (IC base=+0.083)

- **PATRÓN** `libro_liquidez` > `3965.7979` → IC=+0.193 (n=164)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3965.7979 (IC base=+0.083)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6292` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6292
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=102)

- **PATRÓN** `sigma_h` > `0.0025` → IC=+0.183 (n=143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0025 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.230 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.1381` → IC=+0.222 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1381 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.1082` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1082 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.611` → IC=+0.189 (n=130)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 4.611 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `1.1471` → IC=+0.167 (n=160)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1471 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.6754` → IC=+0.176 (n=143)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6754 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.1891` → IC=+0.221 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1891 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.6699` → IC=+0.210 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6699 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.179 (n=129)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `4599.6467` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4599.6467 (IC base=+0.156)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1682` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1682
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=89)

- **FILTRO** `libro_liquidez` < `1549.8575` → IC=-0.173 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 1549.8575
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=98)

- **FILTRO** `ibs_20min` > `0.2038` → IC=-0.127 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2038
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=111)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.144 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 12.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.2038` → IC=+0.155 (n=111)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2038 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.8316` → IC=+0.121 (n=85)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 0.8316 (IC base=+0.059)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.1087` → IC=-0.176 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1087
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=28)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.277 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.252 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9459` → IC=+0.228 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9459 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.6436` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6436 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.768` → IC=+0.275 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.768 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.293 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.818` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.818 (IC base=-0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.1087` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1087 (IC base=-0.035)

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
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.120 (n=1106)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.495 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2933.9421` → IC=+0.152 (n=317)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2933.9421 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=910)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.120 (n=1106)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.495 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2933.9421` → IC=+0.152 (n=317)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2933.9421 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=910)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `py_entrada` < `0.445` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=116)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=147)

- **FILTRO** `libro_liquidez` < `9493.103` → IC=-0.179 (n=107)

  - _Acción_: SKIP cuando `libro_liquidez` < 9493.103
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=56)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=231)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=217)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=46)

- **FILTRO** `libro_liquidez` < `10724.0239` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 10724.0239
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=50)

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
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=2484)

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

- **FILTRO** `ballena_activa_n` > `555.0` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 555.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=62)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=98)

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

- **PATRÓN** `liq_usd_total` > `132184.93` → IC=+0.137 (n=89)

  - _Acción_: Kelly boost +0.69€ cuando `liq_usd_total` > 132184.93 (IC base=+0.057)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.165 (n=156)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.495 (IC base=+0.057)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=984)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=938)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=572)

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
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=286)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.176 (n=103)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.495 (IC base=+0.030)

- **PATRÓN** `libro_liquidez` > `4214.4529` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 4214.4529 (IC base=+0.030)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=748)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=748)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=479)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=479)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=206)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=206)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=168)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.144 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=150)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=119)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=143)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=239)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=114)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=127)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=288)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=288)

- **FILTRO** `libro_liquidez` < `553.1995` → IC=-0.132 (n=104)

  - _Acción_: SKIP cuando `libro_liquidez` < 553.1995
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=214)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=172)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.48` → IC=-0.120 (n=1385)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=753)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `restante_min` < `3.89` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

- **FILTRO** `lag_apertura_s` > `66.89` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.89
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.122 (n=146)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=56)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.145 (n=74)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=192)

- **PATRÓN** `py_entrada` < `0.56` → IC=+0.120 (n=135)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.56 (IC base=+0.019)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.207 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.043)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.174 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=95)

- **FILTRO** `lag_apertura_s` > `290.6` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `lag_apertura_s` > 290.6
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=90)

- **FILTRO** `profundidad_ratio` < `30.1` → IC=-0.137 (n=89)

  - _Acción_: SKIP cuando `profundidad_ratio` < 30.1
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=47)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `restante_min` < `3.99` → IC=-0.126 (n=105)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **FILTRO** `lag_apertura_s` > `60.71` → IC=-0.125 (n=110)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.71
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=37)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.147 (n=137)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=48)

- **FILTRO** `profundidad_ratio` < `54.9` → IC=-0.230 (n=61)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.9
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=124)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=153)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.239 (n=44)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=197)

- **FILTRO** `restante_min` < `3.44` → IC=-0.228 (n=79)

  - _Acción_: SKIP cuando `restante_min` < 3.44
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=162)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.172 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=185)

- **FILTRO** `lag_apertura_s` > `91.82` → IC=-0.223 (n=81)

  - _Acción_: SKIP cuando `lag_apertura_s` > 91.82
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=160)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.160 (n=154)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=85)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.144 (n=85)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` > 0.5 (IC base=-0.052)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.227 (n=75)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=216)

- **FILTRO** `lag_apertura_s` > `104.65` → IC=-0.130 (n=98)

  - _Acción_: SKIP cuando `lag_apertura_s` > 104.65
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=193)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.163 (n=4379)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=13258)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.165 (n=4393)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=13857)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.199 (n=771)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2346)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.151 (n=775)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=2491)

- **PATRÓN** `libro_liquidez` > `1802.0485` → IC=+0.132 (n=1060)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1802.0485 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `1573.1624` → IC=+0.142 (n=1111)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1573.1624 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.177 (n=770)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2396)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=766)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2538)

- **PATRÓN** `libro_liquidez` > `1800.2761` → IC=+0.132 (n=1077)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1800.2761 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.163 (n=755)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=2356)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2420)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3160)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=403)

- **FILTRO** `libro_liquidez` < `17110.7517` → IC=-0.144 (n=237)

  - _Acción_: SKIP cuando `libro_liquidez` < 17110.7517
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=712)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=281)

- **FILTRO** `ibs_20min` > `0.9763` → IC=-0.210 (n=91)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9763
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=276)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1934.3745` → IC=-0.173 (n=325)

  - _Acción_: SKIP cuando `libro_liquidez` < 1934.3745
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=660)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=230)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=12393)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=27441)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.282 (n=9343)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=30491)

- **FILTRO** `ibs_7min` < `0.2612` → IC=-0.233 (n=9958)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2612
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=29876)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=13518)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=26316)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.234 (n=12305)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=38178)

- **FILTRO** `ibs_7min` > `0.2907` → IC=-0.180 (n=12620)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2907
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=37863)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.139 (n=2016)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=4732)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.307 (n=1619)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=5129)

- **FILTRO** `ibs_7min` < `0.7073` → IC=-0.251 (n=2226)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7073
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=4522)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.182 (n=1534)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5214)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.265 (n=2149)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6574)

- **FILTRO** `ibs_7min` > `0.7889` → IC=-0.208 (n=2180)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7889
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6543)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=1626)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5188)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.248 (n=1672)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=5142)

- **FILTRO** `ibs_7min` < `0.7428` → IC=-0.197 (n=1702)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7428
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=5112)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.176 (n=1695)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=5119)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=1619)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=5320)

- **FILTRO** `ibs_7min` > `0.2631` → IC=-0.190 (n=1733)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2631
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5206)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.187 (n=1724)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5215)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.160 (n=1834)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=4581)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=1523)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4892)

- **FILTRO** `ibs_7min` < `0.7022` → IC=-0.245 (n=2115)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7022
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4300)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.213 (n=1494)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4921)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.244 (n=2136)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=7182)

- **FILTRO** `ibs_7min` > `0.7426` → IC=-0.173 (n=2329)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7426
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=6989)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.236 (n=1950)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4602)

- **FILTRO** `ibs_7min` < `0.7394` → IC=-0.187 (n=1638)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7394
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4914)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.176 (n=1602)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4950)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=1667)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=5069)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.179 (n=1683)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=5053)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.182 (n=1657)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=5079)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.264 (n=1685)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=5090)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.231 (n=1658)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=5117)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=2294)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=7352)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.273 (n=1539)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=4991)

- **FILTRO** `ibs_7min` < `0.26` → IC=-0.221 (n=1630)

  - _Acción_: SKIP cuando `ibs_7min` < 0.26
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4900)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1494)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5036)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.209 (n=2127)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=6994)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1199)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=597)

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
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=334)

- **FILTRO** `libro_liquidez` < `3298.5458` → IC=-0.156 (n=161)

  - _Acción_: SKIP cuando `libro_liquidez` < 3298.5458
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=483)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.134 (n=886)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.135 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 14.0 (IC base=+0.120)

- **PATRÓN** `total_vol_5m` < `442.4725` → IC=+0.150 (n=295)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 442.4725 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.128 (n=750)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 53.0 (IC base=+0.120)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.167 (n=70)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.231 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.140 (n=223)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.04 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2602.0106` → IC=+0.218 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2602.0106 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.170 (n=92)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 12.0 (IC base=+0.140)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 10.0 (IC base=+0.106)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.183 (n=121)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.109)

- **PATRÓN** `total_vol_5m` < `390.044` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 390.044 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.183 (n=80)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 73.0 (IC base=+0.109)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3989` → IC=+0.173 (n=157)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.3989 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `8082.459` → IC=+0.154 (n=157)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 8082.459 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 28.0 (IC base=+0.135)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.147 (n=154)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.126 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 15.0 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3635.4092` → IC=+0.175 (n=78)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3635.4092 (IC base=+0.102)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.75` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.75
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=113)

- **FILTRO** `sigma_h` > `0.0044` → IC=-0.235 (n=326)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=162)

- **FILTRO** `T_h` > `57.4571` → IC=-0.210 (n=326)

  - _Acción_: SKIP cuando `T_h` > 57.4571
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=162)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.258 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.245 (n=49)

- **FILTRO** `T_h` > `87.9981` → IC=-0.395 (n=36)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=110)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.245 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.088)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0087` → IC=-0.192 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0087
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=26)

- **FILTRO** `pct_vs_K` |x|> `9.1619` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.1619
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=34)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.202 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0087` → IC=-0.180 (n=298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=154)

- **FILTRO** `T_h` > `72.5264` → IC=-0.147 (n=338)

  - _Acción_: SKIP cuando `T_h` > 72.5264
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=114)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.320 (n=98)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=297)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.310 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=297)

- **FILTRO** `T_h` > `59.6469` → IC=-0.315 (n=296)

  - _Acción_: SKIP cuando `T_h` > 59.6469
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=99)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `68.7654` → IC=-0.147 (n=117)

  - _Acción_: SKIP cuando `T_h` > 68.7654
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=40)

- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.378 (n=39)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=118)

- **FILTRO** `T_h` > `143.8015` → IC=-0.300 (n=48)

  - _Acción_: SKIP cuando `T_h` > 143.8015
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=96)

- **FILTRO** `pct_vs_K` |x|> `3.0893` → IC=-0.446 (n=35)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0893
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=109)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.9851` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `T_h` > 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=96)

- **FILTRO** `pct_vs_K` |x|> `3.4756` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4756
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=96)

- **FILTRO** `sigma_h` > `0.0089` → IC=-0.344 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=91)

- **FILTRO** `sigma_h` < `0.0048` → IC=-0.344 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=91)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0137` → IC=-0.190 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0137
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=85)

- **FILTRO** `sigma_h` < `0.0073` → IC=-0.200 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=84)

- **FILTRO** `T_h` > `135.1308` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `T_h` > 135.1308
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=85)

- **FILTRO** `pct_vs_K` |x|> `4.1091` → IC=-0.429 (n=26)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.1091
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=52)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1236` → IC=+0.469 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1236 (IC base=+0.346)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.396 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.346)

- **PATRÓN** `T_h` > `1.2259` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2259 (IC base=+0.346)

- **PATRÓN** `dist_50` > `0.4067` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4067 (IC base=+0.346)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.365 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.346)

- **PATRÓN** `edge` > `0.096` → IC=+0.454 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.421)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.433 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.421)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.448 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.421)

- **PATRÓN** `T_h` < `0.608` → IC=+0.432 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.608 (IC base=+0.421)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.449 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.421)

- **PATRÓN** `dist_50` > `0.4027` → IC=+0.483 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4027 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.474 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.421)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1072` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1072 (IC base=+0.421)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.406 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.421)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.455 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.421)

- **PATRÓN** `T_h` < `0.9168` → IC=+0.450 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9168 (IC base=+0.421)

- **PATRÓN** `T_h` > `0.5098` → IC=+0.402 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5098 (IC base=+0.421)

- **PATRÓN** `dist_50` > `0.4166` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4166 (IC base=+0.421)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.413 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.431 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.421)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.434)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.469 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.434)

- **PATRÓN** `T_h` > `0.8294` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8294 (IC base=+0.434)

- **PATRÓN** `dist_50` > `0.3691` → IC=+0.452 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3691 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.434)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=235)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=330)

- **PATRÓN** `streak_estiramiento` < `0.5782` → IC=+0.146 (n=145)

  - _Acción_: Kelly boost +0.73€ cuando `streak_estiramiento` < 0.5782 (IC base=+0.032)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=47)

- **FILTRO** `volumen_racha` > `990711.2` → IC=-0.186 (n=33)

  - _Acción_: SKIP cuando `volumen_racha` > 990711.2
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=34)

- **FILTRO** `streak_estiramiento` > `0.4382` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4382
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=41)

- **PATRÓN** `volumen_racha` < `990711.2` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_racha` < 990711.2 (IC base=-0.007)

- **PATRÓN** `streak_estiramiento` < `0.4382` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `streak_estiramiento` < 0.4382 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.122 (n=96)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 48.0 (IC base=+0.062)

- **PATRÓN** `libro_liquidez` > `2492.9344` → IC=+0.124 (n=91)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2492.9344 (IC base=+0.062)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=521)

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
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=744)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=888)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=883)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3288)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1706)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.211 (n=707)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.241 (n=706)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0507` → IC=+0.211 (n=707)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0507 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2208` → IC=+0.214 (n=705)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2208 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1268` → IC=+0.234 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1268 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.209 (n=1960)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=2188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.6173` → IC=+0.280 (n=2116)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6173 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.204 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.845` → IC=+0.278 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.845 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2953.6818` → IC=+0.208 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2953.6818 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.220 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.202)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=910)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.230 (n=449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.276 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.214)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.255 (n=149)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.214)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.271 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.245 (n=414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.214)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.276 (n=448)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.367` → IC=+0.268 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.367 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `16178.7073` → IC=+0.250 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16178.7073 (IC base=+0.214)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.104` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.104
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=545)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.195 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0035 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.170 (n=213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.149)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2346` → IC=+0.177 (n=162)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.2346 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1204` → IC=+0.169 (n=182)

  - _Acción_: Kelly boost +0.84€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1204 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.166 (n=348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.149 (n=223)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 6.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.6559` → IC=+0.270 (n=433)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6559 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.2829` → IC=+0.159 (n=447)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2829 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.546` → IC=+0.238 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.546 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `3410.3513` → IC=+0.164 (n=433)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3410.3513 (IC base=+0.149)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.284 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.1521` → IC=+0.221 (n=227)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1521 (IC base=+0.190)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0615` → IC=+0.200 (n=258)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0615 (IC base=+0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3429` → IC=+0.242 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3429 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.198 (n=230)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_15` > `0.5897` → IC=+0.277 (n=258)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5897 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.1223` → IC=+0.217 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1223 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.286` → IC=+0.360 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.286 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `3201.6733` → IC=+0.295 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3201.6733 (IC base=+0.190)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.003)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0232` → IC=+0.289 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0232 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.226 (n=235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.210)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0641` → IC=+0.215 (n=478)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0641 (IC base=+0.210)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0847` → IC=+0.264 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0847 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.210)

- **PATRÓN** `ibs_15` > `0.5806` → IC=+0.293 (n=534)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5806 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.1349` → IC=+0.221 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1349 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.567` → IC=+0.210 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.567 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.188` → IC=+0.250 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.188 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.305` → IC=+0.210 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.305 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2932.3706` → IC=+0.294 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2932.3706 (IC base=+0.210)

- **PATRÓN** `ibs_15` < `0.1154` → IC=+0.146 (n=597)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` < 0.1154 (IC base=+0.058)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.365 (n=332)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.357)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.364 (n=498)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.357)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.360 (n=333)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.357)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1493` → IC=+0.383 (n=331)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1493 (IC base=+0.357)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1316` → IC=+0.391 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1316 (IC base=+0.357)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.400 (n=239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.357)

- **PATRÓN** `ibs_15` > `0.7856` → IC=+0.396 (n=498)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7856 (IC base=+0.357)

- **PATRÓN** `dist_vwap_pct` > `0.4306` → IC=+0.387 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4306 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.366 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.357 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.357)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.362 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.357)

- **PATRÓN** `libro_liquidez` > `3813.5418` → IC=+0.375 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3813.5418 (IC base=+0.357)

- **PATRÓN** `ballena_activa_n` < `446.0` → IC=+0.379 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 446.0 (IC base=+0.357)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1136` → IC=+0.369 (n=120)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1136 (IC base=+0.363)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.371 (n=239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0025` → IC=+0.365 (n=272)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0025 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.371 (n=91)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.363)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.369 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1529` → IC=+0.385 (n=181)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1529 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.397 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.383 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.394 (n=272)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.3959` → IC=+0.415 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3959 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.032` → IC=+0.367 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.032 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.362 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `16049.8465` → IC=+0.382 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.8465 (IC base=+0.363)

- **PATRÓN** `ballena_activa_n` < `502.0` → IC=+0.415 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 502.0 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.353 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.348)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.376 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.348)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.363 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.348)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.368 (n=202)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.348)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.375 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.348)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.408 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.348)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.399 (n=226)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.348)

- **PATRÓN** `dist_vwap_pct` > `0.4608` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4608 (IC base=+0.348)

- **PATRÓN** `dist_vwap_pct` < `0.2966` → IC=+0.350 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2966 (IC base=+0.348)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.031` → IC=+0.363 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.031 (IC base=+0.348)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.352 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.348)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.354 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.348)

- **PATRÓN** `libro_liquidez` > `4242.86` → IC=+0.372 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4242.86 (IC base=+0.348)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.356 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.348)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.221 (n=797)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=2392)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.203 (n=1135)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2054)

- **PATRÓN** `delta_ratio_macro` |x|> `0.141` → IC=+0.183 (n=518)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio_macro` |x|> 0.141 (IC base=-0.061)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1356` → IC=+0.252 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1356 (IC base=-0.061)

- **PATRÓN** `ibs_15` > `0.6423` → IC=+0.281 (n=777)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6423 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` < `0.2631` → IC=+0.206 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2631 (IC base=-0.061)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1242` → IC=+0.252 (n=1603)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1242 (IC base=-0.021)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1818` → IC=+0.251 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1818 (IC base=-0.021)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.275 (n=2408)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.021)

- **PATRÓN** `dist_vwap_pct` > `0.6634` → IC=+0.298 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6634 (IC base=-0.021)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.206 (n=478)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1435)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.219 (n=478)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1435)

- **FILTRO** `sigma_ewma_delta_pct` > `23.635` → IC=-0.257 (n=270)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.635
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=1643)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.168 (n=185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0028 (IC base=+0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2051` → IC=+0.304 (n=105)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2051 (IC base=+0.087)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.330 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.087)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.123 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 12.0 (IC base=+0.087)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.333 (n=231)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.099` → IC=+0.287 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.099 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.2353` → IC=+0.279 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2353 (IC base=+0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0841` → IC=+0.176 (n=35)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.0841 (IC base=-0.191)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.191)

- **PATRÓN** `ibs_15` < `0.501` → IC=+0.306 (n=34)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.501 (IC base=-0.191)

- **PATRÓN** `dist_vwap_pct` < `0.0553` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0553 (IC base=-0.191)

- **PATRÓN** `ballena_activa_n` < `305.0` → IC=+0.393 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 305.0 (IC base=-0.191)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.173 (n=485)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.170 (n=377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0065 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.168 (n=377)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0034 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.220 (n=166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.163)

- **PATRÓN** `drift_15min` |x|≤ `0.4128` → IC=+0.164 (n=126)

  - _Acción_: Kelly boost +0.82€ cuando `drift_15min` |x|≤ 0.4128 (IC base=+0.163)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.164 (n=251)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.163)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.234 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.188 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 11.0 (IC base=+0.163)

- **PATRÓN** `ibs_15` > `0.6526` → IC=+0.266 (n=378)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6526 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.2829` → IC=+0.175 (n=349)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2829 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.049` → IC=+0.203 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.049 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=485)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `3762.3` → IC=+0.167 (n=337)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3762.3 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.247 (n=906)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.4455` → IC=+0.239 (n=906)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4455 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `0.7761` → IC=+0.250 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7761 (IC base=+0.237)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2074` → IC=+0.265 (n=411)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2074 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=799)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `ibs_15` < `0.3647` → IC=+0.270 (n=906)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3647 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.7528` → IC=+0.306 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7528 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.226` → IC=+0.276 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.226 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.457` → IC=+0.240 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.457 (IC base=+0.237)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.232 (n=252)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=491)

- **FILTRO** `drift_15min` |x|> `0.8976` → IC=-0.275 (n=185)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8976
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=558)

- **FILTRO** `sigma_ewma_delta_pct` > `18.28` → IC=-0.144 (n=400)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.28
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3208)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.151 (n=41)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.172)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.219 (n=55)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=-0.172)

- **PATRÓN** `dist_vwap_pct` < `0.1248` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1248 (IC base=-0.172)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 44.0 (IC base=-0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0785` → IC=+0.227 (n=350)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0785 (IC base=-0.040)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.183` → IC=+0.231 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.183 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.270 (n=394)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.6964` → IC=+0.250 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6964 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.1715` → IC=+0.234 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1715 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0196` → IC=-0.259 (n=450)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0196
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=451)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.260 (n=265)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=636)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1446` → IC=+0.271 (n=277)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1446 (IC base=-0.034)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1078` → IC=+0.323 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1078 (IC base=-0.034)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=609)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` > `0.8607` → IC=+0.355 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8607 (IC base=-0.034)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=8)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.035)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=8)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.035)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.300 (n=707)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.330 (n=268)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.311 (n=268)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2199` → IC=+0.323 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2199 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.327 (n=803)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2727` → IC=+0.329 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2727 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.348 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `13010.2959` → IC=+0.300 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13010.2959 (IC base=+0.293)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.294 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.332 (n=147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2575` → IC=+0.311 (n=146)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2575 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.303 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.314 (n=439)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.4223` → IC=+0.350 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4223 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.15` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.15 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `16196.8854` → IC=+0.326 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16196.8854 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.320 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.301)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.300 (n=364)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0035 (IC base=+0.301)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.322 (n=161)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.301)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.300 (n=243)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.301)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2902` → IC=+0.332 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2902 (IC base=+0.301)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.319 (n=379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.301)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.339 (n=364)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.301)

- **PATRÓN** `dist_vwap_pct` > `0.2899` → IC=+0.312 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2899 (IC base=+0.301)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.337 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.301)

### UPDOWN_OU_5M
- **FILTRO** `sigma_h` > `0.0043` → IC=-0.265 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=197)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.197 (n=64)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=128)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0687` → IC=-0.139 (n=59)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0687
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=117)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.174 (n=44)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=132)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.133 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

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

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.188 (n=30)
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
- **PATRÓN** `T_h` > `80.0063` → IC=+0.228 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 80.0063 (IC base=+0.214)

- **PATRÓN** `ratio` < `0.9753` → IC=+0.471 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9753 (IC base=+0.214)

- **PATRÓN** `T_h` > `145.7579` → IC=+0.393 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7579 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0115` → IC=+0.318 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0115 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `126.1277` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 126.1277 (IC base=+0.194)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.468 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.194)

- **PATRÓN** `T_h` > `103.9325` → IC=+0.296 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.9325 (IC base=+0.288)

- **PATRÓN** `ratio` > `1.0479` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0479 (IC base=+0.288)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `81.6471` → IC=+0.273 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 81.6471 (IC base=+0.249)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.430 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.249)

- **PATRÓN** `T_h` > `110.1026` → IC=+0.339 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 110.1026 (IC base=+0.320)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.353 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.320)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1132` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.401)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6173 sube el IC de +0.202 a +0.280 en UPDOWN_GBM#15min (n=2116). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.214 a +0.276 en UPDOWN_GBM#BTC#15min (n=448). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6559 sube el IC de +0.149 a +0.270 en UPDOWN_GBM#ETH#15min (n=433). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5897 sube el IC de +0.190 a +0.277 en UPDOWN_GBM#SOL#15min (n=258). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5806 sube el IC de +0.210 a +0.293 en UPDOWN_GBM#XRP#15min (n=534). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6423 sube el IC de -0.061 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=777). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.021 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=2408). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.087 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=231). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.501 sube el IC de -0.191 a +0.306 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6526 sube el IC de +0.163 a +0.266 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=378). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3647 sube el IC de +0.237 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=906). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de -0.172 a +0.219 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=55). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.040 a +0.270 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=394). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.034 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=609). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.293 a +0.327 en UPDOWN_GBM_IBS_ALTO (n=803). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.285 a +0.314 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=439). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.301 a +0.339 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=364). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7856 sube el IC de +0.357 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=498). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.363 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=272). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.348 a +0.399 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=226). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1507 | +0.096 | +187.84€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1507 | +0.096 | +187.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1144 | +0.105 | +163.74€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1144 | +0.105 | +163.74€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 261 | +0.063 | +9.98€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 261 | +0.063 | +9.98€ | 6 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 71 | +0.103 | +14.46€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 71 | +0.103 | +14.46€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 101 | +0.034 | +17.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 101 | +0.034 | +17.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 80 | +0.049 | +14.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 80 | +0.049 | +14.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 21 | -0.022 | +3.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 21 | -0.022 | +3.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 32512 | -0.089 | -4333.82€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1670 | -0.020 | -220.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 30842 | -0.093 | -4113.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4208 | -0.114 | -712.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4208 | -0.114 | -712.42€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1670 | -0.020 | -220.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1670 | -0.020 | -220.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3849 | -0.116 | -866.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3849 | -0.116 | -866.34€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8397 | -0.007 | -762.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8397 | -0.007 | -762.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8078 | -0.104 | -565.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8078 | -0.104 | -565.80€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6310 | -0.167 | -1206.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6310 | -0.167 | -1206.88€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 24021 | -0.021 | +3694.83€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6219 | +0.001 | +1746.58€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 17802 | -0.029 | +1948.25€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 24021 | -0.021 | +3694.83€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6219 | +0.001 | +1746.58€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 17802 | -0.029 | +1948.25€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 110748 | +0.113 | -5237.15€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15781 | +0.183 | -497.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 466 | -0.056 | -59.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 87554 | +0.102 | -4411.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6947 | +0.104 | -269.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 14543 | +0.101 | -1090.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 51 | -0.141 | +9.84€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 14477 | +0.102 | -1088.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 22057 | +0.130 | -386.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4790 | +0.199 | -132.12€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 14516 | +0.115 | -165.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2709 | +0.093 | -66.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 14589 | +0.092 | -1230.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 59 | -0.107 | -4.41€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 14515 | +0.094 | -1214.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 23528 | +0.124 | -448.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6315 | +0.176 | -103.85€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 14679 | +0.106 | -275.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2522 | +0.099 | -60.37€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 21470 | +0.114 | -1221.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4514 | +0.187 | -277.03€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 369 | -0.018 | -5.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 14871 | +0.093 | -797.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1716 | +0.130 | -142.13€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 14561 | +0.100 | -860.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 52 | -0.037 | +9.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 14496 | +0.100 | -870.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 17657 | +0.195 | -1092.26€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 17657 | +0.195 | -1092.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4115 | +0.174 | -384.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4115 | +0.174 | -384.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1813 | +0.203 | -20.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1813 | +0.203 | -20.77€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4063 | +0.181 | -332.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4063 | +0.181 | -332.94€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3585 | +0.242 | -117.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3585 | +0.242 | -117.07€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4002 | +0.190 | -250.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4002 | +0.190 | -250.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 826 | +0.432 | -18.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 826 | +0.432 | -18.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 325 | +0.442 | -0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 325 | +0.442 | -0.46€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 312 | +0.433 | -5.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 312 | +0.433 | -5.88€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 177 | +0.411 | -9.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 177 | +0.411 | -9.98€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 61232 | +0.198 | -4657.35€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 61232 | +0.198 | -4657.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10530 | +0.180 | -1156.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10530 | +0.180 | -1156.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9826 | +0.223 | -349.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9826 | +0.223 | -349.90€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10556 | +0.174 | -1219.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10556 | +0.174 | -1219.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9901 | +0.219 | -378.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9901 | +0.219 | -378.59€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10141 | +0.203 | -661.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10141 | +0.203 | -661.12€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10278 | +0.192 | -892.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10278 | +0.192 | -892.03€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 23293 | +0.115 | +121.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 23293 | +0.115 | +121.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 11567 | +0.119 | +119.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 11567 | +0.119 | +119.46€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 11726 | +0.112 | +2.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 11726 | +0.112 | +2.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1686 | +0.288 | -27.01€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1686 | +0.288 | -27.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 757 | +0.279 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 757 | +0.279 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 814 | +0.287 | -12.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 814 | +0.287 | -12.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 115 | +0.346 | +3.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 115 | +0.346 | +3.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 749 | +0.439 | +0.17€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 749 | +0.439 | +0.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 359 | +0.436 | -2.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 359 | +0.436 | -2.40€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 344 | +0.442 | +2.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 344 | +0.442 | +2.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1292 | +0.068 | -64.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 459 | +0.055 | -39.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 833 | +0.075 | -25.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1016 | +0.075 | -31.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 183 | +0.073 | -6.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 833 | +0.075 | -25.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 210 | +0.024 | -34.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 210 | +0.024 | -34.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 44341 | +0.099 | -1225.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3607 | +0.091 | +43.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 40734 | +0.099 | -1268.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 24642 | +0.103 | -323.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3607 | +0.091 | +43.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 21035 | +0.105 | -367.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8707 | +0.107 | -44.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8707 | +0.107 | -44.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 10992 | +0.081 | -856.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 10992 | +0.081 | -856.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 863 | +0.207 | -101.67€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 863 | +0.207 | -101.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 863 | +0.207 | -101.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 863 | +0.207 | -101.67€ | 1 | 4 |
| ✅ GBM_LATE_15M | 31192 | +0.087 | +15403.45€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 31192 | +0.087 | +15403.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5228 | +0.203 | +4019.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5228 | +0.203 | +4019.96€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 4646 | +0.177 | +3331.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4646 | +0.177 | +3331.94€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 5532 | +0.198 | +4137.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5532 | +0.198 | +4137.78€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4444 | +0.030 | +1112.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4444 | +0.030 | +1112.99€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 4443 | -0.031 | +979.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4443 | -0.031 | +979.11€ | 4 | 11 |
| ✅ GBM_LATE_15M#XRP | 6899 | -0.036 | +1821.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6899 | -0.036 | +1821.67€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 33492 | +0.087 | +17841.28€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 33492 | +0.087 | +17841.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6434 | +0.012 | +3329.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6434 | +0.012 | +3329.98€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6959 | +0.014 | +1467.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6959 | +0.014 | +1467.26€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4750 | +0.267 | +4867.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4750 | +0.267 | +4867.05€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5593 | +0.009 | +1233.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5593 | +0.009 | +1233.54€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5414 | +0.035 | +2186.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5414 | +0.035 | +2186.50€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4342 | +0.283 | +4756.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4342 | +0.283 | +4756.95€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 25056 | +0.172 | +19370.25€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 25056 | +0.172 | +19370.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3767 | +0.216 | +3146.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3767 | +0.216 | +3146.28€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3958 | +0.148 | +2871.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3958 | +0.148 | +2871.63€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3970 | +0.212 | +3219.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3970 | +0.212 | +3219.39€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4210 | +0.137 | +3116.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4210 | +0.137 | +3116.98€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4697 | +0.122 | +3409.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4697 | +0.122 | +3409.22€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4454 | +0.209 | +3606.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4454 | +0.209 | +3606.75€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6832 | +0.137 | +3210.40€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6832 | +0.137 | +3210.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 338 | +0.141 | +185.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 338 | +0.141 | +185.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1977 | +0.141 | +1046.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1977 | +0.141 | +1046.73€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2048 | +0.153 | +1005.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2048 | +0.153 | +1005.81€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1561 | +0.108 | +564.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1561 | +0.108 | +564.65€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 534 | +0.134 | +230.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 534 | +0.134 | +230.88€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 31443 | +0.179 | +24134.83€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 31443 | +0.179 | +24134.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4978 | +0.230 | +4410.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4978 | +0.230 | +4410.91€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4889 | +0.147 | +3174.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4889 | +0.147 | +3174.67€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5244 | +0.226 | +4531.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5244 | +0.226 | +4531.48€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5108 | +0.134 | +3590.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5108 | +0.134 | +3590.83€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5530 | +0.121 | +3790.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5530 | +0.121 | +3790.48€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5694 | +0.212 | +4636.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5694 | +0.212 | +4636.46€ | 0 | 25 |
| ✅ GBM_LATE_5M | 8586 | +0.172 | +5668.82€ | 1 | 31 |
| ✅ GBM_LATE_5M#5min | 8586 | +0.172 | +5668.82€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 828 | +0.227 | +715.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 828 | +0.227 | +715.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2073 | +0.166 | +1489.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2073 | +0.166 | +1489.42€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2821 | +0.179 | +1857.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2821 | +0.179 | +1857.08€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 893 | +0.147 | +506.36€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 893 | +0.147 | +506.36€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2238 | +0.072 | +813.39€ | 0 | 12 |
| ✅ GBM_LATE_60M#60min | 2238 | +0.072 | +813.39€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 840 | +0.093 | +300.43€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 840 | +0.093 | +300.43€ | 0 | 14 |
| ✅ GBM_LATE_60M#ETH | 713 | +0.071 | +316.86€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 713 | +0.071 | +316.86€ | 2 | 10 |
| ✅ GBM_LATE_60M#SOL | 685 | +0.049 | +196.10€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 685 | +0.049 | +196.10€ | 2 | 11 |
| 🚫 GBM_LATE_60M_FADE | 443 | -0.239 | -10.18€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 443 | -0.239 | -10.18€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 165 | -0.219 | -5.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 165 | -0.219 | -5.48€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 152 | -0.227 | +0.08€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 152 | -0.227 | +0.08€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 126 | -0.273 | -4.79€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 126 | -0.273 | -4.79€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 939 | +0.088 | +234.88€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 939 | +0.088 | +234.88€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 348 | +0.083 | +74.53€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 348 | +0.083 | +74.53€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 313 | +0.052 | +33.90€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 313 | +0.052 | +33.90€ | 3 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 278 | +0.132 | +126.45€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 278 | +0.132 | +126.45€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2580 | +0.105 | +700.91€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2580 | +0.105 | +700.91€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2580 | +0.105 | +700.91€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2580 | +0.105 | +700.91€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 415 | -0.073 | -33.23€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 415 | -0.073 | -33.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 111 | -0.040 | -2.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 111 | -0.040 | -2.85€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 155 | -0.029 | -5.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 155 | -0.029 | -5.55€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2685 | +0.022 | +76.65€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2685 | +0.022 | +76.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 134 | +0.029 | -0.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 134 | +0.029 | -0.60€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 390 | +0.036 | +36.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 390 | +0.036 | +36.52€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1033 | +0.032 | +31.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1033 | +0.032 | +31.55€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 612 | +0.011 | +0.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 612 | +0.011 | +0.07€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 315 | +0.021 | +15.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 315 | +0.021 | +15.22€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1322 | -0.047 | -31.81€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1322 | -0.047 | -31.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 379 | -0.043 | -14.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 379 | -0.043 | -14.04€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 438 | -0.029 | -2.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 438 | -0.029 | -2.12€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 505 | -0.064 | -15.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 505 | -0.064 | -15.66€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 4068 | -0.024 | +39.30€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1914 | -0.030 | -16.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2154 | -0.018 | +55.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 108 | -0.009 | +2.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 56 | +0.035 | +7.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 52 | -0.056 | -4.31€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1001 | -0.002 | +44.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 468 | -0.009 | +10.31€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 533 | +0.005 | +34.31€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 458 | -0.026 | +6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 221 | -0.043 | -4.34€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 237 | -0.011 | +10.81€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 823 | -0.042 | -30.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 375 | -0.057 | -29.40€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 448 | -0.029 | -1.06€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 803 | -0.027 | +8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 388 | -0.033 | +1.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 415 | -0.020 | +7.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 875 | -0.029 | +7.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 406 | -0.029 | -1.67€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 469 | -0.029 | +8.68€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 35887 | -0.004 | +1707.59€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 35887 | -0.004 | +1707.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6383 | +0.023 | +826.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6383 | +0.023 | +826.81€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5399 | -0.031 | -67.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5399 | -0.031 | -67.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6470 | +0.019 | +624.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6470 | +0.019 | +624.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5187 | -0.052 | -152.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5187 | -0.052 | -152.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6045 | -0.008 | +207.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6045 | -0.008 | +207.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6403 | +0.012 | +268.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6403 | +0.012 | +268.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6103 | -0.059 | -147.04€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6103 | -0.059 | -147.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1484 | -0.080 | -36.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1484 | -0.080 | -36.26€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 701 | -0.126 | -33.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 701 | -0.126 | -33.93€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1802 | -0.076 | -32.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1802 | -0.076 | -32.13€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 854 | -0.015 | -25.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 854 | -0.015 | -25.03€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 90317 | -0.073 | +1800.48€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 90317 | -0.073 | +1800.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 15471 | -0.075 | +894.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 15471 | -0.075 | +894.58€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 13753 | -0.097 | -738.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 13753 | -0.097 | -738.22€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 15733 | -0.066 | +895.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 15733 | -0.066 | +895.22€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 13288 | -0.093 | -329.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 13288 | -0.093 | -329.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 16421 | -0.051 | +344.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 16421 | -0.051 | +344.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 15651 | -0.063 | +734.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 15651 | -0.063 | +734.70€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7948 | -0.030 | -141.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7948 | -0.030 | -141.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1857 | -0.041 | -17.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1857 | -0.041 | -17.03€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2238 | -0.024 | -28.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2238 | -0.024 | -28.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1081 | -0.047 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1081 | -0.047 | -19.84€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 769 | -0.021 | -24.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 769 | -0.021 | -24.37€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1315 | +0.114 | +473.85€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1179 | +0.120 | +461.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 276 | +0.140 | +141.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 276 | +0.140 | +141.66€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 224 | +0.106 | +61.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 224 | +0.106 | +61.70€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 241 | +0.109 | +90.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 241 | +0.109 | +90.42€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 209 | +0.135 | +99.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 209 | +0.135 | +99.80€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 229 | +0.102 | +67.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 229 | +0.102 | +67.68€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 791 | -0.030 | -38.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 791 | -0.030 | -38.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 154 | +0.000 | +5.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 154 | +0.000 | +5.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 113 | -0.030 | -5.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 113 | -0.030 | -5.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 220 | -0.054 | -23.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 220 | -0.054 | -23.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 172 | -0.006 | -2.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 172 | -0.006 | -2.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 132 | -0.052 | -12.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 132 | -0.052 | -12.31€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 705 | -0.093 | -63.48€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 322 | -0.145 | -76.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 251 | -0.188 | -71.36€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 71 | +0.007 | -4.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 249 | -0.054 | -0.94€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 180 | -0.060 | -4.18€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 69 | -0.035 | +3.24€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 134 | -0.037 | +13.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 106 | -0.056 | +7.79€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 28 | +0.033 | +5.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 537 | -0.120 | -67.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 168 | -0.006 | +4.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 847 | -0.201 | -43.79€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 351 | -0.194 | -30.93€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 301 | -0.196 | -31.11€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 50 | -0.173 | +0.17€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 288 | -0.217 | -28.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 247 | -0.227 | -33.90€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 41 | -0.151 | +5.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 208 | -0.186 | +15.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 190 | -0.182 | +11.55€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 18 | -0.180 | +3.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 738 | -0.204 | -53.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 109 | -0.176 | +9.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 352 | +0.401 | +284.61€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 90 | +0.370 | +74.48€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 90 | +0.370 | +74.48€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 222 | +0.460 | +211.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 222 | +0.460 | +211.37€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 352 | +0.401 | +284.61€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 603 | +0.027 | +15.77€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 603 | +0.027 | +15.77€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 43 | +0.056 | +0.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 43 | +0.056 | +0.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 63 | -0.008 | -1.69€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 63 | -0.008 | -1.69€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 202 | +0.039 | +14.40€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 202 | +0.039 | +14.40€ | 3 | 4 |
| ✅ STREAK_FADE_5M | 3037 | -0.024 | -126.72€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3037 | -0.024 | -126.72€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 903 | -0.021 | -32.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 903 | -0.021 | -32.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 577 | -0.025 | -24.71€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 577 | -0.025 | -24.71€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1401 | -0.022 | -55.42€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1401 | -0.022 | -55.42€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 85 | -0.052 | -8.44€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 85 | -0.052 | -8.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9435 | +0.020 | +112.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9435 | +0.020 | +112.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2620 | +0.021 | +28.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2620 | +0.021 | +28.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2163 | +0.029 | +50.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2163 | +0.029 | +50.31€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2839 | +0.011 | +2.43€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2839 | +0.011 | +2.43€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1813 | +0.022 | +31.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1813 | +0.022 | +31.17€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8395 | +0.013 | -43.20€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8395 | +0.013 | -43.20€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3307 | +0.017 | -5.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3307 | +0.017 | -5.56€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3348 | +0.012 | -23.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3348 | +0.012 | -23.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1740 | +0.007 | -14.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1740 | +0.007 | -14.55€ | 1 | 0 |
| ✅ UPDOWN_GBM | 51349 | +0.040 | +3699.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 13123 | +0.076 | +2696.94€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1747 | +0.006 | +10.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 33251 | +0.032 | +957.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3042 | +0.005 | +37.92€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 5237 | +0.076 | +674.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1005 | +0.155 | +439.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4199 | +0.058 | +236.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 9856 | +0.048 | +773.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1697 | +0.090 | +389.29€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 468 | +0.013 | +5.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 6244 | +0.050 | +343.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1377 | +0.005 | +35.07€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 70 | -0.083 | +0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 6037 | +0.046 | +437.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 979 | +0.138 | +350.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 5030 | +0.028 | +89.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 11323 | +0.030 | +600.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3246 | +0.054 | +445.26€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 461 | +0.008 | +9.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 6525 | +0.026 | +144.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1030 | +0.003 | -1.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 61 | -0.119 | +3.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 11462 | +0.020 | +389.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3107 | +0.029 | +258.28€ | 0 | 10 |
| ✅ UPDOWN_GBM#SOL#240min | 451 | -0.001 | -0.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 7216 | +0.020 | +131.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 635 | +0.007 | +4.76€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 53 | -0.154 | -4.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 7432 | +0.045 | +825.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3089 | +0.093 | +814.54€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 306 | +0.006 | -1.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4037 | +0.011 | +12.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 184 | -0.118 | -0.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 663 | +0.357 | +231.53€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 663 | +0.357 | +231.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 362 | +0.363 | +124.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 362 | +0.363 | +124.37€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 301 | +0.348 | +107.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 301 | +0.348 | +107.16€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 14759 | -0.030 | +3423.07€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 14759 | -0.030 | +3423.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1095 | -0.055 | +377.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1095 | -0.055 | +377.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2650 | -0.114 | +115.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2650 | -0.114 | +115.60€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 606 | +0.201 | +456.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 606 | +0.201 | +456.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1709 | +0.215 | +1115.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1709 | +0.215 | +1115.85€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4351 | -0.063 | +619.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4351 | -0.063 | +619.43€ | 3 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4348 | -0.069 | +738.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4348 | -0.069 | +738.01€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 171 | +0.026 | +6.16€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 171 | +0.026 | +6.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 171 | +0.026 | +6.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 171 | +0.026 | +6.16€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1070 | +0.293 | +891.29€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1070 | +0.293 | +891.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 585 | +0.285 | +447.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 585 | +0.285 | +447.34€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 485 | +0.301 | +443.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 485 | +0.301 | +443.95€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 750 | -0.112 | -82.64€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#5min | 750 | -0.112 | -82.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 223 | -0.087 | -17.79€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 223 | -0.087 | -17.79€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 78 | -0.175 | -5.47€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 78 | -0.175 | -5.47€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2782 | +0.306 | +1378.93€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 978 | +0.259 | +147.53€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1063 | +0.298 | +469.33€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 741 | +0.378 | +762.07€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.051) — sin ventaja clara. oversold(IBS<0.3): IC=+0.051 n=18052 | neutral: IC=+0.042 n=19057 | overbought(IBS>0.7): IC=+0.093 n=18305
  - _Datos_: n=57429 IC=+0.062 PNL=+7697.75€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 601 celda(s) pasan gate riguroso completo de 2390 evaluadas (n>=40) y 3385 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.029 < 0.08 — monitorear
  - _Datos_: n=3107 IC=+0.029 PNL=+258.28€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1063/15 IC=+0.298 PNL=+469.33€ | BTC: n=978/15 IC=+0.259 PNL=+147.53€ | SOL: n=741/15 IC=+0.378 PNL=+762.07€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 30 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 11 ops más en GBM@18h (IC actual=-0.067)
  - _Datos_: n=4 IC=-0.067 PNL=-3.02€

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: 51287 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.123 n=489/60 | contraria IC=+0.186 n=486 | gap=-0.063 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=356, boost estimado=+0.008. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 209 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1030/40 IC=+0.003 PNL=-1.92€ | BTC#60min: n=1377/40 IC=+0.005 PNL=+35.07€ | SOL#60min: n=635/40 IC=+0.007 PNL=+4.76€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=411597 | tras_1loss IC=+0.086 n=317238 | tras_2loss IC=+0.055 n=131324/40 | gap=-0.006 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.024 n=6405 | contrario_BTC IC=+0.037 n=5651/40 | gap=+0.013 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.217 > 0.08 con n=429 PNL=+351.48€
  - _Datos_: n=429 IC=+0.217 PNL=+351.48€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.216 > 0.08 con n=481 PNL=+363.52€
  - _Datos_: n=481 IC=+0.216 PNL=+363.52€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.220 > 0.08 con n=48 PNL=+32.92€
  - _Datos_: n=48 IC=+0.220 PNL=+32.92€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=2270 PNL=+1248.26€
  - _Datos_: n=2270 IC=+0.332 PNL=+1248.26€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=397 IC=+0.071 PNL=+44.23€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=397 IC=+0.071 PNL=+44.23€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=62 IC=+0.188 PNL=+41.81€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=62 IC=+0.188 PNL=+41.81€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=49011 IC=+0.039 PNL=+3534.03€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=49011 IC=+0.039 PNL=+3534.03€

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
  - _Estado_: n=2078 IC=+0.007 PNL=+1.75€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2078 IC=+0.007 PNL=+1.75€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=964 IC=+0.000 PNL=+36.17€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=964 IC=+0.000 PNL=+36.17€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=646 IC=+0.015 PNL=+27.45€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=646 IC=+0.015 PNL=+27.45€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.202 > 0.1 con n=2821 PNL=+2001.51€
  - _Datos_: n=2821 IC=+0.202 PNL=+2001.51€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1710 IC=+0.063 PNL=+133.40€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1710 IC=+0.063 PNL=+133.40€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1697 IC=+0.090 PNL=+389.29€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1697 IC=+0.090 PNL=+389.29€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.094 > 0.08 con n=7495 PNL=+2021.05€
  - _Datos_: n=7495 IC=+0.094 PNL=+2021.05€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=199 IC=-0.261 PNL=-11.77€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=199 IC=-0.261 PNL=-11.77€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=321 IC=-0.033 PNL=-5.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=321 IC=-0.033 PNL=-5.99€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=689 IC=+0.022 PNL=+55.52€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=689 IC=+0.022 PNL=+55.52€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=74 IC=+0.053 PNL=+4.31€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=74 IC=+0.053 PNL=+4.31€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=6799 IC=+0.007 PNL=+56.81€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6799 IC=+0.007 PNL=+56.81€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.08 con n=74 PNL=+21.75€
  - _Datos_: n=74 IC=+0.184 PNL=+21.75€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.258 n=122) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=122 IC=+0.258 PNL=+105.64€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=9215 IC=+0.041 PNL=+624.40€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=9215 IC=+0.041 PNL=+624.40€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=3108 IC=+0.060 PNL=+412.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3108 IC=+0.060 PNL=+412.94€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.110 > 0.08 con n=416 PNL=+125.46€
  - _Datos_: n=416 IC=+0.110 PNL=+125.46€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.149 > 0.08 con n=782 PNL=+207.29€
  - _Datos_: n=782 IC=+0.149 PNL=+207.29€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=600 PNL=+347.37€
  - _Datos_: n=600 IC=+0.115 PNL=+347.37€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=64236 IC=+0.118 PNL=+23896.07€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=64236 IC=+0.118 PNL=+23896.07€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=1792 IC=+0.109 PNL=+195.82€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=1792 IC=+0.109 PNL=+195.82€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=7638 IC=+0.046 PNL=+660.76€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7638 IC=+0.046 PNL=+660.76€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.02 con n=752 PNL=+292.12€
  - _Datos_: n=752 IC=+0.121 PNL=+292.12€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=179 IC=-0.064 PNL=+28.99€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=179 IC=-0.064 PNL=+28.99€

**〰️ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: n≥25 y IC<-0.10 para confirmar (evidencia inicial es de solo 3 ops)
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: n=81 IC=-0.030 PNL=+3.88€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=81 IC=-0.030 PNL=+3.88€

**🟡 H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: n≥25 y IC>+0.10 para confirmar
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.451 > 0.1 con n=1299 PNL=+1277.66€
  - _Datos_: n=1299 IC=+0.451 PNL=+1277.66€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=18896 IC=+0.065 PNL=+2564.61€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=18896 IC=+0.065 PNL=+2564.61€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.1 con n=4583 PNL=+2679.75€
  - _Datos_: n=4583 IC=+0.207 PNL=+2679.75€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.155 < -0.1 con n=308 PNL=+27.36€
  - _Datos_: n=308 IC=-0.155 PNL=+27.36€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2377 IC=+0.058 PNL=+251.14€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2377 IC=+0.058 PNL=+251.14€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=101 IC=-0.121 PNL=+1.95€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=101 IC=-0.121 PNL=+1.95€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.1 con n=558 PNL=+145.25€
  - _Datos_: n=558 IC=+0.120 PNL=+145.25€

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
  - _Estado_: n=22686 IC=-0.136 PNL=+1709.39€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=22686 IC=-0.136 PNL=+1709.39€

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
  - _Estado_: n=2334 IC=+0.137 PNL=+1359.87€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2334 IC=+0.137 PNL=+1359.87€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.08 con n=2782 PNL=+1988.88€
  - _Datos_: n=2782 IC=+0.203 PNL=+1988.88€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=5396 IC=+0.033 PNL=+292.55€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5396 IC=+0.033 PNL=+292.55€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=2551 PNL=+1381.14€
  - _Datos_: n=2551 IC=+0.090 PNL=+1381.14€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.08 con n=596 PNL=+318.28€
  - _Datos_: n=596 IC=+0.214 PNL=+318.28€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.227 < -0.1 con n=2250 PNL=-176.57€
  - _Datos_: n=2250 IC=-0.227 PNL=-176.57€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=6589 IC=+0.181 PNL=+4579.67€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=6589 IC=+0.181 PNL=+4579.67€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=90 PNL=+30.93€
  - _Datos_: n=90 IC=+0.098 PNL=+30.93€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2368 IC=+0.070 PNL=+746.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2368 IC=+0.070 PNL=+746.02€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.177 > 0.08 con n=2169 PNL=+1528.22€
  - _Datos_: n=2169 IC=+0.177 PNL=+1528.22€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3623 IC=-0.030 PNL=+951.40€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3623 IC=-0.030 PNL=+951.40€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.085 > 0.08 con n=598 PNL=-53.62€
  - _Datos_: n=598 IC=+0.085 PNL=-53.62€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.240 > 0.08 con n=3819 PNL=-322.24€
  - _Datos_: n=3819 IC=+0.240 PNL=-322.24€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=46 IC=+0.000 PNL=+5.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=46 IC=+0.000 PNL=+5.83€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1313) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1313 IC=+0.102 PNL=+304.56€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.321 > 0.08 con n=333 PNL=+109.90€
  - _Datos_: n=333 IC=+0.321 PNL=+109.90€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.408 n=478) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=478 IC=+0.408 PNL=+671.48€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=10530 IC=+0.180 PNL=-1156.60€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=10530 IC=+0.180 PNL=-1156.60€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.1 con n=168 PNL=+102.14€
  - _Datos_: n=168 IC=+0.206 PNL=+102.14€
