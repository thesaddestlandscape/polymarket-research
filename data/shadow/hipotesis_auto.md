# Hipótesis automáticas — 2026-10-04 06:56 UTC
_Generado por shadow_postmortem.py sobre 740690 resoluciones (PNL=+89583.00€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=573)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.221 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.132)

- **PATRÓN** `n_total_lado` > `71.0` → IC=+0.215 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 71.0 (IC base=+0.132)

- **PATRÓN** `banda_hit_calibrado` > `0.8017` → IC=+0.262 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8017 (IC base=+0.132)

- **PATRÓN** `banda_z` > `9.204` → IC=+0.197 (n=209)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 9.204 (IC base=+0.132)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.717` → IC=+0.132 (n=561)

  - _Acción_: Kelly boost +0.66€ cuando `ballenas_wallet_edge_medio` > 0.717 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.134 (n=424)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 11.0 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=661)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `3816.3674` → IC=+0.143 (n=284)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3816.3674 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `8556.0995` → IC=+0.121 (n=233)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 8556.0995 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.226 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `42.0` → IC=+0.167 (n=467)

  - _Acción_: Kelly boost +0.84€ cuando `n_total_lado` > 42.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.264 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.140)

- **PATRÓN** `banda_z` > `9.958` → IC=+0.208 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.958 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.140 (n=362)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 12.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=563)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4510.9366` → IC=+0.140 (n=226)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 4510.9366 (IC base=+0.140)

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
- **FILTRO** `restante_s_al_confirmar` < `144.28` → IC=-0.216 (n=8213)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.28
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=24646)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `132.52` → IC=-0.268 (n=1060)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.52
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=3181)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `124.8` → IC=-0.307 (n=968)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.8
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2904)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `165.48` → IC=-0.222 (n=2052)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 165.48
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=6159)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.33` → IC=-0.325 (n=1594)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.33
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=4782)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.213 (n=15955)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=3839)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `5427.4647` → IC=+0.171 (n=2490)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5427.4647 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.137 (n=14005)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=17109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=13080)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=6294)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7640.0936` → IC=+0.169 (n=2408)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 7640.0936 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.207 (n=1792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=1835)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=2310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `16039.4185` → IC=+0.221 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16039.4185 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.203 (n=1652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1835)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=2354)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `15958.35` → IC=+0.209 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15958.35 (IC base=+0.196)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.164 (n=394)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.61 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `4587.7919` → IC=+0.126 (n=249)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 4587.7919 (IC base=+0.090)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.094)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=924)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `5732.4723` → IC=+0.151 (n=233)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 5732.4723 (IC base=+0.094)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=3321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.356 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.230 (n=1490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.362 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=1730)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.256 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.138 (n=906)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `1315.39` → IC=+0.143 (n=789)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1315.39 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.406 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=649)
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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.224 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=13990)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=13383)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.234 (n=4437)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=3309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.178 (n=3137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.181 (n=3181)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.174)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.237 (n=1323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.235 (n=1328)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.337 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.233)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=3252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=3105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.190 (n=1270)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.73 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=2862)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.332 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.243)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=3177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=2730)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.192 (n=2408)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.196 (n=1155)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.438 (n=576)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `3895.4216` → IC=+0.446 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3895.4216 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.441 (n=253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.442 (n=169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.453 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `14878.5401` → IC=+0.441 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14878.5401 (IC base=+0.440)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.446 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.465 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.434)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `3369.9988` → IC=+0.450 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3369.9988 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.405 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.409 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.417 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.418 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.406)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `6345.2155` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 6345.2155
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.203 (n=41613)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=18364)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=7166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=5764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.197 (n=7898)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=3729)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.268 (n=4257)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=3078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=7596)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=3763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.270 (n=2564)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6901)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=2744)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=2984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=3189)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=6401)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.124 (n=5942)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.19 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=6145)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.49` → IC=+0.137 (n=5915)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.49 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=3216)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.126 (n=2949)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.16 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=3060)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=3912)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.19` → IC=+0.144 (n=2940)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.19 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.184 (n=3185)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.38 (IC base=+0.112)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.130 (n=3376)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 4.96 (IC base=+0.112)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.134 (n=2988)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.112)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=1354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.290 (n=1278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `4184.0589` → IC=+0.306 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4184.0589 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.289 (n=601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.333 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `4327.0852` → IC=+0.295 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4327.0852 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=435)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.297 (n=643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1713.4258` → IC=+0.309 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1713.4258 (IC base=+0.289)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.439 (n=508)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.444 (n=285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=280)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.457 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.441 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.454 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `2152.0985` → IC=+0.456 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2152.0985 (IC base=+0.443)

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
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=62)

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
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=62)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4871` → IC=+0.130 (n=9983)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4871 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9838` → IC=+0.243 (n=3329)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9838 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2151` → IC=+0.255 (n=2235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2151 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.183 (n=3796)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2103` → IC=+0.250 (n=2791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2103 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6156` → IC=+0.254 (n=2791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6156 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.3018` → IC=+0.226 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3018 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.3274` → IC=+0.219 (n=3164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3274 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5676` → IC=+0.137 (n=12113)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.5676 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.5895` → IC=+0.203 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5895 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.1486` → IC=+0.176 (n=4015)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1486 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `1.1934` → IC=+0.178 (n=4399)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.1934 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.219 (n=2113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `1.8725` → IC=+0.196 (n=5032)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.8725 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.198 (n=7546)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.213 (n=7342)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 117.0 (IC base=+0.069)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.217 (n=746)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.186 (n=743)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0081 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3505` → IC=+0.184 (n=2227)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3505 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.190 (n=1081)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.185 (n=1488)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 11.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.278 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.209` → IC=+0.286 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.209 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.221 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.181 (n=2104)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=2284)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2042.27` → IC=+0.188 (n=742)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2042.27 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.242 (n=1586)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.1255` → IC=+0.267 (n=779)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1255 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0604` → IC=+0.284 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0604 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.49` → IC=+0.247 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.49 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.403` → IC=+0.237 (n=1849)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.403 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` < `0.0939` → IC=+0.230 (n=1557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0939 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.259 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.5977` → IC=+0.245 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5977 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1593.12` → IC=+0.244 (n=1769)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1593.12 (IC base=+0.232)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.237 (n=773)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.244 (n=773)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=1846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9789` → IC=+0.260 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9789 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.1866` → IC=+0.217 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1866 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.3447` → IC=+0.220 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3447 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.779` → IC=+0.257 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.779 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `1.2501` → IC=+0.221 (n=1757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2501 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `0.6161` → IC=+0.221 (n=1757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6161 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.237 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.4155` → IC=+0.242 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4155 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `16018.063` → IC=+0.218 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16018.063 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.184 (n=589)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0026 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0741` → IC=+0.165 (n=589)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0741 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7204` → IC=+0.173 (n=1765)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.7204 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1267` → IC=+0.152 (n=1589)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1267 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.292` → IC=+0.137 (n=282)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 11.292 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.3` → IC=+0.143 (n=1622)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.3 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.147 (n=1765)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2025 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.8505` → IC=+0.137 (n=1177)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.8505 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.170 (n=473)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4485` → IC=+0.149 (n=1654)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4485 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7828` → IC=+0.144 (n=1103)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7828 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.171 (n=695)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 231.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.200 (n=2241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=2357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=2012)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.342` → IC=+0.258 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.342 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.193 (n=1960)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.3482` → IC=+0.201 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3482 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.1652` → IC=+0.206 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1652 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2676)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `1946.6584` → IC=+0.194 (n=1015)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 1946.6584 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.221 (n=1738)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.1763` → IC=+0.221 (n=869)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1763 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=928)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.233 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.237 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.348` → IC=+0.249 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.348 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.7265` → IC=+0.219 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7265 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7565` → IC=+0.221 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7565 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1938.1775` → IC=+0.215 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1938.1775 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.213 (n=1784)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.211)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=120)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2671)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.155 (n=427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0037 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9598` → IC=+0.222 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9598 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.524` → IC=+0.325 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.524 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.904` → IC=+0.174 (n=881)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 4.904 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.332 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8553 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.2251` → IC=+0.329 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2251 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1112` → IC=+0.336 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1112 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.352 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `1.8416` → IC=+0.326 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8416 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.328 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.1014` → IC=+0.156 (n=699)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1014 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.3186` → IC=+0.198 (n=322)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3186 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.152 (n=728)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8471 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2284` → IC=+0.195 (n=185)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2284 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.5219` → IC=+0.162 (n=928)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5219 (IC base=+0.024)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.189 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=411)

- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.194 (n=119)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=364)

- **FILTRO** `ibs_20min` > `0.2381` → IC=-0.126 (n=2695)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=1338)

- **FILTRO** `sigma_ewma_delta_pct` > `8.79` → IC=-0.219 (n=425)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.79
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=3608)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.201 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `1.6532` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6532 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.333` → IC=+0.134 (n=170)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.333 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.266 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8803 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `0.6436` → IC=+0.277 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6436 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1482` → IC=+0.285 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1482 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `2.5444` → IC=+0.281 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5444 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.279 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.2381` → IC=+0.131 (n=1338)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2381 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.1717` → IC=+0.261 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1717 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.273 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` > `1.1776` → IC=+0.242 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1776 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.1602` → IC=+0.316 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1602 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.4034` → IC=+0.291 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4034 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6434` → IC=-0.175 (n=706)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6434
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2124)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.202 (n=679)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2151)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.209 (n=1031)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=3154)

- **PATRÓN** `dist_vwap_pct` > `0.7916` → IC=+0.317 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7916 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.193` → IC=+0.318 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.193 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` < `0.9855` → IC=+0.291 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9855 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.637` → IC=+0.310 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.637 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.300 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.442` → IC=+0.296 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.442 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.8324` → IC=+0.299 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8324 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.8622` → IC=+0.284 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8622 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` < `0.722` → IC=+0.248 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.722 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` > `1.0723` → IC=+0.269 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0723 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.0997` → IC=+0.262 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0997 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.141` → IC=+0.255 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.141 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.418` → IC=+0.250 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.418 (IC base=-0.015)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.200 (n=4334)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.471` → IC=+0.188 (n=11605)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.471 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.9951` → IC=+0.288 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9951 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.681` → IC=+0.158 (n=5923)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.681 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.1783` → IC=+0.246 (n=4732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1783 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.6141` → IC=+0.252 (n=4731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6141 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` < `0.0805` → IC=+0.241 (n=6998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0805 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.263 (n=1089)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.6398` → IC=+0.255 (n=2546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6398 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.276 (n=7183)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.166 (n=4193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0091 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.5465` → IC=+0.157 (n=11066)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5465 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.6946` → IC=+0.250 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6946 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.237` → IC=+0.247 (n=3630)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.237 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `0.7068` → IC=+0.248 (n=1670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7068 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.195` → IC=+0.259 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.195 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2419` → IC=+0.300 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2419 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.5898` → IC=+0.278 (n=2304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5898 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `2.2839` → IC=+0.266 (n=2373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2839 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.280 (n=5127)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.073)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2584` → IC=-0.157 (n=900)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2584
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2707)

- **FILTRO** `ibs_20min` > `0.7615` → IC=-0.174 (n=737)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7615
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2213)

- **FILTRO** `sigma_ewma_delta_pct` > `4.579` → IC=-0.173 (n=664)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.579
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2286)

- **PATRÓN** `ibs_20min` > `0.9053` → IC=+0.280 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9053 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.223` → IC=+0.197 (n=639)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 7.223 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2262` → IC=+0.273 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2262 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4401` → IC=+0.206 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4401 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.189` → IC=+0.233 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.189 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.231 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.0963` → IC=+0.427 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0963 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2231` → IC=+0.427 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2231 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4828` → IC=+0.439 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4828 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.5328` → IC=+0.426 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5328 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.433 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8641` → IC=+0.159 (n=870)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.8641 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.1104` → IC=+0.188 (n=664)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1104 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6747` → IC=+0.177 (n=1092)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6747 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.166 (n=1124)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.220 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4262` → IC=+0.194 (n=400)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4262 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.4378` → IC=+0.184 (n=400)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.4378 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.224 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 230.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1458` → IC=+0.223 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1458 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.611` → IC=+0.224 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.611 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.221 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2686` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2686 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.4389` → IC=+0.230 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4389 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1685` → IC=+0.234 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1685 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.271 (n=1980)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.255 (n=1776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.251 (n=1770)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.778` → IC=+0.281 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.778 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.264 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `1.6236` → IC=+0.258 (n=1891)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6236 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=2343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `2009.7484` → IC=+0.272 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.7484 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.325 (n=745)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1799` → IC=+0.300 (n=724)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1799 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.321 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.3571` → IC=+0.293 (n=1644)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3571 (IC base=+0.287)

- **PATRÓN** `ibs_20min` > `0.1` → IC=+0.288 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.689` → IC=+0.292 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.689 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.1942` → IC=+0.282 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1942 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.1195` → IC=+0.291 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1195 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.7249` → IC=+0.299 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7249 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.6774` → IC=+0.297 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6774 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1931.867` → IC=+0.309 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1931.867 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.289 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.287)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7704` → IC=-0.186 (n=750)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7704
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=2253)

- **PATRÓN** `ibs_20min` > `0.9035` → IC=+0.174 (n=677)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.9035 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3855` → IC=+0.232 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3855 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.0082` → IC=+0.251 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0082 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.1688` → IC=+0.236 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1688 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.0824` → IC=+0.247 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0824 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4078` → IC=+0.265 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4078 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `141.0` → IC=+0.260 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 141.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.1267` → IC=+0.232 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1267 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.176` → IC=+0.216 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.176 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.169` → IC=+0.270 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.169 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8295` → IC=+0.266 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8295 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.251 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.76` → IC=-0.185 (n=1377)

  - _Acción_: SKIP cuando `ibs_20min` < 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.284 (n=1382)

- **FILTRO** `ibs_20min` > `0.6744` → IC=-0.242 (n=693)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6744
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=2082)

- **FILTRO** `sigma_ewma_delta_pct` > `4.818` → IC=-0.204 (n=589)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.818
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=2186)

