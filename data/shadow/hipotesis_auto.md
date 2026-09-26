# Hipótesis automáticas — 2026-09-26 17:59 UTC
_Generado por shadow_postmortem.py sobre 623636 resoluciones (PNL=+71274.76€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=511)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.236 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.209 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.8026` → IC=+0.257 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8026 (IC base=+0.140)

- **PATRÓN** `banda_z` > `4.083` → IC=+0.164 (n=546)

  - _Acción_: Kelly boost +0.82€ cuando `banda_z` > 4.083 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=585)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `3000.2192` → IC=+0.150 (n=364)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3000.2192 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=511)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.054)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=420)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=376)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.258 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.149)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.149)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.265 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.149)

- **PATRÓN** `banda_z` > `4.287` → IC=+0.177 (n=438)

  - _Acción_: Kelly boost +0.89€ cuando `banda_z` > 4.287 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=496)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `4494.3377` → IC=+0.150 (n=198)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4494.3377 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11802.6658` → IC=+0.122 (n=146)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 11802.6658 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.160 (n=145)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 94.0 (IC base=+0.056)

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
- **FILTRO** `restante_s_al_confirmar` < `146.18` → IC=-0.222 (n=7290)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.18
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=21881)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `137.45` → IC=-0.250 (n=950)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 137.45
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2852)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.51` → IC=-0.308 (n=871)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.51
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2613)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `165.94` → IC=-0.207 (n=1778)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 165.94
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=5334)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.48` → IC=-0.338 (n=1435)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.48
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=4307)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.206 (n=14313)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3598)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5663.2952` → IC=+0.177 (n=2293)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 5663.2952 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.138 (n=11843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=14461)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.231 (n=11305)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=5814)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7852.9054` → IC=+0.176 (n=2200)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7852.9054 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1780)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1741)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=2195)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `15944.5355` → IC=+0.236 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15944.5355 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.205 (n=1570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.208 (n=1744)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.263 (n=1582)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2228)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `15869.986` → IC=+0.216 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15869.986 (IC base=+0.202)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.174 (n=335)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.615 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.144 (n=237)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4624.034 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.144 (n=366)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.105)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.144 (n=840)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.120 (n=564)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `5830.4537` → IC=+0.162 (n=223)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5830.4537 (IC base=+0.105)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=2910)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.147 (n=2483)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.344 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.349 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.235 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.232)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.153 (n=479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=619)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.254 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=563)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `1311.0387` → IC=+0.151 (n=683)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1311.0387 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=723)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.432 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.160 (n=1117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 7.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.167 (n=601)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 7.0 (IC base=+0.159)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=740)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.159)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.175 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.365 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.165 (n=189)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `1244.5613` → IC=+0.154 (n=229)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1244.5613 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.209 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.113)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=11970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=11466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.225 (n=3923)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `5111.8837` → IC=+0.335 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5111.8837 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=2884)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.172 (n=2746)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=2734)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.167)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=939)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.243 (n=939)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.348 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.239)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=2693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=2720)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2316)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.249 (n=2504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.325 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.239)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=2655)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.197 (n=2048)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.433 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.427 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `11138.7656` → IC=+0.456 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11138.7656 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.442 (n=102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `14120.495` → IC=+0.444 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14120.495 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.442 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.435 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.426 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `3369.9988` → IC=+0.442 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3369.9988 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.409 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.407)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.409 (n=108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.407)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.421 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.407)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.409 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.407)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=35622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.236 (n=15868)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=7230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.181 (n=4935)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=6660)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=6405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=6397)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.261 (n=3632)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=6486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=6484)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.173)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.230 (n=3205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=2416)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.267 (n=2213)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.210 (n=5898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=2374)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=2536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=5960)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2235)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=5431)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.125 (n=5007)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.16 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=5019)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=6633)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.68` → IC=+0.138 (n=5004)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.68 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=2732)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.12` → IC=+0.127 (n=2493)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.12 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.140 (n=2748)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.136 (n=3691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 8.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `3.32` → IC=+0.142 (n=2484)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.32 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=2699)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.126 (n=2537)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.2 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.132 (n=2787)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.26` → IC=+0.137 (n=2527)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.26 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `4109.4232` → IC=+0.306 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4109.4232 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.298 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.326 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `4267.8515` → IC=+0.298 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4267.8515 (IC base=+0.277)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.330 (n=386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1733.724` → IC=+0.315 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1733.724 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.346 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.341)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.368 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.341)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.384 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.341)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.370 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.341)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.441 (n=454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.438 (n=451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.437 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `2554.5498` → IC=+0.435 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2554.5498 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=247)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.447 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.925` → IC=+0.451 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.925 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.439 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `1981.0007` → IC=+0.463 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1981.0007 (IC base=+0.439)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.309 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.258)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1367.7996` → IC=+0.285 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.7996 (IC base=+0.258)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.309 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.258)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1367.7996` → IC=+0.285 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.7996 (IC base=+0.258)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4857` → IC=+0.123 (n=8435)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.4857 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.9831` → IC=+0.243 (n=2813)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9831 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` < `0.6245` → IC=+0.250 (n=2401)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6245 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.968` → IC=+0.178 (n=3224)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 5.968 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.248 (n=2301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2036 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` > `1.0429` → IC=+0.261 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0429 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.3025` → IC=+0.223 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3025 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` > `1.4616` → IC=+0.204 (n=5806)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4616 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.5703` → IC=+0.134 (n=10177)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5703 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.6054` → IC=+0.203 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6054 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.187 (n=1582)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6973 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `1.0501` → IC=+0.177 (n=1629)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.0501 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.226 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.5706` → IC=+0.201 (n=5427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5706 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `131.0` → IC=+0.212 (n=5863)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 131.0 (IC base=+0.066)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.184 (n=631)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0049 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.175 (n=631)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0082 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.3482` → IC=+0.167 (n=1892)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3482 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.173 (n=909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.168 (n=1273)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 11.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.136` → IC=+0.266 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.136 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.215 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.165 (n=1773)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.178 (n=1931)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.04 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.245 (n=1296)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.275 (n=483)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.248 (n=993)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0517` → IC=+0.293 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0517 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.526` → IC=+0.241 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.526 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.479` → IC=+0.246 (n=1506)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.479 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.265 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.6113` → IC=+0.246 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6113 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=1599)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.234 (n=645)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.236 (n=642)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=1532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.217 (n=1487)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9861` → IC=+0.271 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9861 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.1948` → IC=+0.219 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1948 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.3609` → IC=+0.219 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3609 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.76` → IC=+0.262 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.76 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `1.2505` → IC=+0.219 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2505 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `1.0769` → IC=+0.226 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0769 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.245 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.3798` → IC=+0.233 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3798 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `11154.639` → IC=+0.224 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11154.639 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.164 (n=1012)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0038 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.165 (n=506)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=680)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.7028` → IC=+0.170 (n=1517)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7028 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1289` → IC=+0.155 (n=1359)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1289 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.289` → IC=+0.152 (n=242)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 11.289 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.302` → IC=+0.145 (n=1385)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.302 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.150 (n=1517)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.1954 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.8505` → IC=+0.141 (n=1011)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8505 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1558` → IC=+0.177 (n=404)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1558 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.154 (n=1407)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4221` → IC=+0.148 (n=1407)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4221 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `14087.0235` → IC=+0.146 (n=1011)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 14087.0235 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.169 (n=590)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 234.0 (IC base=+0.140)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.209 (n=628)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=1978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=1693)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.187` → IC=+0.256 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.187 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.189 (n=1633)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.3561` → IC=+0.194 (n=253)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3561 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.6102` → IC=+0.190 (n=1794)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.6102 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=1314)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.220 (n=1430)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6119` → IC=+0.211 (n=1624)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6119 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0643` → IC=+0.246 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0643 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.721` → IC=+0.234 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.721 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.54` → IC=+0.210 (n=1763)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.54 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3506` → IC=+0.266 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3506 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7621` → IC=+0.206 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7621 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.1841` → IC=+0.215 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1841 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.216 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1909.5784` → IC=+0.214 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1909.5784 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.215 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.144 (n=102)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=2292)

- **PATRÓN** `ibs_20min` > `0.9463` → IC=+0.216 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9463 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.3596` → IC=+0.325 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3596 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.5438` → IC=+0.329 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5438 (IC base=+0.028)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.74` → IC=+0.162 (n=741)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.74 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.328 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8553 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `1.2014` → IC=+0.338 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2014 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.353 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4113` → IC=+0.350 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4113 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.330 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.330 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.6717` → IC=+0.209 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6717 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` < `0.6866` → IC=+0.167 (n=388)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6866 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `1.1607` → IC=+0.149 (n=294)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.1607 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.2269` → IC=+0.220 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2269 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.5239` → IC=+0.172 (n=740)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.5239 (IC base=+0.019)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.172 (n=62)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=342)

- **FILTRO** `ibs_20min` < `0.2909` → IC=-0.209 (n=101)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2909
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=303)

- **FILTRO** `ibs_20min` > `0.25` → IC=-0.125 (n=2275)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=1133)

- **FILTRO** `sigma_ewma_delta_pct` > `8.719` → IC=-0.210 (n=364)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.719
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=3044)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.223 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7619 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `1.0858` → IC=+0.286 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0858 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` < `0.6236` → IC=+0.279 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6236 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `0.7675` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7675 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `2.5444` → IC=+0.281 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5444 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` > `1.4528` → IC=+0.264 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4528 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.295 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.124 (n=1133)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.25 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7235` → IC=+0.263 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7235 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `1.0932` → IC=+0.236 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0932 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1582` → IC=+0.260 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1582 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.272 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6536` → IC=-0.184 (n=593)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6536
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1793)

- **FILTRO** `ibs_20min` < `0.7193` → IC=-0.154 (n=1574)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7193
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=812)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.199 (n=459)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1927)

- **FILTRO** `ibs_20min` > `0.77` → IC=-0.203 (n=867)

  - _Acción_: SKIP cuando `ibs_20min` > 0.77
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=2633)

- **PATRÓN** `dist_vwap_pct` > `0.4585` → IC=+0.311 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4585 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2822` → IC=+0.307 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2822 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.6825` → IC=+0.307 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6825 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.295 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.1123` → IC=+0.291 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1123 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.7985` → IC=+0.296 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7985 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.8811` → IC=+0.271 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8811 (IC base=-0.021)

- **PATRÓN** `volumen_regimen` < `0.6536` → IC=+0.254 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6536 (IC base=-0.021)

