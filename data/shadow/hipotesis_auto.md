# Hipótesis automáticas — 2026-09-27 04:46 UTC
_Generado por shadow_postmortem.py sobre 630259 resoluciones (PNL=+72338.30€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=515)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.236 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.209 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.8026` → IC=+0.258 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8026 (IC base=+0.140)

- **PATRÓN** `banda_z` > `4.083` → IC=+0.165 (n=547)

  - _Acción_: Kelly boost +0.82€ cuando `banda_z` > 4.083 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.157 (n=380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=585)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `3000.0061` → IC=+0.151 (n=365)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3000.0061 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.127 (n=515)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.056)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.259 (n=421)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=380)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.259 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.150)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.208 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.150)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.265 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.150)

- **PATRÓN** `banda_z` > `4.287` → IC=+0.178 (n=439)

  - _Acción_: Kelly boost +0.89€ cuando `banda_z` > 4.287 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=496)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `4456.7277` → IC=+0.152 (n=199)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4456.7277 (IC base=+0.150)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.120 (n=380)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.495 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.167 (n=148)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 94.0 (IC base=+0.060)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.214 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=+0.218 (n=101)

- **FILTRO** `banda_hit_calibrado` < `0.6297` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6297
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=90)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.170 (n=107)

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

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.250 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.55 (IC base=+0.110)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.110)

- **PATRÓN** `banda_z` > `8.424` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.424 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1356.6996` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1356.6996 (IC base=+0.110)

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
- **FILTRO** `restante_s_al_confirmar` < `146.08` → IC=-0.220 (n=7330)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.08
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=21996)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `137.22` → IC=-0.249 (n=954)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 137.22
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2863)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.51` → IC=-0.308 (n=871)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.51
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2613)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.14` → IC=-0.204 (n=1788)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.14
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=5367)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `126.93` → IC=-0.337 (n=1443)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 126.93
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=4330)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.230 (n=357)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=408)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=174)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=539)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=563)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.206 (n=14402)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3612)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5639.5091` → IC=+0.177 (n=2305)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 5639.5091 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.138 (n=12092)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=14682)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.232 (n=11407)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=5846)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7845.6927` → IC=+0.176 (n=2215)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7845.6927 (IC base=+0.128)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1743)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=2200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `15942.0974` → IC=+0.237 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15942.0974 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.205 (n=1575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.263 (n=1583)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=2239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `15863.0179` → IC=+0.214 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15863.0179 (IC base=+0.201)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.180 (n=332)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.62 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `4566.8958` → IC=+0.143 (n=239)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4566.8958 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=370)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.103)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.143 (n=847)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `5784.0902` → IC=+0.164 (n=224)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5784.0902 (IC base=+0.103)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2927)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.147 (n=2493)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.346 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.365 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.235 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.232)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=622)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.255 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=568)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `1302.9991` → IC=+0.148 (n=689)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1302.9991 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.405 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.167 (n=605)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 7.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=744)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.160)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.176 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.367 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.162 (n=190)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `1244.1621` → IC=+0.152 (n=231)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1244.1621 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.115)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.211 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.115)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=12051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=11520)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.226 (n=3954)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `5111.8837` → IC=+0.335 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5111.8837 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=2902)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.172 (n=2758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.176 (n=2757)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.167)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.245 (n=950)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.342 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.241)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2861)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=2731)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2329)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.249 (n=2519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.240)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.326 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.240)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.195 (n=2665)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.197 (n=2067)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.193)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.434 (n=555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.427 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `11135.4127` → IC=+0.457 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11135.4127 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.435 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.443 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `14120.495` → IC=+0.444 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14120.495 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.442 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.426 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `3364.1944` → IC=+0.443 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3364.1944 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.411 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.408)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.409 (n=108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.408)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.422 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.408)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.410 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.408)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=35928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.236 (n=16052)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=7282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=4971)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=6732)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=6455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=6431)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=2298)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=6536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=6544)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.173)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.230 (n=3258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.267 (n=2240)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.210 (n=5949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.258 (n=2401)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=7076)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=5994)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2254)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5485)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.126 (n=5100)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=5091)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=6729)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.66` → IC=+0.139 (n=5061)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.66 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=2763)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.12` → IC=+0.128 (n=2519)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.12 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.141 (n=2792)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.94 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.139 (n=3319)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `3.31` → IC=+0.144 (n=2519)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.31 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=2722)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.128 (n=2560)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.2 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.132 (n=2827)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.136 (n=2547)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.320 (n=820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.290)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `4103.1582` → IC=+0.308 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4103.1582 (IC base=+0.290)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.301 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.328 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `4258.3281` → IC=+0.299 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4258.3281 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.331 (n=389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.298 (n=576)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1730.1078` → IC=+0.316 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1730.1078 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.348 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.342)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.368 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.342)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.384 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.342)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.346 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.342)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.372 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.342)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.441 (n=458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.438 (n=451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.437 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `2554.5498` → IC=+0.435 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2554.5498 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=247)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.447 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.925` → IC=+0.452 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.925 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.439 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `1979.4391` → IC=+0.463 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1979.4391 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.389 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.391)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.391)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

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
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

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
- **PATRÓN** `drift_60min` |x|≤ `0.485` → IC=+0.124 (n=8518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.485 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `0.9836` → IC=+0.244 (n=2839)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9836 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` < `0.6174` → IC=+0.252 (n=2433)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6174 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.968` → IC=+0.181 (n=3256)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 5.968 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `1.207` → IC=+0.249 (n=2329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.207 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` > `0.6157` → IC=+0.253 (n=2328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6157 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.3025` → IC=+0.223 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3025 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` > `1.4626` → IC=+0.206 (n=5866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4626 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.57` → IC=+0.134 (n=10289)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.57 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.6036` → IC=+0.204 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6036 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` < `0.697` → IC=+0.189 (n=1603)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.697 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `1.05` → IC=+0.175 (n=1650)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.05 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.225 (n=1744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.2936` → IC=+0.196 (n=5423)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2936 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.5705` → IC=+0.201 (n=5506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5705 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.213 (n=5952)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 130.0 (IC base=+0.067)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.188 (n=636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0049 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.174 (n=637)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0081 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.3473` → IC=+0.169 (n=1908)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3473 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.175 (n=920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.170 (n=1283)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 11.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.136` → IC=+0.269 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.136 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.213 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.167 (n=1789)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.179 (n=1940)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.04 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.246 (n=1318)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.198` → IC=+0.261 (n=978)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.198 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.248 (n=1006)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0526` → IC=+0.289 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0526 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.497` → IC=+0.238 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.497 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.468` → IC=+0.245 (n=1529)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.468 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.0922` → IC=+0.232 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0922 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.267 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.4302` → IC=+0.234 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4302 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.6113` → IC=+0.245 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6113 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=1614)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.235 (n=650)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.0835` → IC=+0.241 (n=492)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0835 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=1546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.218 (n=1496)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9028` → IC=+0.262 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9028 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.5595` → IC=+0.222 (n=1547)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5595 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.688` → IC=+0.264 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.688 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `1.2525` → IC=+0.220 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2525 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `1.0793` → IC=+0.226 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0793 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2768` → IC=+0.244 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2768 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.3807` → IC=+0.230 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3807 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `11128.7666` → IC=+0.223 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11128.7666 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.179 (n=512)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0026 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.164 (n=510)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=684)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.7033` → IC=+0.171 (n=1526)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7033 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1271` → IC=+0.155 (n=1366)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1271 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.279` → IC=+0.150 (n=244)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.279 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.302` → IC=+0.145 (n=1393)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.302 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.150 (n=1526)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.1954 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.8523` → IC=+0.141 (n=1017)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8523 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1558` → IC=+0.176 (n=405)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1558 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.153 (n=1416)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4233` → IC=+0.147 (n=1416)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4233 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `14070.8773` → IC=+0.145 (n=1017)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 14070.8773 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.170 (n=588)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 233.0 (IC base=+0.140)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.211 (n=635)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=1990)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=1703)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.184` → IC=+0.257 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.184 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.190 (n=1651)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.3557` → IC=+0.197 (n=255)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.3557 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.7745` → IC=+0.195 (n=1617)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.7745 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=2259)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.223 (n=1450)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6096` → IC=+0.212 (n=1647)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6096 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=770)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0643` → IC=+0.244 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0643 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.707` → IC=+0.233 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.707 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.512` → IC=+0.211 (n=1789)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.512 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3506` → IC=+0.262 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3506 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.761` → IC=+0.207 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.761 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.179` → IC=+0.215 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.179 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.217 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1910.06` → IC=+0.210 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.06 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.216 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.144 (n=102)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2312)

- **PATRÓN** `ibs_20min` > `0.9479` → IC=+0.215 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9479 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.3544` → IC=+0.328 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3544 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.5334` → IC=+0.329 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5334 (IC base=+0.029)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.752` → IC=+0.165 (n=750)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 4.752 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.331 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `1.2107` → IC=+0.332 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2107 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.31` → IC=+0.344 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.31 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.352 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.2435` → IC=+0.327 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2435 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.333 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 160.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.6684` → IC=+0.209 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6684 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` < `0.6866` → IC=+0.166 (n=393)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6866 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `1.1597` → IC=+0.150 (n=298)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.1597 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.2283` → IC=+0.218 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2283 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.5312` → IC=+0.170 (n=750)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.5312 (IC base=+0.019)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.172 (n=62)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=347)

- **FILTRO** `ibs_20min` < `0.2909` → IC=-0.211 (n=102)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2909
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=307)

- **FILTRO** `ibs_20min` > `0.25` → IC=-0.125 (n=2297)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=1147)

- **FILTRO** `sigma_ewma_delta_pct` > `8.719` → IC=-0.213 (n=367)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.719
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3077)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.232 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7647 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `1.0712` → IC=+0.293 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0712 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` < `0.781` → IC=+0.283 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.781 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.333` → IC=+0.124 (n=147)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 2.333 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.7668` → IC=+0.300 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7668 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.7487` → IC=+0.300 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7487 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` > `1.4536` → IC=+0.270 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4536 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.298 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.126 (n=1147)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.25 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7013` → IC=+0.263 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7013 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `0.6948` → IC=+0.272 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6948 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.276 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.278 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6536` → IC=-0.183 (n=603)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6536
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1811)

- **FILTRO** `ibs_20min` < `0.7179` → IC=-0.156 (n=1593)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7179
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=821)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.204 (n=474)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1940)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.206 (n=882)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=2660)

- **PATRÓN** `dist_vwap_pct` > `0.4581` → IC=+0.311 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4581 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2822` → IC=+0.309 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2822 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` > `0.6851` → IC=+0.309 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6851 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.297 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` < `1.4006` → IC=+0.295 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4006 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.7985` → IC=+0.297 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7985 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.8909` → IC=+0.274 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8909 (IC base=-0.020)

