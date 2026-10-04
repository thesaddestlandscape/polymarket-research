# Hipótesis automáticas — 2026-10-04 02:35 UTC
_Generado por shadow_postmortem.py sobre 738000 resoluciones (PNL=+89249.64€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=573)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.222 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.132)

- **PATRÓN** `n_total_lado` > `71.0` → IC=+0.215 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 71.0 (IC base=+0.132)

- **PATRÓN** `banda_hit_calibrado` > `0.8019` → IC=+0.261 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8019 (IC base=+0.132)

- **PATRÓN** `banda_z` > `9.204` → IC=+0.197 (n=209)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 9.204 (IC base=+0.132)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.717` → IC=+0.132 (n=560)

  - _Acción_: Kelly boost +0.66€ cuando `ballenas_wallet_edge_medio` > 0.717 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.134 (n=421)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 11.0 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=658)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `3816.3674` → IC=+0.142 (n=283)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3816.3674 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `8556.0995` → IC=+0.121 (n=233)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 8556.0995 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.227 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `42.0` → IC=+0.167 (n=466)

  - _Acción_: Kelly boost +0.83€ cuando `n_total_lado` > 42.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.264 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.140)

- **PATRÓN** `banda_z` > `9.958` → IC=+0.208 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.958 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.141 (n=360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 12.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=561)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2879.0602` → IC=+0.141 (n=444)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2879.0602 (IC base=+0.140)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.355` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.232 (n=106)

- **FILTRO** `banda_hit_calibrado` < `0.8019` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8019
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=95)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.181 (n=114)

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

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.253 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.8019` → IC=+0.253 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8019 (IC base=+0.122)

- **PATRÓN** `banda_z` > `6.035` → IC=+0.171 (n=71)

  - _Acción_: Kelly boost +0.86€ cuando `banda_z` > 6.035 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.128 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.181 (n=114)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `1196.2423` → IC=+0.185 (n=71)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1196.2423 (IC base=+0.122)

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
- **FILTRO** `restante_s_al_confirmar` < `144.34` → IC=-0.217 (n=8196)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.34
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=24589)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `132.52` → IC=-0.268 (n=1059)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.52
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=3178)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `124.67` → IC=-0.307 (n=966)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.67
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2899)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `165.61` → IC=-0.221 (n=2045)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 165.61
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=6136)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.33` → IC=-0.327 (n=1591)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.33
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=4773)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.213 (n=15909)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=3834)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `5441.057` → IC=+0.170 (n=2486)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5441.057 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.137 (n=14005)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=16941)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=13045)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=6286)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7645.4381` → IC=+0.169 (n=2405)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7645.4381 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.207 (n=1792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1833)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=2308)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `16039.4185` → IC=+0.221 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16039.4185 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.203 (n=1652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1834)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=2353)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `15958.35` → IC=+0.209 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15958.35 (IC base=+0.196)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.166 (n=393)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `4587.7919` → IC=+0.126 (n=249)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 4587.7919 (IC base=+0.090)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=421)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.094)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=922)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `5754.4405` → IC=+0.150 (n=232)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5754.4405 (IC base=+0.094)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=3314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.356 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.230 (n=1490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.362 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=1725)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=707)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.256 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.138 (n=903)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `1315.39` → IC=+0.144 (n=787)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1315.39 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.406 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=648)
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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=13958)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=13311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.227 (n=5944)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.177 (n=3120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3169)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.174)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` < `0.775` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=63)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.237 (n=1320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.236 (n=1311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.336 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.233)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=3073)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=3092)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.191 (n=1262)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.73 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=2856)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.332 (n=970)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=3171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=2716)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.192 (n=2399)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.197 (n=1151)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `11667.7741` → IC=+0.457 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11667.7741 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.440 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.443 (n=261)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.456 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `14799.7123` → IC=+0.446 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14799.7123 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.446 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.465 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.434)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `3369.9988` → IC=+0.450 (n=158)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=18275)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=7166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.184 (n=5728)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.196 (n=7866)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=3729)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.267 (n=4241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=7571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=7575)

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

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.270 (n=2550)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6901)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=2726)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=2984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.242 (n=3177)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=6385)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=6120)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.49` → IC=+0.137 (n=5895)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.49 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=3209)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=3049)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=3871)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.19` → IC=+0.144 (n=2929)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.19 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.184 (n=3176)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.38 (IC base=+0.112)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.130 (n=3361)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 4.96 (IC base=+0.112)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.134 (n=2976)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.112)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.313 (n=911)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.289 (n=1274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `4186.9259` → IC=+0.306 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4186.9259 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.289 (n=600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.350 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `4327.8819` → IC=+0.294 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4327.8819 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=435)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=641)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1436.9616` → IC=+0.302 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1436.9616 (IC base=+0.288)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.439 (n=504)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.443 (n=243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.439 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.457 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.925` → IC=+0.457 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.925 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `2158.1237` → IC=+0.455 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2158.1237 (IC base=+0.443)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4883` → IC=+0.130 (n=9949)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4883 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9825` → IC=+0.243 (n=3317)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9825 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2178` → IC=+0.256 (n=2227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2178 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.183 (n=3781)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.250 (n=2782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2089 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6148` → IC=+0.254 (n=2781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6148 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.3018` → IC=+0.228 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3018 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `1.4634` → IC=+0.211 (n=6951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4634 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5676` → IC=+0.137 (n=12074)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.5676 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.5912` → IC=+0.203 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5912 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.1495` → IC=+0.176 (n=4004)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1495 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `1.193` → IC=+0.178 (n=4385)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.193 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` > `1.05` → IC=+0.176 (n=1988)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.05 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.1671` → IC=+0.220 (n=2110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1671 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.2814` → IC=+0.196 (n=6618)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2814 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.4477` → IC=+0.198 (n=7519)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4477 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.213 (n=7319)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 118.0 (IC base=+0.069)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.214 (n=744)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.185 (n=741)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0081 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3519` → IC=+0.183 (n=2217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3519 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.190 (n=1081)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.178 (n=1096)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 8.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.277 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.227` → IC=+0.285 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.227 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.219 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.180 (n=2094)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=2271)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2042.1048` → IC=+0.187 (n=739)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2042.1048 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.242 (n=1574)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1259` → IC=+0.268 (n=777)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1259 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0613` → IC=+0.287 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0613 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.484` → IC=+0.247 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.484 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.394` → IC=+0.238 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.394 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0937` → IC=+0.230 (n=1549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0937 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.262 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.5941` → IC=+0.244 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5941 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=1928)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1592.8005` → IC=+0.245 (n=1762)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1592.8005 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.237 (n=773)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.3538` → IC=+0.227 (n=1753)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3538 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=1754)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9785` → IC=+0.262 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9785 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.3455` → IC=+0.220 (n=1631)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3455 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.769` → IC=+0.254 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.769 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `1.2498` → IC=+0.221 (n=1753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2498 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `0.6912` → IC=+0.222 (n=1566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6912 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.240 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.4058` → IC=+0.240 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4058 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `16023.0298` → IC=+0.218 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16023.0298 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.184 (n=589)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0026 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0744` → IC=+0.165 (n=589)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0744 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=800)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7204` → IC=+0.173 (n=1765)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.7204 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1267` → IC=+0.153 (n=1588)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1267 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.292` → IC=+0.140 (n=281)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 11.292 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.3` → IC=+0.143 (n=1622)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.3 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.147 (n=1765)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2025 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.8505` → IC=+0.138 (n=1176)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.8505 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.171 (n=472)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.449` → IC=+0.149 (n=1654)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.449 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7828` → IC=+0.145 (n=1102)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7828 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `14177.8639` → IC=+0.142 (n=1176)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 14177.8639 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.171 (n=695)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 231.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.200 (n=2234)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=2230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=2000)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.343` → IC=+0.261 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.343 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.193 (n=1952)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.3482` → IC=+0.203 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3482 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.1663` → IC=+0.206 (n=1428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1663 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2664)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `1946.7648` → IC=+0.194 (n=1011)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 1946.7648 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.220 (n=1734)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6219` → IC=+0.213 (n=1970)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6219 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.210 (n=920)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.232 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.67` → IC=+0.237 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.67 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.348` → IC=+0.249 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.348 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7249` → IC=+0.218 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7249 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7565` → IC=+0.220 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7565 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1938.1775` → IC=+0.215 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1938.1775 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.212 (n=1776)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=120)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2661)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.153 (n=428)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0037 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9584` → IC=+0.219 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9584 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1949` → IC=+0.331 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1949 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.903` → IC=+0.174 (n=878)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 4.903 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.330 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8546 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.329 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1112` → IC=+0.335 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1112 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.351 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `1.8416` → IC=+0.325 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8416 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.329 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.1014` → IC=+0.156 (n=696)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1014 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.3201` → IC=+0.199 (n=320)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3201 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `0.8475` → IC=+0.149 (n=725)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8475 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2283` → IC=+0.192 (n=183)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2283 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.5204` → IC=+0.162 (n=923)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5204 (IC base=+0.024)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.189 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=411)

- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.194 (n=119)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=364)

- **FILTRO** `ibs_20min` > `0.2381` → IC=-0.126 (n=2685)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=1332)

- **FILTRO** `sigma_ewma_delta_pct` > `8.773` → IC=-0.218 (n=423)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.773
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=3594)

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

- **PATRÓN** `ibs_20min` < `0.2381` → IC=+0.133 (n=1332)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2381 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.1732` → IC=+0.258 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1732 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.276 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.1602` → IC=+0.316 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1602 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.4034` → IC=+0.292 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4034 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6452` → IC=-0.176 (n=704)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6452
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2113)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.203 (n=674)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2143)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.209 (n=1029)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=3139)

- **PATRÓN** `dist_vwap_pct` > `0.7959` → IC=+0.317 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7959 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2041` → IC=+0.317 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2041 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` < `0.9855` → IC=+0.292 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9855 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.637` → IC=+0.308 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.637 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.299 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.294 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.4513` → IC=+0.297 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4513 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.8324` → IC=+0.301 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8324 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.8672` → IC=+0.284 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8672 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` < `0.7234` → IC=+0.251 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7234 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` > `1.0756` → IC=+0.271 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0756 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.1002` → IC=+0.261 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1002 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.141` → IC=+0.256 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.141 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.249 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.42 (IC base=-0.015)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.200 (n=4311)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.188 (n=11558)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4706 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.9982` → IC=+0.287 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9982 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.677` → IC=+0.158 (n=5897)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.677 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.1772` → IC=+0.246 (n=4707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1772 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.6141` → IC=+0.252 (n=4707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6141 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` < `0.0804` → IC=+0.241 (n=6968)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0804 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.264 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.6397` → IC=+0.255 (n=2533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6397 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.276 (n=7140)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.166 (n=4178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0091 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5461` → IC=+0.157 (n=11024)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5461 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.6968` → IC=+0.249 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6968 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2391` → IC=+0.248 (n=3616)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2391 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7075` → IC=+0.249 (n=1663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7075 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1953` → IC=+0.259 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1953 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2416` → IC=+0.302 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2416 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5884` → IC=+0.278 (n=2295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5884 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.280 (n=5103)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2587` → IC=-0.160 (n=897)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2587
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2693)

- **FILTRO** `ibs_20min` > `0.76` → IC=-0.173 (n=734)

  - _Acción_: SKIP cuando `ibs_20min` > 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2205)

- **FILTRO** `sigma_ewma_delta_pct` > `4.568` → IC=-0.173 (n=662)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.568
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2277)

- **PATRÓN** `ibs_20min` > `0.9043` → IC=+0.280 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9043 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.221` → IC=+0.196 (n=637)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 7.221 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2272` → IC=+0.270 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2272 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.205 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.1877` → IC=+0.234 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1877 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.230 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.0982` → IC=+0.427 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0982 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2231` → IC=+0.427 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2231 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.5483` → IC=+0.439 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5483 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.5328` → IC=+0.425 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5328 (IC base=-0.025)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.437 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.025)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8641` → IC=+0.161 (n=868)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.8641 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.1115` → IC=+0.186 (n=661)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1115 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.6746` → IC=+0.177 (n=1087)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6746 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.224 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4262` → IC=+0.193 (n=399)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4262 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.423` → IC=+0.183 (n=399)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.423 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.224 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 231.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.149` → IC=+0.225 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.149 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.6101` → IC=+0.226 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6101 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0728` → IC=+0.220 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0728 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2686` → IC=+0.291 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2686 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.229 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4386 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1685` → IC=+0.236 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1685 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.272 (n=1971)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.254 (n=1984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=1759)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.781` → IC=+0.284 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.781 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.264 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `1.6236` → IC=+0.258 (n=1883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6236 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2332)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `2009.7484` → IC=+0.272 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.7484 (IC base=+0.251)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.301 (n=1639)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.1806` → IC=+0.300 (n=722)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1806 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.321 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.3571` → IC=+0.293 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3571 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `0.1` → IC=+0.287 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.685` → IC=+0.292 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.685 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.1196` → IC=+0.290 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1196 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.7249` → IC=+0.299 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7249 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.6827` → IC=+0.297 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6827 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1931.867` → IC=+0.308 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1931.867 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.288 (n=1321)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.286)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7715` → IC=-0.186 (n=746)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7715
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=2242)

- **PATRÓN** `ibs_20min` > `0.9037` → IC=+0.174 (n=673)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.9037 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.3897` → IC=+0.233 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3897 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.0082` → IC=+0.250 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0082 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.1689` → IC=+0.236 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1689 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.0821` → IC=+0.251 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0821 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4046` → IC=+0.264 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4046 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `141.0` → IC=+0.261 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 141.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.13` → IC=+0.231 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.13 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1804` → IC=+0.216 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1804 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8288` → IC=+0.267 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8288 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.252 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.76` → IC=-0.185 (n=1372)

  - _Acción_: SKIP cuando `ibs_20min` < 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.283 (n=1374)

- **FILTRO** `ibs_20min` > `0.6744` → IC=-0.242 (n=689)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6744
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=2071)

- **FILTRO** `sigma_ewma_delta_pct` > `4.814` → IC=-0.204 (n=586)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.814
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=2174)