- **PATRÓN** `volumen_regimen` > `1.2485` → IC=+0.285 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2485 (IC base=-0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2438` → IC=+0.285 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2438 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.1392` → IC=+0.260 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1392 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.5237` → IC=+0.249 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5237 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.196 (n=3556)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0098 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4756` → IC=+0.187 (n=9519)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4756 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `1.0612` → IC=+0.287 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0612 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.615` → IC=+0.156 (n=4987)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.615 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6901` → IC=+0.250 (n=3399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6901 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.270 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4637` → IC=+0.237 (n=2058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4637 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6456` → IC=+0.247 (n=2058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6456 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.269 (n=5688)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 95.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.159 (n=3525)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0091 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5494` → IC=+0.154 (n=9282)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5494 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7135` → IC=+0.242 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7135 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2498` → IC=+0.241 (n=2984)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2498 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7088` → IC=+0.241 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7088 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.205` → IC=+0.250 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.205 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2421` → IC=+0.304 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2421 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.6001` → IC=+0.260 (n=1834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6001 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2951` → IC=+0.260 (n=1890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2951 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `84.0` → IC=+0.268 (n=4048)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 84.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2558` → IC=-0.151 (n=734)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2558
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=2203)

- **FILTRO** `sigma_ewma_delta_pct` > `4.552` → IC=-0.160 (n=560)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.552
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1872)

- **PATRÓN** `ibs_20min` > `0.8961` → IC=+0.265 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8961 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.851` → IC=+0.205 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.851 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2226` → IC=+0.275 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2226 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4339` → IC=+0.175 (n=312)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4339 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.1445` → IC=+0.204 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1445 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.189 (n=406)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 13.0 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.2202` → IC=+0.466 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2202 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `2.4765` → IC=+0.452 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4765 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` > `1.7555` → IC=+0.446 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7555 (IC base=-0.018)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.018)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8648` → IC=+0.162 (n=714)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.8648 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.3026` → IC=+0.176 (n=387)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.3026 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.6746` → IC=+0.169 (n=881)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6746 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.244 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.188 (n=322)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.3955` → IC=+0.161 (n=322)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.3955 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `241.0` → IC=+0.186 (n=422)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 241.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.1524` → IC=+0.217 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1524 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `0.8539` → IC=+0.226 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8539 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2686` → IC=+0.313 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2686 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.4389` → IC=+0.212 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4389 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.234 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1598 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `461.0` → IC=+0.214 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 461.0 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.288 (n=556)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.247)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.252 (n=1672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.249 (n=1687)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.247)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.247)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.691` → IC=+0.283 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.691 (IC base=+0.247)

- **PATRÓN** `volumen_pendiente_norm` < `0.102` → IC=+0.261 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.102 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` > `3.3565` → IC=+0.264 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3565 (IC base=+0.247)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.253 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.247)

- **PATRÓN** `libro_liquidez` > `1911.2892` → IC=+0.254 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.2892 (IC base=+0.247)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.314 (n=610)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.176` → IC=+0.290 (n=593)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.176 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.323 (n=450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` < `0.0909` → IC=+0.288 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0909 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.816` → IC=+0.295 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.816 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.3376` → IC=+0.304 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3376 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.286 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `2.6975` → IC=+0.287 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6975 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.286 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `1902.4584` → IC=+0.294 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1902.4584 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.286 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.282)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.297` → IC=-0.173 (n=527)

  - _Acción_: SKIP cuando `ibs_20min` < 0.297
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1584)

- **FILTRO** `ibs_20min` > `0.7739` → IC=-0.186 (n=626)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7739
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=1880)

- **PATRÓN** `ibs_20min` > `0.9107` → IC=+0.181 (n=528)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.9107 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` > `0.4352` → IC=+0.221 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4352 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.217 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.9865` → IC=+0.243 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9865 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.5875` → IC=+0.217 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5875 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.0773` → IC=+0.260 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0773 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.5025` → IC=+0.263 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5025 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.270 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` > `0.1481` → IC=+0.216 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1481 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` < `0.3452` → IC=+0.199 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3452 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `0.6439` → IC=+0.234 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6439 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2772` → IC=+0.283 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2772 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.8269` → IC=+0.257 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8269 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `1.435` → IC=+0.234 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.435 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.254 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7333` → IC=-0.194 (n=1127)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=+0.280 (n=1127)

- **FILTRO** `ibs_20min` > `0.6875` → IC=-0.237 (n=573)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6875
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1742)

- **FILTRO** `sigma_ewma_delta_pct` > `4.723` → IC=-0.188 (n=507)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.723
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=1808)

- **PATRÓN** `ibs_20min` > `0.7333` → IC=+0.280 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7333 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `0.8569` → IC=+0.327 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8569 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.646` → IC=+0.167 (n=355)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.646 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8657` → IC=+0.304 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8657 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `0.7279` → IC=+0.293 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7279 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.296 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2703` → IC=+0.298 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2703 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4185` → IC=+0.328 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4185 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.316 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.120 (n=1533)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.5833 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` > `0.7308` → IC=+0.205 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7308 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.2196` → IC=+0.224 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2196 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.7101` → IC=+0.252 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7101 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.215 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.069` → IC=+0.215 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.069 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.46` → IC=+0.226 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.46 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.236 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.316 (n=915)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.294 (n=645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.347 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.2148` → IC=+0.315 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2148 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.623` → IC=+0.301 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.623 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` > `0.8606` → IC=+0.304 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8606 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` < `0.0782` → IC=+0.282 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0782 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.325 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.1484` → IC=+0.298 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1484 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.283 (n=1455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `2476.2478` → IC=+0.291 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2476.2478 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.303 (n=982)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.276)

- **PATRÓN** `drift_60min` |x|≤ `0.1957` → IC=+0.275 (n=648)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1957 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.286 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.276)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.279 (n=732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.276)

- **PATRÓN** `ibs_20min` < `0.14` → IC=+0.334 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.14 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `1.3398` → IC=+0.284 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3398 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.277 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2288 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.47` → IC=+0.291 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.47 (IC base=+0.276)

- **PATRÓN** `volumen_regimen` < `0.6397` → IC=+0.279 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6397 (IC base=+0.276)

- **PATRÓN** `volumen_regimen` > `1.2436` → IC=+0.309 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2436 (IC base=+0.276)

- **PATRÓN** `volumen_pendiente_norm` > `0.2372` → IC=+0.338 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2372 (IC base=+0.276)

- **PATRÓN** `volumen_spike_ratio` < `1.4234` → IC=+0.283 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4234 (IC base=+0.276)

- **PATRÓN** `volumen_spike_ratio` > `2.1403` → IC=+0.276 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1403 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `2623.4578` → IC=+0.279 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2623.4578 (IC base=+0.276)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.173 (n=2744)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0049 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.200 (n=2738)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0902` → IC=+0.184 (n=2740)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0902 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=8567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.5745` → IC=+0.219 (n=8212)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5745 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.1753` → IC=+0.194 (n=3562)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1753 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.254 (n=1677)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.2078` → IC=+0.161 (n=5442)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2078 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.6301` → IC=+0.161 (n=5443)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6301 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2424` → IC=+0.195 (n=1656)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2424 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5573` → IC=+0.168 (n=3469)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5573 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.6101` → IC=+0.177 (n=2628)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6101 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `1952.5984` → IC=+0.169 (n=7336)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1952.5984 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.181 (n=7124)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 112.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.183 (n=5248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0066 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0811` → IC=+0.210 (n=2620)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0811 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3016)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.170 (n=3707)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.4814` → IC=+0.227 (n=7860)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4814 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.2343` → IC=+0.160 (n=5698)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2343 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.344` → IC=+0.193 (n=1330)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 10.344 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.1729` → IC=+0.152 (n=5674)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1729 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.215 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5593` → IC=+0.166 (n=3156)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5593 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.248` → IC=+0.171 (n=3252)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.248 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.175 (n=6822)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 113.0 (IC base=+0.168)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.211 (n=466)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.191 (n=467)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0083 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.3418` → IC=+0.206 (n=1392)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3418 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=1464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=932)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.122` → IC=+0.307 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.122 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2301` → IC=+0.239 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2301 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.182 (n=1290)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=1422)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.244 (n=909)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.249 (n=923)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1866` → IC=+0.292 (n=689)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1866 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=930)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=508)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.3437` → IC=+0.263 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3437 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.344` → IC=+0.250 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.344 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.1603` → IC=+0.235 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1603 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.250 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4205` → IC=+0.266 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4205 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1817.84` → IC=+0.245 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1817.84 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.240 (n=410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0729` → IC=+0.194 (n=407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0729 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=1220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.4049` → IC=+0.227 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4049 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2079` → IC=+0.212 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2079 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.482` → IC=+0.236 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.482 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.6876` → IC=+0.168 (n=537)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6876 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.0696` → IC=+0.170 (n=553)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.0696 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.5031` → IC=+0.179 (n=521)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.5031 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.4541` → IC=+0.163 (n=395)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.4541 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `10634.3743` → IC=+0.171 (n=1219)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10634.3743 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.158 (n=1318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0057 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.293` → IC=+0.162 (n=1319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.293 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.189 (n=1318)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5667 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1331` → IC=+0.161 (n=1311)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1331 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.889` → IC=+0.198 (n=263)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.889 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1967` → IC=+0.159 (n=1318)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1967 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1543` → IC=+0.154 (n=403)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1543 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.442` → IC=+0.147 (n=1206)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.442 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4235` → IC=+0.137 (n=1206)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4235 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.164 (n=376)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 213.0 (IC base=+0.138)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.217 (n=626)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.2368` → IC=+0.217 (n=921)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2368 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.422` → IC=+0.275 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.422 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2039` → IC=+0.202 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2039 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.8041` → IC=+0.199 (n=579)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.8041 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.8078` → IC=+0.214 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8078 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.210 (n=1631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.235 (n=1016)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.0986` → IC=+0.249 (n=385)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0986 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.271 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.3478` → IC=+0.247 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3478 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.729` → IC=+0.259 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.729 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3512` → IC=+0.259 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3512 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7653` → IC=+0.214 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7653 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.1982` → IC=+0.230 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1982 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1907.66` → IC=+0.218 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1907.66 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.213 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.217)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.175 (n=1157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0066 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.4277` → IC=+0.159 (n=1313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4277 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.3749` → IC=+0.197 (n=1313)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3749 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1493` → IC=+0.177 (n=865)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1493 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.228 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.0351` → IC=+0.148 (n=1156)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0351 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6214` → IC=+0.148 (n=1313)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6214 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.197 (n=206)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.154 (n=429)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.5051` → IC=+0.171 (n=429)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5051 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `6488.9388` → IC=+0.185 (n=875)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 6488.9388 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `161.0` → IC=+0.147 (n=1250)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 161.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.154 (n=1378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.3828` → IC=+0.143 (n=1378)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3828 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=535)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6477` → IC=+0.172 (n=1378)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6477 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.3607` → IC=+0.135 (n=1490)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.3607 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.965` → IC=+0.160 (n=489)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 6.965 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8503` → IC=+0.148 (n=919)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8503 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.291` → IC=+0.186 (n=202)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.291 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.8007` → IC=+0.139 (n=837)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8007 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `9988.1936` → IC=+0.162 (n=625)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 9988.1936 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.153 (n=678)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0101 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=1528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5156` → IC=+0.205 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5156 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.5201` → IC=+0.196 (n=646)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.5201 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.8` → IC=+0.255 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.8 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.130 (n=1490)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2145 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.7252` → IC=+0.124 (n=1331)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7252 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.5358` → IC=+0.138 (n=633)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5358 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1553)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2904.4304` → IC=+0.195 (n=676)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2904.4304 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.134 (n=1141)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 49.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.155 (n=665)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0061 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.1048` → IC=+0.164 (n=504)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1048 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=1533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.5745` → IC=+0.210 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5745 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `1.0165` → IC=+0.138 (n=216)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 1.0165 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2064` → IC=+0.139 (n=1382)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2064 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.617` → IC=+0.135 (n=313)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 7.617 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.6379` → IC=+0.144 (n=504)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6379 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.158 (n=188)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4527` → IC=+0.129 (n=454)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4527 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2760.8425` → IC=+0.159 (n=685)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2760.8425 (IC base=+0.114)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.225 (n=1269)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=1477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=644)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.7391` → IC=+0.258 (n=1269)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7391 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.5119` → IC=+0.218 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5119 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.577` → IC=+0.240 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.577 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.205 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2068 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.8567` → IC=+0.222 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8567 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2312` → IC=+0.265 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2312 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.1479` → IC=+0.211 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1479 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.4077` → IC=+0.209 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4077 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.205 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2828.7134` → IC=+0.206 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2828.7134 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.224 (n=647)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.211 (n=667)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0917` → IC=+0.222 (n=490)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0917 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=719)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.4375` → IC=+0.247 (n=1471)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4375 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `1.2202` → IC=+0.222 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2202 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.445` → IC=+0.246 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.445 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.633` → IC=+0.216 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.633 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.293 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.1921` → IC=+0.196 (n=1167)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1921 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.200 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2595.4393` → IC=+0.209 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2595.4393 (IC base=+0.206)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.175 (n=675)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0038 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.174 (n=670)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0088 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.3528` → IC=+0.156 (n=1768)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3528 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.169 (n=1846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 8.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.5377` → IC=+0.190 (n=1795)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.5377 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.8562` → IC=+0.176 (n=331)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.8562 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.719` → IC=+0.179 (n=902)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 3.719 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.871` → IC=+0.170 (n=1183)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.871 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.161 (n=593)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.2084 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1642` → IC=+0.180 (n=554)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1642 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.164 (n=647)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.2097` → IC=+0.162 (n=879)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.2097 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=2275)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `12367.2302` → IC=+0.158 (n=670)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12367.2302 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.171 (n=1786)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 151.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.137 (n=1376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0056 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.124 (n=2078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.5238` → IC=+0.147 (n=1815)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5238 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` < `0.2101` → IC=+0.121 (n=1844)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` < 0.2101 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.6987` → IC=+0.128 (n=818)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.6987 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.4499` → IC=+0.142 (n=663)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4499 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2767.6856` → IC=+0.121 (n=1842)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2767.6856 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.125 (n=852)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 29.0 (IC base=+0.110)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.131 (n=329)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0039 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.3382` → IC=+0.130 (n=493)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.3382 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.157 (n=461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 8.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.2572` → IC=+0.156 (n=492)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.2572 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.3004` → IC=+0.148 (n=174)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.3004 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6182` → IC=+0.159 (n=165)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6182 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `10937.2581` → IC=+0.136 (n=492)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 10937.2581 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.139 (n=156)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 147.0 (IC base=+0.113)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.201 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.3378` → IC=+0.154 (n=646)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3378 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.6091` → IC=+0.183 (n=569)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6091 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.307` → IC=+0.151 (n=682)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.307 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.41` → IC=+0.151 (n=250)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.41 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.177` → IC=+0.135 (n=582)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.177 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.218` → IC=+0.140 (n=646)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.218 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `1.0609` → IC=+0.164 (n=293)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.0609 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.193 (n=174)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.1115` → IC=+0.157 (n=560)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1115 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.4203` → IC=+0.147 (n=636)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4203 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `324.0` → IC=+0.151 (n=540)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 324.0 (IC base=+0.135)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.264 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.203 (n=210)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.222 (n=210)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.9681` → IC=+0.264 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9681 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.1455` → IC=+0.205 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1455 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.200 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.948` → IC=+0.228 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.948 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.0063` → IC=+0.203 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0063 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.1544` → IC=+0.217 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1544 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2624` → IC=+0.263 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2624 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.4004` → IC=+0.224 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4004 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.7512` → IC=+0.227 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7512 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `12451.6072` → IC=+0.222 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12451.6072 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3518` → IC=+0.121 (n=520)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.60€ cuando `drift_60min` |x|≤ 0.3518 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.0837` → IC=+0.158 (n=197)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.0837 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.6865` → IC=+0.141 (n=260)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6865 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.1664` → IC=+0.134 (n=140)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1664 (IC base=+0.094)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.6016` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6016
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=546)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.170 (n=216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.009 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.5425` → IC=+0.135 (n=475)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.5425 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.170 (n=441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 8.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.269 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.9868` → IC=+0.229 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9868 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.239` → IC=+0.205 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.239 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.0712` → IC=+0.150 (n=418)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0712 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `0.7306` → IC=+0.149 (n=425)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7306 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.4827` → IC=+0.143 (n=152)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4827 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `2.2078` → IC=+0.188 (n=206)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.2078 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=511)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `3116.6987` → IC=+0.196 (n=159)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3116.6987 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.5172` → IC=+0.150 (n=421)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5172 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` < `0.7082` → IC=+0.140 (n=187)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.7082 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` < `1.5767` → IC=+0.171 (n=174)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5767 (IC base=+0.083)

- **PATRÓN** `libro_liquidez` > `2590.446` → IC=+0.129 (n=281)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2590.446 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.131 (n=369)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.083)

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
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.206 (n=3519)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=11014)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.308 (n=3545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.9628` → IC=+0.203 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9628 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.348` → IC=+0.244 (n=2651)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.348 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `0.88` → IC=+0.166 (n=4703)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.88 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.203 (n=1454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.589` → IC=+0.189 (n=3384)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.589 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `1794.8354` → IC=+0.172 (n=10547)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 1794.8354 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.196 (n=8099)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 85.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=6372)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1487` → IC=+0.190 (n=4203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1487 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=3599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.184 (n=4422)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5687` → IC=+0.236 (n=9554)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5687 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.25` → IC=+0.162 (n=5935)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.25 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.04` → IC=+0.199 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.04 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.732` → IC=+0.183 (n=9231)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.732 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.164 (n=2882)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7044 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `1.2024` → IC=+0.154 (n=2182)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2024 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2871` → IC=+0.239 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2871 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.614` → IC=+0.193 (n=2933)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.614 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.196 (n=5647)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 47.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.211 (n=596)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.211 (n=1188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.3528` → IC=+0.191 (n=1776)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3528 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.196 (n=1202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.57` → IC=+0.343 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.57 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2272` → IC=+0.253 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2272 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.2395` → IC=+0.196 (n=761)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.2395 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.261 (n=942)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.263 (n=1409)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.127` → IC=+0.283 (n=620)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.127 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=1277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.3517` → IC=+0.286 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3517 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.483` → IC=+0.263 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.483 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.279 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.4331` → IC=+0.259 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4331 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6337` → IC=+0.279 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6337 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=1556)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1812.9625` → IC=+0.264 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1812.9625 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.200 (n=567)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1134` → IC=+0.158 (n=744)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1134 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=1767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3078` → IC=+0.203 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3078 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.128` → IC=+0.185 (n=947)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.128 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.173 (n=386)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.2` → IC=+0.154 (n=1525)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.2 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.6273` → IC=+0.180 (n=564)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6273 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2656` → IC=+0.205 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2656 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1137` → IC=+0.160 (n=1437)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1137 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.7549` → IC=+0.158 (n=1089)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7549 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `11288.2763` → IC=+0.161 (n=1509)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11288.2763 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `471.0` → IC=+0.159 (n=1567)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 471.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.188 (n=489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0026 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2565` → IC=+0.167 (n=1287)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2565 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=660)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.2772` → IC=+0.234 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2772 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.6834` → IC=+0.155 (n=236)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6834 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.132` → IC=+0.165 (n=1328)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.132 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.493` → IC=+0.160 (n=245)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.493 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.303` → IC=+0.154 (n=1327)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.303 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.1847` → IC=+0.164 (n=1462)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1847 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.195 (n=392)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4038` → IC=+0.160 (n=1364)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4038 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.7551` → IC=+0.163 (n=909)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.7551 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `352.0` → IC=+0.159 (n=846)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 352.0 (IC base=+0.152)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.252 (n=574)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=1800)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1748)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.816` → IC=+0.294 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.816 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.1344` → IC=+0.219 (n=1562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1344 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.228 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.227 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1914.6584` → IC=+0.220 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.6584 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.238 (n=1604)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.171` → IC=+0.237 (n=705)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.171 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=753)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.0148` → IC=+0.308 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0148 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.748` → IC=+0.275 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.748 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.3426` → IC=+0.306 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3426 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.7482` → IC=+0.232 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7482 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.175` → IC=+0.234 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.175 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.240 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `1905.4784` → IC=+0.238 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1905.4784 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.246 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.231)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.187 (n=602)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0035 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4332` → IC=+0.148 (n=1795)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4332 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=1876)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.8757` → IC=+0.262 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8757 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.5708` → IC=+0.167 (n=505)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.5708 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.45` → IC=+0.170 (n=292)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.45 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.873` → IC=+0.156 (n=1197)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.873 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2336` → IC=+0.216 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2336 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5167` → IC=+0.153 (n=765)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5167 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.4628` → IC=+0.155 (n=580)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.4628 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `7996.0605` → IC=+0.233 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7996.0605 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.163 (n=564)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 77.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.159 (n=1284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0066 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.4448` → IC=+0.150 (n=1459)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4448 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=666)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.7091` → IC=+0.180 (n=1459)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.7091 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1587` → IC=+0.138 (n=1262)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1587 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.238` → IC=+0.167 (n=220)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.238 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6938` → IC=+0.151 (n=642)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6938 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `1.1945` → IC=+0.141 (n=486)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.1945 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.29` → IC=+0.236 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.29 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.146 (n=1386)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `7204.7935` → IC=+0.197 (n=661)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 7204.7935 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `176.0` → IC=+0.140 (n=1383)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 176.0 (IC base=+0.135)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.141 (n=1194)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0081 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=1843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.191 (n=1790)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4706 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.0929` → IC=+0.196 (n=379)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 1.0929 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.513` → IC=+0.239 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.513 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.8932` → IC=+0.136 (n=1194)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8932 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=1805)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2900.261` → IC=+0.253 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2900.261 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.131 (n=1399)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 54.0 (IC base=+0.115)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.176 (n=576)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0058 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.1334` → IC=+0.161 (n=576)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1334 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.124 (n=1783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.6389` → IC=+0.204 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6389 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2218` → IC=+0.133 (n=1405)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.2218 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.486` → IC=+0.127 (n=1666)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.486 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.7156` → IC=+0.153 (n=760)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7156 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2203` → IC=+0.167 (n=271)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2203 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.139 (n=522)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2810.5407` → IC=+0.175 (n=576)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2810.5407 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.124 (n=1353)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 51.0 (IC base=+0.114)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.227 (n=1592)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1861)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.211 (n=1601)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.258 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.2117` → IC=+0.233 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2117 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.264` → IC=+0.273 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.264 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `1.2439` → IC=+0.212 (n=1783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2439 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.6407` → IC=+0.219 (n=1782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6407 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.252 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.4984` → IC=+0.231 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4984 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.218 (n=1854)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2625.8761` → IC=+0.218 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2625.8761 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.224 (n=635)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.225 (n=635)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.212 (n=1340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.268 (n=1671)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.2377` → IC=+0.207 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2377 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.9192` → IC=+0.207 (n=2112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9192 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.857` → IC=+0.261 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.857 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.240 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.276 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.1803` → IC=+0.200 (n=1508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1803 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4288` → IC=+0.200 (n=1713)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4288 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=3201)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.184 (n=1027)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0049 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.5157` → IC=+0.170 (n=3081)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.5157 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=1215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.169 (n=1374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 6.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.9414` → IC=+0.217 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9414 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.1795` → IC=+0.172 (n=1149)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1795 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` < `0.4691` → IC=+0.160 (n=1940)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.4691 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.2` → IC=+0.195 (n=506)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.2 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `0.6332` → IC=+0.163 (n=2070)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6332 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.1707` → IC=+0.197 (n=854)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1707 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.168 (n=1015)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `1.8762` → IC=+0.169 (n=2029)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.8762 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.161 (n=3434)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `3963.7863` → IC=+0.170 (n=2054)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3963.7863 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.203 (n=806)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4847` → IC=+0.165 (n=2413)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.4847 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=873)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.166 (n=1068)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.1802` → IC=+0.176 (n=1062)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.1802 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6721` → IC=+0.172 (n=468)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.6721 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.252` → IC=+0.158 (n=2405)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.252 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.2449` → IC=+0.153 (n=2311)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2449 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.150 (n=2188)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.0721` → IC=+0.148 (n=1113)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0721 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5347` → IC=+0.159 (n=1049)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5347 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.8164` → IC=+0.149 (n=1588)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8164 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=3201)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `7068.1056` → IC=+0.158 (n=2155)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7068.1056 (IC base=+0.146)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.188 (n=357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0055 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.176 (n=362)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0034 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.0894` → IC=+0.203 (n=136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0894 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.183 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 8.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.5452` → IC=+0.200 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5452 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.2158` → IC=+0.177 (n=190)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2158 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.3732` → IC=+0.174 (n=394)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.3732 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.201` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.201 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.415` → IC=+0.178 (n=427)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 2.415 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.5812` → IC=+0.188 (n=405)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.5812 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.4501` → IC=+0.196 (n=136)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4501 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.6405` → IC=+0.208 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6405 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `12584.8678` → IC=+0.220 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12584.8678 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.218 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.179 (n=319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.176 (n=365)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1386` → IC=+0.178 (n=421)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1386 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.6091` → IC=+0.148 (n=433)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6091 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6926` → IC=+0.177 (n=91)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6926 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.2218` → IC=+0.139 (n=971)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2218 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.372` → IC=+0.163 (n=935)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.372 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8795` → IC=+0.188 (n=638)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8795 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0682` → IC=+0.165 (n=446)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0682 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.4202` → IC=+0.147 (n=318)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4202 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.150 (n=635)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `11475.1782` → IC=+0.153 (n=955)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 11475.1782 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `706.0` → IC=+0.145 (n=910)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 706.0 (IC base=+0.139)

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
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.177 (n=912)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0072 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.3801` → IC=+0.176 (n=913)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3801 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.177 (n=354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 4.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.5342` → IC=+0.187 (n=691)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.5342 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.8839` → IC=+0.181 (n=346)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.8839 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.2173` → IC=+0.178 (n=856)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2173 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.174` → IC=+0.181 (n=927)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 4.174 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.0845` → IC=+0.172 (n=913)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.0845 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6413` → IC=+0.174 (n=1036)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6413 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.190 (n=311)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.4717` → IC=+0.175 (n=1018)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.4717 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.1776` → IC=+0.175 (n=462)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.1776 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=1034)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.196 (n=284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.004 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.183 (n=852)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.161 (n=603)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 11.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.7429` → IC=+0.162 (n=852)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.7429 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.0954` → IC=+0.165 (n=852)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.0954 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.1574` → IC=+0.168 (n=390)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1574 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.639` → IC=+0.163 (n=876)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.639 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.6464` → IC=+0.196 (n=284)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6464 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.7236` → IC=+0.158 (n=761)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7236 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.1512` → IC=+0.158 (n=881)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.1512 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.174 (n=360)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.1956` → IC=+0.172 (n=735)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.1956 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `7521.4583` → IC=+0.173 (n=852)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7521.4583 (IC base=+0.156)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0129` → IC=+0.129 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0129 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.1983` → IC=+0.160 (n=189)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1983 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.325` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 7.325 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6955` → IC=+0.147 (n=117)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6955 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.1658` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1658 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.134 (n=255)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `3433.6178` → IC=+0.160 (n=236)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3433.6178 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.125 (n=246)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 67.0 (IC base=+0.113)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.172 (n=242)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0069 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.6706` → IC=+0.156 (n=242)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.6706 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.169 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 10.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.238 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1429 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.5986` → IC=+0.220 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5986 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.222` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 3.222 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.18` → IC=+0.145 (n=232)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 5.18 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.9502` → IC=+0.152 (n=162)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.9502 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.1129` → IC=+0.201 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1129 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.611` → IC=+0.151 (n=104)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.611 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.1886` → IC=+0.161 (n=107)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.1886 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `3331.2707` → IC=+0.168 (n=242)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 3331.2707 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.186 (n=205)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 47.0 (IC base=+0.136)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.208 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=392)

- **FILTRO** `dist_vwap_pct` > `0.178` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.178
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=351)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.181 (n=430)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.004 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.6641` → IC=+0.194 (n=791)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.6641 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.1487` → IC=+0.151 (n=476)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1487 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.45` → IC=+0.184 (n=207)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 11.45 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.183 (n=118)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` < `2.0999` → IC=+0.123 (n=678)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.0999 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `2435.8886` → IC=+0.134 (n=391)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2435.8886 (IC base=+0.087)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.121 (n=262)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0045 (IC base=+0.015)

- **PATRÓN** `ibs_20min` < `0.0667` → IC=+0.279 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0667 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.178` → IC=+0.123 (n=351)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.178 (IC base=+0.015)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.187` → IC=+0.132 (n=123)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 3.187 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.1373` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1373 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.5298` → IC=+0.134 (n=255)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.5298 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.4395` → IC=+0.130 (n=228)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4395 (IC base=+0.015)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.153 (n=335)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0059 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4737` → IC=+0.183 (n=304)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.4737 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.173 (n=157)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `2.0448` → IC=+0.160 (n=233)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.0448 (IC base=+0.100)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.126 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0045 (IC base=+0.062)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.167 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.3241` → IC=+0.247 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3241 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.585` → IC=+0.150 (n=121)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.585 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` < `2.3987` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.3987 (IC base=+0.062)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0059` → IC=-0.214 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0059
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=122)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=127)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.150 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.005 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.129 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.6632` → IC=+0.222 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6632 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.3353` → IC=+0.181 (n=117)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.3353 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.658` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.658 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2766` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2766 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.7354` → IC=+0.159 (n=165)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.7354 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `1133.2011` → IC=+0.158 (n=264)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1133.2011 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.7041` → IC=+0.147 (n=100)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.7041 (IC base=-0.006)

- **PATRÓN** `dist_vwap_pct` < `0.1269` → IC=+0.129 (n=103)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1269 (IC base=-0.006)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.258` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.258 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.1353` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1353 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.268` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.268 (IC base=-0.006)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=-0.006)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.276 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=94)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.233 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=98)