- **PATRÓN** `ibs_20min` > `0.76` → IC=+0.284 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.76 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.213` → IC=+0.317 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.213 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.678` → IC=+0.171 (n=436)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.678 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.310 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.303 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6398 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.301 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.306 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.4244` → IC=+0.319 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4244 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.322 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.133 (n=1832)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5714 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.267` → IC=+0.241 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.267 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.269 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.1845` → IC=+0.232 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1845 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.069` → IC=+0.259 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.069 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.4118` → IC=+0.250 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4118 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.261 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.020)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.328 (n=1430)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.284)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.304 (n=755)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `0.6494` → IC=+0.317 (n=1597)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6494 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2129` → IC=+0.318 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2129 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.755` → IC=+0.310 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.755 (IC base=+0.284)

- **PATRÓN** `volumen_regimen` > `0.6276` → IC=+0.298 (n=1597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6276 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.331 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.296 (n=1526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=1581)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2474.544` → IC=+0.296 (n=1427)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2474.544 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.322 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.314 (n=1127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.1933` → IC=+0.283 (n=745)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1933 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.289 (n=1607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.308 (n=1693)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.3086` → IC=+0.294 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3086 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.516` → IC=+0.297 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.516 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` < `0.7178` → IC=+0.284 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7178 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` > `1.2318` → IC=+0.315 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2318 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.2342` → IC=+0.332 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2342 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.292 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.1396` → IC=+0.282 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1396 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2429.1954` → IC=+0.288 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2429.1954 (IC base=+0.283)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.187 (n=3264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0048 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.206 (n=3252)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.3576` → IC=+0.184 (n=8581)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3576 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=10150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.226 (n=9752)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1712` → IC=+0.197 (n=4207)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1712 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.406` → IC=+0.253 (n=1964)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.406 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.2075` → IC=+0.167 (n=6486)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2075 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6293` → IC=+0.163 (n=6485)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6293 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.197 (n=1450)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.173 (n=4134)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6037` → IC=+0.182 (n=3131)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6037 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `1978.841` → IC=+0.176 (n=8710)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1978.841 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.189 (n=8674)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 106.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.187 (n=6213)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0066 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.0805` → IC=+0.219 (n=3107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0805 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=3570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.4865` → IC=+0.229 (n=9311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4865 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` < `0.1689` → IC=+0.167 (n=6474)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1689 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.303` → IC=+0.195 (n=1564)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.303 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1775` → IC=+0.161 (n=6676)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1775 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2915` → IC=+0.214 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2915 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.5572` → IC=+0.173 (n=3791)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5572 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6138` → IC=+0.175 (n=2872)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6138 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.181 (n=8273)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 107.0 (IC base=+0.173)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.246 (n=550)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.204 (n=548)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3418` → IC=+0.220 (n=1639)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3418 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1728)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.206 (n=1097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.9141` → IC=+0.287 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9141 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.239` → IC=+0.330 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.239 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.243 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4332` → IC=+0.196 (n=1532)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4332 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2043.02` → IC=+0.203 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2043.02 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.250 (n=1091)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.246 (n=1238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1033` → IC=+0.299 (n=545)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1033 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.252 (n=1189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.1034` → IC=+0.278 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1034 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.394` → IC=+0.242 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.394 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.234` → IC=+0.248 (n=1340)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.234 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.262 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4205` → IC=+0.266 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4205 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.6147` → IC=+0.240 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6147 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.244 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1592.8005` → IC=+0.257 (n=1238)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1592.8005 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.227 (n=489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.0691` → IC=+0.194 (n=488)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0691 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=1542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.3933` → IC=+0.223 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3933 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.141` → IC=+0.202 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.141 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.528` → IC=+0.230 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.528 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6882` → IC=+0.167 (n=644)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6882 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.195 (n=231)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.413` → IC=+0.181 (n=475)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.413 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `11950.6339` → IC=+0.159 (n=1306)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11950.6339 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `382.0` → IC=+0.159 (n=1221)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 382.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.162 (n=1538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.2957` → IC=+0.165 (n=1536)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2957 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.173 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=724)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.5914` → IC=+0.195 (n=1536)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5914 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.168 (n=1519)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.883` → IC=+0.195 (n=303)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.883 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.160 (n=1536)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2116 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.2271` → IC=+0.144 (n=1575)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.2271 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.0697` → IC=+0.147 (n=689)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0697 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4679` → IC=+0.151 (n=1424)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4679 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.176 (n=449)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 208.0 (IC base=+0.142)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.231 (n=544)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2464` → IC=+0.220 (n=1085)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2464 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.488` → IC=+0.282 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.488 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.1273` → IC=+0.210 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1273 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.7237` → IC=+0.218 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7237 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2009.4584` → IC=+0.216 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.4584 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.241 (n=1231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1429` → IC=+0.261 (n=616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1429 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.278 (n=484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` < `0.3509` → IC=+0.248 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3509 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.666` → IC=+0.253 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.666 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.3529` → IC=+0.259 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3529 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.7484` → IC=+0.237 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7484 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.1709` → IC=+0.226 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1709 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `1933.4584` → IC=+0.228 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.4584 (IC base=+0.223)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.217 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.223)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.183 (n=1379)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0065 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.4208` → IC=+0.166 (n=1567)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4208 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.3395` → IC=+0.205 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3395 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1416` → IC=+0.187 (n=1024)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1416 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.221 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.164 (n=1045)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.856 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.173 (n=655)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4294` → IC=+0.169 (n=512)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4294 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.5215` → IC=+0.162 (n=512)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.5215 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `5109.0415` → IC=+0.193 (n=1045)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 5109.0415 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.154 (n=1503)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 152.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.157 (n=1634)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0071 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3831` → IC=+0.146 (n=1633)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3831 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6656` → IC=+0.179 (n=1633)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6656 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1497` → IC=+0.147 (n=1595)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1497 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.869` → IC=+0.164 (n=566)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.869 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.153 (n=1089)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8554 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.182 (n=243)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.8136` → IC=+0.138 (n=1006)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8136 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5362` → IC=+0.132 (n=503)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.5362 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `4262.9422` → IC=+0.158 (n=1089)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4262.9422 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.122 (n=1447)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 151.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.159 (n=810)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.01 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.453` → IC=+0.127 (n=1570)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.453 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=1820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.5045` → IC=+0.214 (n=1784)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5045 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `1.0671` → IC=+0.216 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0671 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.864` → IC=+0.261 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.864 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.2085` → IC=+0.137 (n=1784)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2085 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.647` → IC=+0.132 (n=1784)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.647 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1624` → IC=+0.133 (n=1793)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1624 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.128 (n=742)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5391` → IC=+0.144 (n=759)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5391 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=1864)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2388.5554` → IC=+0.182 (n=1189)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2388.5554 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.144 (n=1426)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 47.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.160 (n=789)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0062 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.103` → IC=+0.173 (n=598)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.103 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=1809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5789` → IC=+0.217 (n=1793)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5789 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.9994` → IC=+0.123 (n=234)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.9994 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.198` → IC=+0.147 (n=1648)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.198 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.338` → IC=+0.130 (n=547)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 5.338 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.6382` → IC=+0.152 (n=599)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6382 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2277` → IC=+0.157 (n=313)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2277 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.139 (n=547)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4234` → IC=+0.127 (n=547)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4234 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2743.5149` → IC=+0.182 (n=813)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2743.5149 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.127 (n=1595)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 52.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.228 (n=1673)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.2904` → IC=+0.216 (n=1116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2904 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.245 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.1984` → IC=+0.215 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1984 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.245 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.1935` → IC=+0.211 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1935 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.218 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6237 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.269 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.47` → IC=+0.212 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.47 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4217` → IC=+0.214 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4217 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1633)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2466.2754` → IC=+0.209 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2466.2754 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.228 (n=755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.217 (n=778)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0924` → IC=+0.239 (n=572)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0924 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.235 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.4279` → IC=+0.243 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4279 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `1.1799` → IC=+0.231 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1799 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.355` → IC=+0.250 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.355 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.6365` → IC=+0.223 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6365 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.273 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `2.2062` → IC=+0.204 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2062 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4369` → IC=+0.212 (n=1569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4369 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2407.4354` → IC=+0.218 (n=1532)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.4354 (IC base=+0.212)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.191 (n=1127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0042 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.169 (n=854)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0084 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3428` → IC=+0.178 (n=2252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3428 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=1264)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.3438` → IC=+0.196 (n=2559)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3438 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.7962` → IC=+0.189 (n=406)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.7962 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.754` → IC=+0.195 (n=1121)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.754 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.189 (n=1521)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8725 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.176 (n=761)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.2084 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1631` → IC=+0.176 (n=683)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1631 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4373` → IC=+0.184 (n=828)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4373 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.8208` → IC=+0.173 (n=1655)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8208 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=2908)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2681.708` → IC=+0.169 (n=2287)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2681.708 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.187 (n=2337)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 143.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.152 (n=878)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0037 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.191 (n=878)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0714 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.144 (n=850)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2742.8483` → IC=+0.124 (n=2347)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2742.8483 (IC base=+0.106)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.124 (n=1106)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 28.0 (IC base=+0.106)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.198 (n=303)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0028 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.3311` → IC=+0.165 (n=684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3311 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.183 (n=632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.6364` → IC=+0.205 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6364 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.2868` → IC=+0.170 (n=237)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.2868 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1178` → IC=+0.144 (n=554)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1178 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.181` → IC=+0.166 (n=297)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.181 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.952` → IC=+0.144 (n=718)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.952 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.892` → IC=+0.172 (n=456)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.892 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.1571` → IC=+0.147 (n=712)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.1571 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.147 (n=270)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.2382` → IC=+0.150 (n=587)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.2382 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.5157` → IC=+0.152 (n=595)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5157 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `10742.0445` → IC=+0.153 (n=684)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 10742.0445 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.192 (n=290)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 154.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.206 (n=277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3449` → IC=+0.161 (n=820)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3449 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.147 (n=791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.144 (n=826)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.181 (n=722)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6112 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1811` → IC=+0.155 (n=809)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1811 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.074` → IC=+0.146 (n=750)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.074 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.218` → IC=+0.145 (n=820)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.218 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.153 (n=733)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.693 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1607` → IC=+0.194 (n=220)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1607 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1178` → IC=+0.157 (n=713)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1178 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4135` → IC=+0.147 (n=810)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4135 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=1062)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `11946.3416` → IC=+0.143 (n=733)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 11946.3416 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `356.0` → IC=+0.151 (n=789)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 356.0 (IC base=+0.140)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.244 (n=534)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.3984` → IC=+0.215 (n=801)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3984 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.6741` → IC=+0.252 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6741 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.365` → IC=+0.217 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.365 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.2089` → IC=+0.208 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2089 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.096` → IC=+0.226 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.096 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.8419` → IC=+0.215 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8419 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.182` → IC=+0.221 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.182 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.1552` → IC=+0.235 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1552 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.241 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4208 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.4387` → IC=+0.233 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4387 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.123 (n=515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 11.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.087` → IC=+0.144 (n=251)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.087 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.6868` → IC=+0.140 (n=331)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6868 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.130 (n=117)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `7843.9331` → IC=+0.133 (n=502)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 7843.9331 (IC base=+0.094)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4762` → IC=-0.122 (n=265)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4762
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=517)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.157 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0071 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.171 (n=609)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0051 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.5376` → IC=+0.159 (n=607)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.5376 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 8.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.275 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.9532` → IC=+0.239 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9532 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.363` → IC=+0.218 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.363 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.0661` → IC=+0.175 (n=534)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0661 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.6528` → IC=+0.165 (n=607)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6528 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.17` → IC=+0.167 (n=169)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.17 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4594` → IC=+0.162 (n=196)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4594 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.1945` → IC=+0.172 (n=266)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1945 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.162 (n=642)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `3079.1777` → IC=+0.193 (n=203)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3079.1777 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.4762` → IC=+0.147 (n=517)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.4762 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` < `1.4649` → IC=+0.135 (n=187)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4649 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `2868.2407` → IC=+0.153 (n=266)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2868.2407 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.126 (n=359)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 23.0 (IC base=+0.056)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.172 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0238 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.188 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.007 (IC base=+0.155)

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

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.177 (n=190)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6182 (IC base=+0.155)

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
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.178 (n=4218)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0046 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.210 (n=4199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=13156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.9938` → IC=+0.308 (n=4199)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9938 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.9094` → IC=+0.200 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9094 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.37` → IC=+0.249 (n=3109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.37 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `0.88` → IC=+0.172 (n=5630)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.88 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.200 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.5891` → IC=+0.197 (n=4060)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5891 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1811.5082` → IC=+0.179 (n=12597)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1811.5082 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.202 (n=9905)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.195 (n=4992)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1478` → IC=+0.193 (n=4984)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1478 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=4278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.4529` → IC=+0.246 (n=9968)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4529 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2436` → IC=+0.163 (n=7051)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2436 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.05` → IC=+0.201 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.05 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.729` → IC=+0.184 (n=10936)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.729 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.7048` → IC=+0.163 (n=3382)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7048 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.246 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6094` → IC=+0.191 (n=3520)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6094 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1742.9232` → IC=+0.183 (n=11328)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1742.9232 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.205 (n=6866)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.246 (n=700)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.226 (n=699)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.3577` → IC=+0.210 (n=2094)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3577 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.223 (n=1013)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=1407)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.330 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.666` → IC=+0.352 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.666 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2273` → IC=+0.259 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2273 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.2375` → IC=+0.215 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2375 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2042.3486` → IC=+0.219 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.3486 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.223 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.262 (n=1143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.261 (n=1711)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1254` → IC=+0.282 (n=752)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1254 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3606` → IC=+0.283 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3606 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.511` → IC=+0.263 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.511 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.290 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.549` → IC=+0.256 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.549 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.622` → IC=+0.275 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.622 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=1872)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1592.66` → IC=+0.269 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1592.66 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.209 (n=676)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1817` → IC=+0.162 (n=1346)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1817 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=2110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.2865` → IC=+0.204 (n=2018)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2865 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1246` → IC=+0.185 (n=1144)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1246 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.754` → IC=+0.180 (n=339)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.754 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.2` → IC=+0.149 (n=1845)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.2 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.7006` → IC=+0.167 (n=888)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.7006 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.197 (n=288)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1361` → IC=+0.159 (n=1726)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1361 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5137` → IC=+0.152 (n=1752)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5137 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `277.0` → IC=+0.173 (n=835)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 277.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1688)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.3291` → IC=+0.159 (n=1688)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3291 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.150 (n=769)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.2923` → IC=+0.240 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2923 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1297` → IC=+0.163 (n=1538)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1297 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.518` → IC=+0.154 (n=284)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.518 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.315` → IC=+0.147 (n=1534)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.315 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.1894` → IC=+0.159 (n=1688)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1894 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1533` → IC=+0.200 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1533 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.156 (n=1589)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7717` → IC=+0.158 (n=1059)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7717 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `347.0` → IC=+0.145 (n=995)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 347.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.255 (n=687)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=1853)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.839` → IC=+0.294 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.839 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.2057` → IC=+0.223 (n=2072)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2057 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.6213` → IC=+0.228 (n=1982)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6213 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2458)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1946.6584` → IC=+0.231 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1946.6584 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.242 (n=1702)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1786` → IC=+0.247 (n=851)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1786 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0146` → IC=+0.302 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0146 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.177` → IC=+0.275 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.177 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3426` → IC=+0.293 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3426 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.735` → IC=+0.237 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.735 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1534` → IC=+0.241 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1534 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1933.251` → IC=+0.247 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.251 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.235 (n=1744)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.195 (n=953)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0039 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4326` → IC=+0.154 (n=2154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4326 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2715` → IC=+0.189 (n=2154)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2715 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3551` → IC=+0.160 (n=828)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3551 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.581` → IC=+0.166 (n=348)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.581 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8735` → IC=+0.163 (n=1436)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8735 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2358` → IC=+0.188 (n=389)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2358 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5213` → IC=+0.162 (n=922)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5213 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1724` → IC=+0.154 (n=950)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1724 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7469.8444` → IC=+0.232 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7469.8444 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.179 (n=686)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 71.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.166 (n=1154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0051 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3527` → IC=+0.137 (n=1522)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.3527 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=800)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.5979` → IC=+0.196 (n=1522)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5979 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1516` → IC=+0.132 (n=1513)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1516 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.292` → IC=+0.162 (n=261)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.292 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6226` → IC=+0.143 (n=578)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6226 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.226 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.140 (n=1656)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `9123.6009` → IC=+0.200 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9123.6009 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `168.0` → IC=+0.130 (n=1653)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 168.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.134 (n=2163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0057 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.5664` → IC=+0.129 (n=2162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.5664 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.4621` → IC=+0.202 (n=2162)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4621 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `1.0536` → IC=+0.213 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0536 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.567` → IC=+0.246 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.567 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8923` → IC=+0.150 (n=1442)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8923 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1609` → IC=+0.129 (n=2228)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1609 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.456` → IC=+0.128 (n=2105)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.456 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2198)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2550.0226` → IC=+0.233 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2550.0226 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.145 (n=1338)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 42.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.182 (n=687)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0057 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1315` → IC=+0.164 (n=686)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1315 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=2119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5128` → IC=+0.235 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5128 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.217` → IC=+0.139 (n=1700)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.217 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.486` → IC=+0.131 (n=1984)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.486 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.645` → IC=+0.166 (n=686)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.645 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.221` → IC=+0.185 (n=328)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.221 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `2.1505` → IC=+0.136 (n=1663)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1505 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2799.1755` → IC=+0.197 (n=685)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2799.1755 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.136 (n=1649)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 50.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.230 (n=2112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.217 (n=1527)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.262 (n=1894)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.208` → IC=+0.234 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.208 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.264` → IC=+0.268 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.264 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.2365` → IC=+0.216 (n=2111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2365 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.64` → IC=+0.221 (n=2111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.64 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.244 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.5063` → IC=+0.244 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5063 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=2035)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2464.3002` → IC=+0.219 (n=1886)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2464.3002 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.219 (n=739)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.229 (n=1004)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.226 (n=1568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.260 (n=1951)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `1.2129` → IC=+0.217 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2129 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.212` → IC=+0.215 (n=1962)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.212 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.844` → IC=+0.251 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.844 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `1.2298` → IC=+0.236 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2298 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.279 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4285` → IC=+0.209 (n=2025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4285 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2414.1306` → IC=+0.214 (n=1978)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2414.1306 (IC base=+0.211)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.164 (n=3720)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.222 (n=1237)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.5039` → IC=+0.193 (n=3703)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.5039 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=1392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.183 (n=1691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.9415` → IC=+0.240 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9415 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.1686` → IC=+0.190 (n=1381)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1686 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.215` → IC=+0.215 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.215 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7117` → IC=+0.188 (n=1122)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.7117 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.8944` → IC=+0.184 (n=1700)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.8944 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.1685` → IC=+0.210 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1685 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.4536` → IC=+0.191 (n=1219)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4536 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.8592` → IC=+0.186 (n=2437)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8592 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=2763)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2917.107` → IC=+0.189 (n=3308)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2917.107 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.218 (n=935)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.4865` → IC=+0.178 (n=2802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.4865 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=1266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.1827` → IC=+0.186 (n=1233)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1827 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.657` → IC=+0.182 (n=523)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.657 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` < `0.2353` → IC=+0.155 (n=2487)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.2353 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.212` → IC=+0.171 (n=2795)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.212 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.2562` → IC=+0.167 (n=2638)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2562 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.168 (n=2559)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.5357` → IC=+0.171 (n=1218)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5357 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.8264` → IC=+0.173 (n=1844)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8264 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=3720)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `5122.641` → IC=+0.165 (n=2503)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5122.641 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.168 (n=1825)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 85.0 (IC base=+0.162)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.232 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0811` → IC=+0.260 (n=173)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0811 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.214 (n=236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.5157` → IC=+0.229 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5157 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.7635` → IC=+0.212 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7635 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.3179` → IC=+0.217 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3179 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.039` → IC=+0.226 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.039 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.554` → IC=+0.211 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.554 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.219 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.5963` → IC=+0.218 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5963 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.231 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `12563.2849` → IC=+0.236 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12563.2849 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.229 (n=467)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.366` → IC=+0.165 (n=1056)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.366 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.198 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 4.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.1485` → IC=+0.181 (n=465)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1485 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.153 (n=479)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6084 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6649` → IC=+0.189 (n=101)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6649 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.2114` → IC=+0.151 (n=1071)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2114 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.38` → IC=+0.168 (n=1038)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.38 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.188 (n=704)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8812 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2218` → IC=+0.180 (n=220)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2218 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.5397` → IC=+0.157 (n=1052)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.5397 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.825` → IC=+0.167 (n=701)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.825 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11518.9437` → IC=+0.162 (n=1056)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11518.9437 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `696.0` → IC=+0.160 (n=1010)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 696.0 (IC base=+0.149)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.218 (n=392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.1516` → IC=+0.211 (n=517)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1516 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.194 (n=537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` < `0.5225` → IC=+0.203 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5225 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `0.8839` → IC=+0.195 (n=392)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.8839 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.2041` → IC=+0.202 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2041 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.171` → IC=+0.199 (n=1056)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 4.171 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `1.0845` → IC=+0.195 (n=1033)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.0845 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` > `1.2457` → IC=+0.193 (n=392)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 1.2457 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.192 (n=1078)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.204 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `2.4736` → IC=+0.197 (n=1151)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.4736 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=1182)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.191)

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

- **PATRÓN** `dist_vwap_pct` < `0.2152` → IC=+0.166 (n=874)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.2152 (IC base=+0.165)

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
- **PATRÓN** `sigma_h` < `0.011` → IC=+0.160 (n=327)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.011 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.162 (n=365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 3.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.134 (n=378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 14.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.5833` → IC=+0.189 (n=332)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5833 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.5213` → IC=+0.210 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5213 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.7119` → IC=+0.187 (n=164)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.7119 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.282` → IC=+0.135 (n=124)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.282 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.220 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `2.4285` → IC=+0.189 (n=120)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4285 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=440)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2958.069` → IC=+0.160 (n=372)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2958.069 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.147 (n=355)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 60.0 (IC base=+0.134)

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
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.164 (n=527)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0038 (IC base=+0.083)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.126 (n=548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 16.0 (IC base=+0.083)

- **PATRÓN** `ibs_20min` > `0.6473` → IC=+0.180 (n=987)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6473 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.1411` → IC=+0.146 (n=605)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1411 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.465` → IC=+0.191 (n=257)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.465 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.2771` → IC=+0.193 (n=151)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2771 (IC base=+0.083)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.121 (n=460)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0056 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.2296` → IC=+0.262 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2296 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.1925` → IC=+0.135 (n=489)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1925 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.082` → IC=+0.148 (n=373)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.082 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.141` → IC=+0.204 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.141 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `2.6035` → IC=+0.155 (n=384)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.6035 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` > `1.7271` → IC=+0.143 (n=256)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7271 (IC base=+0.054)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.140 (n=409)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0057 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.120 (n=414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.4395` → IC=+0.168 (n=378)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.4395 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1188` → IC=+0.163 (n=203)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1188 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `2.0849` → IC=+0.129 (n=297)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.0849 (IC base=+0.096)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.124 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0053 (IC base=+0.089)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.196 (n=67)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.310 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.0686` → IC=+0.143 (n=208)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.0686 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.876` → IC=+0.175 (n=204)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 6.876 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.5863` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.5863 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `0.8122` → IC=+0.148 (n=140)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.8122 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.182 (n=83)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `2.4384` → IC=+0.158 (n=188)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4384 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `1.7169` → IC=+0.138 (n=125)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.7169 (IC base=+0.089)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=165)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.154 (n=264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0047 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.133 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.219 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7143 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.1242` → IC=+0.180 (n=201)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1242 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.853` → IC=+0.291 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.853 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `0.8` → IC=+0.137 (n=243)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `1.7849` → IC=+0.146 (n=207)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.7849 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `1136.0742` → IC=+0.153 (n=321)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1136.0742 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.7041` → IC=+0.149 (n=129)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.7041 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.005)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.011` → IC=-0.245 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=136)

- **FILTRO** `ibs_20min` > `0.1176` → IC=-0.266 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1176
  - _Potencial_: sin este filtro IC_bueno=+0.304 (n=95)

- **PATRÓN** `ibs_20min` > `0.7778` → IC=+0.169 (n=243)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.7778 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.606` → IC=+0.150 (n=78)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 9.606 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2389` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2389 (IC base=+0.053)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.164 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0088 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.1176` → IC=+0.304 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1176 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` < `0.1744` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1744 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.93` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.93 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.84` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.84 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.9843` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.9843 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.1346` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1346 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.201 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5975 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` > `1.8705` → IC=+0.212 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8705 (IC base=+0.046)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.188 (n=75)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.06 (IC base=+0.046)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.241 (n=160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=83)

- **FILTRO** `dist_vwap_pct` > `0.2381` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=228)

- **FILTRO** `volumen_regimen` < `0.7363` → IC=-0.355 (n=60)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7363
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=183)

- **FILTRO** `sigma_h` > `0.0057` → IC=-0.368 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=157)

- **FILTRO** `ibs_20min` > `0.92` → IC=-0.330 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` > 0.92
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=157)

- **FILTRO** `dist_vwap_pct` > `0.3328` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3328
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=175)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=97)

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
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=65)

- **FILTRO** `ibs_20min` > `0.92` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` > 0.92
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=65)

- **FILTRO** `sigma_ewma_delta_pct` > `2.482` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.482
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=56)

- **FILTRO** `volumen_regimen` > `0.8507` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8507
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=65)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.7738` → IC=-0.402 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7738
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.370 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=56)

- **FILTRO** `ibs_20min` > `0.5972` → IC=-0.350 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5972
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=39)

- **FILTRO** `libro_liquidez` < `1289.9986` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 1289.9986
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=52)

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
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.179 (n=163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0058 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.134 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.6438` → IC=+0.144 (n=358)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6438 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.4828` → IC=+0.199 (n=81)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.4828 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `1.4189` → IC=+0.148 (n=86)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4189 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.135 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 14.0 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.179 (n=322)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.156 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.664` → IC=+0.214 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.664 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` < `2.6699` → IC=+0.130 (n=290)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.6699 (IC base=+0.083)

- **PATRÓN** `libro_liquidez` > `3965.7979` → IC=+0.191 (n=166)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3965.7979 (IC base=+0.083)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6295` → IC=-0.278 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6295
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=104)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.185 (n=147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0024 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.223 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.215 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1435 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.1046` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1046 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.332` → IC=+0.181 (n=133)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 4.332 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.1443` → IC=+0.161 (n=163)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1443 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.6733` → IC=+0.169 (n=146)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.6733 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.1891` → IC=+0.214 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1891 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.6869` → IC=+0.202 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6869 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.179 (n=132)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `4587.7919` → IC=+0.167 (n=109)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4587.7919 (IC base=+0.153)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_liquidez` < `1558.1749` → IC=-0.147 (n=49)

  - _Acción_: SKIP cuando `libro_liquidez` < 1558.1749
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=102)

- **FILTRO** `ibs_20min` > `0.2038` → IC=-0.127 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2038
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=112)

- **PATRÓN** `volumen_spike_ratio` < `1.8267` → IC=+0.123 (n=59)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.8267 (IC base=+0.049)

- **PATRÓN** `libro_liquidez` > `1558.1749` → IC=+0.144 (n=102)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1558.1749 (IC base=+0.049)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.148 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 12.0 (IC base=+0.061)

- **PATRÓN** `ibs_20min` < `0.2038` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.2038 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` < `0.8316` → IC=+0.121 (n=85)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 0.8316 (IC base=+0.061)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.0941` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0941
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=31)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.281 (n=94)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.248 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.223 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7333 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.9298` → IC=+0.229 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9298 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.6353` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6353 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` < `0.1348` → IC=+0.225 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1348 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.379` → IC=+0.273 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.379 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `1.0151` → IC=+0.264 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0151 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.089` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.089 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.354 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.225 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.662` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.662 (IC base=-0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.0941` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0941 (IC base=-0.034)

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
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.120 (n=1127)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.495 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2929.6426` → IC=+0.156 (n=324)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2929.6426 (IC base=+0.109)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.120 (n=1127)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.495 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2929.6426` → IC=+0.156 (n=324)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2929.6426 (IC base=+0.109)

### LIQUIDACIONES_15M
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
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=2507)

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

- **PATRÓN** `liq_usd_total` > `129721.58` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `liq_usd_total` > 129721.58 (IC base=+0.061)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=157)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.061)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=990)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=944)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=583)

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
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=289)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.179 (n=104)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.495 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `3946.3264` → IC=+0.141 (n=104)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3946.3264 (IC base=+0.034)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=752)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=752)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.131 (n=242)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=590)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=486)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=486)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=120)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=144)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=241)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=117)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=130)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=290)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=290)