- **PATRÓN** `ibs_20min` > `0.76` → IC=+0.283 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.76 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.213` → IC=+0.317 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.213 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.658` → IC=+0.169 (n=433)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.658 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8591` → IC=+0.310 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8591 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.303 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.300 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.321 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.322 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.133 (n=1823)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5714 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.2679` → IC=+0.241 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2679 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.7092` → IC=+0.270 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7092 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.1845` → IC=+0.231 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1845 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.069` → IC=+0.259 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.069 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4082` → IC=+0.249 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4082 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.260 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.021)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.328 (n=1422)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.284)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.304 (n=748)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `0.6454` → IC=+0.316 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6454 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2145` → IC=+0.317 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2145 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.76` → IC=+0.309 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.76 (IC base=+0.284)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.298 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.330 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.296 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=1576)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2474.544` → IC=+0.296 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2474.544 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.322 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.314 (n=1127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.1944` → IC=+0.285 (n=743)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1944 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.294 (n=576)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.309 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.3125` → IC=+0.294 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3125 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` < `0.2283` → IC=+0.283 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2283 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.529` → IC=+0.298 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.529 (IC base=+0.284)

- **PATRÓN** `volumen_regimen` < `0.7178` → IC=+0.285 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7178 (IC base=+0.284)

- **PATRÓN** `volumen_regimen` > `1.2318` → IC=+0.314 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2318 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.332 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` < `1.4219` → IC=+0.294 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4219 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.1376` → IC=+0.281 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1376 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2430.3904` → IC=+0.289 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2430.3904 (IC base=+0.284)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.186 (n=3242)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0048 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.205 (n=3239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.3596` → IC=+0.183 (n=8542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3596 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=10120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.226 (n=9708)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1719` → IC=+0.197 (n=4184)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1719 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.412` → IC=+0.254 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.412 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.2075` → IC=+0.167 (n=6461)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2075 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.162 (n=6459)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6297 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.198 (n=1441)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.5607` → IC=+0.172 (n=4115)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5607 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6003` → IC=+0.181 (n=3118)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6003 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `1978.7554` → IC=+0.176 (n=8672)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1978.7554 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.189 (n=8622)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 106.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.187 (n=6198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0066 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.0807` → IC=+0.218 (n=3099)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0807 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=3570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.4872` → IC=+0.229 (n=9294)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4872 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` < `0.1698` → IC=+0.167 (n=6467)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1698 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.303` → IC=+0.196 (n=1560)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.303 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1775` → IC=+0.161 (n=6664)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1775 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.215 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.5562` → IC=+0.173 (n=3783)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5562 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6122` → IC=+0.174 (n=2866)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6122 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.182 (n=8274)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 108.0 (IC base=+0.173)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.244 (n=545)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.205 (n=543)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.3424` → IC=+0.219 (n=1629)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3424 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=1722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.201 (n=1188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.914` → IC=+0.286 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.914 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.249` → IC=+0.329 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.249 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.240 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.4332` → IC=+0.196 (n=1522)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4332 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2042.94` → IC=+0.201 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.94 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.251 (n=1088)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.246 (n=1237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.1037` → IC=+0.301 (n=545)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1037 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.252 (n=1189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.3503` → IC=+0.263 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3503 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.392` → IC=+0.242 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.392 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.224` → IC=+0.248 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.224 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.262 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4205` → IC=+0.266 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4205 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.6147` → IC=+0.239 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6147 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.244 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1592.1` → IC=+0.256 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1592.1 (IC base=+0.242)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.227 (n=489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.1672` → IC=+0.179 (n=973)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1672 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=1458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.3916` → IC=+0.222 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3916 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.1985` → IC=+0.207 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1985 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.528` → IC=+0.229 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.528 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.6876` → IC=+0.168 (n=642)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6876 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.197 (n=229)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4127` → IC=+0.181 (n=474)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4127 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.4826` → IC=+0.155 (n=474)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.4826 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `11951.166` → IC=+0.159 (n=1303)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11951.166 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `382.0` → IC=+0.159 (n=1216)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 382.0 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.162 (n=1537)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.2957` → IC=+0.166 (n=1535)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2957 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.173 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=723)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.591` → IC=+0.196 (n=1535)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.591 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1334` → IC=+0.168 (n=1518)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1334 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.882` → IC=+0.197 (n=302)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.882 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2113` → IC=+0.160 (n=1535)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2113 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.2275` → IC=+0.145 (n=1575)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.2275 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.0697` → IC=+0.148 (n=688)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0697 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4679` → IC=+0.151 (n=1423)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4679 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7587` → IC=+0.141 (n=949)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7587 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.176 (n=449)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 208.0 (IC base=+0.142)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.229 (n=540)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2482` → IC=+0.221 (n=1080)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2482 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.494` → IC=+0.286 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.494 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.1276` → IC=+0.211 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1276 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.7274` → IC=+0.220 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7274 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1923)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2009.7484` → IC=+0.216 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.7484 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.240 (n=1226)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.0995` → IC=+0.265 (n=465)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0995 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.278 (n=484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.3509` → IC=+0.248 (n=1394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3509 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.663` → IC=+0.253 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.663 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3528` → IC=+0.258 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3528 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.238 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.1697` → IC=+0.226 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1697 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1933.3634` → IC=+0.229 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.3634 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.217 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.222)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.183 (n=1378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0065 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.4219` → IC=+0.166 (n=1564)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4219 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3395` → IC=+0.205 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3395 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1434` → IC=+0.186 (n=1022)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1434 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.224 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.164 (n=1043)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.856 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.174 (n=652)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4275` → IC=+0.171 (n=511)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4275 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.5215` → IC=+0.163 (n=511)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.5215 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5128.1918` → IC=+0.194 (n=1042)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 5128.1918 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.154 (n=1500)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 153.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.156 (n=1630)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0071 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3834` → IC=+0.146 (n=1630)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3834 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6656` → IC=+0.179 (n=1630)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6656 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.1504` → IC=+0.146 (n=1592)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1504 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.865` → IC=+0.164 (n=564)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.865 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.153 (n=1087)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8554 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.180 (n=242)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8129` → IC=+0.137 (n=1004)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8129 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.5362` → IC=+0.131 (n=502)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5362 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `4266.2624` → IC=+0.158 (n=1087)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4266.2624 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.126 (n=1278)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 127.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.160 (n=804)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.01 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.4552` → IC=+0.128 (n=1561)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4552 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=1814)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.5066` → IC=+0.215 (n=1773)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5066 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `1.0724` → IC=+0.213 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0724 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.866` → IC=+0.261 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.866 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2106` → IC=+0.137 (n=1774)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2106 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `0.6502` → IC=+0.131 (n=1773)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6502 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1617` → IC=+0.133 (n=1782)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1617 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.126 (n=736)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5384` → IC=+0.144 (n=754)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5384 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=1852)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2388.5554` → IC=+0.182 (n=1182)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2388.5554 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.144 (n=1413)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 47.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.163 (n=791)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0062 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1031` → IC=+0.174 (n=597)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1031 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=1807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5789` → IC=+0.217 (n=1791)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5789 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0011` → IC=+0.123 (n=234)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 1.0011 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.1985` → IC=+0.148 (n=1645)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1985 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.436` → IC=+0.132 (n=734)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 3.436 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6382` → IC=+0.153 (n=597)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6382 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.162 (n=223)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4467` → IC=+0.139 (n=546)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4467 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4215` → IC=+0.131 (n=546)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4215 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2743.5857` → IC=+0.183 (n=811)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2743.5857 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.128 (n=1590)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 52.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.228 (n=1666)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.2914` → IC=+0.216 (n=1111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2914 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=754)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.245 (n=1670)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.2034` → IC=+0.214 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2034 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.6` → IC=+0.246 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.6 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.1937` → IC=+0.212 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1937 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.218 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6237 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.271 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.47` → IC=+0.212 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.47 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4217` → IC=+0.214 (n=1614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4217 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1628)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2466.2754` → IC=+0.209 (n=1488)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2466.2754 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.229 (n=753)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.216 (n=776)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.236 (n=571)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.235 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.4286` → IC=+0.244 (n=1711)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4286 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `1.1821` → IC=+0.231 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1821 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.355` → IC=+0.250 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.355 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.639` → IC=+0.223 (n=1711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.639 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.274 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `2.2006` → IC=+0.204 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2006 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4366` → IC=+0.212 (n=1566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4366 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2404.9954` → IC=+0.219 (n=1529)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2404.9954 (IC base=+0.212)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.192 (n=1129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0042 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.169 (n=853)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0084 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3431` → IC=+0.179 (n=2248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3431 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=1264)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.3437` → IC=+0.197 (n=2554)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3437 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.7982` → IC=+0.189 (n=406)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.7982 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.743` → IC=+0.195 (n=1118)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.743 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.189 (n=1517)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8725 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.173 (n=2275)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.6213 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.163` → IC=+0.178 (n=681)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.163 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4373` → IC=+0.185 (n=826)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4373 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.174 (n=1653)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.173 (n=2902)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2682.644` → IC=+0.170 (n=2282)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2682.644 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.187 (n=2335)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 144.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.153 (n=878)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0037 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.190 (n=876)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0714 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.0752` → IC=+0.121 (n=996)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.0752 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `1.4408` → IC=+0.143 (n=848)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4408 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2749.8` → IC=+0.124 (n=2343)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2749.8 (IC base=+0.106)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.124 (n=1105)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 28.0 (IC base=+0.106)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.201 (n=302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.3311` → IC=+0.166 (n=683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3311 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.183 (n=632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.6364` → IC=+0.207 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6364 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.287` → IC=+0.168 (n=236)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.287 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.181` → IC=+0.166 (n=297)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.181 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.952` → IC=+0.145 (n=717)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.952 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.892` → IC=+0.172 (n=456)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.892 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.157` → IC=+0.147 (n=712)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.157 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.148 (n=271)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.2348` → IC=+0.150 (n=586)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.2348 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.5129` → IC=+0.152 (n=595)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5129 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `10742.0445` → IC=+0.154 (n=683)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 10742.0445 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.192 (n=290)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 154.0 (IC base=+0.145)

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
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.260 (n=352)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.212` → IC=+0.227 (n=533)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.212 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.3605` → IC=+0.238 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3605 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.3651` → IC=+0.216 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3651 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.2103` → IC=+0.209 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2103 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.09` → IC=+0.226 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.09 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `0.8419` → IC=+0.216 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8419 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `1.182` → IC=+0.221 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.182 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.1552` → IC=+0.235 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1552 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.4188` → IC=+0.240 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4188 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.4387` → IC=+0.236 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4387 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.123 (n=515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 11.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.0873` → IC=+0.144 (n=251)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.0873 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6872` → IC=+0.140 (n=331)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6872 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `7846.5169` → IC=+0.134 (n=501)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 7846.5169 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4783` → IC=-0.120 (n=264)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4783
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=514)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.157 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0071 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.170 (n=604)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0051 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.5376` → IC=+0.158 (n=604)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.5376 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 8.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.9607` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9607 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.363` → IC=+0.216 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.363 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.0671` → IC=+0.176 (n=532)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0671 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.6528` → IC=+0.165 (n=604)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6528 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.17` → IC=+0.169 (n=167)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.17 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.482` → IC=+0.158 (n=583)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.482 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.1945` → IC=+0.169 (n=264)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.1945 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.162 (n=639)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `3080.6393` → IC=+0.196 (n=202)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3080.6393 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.4783` → IC=+0.149 (n=514)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.4783 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.5687` → IC=+0.128 (n=245)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5687 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `2878.0292` → IC=+0.152 (n=265)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2878.0292 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.128 (n=358)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 23.0 (IC base=+0.058)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.178 (n=4202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0047 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.210 (n=4190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=13124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.9934` → IC=+0.309 (n=4184)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9934 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.9142` → IC=+0.200 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9142 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.369` → IC=+0.250 (n=3097)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.369 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `0.88` → IC=+0.172 (n=5613)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.88 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.201 (n=1703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.587` → IC=+0.197 (n=4045)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.587 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1811.12` → IC=+0.179 (n=12551)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1811.12 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.202 (n=9851)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=7549)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1487` → IC=+0.192 (n=4971)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1487 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=4278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.4523` → IC=+0.247 (n=9941)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4523 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2447` → IC=+0.163 (n=7039)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2447 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.045` → IC=+0.203 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.045 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.73` → IC=+0.184 (n=10907)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.73 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.163 (n=3373)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7049 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.246 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6067` → IC=+0.191 (n=3509)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6067 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1742.04` → IC=+0.183 (n=11295)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1742.04 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.205 (n=6835)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.244 (n=697)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.225 (n=696)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.3602` → IC=+0.209 (n=2085)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3602 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.223 (n=1013)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=1395)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.330 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.354 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2729` → IC=+0.260 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2729 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.2375` → IC=+0.214 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2375 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2042.27` → IC=+0.217 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.27 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.264 (n=1136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.262 (n=1707)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1255` → IC=+0.283 (n=750)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1255 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3605` → IC=+0.284 (n=1499)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3605 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.511` → IC=+0.262 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.511 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.293 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.6218` → IC=+0.276 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6218 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1592.1` → IC=+0.269 (n=1703)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1592.1 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.209 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.162 (n=1343)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=2106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.2865` → IC=+0.204 (n=2013)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2865 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1252` → IC=+0.185 (n=1142)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1252 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.75` → IC=+0.181 (n=340)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 11.75 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.184` → IC=+0.149 (n=1841)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.184 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6998` → IC=+0.167 (n=886)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6998 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.198 (n=286)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.132` → IC=+0.159 (n=1722)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.132 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.5125` → IC=+0.153 (n=1748)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5125 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `277.0` → IC=+0.173 (n=833)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 277.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1687)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.3291` → IC=+0.159 (n=1687)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3291 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.151 (n=768)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.2922` → IC=+0.240 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2922 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1302` → IC=+0.164 (n=1538)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1302 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.516` → IC=+0.156 (n=283)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.516 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.315` → IC=+0.147 (n=1534)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.315 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.1888` → IC=+0.159 (n=1687)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1888 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1532` → IC=+0.200 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1532 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.157 (n=1588)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.159 (n=1059)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `348.0` → IC=+0.146 (n=1003)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 348.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.257 (n=684)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=1842)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.402` → IC=+0.302 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.402 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.2061` → IC=+0.224 (n=2063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2061 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.6207` → IC=+0.228 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6207 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2447)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1946.6584` → IC=+0.231 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1946.6584 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.241 (n=1698)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.245 (n=849)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0141` → IC=+0.302 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0141 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.186` → IC=+0.275 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.186 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3426` → IC=+0.293 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3426 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7349` → IC=+0.236 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7349 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.1508` → IC=+0.239 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1508 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1933.251` → IC=+0.247 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.251 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.234 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.233)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.194 (n=946)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0039 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4329` → IC=+0.154 (n=2148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4329 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2715` → IC=+0.189 (n=2148)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2715 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3564` → IC=+0.161 (n=826)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3564 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.576` → IC=+0.167 (n=346)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.576 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8733` → IC=+0.163 (n=1432)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8733 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2361` → IC=+0.190 (n=388)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2361 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5213` → IC=+0.162 (n=920)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5213 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1702` → IC=+0.154 (n=947)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1702 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7494.2495` → IC=+0.232 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7494.2495 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.179 (n=680)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 71.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.166 (n=1152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0051 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4447` → IC=+0.140 (n=1725)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4447 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.128 (n=793)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.176 (n=1725)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7333 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1533` → IC=+0.131 (n=1508)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1533 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.265` → IC=+0.163 (n=259)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.265 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.6226` → IC=+0.142 (n=576)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6226 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.220 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `2.2469` → IC=+0.131 (n=1453)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.2469 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.139 (n=1650)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `9209.6094` → IC=+0.200 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9209.6094 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `168.0` → IC=+0.130 (n=1647)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 168.0 (IC base=+0.127)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.144 (n=1436)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0081 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.5688` → IC=+0.130 (n=2152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.5688 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.463` → IC=+0.203 (n=2151)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.463 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `1.0609` → IC=+0.211 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0609 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.559` → IC=+0.246 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.559 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8926` → IC=+0.149 (n=1435)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8926 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1608` → IC=+0.129 (n=2216)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1608 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.8311` → IC=+0.126 (n=1396)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8311 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.456` → IC=+0.128 (n=2094)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.456 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=2187)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2551.935` → IC=+0.233 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2551.935 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.147 (n=1325)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 42.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.186 (n=682)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0057 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.132` → IC=+0.165 (n=682)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.132 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=2115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5128` → IC=+0.235 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5128 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.2176` → IC=+0.140 (n=1694)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2176 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.469` → IC=+0.130 (n=1973)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.469 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6459` → IC=+0.166 (n=683)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6459 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2203` → IC=+0.186 (n=326)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2203 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `2.1459` → IC=+0.135 (n=1654)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1459 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2799.1755` → IC=+0.196 (n=682)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2799.1755 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.137 (n=1638)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 50.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.230 (n=2103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.217 (n=1517)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.262 (n=1886)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.2101` → IC=+0.233 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2101 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.264` → IC=+0.272 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.264 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.0566` → IC=+0.217 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0566 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.6407` → IC=+0.221 (n=2103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6407 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.245 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.5063` → IC=+0.244 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5063 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=2030)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2464.3002` → IC=+0.219 (n=1879)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2464.3002 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.218 (n=737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.229 (n=1001)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0228 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.226 (n=1568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.260 (n=1947)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `1.2168` → IC=+0.217 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2168 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.2144` → IC=+0.216 (n=1957)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2144 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.844` → IC=+0.253 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.844 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `1.2299` → IC=+0.236 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2299 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.279 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4288` → IC=+0.209 (n=2019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4288 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2414.1045` → IC=+0.214 (n=1973)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2414.1045 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.202 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.211)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.163 (n=3716)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.221 (n=1233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.5046` → IC=+0.193 (n=3698)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.5046 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=1392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.182 (n=1684)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.942` → IC=+0.239 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.942 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1691` → IC=+0.190 (n=1378)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1691 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.4398` → IC=+0.180 (n=2439)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.4398 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.223` → IC=+0.214 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.223 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.7117` → IC=+0.187 (n=1120)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.7117 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.8944` → IC=+0.183 (n=1697)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.8944 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.1685` → IC=+0.209 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1685 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.4535` → IC=+0.192 (n=1217)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4535 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.8601` → IC=+0.186 (n=2433)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8601 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=2758)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `2917.107` → IC=+0.189 (n=3304)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2917.107 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.218 (n=933)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.487` → IC=+0.177 (n=2799)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.487 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=1262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.1827` → IC=+0.186 (n=1232)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1827 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.6573` → IC=+0.182 (n=523)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6573 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` < `0.2355` → IC=+0.155 (n=2483)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2355 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.212` → IC=+0.171 (n=2793)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.212 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.2566` → IC=+0.167 (n=2635)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2566 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.168 (n=2556)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.5356` → IC=+0.170 (n=1216)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5356 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.8264` → IC=+0.172 (n=1842)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8264 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=3716)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `5231.3826` → IC=+0.165 (n=2500)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5231.3826 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.167 (n=1821)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.164 (n=528)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0039 (IC base=+0.082)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.126 (n=548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 16.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.6473` → IC=+0.179 (n=984)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6473 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1412` → IC=+0.145 (n=604)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1412 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.465` → IC=+0.191 (n=257)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.465 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.193 (n=151)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.082)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.121 (n=455)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0056 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.2308` → IC=+0.260 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2308 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.1993` → IC=+0.136 (n=484)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1993 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.082` → IC=+0.148 (n=370)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.082 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.1407` → IC=+0.204 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1407 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `2.581` → IC=+0.152 (n=380)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.581 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` > `1.7271` → IC=+0.147 (n=253)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7271 (IC base=+0.054)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.141 (n=410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0058 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.120 (n=414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.4301` → IC=+0.168 (n=378)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.4301 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1188` → IC=+0.163 (n=203)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1188 (IC base=+0.095)

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
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=162)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.153 (n=263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0047 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.133 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.7146` → IC=+0.218 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7146 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1242` → IC=+0.180 (n=201)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1242 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.779` → IC=+0.279 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.779 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `0.8` → IC=+0.135 (n=242)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.7889` → IC=+0.146 (n=207)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.7889 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `1137.4035` → IC=+0.155 (n=320)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1137.4035 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.7058` → IC=+0.143 (n=127)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.7058 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.003)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.011` → IC=-0.261 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=135)

- **FILTRO** `ibs_20min` > `0.2105` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2105
  - _Potencial_: sin este filtro IC_bueno=+0.264 (n=104)

- **PATRÓN** `ibs_20min` > `0.7778` → IC=+0.168 (n=242)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.7778 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.58` → IC=+0.146 (n=77)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 9.58 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2355` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2355 (IC base=+0.051)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.150 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.011 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.2105` → IC=+0.264 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2105 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.93` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.93 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` < `0.84` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.84 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.9843` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.9843 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.1345` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1345 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `2.5569` → IC=+0.198 (n=84)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.5569 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` > `1.8571` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8571 (IC base=+0.047)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.06 (IC base=+0.047)

- **PATRÓN** `libro_liquidez` > `595.3258` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 595.3258 (IC base=+0.047)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.300 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=184)

- **FILTRO** `dist_vwap_pct` > `0.2381` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=227)

- **FILTRO** `volumen_regimen` < `0.7363` → IC=-0.355 (n=60)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7363
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=182)

- **FILTRO** `sigma_h` > `0.0057` → IC=-0.368 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=157)

- **FILTRO** `dist_vwap_pct` > `0.3328` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3328
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=175)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=178)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=97)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.238 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=40)

- **FILTRO** `volumen_regimen` < `1.2353` → IC=-0.262 (n=40)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2353
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=40)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=65)

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

- **FILTRO** `sigma_h` < `0.0039` → IC=-0.288 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=27)

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
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=67)