- **PATRÓN** `ibs_20min` > `0.6606` → IC=+0.153 (n=252)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.6606 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.2066` → IC=+0.125 (n=158)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.2066 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.438` → IC=+0.143 (n=113)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 5.438 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` > `1.062` → IC=+0.167 (n=94)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.062 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.061)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.194 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0056 (IC base=-0.032)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0714 (IC base=-0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.25` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.25 (IC base=-0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=-0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.3662` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.3662 (IC base=-0.032)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0033` → IC=-0.300 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=144)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.365 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=162)

- **FILTRO** `dist_vwap_pct` > `0.2402` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2402
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=197)

- **FILTRO** `volumen_regimen` < `0.7761` → IC=-0.345 (n=69)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7761
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=143)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.352 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=117)

- **FILTRO** `hora_utc` < `4.0` → IC=-0.305 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=137)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=154)

- **FILTRO** `sigma_ewma_delta_pct` > `8.432` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.432
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=147)

- **FILTRO** `volumen_pendiente_norm` > `0.0765` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0765
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=73)

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
- **FILTRO** `ibs_20min` < `0.899` → IC=-0.413 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` < 0.899
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.357 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=41)

- **FILTRO** `ibs_20min` > `0.8406` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8406
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=40)

- **FILTRO** `volumen_spike_ratio` < `1.7061` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.7061
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `ibs_20min` > `0.9883` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9883 (IC base=-0.225)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1754` → IC=-0.125 (n=126)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1754
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=245)