- **PATRÓN** `volumen_regimen` < `0.7321` → IC=+0.257 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7321 (IC base=-0.020)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.286 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=-0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.276 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.1375` → IC=+0.264 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1375 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.5235` → IC=+0.252 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5235 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.198 (n=3602)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0097 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.4748` → IC=+0.187 (n=9640)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4748 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `1.0522` → IC=+0.289 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0522 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.157 (n=5036)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6905` → IC=+0.251 (n=3440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6905 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.269 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.4651` → IC=+0.237 (n=2084)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4651 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.6635` → IC=+0.248 (n=2082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6635 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.270 (n=5764)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 95.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.159 (n=3559)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0091 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.549` → IC=+0.154 (n=9380)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.549 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7093` → IC=+0.242 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7093 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.246` → IC=+0.243 (n=3022)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.246 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.635` → IC=+0.245 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.635 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.2044` → IC=+0.248 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2044 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2421` → IC=+0.306 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2421 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.6017` → IC=+0.263 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6017 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2958` → IC=+0.260 (n=1919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2958 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `84.0` → IC=+0.269 (n=4117)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 84.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2542` → IC=-0.149 (n=744)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2542
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=2235)

- **FILTRO** `sigma_ewma_delta_pct` > `4.552` → IC=-0.164 (n=566)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.552
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1888)

- **PATRÓN** `ibs_20min` > `0.8947` → IC=+0.267 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8947 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.845` → IC=+0.205 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.845 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2224` → IC=+0.271 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2224 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4388` → IC=+0.177 (n=317)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4388 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.1651` → IC=+0.206 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1651 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.195 (n=417)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 13.0 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.1456` → IC=+0.463 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1456 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.4436` → IC=+0.454 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4436 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.0444` → IC=+0.450 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0444 (IC base=-0.020)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.474 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8658` → IC=+0.162 (n=723)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.8658 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.3002` → IC=+0.175 (n=392)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.3002 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` > `0.6746` → IC=+0.171 (n=891)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6746 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.235 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.189 (n=326)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` > `2.4028` → IC=+0.165 (n=326)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.4028 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.190 (n=427)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 239.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.1497` → IC=+0.216 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1497 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `0.857` → IC=+0.225 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.857 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2683` → IC=+0.316 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2683 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.4389` → IC=+0.215 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4389 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1657` → IC=+0.229 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1657 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `460.0` → IC=+0.214 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 460.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.289 (n=561)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.248)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.252 (n=1768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.249 (n=1697)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.248)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.691` → IC=+0.284 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.691 (IC base=+0.248)

- **PATRÓN** `volumen_pendiente_norm` < `0.1014` → IC=+0.261 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1014 (IC base=+0.248)

- **PATRÓN** `volumen_spike_ratio` > `3.3565` → IC=+0.266 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3565 (IC base=+0.248)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=1983)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.248)

- **PATRÓN** `libro_liquidez` > `1912.1779` → IC=+0.257 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.1779 (IC base=+0.248)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.314 (n=620)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.1764` → IC=+0.291 (n=601)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1764 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.324 (n=465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` < `0.3427` → IC=+0.289 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3427 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.694` → IC=+0.295 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.694 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.739` → IC=+0.282 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.739 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.3385` → IC=+0.302 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3385 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.288 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `2.695` → IC=+0.287 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.695 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.286 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `1903.24` → IC=+0.294 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1903.24 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.287 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.282)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.3002` → IC=-0.169 (n=536)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3002
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1611)

- **FILTRO** `ibs_20min` > `0.7735` → IC=-0.185 (n=633)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7735
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=1902)

- **PATRÓN** `ibs_20min` > `0.9105` → IC=+0.181 (n=537)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.9105 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.659` → IC=+0.222 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.659 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `0.9984` → IC=+0.243 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9984 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` > `0.5902` → IC=+0.220 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5902 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.261 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `1.5105` → IC=+0.264 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5105 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` > `2.4161` → IC=+0.235 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4161 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.275 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` > `0.1443` → IC=+0.212 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1443 (IC base=-0.006)

- **PATRÓN** `dist_vwap_pct` < `0.3419` → IC=+0.204 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3419 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` < `0.641` → IC=+0.237 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.641 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.8269` → IC=+0.258 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8269 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.1499` → IC=+0.240 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1499 (IC base=-0.006)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.257 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7353` → IC=-0.196 (n=1143)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7353
  - _Potencial_: sin este filtro IC_bueno=+0.280 (n=1144)

- **FILTRO** `ibs_20min` > `0.6842` → IC=-0.235 (n=584)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6842
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=1753)

- **FILTRO** `sigma_ewma_delta_pct` > `4.739` → IC=-0.189 (n=509)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.739
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=1828)

- **PATRÓN** `ibs_20min` > `0.7353` → IC=+0.280 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7353 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` > `0.8494` → IC=+0.329 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8494 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.658` → IC=+0.169 (n=358)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.658 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.305 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `0.7279` → IC=+0.295 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7279 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.1016` → IC=+0.297 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1016 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2703` → IC=+0.300 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2703 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4267` → IC=+0.323 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4267 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.320 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.122 (n=1549)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.5833 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.4659` → IC=+0.219 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4659 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.257 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.0971` → IC=+0.218 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0971 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.069` → IC=+0.217 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.069 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.481` → IC=+0.231 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.481 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.240 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.015)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.317 (n=920)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.285 (n=1448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.348 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2152` → IC=+0.316 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2152 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.658` → IC=+0.303 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.658 (IC base=+0.279)

- **PATRÓN** `volumen_regimen` > `0.8606` → IC=+0.304 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8606 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` < `0.0782` → IC=+0.282 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0782 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.327 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.288 (n=1312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `2474.544` → IC=+0.291 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2474.544 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.306 (n=991)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.1961` → IC=+0.277 (n=654)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1961 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.288 (n=512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.277)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.281 (n=741)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` < `0.2927` → IC=+0.316 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2927 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.3138` → IC=+0.281 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3138 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.278 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2288 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.471` → IC=+0.291 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.471 (IC base=+0.277)

- **PATRÓN** `volumen_regimen` < `0.6405` → IC=+0.281 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6405 (IC base=+0.277)

- **PATRÓN** `volumen_regimen` > `1.2434` → IC=+0.309 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2434 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` > `0.2363` → IC=+0.338 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2363 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` < `1.4227` → IC=+0.285 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4227 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `2.1399` → IC=+0.277 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1399 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `2620.0234` → IC=+0.277 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2620.0234 (IC base=+0.277)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.174 (n=2773)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0049 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.201 (n=2758)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3577` → IC=+0.176 (n=7280)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3577 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=8618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.5741` → IC=+0.219 (n=8272)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5741 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.1742` → IC=+0.193 (n=3588)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1742 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.362` → IC=+0.255 (n=1686)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.362 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.161 (n=5485)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2084 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.63` → IC=+0.161 (n=5484)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.63 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2429` → IC=+0.195 (n=1669)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2429 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.5582` → IC=+0.167 (n=3495)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5582 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.613` → IC=+0.177 (n=2649)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.613 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `1952.9463` → IC=+0.170 (n=7390)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1952.9463 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.182 (n=7186)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 112.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.184 (n=5304)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0066 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.0808` → IC=+0.211 (n=2650)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0808 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=3070)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.169 (n=3772)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.4807` → IC=+0.226 (n=7949)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4807 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` < `0.233` → IC=+0.160 (n=5764)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.233 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.341` → IC=+0.192 (n=1341)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 10.341 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.1725` → IC=+0.153 (n=5732)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1725 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.212 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.5594` → IC=+0.167 (n=3195)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5594 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6198` → IC=+0.169 (n=2421)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.6198 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.175 (n=6915)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 112.0 (IC base=+0.169)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.209 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.191 (n=467)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0083 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.341` → IC=+0.208 (n=1401)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.341 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=1472)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=937)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.22` → IC=+0.327 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.22 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.236 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.183 (n=1299)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=1426)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.242 (n=921)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.247 (n=936)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1824` → IC=+0.286 (n=698)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1824 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3437` → IC=+0.260 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3437 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.325` → IC=+0.249 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.325 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.236 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.247 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4215` → IC=+0.266 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4215 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1997.707` → IC=+0.244 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1997.707 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.238 (n=411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.0729` → IC=+0.195 (n=411)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0729 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=1231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.4061` → IC=+0.227 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4061 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.2068` → IC=+0.212 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2068 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.237 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `0.6876` → IC=+0.167 (n=542)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6876 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `0.8746` → IC=+0.167 (n=820)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.8746 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.206 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.5076` → IC=+0.176 (n=526)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.5076 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `2.4598` → IC=+0.161 (n=399)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4598 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `10668.8677` → IC=+0.171 (n=1230)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10668.8677 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.202 (n=444)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2908` → IC=+0.162 (n=1325)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2908 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.174 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=622)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5687` → IC=+0.189 (n=1325)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5687 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1321` → IC=+0.162 (n=1319)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1321 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.883` → IC=+0.196 (n=264)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.883 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1939` → IC=+0.159 (n=1325)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1939 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1543` → IC=+0.153 (n=404)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.1543 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4443` → IC=+0.148 (n=1213)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4443 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4241` → IC=+0.136 (n=1213)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4241 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.165 (n=377)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 212.0 (IC base=+0.137)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.218 (n=629)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.2367` → IC=+0.218 (n=926)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2367 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.208 (n=1438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.414` → IC=+0.276 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.414 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2038` → IC=+0.203 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2038 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.8017` → IC=+0.199 (n=582)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.8017 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.8061` → IC=+0.216 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8061 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.210 (n=1637)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.231 (n=1172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.0995` → IC=+0.253 (n=391)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0995 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.273 (n=407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.3478` → IC=+0.246 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3478 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.707` → IC=+0.257 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.707 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3529` → IC=+0.254 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3529 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.216 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.1982` → IC=+0.229 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1982 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.211 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.217)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.216 (n=446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.4235` → IC=+0.160 (n=1325)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4235 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.3743` → IC=+0.197 (n=1323)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3743 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1451` → IC=+0.177 (n=873)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1451 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.01` → IC=+0.232 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.01 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.0344` → IC=+0.149 (n=1165)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0344 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6214` → IC=+0.147 (n=1323)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6214 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2914` → IC=+0.199 (n=207)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2914 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.4294` → IC=+0.154 (n=432)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4294 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.5113` → IC=+0.173 (n=432)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5113 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `5983.7933` → IC=+0.183 (n=882)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 5983.7933 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `161.0` → IC=+0.148 (n=1264)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 161.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.154 (n=1393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.3804` → IC=+0.142 (n=1393)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3804 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6477` → IC=+0.172 (n=1393)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6477 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.1534` → IC=+0.140 (n=1366)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1534 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.965` → IC=+0.157 (n=494)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.965 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.849` → IC=+0.151 (n=929)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.849 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.178 (n=206)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.8013` → IC=+0.142 (n=847)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.8013 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `9988.1936` → IC=+0.159 (n=632)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 9988.1936 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.152 (n=680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0101 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=1536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5143` → IC=+0.205 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5143 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.2811` → IC=+0.183 (n=852)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2811 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.8` → IC=+0.256 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.8 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.131 (n=1501)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2145 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1633` → IC=+0.126 (n=1507)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1633 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.121 (n=632)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.5369` → IC=+0.136 (n=638)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.5369 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=1566)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2903.4322` → IC=+0.194 (n=680)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2903.4322 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.134 (n=1154)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 49.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.159 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0061 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.105` → IC=+0.166 (n=510)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.105 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.5735` → IC=+0.213 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5735 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.0108` → IC=+0.134 (n=219)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 1.0108 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.2006` → IC=+0.142 (n=1399)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2006 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.618` → IC=+0.139 (n=319)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 7.618 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.6381` → IC=+0.149 (n=511)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6381 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.162 (n=190)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.4547` → IC=+0.133 (n=459)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4547 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.4205` → IC=+0.131 (n=459)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4205 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2760.8425` → IC=+0.160 (n=693)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2760.8425 (IC base=+0.115)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.227 (n=1279)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.1795` → IC=+0.203 (n=630)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1795 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=1487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.206 (n=648)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.7381` → IC=+0.260 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7381 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.5174` → IC=+0.218 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5174 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.242 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.207 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2068 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.8567` → IC=+0.223 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8567 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2322` → IC=+0.266 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2322 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.1485` → IC=+0.211 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1485 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4077` → IC=+0.210 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4077 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.205 (n=1502)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2827.677` → IC=+0.207 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2827.677 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.223 (n=655)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.212 (n=675)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0929` → IC=+0.223 (n=496)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0929 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=684)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.4375` → IC=+0.246 (n=1488)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4375 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `1.2307` → IC=+0.221 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2307 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.43` → IC=+0.244 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.43 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.6328` → IC=+0.215 (n=1488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6328 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.286 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.1914` → IC=+0.198 (n=1183)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1914 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4271` → IC=+0.202 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4271 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2587.456` → IC=+0.206 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2587.456 (IC base=+0.206)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.183 (n=683)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0038 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.174 (n=683)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0087 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3484` → IC=+0.159 (n=1800)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3484 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.190 (n=1028)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.7491` → IC=+0.210 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7491 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.8428` → IC=+0.175 (n=336)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.8428 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.756` → IC=+0.181 (n=920)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.756 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8709` → IC=+0.175 (n=1207)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.8709 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.21` → IC=+0.162 (n=604)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.21 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1644` → IC=+0.177 (n=561)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1644 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4431` → IC=+0.164 (n=659)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4431 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.8284` → IC=+0.163 (n=1317)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.8284 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.159 (n=2317)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `12366.3016` → IC=+0.159 (n=682)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 12366.3016 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.175 (n=1827)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 151.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.136 (n=1398)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0056 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.3414` → IC=+0.126 (n=1842)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.3414 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.124 (n=2099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.0596` → IC=+0.191 (n=698)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0596 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.2059` → IC=+0.120 (n=1873)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` < 0.2059 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.6987` → IC=+0.129 (n=831)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.6987 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.128 (n=525)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4529` → IC=+0.143 (n=673)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4529 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2761.0504` → IC=+0.121 (n=1870)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2761.0504 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.129 (n=671)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 20.0 (IC base=+0.111)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.137 (n=337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0039 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1102` → IC=+0.143 (n=222)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.1102 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.158 (n=472)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 8.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.6665` → IC=+0.192 (n=336)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.6665 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.291` → IC=+0.150 (n=178)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.291 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.243` → IC=+0.132 (n=229)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 3.243 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.9061` → IC=+0.149 (n=337)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.9061 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.0905` → IC=+0.134 (n=181)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.0905 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `10925.7104` → IC=+0.136 (n=504)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 10925.7104 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.159 (n=162)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 146.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.203 (n=217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.3374` → IC=+0.153 (n=650)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3374 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.6091` → IC=+0.183 (n=572)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.6091 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.476` → IC=+0.150 (n=746)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.476 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.421` → IC=+0.150 (n=252)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.421 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.2185` → IC=+0.141 (n=650)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2185 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `1.0611` → IC=+0.160 (n=295)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.0611 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.189 (n=175)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.1137` → IC=+0.157 (n=563)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1137 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.4209` → IC=+0.146 (n=640)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4209 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `324.0` → IC=+0.150 (n=544)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 324.0 (IC base=+0.135)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.271 (n=282)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.227 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.9681` → IC=+0.267 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9681 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.1397` → IC=+0.208 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1397 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.2089` → IC=+0.207 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2089 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.951` → IC=+0.230 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.951 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.0076` → IC=+0.208 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0076 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `1.1573` → IC=+0.221 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1573 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2651` → IC=+0.277 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2651 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `1.401` → IC=+0.228 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.401 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.7564` → IC=+0.235 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7564 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.212 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `12428.4336` → IC=+0.221 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12428.4336 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.084` → IC=+0.155 (n=201)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.084 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` < `0.6874` → IC=+0.140 (n=265)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6874 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.2277` → IC=+0.129 (n=95)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2277 (IC base=+0.091)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.009` → IC=+0.165 (n=222)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.009 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.5423` → IC=+0.136 (n=490)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.5423 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.171 (n=454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 8.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.947` → IC=+0.217 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.947 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.505` → IC=+0.194 (n=263)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.505 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.0738` → IC=+0.154 (n=431)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0738 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4827` → IC=+0.141 (n=157)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4827 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `2.212` → IC=+0.184 (n=213)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.212 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.138 (n=525)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `3116.6987` → IC=+0.197 (n=163)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3116.6987 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.525` → IC=+0.152 (n=438)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.525 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.146 (n=193)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.7052 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` < `1.5803` → IC=+0.174 (n=182)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5803 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `2594.3232` → IC=+0.133 (n=292)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2594.3232 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.142 (n=383)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 41.0 (IC base=+0.090)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.183 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0068 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.191 (n=179)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.2434` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2434 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `1.0655` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0655 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.177 (n=153)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.0007` → IC=+0.148 (n=157)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0007 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.6087` → IC=+0.167 (n=178)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6087 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.2548` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.2548 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2497.2192` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2497.2192 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.152 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0091 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.139 (n=203)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.6 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.1734` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1734 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.53` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.53 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.0734` → IC=+0.122 (n=178)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0734 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.132 (n=202)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6515 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1181` → IC=+0.126 (n=180)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1181 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.5435` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5435 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.8185` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.8185 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.142 (n=163)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 17.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.207 (n=3550)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=11089)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.308 (n=3586)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.9579` → IC=+0.203 (n=1506)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9579 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.354` → IC=+0.247 (n=2678)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.354 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `0.8801` → IC=+0.168 (n=4750)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8801 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2883` → IC=+0.205 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2883 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.5936` → IC=+0.190 (n=3418)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.5936 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `1795.4448` → IC=+0.174 (n=10649)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 1795.4448 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.198 (n=8204)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 85.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=6443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1486` → IC=+0.191 (n=4250)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1486 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.184 (n=4482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5673` → IC=+0.237 (n=9654)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5673 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.248` → IC=+0.163 (n=5996)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.248 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.036` → IC=+0.198 (n=1354)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.036 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.731` → IC=+0.184 (n=9336)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.731 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7039` → IC=+0.165 (n=2907)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7039 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `1.2022` → IC=+0.154 (n=2203)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2022 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2876` → IC=+0.237 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2876 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6149` → IC=+0.191 (n=2967)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6149 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.197 (n=5745)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 47.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.212 (n=598)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.210 (n=1195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.3502` → IC=+0.194 (n=1791)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3502 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.198 (n=1212)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 11.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.593` → IC=+0.347 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.593 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.255 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.5605` → IC=+0.198 (n=565)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.5605 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1807)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.262 (n=953)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.264 (n=1427)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1253` → IC=+0.284 (n=628)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1253 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=1290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.3517` → IC=+0.284 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3517 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.467` → IC=+0.262 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.467 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.282 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.4366` → IC=+0.260 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4366 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6339` → IC=+0.277 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6339 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=1570)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1817.785` → IC=+0.263 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1817.785 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.198 (n=574)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0028 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.1128` → IC=+0.158 (n=750)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1128 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=1780)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.3085` → IC=+0.203 (n=1705)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3085 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.1256` → IC=+0.185 (n=961)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1256 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.176 (n=390)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.184` → IC=+0.153 (n=1538)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.184 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6272` → IC=+0.179 (n=569)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6272 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2656` → IC=+0.204 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2656 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.1149` → IC=+0.162 (n=1451)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1149 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.7559` → IC=+0.159 (n=1099)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7559 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `11277.2096` → IC=+0.160 (n=1523)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11277.2096 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `470.0` → IC=+0.161 (n=1580)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 470.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.164 (n=1471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.3231` → IC=+0.163 (n=1471)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3231 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.171 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.158 (n=664)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.2761` → IC=+0.235 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2761 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.6767` → IC=+0.158 (n=238)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6767 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1297` → IC=+0.165 (n=1334)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1297 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.493` → IC=+0.157 (n=246)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.493 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.285` → IC=+0.154 (n=1335)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.285 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.165 (n=1471)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1856 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1506` → IC=+0.195 (n=395)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1506 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4046` → IC=+0.161 (n=1373)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4046 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.7562` → IC=+0.162 (n=915)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7562 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `350.0` → IC=+0.157 (n=852)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 350.0 (IC base=+0.152)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.252 (n=579)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=1812)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.809` → IC=+0.297 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.809 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.2091` → IC=+0.221 (n=1725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2091 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.6227` → IC=+0.226 (n=1657)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6227 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1915.5084` → IC=+0.224 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.5084 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.238 (n=1624)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.1717` → IC=+0.238 (n=715)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1717 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.259 (n=621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=766)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.0141` → IC=+0.303 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0141 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.751` → IC=+0.271 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.751 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.3426` → IC=+0.301 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3426 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.7518` → IC=+0.233 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7518 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.1714` → IC=+0.234 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1714 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.240 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `1907.66` → IC=+0.238 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1907.66 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.245 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.231)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.189 (n=605)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0034 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4312` → IC=+0.150 (n=1813)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4312 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=1890)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.8757` → IC=+0.265 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8757 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.5656` → IC=+0.167 (n=511)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.5656 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.515` → IC=+0.172 (n=297)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.515 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.873` → IC=+0.158 (n=1209)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.873 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.222 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5221` → IC=+0.153 (n=774)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5221 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.1479` → IC=+0.157 (n=797)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1479 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7942.2025` → IC=+0.232 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7942.2025 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.168 (n=564)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 76.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.170 (n=983)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0052 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.444` → IC=+0.148 (n=1473)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.444 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=675)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.7101` → IC=+0.180 (n=1473)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.7101 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.3648` → IC=+0.136 (n=1488)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.3648 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.238` → IC=+0.164 (n=221)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.238 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6938` → IC=+0.151 (n=648)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6938 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.1945` → IC=+0.141 (n=491)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.1945 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.235 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.145 (n=1400)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `10628.2406` → IC=+0.198 (n=491)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 10628.2406 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `175.0` → IC=+0.140 (n=1395)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 175.0 (IC base=+0.134)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.139 (n=1206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0081 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.135 (n=1855)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.4694` → IC=+0.192 (n=1808)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4694 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.0886` → IC=+0.198 (n=382)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 1.0886 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.513` → IC=+0.240 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.513 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.8936` → IC=+0.137 (n=1206)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8936 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=1826)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2898.7698` → IC=+0.250 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2898.7698 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.132 (n=1395)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 53.0 (IC base=+0.116)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.179 (n=584)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0058 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.1331` → IC=+0.164 (n=582)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1331 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.126 (n=1797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.206 (n=1746)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.2204` → IC=+0.135 (n=1418)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.2204 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.486` → IC=+0.128 (n=1684)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.486 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.7146` → IC=+0.158 (n=768)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7146 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2203` → IC=+0.168 (n=275)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2203 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.4366` → IC=+0.143 (n=528)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4366 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2809.3195` → IC=+0.176 (n=582)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2809.3195 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.126 (n=1373)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 51.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.229 (n=1608)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=1874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.212 (n=1611)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.260 (n=1616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.2116` → IC=+0.233 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2116 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.275` → IC=+0.274 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.275 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.2447` → IC=+0.214 (n=1800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2447 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.64` → IC=+0.220 (n=1800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.64 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.253 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4378` → IC=+0.219 (n=1740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4378 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.219 (n=1863)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2460.3759` → IC=+0.217 (n=1608)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2460.3759 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.221 (n=640)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.225 (n=642)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.214 (n=1353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.268 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `1.2407` → IC=+0.209 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2407 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.9238` → IC=+0.207 (n=2141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9238 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.848` → IC=+0.263 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.848 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.240 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.272 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.1736` → IC=+0.202 (n=1525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1736 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.4282` → IC=+0.201 (n=1733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4282 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=3226)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.190 (n=1046)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0048 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.5134` → IC=+0.173 (n=3124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.5134 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=1241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.171 (n=1406)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.220 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.1763` → IC=+0.172 (n=1163)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1763 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` < `0.4615` → IC=+0.161 (n=1967)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4615 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.22` → IC=+0.198 (n=518)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.22 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `0.6307` → IC=+0.164 (n=2095)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6307 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.1707` → IC=+0.196 (n=870)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1707 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.171 (n=1029)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.8762` → IC=+0.170 (n=2057)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8762 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=2233)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `3919.0332` → IC=+0.172 (n=2083)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3919.0332 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.204 (n=818)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.4826` → IC=+0.167 (n=2431)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4826 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=891)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=1075)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.18` → IC=+0.178 (n=1070)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.18 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6705` → IC=+0.172 (n=470)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.6705 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.241` → IC=+0.158 (n=2425)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.241 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.101` → IC=+0.158 (n=2045)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.101 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.150 (n=2203)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.0723` → IC=+0.150 (n=1122)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0723 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.5361` → IC=+0.160 (n=1057)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5361 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.8202` → IC=+0.153 (n=1601)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.8202 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=3226)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `6959.7194` → IC=+0.157 (n=2172)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 6959.7194 (IC base=+0.147)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.189 (n=358)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0055 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.178 (n=364)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0033 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.0893` → IC=+0.210 (n=136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0893 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.185 (n=182)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 8.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.5452` → IC=+0.201 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5452 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.2062` → IC=+0.174 (n=191)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.2062 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` < `0.3731` → IC=+0.176 (n=396)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.3731 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.201` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.201 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.415` → IC=+0.180 (n=429)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 2.415 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.8402` → IC=+0.203 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8402 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.3018` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3018 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.203 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6311` → IC=+0.203 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6311 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `12574.1361` → IC=+0.221 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12574.1361 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.216 (n=421)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.1137` → IC=+0.174 (n=421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1137 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.174 (n=366)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.1386` → IC=+0.178 (n=421)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1386 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.6103` → IC=+0.147 (n=434)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6103 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.6926` → IC=+0.177 (n=91)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6926 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.372` → IC=+0.161 (n=937)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.372 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8794` → IC=+0.188 (n=638)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8794 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0682` → IC=+0.165 (n=446)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0682 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4202` → IC=+0.147 (n=318)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4202 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.149 (n=636)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `14911.0423` → IC=+0.161 (n=434)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 14911.0423 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `705.0` → IC=+0.144 (n=911)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 705.0 (IC base=+0.138)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.181 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0099 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.5715` → IC=+0.174 (n=623)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.5715 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.3499` → IC=+0.170 (n=749)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.3499 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `3.3904` → IC=+0.167 (n=622)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.3904 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `2425.929` → IC=+0.198 (n=283)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2425.929 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.312 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.213` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.213 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `2.5115` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5115 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `3.6446` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6446 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `2362.106` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2362.106 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.187 (n=464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0047 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.3792` → IC=+0.178 (n=921)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3792 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.182 (n=360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 4.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.5305` → IC=+0.189 (n=698)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5305 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.8838` → IC=+0.184 (n=349)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.8838 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` < `0.2134` → IC=+0.182 (n=868)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2134 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.19` → IC=+0.184 (n=935)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 4.19 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.0854` → IC=+0.175 (n=921)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.0854 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6413` → IC=+0.176 (n=1046)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6413 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.193 (n=317)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `2.4736` → IC=+0.178 (n=1027)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.4736 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.175 (n=920)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=1044)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.201 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.4827` → IC=+0.185 (n=858)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4827 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.160 (n=604)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 11.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.7466` → IC=+0.161 (n=859)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.7466 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.0945` → IC=+0.165 (n=858)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.0945 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.6041` → IC=+0.172 (n=187)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.6041 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.399` → IC=+0.166 (n=779)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 4.399 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6469` → IC=+0.198 (n=286)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.6469 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.7253` → IC=+0.158 (n=766)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7253 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.175 (n=364)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.1996` → IC=+0.171 (n=740)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.1996 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `7506.7691` → IC=+0.172 (n=858)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7506.7691 (IC base=+0.157)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.148 (n=245)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0111 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.141 (n=268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 3.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.9615` → IC=+0.244 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9615 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.191` → IC=+0.168 (n=200)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.191 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.177` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.177 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.9028` → IC=+0.154 (n=186)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.9028 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.1658` → IC=+0.185 (n=87)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1658 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.5557` → IC=+0.136 (n=119)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.5557 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.135 (n=269)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=333)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `3413.2842` → IC=+0.161 (n=249)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3413.2842 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.128 (n=259)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 65.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.176 (n=248)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0067 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.6673` → IC=+0.168 (n=248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.6673 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.146 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 16.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.194 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.1176` → IC=+0.241 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1176 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.8823` → IC=+0.222 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8823 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.222` → IC=+0.145 (n=119)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.222 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.203` → IC=+0.156 (n=239)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 5.203 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.6758` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6758 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.1103` → IC=+0.209 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1103 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.6178` → IC=+0.157 (n=106)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.6178 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.1901` → IC=+0.170 (n=110)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.1901 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3309.2496` → IC=+0.176 (n=248)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3309.2496 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.198 (n=213)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 47.0 (IC base=+0.145)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0065` → IC=-0.207 (n=131)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0065
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=396)

- **FILTRO** `dist_vwap_pct` > `0.1778` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1778
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=358)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.173 (n=439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0039 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6606` → IC=+0.191 (n=804)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.6606 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1412` → IC=+0.150 (n=486)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1412 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.471` → IC=+0.179 (n=210)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.471 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.178 (n=119)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `2435.8886` → IC=+0.133 (n=398)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2435.8886 (IC base=+0.085)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.123 (n=266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0045 (IC base=+0.020)

- **PATRÓN** `ibs_20min` < `0.0508` → IC=+0.283 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0508 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.1778` → IC=+0.128 (n=358)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1778 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.191` → IC=+0.130 (n=125)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 3.191 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.138` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.138 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.5569` → IC=+0.140 (n=259)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5569 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.4422` → IC=+0.133 (n=232)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.4422 (IC base=+0.020)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.151 (n=342)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0059 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.4717` → IC=+0.183 (n=310)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.4717 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.1286` → IC=+0.175 (n=161)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1286 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` < `0.067` → IC=+0.131 (n=242)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.067 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `2.392` → IC=+0.145 (n=271)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.392 (IC base=+0.101)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.138 (n=147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0044 (IC base=+0.067)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.181 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.2917` → IC=+0.245 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2917 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.0631` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.0631 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.698` → IC=+0.159 (n=124)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.698 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` < `0.6161` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6161 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0709` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0709 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.4111` → IC=+0.167 (n=121)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.4111 (IC base=+0.067)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6568` → IC=-0.122 (n=133)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6568
  - _Potencial_: sin este filtro IC_bueno=+0.216 (n=273)

- **FILTRO** `sigma_h` > `0.0059` → IC=-0.214 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0059
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=123)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=128)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.142 (n=224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.005 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.129 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.6568` → IC=+0.216 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6568 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.3316` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.3316 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.658` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.658 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `1.7369` → IC=+0.153 (n=168)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.7369 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `1125.4271` → IC=+0.152 (n=268)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1125.4271 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.1891` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1891 (IC base=-0.003)

- **PATRÓN** `dist_vwap_pct` < `0.1197` → IC=+0.132 (n=104)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1197 (IC base=-0.003)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.258` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.258 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.1353` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1353 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.268` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.268 (IC base=-0.003)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=-0.003)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.280 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=94)

- **FILTRO** `ibs_20min` > `0.2105` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2105
  - _Potencial_: sin este filtro IC_bueno=+0.225 (n=67)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.147 (n=256)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.66 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.606` → IC=+0.139 (n=59)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.606 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` > `1.062` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.062 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.058)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.194 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0056 (IC base=-0.028)

- **PATRÓN** `ibs_20min` < `0.2105` → IC=+0.225 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2105 (IC base=-0.028)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.25` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.25 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.1368` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1368 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5975 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.3662` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.3662 (IC base=-0.028)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0033` → IC=-0.306 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=143)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.365 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=163)

- **FILTRO** `dist_vwap_pct` > `0.2402` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2402
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=198)

- **FILTRO** `volumen_regimen` < `0.7782` → IC=-0.333 (n=70)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7782
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=143)

- **FILTRO** `sigma_h` > `0.0051` → IC=-0.355 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=117)

- **FILTRO** `dist_vwap_pct` > `0.3287` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3287
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=144)

- **FILTRO** `sigma_ewma_delta_pct` > `8.432` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.432
  - _Potencial_: sin este filtro IC_bueno=-0.280 (n=148)

- **FILTRO** `volumen_pendiente_norm` > `0.0812` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0812
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=75)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=51)

- **FILTRO** `volumen_regimen` < `1.2175` → IC=-0.269 (n=37)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2175
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=38)

- **FILTRO** `sigma_h` < `0.0018` → IC=-0.300 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=55)

- **FILTRO** `dist_vwap_pct` < `0.0689` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0689
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

- **FILTRO** `volumen_regimen` > `0.9258` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9258
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=55)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6783` → IC=-0.443 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6783
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=34)

- **FILTRO** `volumen_regimen` > `1.1069` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.1069
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=51)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.441 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=46)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.357 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=42)

- **FILTRO** `volumen_spike_ratio` < `1.7371` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.7371
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `ibs_20min` > `0.9883` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9883 (IC base=-0.225)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2367` → IC=-0.447 (n=17)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2367
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=53)

- **FILTRO** `volumen_spike_ratio` > `2.138` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.138
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1684` → IC=-0.131 (n=128)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1684
  - _Potencial_: sin este filtro IC_bueno=+0.171 (n=250)

- **FILTRO** `dist_vwap_pct` > `0.6226` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6226
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=351)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.161 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0058 (IC base=+0.079)

- **PATRÓN** `ibs_20min` > `0.641` → IC=+0.145 (n=271)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.641 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.4919` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.4919 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.1684` → IC=+0.171 (n=250)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1684 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.105` → IC=+0.150 (n=115)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.105 (IC base=+0.068)

- **PATRÓN** `libro_liquidez` > `3751.1947` → IC=+0.172 (n=129)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3751.1947 (IC base=+0.068)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.239 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=96)

- **FILTRO** `ibs_20min` < `0.5882` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5882
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=88)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.159 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0033 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.2285` → IC=+0.155 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.2285 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.206 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.146 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.1026` → IC=+0.207 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1026 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.191` → IC=+0.136 (n=149)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.191 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.138` → IC=+0.144 (n=130)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.138 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1907` → IC=+0.190 (n=98)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1907 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.2899` → IC=+0.171 (n=86)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.2899 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.150 (n=98)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3751.1947` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3751.1947 (IC base=+0.126)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.6061` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6061
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=75)

- **FILTRO** `volumen_pendiente_norm` > `0.0671` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0671
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=39)

- **FILTRO** `ibs_20min` > `0.1644` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1644
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=82)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.194 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0022 (IC base=+0.015)

- **PATRÓN** `ibs_20min` > `0.8782` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8782 (IC base=+0.015)

- **PATRÓN** `libro_liquidez` > `1624.9844` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 1624.9844 (IC base=+0.015)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.144 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0029 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.1644` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1644 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.056)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=62)