- **FILTRO** `ibs_20min` < `0.125` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.125
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=64)

- **FILTRO** `volumen_spike_ratio` < `1.6219` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.6219
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=39)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=57)

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
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.177 (n=162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0058 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.134 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.6472` → IC=+0.143 (n=354)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6472 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.4856` → IC=+0.199 (n=81)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.4856 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.6625` → IC=+0.133 (n=118)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.6625 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `2.4417` → IC=+0.121 (n=254)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4417 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.135 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 14.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.178 (n=321)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.156 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.664` → IC=+0.214 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.664 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `2.6699` → IC=+0.129 (n=289)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.6699 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `3965.7979` → IC=+0.191 (n=166)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3965.7979 (IC base=+0.082)

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
- **FILTRO** `libro_liquidez` < `1555.6741` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `libro_liquidez` < 1555.6741
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=100)

- **FILTRO** `ibs_20min` > `0.2038` → IC=-0.127 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2038
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=112)

- **PATRÓN** `libro_liquidez` > `1555.6741` → IC=+0.157 (n=100)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1555.6741 (IC base=+0.053)

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
  - _Potencial_: sin este filtro IC_bueno=+0.219 (n=30)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.279 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.248 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.7358` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7358 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.226 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.6388` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6388 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` < `0.1348` → IC=+0.222 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1348 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.268 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.0151` → IC=+0.268 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0151 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.11` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.11 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.818` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.818 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0941` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0941 (IC base=-0.039)

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
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.120 (n=1123)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.495 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2931.0266` → IC=+0.155 (n=323)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2931.0266 (IC base=+0.109)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.120 (n=1123)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.495 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2931.0266` → IC=+0.155 (n=323)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2931.0266 (IC base=+0.109)

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
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=2500)

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

  - _Acción_: Kelly boost +0.71€ cuando `liq_usd_total` > 129721.58 (IC base=+0.060)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.165 (n=156)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.495 (IC base=+0.060)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=989)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=943)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=579)

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
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=288)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.179 (n=104)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.495 (IC base=+0.033)

- **PATRÓN** `libro_liquidez` > `3946.3264` → IC=+0.141 (n=104)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3946.3264 (IC base=+0.033)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=751)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=751)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.131 (n=242)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=589)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=485)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=485)

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
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=116)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=129)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=289)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=289)

- **FILTRO** `libro_liquidez` < `553.2637` → IC=-0.136 (n=105)

  - _Acción_: SKIP cuando `libro_liquidez` < 553.2637
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=214)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=175)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.48` → IC=-0.120 (n=1393)

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
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=197)