- **FILTRO** `libro_liquidez` < `553.2637` → IC=-0.136 (n=105)

  - _Acción_: SKIP cuando `libro_liquidez` < 553.2637
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=215)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=175)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.48` → IC=-0.120 (n=1394)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=768)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.125 (n=134)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=71)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.149 (n=75)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=199)

- **PATRÓN** `py_entrada` < `0.48` → IC=+0.138 (n=92)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.48 (IC base=+0.018)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.043)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.125 (n=86)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=55)

- **FILTRO** `restante_min` < `10.05` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `restante_min` < 10.05
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=95)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.167 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=98)

- **FILTRO** `lag_apertura_s` > `290.6` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `lag_apertura_s` > 290.6
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=94)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.189 (n=43)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=106)

- **FILTRO** `restante_min` < `3.99` → IC=-0.133 (n=107)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **FILTRO** `lag_apertura_s` > `60.75` → IC=-0.137 (n=111)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.75
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=38)

- **PATRÓN** `py_entrada` < `0.49` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.49 (IC base=+0.081)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.155 (n=140)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.173 (n=47)

- **FILTRO** `profundidad_ratio` < `54.8` → IC=-0.230 (n=61)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.8
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=126)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=157)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.239 (n=44)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=199)

- **FILTRO** `restante_min` < `3.43` → IC=-0.220 (n=80)

  - _Acción_: SKIP cuando `restante_min` < 3.43
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=163)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.172 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=187)

- **FILTRO** `lag_apertura_s` > `92.29` → IC=-0.202 (n=82)

  - _Acción_: SKIP cuando `lag_apertura_s` > 92.29
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=161)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.156 (n=155)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=86)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.148 (n=86)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` > 0.5 (IC base=-0.047)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.222 (n=77)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=216)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.162 (n=4450)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=13500)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.164 (n=4640)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=13930)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.195 (n=786)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2393)