- **FILTRO** `dist_vwap_pct` > `0.6344` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6344
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=345)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.153 (n=122)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0058 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.641` → IC=+0.148 (n=268)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.641 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.4941` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.4941 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.1754` → IC=+0.160 (n=245)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1754 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.0` → IC=+0.149 (n=112)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.0 (IC base=+0.063)

- **PATRÓN** `libro_liquidez` > `3752.8201` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3752.8201 (IC base=+0.063)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.584` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.584
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=87)

- **FILTRO** `volumen_regimen` < `0.7797` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7797
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=87)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.159 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0033 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.2293` → IC=+0.158 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2293 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.214 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.1761` → IC=+0.182 (n=127)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1761 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1936` → IC=+0.135 (n=146)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1936 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.021` → IC=+0.132 (n=112)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.021 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1907` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1907 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.2899` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.2899 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.126)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.6061` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6061
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=73)

- **FILTRO** `ibs_20min` > `0.1754` → IC=-0.151 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1754
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=80)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.243 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0023 (IC base=+0.025)

- **PATRÓN** `ibs_20min` > `0.6061` → IC=+0.127 (n=73)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.6061 (IC base=+0.025)

- **PATRÓN** `libro_liquidez` > `1653.8347` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1653.8347 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.1754` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.1754 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.045)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=61)

- **FILTRO** `dist_vwap_pct` > `0.1415` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1415
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=56)

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

- **PATRÓN** `volumen_pendiente_norm` > `0.0808` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0808 (IC base=-0.042)

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

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.211)

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

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.211)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=745)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2920.5936` → IC=+0.174 (n=253)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2920.5936 (IC base=+0.107)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=745)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2920.5936` → IC=+0.174 (n=253)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2920.5936 (IC base=+0.107)

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
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=214)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=200)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=1887)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9583` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9583
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=82)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=61)

### LIQUIDACIONES_5M#BNB#5min
- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 25.0 (IC base=+0.049)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35750.18` → IC=-0.127 (n=65)

  - _Acción_: SKIP cuando `liq_usd_total` < 35750.18
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=134)

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

- **PATRÓN** `liq_n` > `18.0` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `liq_n` > 18.0 (IC base=+0.017)

- **PATRÓN** `liq_usd_total` > `73032.76` → IC=+0.147 (n=100)

  - _Acción_: Kelly boost +0.74€ cuando `liq_usd_total` > 73032.76 (IC base=+0.017)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=140)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=824)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=778)

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
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=642)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=642)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=514)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=377)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=377)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=174)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=174)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=109)

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
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=210)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9803` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9803
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=87)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=90)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=243)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=243)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=134)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.42` → IC=-0.135 (n=381)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=455)

- **FILTRO** `restante_min` < `3.83` → IC=-0.120 (n=272)

  - _Acción_: SKIP cuando `restante_min` < 3.83
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=564)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.164 (n=224)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.47 (IC base=+0.019)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.5 (IC base=+0.026)

- **PATRÓN** `restante_min` > `13.13` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` > 13.13 (IC base=+0.026)