- **PATRÓN** `py_entrada` < `0.48` → IC=+0.145 (n=91)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.48 (IC base=+0.018)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.043)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=55)

- **FILTRO** `restante_min` < `10.16` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `restante_min` < 10.16
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=94)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.159 (n=42)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=98)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.162 (n=4436)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=13434)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.164 (n=4617)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=13876)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.197 (n=783)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2381)

- **PATRÓN** `libro_liquidez` > `1806.42` → IC=+0.132 (n=1076)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1806.42 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `1581.1195` → IC=+0.147 (n=1125)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1581.1195 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.179 (n=781)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2429)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=776)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=2575)

- **PATRÓN** `libro_liquidez` > `1803.3584` → IC=+0.134 (n=1092)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 1803.3584 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.162 (n=762)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=2391)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2431)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3171)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=12468)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=27862)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=9473)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=30857)

- **FILTRO** `ibs_7min` < `0.2614` → IC=-0.233 (n=10077)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2614
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=30253)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=13649)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=26681)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.235 (n=12450)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=38688)

- **FILTRO** `ibs_7min` > `0.2906` → IC=-0.181 (n=12782)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2906
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=38356)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.141 (n=2030)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4813)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.307 (n=1639)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=5204)

- **FILTRO** `ibs_7min` < `0.708` → IC=-0.251 (n=2257)

  - _Acción_: SKIP cuando `ibs_7min` < 0.708
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=4586)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.183 (n=1542)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5301)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.264 (n=2167)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6672)