- **PATRÓN** `libro_liquidez` > `1806.8572` → IC=+0.132 (n=1081)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1806.8572 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1581.1195` → IC=+0.145 (n=1129)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1581.1195 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.180 (n=785)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=2440)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=780)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=2587)

- **PATRÓN** `libro_liquidez` > `1803.3703` → IC=+0.132 (n=1097)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1803.3703 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.162 (n=764)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=2405)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2434)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3174)

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
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=283)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1934.3745` → IC=-0.173 (n=325)

  - _Acción_: SKIP cuando `libro_liquidez` < 1934.3745
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=662)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=12616)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=27862)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=9510)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=30968)

- **FILTRO** `ibs_7min` < `0.2614` → IC=-0.234 (n=10116)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2614
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=30362)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=13693)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=26785)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.235 (n=12497)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=38829)

- **FILTRO** `ibs_7min` > `0.2903` → IC=-0.181 (n=12829)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2903
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=38497)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.140 (n=2052)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4813)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=1643)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=5222)

- **FILTRO** `ibs_7min` < `0.7083` → IC=-0.250 (n=2265)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=4600)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.183 (n=1542)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5323)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.265 (n=2179)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6695)

- **FILTRO** `ibs_7min` > `0.788` → IC=-0.209 (n=2218)

  - _Acción_: SKIP cuando `ibs_7min` > 0.788
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6656)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=1661)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5261)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.249 (n=1699)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=5223)