- **PATRÓN** `profundidad_ratio` > `1112.4` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `profundidad_ratio` > 1112.4 (IC base=+0.026)

- **PATRÓN** `py_entrada` < `0.54` → IC=+0.141 (n=62)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.54 (IC base=+0.021)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.59` → IC=+0.126 (n=89)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.59 (IC base=+0.074)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` > `0.39` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=24)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=45)

- **FILTRO** `restante_min` < `3.98` → IC=-0.188 (n=46)

  - _Acción_: SKIP cuando `restante_min` < 3.98
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

- **FILTRO** `lag_apertura_s` > `61.04` → IC=-0.200 (n=48)

  - _Acción_: SKIP cuando `lag_apertura_s` > 61.04
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=17)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.54` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `py_entrada` < 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=16)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=54)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=65)

- **FILTRO** `restante_min` < `3.82` → IC=-0.314 (n=41)

  - _Acción_: SKIP cuando `restante_min` < 3.82
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=44)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=68)

- **FILTRO** `lag_apertura_s` > `70.6` → IC=-0.318 (n=42)

  - _Acción_: SKIP cuando `lag_apertura_s` > 70.6
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=43)

- **FILTRO** `profundidad_ratio` < `70.6` → IC=-0.250 (n=42)

  - _Acción_: SKIP cuando `profundidad_ratio` < 70.6
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=43)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.45 (IC base=+0.033)

- **PATRÓN** `profundidad_ratio` > `48.0` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `profundidad_ratio` > 48.0 (IC base=+0.033)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `restante_min` < `12.93` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `restante_min` < 12.93
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=35)

- **FILTRO** `lag_apertura_s` > `124.29` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `lag_apertura_s` > 124.29
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=35)

- **PATRÓN** `py_entrada` > `0.51` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.51 (IC base=-0.007)

- **PATRÓN** `restante_min` > `13.48` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `restante_min` > 13.48 (IC base=-0.007)

- **PATRÓN** `lag_apertura_s` < `90.91` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 90.91 (IC base=-0.007)

- **PATRÓN** `py_entrada` < `0.6` → IC=+0.132 (n=55)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.6 (IC base=+0.018)

- **PATRÓN** `restante_min` > `13.48` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `restante_min` > 13.48 (IC base=+0.018)

- **PATRÓN** `lag_apertura_s` < `90.9` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `lag_apertura_s` < 90.9 (IC base=+0.018)

- **PATRÓN** `profundidad_ratio` > `4.8` → IC=+0.128 (n=41)

  - _Acción_: Kelly boost +0.64€ cuando `profundidad_ratio` > 4.8 (IC base=+0.018)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `restante_min` < `3.72` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `restante_min` < 3.72
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=32)

- **FILTRO** `lag_apertura_s` > `76.72` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `lag_apertura_s` > 76.72
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=32)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.180 (n=73)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=38)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.214 (n=61)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=65)

- **FILTRO** `restante_min` < `2.81` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `restante_min` < 2.81
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=95)

- **FILTRO** `lag_apertura_s` > `131.11` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `lag_apertura_s` > 131.11
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=95)

- **PATRÓN** `py_entrada` < `0.58` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.58 (IC base=+0.017)

- **PATRÓN** `restante_min` > `3.83` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 3.83 (IC base=+0.017)

- **PATRÓN** `lag_apertura_s` < `69.99` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `lag_apertura_s` < 69.99 (IC base=+0.017)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=7666)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.168 (n=3669)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=11232)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.165 (n=3814)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=11609)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.208 (n=631)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1961)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.187 (n=657)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=1987)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.207 (n=670)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=2098)

- **FILTRO** `ibs_20min` > `0.281` → IC=-0.165 (n=691)

  - _Acción_: SKIP cuando `ibs_20min` > 0.281
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=2077)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.171 (n=642)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=1944)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.175 (n=665)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=2111)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2215)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.205 (n=751)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2285)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3015)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.175 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=404)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.144 (n=130)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=395)

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

- **FILTRO** `py_entrada` > `0.62` → IC=-0.214 (n=82)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=249)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=226)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=10450)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=23500)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.274 (n=8350)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=25600)

- **FILTRO** `ibs_7min` < `0.2794` → IC=-0.235 (n=8486)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2794
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=25464)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=11479)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=22471)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.230 (n=10483)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=32282)

- **FILTRO** `ibs_7min` > `0.2922` → IC=-0.177 (n=10690)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2922
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=32075)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=1702)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3943)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.311 (n=1339)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4306)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.252 (n=1862)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3783)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.188 (n=1249)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=4396)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.258 (n=1815)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=5537)

- **FILTRO** `drift_7min_pct` |x|> `0.1379` → IC=-0.130 (n=1837)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1379
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5515)

- **FILTRO** `ibs_7min` > `0.7875` → IC=-0.207 (n=1837)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7875
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=5515)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.139 (n=1372)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4481)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1421)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4432)

- **FILTRO** `ibs_7min` < `0.7473` → IC=-0.193 (n=1463)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7473
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=4390)

- **FILTRO** `ballena_activa_n` > `160.0` → IC=-0.177 (n=1455)

  - _Acción_: SKIP cuando `ballena_activa_n` > 160.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=4398)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=1373)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=4574)

- **FILTRO** `ibs_7min` > `0.2609` → IC=-0.181 (n=1485)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2609
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4462)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.183 (n=1476)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4471)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.166 (n=1313)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=4061)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.303 (n=1331)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=4043)

- **FILTRO** `ibs_7min` < `0.1928` → IC=-0.259 (n=1343)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1928
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4031)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.222 (n=1201)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4173)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.239 (n=1810)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=6056)

- **FILTRO** `ibs_7min` > `0.75` → IC=-0.172 (n=1962)

  - _Acción_: SKIP cuando `ibs_7min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5904)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=1802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=3796)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.233 (n=1656)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=3942)

- **FILTRO** `ibs_7min` < `0.74` → IC=-0.182 (n=1399)

  - _Acción_: SKIP cuando `ibs_7min` < 0.74
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4199)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.174 (n=1396)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4202)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.257 (n=1432)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=4297)

- **FILTRO** `ibs_7min` > `0.2745` → IC=-0.177 (n=1431)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2745
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4298)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.183 (n=1397)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4332)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.256 (n=1465)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=4422)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.233 (n=1467)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=4420)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.179 (n=1930)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=6216)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.254 (n=1827)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=3766)

- **FILTRO** `ibs_7min` < `0.299` → IC=-0.224 (n=1398)

  - _Acción_: SKIP cuando `ibs_7min` < 0.299
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4195)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.214 (n=1355)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4238)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.208 (n=1819)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=5906)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1115)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=546)

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
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=567)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3978` → IC=+0.126 (n=776)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.63€ cuando `delta_ratio` |x|> 0.3978 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.124 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 14.0 (IC base=+0.111)

- **PATRÓN** `total_vol_5m` < `469.512` → IC=+0.144 (n=259)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 469.512 (IC base=+0.111)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4376` → IC=+0.139 (n=59)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4376 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `451.687` → IC=+0.139 (n=156)

  - _Acción_: Kelly boost +0.70€ cuando `total_vol_5m` < 451.687 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 15.0 (IC base=+0.135)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4134` → IC=+0.179 (n=107)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio` |x|> 0.4134 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.097)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `total_vol_5m` < 388.5476 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.180 (n=73)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 77.0 (IC base=+0.097)

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
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.129 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 13.0 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `3584.1484` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3584.1484 (IC base=+0.096)

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

- **FILTRO** `T_h` < `97.926` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `T_h` < 97.926
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=88)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
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

- **PATRÓN** `edge` > `0.1135` → IC=+0.455 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1135 (IC base=+0.415)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.415)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.441 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.415)

- **PATRÓN** `T_h` < `0.6208` → IC=+0.424 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6208 (IC base=+0.415)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.443 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.415)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.492 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.415)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.471 (n=101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.415)

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

- **PATRÓN** `edge` > `0.115` → IC=+0.467 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.115 (IC base=+0.459)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.480 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.459)

- **PATRÓN** `T_h` > `0.9178` → IC=+0.467 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9178 (IC base=+0.459)

- **PATRÓN** `dist_50` > `0.5` → IC=+0.482 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.5 (IC base=+0.459)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.463 (n=107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.459)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=191)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=302)

- **FILTRO** `streak_estiramiento` > `0.8382` → IC=-0.172 (n=65)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8382
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=196)

- **PATRÓN** `streak_estiramiento` < `0.4763` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.4763 (IC base=+0.029)

- **PATRÓN** `streak_estiramiento` < `0.7313` → IC=+0.123 (n=173)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.7313 (IC base=+0.038)

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
- **FILTRO** `streak_estiramiento` > `0.479` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.479
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=35)

- **PATRÓN** `streak_estiramiento` < `0.479` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.479 (IC base=-0.025)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.130 (n=90)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 49.0 (IC base=+0.058)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=420)

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
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=630)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1163)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=788)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=757)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3015)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1534)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1542)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.189 (n=573)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0044 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.220 (n=777)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0512` → IC=+0.202 (n=572)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0512 (IC base=+0.186)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2154` → IC=+0.188 (n=572)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.2154 (IC base=+0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1268` → IC=+0.234 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1268 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=1595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `ibs_15` > `0.6077` → IC=+0.266 (n=1714)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6077 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.3029` → IC=+0.185 (n=566)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.3029 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.6134` → IC=+0.181 (n=1629)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.6134 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.803` → IC=+0.273 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.803 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `2959.1226` → IC=+0.195 (n=1143)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2959.1226 (IC base=+0.186)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=672)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.219 (n=379)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.291 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.207)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.250 (n=126)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.207)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.277 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.207)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.274 (n=378)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.3935` → IC=+0.257 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3935 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.199` → IC=+0.271 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.199 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `16113.4131` → IC=+0.242 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16113.4131 (IC base=+0.207)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `24.226` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 24.226
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=411)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.169 (n=134)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0035 (IC base=+0.135)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.145 (n=266)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.005 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.163 (n=176)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.135)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.181 (n=133)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.263` → IC=+0.152 (n=288)

  - _Acción_: Kelly boost +0.76€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.263 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.154 (n=293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.135 (n=179)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.6559` → IC=+0.255 (n=357)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6559 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1109` → IC=+0.159 (n=285)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1109 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.19` → IC=+0.211 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.19 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `9475.4181` → IC=+0.150 (n=181)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 9475.4181 (IC base=+0.135)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.176 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=105)