- **FILTRO** `ibs_7min` > `0.7875` → IC=-0.209 (n=2209)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7875
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6630)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.132 (n=1637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5258)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.249 (n=1695)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=5200)

- **FILTRO** `ibs_7min` < `0.7432` → IC=-0.196 (n=1723)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7432
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=5172)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.177 (n=1712)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=5183)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.265 (n=1647)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5378)

- **FILTRO** `ibs_7min` > `0.2635` → IC=-0.193 (n=1755)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2635
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5270)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.189 (n=1751)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5274)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.160 (n=1610)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=4885)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=1544)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4951)

- **FILTRO** `ibs_7min` < `0.703` → IC=-0.246 (n=2143)

  - _Acción_: SKIP cuando `ibs_7min` < 0.703
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4352)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.214 (n=1508)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4987)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.244 (n=2164)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=7277)

- **FILTRO** `ibs_7min` > `0.7416` → IC=-0.174 (n=2360)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7416
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=7081)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.237 (n=1974)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4657)

- **FILTRO** `ibs_7min` < `0.7406` → IC=-0.185 (n=1657)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7406
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4974)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.178 (n=1615)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=5016)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=1691)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=5130)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.180 (n=1704)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5117)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.184 (n=1673)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=5148)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.264 (n=1711)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=5144)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.231 (n=1681)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5174)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=2329)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=7425)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.272 (n=1562)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=5049)

- **FILTRO** `ibs_7min` < `0.2593` → IC=-0.221 (n=1652)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2593
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4959)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.199 (n=1646)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=4965)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.209 (n=2146)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=7112)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1206)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=607)

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
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=486)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.135 (n=894)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.139 (n=411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.121)

- **PATRÓN** `total_vol_5m` < `442.4725` → IC=+0.151 (n=299)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 442.4725 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.129 (n=760)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 53.0 (IC base=+0.121)

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
- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.162 (n=72)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 10.0 (IC base=+0.108)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.185 (n=122)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.203 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.114)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.211 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 73.0 (IC base=+0.114)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.169 (n=161)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.84€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.189 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `8082.459` → IC=+0.156 (n=161)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 8082.459 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 28.0 (IC base=+0.139)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4006` → IC=+0.143 (n=155)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4006 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.124 (n=155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 13.0 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `3602.5746` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3602.5746 (IC base=+0.101)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.75` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.75
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=113)

- **FILTRO** `sigma_h` > `0.0044` → IC=-0.234 (n=332)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=165)

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
- **FILTRO** `sigma_h` > `0.0087` → IC=-0.192 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0087
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=26)

- **FILTRO** `pct_vs_K` |x|> `9.1619` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.1619
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=34)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.196 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0087` → IC=-0.178 (n=302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=157)

- **FILTRO** `T_h` > `72.5264` → IC=-0.150 (n=344)

  - _Acción_: SKIP cuando `T_h` > 72.5264
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=115)

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

- **FILTRO** `sigma_h` < `0.0073` → IC=-0.200 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=86)

- **FILTRO** `T_h` > `135.1248` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `T_h` > 135.1248
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=86)

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

- **PATRÓN** `edge` > `0.096` → IC=+0.454 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.421)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.433 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.421)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.448 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.421)

- **PATRÓN** `T_h` < `0.9836` → IC=+0.431 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9836 (IC base=+0.421)

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

- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.065)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=529)

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
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=752)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=904)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=894)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3323)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1721)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.211 (n=722)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.244 (n=722)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.1592` → IC=+0.206 (n=1907)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1592 (IC base=+0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2213` → IC=+0.215 (n=722)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2213 (IC base=+0.203)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1283` → IC=+0.233 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1283 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=2009)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=2234)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `ibs_15` > `0.619` → IC=+0.282 (n=2166)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.619 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.118` → IC=+0.205 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.118 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.798` → IC=+0.277 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.798 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2950.6032` → IC=+0.208 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2950.6032 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.222 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.203)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=926)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.230 (n=454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.279 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.217)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.258 (n=151)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.217)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.273 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=421)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.217)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.279 (n=454)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.3854` → IC=+0.273 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3854 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.270 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `16113.4131` → IC=+0.253 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16113.4131 (IC base=+0.217)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.849` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.849
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=554)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.201 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0669` → IC=+0.167 (n=217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0669 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2356` → IC=+0.183 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio_macro` |x|> 0.2356 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1204` → IC=+0.165 (n=186)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1204 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.164 (n=355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.149 (n=517)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5797` → IC=+0.237 (n=493)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5797 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2773` → IC=+0.157 (n=455)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.2773 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.56` → IC=+0.232 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.56 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3426.0142` → IC=+0.161 (n=441)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3426.0142 (IC base=+0.146)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.293 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.1505` → IC=+0.210 (n=236)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1505 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0606` → IC=+0.200 (n=268)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0606 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3456` → IC=+0.240 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3456 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=239)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.5897` → IC=+0.274 (n=268)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5897 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.216 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.367` → IC=+0.352 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.367 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=181)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `3089.3424` → IC=+0.282 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3089.3424 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.224 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.188)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.000)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0232` → IC=+0.288 (n=182)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0232 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.0837` → IC=+0.227 (n=240)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0837 (IC base=+0.213)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0429` → IC=+0.217 (n=545)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0429 (IC base=+0.213)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0875` → IC=+0.263 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0875 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.243 (n=270)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.213)

- **PATRÓN** `ibs_15` > `0.5849` → IC=+0.297 (n=545)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5849 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.1332` → IC=+0.225 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1332 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.5569` → IC=+0.213 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5569 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.241` → IC=+0.250 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.241 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.277` → IC=+0.216 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.277 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2842.5383` → IC=+0.279 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2842.5383 (IC base=+0.213)

- **PATRÓN** `ibs_15` < `0.1148` → IC=+0.145 (n=603)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.72€ cuando `ibs_15` < 0.1148 (IC base=+0.059)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.370 (n=336)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.359)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.377 (n=168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.359)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.361 (n=337)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.359)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.384 (n=335)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.359)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1316` → IC=+0.393 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1316 (IC base=+0.359)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.403 (n=245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.359)

- **PATRÓN** `ibs_15` > `0.7862` → IC=+0.397 (n=504)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7862 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.388 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.247` → IC=+0.368 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.247 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.358 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.359)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `3813.5418` → IC=+0.376 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3813.5418 (IC base=+0.359)

- **PATRÓN** `ballena_activa_n` < `446.0` → IC=+0.381 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 446.0 (IC base=+0.359)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1124` → IC=+0.371 (n=122)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1124 (IC base=+0.364)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.373 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.363 (n=246)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.372 (n=92)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.364)

- **PATRÓN** `drift_15min` |x|≤ `0.5146` → IC=+0.371 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5146 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1537` → IC=+0.387 (n=183)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1537 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.398 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.385 (n=276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.8057` → IC=+0.396 (n=276)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8057 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.2544` → IC=+0.398 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2544 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.032` → IC=+0.370 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.032 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.364 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `16045.3097` → IC=+0.383 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16045.3097 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `502.0` → IC=+0.416 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 502.0 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.354 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.350)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.368 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.350)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.364 (n=153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.350)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.369 (n=204)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.350)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.376 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.350)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.411 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.350)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.400 (n=228)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.350)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.373 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.350)

- **PATRÓN** `dist_vwap_pct` < `0.2966` → IC=+0.352 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2966 (IC base=+0.350)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.031` → IC=+0.365 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.031 (IC base=+0.350)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.353 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.350)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.356 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.350)

- **PATRÓN** `libro_liquidez` > `4242.86` → IC=+0.372 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4242.86 (IC base=+0.350)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.357 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.350)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0123` → IC=-0.219 (n=812)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0123
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=2439)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.201 (n=1165)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1412` → IC=+0.183 (n=528)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio_macro` |x|> 0.1412 (IC base=-0.061)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1365` → IC=+0.246 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1365 (IC base=-0.061)

- **PATRÓN** `ibs_15` > `0.6409` → IC=+0.278 (n=792)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6409 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.196 (n=452)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1047 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` < `0.2631` → IC=+0.201 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2631 (IC base=-0.061)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1246` → IC=+0.248 (n=1635)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1246 (IC base=-0.022)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1822` → IC=+0.249 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1822 (IC base=-0.022)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.274 (n=2457)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.022)