- **FILTRO** `ibs_7min` < `0.7428` → IC=-0.197 (n=1728)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7428
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=5194)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.177 (n=1715)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=5207)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.266 (n=1656)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5395)

- **FILTRO** `ibs_7min` > `0.2644` → IC=-0.194 (n=1760)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2644
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5291)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.189 (n=1755)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5296)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.162 (n=1866)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=4653)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=1552)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4967)

- **FILTRO** `ibs_7min` < `0.703` → IC=-0.246 (n=2149)

  - _Acción_: SKIP cuando `ibs_7min` < 0.703
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=4370)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.215 (n=1512)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5007)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.244 (n=2169)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=7305)

- **FILTRO** `ibs_7min` > `0.741` → IC=-0.173 (n=2368)

  - _Acción_: SKIP cuando `ibs_7min` > 0.741
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=7106)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=2164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=4491)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.237 (n=1983)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4672)

- **FILTRO** `ibs_7min` < `0.7406` → IC=-0.186 (n=1663)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7406
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4992)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.179 (n=1620)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=5035)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=1696)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=5154)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.180 (n=1712)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5138)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.184 (n=1680)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=5170)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.263 (n=1717)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=5164)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.231 (n=1686)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5195)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=2336)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=7450)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.274 (n=1570)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=5066)

- **FILTRO** `ibs_7min` < `0.2581` → IC=-0.221 (n=1659)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2581
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4977)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.199 (n=1651)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4985)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.210 (n=2152)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=7139)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1207)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=610)

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
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=336)

- **FILTRO** `libro_liquidez` < `3302.3462` → IC=-0.159 (n=162)

  - _Acción_: SKIP cuando `libro_liquidez` < 3302.3462
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=487)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.136 (n=898)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.139 (n=411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `442.4725` → IC=+0.152 (n=300)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 442.4725 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.129 (n=764)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 53.0 (IC base=+0.122)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.167 (n=70)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.224 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `307.527` → IC=+0.141 (n=140)

  - _Acción_: Kelly boost +0.70€ cuando `total_vol_5m` < 307.527 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2602.0106` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2602.0106 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.174 (n=93)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 12.0 (IC base=+0.139)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 10.0 (IC base=+0.110)

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
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.171 (n=162)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.142)

- **PATRÓN** `total_vol_5m` < `8082.459` → IC=+0.161 (n=163)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 8082.459 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 28.0 (IC base=+0.142)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4006` → IC=+0.139 (n=156)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4006 (IC base=+0.098)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.120 (n=156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 13.0 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `3602.5746` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3602.5746 (IC base=+0.098)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.75` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.75
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=114)

- **FILTRO** `sigma_h` > `0.0044` → IC=-0.234 (n=333)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=165)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0052` → IC=-0.262 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=50)

- **FILTRO** `T_h` > `88.6528` → IC=-0.397 (n=37)

  - _Acción_: SKIP cuando `T_h` > 88.6528
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=112)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.269 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=-0.083)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7678` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `pct_vs_K` |x|≤ 1.7678 (IC base=-0.083)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0081` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0081
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `pct_vs_K` |x|> `8.662` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.662
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=34)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.196 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `3.7615` → IC=-0.250 (n=114)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7615
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=345)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.304 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=302)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.314 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=302)

- **FILTRO** `T_h` > `58.2176` → IC=-0.315 (n=301)

  - _Acción_: SKIP cuando `T_h` > 58.2176
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=101)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `68.7654` → IC=-0.145 (n=119)

  - _Acción_: SKIP cuando `T_h` > 68.7654
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=41)

- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.378 (n=39)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=121)

- **FILTRO** `sigma_h` > `0.0056` → IC=-0.327 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=74)

- **FILTRO** `T_h` > `143.6315` → IC=-0.304 (n=49)

  - _Acción_: SKIP cuando `T_h` > 143.6315
  - _Potencial_: sin este filtro IC_bueno=-0.280 (n=98)

- **FILTRO** `T_h` < `96.6729` → IC=-0.340 (n=48)

  - _Acción_: SKIP cuando `T_h` < 96.6729
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=99)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0048` → IC=-0.267 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=87)

- **FILTRO** `T_h` > `135.9851` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `T_h` > 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=97)

- **FILTRO** `sigma_h` > `0.0089` → IC=-0.344 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=93)

- **FILTRO** `sigma_h` < `0.0048` → IC=-0.344 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=93)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0137` → IC=-0.167 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0137
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=86)

- **FILTRO** `T_h` > `135.1248` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `T_h` > 135.1248
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=86)

- **FILTRO** `pct_vs_K` |x|> `3.7818` → IC=-0.250 (n=38)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7818
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=76)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.352 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=21)

- **FILTRO** `T_h` > `49.3573` → IC=-0.385 (n=59)

  - _Acción_: SKIP cuando `T_h` > 49.3573
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1255` → IC=+0.469 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1255 (IC base=+0.349)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.398 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.349)

- **PATRÓN** `T_h` > `1.2173` → IC=+0.423 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2173 (IC base=+0.349)

- **PATRÓN** `dist_50` > `0.4086` → IC=+0.459 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4086 (IC base=+0.349)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.369 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.349)

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
- **PATRÓN** `edge` > `0.225` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.436)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.469 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.436)

- **PATRÓN** `T_h` > `0.801` → IC=+0.452 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.801 (IC base=+0.436)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.469 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.436)

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
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=331)

- **PATRÓN** `streak_estiramiento` < `0.5782` → IC=+0.149 (n=146)

  - _Acción_: Kelly boost +0.74€ cuando `streak_estiramiento` < 0.5782 (IC base=+0.034)

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

- **PATRÓN** `streak_estiramiento` < `0.4964` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `streak_estiramiento` < 0.4964 (IC base=+0.065)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.126 (n=97)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 48.0 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `2479.8468` → IC=+0.128 (n=92)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2479.8468 (IC base=+0.065)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=530)

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
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=755)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=906)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=895)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3337)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1732)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.211 (n=728)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.244 (n=728)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.1592` → IC=+0.207 (n=1922)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1592 (IC base=+0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2215` → IC=+0.217 (n=729)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2215 (IC base=+0.203)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1288` → IC=+0.235 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1288 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=2015)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=2258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `ibs_15` > `0.6198` → IC=+0.283 (n=2183)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6198 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.1185` → IC=+0.205 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1185 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.825` → IC=+0.275 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.825 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2947.1524` → IC=+0.209 (n=1455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2947.1524 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.222 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.203)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=932)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.231 (n=456)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.279 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.218)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2017` → IC=+0.251 (n=207)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2017 (IC base=+0.218)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1075` → IC=+0.275 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1075 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.248 (n=422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.218)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.280 (n=456)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.274 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.272 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `16113.4131` → IC=+0.253 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16113.4131 (IC base=+0.218)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.849` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.849
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=558)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.201 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.067` → IC=+0.164 (n=218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.067 (IC base=+0.147)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2358` → IC=+0.183 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio_macro` |x|> 0.2358 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1204` → IC=+0.165 (n=186)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1204 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.164 (n=355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.150 (n=518)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5797` → IC=+0.238 (n=494)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5797 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.2773` → IC=+0.157 (n=456)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2773 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.57` → IC=+0.236 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.57 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `3426.0142` → IC=+0.161 (n=441)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3426.0142 (IC base=+0.147)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.298 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.1511` → IC=+0.216 (n=241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1511 (IC base=+0.187)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0592` → IC=+0.199 (n=274)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0592 (IC base=+0.187)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3457` → IC=+0.238 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3457 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=247)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `ibs_15` > `0.5897` → IC=+0.275 (n=274)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5897 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.208 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.286` → IC=+0.357 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.286 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.187 (n=292)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `3082.6104` → IC=+0.287 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3082.6104 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.226 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.187)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=-0.003)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.253 (n=492)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0827` → IC=+0.222 (n=243)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0827 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0431` → IC=+0.216 (n=551)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0431 (IC base=+0.212)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0883` → IC=+0.266 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0883 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` > `0.5882` → IC=+0.294 (n=551)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5882 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1339` → IC=+0.222 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1339 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.5526` → IC=+0.212 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5526 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.303` → IC=+0.239 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.303 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.318` → IC=+0.216 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.318 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2925.3906` → IC=+0.290 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2925.3906 (IC base=+0.212)

- **PATRÓN** `ibs_15` < `0.1154` → IC=+0.145 (n=610)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` < 0.1154 (IC base=+0.059)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.370 (n=337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.359)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.364 (n=505)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.359)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.362 (n=339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.359)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1503` → IC=+0.388 (n=336)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1503 (IC base=+0.359)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1326` → IC=+0.393 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1326 (IC base=+0.359)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.403 (n=245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.359)

- **PATRÓN** `ibs_15` > `0.7862` → IC=+0.397 (n=505)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7862 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.388 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.369 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.359)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `3813.5418` → IC=+0.376 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3813.5418 (IC base=+0.359)

- **PATRÓN** `ballena_activa_n` < `446.0` → IC=+0.381 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 446.0 (IC base=+0.359)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1123` → IC=+0.371 (n=122)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1123 (IC base=+0.365)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.373 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.363 (n=247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.365)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.374 (n=93)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.365)

- **PATRÓN** `drift_15min` |x|≤ `0.5146` → IC=+0.372 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5146 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1537` → IC=+0.387 (n=184)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1537 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.13` → IC=+0.399 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.13 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.385 (n=276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.8057` → IC=+0.396 (n=276)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8057 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.405 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.072` → IC=+0.371 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.072 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.364 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `16045.3097` → IC=+0.383 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16045.3097 (IC base=+0.365)

- **PATRÓN** `ballena_activa_n` < `500.0` → IC=+0.421 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 500.0 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.354 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.350)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.368 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.350)

- **PATRÓN** `drift_60min` |x|≤ `0.1054` → IC=+0.364 (n=153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1054 (IC base=+0.350)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.370 (n=205)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.350)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2986` → IC=+0.377 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2986 (IC base=+0.350)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.411 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.350)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.400 (n=229)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.350)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.373 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.350)

- **PATRÓN** `dist_vwap_pct` < `0.2948` → IC=+0.352 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2948 (IC base=+0.350)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.031` → IC=+0.366 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.031 (IC base=+0.350)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.353 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.350)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.357 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.350)