- **FILTRO** `dist_vwap_pct` > `0.1415` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1415
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=57)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.218 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.231 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.228 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.209 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.9714` → IC=+0.233 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9714 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.081` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.081 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.209 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.036)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.296)

- **PATRÓN** `elapsed_s` > `193.7` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.7 (IC base=+0.296)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.365 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `1294.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1294.0 (IC base=+0.296)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.211)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.211)

- **PATRÓN** `drift_15min` |x|≤ `2.1869` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1869 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.7195` → IC=+0.321 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7195 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `1573.0` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1573.0 (IC base=+0.211)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.296)

- **PATRÓN** `elapsed_s` > `193.7` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.7 (IC base=+0.296)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.365 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `1294.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1294.0 (IC base=+0.296)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.211)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.211)

- **PATRÓN** `drift_15min` |x|≤ `2.1869` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1869 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.7195` → IC=+0.321 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7195 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `1573.0` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1573.0 (IC base=+0.211)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=760)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2917.3018` → IC=+0.167 (n=259)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2917.3018 (IC base=+0.106)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=760)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2917.3018` → IC=+0.167 (n=259)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2917.3018 (IC base=+0.106)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=80)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=133)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=215)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=201)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=86)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1895)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=50)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=77)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.120 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 16.0 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 26.0 (IC base=+0.044)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35151.71` → IC=-0.132 (n=66)

  - _Acción_: SKIP cuando `liq_usd_total` < 35151.71
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=136)

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

- **PATRÓN** `liq_n` > `18.0` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.020)

- **PATRÓN** `liq_usd_total` > `73032.76` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `liq_usd_total` > 73032.76 (IC base=+0.020)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=140)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=828)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=782)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=435)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=203)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=647)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=647)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=519)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=381)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=381)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=175)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=175)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=110)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=75)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=89)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=113)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=212)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9815` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9815
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=88)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=95)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=245)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=245)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=136)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.42` → IC=-0.127 (n=395)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=484)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.165 (n=234)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.47 (IC base=+0.017)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **PATRÓN** `py_entrada` > `0.54` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.54 (IC base=+0.031)

- **PATRÓN** `restante_min` > `12.8` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 12.8 (IC base=+0.031)

- **PATRÓN** `profundidad_ratio` > `1136.9` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `profundidad_ratio` > 1136.9 (IC base=+0.031)

- **PATRÓN** `py_entrada` < `0.54` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.54 (IC base=+0.016)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.157 (n=68)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.56 (IC base=+0.073)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.073)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `restante_min` > `13.45` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `restante_min` > 13.45
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.227 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=41)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=46)

- **FILTRO** `restante_min` < `3.98` → IC=-0.188 (n=46)

  - _Acción_: SKIP cuando `restante_min` < 3.98
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `lag_apertura_s` > `60.98` → IC=-0.206 (n=49)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.98
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=17)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `profundidad_ratio` < `71.7` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `profundidad_ratio` < 71.7
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=34)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.143 (n=54)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=27)

- **PATRÓN** `py_entrada` < `0.52` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.52 (IC base=-0.042)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=69)

- **FILTRO** `restante_min` < `3.88` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `restante_min` < 3.88
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=45)

- **FILTRO** `lag_apertura_s` > `66.94` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.94
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=45)

- **FILTRO** `profundidad_ratio` < `70.6` → IC=-0.239 (n=44)

  - _Acción_: SKIP cuando `profundidad_ratio` < 70.6
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=45)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.44 (IC base=+0.052)

- **PATRÓN** `profundidad_ratio` > `49.7` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `profundidad_ratio` > 49.7 (IC base=+0.052)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=38)

- **FILTRO** `restante_min` < `13.48` → IC=-0.140 (n=48)

  - _Acción_: SKIP cuando `restante_min` < 13.48
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=26)

- **FILTRO** `lag_apertura_s` > `90.99` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `lag_apertura_s` > 90.99
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=25)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=56)

- **PATRÓN** `restante_min` > `13.49` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 13.49 (IC base=-0.013)

- **PATRÓN** `lag_apertura_s` < `90.83` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 90.83 (IC base=-0.013)

- **PATRÓN** `py_entrada` < `0.6` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.6 (IC base=+0.024)

- **PATRÓN** `restante_min` > `13.48` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `restante_min` > 13.48 (IC base=+0.024)

- **PATRÓN** `lag_apertura_s` < `90.67` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `lag_apertura_s` < 90.67 (IC base=+0.024)

- **PATRÓN** `profundidad_ratio` > `4.8` → IC=+0.128 (n=41)

  - _Acción_: Kelly boost +0.64€ cuando `profundidad_ratio` > 4.8 (IC base=+0.024)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `restante_min` < `3.75` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `restante_min` < 3.75
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=34)

- **FILTRO** `lag_apertura_s` > `76.72` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `lag_apertura_s` > 76.72
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=35)

- **PATRÓN** `lag_apertura_s` < `76.72` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `lag_apertura_s` < 76.72 (IC base=-0.014)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.175 (n=75)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=43)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=64)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.170 (n=101)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=35)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=7705)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.168 (n=3700)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=11380)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.165 (n=3855)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=11765)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.206 (n=640)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=1986)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.188 (n=664)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=2012)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.208 (n=677)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2130)

- **FILTRO** `ibs_20min` > `0.2806` → IC=-0.166 (n=701)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2806
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=2106)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.172 (n=645)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=1975)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.175 (n=668)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=2144)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2218)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2293)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3033)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.175 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=407)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.144 (n=130)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=398)

- **FILTRO** `libro_liquidez` < `17011.7455` → IC=-0.143 (n=228)

  - _Acción_: SKIP cuando `libro_liquidez` < 17011.7455
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=685)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `hora_utc` > `18.0` → IC=-0.146 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=257)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.214 (n=82)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=255)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `drift_20min_pct` |x|> `0.2315` → IC=-0.120 (n=314)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2315
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=612)

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

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.032)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=10587)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=23730)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.275 (n=8466)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=25851)

- **FILTRO** `ibs_7min` < `0.2775` → IC=-0.235 (n=8579)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2775
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=25738)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=11575)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=22742)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.231 (n=10594)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=32706)

- **FILTRO** `ibs_7min` > `0.2917` → IC=-0.178 (n=10806)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2917
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=32494)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.138 (n=1726)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3984)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=1360)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4350)

- **FILTRO** `ibs_7min` < `0.7109` → IC=-0.253 (n=1884)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7109
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3826)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.189 (n=1251)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=4459)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.258 (n=1835)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=5610)

- **FILTRO** `drift_7min_pct` |x|> `0.1372` → IC=-0.129 (n=1860)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1372
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=5585)

- **FILTRO** `ibs_7min` > `0.7857` → IC=-0.208 (n=1861)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7857
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=5584)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.140 (n=1393)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4519)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.252 (n=1440)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4472)

- **FILTRO** `ibs_7min` < `0.7471` → IC=-0.195 (n=1478)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7471
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=4434)

- **FILTRO** `ballena_activa_n` > `159.0` → IC=-0.177 (n=1474)

  - _Acción_: SKIP cuando `ballena_activa_n` > 159.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=4438)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=1388)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4630)

- **FILTRO** `ibs_7min` > `0.2609` → IC=-0.181 (n=1502)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2609
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4516)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.181 (n=1497)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4521)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.168 (n=1335)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=4105)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.304 (n=1357)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=4083)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.245 (n=1789)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3651)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.222 (n=1205)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4235)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.240 (n=1830)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=6141)

- **FILTRO** `ibs_7min` > `0.7458` → IC=-0.173 (n=1992)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7458
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=5979)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=1823)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=3835)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.234 (n=1670)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=3988)

- **FILTRO** `ibs_7min` < `0.7397` → IC=-0.185 (n=1414)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7397
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4244)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.175 (n=1400)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=4258)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.264 (n=1284)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4514)

- **FILTRO** `ibs_7min` > `0.2748` → IC=-0.179 (n=1449)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2748
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4349)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.183 (n=1409)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4389)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.263 (n=1373)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4567)

- **FILTRO** `ibs_7min` < `0.2903` → IC=-0.234 (n=1482)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2903
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=4458)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.178 (n=1953)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=6294)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.255 (n=1849)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=3808)

- **FILTRO** `ibs_7min` < `0.299` → IC=-0.225 (n=1414)

  - _Acción_: SKIP cuando `ibs_7min` < 0.299
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4243)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.214 (n=1362)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4295)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.208 (n=1831)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=5990)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1124)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=557)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=325)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=569)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3978` → IC=+0.130 (n=784)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3978 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.114)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.154 (n=261)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 459.6089 (IC base=+0.114)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4374` → IC=+0.145 (n=60)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4374 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.205 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `453.526` → IC=+0.138 (n=158)

  - _Acción_: Kelly boost +0.69€ cuando `total_vol_5m` < 453.526 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.172 (n=62)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 12.0 (IC base=+0.138)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.147 (n=66)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 11.0 (IC base=+0.097)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4137` → IC=+0.194 (n=109)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio` |x|> 0.4137 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.122 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 4.0 (IC base=+0.103)

- **PATRÓN** `total_vol_5m` < `384.339` → IC=+0.203 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 384.339 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 75.0 (IC base=+0.103)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.167 (n=136)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.229 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `6100.528` → IC=+0.156 (n=120)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 6100.528 (IC base=+0.128)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.134 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 13.0 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3584.1484` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3584.1484 (IC base=+0.100)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0046` → IC=-0.262 (n=271)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=134)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `54.3209` → IC=-0.328 (n=62)

  - _Acción_: SKIP cuando `T_h` > 54.3209
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=64)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.235 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.117)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.211 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `2.719` → IC=-0.226 (n=199)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.719
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=203)

- **FILTRO** `sigma_h` > `0.0095` → IC=-0.318 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.297 (n=259)

- **FILTRO** `sigma_h` < `0.0044` → IC=-0.330 (n=86)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.293 (n=259)

- **FILTRO** `T_h` > `61.7816` → IC=-0.331 (n=258)

  - _Acción_: SKIP cuando `T_h` > 61.7816
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=87)

- **PATRÓN** `pct_vs_K` |x|≤ `1.14` → IC=+0.180 (n=101)

  - _Acción_: Kelly boost +0.90€ cuando `pct_vs_K` |x|≤ 1.14 (IC base=-0.114)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `79.3043` → IC=-0.149 (n=95)

  - _Acción_: SKIP cuando `T_h` > 79.3043
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=47)

- **FILTRO** `pct_vs_K` |x|> `2.9087` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9087
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=110)

- **FILTRO** `pct_vs_K` |x|> `2.9509` → IC=-0.435 (n=44)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9509
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=86)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.9806` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `T_h` > 135.9806
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=86)