- **PATRÓN** `dist_vwap_pct` > `0.6528` → IC=+0.293 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6528 (IC base=-0.022)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.243 (n=2139)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=-0.022)

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

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.177 (n=187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0027 (IC base=+0.089)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.307 (n=107)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.089)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.126 (n=380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 12.0 (IC base=+0.089)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.335 (n=235)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.0996` → IC=+0.293 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0996 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.2353` → IC=+0.278 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2353 (IC base=+0.089)

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
  - _Potencial_: sin este filtro IC_bueno=+0.168 (n=495)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.162 (n=385)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0064 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.173 (n=344)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0038 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.0735` → IC=+0.213 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0735 (IC base=+0.158)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.158 (n=384)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.158)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2962` → IC=+0.220 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2962 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.185 (n=274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 11.0 (IC base=+0.158)

- **PATRÓN** `ibs_15` > `0.6526` → IC=+0.260 (n=385)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6526 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` < `0.2773` → IC=+0.170 (n=355)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.2773 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.201 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=495)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `11347.841` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 11347.841 (IC base=+0.158)

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
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.206 (n=569)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=190)

- **FILTRO** `drift_60min` |x|> `0.1682` → IC=-0.238 (n=258)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=501)

- **FILTRO** `drift_15min` |x|> `0.89` → IC=-0.275 (n=189)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=570)

- **FILTRO** `sigma_ewma_delta_pct` > `18.27` → IC=-0.143 (n=404)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.27
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.159 (n=42)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.173)

- **PATRÓN** `ibs_15` > `0.6071` → IC=+0.224 (n=56)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6071 (IC base=-0.173)

- **PATRÓN** `dist_vwap_pct` < `0.1248` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1248 (IC base=-0.173)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 44.0 (IC base=-0.173)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0777` → IC=+0.228 (n=358)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0777 (IC base=-0.040)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1843` → IC=+0.229 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1843 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.3462` → IC=+0.269 (n=400)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3462 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.6758` → IC=+0.235 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6758 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.1683` → IC=+0.234 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1683 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1319` → IC=-0.209 (n=459)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1319
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=461)

- **FILTRO** `sigma_h` > `0.0195` → IC=-0.259 (n=459)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.137 (n=461)

- **FILTRO** `drift_60min` |x|> `0.1552` → IC=-0.201 (n=229)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1552
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=691)

- **FILTRO** `drift_15min` |x|> `1.2315` → IC=-0.275 (n=229)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2315
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=691)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.199)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.199)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1454` → IC=+0.269 (n=284)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1454 (IC base=-0.034)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1693` → IC=+0.302 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1693 (IC base=-0.034)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.294 (n=623)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` > `1.0955` → IC=+0.354 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0955 (IC base=-0.034)

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
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.305 (n=543)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.329 (n=272)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2408` → IC=+0.309 (n=271)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2408 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2191` → IC=+0.317 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2191 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.327 (n=814)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.4372` → IC=+0.336 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4372 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.341 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12879.5491` → IC=+0.303 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12879.5491 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.308 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.334 (n=149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.288)

- **PATRÓN** `drift_15min` |x|≤ `0.4183` → IC=+0.288 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4183 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2073` → IC=+0.313 (n=201)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2073 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3977` → IC=+0.305 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3977 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8303` → IC=+0.318 (n=444)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8303 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.2565` → IC=+0.343 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2565 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `16193.642` → IC=+0.327 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16193.642 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.307 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.296)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.301 (n=370)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.318 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2883` → IC=+0.321 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2883 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.326 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8722` → IC=+0.350 (n=331)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8722 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.308 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.564` → IC=+0.323 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.564 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0878` → IC=-0.263 (n=74)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0878
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=225)

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

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1065` → IC=-0.200 (n=18)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1065
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=23)

- **FILTRO** `sigma_h` > `0.0054` → IC=-0.182 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.619 sube el IC de +0.203 a +0.282 en UPDOWN_GBM#15min (n=2166). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.217 a +0.279 en UPDOWN_GBM#BTC#15min (n=454). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5797 sube el IC de +0.146 a +0.237 en UPDOWN_GBM#ETH#15min (n=493). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5897 sube el IC de +0.188 a +0.274 en UPDOWN_GBM#SOL#15min (n=268). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5849 sube el IC de +0.213 a +0.297 en UPDOWN_GBM#XRP#15min (n=545). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6409 sube el IC de -0.061 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=792). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.022 a +0.274 en UPDOWN_GBM_15M_TARDIO (n=2457). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.089 a +0.335 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=235). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.501 sube el IC de -0.193 a +0.306 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6526 sube el IC de +0.158 a +0.260 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=385). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3647 sube el IC de +0.234 a +0.266 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=918). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.6071 sube el IC de -0.173 a +0.224 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=56). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3462 sube el IC de -0.040 a +0.269 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=400). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.199 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.034 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=623). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.292 a +0.327 en UPDOWN_GBM_IBS_ALTO (n=814). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.288 a +0.318 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=444). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8722 sube el IC de +0.296 a +0.350 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=331). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.359 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=504). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.364 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=276). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.350 a +0.400 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=228). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1517 | +0.097 | +193.06€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1517 | +0.097 | +193.06€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1152 | +0.105 | +166.66€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1152 | +0.105 | +166.66€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 262 | +0.064 | +10.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 262 | +0.064 | +10.69€ | 6 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 113 | +0.013 | +17.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 113 | +0.013 | +17.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 91 | +0.027 | +15.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 91 | +0.027 | +15.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 32785 | -0.089 | -4302.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1685 | -0.019 | -218.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 31100 | -0.093 | -4083.18€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4237 | -0.116 | -710.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4237 | -0.116 | -710.48€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1685 | -0.019 | -218.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1685 | -0.019 | -218.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3865 | -0.114 | -866.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3865 | -0.114 | -866.42€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8453 | -0.005 | -761.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8453 | -0.005 | -761.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8181 | -0.106 | -534.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8181 | -0.106 | -534.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6364 | -0.166 | -1209.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6364 | -0.166 | -1209.95€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 24415 | -0.021 | +3670.39€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6318 | +0.001 | +1736.92€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 18097 | -0.029 | +1933.47€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 24415 | -0.021 | +3670.39€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6318 | +0.001 | +1736.92€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 18097 | -0.029 | +1933.47€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 111935 | +0.113 | -5129.88€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15892 | +0.183 | -483.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 472 | -0.055 | -59.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 88566 | +0.102 | -4323.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7005 | +0.104 | -263.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 14711 | +0.101 | -1082.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 52 | -0.130 | +12.55€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 14644 | +0.103 | -1083.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 22275 | +0.131 | -342.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4813 | +0.199 | -120.54€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 14685 | +0.116 | -138.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2735 | +0.092 | -61.07€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 14757 | +0.093 | -1225.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 60 | -0.113 | -5.60€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 14682 | +0.094 | -1208.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 23776 | +0.124 | -432.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6372 | +0.176 | -102.13€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 14849 | +0.106 | -263.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2543 | +0.100 | -58.69€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 21687 | +0.114 | -1202.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4541 | +0.187 | -277.64€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 375 | -0.017 | -5.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 15044 | +0.094 | -775.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1727 | +0.130 | -143.98€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 14729 | +0.101 | -844.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 54 | -0.036 | +10.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 14662 | +0.101 | -854.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 17853 | +0.194 | -1109.98€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 17853 | +0.194 | -1109.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4161 | +0.174 | -389.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4161 | +0.174 | -389.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1853 | +0.202 | -24.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1853 | +0.202 | -24.32€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4099 | +0.181 | -335.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4099 | +0.181 | -335.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3618 | +0.243 | -117.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3618 | +0.243 | -117.92€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4043 | +0.190 | -256.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4043 | +0.190 | -256.41€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 834 | +0.432 | -19.93€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 834 | +0.432 | -19.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 328 | +0.442 | -0.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 328 | +0.442 | -0.09€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 316 | +0.434 | -5.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 316 | +0.434 | -5.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 178 | +0.406 | -12.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 178 | +0.406 | -12.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 61924 | +0.199 | -4663.29€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 61924 | +0.199 | -4663.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10654 | +0.181 | -1154.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10654 | +0.181 | -1154.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9944 | +0.224 | -348.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9944 | +0.224 | -348.02€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10669 | +0.175 | -1223.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10669 | +0.175 | -1223.60€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10015 | +0.220 | -373.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10015 | +0.220 | -373.61€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10253 | +0.203 | -669.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10253 | +0.203 | -669.49€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10389 | +0.193 | -893.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10389 | +0.193 | -893.67€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 23549 | +0.116 | +130.68€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 23549 | +0.116 | +130.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 11693 | +0.119 | +127.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 11693 | +0.119 | +127.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 11856 | +0.112 | +3.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 11856 | +0.112 | +3.62€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1697 | +0.288 | -26.36€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1697 | +0.288 | -26.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 763 | +0.278 | -20.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 763 | +0.278 | -20.73€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 819 | +0.288 | -9.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 819 | +0.288 | -9.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 115 | +0.346 | +3.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 115 | +0.346 | +3.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 756 | +0.439 | +1.04€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 756 | +0.439 | +1.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 362 | +0.437 | -2.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 362 | +0.437 | -2.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 348 | +0.443 | +2.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 348 | +0.443 | +2.55€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1302 | +0.070 | -60.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 465 | +0.057 | -38.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 837 | +0.077 | -21.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1023 | +0.077 | -28.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 186 | +0.074 | -6.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 837 | +0.077 | -21.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 213 | +0.026 | -33.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 213 | +0.026 | -33.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 44891 | +0.099 | -1227.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3648 | +0.092 | +49.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 41243 | +0.100 | -1276.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 24935 | +0.104 | -308.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3648 | +0.092 | +49.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 21287 | +0.106 | -357.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8827 | +0.107 | -49.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8827 | +0.107 | -49.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 11129 | +0.081 | -869.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 11129 | +0.081 | -869.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 865 | +0.206 | -102.69€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 865 | +0.206 | -102.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 865 | +0.206 | -102.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 865 | +0.206 | -102.69€ | 1 | 4 |
| ✅ GBM_LATE_15M | 31555 | +0.087 | +15608.35€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 31555 | +0.087 | +15608.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5304 | +0.202 | +4068.23€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5304 | +0.202 | +4068.23€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 4689 | +0.177 | +3355.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4689 | +0.177 | +3355.30€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 5598 | +0.199 | +4206.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5598 | +0.199 | +4206.58€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4479 | +0.030 | +1121.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4479 | +0.030 | +1121.92€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4500 | -0.031 | +995.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4500 | -0.031 | +995.48€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6985 | -0.036 | +1860.84€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6985 | -0.036 | +1860.84€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 33945 | +0.087 | +18101.81€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 33945 | +0.087 | +18101.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6529 | +0.012 | +3387.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6529 | +0.012 | +3387.12€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7048 | +0.015 | +1494.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7048 | +0.015 | +1494.22€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4811 | +0.267 | +4934.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4811 | +0.267 | +4934.05€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5680 | +0.009 | +1265.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5680 | +0.009 | +1265.28€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5506 | +0.035 | +2219.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5506 | +0.035 | +2219.10€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4371 | +0.284 | +4802.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4371 | +0.284 | +4802.05€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 25330 | +0.173 | +19650.17€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 25330 | +0.173 | +19650.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3818 | +0.217 | +3198.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3818 | +0.217 | +3198.02€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3990 | +0.149 | +2895.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3990 | +0.149 | +2895.28€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4016 | +0.213 | +3281.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4016 | +0.213 | +3281.03€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4257 | +0.137 | +3145.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4257 | +0.137 | +3145.02€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4748 | +0.123 | +3475.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4748 | +0.123 | +3475.71€ | 0 | 27 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4501 | +0.209 | +3655.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4501 | +0.209 | +3655.11€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6901 | +0.137 | +3246.72€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6901 | +0.137 | +3246.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 339 | +0.142 | +189.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 339 | +0.142 | +189.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2003 | +0.142 | +1070.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2003 | +0.142 | +1070.02€ | 0 | 29 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2066 | +0.152 | +1001.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2066 | +0.152 | +1001.43€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1583 | +0.108 | +573.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1583 | +0.108 | +573.67€ | 1 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 535 | +0.135 | +236.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 535 | +0.135 | +236.68€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 31794 | +0.179 | +24452.83€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 31794 | +0.179 | +24452.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5049 | +0.230 | +4469.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5049 | +0.230 | +4469.39€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4933 | +0.148 | +3203.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4933 | +0.148 | +3203.18€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5307 | +0.227 | +4602.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5307 | +0.227 | +4602.40€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5162 | +0.134 | +3610.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5162 | +0.134 | +3610.95€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5595 | +0.123 | +3884.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5595 | +0.123 | +3884.30€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5748 | +0.212 | +4682.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5748 | +0.212 | +4682.62€ | 0 | 24 |
| ✅ GBM_LATE_5M | 8661 | +0.173 | +5762.61€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 8661 | +0.173 | +5762.61€ | 0 | 0 |
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
| ✅ GBM_LATE_5M#XRP | 1091 | +0.143 | +549.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1091 | +0.143 | +549.35€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2278 | +0.074 | +828.78€ | 0 | 13 |
| ✅ GBM_LATE_60M#60min | 2278 | +0.074 | +828.78€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 856 | +0.093 | +307.38€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 856 | +0.093 | +307.38€ | 0 | 14 |
| ✅ GBM_LATE_60M#ETH | 721 | +0.073 | +324.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 721 | +0.073 | +324.34€ | 1 | 11 |
| ✅ GBM_LATE_60M#SOL | 701 | +0.051 | +197.07€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 701 | +0.051 | +197.07€ | 2 | 13 |
| 🚫 GBM_LATE_60M_FADE | 450 | -0.243 | -13.75€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 450 | -0.243 | -13.75€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 166 | -0.220 | -5.99€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 166 | -0.220 | -5.99€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 156 | -0.234 | -1.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 156 | -0.234 | -1.96€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 128 | -0.277 | -5.81€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 128 | -0.277 | -5.81€ | 7 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 957 | +0.088 | +246.36€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 957 | +0.088 | +246.36€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 355 | +0.080 | +76.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 355 | +0.080 | +76.52€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 317 | +0.058 | +39.57€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 317 | +0.058 | +39.57€ | 2 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 285 | +0.131 | +130.27€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 285 | +0.131 | +130.27€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2621 | +0.104 | +704.41€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2621 | +0.104 | +704.41€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2621 | +0.104 | +704.41€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2621 | +0.104 | +704.41€ | 0 | 2 |
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
| ✅ LIQUIDACIONES_5M | 2701 | +0.024 | +82.61€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2701 | +0.024 | +82.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 134 | +0.029 | -0.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 134 | +0.029 | -0.60€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 392 | +0.038 | +37.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 392 | +0.038 | +37.64€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1038 | +0.033 | +32.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1038 | +0.033 | +32.08€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 619 | +0.015 | +2.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 619 | +0.015 | +2.51€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 317 | +0.024 | +17.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 317 | +0.024 | +17.11€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1331 | -0.046 | -31.02€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1331 | -0.046 | -31.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 380 | -0.042 | -13.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 380 | -0.042 | -13.47€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 442 | -0.027 | -0.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 442 | -0.027 | -0.93€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 509 | -0.066 | -16.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 509 | -0.066 | -16.62€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 4127 | -0.021 | +57.21€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1947 | -0.024 | +6.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2180 | -0.018 | +51.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 114 | +0.000 | +4.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 59 | +0.057 | +10.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 55 | -0.061 | -5.83€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1014 | -0.002 | +43.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 477 | -0.007 | +11.27€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 537 | +0.003 | +31.75€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 466 | -0.021 | +9.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 226 | -0.031 | +0.03€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 240 | -0.012 | +9.34€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 834 | -0.037 | -23.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 381 | -0.051 | -24.58€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 453 | -0.025 | +1.54€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 811 | -0.025 | +9.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 392 | -0.030 | +2.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 419 | -0.020 | +6.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 888 | -0.026 | +14.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 412 | -0.022 | +6.69€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 476 | -0.029 | +7.61€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 36363 | -0.004 | +1745.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 36363 | -0.004 | +1745.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6470 | +0.023 | +849.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6470 | +0.023 | +849.08€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5463 | -0.031 | -61.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5463 | -0.031 | -61.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6561 | +0.019 | +627.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6561 | +0.019 | +627.85€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5253 | -0.053 | -158.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5253 | -0.053 | -158.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6125 | -0.008 | +211.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6125 | -0.008 | +211.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6491 | +0.012 | +276.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6491 | +0.012 | +276.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6114 | -0.059 | -147.04€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6114 | -0.059 | -147.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1490 | -0.079 | -34.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1490 | -0.079 | -34.78€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 91468 | -0.073 | +1746.39€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 91468 | -0.073 | +1746.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 15682 | -0.074 | +929.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 15682 | -0.074 | +929.34€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 13920 | -0.097 | -778.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 13920 | -0.097 | -778.29€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 15936 | -0.066 | +887.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 15936 | -0.066 | +887.15€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 13452 | -0.094 | -356.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 13452 | -0.094 | -356.25€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 16609 | -0.051 | +334.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 16609 | -0.051 | +334.43€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 15869 | -0.063 | +730.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 15869 | -0.063 | +730.01€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7973 | -0.030 | -145.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7973 | -0.030 | -145.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1875 | -0.042 | -19.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1875 | -0.042 | -19.29€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2238 | -0.024 | -28.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2238 | -0.024 | -28.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1087 | -0.047 | -20.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1087 | -0.047 | -20.70€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 770 | -0.022 | -24.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 770 | -0.022 | -24.88€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1328 | +0.115 | +487.27€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1192 | +0.121 | +474.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 278 | +0.139 | +141.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 278 | +0.139 | +141.54€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 225 | +0.108 | +63.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 225 | +0.108 | +63.66€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 244 | +0.114 | +96.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 244 | +0.114 | +96.04€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 214 | +0.139 | +105.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 214 | +0.139 | +105.56€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 231 | +0.101 | +67.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 231 | +0.101 | +67.88€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 829 | -0.021 | -26.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 829 | -0.021 | -26.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 164 | +0.006 | +8.78€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 164 | +0.006 | +8.78€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 118 | -0.017 | -4.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 118 | -0.017 | -4.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 225 | -0.051 | -22.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 225 | -0.051 | -22.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 182 | +0.016 | +6.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 182 | +0.016 | +6.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 140 | -0.056 | -15.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 140 | -0.056 | -15.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 714 | -0.092 | -64.70€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 326 | -0.146 | -77.67€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 255 | -0.189 | -72.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 71 | +0.007 | -4.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 252 | -0.051 | -1.07€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 183 | -0.057 | -4.31€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 69 | -0.035 | +3.24€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 136 | -0.036 | +14.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 108 | -0.054 | +8.12€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 28 | +0.033 | +5.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 546 | -0.119 | -68.98€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 168 | -0.006 | +4.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 861 | -0.201 | -47.19€ | 5 | 0 |
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
| ✅ RESOLUTION_SNIPER | 354 | +0.402 | +287.59€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 90 | +0.370 | +74.48€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 90 | +0.370 | +74.48€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 224 | +0.460 | +214.35€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 224 | +0.460 | +214.35€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 354 | +0.402 | +287.59€ | 0 | 0 |
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
| ✅ STREAK_FADE_5M | 3046 | -0.023 | -126.35€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3046 | -0.023 | -126.35€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 904 | -0.022 | -32.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 904 | -0.022 | -32.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 577 | -0.025 | -24.71€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 577 | -0.025 | -24.71€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1409 | -0.021 | -54.55€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1409 | -0.021 | -54.55€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 85 | -0.052 | -8.44€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 85 | -0.052 | -8.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9507 | +0.020 | +108.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9507 | +0.020 | +108.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2622 | +0.021 | +28.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2622 | +0.021 | +28.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2191 | +0.029 | +51.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2191 | +0.029 | +51.06€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2854 | +0.010 | -0.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2854 | +0.010 | -0.22€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1840 | +0.021 | +29.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1840 | +0.021 | +29.33€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8469 | +0.013 | -42.61€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8469 | +0.013 | -42.61€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3342 | +0.017 | -5.75€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3342 | +0.017 | -5.75€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3372 | +0.011 | -24.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3372 | +0.011 | -24.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1755 | +0.008 | -12.30€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1755 | +0.008 | -12.30€ | 1 | 0 |
| ✅ UPDOWN_GBM | 52655 | +0.041 | +3854.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 13342 | +0.077 | +2765.19€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1767 | +0.006 | +9.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 34263 | +0.034 | +1046.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3094 | +0.004 | +36.58€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 5369 | +0.077 | +705.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1035 | +0.157 | +458.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4301 | +0.059 | +247.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 10114 | +0.048 | +795.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1716 | +0.090 | +393.81€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 474 | +0.013 | +5.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 6453 | +0.051 | +361.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1400 | +0.005 | +34.29€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 71 | -0.089 | +0.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 6225 | +0.049 | +473.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1007 | +0.138 | +362.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 5190 | +0.032 | +112.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 11594 | +0.031 | +613.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3288 | +0.053 | +444.03€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 467 | +0.007 | +9.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 6729 | +0.027 | +159.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1048 | +0.004 | -1.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 62 | -0.125 | +2.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 11751 | +0.021 | +401.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3161 | +0.030 | +265.28€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 457 | -0.001 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 7433 | +0.021 | +138.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 646 | +0.005 | +3.38€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 54 | -0.161 | -4.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 7600 | +0.047 | +866.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3135 | +0.095 | +840.80€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 308 | +0.006 | -1.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4157 | +0.015 | +26.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 187 | -0.124 | -2.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 671 | +0.359 | +236.30€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 671 | +0.359 | +236.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 367 | +0.364 | +128.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 367 | +0.364 | +128.06€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 304 | +0.350 | +108.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 304 | +0.350 | +108.24€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 14975 | -0.030 | +3441.12€ | 2 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 14975 | -0.030 | +3441.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1128 | -0.058 | +372.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1128 | -0.058 | +372.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2669 | -0.114 | +110.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2669 | -0.114 | +110.45€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 621 | +0.203 | +473.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 621 | +0.203 | +473.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1735 | +0.212 | +1108.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1735 | +0.212 | +1108.89€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4408 | -0.063 | +616.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4408 | -0.063 | +616.86€ | 4 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4414 | -0.068 | +758.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4414 | -0.068 | +758.99€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 171 | +0.026 | +6.16€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 171 | +0.026 | +6.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 171 | +0.026 | +6.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 171 | +0.026 | +6.16€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1085 | +0.292 | +897.41€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1085 | +0.292 | +897.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 592 | +0.288 | +455.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 592 | +0.288 | +455.49€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 493 | +0.296 | +441.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 493 | +0.296 | +441.92€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 752 | -0.111 | -82.58€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#5min | 752 | -0.111 | -82.58€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 224 | -0.088 | -18.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 224 | -0.088 | -18.30€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 71 | -0.158 | -8.76€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 71 | -0.158 | -8.76€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 78 | -0.175 | -5.47€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 78 | -0.175 | -5.47€ | 3 | 0 |
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
  - _Estado_: Spread bajo (0.051) — sin ventaja clara. oversold(IBS<0.3): IC=+0.051 n=18453 | neutral: IC=+0.043 n=19516 | overbought(IBS>0.7): IC=+0.094 n=18787
  - _Datos_: n=58842 IC=+0.063 PNL=+7902.55€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 603 celda(s) pasan gate riguroso completo de 2405 evaluadas (n>=40) y 3392 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.030 < 0.08 — monitorear
  - _Datos_: n=3161 IC=+0.030 PNL=+265.28€

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
  - _Estado_: 52593 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.127 n=496/60 | contraria IC=+0.186 n=504 | gap=-0.059 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=364, boost estimado=+0.006. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 214 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1048/40 IC=+0.004 PNL=-1.09€ | BTC#60min: n=1400/40 IC=+0.005 PNL=+34.29€ | SOL#60min: n=646/40 IC=+0.005 PNL=+3.38€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=416841 | tras_1loss IC=+0.086 n=320864 | tras_2loss IC=+0.055 n=132634/40 | gap=-0.007 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.023 n=6571 | contrario_BTC IC=+0.038 n=5823/40 | gap=+0.015 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: n=63 IC=+0.177 PNL=+39.77€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=63 IC=+0.177 PNL=+39.77€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=49979 IC=+0.040 PNL=+3659.66€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=49979 IC=+0.040 PNL=+3659.66€

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
  - _Estado_: n=2114 IC=+0.007 PNL=+1.30€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2114 IC=+0.007 PNL=+1.30€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=980 IC=-0.001 PNL=+35.28€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=980 IC=-0.001 PNL=+35.28€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.1 con n=2886 PNL=+2055.31€
  - _Datos_: n=2886 IC=+0.203 PNL=+2055.31€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1987 IC=+0.065 PNL=+158.02€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1987 IC=+0.065 PNL=+158.02€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1716 IC=+0.090 PNL=+393.81€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1716 IC=+0.090 PNL=+393.81€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.095 > 0.08 con n=7626 PNL=+2076.99€
  - _Datos_: n=7626 IC=+0.095 PNL=+2076.99€

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
  - _Estado_: n=9287 IC=+0.042 PNL=+633.81€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=9287 IC=+0.042 PNL=+633.81€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=3162 IC=+0.061 PNL=+430.87€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3162 IC=+0.061 PNL=+430.87€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.08 con n=418 PNL=+129.42€
  - _Datos_: n=418 IC=+0.112 PNL=+129.42€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.152 > 0.08 con n=793 PNL=+211.45€
  - _Datos_: n=793 IC=+0.152 PNL=+211.45€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.107 > 0.08 con n=614 PNL=+335.72€
  - _Datos_: n=614 IC=+0.107 PNL=+335.72€

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
  - _Estado_: n=7878 IC=+0.046 PNL=+675.71€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7878 IC=+0.046 PNL=+675.71€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.02 con n=760 PNL=+296.04€
  - _Datos_: n=760 IC=+0.121 PNL=+296.04€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.451 > 0.1 con n=1320 PNL=+1295.87€
  - _Datos_: n=1320 IC=+0.451 PNL=+1295.87€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=19481 IC=+0.067 PNL=+2684.56€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=19481 IC=+0.067 PNL=+2684.56€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.1 con n=4687 PNL=+2741.38€
  - _Datos_: n=4687 IC=+0.207 PNL=+2741.38€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.155 < -0.1 con n=311 PNL=+27.07€
  - _Datos_: n=311 IC=-0.155 PNL=+27.07€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2409 IC=+0.059 PNL=+258.11€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2409 IC=+0.059 PNL=+258.11€

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
  - _Estado_: n=22928 IC=-0.135 PNL=+1752.22€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=22928 IC=-0.135 PNL=+1752.22€

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
  - _Estado_: n=2352 IC=+0.137 PNL=+1361.11€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2352 IC=+0.137 PNL=+1361.11€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.204 > 0.08 con n=2847 PNL=+2042.68€
  - _Datos_: n=2847 IC=+0.204 PNL=+2042.68€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.216 > 0.08 con n=604 PNL=+324.39€
  - _Datos_: n=604 IC=+0.216 PNL=+324.39€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.226 < -0.1 con n=2289 PNL=-172.75€
  - _Datos_: n=2289 IC=-0.226 PNL=-172.75€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=6621 IC=+0.182 PNL=+4608.90€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=6621 IC=+0.182 PNL=+4608.90€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=93 PNL=+36.81€
  - _Datos_: n=93 IC=+0.111 PNL=+36.81€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2390 IC=+0.070 PNL=+748.28€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2390 IC=+0.070 PNL=+748.28€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.178 > 0.08 con n=2191 PNL=+1550.31€
  - _Datos_: n=2191 IC=+0.178 PNL=+1550.31€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3670 IC=-0.030 PNL=+970.78€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3670 IC=-0.030 PNL=+970.78€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=601 PNL=-53.56€
  - _Datos_: n=601 IC=+0.084 PNL=-53.56€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.239 > 0.08 con n=3854 PNL=-327.41€
  - _Datos_: n=3854 IC=+0.239 PNL=-327.41€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.100 n=1332) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1332 IC=+0.100 PNL=+301.54€

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
  - _Estado_: n=10654 IC=+0.181 PNL=-1154.90€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=10654 IC=+0.181 PNL=-1154.90€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.1 con n=172 PNL=+105.24€
  - _Datos_: n=172 IC=+0.207 PNL=+105.24€