- **PATRÓN** `libro_liquidez` > `4204.0039` → IC=+0.373 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4204.0039 (IC base=+0.350)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.358 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.350)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0123` → IC=-0.219 (n=816)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0123
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=2451)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.201 (n=1172)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1412` → IC=+0.184 (n=529)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio_macro` |x|> 0.1412 (IC base=-0.061)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1366` → IC=+0.247 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1366 (IC base=-0.061)

- **PATRÓN** `ibs_15` > `0.6409` → IC=+0.279 (n=793)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6409 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.197 (n=453)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1047 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` < `0.2628` → IC=+0.203 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2628 (IC base=-0.061)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2134` → IC=+0.252 (n=820)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2134 (IC base=-0.022)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.183` → IC=+0.249 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.183 (IC base=-0.022)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.273 (n=2464)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.022)

- **PATRÓN** `dist_vwap_pct` > `0.651` → IC=+0.293 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.651 (IC base=-0.022)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.207 (n=480)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1442)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.222 (n=480)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1442)

- **FILTRO** `sigma_ewma_delta_pct` > `23.641` → IC=-0.259 (n=272)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.641
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1650)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.179 (n=188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0027 (IC base=+0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.307 (n=107)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.126 (n=380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 12.0 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.335 (n=235)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.0996` → IC=+0.293 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0996 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.2353` → IC=+0.278 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2353 (IC base=+0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0841` → IC=+0.176 (n=35)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.0841 (IC base=-0.193)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.193)

- **PATRÓN** `ibs_15` < `0.501` → IC=+0.306 (n=34)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.501 (IC base=-0.193)

- **PATRÓN** `dist_vwap_pct` < `0.0553` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0553 (IC base=-0.193)

- **PATRÓN** `ballena_activa_n` < `305.0` → IC=+0.393 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 305.0 (IC base=-0.193)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.169 (n=496)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.164 (n=385)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0064 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.173 (n=344)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0038 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.0735` → IC=+0.215 (n=170)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0735 (IC base=+0.158)

- **PATRÓN** `delta_ratio_macro` |x|> `0.141` → IC=+0.160 (n=257)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.141 (IC base=+0.158)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2962` → IC=+0.220 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2962 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.185 (n=274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 11.0 (IC base=+0.158)

- **PATRÓN** `ibs_15` > `0.6526` → IC=+0.260 (n=386)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6526 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` < `0.2726` → IC=+0.170 (n=356)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.2726 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.205 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=496)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `9596.597` → IC=+0.167 (n=175)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 9596.597 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.242 (n=919)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4443` → IC=+0.236 (n=918)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4443 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.7706` → IC=+0.246 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7706 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2077` → IC=+0.261 (n=416)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2077 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.236 (n=650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.234 (n=869)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.3647` → IC=+0.266 (n=918)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3647 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.7445` → IC=+0.309 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7445 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.226` → IC=+0.270 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.226 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.472` → IC=+0.237 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.472 (IC base=+0.234)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.204 (n=572)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=192)

- **FILTRO** `drift_60min` |x|> `0.1682` → IC=-0.239 (n=259)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=505)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.276 (n=190)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=574)

- **FILTRO** `sigma_ewma_delta_pct` > `18.27` → IC=-0.145 (n=406)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.27
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3259)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.159 (n=42)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.174)

- **PATRÓN** `ibs_15` > `0.6071` → IC=+0.224 (n=56)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6071 (IC base=-0.174)