- **FILTRO** `pct_vs_K` |x|> `2.4229` → IC=-0.357 (n=54)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4229
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=60)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.328 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=82)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.328 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=82)

- **FILTRO** `T_h` > `60.9515` → IC=-0.327 (n=73)

  - _Acción_: SKIP cuando `T_h` > 60.9515
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=36)

- **PATRÓN** `pct_vs_K` |x|≤ `1.3415` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.3415 (IC base=-0.198)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `T_h` > `132.7892` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `T_h` > 132.7892
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=65)

- **FILTRO** `pct_vs_K` |x|> `4.8556` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.8556
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=73)

- **FILTRO** `sigma_h` < `0.0146` → IC=-0.375 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0146
  - _Potencial_: sin este filtro IC_bueno=-0.308 (n=24)

- **FILTRO** `T_h` > `58.31` → IC=-0.389 (n=52)

  - _Acción_: SKIP cuando `T_h` > 58.31
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=18)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1186` → IC=+0.451 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1186 (IC base=+0.378)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.407 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.378)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.427 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.378)

- **PATRÓN** `T_h` > `0.4704` → IC=+0.435 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4704 (IC base=+0.378)

- **PATRÓN** `dist_50` > `0.4377` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4377 (IC base=+0.378)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.378)

- **PATRÓN** `edge` > `0.1118` → IC=+0.456 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1118 (IC base=+0.416)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.416)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.442 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.416)

- **PATRÓN** `T_h` < `0.6208` → IC=+0.424 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6208 (IC base=+0.416)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.462 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.416)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.492 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.472 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.416)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1078` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1078 (IC base=+0.414)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.400 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.414)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.450 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.414)