- **FILTRO** `ibs_15` > `0.2079` → IC=-0.250 (n=34)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2079
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=103)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.283 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.1498` → IC=+0.193 (n=177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1498 (IC base=+0.170)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0757` → IC=+0.187 (n=180)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.0757 (IC base=+0.170)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2673` → IC=+0.225 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2673 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.191 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `ibs_15` > `0.6122` → IC=+0.264 (n=201)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6122 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.122` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.122 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `0.6827` → IC=+0.172 (n=230)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.6827 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.389 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=231)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `3071.8702` → IC=+0.277 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3071.8702 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.223 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.170)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.698` → IC=-0.153 (n=99)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.698
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=1029)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.936` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 8.936 (IC base=-0.004)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0235` → IC=+0.270 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0235 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.216 (n=199)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.191)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0394` → IC=+0.195 (n=450)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.0394 (IC base=+0.191)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0904` → IC=+0.250 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0904 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.226 (n=155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.191)

- **PATRÓN** `ibs_15` > `0.5593` → IC=+0.281 (n=450)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5593 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.352` → IC=+0.208 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.352 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.8136` → IC=+0.193 (n=522)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.8136 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.916` → IC=+0.211 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.916 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.785` → IC=+0.195 (n=453)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 10.785 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `2914.5894` → IC=+0.283 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2914.5894 (IC base=+0.191)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.157 (n=508)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1176 (IC base=+0.053)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.347 (n=285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.344)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.372 (n=194)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.344)

- **PATRÓN** `drift_60min` |x|≤ `0.1078` → IC=+0.350 (n=285)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1078 (IC base=+0.344)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.371 (n=284)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=+0.344)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1304` → IC=+0.382 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1304 (IC base=+0.344)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.364 (n=431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.344)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.386 (n=427)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.344)

- **PATRÓN** `dist_vwap_pct` > `0.4267` → IC=+0.386 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4267 (IC base=+0.344)

- **PATRÓN** `dist_vwap_pct` < `0.1075` → IC=+0.346 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1075 (IC base=+0.344)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.231` → IC=+0.350 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.231 (IC base=+0.344)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.345 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.344)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.349 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.344)

- **PATRÓN** `libro_liquidez` > `3465.3078` → IC=+0.355 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3465.3078 (IC base=+0.344)

- **PATRÓN** `ballena_activa_n` < `460.0` → IC=+0.365 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 460.0 (IC base=+0.344)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.357 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.348)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.377 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.348)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.377 (n=79)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.348)

- **PATRÓN** `drift_15min` |x|≤ `0.4185` → IC=+0.358 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4185 (IC base=+0.348)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.357 (n=236)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.348)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1231` → IC=+0.389 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1231 (IC base=+0.348)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.374 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.348)

- **PATRÓN** `ibs_15` > `0.8154` → IC=+0.382 (n=236)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8154 (IC base=+0.348)

- **PATRÓN** `dist_vwap_pct` > `0.4001` → IC=+0.414 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4001 (IC base=+0.348)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.354 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.348)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.763` → IC=+0.352 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.763 (IC base=+0.348)

- **PATRÓN** `libro_liquidez` > `11137.3038` → IC=+0.368 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11137.3038 (IC base=+0.348)

- **PATRÓN** `ballena_activa_n` < `571.0` → IC=+0.394 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 571.0 (IC base=+0.348)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.335 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.337)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.369 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.337)

- **PATRÓN** `drift_60min` |x|≤ `0.0642` → IC=+0.351 (n=85)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0642 (IC base=+0.337)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.361 (n=171)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.337)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.363 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.337)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.401 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.337)

- **PATRÓN** `ibs_15` > `0.743` → IC=+0.392 (n=192)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.743 (IC base=+0.337)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.371 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.337)

- **PATRÓN** `dist_vwap_pct` < `0.1109` → IC=+0.356 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1109 (IC base=+0.337)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.337)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.340 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.337)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.346 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.337)

- **PATRÓN** `libro_liquidez` > `3480.6224` → IC=+0.346 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3480.6224 (IC base=+0.337)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0128` → IC=-0.221 (n=687)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0128
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2062)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.202 (n=948)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1801)

- **FILTRO** `libro_liquidez` < `3880.2832` → IC=-0.143 (n=1814)

  - _Acción_: SKIP cuando `libro_liquidez` < 3880.2832
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=935)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.250 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.6409` → IC=+0.273 (n=654)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6409 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.1081` → IC=+0.196 (n=413)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1081 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0764` → IC=+0.244 (n=1704)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0764 (IC base=-0.029)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1781` → IC=+0.238 (n=1234)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1781 (IC base=-0.029)

- **PATRÓN** `ibs_15` < `0.3462` → IC=+0.275 (n=1908)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3462 (IC base=-0.029)

- **PATRÓN** `dist_vwap_pct` > `0.6896` → IC=+0.301 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6896 (IC base=-0.029)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.224 (n=415)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=1247)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.224 (n=415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=1247)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.210 (n=1049)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=613)

- **FILTRO** `sigma_ewma_delta_pct` > `19.475` → IC=-0.252 (n=296)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.475
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1366)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.171 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0028 (IC base=+0.083)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.298 (n=82)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.083)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.331 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.083)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.123 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 12.0 (IC base=+0.083)

- **PATRÓN** `ibs_15` > `0.7497` → IC=+0.330 (n=180)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7497 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.0996` → IC=+0.282 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0996 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` < `0.3693` → IC=+0.274 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3693 (IC base=+0.083)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.166 (n=399)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.154 (n=313)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0068 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.176 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.005 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.229 (n=138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.153)

- **PATRÓN** `drift_15min` |x|≤ `0.4169` → IC=+0.182 (n=105)

  - _Acción_: Kelly boost +0.91€ cuando `drift_15min` |x|≤ 0.4169 (IC base=+0.153)

- **PATRÓN** `delta_ratio_macro` |x|> `0.061` → IC=+0.156 (n=312)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.061 (IC base=+0.153)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.234 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_15` > `0.6675` → IC=+0.264 (n=312)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6675 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.192 (n=225)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.694` → IC=+0.160 (n=251)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.694 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=399)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `11008.7835` → IC=+0.188 (n=142)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 11008.7835 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.246 (n=733)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.4386` → IC=+0.236 (n=733)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4386 (IC base=+0.232)

- **PATRÓN** `drift_15min` |x|≤ `0.476` → IC=+0.254 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.476 (IC base=+0.232)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2044` → IC=+0.261 (n=333)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2044 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.248 (n=276)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.232)

- **PATRÓN** `ibs_15` < `0.3469` → IC=+0.270 (n=733)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3469 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.7536` → IC=+0.324 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7536 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.558` → IC=+0.253 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.558 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.254` → IC=+0.240 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.254 (IC base=+0.232)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.250 (n=162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=487)

- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.221 (n=220)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=429)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.268 (n=162)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=487)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.186 (n=49)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.93€ cuando `ibs_15` > 0.5625 (IC base=-0.173)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0765` → IC=+0.227 (n=291)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0765 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.259 (n=326)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7573` → IC=+0.225 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7573 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.199` → IC=+0.224 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.199 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1996` → IC=-0.202 (n=273)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1996
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=530)

- **FILTRO** `sigma_h` > `0.0197` → IC=-0.259 (n=401)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=402)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.262 (n=204)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=599)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1363` → IC=+0.301 (n=229)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1363 (IC base=-0.040)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1053` → IC=+0.333 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1053 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.34` → IC=+0.305 (n=505)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.34 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.9056` → IC=+0.338 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9056 (IC base=-0.040)

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
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.300 (n=459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.332 (n=230)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2389` → IC=+0.305 (n=229)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2389 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1083` → IC=+0.345 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1083 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=720)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8411` → IC=+0.328 (n=688)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8411 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.4391` → IC=+0.333 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4391 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.341 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.293 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `13074.8557` → IC=+0.299 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13074.8557 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.305 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.285 (n=338)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.003 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.352 (n=126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.305 (n=126)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.384` → IC=+0.312 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.384 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.316 (n=378)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.4275` → IC=+0.353 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4275 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.362 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16193.642` → IC=+0.328 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16193.642 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.311 (n=311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.1119` → IC=+0.305 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1119 (IC base=+0.298)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.304 (n=207)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.298)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.332 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.319 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.298)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.340 (n=311)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` > `0.6145` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6145 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` < `0.1109` → IC=+0.306 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1109 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.221` → IC=+0.328 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.221 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.304 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.298)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2547` → IC=-0.158 (n=71)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2547
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=215)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1143` → IC=-0.171 (n=71)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1143
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=215)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.164 (n=111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=335)

- **FILTRO** `ballena_activa_n` > `43.0` → IC=-0.214 (n=61)

  - _Acción_: SKIP cuando `ballena_activa_n` > 43.0
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=124)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0681` → IC=-0.161 (n=57)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0681
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=111)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1232` → IC=-0.159 (n=42)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1232
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `sigma_h` > `0.0034` → IC=-0.208 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=23)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
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
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

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