- **PATRÓN** `dist_vwap_pct` < `0.1248` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1248 (IC base=-0.174)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 44.0 (IC base=-0.174)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0785` → IC=+0.229 (n=360)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0785 (IC base=-0.040)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1866` → IC=+0.231 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1866 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.269 (n=405)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.6684` → IC=+0.235 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6684 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.1683` → IC=+0.232 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1683 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0194` → IC=-0.259 (n=462)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0194
  - _Potencial_: sin este filtro IC_bueno=-0.137 (n=464)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.251 (n=279)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=647)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.198)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.198)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1053` → IC=+0.266 (n=416)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1053 (IC base=-0.034)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1698` → IC=+0.301 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1698 (IC base=-0.034)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.292 (n=627)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` > `0.8342` → IC=+0.351 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8342 (IC base=-0.034)

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
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.306 (n=544)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.329 (n=272)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2408` → IC=+0.310 (n=272)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2408 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2199` → IC=+0.317 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2199 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=850)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.328 (n=816)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.437` → IC=+0.337 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.437 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.342 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12848.0159` → IC=+0.304 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12848.0159 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.297 (n=392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.334 (n=149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.288)

- **PATRÓN** `drift_15min` |x|≤ `0.4181` → IC=+0.288 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4181 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2575` → IC=+0.313 (n=148)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2575 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3977` → IC=+0.306 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3977 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8303` → IC=+0.319 (n=445)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8303 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.343 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `16178.7073` → IC=+0.328 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16178.7073 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.308 (n=248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.296)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.299 (n=371)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.318 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2902` → IC=+0.321 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2902 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.326 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8732` → IC=+0.350 (n=331)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8732 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.308 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.619` → IC=+0.324 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.619 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0878` → IC=-0.263 (n=74)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0878
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=225)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.197 (n=64)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=130)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2557` → IC=-0.145 (n=29)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2557
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

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

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.206 (n=32)
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
- **PATRÓN** `T_h` > `80.0063` → IC=+0.231 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 80.0063 (IC base=+0.215)

- **PATRÓN** `ratio` < `0.9752` → IC=+0.471 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9752 (IC base=+0.215)

- **PATRÓN** `T_h` > `145.7579` → IC=+0.393 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7579 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0115` → IC=+0.320 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0115 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `126.6969` → IC=+0.239 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 126.6969 (IC base=+0.196)

- **PATRÓN** `ratio` < `0.972` → IC=+0.468 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.972 (IC base=+0.196)

- **PATRÓN** `T_h` > `105.6124` → IC=+0.296 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 105.6124 (IC base=+0.289)

- **PATRÓN** `ratio` > `1.0057` → IC=+0.273 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0057 (IC base=+0.289)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `82.5234` → IC=+0.271 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 82.5234 (IC base=+0.249)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.431 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.249)

- **PATRÓN** `T_h` > `111.9558` → IC=+0.343 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9558 (IC base=+0.322)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.354 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.322)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1132` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.401)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6198 sube el IC de +0.203 a +0.283 en UPDOWN_GBM#15min (n=2183). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.218 a +0.280 en UPDOWN_GBM#BTC#15min (n=456). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5797 sube el IC de +0.147 a +0.238 en UPDOWN_GBM#ETH#15min (n=494). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5897 sube el IC de +0.187 a +0.275 en UPDOWN_GBM#SOL#15min (n=274). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5882 sube el IC de +0.212 a +0.294 en UPDOWN_GBM#XRP#15min (n=551). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6409 sube el IC de -0.061 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=793). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.022 a +0.273 en UPDOWN_GBM_15M_TARDIO (n=2464). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.088 a +0.335 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=235). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.501 sube el IC de -0.193 a +0.306 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6526 sube el IC de +0.158 a +0.260 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=386). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3647 sube el IC de +0.234 a +0.266 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=918). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.6071 sube el IC de -0.174 a +0.224 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=56). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.040 a +0.269 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=405). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.198 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.034 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=627). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.292 a +0.328 en UPDOWN_GBM_IBS_ALTO (n=816). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.288 a +0.319 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=445). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8732 sube el IC de +0.296 a +0.350 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=331). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.359 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=505). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.365 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=276). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.350 a +0.400 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=229). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1520 | +0.097 | +193.23€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1520 | +0.097 | +193.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1154 | +0.105 | +166.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1154 | +0.105 | +166.32€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 263 | +0.066 | +11.20€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 263 | +0.066 | +11.20€ | 6 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 120 | +0.016 | +19.86€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 120 | +0.016 | +19.86€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 97 | +0.025 | +17.11€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 97 | +0.025 | +17.11€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 32859 | -0.089 | -4318.39€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1687 | -0.018 | -217.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 31172 | -0.093 | -4101.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4241 | -0.116 | -714.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4241 | -0.116 | -714.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1687 | -0.018 | -217.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1687 | -0.018 | -217.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3872 | -0.114 | -868.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3872 | -0.114 | -868.83€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8472 | -0.004 | -762.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8472 | -0.004 | -762.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8211 | -0.107 | -546.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8211 | -0.107 | -546.32€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6376 | -0.165 | -1208.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6376 | -0.165 | -1208.54€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 24532 | -0.021 | +3662.36€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6348 | +0.001 | +1733.75€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 18184 | -0.028 | +1928.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 24532 | -0.021 | +3662.36€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6348 | +0.001 | +1733.75€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 18184 | -0.028 | +1928.62€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 112301 | +0.113 | -5127.53€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15920 | +0.183 | -483.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 473 | -0.054 | -58.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 88886 | +0.102 | -4318.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7022 | +0.104 | -266.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 14763 | +0.102 | -1080.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 52 | -0.130 | +12.55€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 14696 | +0.103 | -1080.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 22339 | +0.131 | -340.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4816 | +0.199 | -120.10€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 14738 | +0.116 | -135.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2743 | +0.092 | -62.80€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 14810 | +0.093 | -1226.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 60 | -0.113 | -5.60€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 14735 | +0.094 | -1209.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 23854 | +0.124 | -429.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6391 | +0.176 | -103.93€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 14902 | +0.106 | -259.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2549 | +0.100 | -57.25€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 21754 | +0.114 | -1204.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4547 | +0.187 | -277.07€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 376 | -0.016 | -4.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 15101 | +0.094 | -776.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1730 | +0.130 | -146.51€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 14781 | +0.101 | -846.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 54 | -0.036 | +10.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 14714 | +0.101 | -856.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 17925 | +0.194 | -1115.34€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 17925 | +0.194 | -1115.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4176 | +0.174 | -389.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4176 | +0.174 | -389.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1870 | +0.202 | -25.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1870 | +0.202 | -25.10€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4112 | +0.181 | -338.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4112 | +0.181 | -338.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3631 | +0.243 | -118.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3631 | +0.243 | -118.24€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4057 | +0.190 | -258.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4057 | +0.190 | -258.13€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 839 | +0.431 | -21.51€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 839 | +0.431 | -21.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 332 | +0.440 | -1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 332 | +0.440 | -1.79€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 317 | +0.434 | -5.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 317 | +0.434 | -5.26€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 178 | +0.406 | -12.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 178 | +0.406 | -12.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 62118 | +0.199 | -4655.14€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 62118 | +0.199 | -4655.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10690 | +0.182 | -1149.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10690 | +0.182 | -1149.62€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9976 | +0.224 | -346.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9976 | +0.224 | -346.23€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10697 | +0.175 | -1224.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10697 | +0.175 | -1224.04€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10046 | +0.220 | -377.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10046 | +0.220 | -377.92€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10288 | +0.203 | -668.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10288 | +0.203 | -668.25€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10421 | +0.194 | -889.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10421 | +0.194 | -889.08€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 23634 | +0.116 | +135.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 23634 | +0.116 | +135.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 11734 | +0.120 | +138.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 11734 | +0.120 | +138.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 11900 | +0.112 | -2.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 11900 | +0.112 | -2.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1701 | +0.289 | -23.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1701 | +0.289 | -23.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 765 | +0.278 | -19.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 765 | +0.278 | -19.29€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 821 | +0.289 | -7.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 821 | +0.289 | -7.56€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 115 | +0.346 | +3.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 115 | +0.346 | +3.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 760 | +0.440 | +1.47€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 760 | +0.440 | +1.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 364 | +0.437 | -1.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 364 | +0.437 | -1.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 350 | +0.443 | +2.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 350 | +0.443 | +2.78€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1304 | +0.070 | -58.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 466 | +0.058 | -37.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 838 | +0.077 | -20.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1024 | +0.077 | -27.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 186 | +0.074 | -6.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 838 | +0.077 | -20.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 214 | +0.028 | -33.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 214 | +0.028 | -33.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 45063 | +0.099 | -1204.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3660 | +0.092 | +47.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 41403 | +0.100 | -1252.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 25025 | +0.104 | -302.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3660 | +0.092 | +47.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 21365 | +0.106 | -350.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8869 | +0.108 | -38.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8869 | +0.108 | -38.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 11169 | +0.082 | -863.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 11169 | +0.082 | -863.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 865 | +0.206 | -102.69€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 865 | +0.206 | -102.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 865 | +0.206 | -102.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 865 | +0.206 | -102.69€ | 1 | 4 |
| ✅ GBM_LATE_15M | 31663 | +0.087 | +15674.06€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 31663 | +0.087 | +15674.06€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5326 | +0.202 | +4087.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5326 | +0.202 | +4087.48€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 4695 | +0.177 | +3358.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4695 | +0.177 | +3358.58€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 5618 | +0.199 | +4221.91€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5618 | +0.199 | +4221.91€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4493 | +0.031 | +1135.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4493 | +0.031 | +1135.76€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4516 | -0.031 | +994.22€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4516 | -0.031 | +994.22€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 7015 | -0.036 | +1876.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7015 | -0.036 | +1876.11€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 34086 | +0.087 | +18179.47€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 34086 | +0.087 | +18179.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6557 | +0.012 | +3407.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6557 | +0.012 | +3407.36€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7073 | +0.015 | +1497.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7073 | +0.015 | +1497.33€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4829 | +0.267 | +4953.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4829 | +0.267 | +4953.45€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5710 | +0.010 | +1277.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5710 | +0.010 | +1277.86€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5534 | +0.035 | +2229.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5534 | +0.035 | +2229.66€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4383 | +0.284 | +4813.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4383 | +0.284 | +4813.82€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 25413 | +0.173 | +19703.24€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 25413 | +0.173 | +19703.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3834 | +0.217 | +3217.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3834 | +0.217 | +3217.52€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3996 | +0.149 | +2898.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3996 | +0.149 | +2898.56€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4033 | +0.213 | +3294.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4033 | +0.213 | +3294.47€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4266 | +0.137 | +3145.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4266 | +0.137 | +3145.36€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4768 | +0.123 | +3482.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4768 | +0.123 | +3482.58€ | 0 | 27 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4516 | +0.209 | +3664.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4516 | +0.209 | +3664.76€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6914 | +0.137 | +3244.15€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6914 | +0.137 | +3244.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 339 | +0.142 | +189.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 339 | +0.142 | +189.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2004 | +0.142 | +1067.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2004 | +0.142 | +1067.98€ | 0 | 30 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2070 | +0.151 | +1000.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2070 | +0.151 | +1000.52€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1591 | +0.108 | +574.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1591 | +0.108 | +574.06€ | 1 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 535 | +0.135 | +236.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 535 | +0.135 | +236.68€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 31898 | +0.179 | +24534.98€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 31898 | +0.179 | +24534.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5069 | +0.230 | +4492.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5069 | +0.230 | +4492.72€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4940 | +0.147 | +3204.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4940 | +0.147 | +3204.42€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5324 | +0.227 | +4619.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5324 | +0.227 | +4619.84€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5177 | +0.135 | +3628.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5177 | +0.135 | +3628.53€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5622 | +0.123 | +3895.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5622 | +0.123 | +3895.33€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5766 | +0.212 | +4694.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5766 | +0.212 | +4694.15€ | 0 | 23 |
| ✅ GBM_LATE_5M | 8672 | +0.173 | +5784.14€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 8672 | +0.173 | +5784.14€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2095 | +0.169 | +1524.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2095 | +0.169 | +1524.45€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2824 | +0.179 | +1865.46€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2824 | +0.179 | +1865.46€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 894 | +0.146 | +504.32€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 894 | +0.146 | +504.32€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1102 | +0.147 | +570.87€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1102 | +0.147 | +570.87€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2287 | +0.074 | +832.04€ | 0 | 13 |
| ✅ GBM_LATE_60M#60min | 2287 | +0.074 | +832.04€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 857 | +0.094 | +307.63€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 857 | +0.094 | +307.63€ | 0 | 15 |
| ✅ GBM_LATE_60M#ETH | 725 | +0.074 | +324.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 725 | +0.074 | +324.34€ | 1 | 11 |
| ✅ GBM_LATE_60M#SOL | 705 | +0.052 | +200.07€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 705 | +0.052 | +200.07€ | 2 | 13 |
| 🚫 GBM_LATE_60M_FADE | 451 | -0.242 | -12.65€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 451 | -0.242 | -12.65€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 166 | -0.220 | -5.99€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 166 | -0.220 | -5.99€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 156 | -0.234 | -1.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 156 | -0.234 | -1.96€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 129 | -0.271 | -4.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 129 | -0.271 | -4.71€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 964 | +0.088 | +249.10€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 964 | +0.088 | +249.10€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 355 | +0.080 | +76.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 355 | +0.080 | +76.52€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 320 | +0.056 | +37.86€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 320 | +0.056 | +37.86€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 289 | +0.132 | +134.72€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 289 | +0.132 | +134.72€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2635 | +0.104 | +705.57€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2635 | +0.104 | +705.57€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2635 | +0.104 | +705.57€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2635 | +0.104 | +705.57€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 415 | -0.073 | -33.23€ | 4 | 0 |
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
| ✅ LIQUIDACIONES_5M | 2708 | +0.024 | +83.15€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2708 | +0.024 | +83.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 134 | +0.029 | -0.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 134 | +0.029 | -0.60€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 393 | +0.039 | +38.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 393 | +0.039 | +38.24€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1039 | +0.032 | +31.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1039 | +0.032 | +31.57€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 623 | +0.015 | +2.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 623 | +0.015 | +2.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 318 | +0.025 | +17.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 318 | +0.025 | +17.59€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1333 | -0.045 | -29.84€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1333 | -0.045 | -29.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 380 | -0.042 | -13.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 380 | -0.042 | -13.47€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 443 | -0.026 | -0.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 443 | -0.026 | -0.36€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 510 | -0.065 | -16.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 510 | -0.065 | -16.01€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 4138 | -0.021 | +56.84€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1952 | -0.025 | +5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2186 | -0.018 | +51.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 114 | +0.000 | +4.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 59 | +0.057 | +10.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 55 | -0.061 | -5.83€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1016 | -0.002 | +43.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 479 | -0.007 | +11.41€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 537 | +0.003 | +31.75€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 467 | -0.022 | +8.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 227 | -0.033 | -1.04€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 240 | -0.012 | +9.34€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 836 | -0.036 | -20.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 381 | -0.051 | -24.58€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 455 | -0.023 | +3.75€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 816 | -0.026 | +8.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 394 | -0.030 | +3.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 422 | -0.021 | +5.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 889 | -0.026 | +13.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 412 | -0.022 | +6.69€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 477 | -0.030 | +6.54€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 36520 | -0.004 | +1747.76€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 36520 | -0.004 | +1747.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6497 | +0.023 | +855.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6497 | +0.023 | +855.76€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5486 | -0.031 | -70.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5486 | -0.031 | -70.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6592 | +0.019 | +633.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6592 | +0.019 | +633.53€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5273 | -0.053 | -158.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5273 | -0.053 | -158.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6149 | -0.008 | +213.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6149 | -0.008 | +213.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6523 | +0.012 | +274.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6523 | +0.012 | +274.16€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6117 | -0.060 | -147.45€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6117 | -0.060 | -147.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1493 | -0.079 | -35.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1493 | -0.079 | -35.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 703 | -0.127 | -34.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 703 | -0.127 | -34.95€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1804 | -0.076 | -32.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1804 | -0.076 | -32.07€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 91804 | -0.073 | +1684.18€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 91804 | -0.073 | +1684.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 15739 | -0.074 | +921.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 15739 | -0.074 | +921.86€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 13973 | -0.098 | -795.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 13973 | -0.098 | -795.80€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 15993 | -0.066 | +875.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 15993 | -0.066 | +875.94€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 13505 | -0.094 | -368.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 13505 | -0.094 | -368.26€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 16667 | -0.051 | +337.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 16667 | -0.051 | +337.75€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 15927 | -0.063 | +712.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 15927 | -0.063 | +712.68€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7978 | -0.030 | -145.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7978 | -0.030 | -145.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1879 | -0.042 | -18.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1879 | -0.042 | -18.55€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2238 | -0.024 | -28.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2238 | -0.024 | -28.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1088 | -0.048 | -21.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1088 | -0.048 | -21.21€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 770 | -0.022 | -24.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 770 | -0.022 | -24.88€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1333 | +0.116 | +493.09€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1197 | +0.122 | +480.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 278 | +0.139 | +141.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 278 | +0.139 | +141.54€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 226 | +0.110 | +65.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 226 | +0.110 | +65.51€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 245 | +0.115 | +98.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 245 | +0.115 | +98.12€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 216 | +0.142 | +109.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 216 | +0.142 | +109.48€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 232 | +0.098 | +65.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 232 | +0.098 | +65.84€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 840 | -0.019 | -25.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 840 | -0.019 | -25.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 164 | +0.006 | +8.78€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 164 | +0.006 | +8.78€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 119 | -0.012 | -2.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 119 | -0.012 | -2.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 228 | -0.043 | -19.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 228 | -0.043 | -19.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 187 | +0.013 | +4.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 187 | +0.013 | +4.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 142 | -0.056 | -15.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 142 | -0.056 | -15.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 716 | -0.092 | -65.10€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 326 | -0.146 | -77.67€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 255 | -0.189 | -72.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 71 | +0.007 | -4.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 254 | -0.051 | -1.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 183 | -0.057 | -4.31€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 71 | -0.034 | +2.83€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 136 | -0.036 | +14.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 108 | -0.054 | +8.12€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 28 | +0.033 | +5.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 546 | -0.119 | -68.98€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 170 | -0.006 | +3.87€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 861 | -0.201 | -47.19€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 357 | -0.194 | -31.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 307 | -0.196 | -31.46€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 50 | -0.173 | +0.17€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 292 | -0.218 | -29.97€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 251 | -0.227 | -35.81€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 41 | -0.151 | +5.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 212 | -0.187 | +14.07€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 194 | -0.184 | +10.42€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 18 | -0.180 | +3.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 752 | -0.204 | -56.86€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 109 | -0.176 | +9.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 355 | +0.402 | +289.03€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 91 | +0.371 | +75.92€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 91 | +0.371 | +75.92€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 224 | +0.460 | +214.35€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 224 | +0.460 | +214.35€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 355 | +0.402 | +289.03€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 608 | +0.026 | +15.17€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 608 | +0.026 | +15.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 43 | +0.056 | +0.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 43 | +0.056 | +0.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 64 | -0.015 | -2.20€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 64 | -0.015 | -2.20€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 206 | +0.038 | +14.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 206 | +0.038 | +14.31€ | 3 | 4 |
| ✅ STREAK_FADE_5M | 3047 | -0.023 | -125.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3047 | -0.023 | -125.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 904 | -0.022 | -32.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 904 | -0.022 | -32.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 577 | -0.025 | -24.71€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 577 | -0.025 | -24.71€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1410 | -0.021 | -54.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1410 | -0.021 | -54.07€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 85 | -0.052 | -8.44€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 85 | -0.052 | -8.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9520 | +0.019 | +105.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9520 | +0.019 | +105.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2622 | +0.021 | +28.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2622 | +0.021 | +28.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2195 | +0.028 | +50.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2195 | +0.028 | +50.03€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2860 | +0.010 | -0.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2860 | +0.010 | -0.30€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1843 | +0.020 | +27.80€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1843 | +0.020 | +27.80€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8506 | +0.013 | -44.83€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8506 | +0.013 | -44.83€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3356 | +0.017 | -8.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3356 | +0.017 | -8.05€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3384 | +0.011 | -23.82€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3384 | +0.011 | -23.82€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1766 | +0.008 | -12.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1766 | +0.008 | -12.96€ | 1 | 0 |
| ✅ UPDOWN_GBM | 53100 | +0.042 | +3920.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 13393 | +0.077 | +2787.49€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1773 | +0.006 | +9.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 34637 | +0.034 | +1090.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3108 | +0.005 | +37.17€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 5398 | +0.079 | +721.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1040 | +0.158 | +466.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4325 | +0.060 | +255.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 10211 | +0.048 | +804.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1719 | +0.090 | +397.22€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 476 | +0.013 | +4.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 6537 | +0.051 | +367.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1408 | +0.005 | +34.68€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 71 | -0.089 | +0.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 6286 | +0.051 | +487.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1010 | +0.138 | +363.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 5248 | +0.035 | +125.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 11682 | +0.031 | +619.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3293 | +0.054 | +444.84€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 469 | +0.007 | +9.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 6806 | +0.028 | +163.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1052 | +0.005 | +0.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 62 | -0.125 | +2.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 11847 | +0.021 | +412.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3181 | +0.031 | +270.96€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 459 | -0.001 | -0.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 7505 | +0.021 | +144.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 648 | +0.005 | +2.48€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 54 | -0.161 | -4.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 7674 | +0.048 | +877.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3150 | +0.095 | +844.09€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 308 | +0.006 | -1.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4216 | +0.016 | +34.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 187 | -0.124 | -2.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 673 | +0.359 | +238.03€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 673 | +0.359 | +238.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 368 | +0.365 | +128.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 368 | +0.365 | +128.82€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 305 | +0.350 | +109.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 305 | +0.350 | +109.21€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 15027 | -0.030 | +3438.20€ | 2 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 15027 | -0.030 | +3438.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1134 | -0.058 | +369.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1134 | -0.058 | +369.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2673 | -0.114 | +108.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2673 | -0.114 | +108.56€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 622 | +0.203 | +475.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 622 | +0.203 | +475.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1736 | +0.212 | +1109.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1736 | +0.212 | +1109.86€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4429 | -0.063 | +615.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4429 | -0.063 | +615.18€ | 4 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4433 | -0.068 | +760.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4433 | -0.068 | +760.04€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 171 | +0.026 | +6.16€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 171 | +0.026 | +6.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 171 | +0.026 | +6.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 171 | +0.026 | +6.16€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1087 | +0.292 | +900.55€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1087 | +0.292 | +900.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 593 | +0.288 | +457.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 593 | +0.288 | +457.66€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 494 | +0.296 | +442.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 494 | +0.296 | +442.88€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 754 | -0.112 | -83.60€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#5min | 754 | -0.112 | -83.60€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 224 | -0.088 | -18.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 224 | -0.088 | -18.30€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 71 | -0.158 | -8.76€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 71 | -0.158 | -8.76€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 80 | -0.183 | -6.49€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 80 | -0.183 | -6.49€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2823 | +0.307 | +1399.95€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 994 | +0.260 | +149.29€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1079 | +0.299 | +475.76€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 750 | +0.378 | +774.90€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.050) — sin ventaja clara. oversold(IBS<0.3): IC=+0.052 n=18573 | neutral: IC=+0.043 n=19637 | overbought(IBS>0.7): IC=+0.094 n=18970
  - _Datos_: n=59301 IC=+0.064 PNL=+7979.36€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 605 celda(s) pasan gate riguroso completo de 2408 evaluadas (n>=40) y 3394 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.031 < 0.08 — monitorear
  - _Datos_: n=3181 IC=+0.031 PNL=+270.96€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1079/15 IC=+0.299 PNL=+475.76€ | BTC: n=994/15 IC=+0.260 PNL=+149.29€ | SOL: n=750/15 IC=+0.378 PNL=+774.90€

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
  - _Estado_: 53038 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.125 n=497/60 | contraria IC=+0.184 n=507 | gap=-0.058 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=367, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 216 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1052/40 IC=+0.005 PNL=+0.01€ | BTC#60min: n=1408/40 IC=+0.005 PNL=+34.68€ | SOL#60min: n=648/40 IC=+0.005 PNL=+2.48€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=418394 | tras_1loss IC=+0.087 n=322000 | tras_2loss IC=+0.055 n=133062/40 | gap=-0.007 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.023 n=6609 | contrario_BTC IC=+0.039 n=5862/40 | gap=+0.016 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.08 con n=442 PNL=+357.10€
  - _Datos_: n=442 IC=+0.214 PNL=+357.10€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.221 > 0.08 con n=500 PNL=+386.61€
  - _Datos_: n=500 IC=+0.221 PNL=+386.61€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=2303 PNL=+1267.98€
  - _Datos_: n=2303 IC=+0.333 PNL=+1267.98€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=419 IC=+0.077 PNL=+48.81€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=419 IC=+0.077 PNL=+48.81€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=64 IC=+0.182 PNL=+41.73€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=64 IC=+0.182 PNL=+41.73€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=50271 IC=+0.041 PNL=+3713.01€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=50271 IC=+0.041 PNL=+3713.01€

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
  - _Estado_: n=2122 IC=+0.007 PNL=+2.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2122 IC=+0.007 PNL=+2.29€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=986 IC=-0.001 PNL=+34.88€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=986 IC=-0.001 PNL=+34.88€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=668 IC=+0.016 PNL=+30.07€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=668 IC=+0.016 PNL=+30.07€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.1 con n=2910 PNL=+2072.76€
  - _Datos_: n=2910 IC=+0.203 PNL=+2072.76€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=2131 IC=+0.066 PNL=+170.45€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2131 IC=+0.066 PNL=+170.45€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1719 IC=+0.090 PNL=+397.22€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1719 IC=+0.090 PNL=+397.22€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.096 > 0.08 con n=7666 PNL=+2100.69€
  - _Datos_: n=7666 IC=+0.096 PNL=+2100.69€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=201 IC=-0.264 PNL=-12.84€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=201 IC=-0.264 PNL=-12.84€

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
  - _Estado_: n=6808 IC=+0.007 PNL=+58.41€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6808 IC=+0.007 PNL=+58.41€

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
  - _Estado_: n=9306 IC=+0.042 PNL=+636.73€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=9306 IC=+0.042 PNL=+636.73€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=3181 IC=+0.062 PNL=+442.71€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3181 IC=+0.062 PNL=+442.71€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=420 PNL=+129.23€
  - _Datos_: n=420 IC=+0.111 PNL=+129.23€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.152 > 0.08 con n=798 PNL=+215.40€
  - _Datos_: n=798 IC=+0.152 PNL=+215.40€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.08 con n=616 PNL=+332.25€
  - _Datos_: n=616 IC=+0.105 PNL=+332.25€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=64288 IC=+0.118 PNL=+23913.28€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=64288 IC=+0.118 PNL=+23913.28€

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
  - _Estado_: n=8027 IC=+0.047 PNL=+698.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8027 IC=+0.047 PNL=+698.29€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.02 con n=764 PNL=+299.90€
  - _Datos_: n=764 IC=+0.121 PNL=+299.90€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=180 IC=-0.066 PNL=+28.48€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=180 IC=-0.066 PNL=+28.48€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.451 > 0.1 con n=1320 PNL=+1295.87€
  - _Datos_: n=1320 IC=+0.451 PNL=+1295.87€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=19690 IC=+0.068 PNL=+2730.81€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=19690 IC=+0.068 PNL=+2730.81€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.1 con n=4718 PNL=+2757.56€
  - _Datos_: n=4718 IC=+0.207 PNL=+2757.56€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.152 < -0.1 con n=314 PNL=+29.30€
  - _Datos_: n=314 IC=-0.152 PNL=+29.30€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2416 IC=+0.059 PNL=+257.86€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2416 IC=+0.059 PNL=+257.86€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.1 con n=569 PNL=+148.35€
  - _Datos_: n=569 IC=+0.120 PNL=+148.35€

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
  - _Estado_: n=23002 IC=-0.135 PNL=+1750.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=23002 IC=-0.135 PNL=+1750.74€

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
  - _Estado_: n=2353 IC=+0.137 PNL=+1359.07€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2353 IC=+0.137 PNL=+1359.07€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.204 > 0.08 con n=2871 PNL=+2060.13€
  - _Datos_: n=2871 IC=+0.204 PNL=+2060.13€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=5598 IC=+0.036 PNL=+319.42€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5598 IC=+0.036 PNL=+319.42€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=2601 PNL=+1406.25€
  - _Datos_: n=2601 IC=+0.090 PNL=+1406.25€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.217 > 0.08 con n=606 PNL=+327.32€
  - _Datos_: n=606 IC=+0.217 PNL=+327.32€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.226 < -0.1 con n=2298 PNL=-172.11€
  - _Datos_: n=2298 IC=-0.226 PNL=-172.11€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=6641 IC=+0.182 PNL=+4635.89€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=6641 IC=+0.182 PNL=+4635.89€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=94 PNL=+38.77€
  - _Datos_: n=94 IC=+0.115 PNL=+38.77€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2399 IC=+0.070 PNL=+754.90€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2399 IC=+0.070 PNL=+754.90€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.178 > 0.08 con n=2195 PNL=+1553.37€
  - _Datos_: n=2195 IC=+0.178 PNL=+1553.37€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3685 IC=-0.030 PNL=+985.33€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3685 IC=-0.030 PNL=+985.33€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=602 PNL=-51.71€
  - _Datos_: n=602 IC=+0.084 PNL=-51.71€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.239 > 0.08 con n=3864 PNL=-329.51€
  - _Datos_: n=3864 IC=+0.239 PNL=-329.51€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=47 IC=-0.010 PNL=+5.23€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=47 IC=-0.010 PNL=+5.23€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.100 n=1339) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1339 IC=+0.100 PNL=+302.31€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.316 > 0.08 con n=341 PNL=+110.42€
  - _Datos_: n=341 IC=+0.316 PNL=+110.42€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.408 n=487) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=487 IC=+0.408 PNL=+684.31€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=10690 IC=+0.182 PNL=-1149.62€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=10690 IC=+0.182 PNL=-1149.62€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.1 con n=172 PNL=+105.24€
  - _Datos_: n=172 IC=+0.207 PNL=+105.24€