- **PATRÓN** `T_h` < `0.9168` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9168 (IC base=+0.414)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.469 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.414)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.429 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.414)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0154` → IC=+0.472 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0154 (IC base=+0.464)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.446 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.464)

- **PATRÓN** `T_h` > `0.8497` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8497 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.464 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.464 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.464)

- **PATRÓN** `edge` > `0.1135` → IC=+0.467 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1135 (IC base=+0.460)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.485 (n=67)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.460)

- **PATRÓN** `T_h` > `0.9332` → IC=+0.467 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9332 (IC base=+0.460)

- **PATRÓN** `dist_50` > `0.5` → IC=+0.482 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.5 (IC base=+0.460)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.464 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.460)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=196)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=303)

- **PATRÓN** `streak_estiramiento` < `0.4763` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `streak_estiramiento` < 0.4763 (IC base=+0.030)

- **PATRÓN** `streak_estiramiento` < `0.5654` → IC=+0.164 (n=132)

  - _Acción_: Kelly boost +0.82€ cuando `streak_estiramiento` < 0.5654 (IC base=+0.040)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=18)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.014)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `2331737.7` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 2331737.7
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=46)

- **FILTRO** `streak_estiramiento` > `0.479` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.479
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=37)

- **PATRÓN** `streak_estiramiento` < `0.479` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.479 (IC base=-0.008)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.130 (n=79)

  - _Acción_: Kelly boost +0.65€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 49.0 (IC base=+0.061)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=92)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=36)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=31)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=797)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=803)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=423)

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
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=640)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1179)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=792)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=770)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3032)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1540)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1548)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.193 (n=578)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0043 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.228 (n=578)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.0511` → IC=+0.202 (n=578)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0511 (IC base=+0.187)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2172` → IC=+0.193 (n=578)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.2172 (IC base=+0.187)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.234 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.199 (n=1613)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.187)

- **PATRÓN** `ibs_15` > `0.6087` → IC=+0.267 (n=1733)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6087 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.3024` → IC=+0.188 (n=574)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.3024 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.6111` → IC=+0.182 (n=1648)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.6111 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.899` → IC=+0.275 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.899 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `8780.1789` → IC=+0.198 (n=578)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 8780.1789 (IC base=+0.187)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=684)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.221 (n=385)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.294 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.210)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2587` → IC=+0.254 (n=128)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2587 (IC base=+0.210)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.275 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.242 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.210)

- **PATRÓN** `ibs_15` > `0.7077` → IC=+0.275 (n=384)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7077 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.261 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.537` → IC=+0.275 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.537 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `16111.0352` → IC=+0.238 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16111.0352 (IC base=+0.210)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.172 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0035 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.142 (n=269)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.005 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.161 (n=178)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.179 (n=135)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.133)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1201` → IC=+0.162 (n=146)

  - _Acción_: Kelly boost +0.81€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1201 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.154 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.137 (n=422)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.6559` → IC=+0.255 (n=361)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6559 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.11` → IC=+0.154 (n=287)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.11 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.307` → IC=+0.216 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.307 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `9459.3828` → IC=+0.143 (n=183)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 9459.3828 (IC base=+0.133)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.176 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=106)

- **FILTRO** `ibs_15` > `0.2079` → IC=-0.250 (n=34)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2079
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=104)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.271 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.1543` → IC=+0.192 (n=180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1543 (IC base=+0.169)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0781` → IC=+0.183 (n=181)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio_macro` |x|> 0.0781 (IC base=+0.169)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2673` → IC=+0.219 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2673 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.189 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `ibs_15` > `0.6122` → IC=+0.261 (n=203)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6122 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.122` → IC=+0.183 (n=118)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.122 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` < `0.6791` → IC=+0.171 (n=232)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.6791 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.389 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=152)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3074.7539` → IC=+0.277 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3074.7539 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.219 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.169)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.6834` → IC=-0.160 (n=104)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6834
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=1076)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.943` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.943 (IC base=+0.000)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0234` → IC=+0.273 (n=152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0234 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.0827` → IC=+0.218 (n=200)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0827 (IC base=+0.194)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0394` → IC=+0.198 (n=455)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio_macro` |x|> 0.0394 (IC base=+0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0904` → IC=+0.254 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0904 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.231 (n=158)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.194)

- **PATRÓN** `ibs_15` > `0.5676` → IC=+0.286 (n=455)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5676 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.3546` → IC=+0.210 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3546 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.8177` → IC=+0.196 (n=528)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.8177 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.941` → IC=+0.222 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.941 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.356` → IC=+0.197 (n=411)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 7.356 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2912.3955` → IC=+0.279 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2912.3955 (IC base=+0.194)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.155 (n=514)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1176 (IC base=+0.053)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.349 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.346)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.369 (n=197)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.346)

- **PATRÓN** `drift_60min` |x|≤ `0.1082` → IC=+0.352 (n=289)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1082 (IC base=+0.346)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0705` → IC=+0.359 (n=432)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0705 (IC base=+0.346)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1326` → IC=+0.384 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1326 (IC base=+0.346)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.366 (n=437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.346)

- **PATRÓN** `ibs_15` > `0.7873` → IC=+0.387 (n=433)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7873 (IC base=+0.346)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.386 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.346)

- **PATRÓN** `dist_vwap_pct` < `0.1081` → IC=+0.347 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1081 (IC base=+0.346)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.247` → IC=+0.353 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.247 (IC base=+0.346)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.018` → IC=+0.346 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.018 (IC base=+0.346)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.351 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.346)

- **PATRÓN** `libro_liquidez` > `3456.6166` → IC=+0.357 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3456.6166 (IC base=+0.346)

- **PATRÓN** `ballena_activa_n` < `457.0` → IC=+0.368 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 457.0 (IC base=+0.346)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.359 (n=211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.350)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.378 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.350)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.378 (n=80)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.350)

- **PATRÓN** `drift_15min` |x|≤ `0.4231` → IC=+0.361 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4231 (IC base=+0.350)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0763` → IC=+0.359 (n=239)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0763 (IC base=+0.350)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1241` → IC=+0.392 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1241 (IC base=+0.350)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.376 (n=240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.350)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.384 (n=240)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.350)

- **PATRÓN** `dist_vwap_pct` > `0.3935` → IC=+0.403 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3935 (IC base=+0.350)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.381` → IC=+0.359 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.381 (IC base=+0.350)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.353 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.350)