- **PATRÓN** `T_h` < `111.9969` → IC=+0.295 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9969 (IC base=+0.283)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6077 sube el IC de +0.186 a +0.266 en UPDOWN_GBM#15min (n=1714). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.207 a +0.274 en UPDOWN_GBM#BTC#15min (n=378). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6559 sube el IC de +0.135 a +0.255 en UPDOWN_GBM#ETH#15min (n=357). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6122 sube el IC de +0.170 a +0.264 en UPDOWN_GBM#SOL#15min (n=201). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5593 sube el IC de +0.191 a +0.281 en UPDOWN_GBM#XRP#15min (n=450). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.053 a +0.157 en UPDOWN_GBM#XRP#15min (n=508). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6409 sube el IC de -0.066 a +0.273 en UPDOWN_GBM_15M_TARDIO (n=654). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3462 sube el IC de -0.029 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=1908). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7497 sube el IC de +0.083 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=180). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6675 sube el IC de +0.153 a +0.264 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=312). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3469 sube el IC de +0.232 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=733). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.173 a +0.186 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=49). Ya aplicado como kelly_boost=+0.93€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.042 a +0.259 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=326). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.34 sube el IC de -0.040 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=505). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8411 sube el IC de +0.292 a +0.328 en UPDOWN_GBM_IBS_ALTO (n=688). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.286 a +0.316 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=378). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.298 a +0.340 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=311). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.344 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=427). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8154 sube el IC de +0.348 a +0.382 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=236). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.743 sube el IC de +0.337 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=192). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1351 | +0.100 | +203.51€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1351 | +0.100 | +203.51€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1010 | +0.110 | +175.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1010 | +0.110 | +175.81€ | 2 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 29171 | -0.085 | -3885.41€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1540 | -0.036 | -226.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 27631 | -0.088 | -3658.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3802 | -0.099 | -626.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3802 | -0.099 | -626.29€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1540 | -0.036 | -226.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1540 | -0.036 | -226.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3484 | -0.096 | -788.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3484 | -0.096 | -788.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7491 | -0.020 | -705.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7491 | -0.020 | -705.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7112 | -0.089 | -448.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7112 | -0.089 | -448.79€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5742 | -0.164 | -1088.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5742 | -0.164 | -1088.83€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 19430 | -0.026 | +3958.66€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5053 | +0.001 | +1814.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 14377 | -0.036 | +2143.82€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 19430 | -0.026 | +3958.66€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5053 | +0.001 | +1814.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 14377 | -0.036 | +2143.82€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 96731 | +0.113 | -4760.08€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 14464 | +0.185 | -432.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 391 | -0.075 | -50.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 75649 | +0.100 | -4056.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6227 | +0.107 | -220.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 12577 | +0.099 | -1021.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 46 | -0.167 | -1.52€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 12516 | +0.101 | -1008.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 19546 | +0.132 | -369.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4565 | +0.203 | -132.37€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 12541 | +0.112 | -189.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2398 | +0.102 | -26.05€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 12616 | +0.090 | -1132.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 53 | -0.100 | -7.49€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 12548 | +0.092 | -1113.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 20550 | +0.124 | -382.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5604 | +0.175 | -77.90€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 12680 | +0.106 | -239.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2254 | +0.099 | -56.81€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 18852 | +0.114 | -1091.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4149 | +0.189 | -221.26€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 294 | -0.034 | +3.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 12834 | +0.091 | -735.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1575 | +0.127 | -137.79€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 12590 | +0.100 | -761.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 47 | -0.031 | +8.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 12530 | +0.100 | -769.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 15343 | +0.191 | -1014.71€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 15343 | +0.191 | -1014.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3640 | +0.167 | -386.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3640 | +0.167 | -386.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1349 | +0.196 | -17.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1349 | +0.196 | -17.24€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3591 | +0.180 | -307.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3591 | +0.180 | -307.16€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3168 | +0.239 | -103.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3168 | +0.239 | -103.37€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3516 | +0.192 | -214.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3516 | +0.192 | -214.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 724 | +0.427 | -24.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 724 | +0.427 | -24.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 281 | +0.436 | -3.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 281 | +0.436 | -3.53€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 274 | +0.427 | -8.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 274 | +0.427 | -8.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 159 | +0.407 | -10.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 159 | +0.407 | -10.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 52974 | +0.197 | -4136.21€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 52974 | +0.197 | -4136.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9148 | +0.176 | -1054.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9148 | +0.176 | -1054.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 8473 | +0.223 | -311.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 8473 | +0.223 | -311.68€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 9150 | +0.173 | -1087.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 9150 | +0.173 | -1087.02€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 8568 | +0.218 | -346.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 8568 | +0.218 | -346.70€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 8752 | +0.204 | -569.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 8752 | +0.204 | -569.34€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8883 | +0.193 | -766.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8883 | +0.193 | -766.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 20007 | +0.117 | +153.59€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 20007 | +0.117 | +153.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 9931 | +0.121 | +134.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 9931 | +0.121 | +134.38€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 10076 | +0.113 | +19.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 10076 | +0.113 | +19.21€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1519 | +0.289 | -19.92€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1519 | +0.289 | -19.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 678 | +0.277 | -20.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 678 | +0.277 | -20.21€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 730 | +0.291 | -1.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 730 | +0.291 | -1.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 111 | +0.341 | +2.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 111 | +0.341 | +2.12€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 671 | +0.436 | -3.09€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 671 | +0.436 | -3.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 319 | +0.435 | -2.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 319 | +0.435 | -2.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 308 | +0.439 | -0.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 308 | +0.439 | -0.50€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 44 | +0.391 | +0.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 44 | +0.391 | +0.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1152 | +0.071 | -52.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 399 | +0.054 | -36.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 753 | +0.080 | -16.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 912 | +0.078 | -24.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 159 | +0.065 | -8.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 753 | +0.080 | -16.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 179 | +0.019 | -31.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 179 | +0.019 | -31.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 37354 | +0.098 | -1115.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3078 | +0.090 | +27.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 34276 | +0.098 | -1142.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 20927 | +0.102 | -325.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3078 | +0.090 | +27.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 17849 | +0.104 | -353.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 7095 | +0.107 | -41.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 7095 | +0.107 | -41.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 9332 | +0.081 | -747.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 9332 | +0.081 | -747.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 836 | +0.217 | -101.70€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 836 | +0.217 | -101.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 836 | +0.217 | -101.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 836 | +0.217 | -101.70€ | 2 | 4 |
| ✅ GBM_LATE_15M | 26665 | +0.083 | +12756.98€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 26665 | +0.083 | +12756.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4452 | +0.195 | +3266.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4452 | +0.195 | +3266.00€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 3967 | +0.178 | +2801.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3967 | +0.178 | +2801.37€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 4673 | +0.197 | +3461.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4673 | +0.197 | +3461.55€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 3875 | +0.023 | +859.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3875 | +0.023 | +859.04€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3812 | -0.033 | +867.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3812 | -0.033 | +867.95€ | 4 | 12 |
| ✅ GBM_LATE_15M#XRP | 5886 | -0.040 | +1501.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5886 | -0.040 | +1501.07€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 28270 | +0.086 | +14777.21€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 28270 | +0.086 | +14777.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5369 | +0.015 | +2806.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5369 | +0.015 | +2806.48€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5906 | +0.016 | +1241.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5906 | +0.016 | +1241.00€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4018 | +0.263 | +4052.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4018 | +0.263 | +4052.62€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4617 | +0.004 | +887.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4617 | +0.004 | +887.24€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4569 | +0.028 | +1732.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4569 | +0.028 | +1732.04€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3791 | +0.277 | +4057.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3791 | +0.277 | +4057.82€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 21428 | +0.168 | +16055.25€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 21428 | +0.168 | +16055.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3230 | +0.207 | +2575.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3230 | +0.207 | +2575.85€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3381 | +0.150 | +2486.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3381 | +0.150 | +2486.06€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3378 | +0.208 | +2684.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3378 | +0.208 | +2684.16€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3586 | +0.133 | +2499.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3586 | +0.133 | +2499.62€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4000 | +0.116 | +2765.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4000 | +0.116 | +2765.05€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3853 | +0.204 | +3044.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3853 | +0.204 | +3044.51€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 5427 | +0.131 | +2360.92€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 5427 | +0.131 | +2360.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 211 | +0.110 | +81.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 211 | +0.110 | +81.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1517 | +0.125 | +706.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1517 | +0.125 | +706.97€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 373 | +0.143 | +176.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 373 | +0.143 | +176.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1626 | +0.149 | +760.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1626 | +0.149 | +760.79€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1194 | +0.110 | +419.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1194 | +0.110 | +419.71€ | 1 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 26798 | +0.176 | +20083.66€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 26798 | +0.176 | +20083.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4243 | +0.221 | +3592.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4243 | +0.221 | +3592.91€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4200 | +0.152 | +2805.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4200 | +0.152 | +2805.13€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4425 | +0.224 | +3792.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4425 | +0.224 | +3792.40€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4336 | +0.136 | +2973.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4336 | +0.136 | +2973.63€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4687 | +0.114 | +3027.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4687 | +0.114 | +3027.25€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4907 | +0.207 | +3892.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4907 | +0.207 | +3892.34€ | 0 | 24 |
| ✅ GBM_LATE_5M | 7323 | +0.154 | +4368.66€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 7323 | +0.154 | +4368.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1813 | +0.149 | +1210.79€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1813 | +0.149 | +1210.79€ | 0 | 30 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2516 | +0.164 | +1557.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2516 | +0.164 | +1557.21€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 674 | +0.124 | +292.69€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 674 | +0.124 | +292.69€ | 0 | 23 |
| ✅ GBM_LATE_5M#XRP | 837 | +0.116 | +326.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 837 | +0.116 | +326.92€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1822 | +0.067 | +731.57€ | 2 | 14 |
| ✅ GBM_LATE_60M#60min | 1822 | +0.067 | +731.57€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 663 | +0.088 | +259.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 663 | +0.088 | +259.03€ | 0 | 11 |
| ✅ GBM_LATE_60M#ETH | 603 | +0.070 | +293.93€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 603 | +0.070 | +293.93€ | 2 | 14 |
| ✅ GBM_LATE_60M#SOL | 556 | +0.038 | +178.61€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 556 | +0.038 | +178.61€ | 2 | 10 |
| 🚫 GBM_LATE_60M_FADE | 388 | -0.251 | -17.38€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 388 | -0.251 | -17.38€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 148 | -0.220 | -6.61€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 148 | -0.220 | -6.61€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 127 | -0.252 | -5.45€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 127 | -0.252 | -5.45€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 113 | -0.283 | -5.32€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 113 | -0.283 | -5.32€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 728 | +0.073 | +156.56€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 728 | +0.073 | +156.56€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 284 | +0.063 | +51.09€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 284 | +0.063 | +51.09€ | 2 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 218 | +0.036 | +11.90€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 218 | +0.036 | +11.90€ | 2 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 226 | +0.118 | +93.56€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 226 | +0.118 | +93.56€ | 2 | 12 |
| ✅ LATE_WINDOW_5MIN | 102 | +0.260 | +85.53€ | 0 | 10 |
| ✅ LATE_WINDOW_5MIN#5min | 102 | +0.260 | +85.53€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 102 | +0.260 | +85.53€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 102 | +0.260 | +85.53€ | 0 | 10 |
| ✅ LEADLAG_BTC_XRP_15M | 2071 | +0.105 | +578.30€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2071 | +0.105 | +578.30€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2071 | +0.105 | +578.30€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2071 | +0.105 | +578.30€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 384 | -0.080 | -34.80€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 384 | -0.080 | -34.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 96 | -0.061 | -5.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 96 | -0.061 | -5.23€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 140 | -0.028 | -5.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 140 | -0.028 | -5.25€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 2086 | +0.009 | +21.29€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2086 | +0.009 | +21.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 106 | +0.028 | +0.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 106 | +0.028 | +0.43€ | 0 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 234 | -0.013 | +6.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 234 | -0.013 | +6.91€ | 5 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 168 | -0.024 | -5.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 168 | -0.024 | -5.38€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 871 | +0.026 | +23.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 871 | +0.026 | +23.75€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 475 | +0.001 | -4.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 475 | +0.001 | -4.40€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 232 | +0.000 | -0.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 232 | +0.000 | -0.03€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M | 1114 | -0.043 | -26.36€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1114 | -0.043 | -26.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 317 | -0.042 | -13.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 317 | -0.042 | -13.22€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 375 | -0.028 | -1.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 375 | -0.028 | -1.52€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 422 | -0.057 | -11.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 422 | -0.057 | -11.62€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 1711 | -0.020 | +29.70€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 816 | -0.022 | +2.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 895 | -0.018 | +27.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 42 | +0.023 | +6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 25 | +0.018 | +2.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 17 | +0.022 | +3.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 420 | +0.033 | +53.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 195 | +0.023 | +14.59€ | 0 | 4 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 225 | +0.042 | +38.48€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 232 | -0.051 | -7.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 112 | -0.070 | -9.52€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 120 | -0.033 | +1.86€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 318 | -0.059 | -26.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 143 | -0.059 | -10.89€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 175 | -0.059 | -15.31€ | 5 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 295 | -0.005 | +15.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 150 | +0.007 | +10.86€ | 2 | 7 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 145 | -0.017 | +4.42€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 404 | -0.042 | -10.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 191 | -0.039 | -5.49€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 213 | -0.044 | -5.42€ | 3 | 3 |
| ✅ MOMENTUM_IBS_15M | 14530 | -0.012 | -209.46€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14530 | -0.012 | -209.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3247 | -0.020 | -62.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3247 | -0.020 | -62.64€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 30324 | -0.006 | +1360.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 30324 | -0.006 | +1360.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5353 | +0.018 | +652.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5353 | +0.018 | +652.82€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4665 | -0.027 | -42.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4665 | -0.027 | -42.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5412 | +0.014 | +470.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5412 | +0.014 | +470.43€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4444 | -0.051 | -134.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4444 | -0.051 | -134.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5088 | -0.010 | +199.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5088 | -0.010 | +199.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5362 | +0.008 | +215.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5362 | +0.008 | +215.17€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5948 | -0.059 | -140.57€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5948 | -0.059 | -140.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1438 | -0.083 | -38.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1438 | -0.083 | -38.02€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 665 | -0.118 | -24.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 665 | -0.118 | -24.90€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1735 | -0.078 | -32.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1735 | -0.078 | -32.71€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 850 | -0.015 | -25.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 850 | -0.015 | -25.14€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 76715 | -0.073 | +1720.58€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 76715 | -0.073 | +1720.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 12997 | -0.078 | +750.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 12997 | -0.078 | +750.86€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 11800 | -0.094 | -558.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 11800 | -0.094 | -558.24€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 13240 | -0.067 | +717.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 13240 | -0.067 | +717.99€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 11327 | -0.094 | -207.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 11327 | -0.094 | -207.45€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 14033 | -0.048 | +399.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 14033 | -0.048 | +399.52€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 13318 | -0.062 | +617.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 13318 | -0.062 | +617.91€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7683 | -0.025 | -122.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7683 | -0.025 | -122.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1722 | -0.031 | -8.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1722 | -0.031 | -8.17€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2169 | -0.019 | -21.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2169 | -0.019 | -21.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1049 | -0.043 | -18.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1049 | -0.043 | -18.25€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 744 | -0.020 | -23.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 744 | -0.020 | -23.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1169 | +0.105 | +380.47€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 1033 | +0.111 | +367.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 236 | +0.135 | +114.78€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 236 | +0.135 | +114.78€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 196 | +0.091 | +43.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 196 | +0.091 | +43.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 214 | +0.097 | +72.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 214 | +0.097 | +72.29€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 181 | +0.128 | +80.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 181 | +0.128 | +80.60€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 206 | +0.096 | +56.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 206 | +0.096 | +56.35€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 550 | -0.056 | -60.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 550 | -0.056 | -60.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 115 | -0.013 | +0.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 115 | -0.013 | +0.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 67 | -0.152 | -22.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 67 | -0.152 | -22.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 163 | -0.058 | -23.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 163 | -0.058 | -23.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 115 | -0.013 | -1.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 115 | -0.013 | -1.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 90 | -0.087 | -14.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 90 | -0.087 | -14.24€ | 0 | 0 |
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
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 223 | -0.224 | -27.46€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 183 | -0.181 | +19.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 167 | -0.180 | +14.86€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 662 | -0.203 | -40.85€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 309 | +0.407 | +225.92€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 32 | +0.088 | -2.58€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 32 | +0.088 | -2.58€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 81 | +0.380 | +59.35€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 81 | +0.380 | +59.35€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 196 | +0.465 | +169.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 196 | +0.465 | +169.15€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 309 | +0.407 | +225.92€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 531 | +0.035 | +17.83€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 531 | +0.035 | +17.83€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 253 | +0.037 | +6.82€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 253 | +0.037 | +6.82€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 36 | +0.079 | +2.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 36 | +0.079 | +2.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 56 | +0.000 | -1.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 56 | +0.000 | -1.02€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 186 | +0.032 | +9.95€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 186 | +0.032 | +9.95€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 2816 | -0.023 | -116.51€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2816 | -0.023 | -116.51€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 814 | -0.018 | -26.88€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 814 | -0.018 | -26.88€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 570 | -0.023 | -23.26€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 570 | -0.023 | -23.26€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1277 | -0.022 | -51.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1277 | -0.022 | -51.44€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 75 | -0.058 | -7.51€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 75 | -0.058 | -7.51€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 37 | -0.013 | -3.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 37 | -0.013 | -3.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 8063 | +0.025 | +133.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8063 | +0.025 | +133.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2176 | +0.023 | +26.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2176 | +0.023 | +26.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1832 | +0.035 | +55.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1832 | +0.035 | +55.53€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2468 | +0.016 | +14.56€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2468 | +0.016 | +14.56€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1587 | +0.028 | +37.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1587 | +0.028 | +37.35€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7557 | +0.014 | -30.11€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7557 | +0.014 | -30.11€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3034 | +0.018 | -3.82€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3034 | +0.018 | -3.82€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2957 | +0.014 | -13.36€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2957 | +0.014 | -13.36€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1566 | +0.007 | -12.94€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1566 | +0.007 | -12.94€ | 2 | 0 |
| ✅ UPDOWN_GBM | 40185 | +0.032 | +2485.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 10732 | +0.070 | +1999.89€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1454 | +0.005 | +7.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 25417 | +0.022 | +463.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2429 | +0.001 | +15.90€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4180 | +0.070 | +477.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 756 | +0.154 | +309.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3391 | +0.052 | +169.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 7474 | +0.037 | +522.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1351 | +0.085 | +303.23€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 390 | +0.018 | +7.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 4581 | +0.035 | +188.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1093 | +0.001 | +22.21€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 59 | -0.090 | +1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4752 | +0.042 | +306.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 710 | +0.140 | +253.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4014 | +0.025 | +54.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 8570 | +0.020 | +335.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2718 | +0.049 | +308.37€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 381 | +0.006 | +7.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 4603 | +0.009 | +25.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 818 | -0.002 | -8.51€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 50 | -0.135 | +3.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 9339 | +0.015 | +229.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2578 | +0.026 | +175.91€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 373 | -0.004 | -1.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5828 | +0.013 | +57.41€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 518 | +0.006 | +2.19€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 42 | -0.182 | -3.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 5868 | +0.037 | +614.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2619 | +0.085 | +649.52€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 249 | -0.002 | -3.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3000 | -0.001 | -31.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 151 | -0.134 | +0.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 569 | +0.344 | +176.69€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 569 | +0.344 | +176.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 314 | +0.348 | +94.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 314 | +0.348 | +94.03€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 255 | +0.337 | +82.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 255 | +0.337 | +82.67€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 12565 | -0.037 | +2720.89€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 12565 | -0.037 | +2720.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 856 | -0.045 | +360.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 856 | -0.045 | +360.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2284 | -0.121 | +20.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2284 | -0.121 | +20.16€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 450 | +0.181 | +303.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 450 | +0.181 | +303.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1393 | +0.209 | +847.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1393 | +0.209 | +847.09€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3773 | -0.065 | +566.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3773 | -0.065 | +566.47€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3809 | -0.074 | +623.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3809 | -0.074 | +623.07€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 146 | +0.041 | +9.21€ | 2 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 146 | +0.041 | +9.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 146 | +0.041 | +9.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 146 | +0.041 | +9.21€ | 2 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 917 | +0.292 | +734.95€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 917 | +0.292 | +734.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 503 | +0.286 | +380.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 503 | +0.286 | +380.67€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 414 | +0.298 | +354.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 414 | +0.298 | +354.28€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 732 | -0.113 | -84.31€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 732 | -0.113 | -84.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 213 | -0.086 | -16.82€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 213 | -0.086 | -16.82€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 70 | -0.194 | -8.11€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 70 | -0.194 | -8.11€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2483 | +0.301 | +1240.78€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 859 | +0.250 | +121.37€ | 0 | 5 |
| ✅ WEEKLY_PRICE#ETH | 937 | +0.290 | +403.74€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 687 | +0.377 | +715.68€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.017 n=507 — no justifica filtro, seguir monitorizando
  - _Datos_: n=507 IC=+0.017 PNL=+20.68€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 546 celda(s) pasan gate riguroso completo de 2274 evaluadas (n>=40) y 3247 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.027 < 0.08 — monitorear
  - _Datos_: n=2576 IC=+0.027 PNL=+176.93€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.118 n=357/60 | contraria IC=+0.160 n=333 | gap=-0.041 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=306, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=817/40 IC=-0.002 PNL=-8.00€ | BTC#60min: n=1092/40 IC=+0.002 PNL=+22.72€ | SOL#60min: n=518/40 IC=+0.006 PNL=+2.19€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.050 n=350689 | tras_1loss IC=+0.080 n=272092 | tras_2loss IC=+0.050 n=114250/40 | gap=+0.000 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.244 > 0.08 con n=41 PNL=+31.47€
  - _Datos_: n=41 IC=+0.244 PNL=+31.47€

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
  - _Estado_: n=293 IC=+0.073 PNL=+34.01€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=293 IC=+0.073 PNL=+34.01€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=54 IC=+0.179 PNL=+34.09€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=54 IC=+0.179 PNL=+34.09€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: n=1701 IC=+0.008 PNL=+3.87€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1701 IC=+0.008 PNL=+3.87€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=726 IC=-0.014 PNL=+13.05€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=726 IC=-0.014 PNL=+13.05€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=507 IC=+0.017 PNL=+20.68€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=507 IC=+0.017 PNL=+20.68€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.186 > 0.1 con n=2285 PNL=+1443.14€
  - _Datos_: n=2285 IC=+0.186 PNL=+1443.14€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1351 IC=+0.085 PNL=+303.23€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1351 IC=+0.085 PNL=+303.23€

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
  - _Estado_: n=570 IC=+0.025 PNL=+44.71€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=570 IC=+0.025 PNL=+44.71€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=56 IC=+0.052 PNL=+3.51€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=56 IC=+0.052 PNL=+3.51€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.260 n=102) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=102 IC=+0.260 PNL=+85.53€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.114 > 0.02 con n=659 PNL=+235.18€
  - _Datos_: n=659 IC=+0.114 PNL=+235.18€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=147 IC=-0.044 PNL=+35.89€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=147 IC=-0.044 PNL=+35.89€

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
  - _Estado_: n=14249 IC=+0.054 PNL=+1716.24€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=14249 IC=+0.054 PNL=+1716.24€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.144 < -0.1 con n=245 PNL=+26.71€
  - _Datos_: n=245 IC=-0.144 PNL=+26.71€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2016 IC=+0.052 PNL=+219.72€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2016 IC=+0.052 PNL=+219.72€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.1 con n=438 PNL=+129.86€
  - _Datos_: n=438 IC=+0.127 PNL=+129.86€

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
  - _Estado_: n=18862 IC=-0.138 PNL=+1166.00€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=18862 IC=-0.138 PNL=+1166.00€

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
  - _Estado_: n=2021 IC=+0.140 PNL=+1133.93€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2021 IC=+0.140 PNL=+1133.93€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=4247 IC=+0.022 PNL=+148.54€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4247 IC=+0.022 PNL=+148.54€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.085 > 0.08 con n=2169 PNL=+1134.93€
  - _Datos_: n=2169 IC=+0.085 PNL=+1134.93€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.238 < -0.1 con n=1846 PNL=-212.41€
  - _Datos_: n=1846 IC=-0.238 PNL=-212.41€

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

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 37/40 ops en el filtro definido (IC actual=-0.013 PNL=+3.98€)
  - _Datos_: n=37 IC=-0.013 PNL=+3.98€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1056) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1056 IC=+0.102 PNL=+256.82€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: n=9141 IC=+0.177 PNL=-1050.20€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=9141 IC=+0.177 PNL=-1050.20€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.202 > 0.1 con n=139 PNL=+83.53€
  - _Datos_: n=139 IC=+0.202 PNL=+83.53€