- **PATRÓN** `libro_liquidez` > `11090.434` → IC=+0.370 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11090.434 (IC base=+0.350)

- **PATRÓN** `ballena_activa_n` < `569.0` → IC=+0.396 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 569.0 (IC base=+0.350)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.337 (n=194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.339)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.378 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.339)

- **PATRÓN** `drift_60min` |x|≤ `0.1054` → IC=+0.348 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1054 (IC base=+0.339)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.363 (n=173)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.339)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.365 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.339)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.403 (n=91)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.339)

- **PATRÓN** `ibs_15` > `0.743` → IC=+0.393 (n=194)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.743 (IC base=+0.339)

- **PATRÓN** `dist_vwap_pct` > `0.4534` → IC=+0.373 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4534 (IC base=+0.339)

- **PATRÓN** `dist_vwap_pct` < `0.1133` → IC=+0.350 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1133 (IC base=+0.339)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.031` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.031 (IC base=+0.339)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.341 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.339)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.339)

- **PATRÓN** `libro_liquidez` > `3469.9204` → IC=+0.347 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3469.9204 (IC base=+0.339)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0129` → IC=-0.223 (n=694)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2086)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.204 (n=963)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1817)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1366` → IC=+0.249 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1366 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.6395` → IC=+0.272 (n=661)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6395 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.190 (n=530)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0765` → IC=+0.244 (n=1732)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0765 (IC base=-0.029)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1785` → IC=+0.240 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1785 (IC base=-0.029)

- **PATRÓN** `ibs_15` < `0.346` → IC=+0.275 (n=1938)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.346 (IC base=-0.029)

- **PATRÓN** `dist_vwap_pct` > `0.6856` → IC=+0.299 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6856 (IC base=-0.029)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.221 (n=417)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=1255)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.226 (n=418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=1254)

- **FILTRO** `sigma_ewma_delta_pct` > `19.521` → IC=-0.253 (n=298)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.521
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1374)

- **FILTRO** `libro_liquidez` < `14458.3413` → IC=-0.205 (n=551)

  - _Acción_: SKIP cuando `libro_liquidez` < 14458.3413
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=1121)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.165 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0028 (IC base=+0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2051` → IC=+0.291 (n=84)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2051 (IC base=+0.085)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.335 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.085)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.127 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 12.0 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.7497` → IC=+0.329 (n=185)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7497 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.099` → IC=+0.283 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.099 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` < `0.3672` → IC=+0.278 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3672 (IC base=+0.085)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.163 (n=402)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.153 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0068 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0041` → IC=+0.171 (n=281)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0041 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0736` → IC=+0.216 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0736 (IC base=+0.151)

- **PATRÓN** `drift_15min` |x|≤ `0.4169` → IC=+0.182 (n=105)

  - _Acción_: Kelly boost +0.91€ cuando `drift_15min` |x|≤ 0.4169 (IC base=+0.151)

- **PATRÓN** `delta_ratio_macro` |x|> `0.061` → IC=+0.153 (n=315)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.061 (IC base=+0.151)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.232 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.205 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.151)

- **PATRÓN** `ibs_15` > `0.6642` → IC=+0.264 (n=316)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6642 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.6362` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6362 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.189 (n=226)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.031` → IC=+0.157 (n=269)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 9.031 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=402)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `11008.7835` → IC=+0.183 (n=143)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 11008.7835 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.246 (n=742)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.4379` → IC=+0.235 (n=742)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4379 (IC base=+0.232)

- **PATRÓN** `drift_15min` |x|≤ `0.4743` → IC=+0.254 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4743 (IC base=+0.232)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2046` → IC=+0.260 (n=336)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2046 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.252 (n=284)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.232)

- **PATRÓN** `ibs_15` < `0.2696` → IC=+0.283 (n=653)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2696 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.7529` → IC=+0.324 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7529 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.593` → IC=+0.250 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.593 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.346` → IC=+0.240 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.346 (IC base=+0.232)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.252 (n=163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=492)

- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.223 (n=222)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=433)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.270 (n=163)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=492)

- **PATRÓN** `ibs_15` > `0.9` → IC=+0.300 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9 (IC base=-0.174)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0766` → IC=+0.226 (n=297)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0766 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3455` → IC=+0.258 (n=332)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3455 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7388` → IC=+0.229 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7388 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1869` → IC=+0.223 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1869 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1995` → IC=-0.205 (n=276)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1995
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=536)

- **FILTRO** `sigma_h` > `0.0197` → IC=-0.259 (n=405)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=407)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.259 (n=210)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=602)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1385` → IC=+0.300 (n=233)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1385 (IC base=-0.040)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.107` → IC=+0.336 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.107 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.3391` → IC=+0.305 (n=515)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3391 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.9133` → IC=+0.338 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9133 (IC base=-0.040)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `dist_vwap_pct` > `0.1565` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1565 (IC base=+0.054)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `dist_vwap_pct` > `0.1565` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1565 (IC base=+0.054)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.305 (n=465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.334 (n=233)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2402` → IC=+0.312 (n=232)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2402 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.343 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=729)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8408` → IC=+0.327 (n=696)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8408 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.4357` → IC=+0.336 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4357 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.344 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.293 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `13060.5836` → IC=+0.299 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13060.5836 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.308 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.354 (n=128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2616` → IC=+0.308 (n=128)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2616 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3892` → IC=+0.313 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3892 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.316 (n=383)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.345 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.364 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `16178.7073` → IC=+0.323 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16178.7073 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.313 (n=314)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.0684` → IC=+0.307 (n=138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0684 (IC base=+0.298)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.306 (n=209)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.298)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.330 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.317 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.298)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.339 (n=314)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` > `0.2774` → IC=+0.307 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2774 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` < `0.1109` → IC=+0.302 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1109 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.331 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.303 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.298)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2547` → IC=-0.158 (n=71)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2547
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=216)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1143` → IC=-0.171 (n=71)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1143
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=216)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.164 (n=111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=336)

- **FILTRO** `ballena_activa_n` > `56.0` → IC=-0.208 (n=46)

  - _Acción_: SKIP cuando `ballena_activa_n` > 56.0
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=140)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1232` → IC=-0.159 (n=42)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1232
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=127)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1681` → IC=-0.250 (n=22)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1681
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1055` → IC=-0.289 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1055
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

### UPDOWN_OU_5M#ETH#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.133 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0943` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0943
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.2131` → IC=-0.231 (n=24)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2131
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

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
- **PATRÓN** `T_h` > `79.068` → IC=+0.220 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 79.068 (IC base=+0.204)

- **PATRÓN** `ratio` < `0.9779` → IC=+0.466 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9779 (IC base=+0.204)

- **PATRÓN** `T_h` > `145.7785` → IC=+0.394 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7785 (IC base=+0.332)

- **PATRÓN** `ratio` > `1.0115` → IC=+0.286 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0115 (IC base=+0.332)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `121.3227` → IC=+0.219 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 121.3227 (IC base=+0.179)

- **PATRÓN** `ratio` < `0.973` → IC=+0.446 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.179)

- **PATRÓN** `T_h` > `103.3918` → IC=+0.288 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.283)

- **PATRÓN** `ratio` > `1.0474` → IC=+0.354 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0474 (IC base=+0.283)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `93.6267` → IC=+0.287 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 93.6267 (IC base=+0.244)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.424 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.244)

- **PATRÓN** `T_h` > `103.7717` → IC=+0.325 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.7717 (IC base=+0.312)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.330 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.312)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1359` → IC=+0.457 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1359 (IC base=+0.403)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6087 sube el IC de +0.187 a +0.267 en UPDOWN_GBM#15min (n=1733). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7077 sube el IC de +0.210 a +0.275 en UPDOWN_GBM#BTC#15min (n=384). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6559 sube el IC de +0.133 a +0.255 en UPDOWN_GBM#ETH#15min (n=361). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6122 sube el IC de +0.169 a +0.261 en UPDOWN_GBM#SOL#15min (n=203). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5676 sube el IC de +0.194 a +0.286 en UPDOWN_GBM#XRP#15min (n=455). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.053 a +0.155 en UPDOWN_GBM#XRP#15min (n=514). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6395 sube el IC de -0.066 a +0.272 en UPDOWN_GBM_15M_TARDIO (n=661). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.346 sube el IC de -0.029 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=1938). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7497 sube el IC de +0.085 a +0.329 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=185). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6642 sube el IC de +0.151 a +0.264 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=316). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2696 sube el IC de +0.232 a +0.283 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=653). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9 sube el IC de -0.174 a +0.300 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=18). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3455 sube el IC de -0.042 a +0.258 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=332). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3391 sube el IC de -0.040 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=515). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8408 sube el IC de +0.292 a +0.327 en UPDOWN_GBM_IBS_ALTO (n=696). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.287 a +0.316 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=383). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.298 a +0.339 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=314). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7873 sube el IC de +0.346 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=433). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.350 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=240). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.743 sube el IC de +0.339 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=194). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1356 | +0.102 | +208.52€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1356 | +0.102 | +208.52€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1015 | +0.112 | +180.82€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1015 | +0.112 | +180.82€ | 2 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 29326 | -0.085 | -3913.90€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1547 | -0.034 | -222.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 27779 | -0.088 | -3691.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3817 | -0.099 | -633.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3817 | -0.099 | -633.59€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1547 | -0.034 | -222.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1547 | -0.034 | -222.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3484 | -0.096 | -788.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3484 | -0.096 | -788.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7550 | -0.019 | -716.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7550 | -0.019 | -716.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7155 | -0.089 | -451.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7155 | -0.089 | -451.85€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5773 | -0.163 | -1100.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5773 | -0.163 | -1100.81€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 19723 | -0.026 | +3927.43€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5128 | +0.001 | +1808.56€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 14595 | -0.035 | +2118.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 19723 | -0.026 | +3927.43€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5128 | +0.001 | +1808.56€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 14595 | -0.035 | +2118.87€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1478 | -0.103 | -191.97€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 168 | -0.053 | -21.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1310 | -0.110 | -170.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 780 | -0.091 | -97.63€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 144 | -0.048 | -16.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 491 | -0.125 | -74.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 467 | -0.127 | -69.10€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 97651 | +0.113 | -4749.76€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 14549 | +0.185 | -421.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 396 | -0.073 | -50.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 76433 | +0.101 | -4060.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6273 | +0.107 | -216.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 12707 | +0.099 | -1024.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 47 | -0.173 | -2.03€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 12645 | +0.101 | -1010.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 19711 | +0.132 | -349.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4581 | +0.203 | -133.86€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 12671 | +0.113 | -167.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2417 | +0.102 | -25.53€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 12746 | +0.090 | -1145.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 54 | -0.107 | -8.00€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 12677 | +0.092 | -1126.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 20745 | +0.124 | -373.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5649 | +0.176 | -67.67€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 12813 | +0.106 | -239.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2271 | +0.099 | -57.45€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 19022 | +0.114 | -1091.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4170 | +0.189 | -217.82€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 299 | -0.032 | +3.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 12968 | +0.092 | -742.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1585 | +0.128 | -134.00€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 12720 | +0.100 | -765.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 48 | -0.040 | +7.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 12659 | +0.100 | -772.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 15476 | +0.192 | -1005.78€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 15476 | +0.192 | -1005.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3670 | +0.168 | -385.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3670 | +0.168 | -385.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1376 | +0.198 | -14.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1376 | +0.198 | -14.08€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3618 | +0.180 | -306.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3618 | +0.180 | -306.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3192 | +0.240 | -103.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3192 | +0.240 | -103.33€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3541 | +0.193 | -209.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3541 | +0.193 | -209.68€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 732 | +0.428 | -23.40€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 732 | +0.428 | -23.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 284 | +0.437 | -3.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 284 | +0.437 | -3.23€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 277 | +0.428 | -7.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 277 | +0.428 | -7.80€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 161 | +0.408 | -9.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 161 | +0.408 | -9.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 53486 | +0.197 | -4189.49€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 53486 | +0.197 | -4189.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9236 | +0.176 | -1071.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9236 | +0.176 | -1071.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 8556 | +0.224 | -305.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 8556 | +0.224 | -305.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 9235 | +0.173 | -1097.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 9235 | +0.173 | -1097.65€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 8653 | +0.218 | -353.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 8653 | +0.218 | -353.31€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 8839 | +0.203 | -578.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 8839 | +0.203 | -578.54€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8967 | +0.193 | -782.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8967 | +0.193 | -782.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 20229 | +0.118 | +179.44€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 20229 | +0.118 | +179.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 10042 | +0.121 | +142.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 10042 | +0.121 | +142.47€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 10187 | +0.114 | +36.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 10187 | +0.114 | +36.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1530 | +0.290 | -13.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1530 | +0.290 | -13.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 684 | +0.278 | -16.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 684 | +0.278 | -16.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 734 | +0.292 | +0.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 734 | +0.292 | +0.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 112 | +0.342 | +2.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 112 | +0.342 | +2.77€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 675 | +0.436 | -2.47€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 675 | +0.436 | -2.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 321 | +0.435 | -2.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 321 | +0.435 | -2.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 310 | +0.439 | -0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 310 | +0.439 | -0.14€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 44 | +0.391 | +0.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 44 | +0.391 | +0.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1161 | +0.071 | -53.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 405 | +0.053 | -37.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 756 | +0.081 | -15.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 918 | +0.078 | -23.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 162 | +0.067 | -8.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 756 | +0.081 | -15.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 182 | +0.016 | -32.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 182 | +0.016 | -32.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 37783 | +0.098 | -1088.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3109 | +0.091 | +33.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 34674 | +0.099 | -1121.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 21150 | +0.102 | -303.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3109 | +0.091 | +33.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 18041 | +0.104 | -336.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 7195 | +0.108 | -26.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 7195 | +0.108 | -26.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 9438 | +0.081 | -758.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 9438 | +0.081 | -758.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 842 | +0.218 | -101.00€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 842 | +0.218 | -101.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 842 | +0.218 | -101.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 842 | +0.218 | -101.00€ | 2 | 4 |
| ✅ GBM_LATE_15M | 26939 | +0.084 | +12907.04€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 26939 | +0.084 | +12907.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4498 | +0.195 | +3312.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4498 | +0.195 | +3312.13€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 4001 | +0.178 | +2819.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4001 | +0.178 | +2819.78€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 4725 | +0.198 | +3511.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4725 | +0.198 | +3511.53€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 3906 | +0.023 | +872.84€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3906 | +0.023 | +872.84€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3853 | -0.032 | +880.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3853 | -0.032 | +880.82€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 5956 | -0.040 | +1509.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5956 | -0.040 | +1509.94€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 28599 | +0.086 | +14966.81€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 28599 | +0.086 | +14966.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5433 | +0.014 | +2836.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5433 | +0.014 | +2836.50€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5974 | +0.015 | +1251.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5974 | +0.015 | +1251.60€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4065 | +0.264 | +4112.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4065 | +0.264 | +4112.81€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4682 | +0.004 | +898.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4682 | +0.004 | +898.94€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4624 | +0.029 | +1762.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4624 | +0.029 | +1762.57€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3821 | +0.278 | +4104.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3821 | +0.278 | +4104.38€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 21627 | +0.169 | +16239.78€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 21627 | +0.169 | +16239.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3262 | +0.207 | +2602.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3262 | +0.207 | +2602.74€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3406 | +0.149 | +2489.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3406 | +0.149 | +2489.04€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3412 | +0.208 | +2717.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3412 | +0.208 | +2717.56€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3620 | +0.133 | +2535.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3620 | +0.133 | +2535.51€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4036 | +0.117 | +2808.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4036 | +0.117 | +2808.09€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3891 | +0.205 | +3086.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3891 | +0.205 | +3086.85€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 5516 | +0.132 | +2429.01€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 5516 | +0.132 | +2429.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 211 | +0.110 | +81.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 211 | +0.110 | +81.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1538 | +0.127 | +724.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1538 | +0.127 | +724.57€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1652 | +0.149 | +775.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1652 | +0.149 | +775.69€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1235 | +0.114 | +454.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1235 | +0.114 | +454.92€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 27069 | +0.176 | +20354.48€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 27069 | +0.176 | +20354.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4287 | +0.222 | +3643.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4287 | +0.222 | +3643.12€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4233 | +0.152 | +2818.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4233 | +0.152 | +2818.08€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4477 | +0.225 | +3840.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4477 | +0.225 | +3840.77€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4380 | +0.137 | +3017.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4380 | +0.137 | +3017.53€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4736 | +0.115 | +3083.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4736 | +0.115 | +3083.66€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4956 | +0.208 | +3951.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4956 | +0.208 | +3951.32€ | 0 | 24 |
| ✅ GBM_LATE_5M | 7406 | +0.156 | +4452.92€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 7406 | +0.156 | +4452.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 625 | +0.192 | +453.04€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 625 | +0.192 | +453.04€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1817 | +0.149 | +1207.46€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1817 | +0.149 | +1207.46€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2537 | +0.166 | +1572.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2537 | +0.166 | +1572.58€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 701 | +0.132 | +328.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 701 | +0.132 | +328.42€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 837 | +0.116 | +326.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 837 | +0.116 | +326.92€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1849 | +0.067 | +732.40€ | 2 | 13 |
| ✅ GBM_LATE_60M#60min | 1849 | +0.067 | +732.40€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 676 | +0.090 | +264.53€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 676 | +0.090 | +264.53€ | 0 | 14 |
| ✅ GBM_LATE_60M#ETH | 610 | +0.069 | +290.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 610 | +0.069 | +290.00€ | 3 | 14 |
| ✅ GBM_LATE_60M#SOL | 563 | +0.036 | +177.87€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 563 | +0.036 | +177.87€ | 2 | 10 |
| 🚫 GBM_LATE_60M_FADE | 390 | -0.253 | -18.40€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 390 | -0.253 | -18.40€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 148 | -0.220 | -6.61€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 148 | -0.220 | -6.61€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 128 | -0.254 | -5.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 128 | -0.254 | -5.96€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 114 | -0.284 | -5.83€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 114 | -0.284 | -5.83€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 739 | +0.073 | +163.22€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 739 | +0.073 | +163.22€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 289 | +0.064 | +54.25€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 289 | +0.064 | +54.25€ | 2 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 223 | +0.038 | +9.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 223 | +0.038 | +9.70€ | 3 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 227 | +0.120 | +99.27€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 227 | +0.120 | +99.27€ | 2 | 12 |
| ✅ LATE_WINDOW_5MIN | 102 | +0.260 | +85.53€ | 0 | 10 |
| ✅ LATE_WINDOW_5MIN#5min | 102 | +0.260 | +85.53€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 102 | +0.260 | +85.53€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 102 | +0.260 | +85.53€ | 0 | 10 |
| ✅ LEADLAG_BTC_XRP_15M | 2104 | +0.106 | +588.84€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2104 | +0.106 | +588.84€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2104 | +0.106 | +588.84€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2104 | +0.106 | +588.84€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 385 | -0.081 | -35.31€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 385 | -0.081 | -35.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 96 | -0.061 | -5.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 96 | -0.061 | -5.23€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 140 | -0.028 | -5.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 140 | -0.028 | -5.25€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 2094 | +0.009 | +21.22€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2094 | +0.009 | +21.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 107 | +0.023 | -0.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 107 | +0.023 | -0.08€ | 1 | 2 |
| ✅ LIQUIDACIONES_5M#BTC | 237 | -0.011 | +8.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 237 | -0.011 | +8.35€ | 5 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 168 | -0.024 | -5.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 168 | -0.024 | -5.38€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 875 | +0.025 | +22.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 875 | +0.025 | +22.75€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 475 | +0.001 | -4.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 475 | +0.001 | -4.40€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 232 | +0.000 | -0.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 232 | +0.000 | -0.03€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M | 1123 | -0.043 | -26.63€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1123 | -0.043 | -26.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 318 | -0.044 | -13.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 318 | -0.044 | -13.73€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 379 | -0.028 | -1.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 379 | -0.028 | -1.40€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 426 | -0.056 | -11.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 426 | -0.056 | -11.50€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 1790 | -0.018 | +35.48€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 854 | -0.019 | +8.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 936 | -0.018 | +27.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 45 | +0.011 | +5.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 26 | +0.036 | +3.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 19 | -0.023 | +1.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 437 | +0.033 | +55.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 205 | +0.022 | +15.66€ | 0 | 4 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 232 | +0.043 | +39.51€ | 0 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 237 | -0.052 | -8.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 115 | -0.064 | -8.43€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 122 | -0.040 | -0.28€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 332 | -0.042 | -15.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 149 | -0.043 | -6.30€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 183 | -0.041 | -8.90€ | 4 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 308 | +0.000 | +19.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 156 | +0.006 | +11.28€ | 4 | 6 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 152 | -0.006 | +8.09€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 431 | -0.050 | -20.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 203 | -0.042 | -8.11€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 228 | -0.057 | -12.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14569 | -0.012 | -210.16€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14569 | -0.012 | -210.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3286 | -0.020 | -63.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3286 | -0.020 | -63.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 30700 | -0.006 | +1353.93€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 30700 | -0.006 | +1353.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5420 | +0.018 | +655.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5420 | +0.018 | +655.86€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4715 | -0.027 | -43.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4715 | -0.027 | -43.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5483 | +0.015 | +470.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5483 | +0.015 | +470.10€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4496 | -0.052 | -147.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4496 | -0.052 | -147.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5154 | -0.010 | +204.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5154 | -0.010 | +204.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5432 | +0.008 | +214.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5432 | +0.008 | +214.29€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5969 | -0.060 | -146.85€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5969 | -0.060 | -146.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1441 | -0.084 | -39.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1441 | -0.084 | -39.55€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 671 | -0.120 | -26.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 671 | -0.120 | -26.78€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1743 | -0.079 | -35.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1743 | -0.079 | -35.69€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 854 | -0.015 | -25.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 854 | -0.015 | -25.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3345 | +0.004 | -2.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3345 | +0.004 | -2.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1315 | +0.007 | +7.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1315 | +0.007 | +7.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 77617 | -0.072 | +1734.88€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 77617 | -0.072 | +1734.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 13155 | -0.078 | +781.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 13155 | -0.078 | +781.20€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 11930 | -0.094 | -580.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 11930 | -0.094 | -580.27€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 13411 | -0.067 | +713.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 13411 | -0.067 | +713.50€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 11456 | -0.094 | -211.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 11456 | -0.094 | -211.87€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 14187 | -0.048 | +412.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 14187 | -0.048 | +412.15€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 13478 | -0.062 | +620.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 13478 | -0.062 | +620.17€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7715 | -0.026 | -132.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7715 | -0.026 | -132.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1742 | -0.034 | -13.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1742 | -0.034 | -13.89€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2177 | -0.020 | -24.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2177 | -0.020 | -24.34€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1051 | -0.044 | -19.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1051 | -0.044 | -19.27€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 746 | -0.020 | -23.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 746 | -0.020 | -23.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1179 | +0.108 | +398.06€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 1043 | +0.114 | +385.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 238 | +0.138 | +118.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 238 | +0.138 | +118.70€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 199 | +0.097 | +47.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 199 | +0.097 | +47.88€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 217 | +0.103 | +78.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 217 | +0.103 | +78.23€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 181 | +0.128 | +80.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 181 | +0.128 | +80.60€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 208 | +0.100 | +60.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 208 | +0.100 | +60.07€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 562 | -0.053 | -58.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 562 | -0.053 | -58.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 115 | -0.013 | +0.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 115 | -0.013 | +0.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 69 | -0.134 | -19.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 69 | -0.134 | -19.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 166 | -0.059 | -24.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 166 | -0.059 | -24.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 118 | -0.017 | -2.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 118 | -0.017 | -2.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 94 | -0.073 | -12.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 94 | -0.073 | -12.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 590 | -0.108 | -49.72€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 271 | -0.159 | -64.60€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 223 | -0.202 | -67.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 48 | +0.040 | +2.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 204 | -0.073 | +1.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 160 | -0.080 | -7.07€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 44 | -0.043 | +8.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 115 | -0.047 | +13.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 93 | -0.068 | +7.11€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 476 | -0.136 | -67.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 747 | -0.202 | -31.92€ | 4 | 1 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 309 | -0.201 | -28.65€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 272 | -0.197 | -28.25€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 255 | -0.216 | -22.80€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 223 | -0.224 | -27.46€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 183 | -0.181 | +19.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 167 | -0.180 | +14.86€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 662 | -0.203 | -40.85€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 312 | +0.408 | +226.50€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 32 | +0.088 | -2.58€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 32 | +0.088 | -2.58€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 81 | +0.380 | +59.35€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 81 | +0.380 | +59.35€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 199 | +0.465 | +169.73€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 199 | +0.465 | +169.73€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 312 | +0.408 | +226.50€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 537 | +0.036 | +20.56€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 537 | +0.036 | +20.56€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 256 | +0.035 | +6.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 256 | +0.035 | +6.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 36 | +0.079 | +2.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 36 | +0.079 | +2.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 56 | +0.000 | -1.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 56 | +0.000 | -1.02€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 189 | +0.039 | +13.20€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 189 | +0.039 | +13.20€ | 2 | 3 |
| ✅ STREAK_FADE_5M | 2823 | -0.022 | -115.03€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2823 | -0.022 | -115.03€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 818 | -0.018 | -26.83€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 818 | -0.018 | -26.83€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 570 | -0.023 | -23.26€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 570 | -0.023 | -23.26€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1280 | -0.021 | -50.01€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1280 | -0.021 | -50.01€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 75 | -0.058 | -7.51€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 75 | -0.058 | -7.51€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 37 | -0.013 | -3.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 37 | -0.013 | -3.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 8170 | +0.025 | +140.42€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8170 | +0.025 | +140.42€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2210 | +0.024 | +29.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2210 | +0.024 | +29.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1857 | +0.035 | +55.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1857 | +0.035 | +55.84€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2499 | +0.016 | +13.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2499 | +0.016 | +13.86€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1604 | +0.030 | +40.75€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1604 | +0.030 | +40.75€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7606 | +0.014 | -27.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7606 | +0.014 | -27.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3051 | +0.018 | -1.97€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3051 | +0.018 | -1.97€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2983 | +0.014 | -13.99€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2983 | +0.014 | -13.99€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1572 | +0.008 | -11.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1572 | +0.008 | -11.05€ | 2 | 0 |
| ✅ UPDOWN_GBM | 40981 | +0.033 | +2560.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 10848 | +0.071 | +2028.81€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1476 | +0.004 | +5.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 26036 | +0.023 | +511.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2468 | +0.001 | +15.63€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4248 | +0.071 | +491.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 760 | +0.156 | +315.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3455 | +0.053 | +175.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 7650 | +0.039 | +548.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1369 | +0.087 | +314.00€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 395 | +0.016 | +6.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 4715 | +0.037 | +202.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1112 | +0.002 | +23.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 59 | -0.090 | +1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4807 | +0.042 | +306.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 718 | +0.139 | +252.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4061 | +0.025 | +54.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 8774 | +0.021 | +345.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2744 | +0.048 | +305.78€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 387 | +0.006 | +7.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 4763 | +0.012 | +39.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 830 | -0.004 | -9.71€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 50 | -0.135 | +3.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 9525 | +0.015 | +236.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2609 | +0.027 | +178.12€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 379 | -0.004 | -2.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5969 | +0.014 | +62.71€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 526 | +0.006 | +1.59€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 42 | -0.182 | -3.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 5975 | +0.039 | +635.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2648 | +0.086 | +662.63€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 254 | -0.004 | -3.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3073 | +0.002 | -23.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 151 | -0.134 | +0.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 577 | +0.346 | +185.57€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 577 | +0.346 | +185.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 319 | +0.350 | +99.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 319 | +0.350 | +99.12€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 258 | +0.339 | +86.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 258 | +0.339 | +86.44€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 12685 | -0.037 | +2724.79€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 12685 | -0.037 | +2724.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 860 | -0.046 | +358.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 860 | -0.046 | +358.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2306 | -0.120 | +20.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2306 | -0.120 | +20.65€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 456 | +0.181 | +307.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 456 | +0.181 | +307.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1407 | +0.208 | +849.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1407 | +0.208 | +849.65€ | 1 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3810 | -0.065 | +569.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3810 | -0.065 | +569.25€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3846 | -0.074 | +619.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3846 | -0.074 | +619.16€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 146 | +0.041 | +9.21€ | 2 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 146 | +0.041 | +9.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 146 | +0.041 | +9.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 146 | +0.041 | +9.21€ | 2 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 928 | +0.292 | +744.01€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 928 | +0.292 | +744.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 510 | +0.287 | +388.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 510 | +0.287 | +388.00€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 418 | +0.298 | +356.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 418 | +0.298 | +356.01€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 734 | -0.113 | -84.23€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 734 | -0.113 | -84.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 214 | -0.083 | -16.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 214 | -0.083 | -16.23€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 71 | -0.199 | -8.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 71 | -0.199 | -8.62€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2483 | +0.301 | +1240.78€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 859 | +0.250 | +121.37€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 937 | +0.290 | +403.74€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 687 | +0.377 | +715.68€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.059) — sin ventaja clara. oversold(IBS<0.3): IC=+0.047 n=14527 | neutral: IC=+0.030 n=15294 | overbought(IBS>0.7): IC=+0.090 n=14619
  - _Datos_: n=46031 IC=+0.056 PNL=+5683.53€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 548 celda(s) pasan gate riguroso completo de 2278 evaluadas (n>=40) y 3249 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.027 < 0.08 — monitorear
  - _Datos_: n=2609 IC=+0.027 PNL=+178.12€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=937/15 IC=+0.290 PNL=+403.74€ | BTC: n=859/15 IC=+0.250 PNL=+121.37€ | SOL: n=687/15 IC=+0.377 PNL=+715.68€

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
  - _Estado_: 40919 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.122 n=366/60 | contraria IC=+0.159 n=341 | gap=-0.037 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=309, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 181 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=830/40 IC=-0.004 PNL=-9.71€ | BTC#60min: n=1112/40 IC=+0.002 PNL=+23.76€ | SOL#60min: n=526/40 IC=+0.006 PNL=+1.59€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.050 n=354933 | tras_1loss IC=+0.081 n=275035 | tras_2loss IC=+0.051 n=115306/40 | gap=-0.000 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.016 n=4777 | contrario_BTC IC=+0.027 n=4270/40 | gap=+0.011 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.185 > 0.08 con n=347 PNL=+223.07€
  - _Datos_: n=347 IC=+0.185 PNL=+223.07€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.217 > 0.08 con n=404 PNL=+311.34€
  - _Datos_: n=404 IC=+0.217 PNL=+311.34€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.256 > 0.08 con n=43 PNL=+34.94€
  - _Datos_: n=43 IC=+0.256 PNL=+34.94€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.328 > 0.1 con n=2029 PNL=+1125.32€
  - _Datos_: n=2029 IC=+0.328 PNL=+1125.32€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=309 IC=+0.063 PNL=+31.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=309 IC=+0.063 PNL=+31.84€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=54 IC=+0.179 PNL=+34.09€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=54 IC=+0.179 PNL=+34.09€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=39197 IC=+0.033 PNL=+2441.83€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=39197 IC=+0.033 PNL=+2441.83€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 3/15 ops en el filtro definido (IC actual=+0.045 PNL=+5.14€)
  - _Datos_: n=3 IC=+0.045 PNL=+5.14€

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
  - _Estado_: n=1730 IC=+0.007 PNL=+2.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1730 IC=+0.007 PNL=+2.02€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=738 IC=-0.013 PNL=+13.61€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=738 IC=-0.013 PNL=+13.61€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=532 IC=+0.019 PNL=+22.73€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=532 IC=+0.019 PNL=+22.73€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.187 > 0.1 con n=2310 PNL=+1462.94€
  - _Datos_: n=2310 IC=+0.187 PNL=+1462.94€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1288 IC=+0.051 PNL=+92.00€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1288 IC=+0.051 PNL=+92.00€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1369 IC=+0.087 PNL=+314.00€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1369 IC=+0.087 PNL=+314.00€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=6172 PNL=+1474.24€
  - _Datos_: n=6172 IC=+0.084 PNL=+1474.24€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=156 IC=-0.234 PNL=-2.93€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=156 IC=-0.234 PNL=-2.93€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=273 IC=-0.042 PNL=-5.56€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=273 IC=-0.042 PNL=-5.56€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=570 IC=+0.025 PNL=+44.71€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=570 IC=+0.025 PNL=+44.71€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=56 IC=+0.052 PNL=+3.51€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=56 IC=+0.052 PNL=+3.51€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=6010 IC=-0.002 PNL=-6.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6010 IC=-0.002 PNL=-6.83€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.171 > 0.08 con n=68 PNL=+18.45€
  - _Datos_: n=68 IC=+0.171 PNL=+18.45€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.260 n=102) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=102 IC=+0.260 PNL=+85.53€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=7717 IC=+0.038 PNL=+499.29€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=7717 IC=+0.038 PNL=+499.29€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=2500 IC=+0.057 PNL=+304.66€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2500 IC=+0.057 PNL=+304.66€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.104 > 0.08 con n=372 PNL=+104.15€
  - _Datos_: n=372 IC=+0.104 PNL=+104.15€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.148 > 0.08 con n=645 PNL=+161.58€
  - _Datos_: n=645 IC=+0.148 PNL=+161.58€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.08 con n=488 PNL=+234.64€
  - _Datos_: n=488 IC=+0.116 PNL=+234.64€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=49398 IC=+0.114 PNL=+17326.58€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=49398 IC=+0.114 PNL=+17326.58€

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
  - _Estado_: n=6069 IC=+0.040 PNL=+448.88€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6069 IC=+0.040 PNL=+448.88€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.02 con n=665 PNL=+246.41€
  - _Datos_: n=665 IC=+0.118 PNL=+246.41€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=147 IC=-0.044 PNL=+35.89€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=147 IC=-0.044 PNL=+35.89€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.446 > 0.1 con n=1174 PNL=+1163.79€
  - _Datos_: n=1174 IC=+0.446 PNL=+1163.79€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=14630 IC=+0.054 PNL=+1752.40€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=14630 IC=+0.054 PNL=+1752.40€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.202 > 0.1 con n=3756 PNL=+2046.93€
  - _Datos_: n=3756 IC=+0.202 PNL=+2046.93€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.144 < -0.1 con n=248 PNL=+26.49€
  - _Datos_: n=248 IC=-0.144 PNL=+26.49€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2042 IC=+0.053 PNL=+222.84€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2042 IC=+0.053 PNL=+222.84€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=83 IC=-0.135 PNL=+2.08€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=83 IC=-0.135 PNL=+2.08€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.1 con n=449 PNL=+137.91€
  - _Datos_: n=449 IC=+0.130 PNL=+137.91€

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
  - _Estado_: n=19077 IC=-0.138 PNL=+1200.26€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=19077 IC=-0.138 PNL=+1200.26€

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
  - _Estado_: n=2034 IC=+0.140 PNL=+1133.19€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2034 IC=+0.140 PNL=+1133.19€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.08 con n=2271 PNL=+1450.30€
  - _Datos_: n=2271 IC=+0.189 PNL=+1450.30€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=4310 IC=+0.024 PNL=+154.25€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4310 IC=+0.024 PNL=+154.25€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=2186 PNL=+1146.51€
  - _Datos_: n=2186 IC=+0.086 PNL=+1146.51€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.08 con n=511 PNL=+264.17€
  - _Datos_: n=511 IC=+0.210 PNL=+264.17€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.239 < -0.1 con n=1879 PNL=-223.07€
  - _Datos_: n=1879 IC=-0.239 PNL=-223.07€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=5616 IC=+0.169 PNL=+3743.24€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=5616 IC=+0.169 PNL=+3743.24€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.08 con n=78 PNL=+27.38€
  - _Datos_: n=78 IC=+0.100 PNL=+27.38€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2074 IC=+0.065 PNL=+602.28€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2074 IC=+0.065 PNL=+602.28€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.181 > 0.08 con n=1892 PNL=+1335.76€
  - _Datos_: n=1892 IC=+0.181 PNL=+1335.76€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3127 IC=-0.030 PNL=+813.76€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3127 IC=-0.030 PNL=+813.76€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=570 PNL=-51.55€
  - _Datos_: n=570 IC=+0.087 PNL=-51.55€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.236 > 0.08 con n=3414 PNL=-308.03€
  - _Datos_: n=3414 IC=+0.236 PNL=-308.03€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 39/40 ops en el filtro definido (IC actual=-0.012 PNL=+3.98€)
  - _Datos_: n=39 IC=-0.012 PNL=+3.98€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.105 n=1070) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1070 IC=+0.105 PNL=+267.40€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.343 > 0.08 con n=279 PNL=+103.18€
  - _Datos_: n=279 IC=+0.343 PNL=+103.18€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=447) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=447 IC=+0.411 PNL=+630.53€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=9236 IC=+0.176 PNL=-1071.57€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=9236 IC=+0.176 PNL=-1071.57€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.208 > 0.1 con n=142 PNL=+87.89€
  - _Datos_: n=142 IC=+0.208 PNL=+87.89€
