# Hipótesis automáticas — 2026-09-28 00:02 UTC
_Generado por shadow_postmortem.py sobre 642646 resoluciones (PNL=+74500.46€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=522)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.236 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.210 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.8033` → IC=+0.254 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8033 (IC base=+0.139)

- **PATRÓN** `banda_z` > `4.143` → IC=+0.166 (n=558)

  - _Acción_: Kelly boost +0.83€ cuando `banda_z` > 4.143 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.156 (n=390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 11.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=597)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4881.4177` → IC=+0.160 (n=186)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4881.4177 (IC base=+0.139)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=522)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=387)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.238 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.148)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.209 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.148)

- **PATRÓN** `banda_hit_calibrado` > `0.7988` → IC=+0.264 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7988 (IC base=+0.148)

- **PATRÓN** `banda_z` > `4.341` → IC=+0.171 (n=448)

  - _Acción_: Kelly boost +0.86€ cuando `banda_z` > 4.341 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.168 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=508)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `8596.0083` → IC=+0.122 (n=220)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 8596.0083 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 94.0 (IC base=+0.058)

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
- **FILTRO** `restante_s_al_confirmar` < `146.13` → IC=-0.217 (n=7426)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.13
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=22281)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `138.32` → IC=-0.246 (n=967)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.32
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=2903)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.51` → IC=-0.309 (n=877)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.51
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2631)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.68` → IC=-0.202 (n=1815)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.68
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=5446)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.34` → IC=-0.336 (n=1458)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.34
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=4377)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.207 (n=14559)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3637)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5625.8819` → IC=+0.177 (n=2327)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 5625.8819 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=12303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=14797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.231 (n=11556)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=5895)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7826.0587` → IC=+0.174 (n=2238)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7826.0587 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1753)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=2213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `15920.3308` → IC=+0.236 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15920.3308 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.203 (n=1589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.206 (n=1763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.262 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=2257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `15860.4955` → IC=+0.213 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15860.4955 (IC base=+0.200)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.176 (n=338)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.62 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `4566.8958` → IC=+0.145 (n=240)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4566.8958 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.101)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.144 (n=854)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5754.4405` → IC=+0.167 (n=226)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5754.4405 (IC base=+0.101)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=2980)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.347 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.365 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.235 (n=1556)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.232)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=631)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.251 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=573)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `1311.0387` → IC=+0.148 (n=699)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1311.0387 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.404 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.158 (n=574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.165 (n=609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 7.0 (IC base=+0.156)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=750)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.156)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.369 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=191)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `1244.5613` → IC=+0.152 (n=231)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1244.5613 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.208 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.117)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.204 (n=11681)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=11723)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.228 (n=4014)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `5111.8837` → IC=+0.335 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5111.8837 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=2801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.172 (n=2803)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.176 (n=2811)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.250 (n=1009)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.252 (n=1044)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.244)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.343 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.244)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=2761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=2769)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=2362)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.251 (n=2567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.326 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.307 (n=55)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.195 (n=2710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.198 (n=2108)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.193)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.435 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `11138.7656` → IC=+0.457 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11138.7656 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.441 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.444 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `14120.495` → IC=+0.446 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14120.495 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.444 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `3322.2122` → IC=+0.444 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3322.2122 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.412 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.411 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.424 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.410 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.409)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=36734)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.236 (n=16292)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.179 (n=6334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=5044)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=6860)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=6602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=6543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.263 (n=3748)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.179 (n=6301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=6662)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=3327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=2469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=2273)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=6089)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.257 (n=2442)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.197 (n=6137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2290)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=5564)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.125 (n=5182)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.17 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=5188)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.128 (n=7657)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 8.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.65` → IC=+0.139 (n=5150)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.65 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=2803)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.12` → IC=+0.126 (n=2557)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.12 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.140 (n=2846)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.137 (n=2940)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 6.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.31` → IC=+0.143 (n=2569)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.31 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=2761)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.127 (n=2606)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.2 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.133 (n=2880)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.26` → IC=+0.138 (n=2608)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.26 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=834)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `4103.5959` → IC=+0.306 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4103.5959 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.288 (n=549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.332 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `4254.7258` → IC=+0.297 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4254.7258 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.324 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=585)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1436.9616` → IC=+0.305 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1436.9616 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.350 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.344)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.362 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.344)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.385 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.344)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.344)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.372 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.344)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.438 (n=516)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.435 (n=459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.435 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.437 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.437 (n=252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.454 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.444 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.437 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `1978.5089` → IC=+0.464 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.5089 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.394)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.406 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.394)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.394)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=56)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=56)

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
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=56)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=56)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4845` → IC=+0.126 (n=8675)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.4845 (IC base=+0.109)

- **PATRÓN** `ibs_20min` > `0.9834` → IC=+0.243 (n=2891)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9834 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` < `0.2184` → IC=+0.258 (n=1904)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2184 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.343` → IC=+0.189 (n=2298)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 8.343 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.252 (n=2381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2089 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` > `0.6146` → IC=+0.255 (n=2381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6146 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.227 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `1.9016` → IC=+0.213 (n=3996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9016 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.5708` → IC=+0.134 (n=10482)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5708 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.6012` → IC=+0.205 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6012 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` < `0.6976` → IC=+0.188 (n=1637)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6976 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `0.8683` → IC=+0.177 (n=2481)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8683 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.1674` → IC=+0.227 (n=1783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1674 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.5708` → IC=+0.201 (n=5632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5708 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `129.0` → IC=+0.214 (n=6100)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 129.0 (IC base=+0.067)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.196 (n=649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0049 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.174 (n=648)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0081 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3472` → IC=+0.173 (n=1944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3472 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.178 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.173 (n=1303)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.138` → IC=+0.269 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.138 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.211 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.44` → IC=+0.170 (n=1825)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.44 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.181 (n=1979)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.247 (n=1344)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.275 (n=499)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.249 (n=1033)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.290 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.526` → IC=+0.244 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.526 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.468` → IC=+0.245 (n=1565)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.468 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.0922` → IC=+0.233 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0922 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.269 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.4333` → IC=+0.233 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4333 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.6131` → IC=+0.248 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6131 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=1648)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1821.6` → IC=+0.239 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1821.6 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.239 (n=664)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.243 (n=663)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.237 (n=1509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=1527)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.9864` → IC=+0.268 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9864 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.3452` → IC=+0.225 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3452 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.507` → IC=+0.266 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.507 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2572` → IC=+0.223 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2572 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.0844` → IC=+0.231 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0844 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.251 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.3849` → IC=+0.237 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3849 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `11109.7462` → IC=+0.224 (n=1506)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11109.7462 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.179 (n=521)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0026 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0745` → IC=+0.167 (n=517)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0745 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.146 (n=687)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.7079` → IC=+0.170 (n=1550)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7079 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1271` → IC=+0.154 (n=1387)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1271 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.294` → IC=+0.153 (n=246)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.294 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.327` → IC=+0.144 (n=1419)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.327 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.151 (n=1550)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2044 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.8532` → IC=+0.141 (n=1033)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8532 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1567` → IC=+0.175 (n=411)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1567 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4386` → IC=+0.153 (n=1440)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4386 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.7721` → IC=+0.145 (n=960)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7721 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `14067.2635` → IC=+0.146 (n=1033)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 14067.2635 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.167 (n=599)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 233.0 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.214 (n=648)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=2043)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=1733)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.269` → IC=+0.257 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.269 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.190 (n=1689)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.3557` → IC=+0.202 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3557 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.7731` → IC=+0.197 (n=1653)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.7731 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=2308)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.223 (n=1481)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6119` → IC=+0.214 (n=1679)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6119 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=775)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.241 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.707` → IC=+0.234 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.707 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.512` → IC=+0.212 (n=1825)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.512 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3506` → IC=+0.263 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3506 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7572` → IC=+0.208 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7572 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.1788` → IC=+0.217 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1788 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1983.3` → IC=+0.213 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1983.3 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.214 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.212)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=105)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=2353)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.146 (n=379)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0037 (IC base=+0.032)

- **PATRÓN** `ibs_20min` > `0.9479` → IC=+0.216 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9479 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `0.3545` → IC=+0.328 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3545 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.1931` → IC=+0.331 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1931 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.805` → IC=+0.169 (n=765)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 4.805 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.335 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `1.211` → IC=+0.329 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.211 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.357 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `2.21` → IC=+0.332 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.21 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.335 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.1049` → IC=+0.151 (n=615)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1049 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.6641` → IC=+0.213 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6641 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` < `0.8511` → IC=+0.157 (n=613)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8511 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `1.1615` → IC=+0.144 (n=307)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1615 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.219 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.5277` → IC=+0.169 (n=774)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.5277 (IC base=+0.019)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.182 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=355)

- **FILTRO** `ibs_20min` < `0.2909` → IC=-0.207 (n=104)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2909
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=315)

- **FILTRO** `ibs_20min` > `0.25` → IC=-0.126 (n=2337)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=1173)

- **FILTRO** `sigma_ewma_delta_pct` > `8.719` → IC=-0.214 (n=372)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.719
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=3138)

- **PATRÓN** `ibs_20min` > `0.7834` → IC=+0.224 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7834 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `1.8814` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.8814 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` < `0.5572` → IC=+0.274 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5572 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.253` → IC=+0.121 (n=151)

  - _Acción_: Kelly boost +0.60€ cuando `sigma_ewma_delta_pct` > 2.253 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `1.0815` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0815 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.7465` → IC=+0.286 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7465 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.289 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.124 (n=1173)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.25 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7235` → IC=+0.265 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7235 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.4545` → IC=+0.230 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4545 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `0.6728` → IC=+0.273 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6728 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.159` → IC=+0.284 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.159 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.280 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6536` → IC=-0.183 (n=610)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6536
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1841)

- **FILTRO** `ibs_20min` < `0.7197` → IC=-0.155 (n=1617)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7197
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=834)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.200 (n=494)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1957)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.207 (n=897)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=2718)

- **PATRÓN** `dist_vwap_pct` > `0.4581` → IC=+0.314 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4581 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2041` → IC=+0.315 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2041 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.308 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6226 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.298 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.4256` → IC=+0.298 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4256 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.8015` → IC=+0.296 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8015 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.5572` → IC=+0.273 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5572 (IC base=-0.021)

- **PATRÓN** `volumen_regimen` < `0.7331` → IC=+0.260 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7331 (IC base=-0.021)

- **PATRÓN** `volumen_regimen` > `1.2485` → IC=+0.284 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2485 (IC base=-0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.276 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.141` → IC=+0.266 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.141 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.5237` → IC=+0.251 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5237 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.199 (n=3681)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0097 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.475` → IC=+0.186 (n=9859)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.475 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `1.0343` → IC=+0.290 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0343 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.63` → IC=+0.158 (n=5131)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.63 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6901` → IC=+0.253 (n=3528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6901 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.271 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4651` → IC=+0.240 (n=2137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4651 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6654` → IC=+0.249 (n=2136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6654 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.272 (n=5930)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.160 (n=3624)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0091 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.5509` → IC=+0.153 (n=9557)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.5509 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.707` → IC=+0.243 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.707 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2458` → IC=+0.245 (n=3072)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2458 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `0.6345` → IC=+0.245 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6345 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.2049` → IC=+0.250 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2049 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2416` → IC=+0.308 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2416 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.6004` → IC=+0.265 (n=1903)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6004 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `2.2956` → IC=+0.263 (n=1961)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2956 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.272 (n=4200)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 83.0 (IC base=+0.073)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2567` → IC=-0.150 (n=761)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2567
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=2286)

- **FILTRO** `sigma_ewma_delta_pct` > `4.528` → IC=-0.164 (n=579)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.528
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1927)

- **PATRÓN** `ibs_20min` > `0.8961` → IC=+0.271 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8961 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.846` → IC=+0.204 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.846 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2224` → IC=+0.268 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2224 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.183 (n=326)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.185` → IC=+0.212 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.185 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.205 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.2144` → IC=+0.469 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2144 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4082` → IC=+0.457 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4082 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.167` → IC=+0.455 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.167 (IC base=-0.024)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=-0.024)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8671` → IC=+0.165 (n=739)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8671 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.2975` → IC=+0.174 (n=397)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.2975 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.6754` → IC=+0.179 (n=913)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6754 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.248 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4262` → IC=+0.191 (n=334)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4262 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.4088` → IC=+0.181 (n=334)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.4088 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `238.0` → IC=+0.202 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 238.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1497` → IC=+0.221 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1497 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `0.8577` → IC=+0.231 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8577 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2683` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2683 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.4389` → IC=+0.222 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4389 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1651` → IC=+0.235 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1651 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `460.0` → IC=+0.221 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 460.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.290 (n=574)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.253 (n=1724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.249 (n=1730)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.749` → IC=+0.284 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.749 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.262 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.101 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `3.3253` → IC=+0.269 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3253 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2025)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `1914.9184` → IC=+0.258 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.9184 (IC base=+0.249)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.315 (n=634)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.6123` → IC=+0.287 (n=1396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6123 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.326 (n=476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` < `0.3459` → IC=+0.293 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3459 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.299 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.3385` → IC=+0.301 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3385 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` < `1.739` → IC=+0.289 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.739 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.6939` → IC=+0.292 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6939 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `1908.1032` → IC=+0.302 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1908.1032 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.282 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.284)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.3034` → IC=-0.162 (n=551)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3034
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1654)

- **FILTRO** `ibs_20min` > `0.7735` → IC=-0.182 (n=649)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7735
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=1948)

- **PATRÓN** `ibs_20min` > `0.912` → IC=+0.177 (n=552)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.912 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` < `0.1817` → IC=+0.226 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1817 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` < `0.9991` → IC=+0.243 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9991 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` > `0.5875` → IC=+0.220 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5875 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.262 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.5082` → IC=+0.263 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5082 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.275 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 70.0 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` > `0.1468` → IC=+0.217 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1468 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` < `0.6392` → IC=+0.239 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6392 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.8148` → IC=+0.256 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8148 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.1392` → IC=+0.247 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1392 (IC base=-0.006)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.258 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 137.0 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.74` → IC=-0.193 (n=1170)

  - _Acción_: SKIP cuando `ibs_20min` < 0.74
  - _Potencial_: sin este filtro IC_bueno=+0.279 (n=1171)

- **FILTRO** `ibs_20min` > `0.6842` → IC=-0.234 (n=592)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6842
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=1781)

- **FILTRO** `sigma_ewma_delta_pct` > `4.748` → IC=-0.189 (n=519)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.748
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=1854)

- **PATRÓN** `ibs_20min` > `0.74` → IC=+0.279 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.74 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `0.8494` → IC=+0.327 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8494 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.658` → IC=+0.171 (n=369)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.658 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.305 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8646 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `0.6422` → IC=+0.297 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6422 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1022` → IC=+0.296 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1022 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2714` → IC=+0.305 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2714 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4355` → IC=+0.325 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4355 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.319 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.582` → IC=+0.124 (n=1567)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.582 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` < `0.2196` → IC=+0.227 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2196 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` < `0.6964` → IC=+0.257 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6964 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` < `0.0971` → IC=+0.219 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0971 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.223 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` < `2.4641` → IC=+0.233 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4641 (IC base=+0.016)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.241 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.016)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0167` → IC=+0.316 (n=937)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0167 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.295 (n=658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` > `0.7395` → IC=+0.323 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7395 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.314 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.675` → IC=+0.303 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.675 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `0.8619` → IC=+0.307 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8619 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.329 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.288 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.283 (n=1468)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2468.9246` → IC=+0.289 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2468.9246 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.320 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0155` → IC=+0.307 (n=1002)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0155 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.1979` → IC=+0.280 (n=661)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1979 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.289 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.281 (n=743)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.29` → IC=+0.317 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.29 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.3138` → IC=+0.284 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3138 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.279 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2288 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.471` → IC=+0.294 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.471 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` < `0.6412` → IC=+0.283 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6412 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` > `1.2464` → IC=+0.307 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2464 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.2357` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2357 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.4234` → IC=+0.286 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4234 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.1452` → IC=+0.275 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1452 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `2613.3526` → IC=+0.279 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2613.3526 (IC base=+0.278)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.177 (n=2813)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0048 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.203 (n=2814)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.357` → IC=+0.178 (n=7420)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.357 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=8828)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.5738` → IC=+0.220 (n=8430)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5738 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.1749` → IC=+0.193 (n=3651)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1749 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.354` → IC=+0.256 (n=1721)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.354 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.2087` → IC=+0.162 (n=5590)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2087 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.6283` → IC=+0.161 (n=5589)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6283 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2425` → IC=+0.196 (n=1707)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2425 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.5586` → IC=+0.168 (n=3564)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5586 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.613` → IC=+0.177 (n=2701)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.613 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `1957.2184` → IC=+0.171 (n=7531)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1957.2184 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.183 (n=7340)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 110.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.184 (n=5389)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0066 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.0809` → IC=+0.212 (n=2695)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0809 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.4828` → IC=+0.227 (n=8086)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4828 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` < `0.2332` → IC=+0.161 (n=5850)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2332 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.345` → IC=+0.196 (n=1372)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.345 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.1737` → IC=+0.154 (n=5827)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1737 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2915` → IC=+0.216 (n=1177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2915 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.561` → IC=+0.169 (n=3254)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.561 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6251` → IC=+0.172 (n=2465)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6251 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.177 (n=7045)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 111.0 (IC base=+0.169)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.222 (n=477)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.189 (n=477)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0083 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3396` → IC=+0.212 (n=1429)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3396 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=1509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=956)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.137` → IC=+0.309 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.137 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.238 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.186 (n=1327)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=1456)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.241 (n=936)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.248 (n=951)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.285 (n=709)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=522)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3455` → IC=+0.260 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3455 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.317` → IC=+0.248 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.317 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.236 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.252 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4215` → IC=+0.267 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4215 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.234 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1822.0188` → IC=+0.244 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1822.0188 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.236 (n=419)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0719` → IC=+0.200 (n=418)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0719 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=1261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.4039` → IC=+0.228 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4039 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2016` → IC=+0.211 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2016 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.481` → IC=+0.234 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.481 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.2593` → IC=+0.166 (n=1254)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2593 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.0767` → IC=+0.169 (n=569)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.0767 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.201 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.5076` → IC=+0.178 (n=536)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.5076 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.4674` → IC=+0.167 (n=406)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.4674 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `10596.8161` → IC=+0.170 (n=1254)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10596.8161 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `445.0` → IC=+0.161 (n=1175)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 445.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.198 (n=452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.29` → IC=+0.161 (n=1344)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.29 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5744` → IC=+0.189 (n=1344)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5744 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1321` → IC=+0.162 (n=1336)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1321 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.901` → IC=+0.205 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.901 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.158 (n=1344)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2025 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.155 (n=412)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4507` → IC=+0.147 (n=1232)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4507 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4266` → IC=+0.136 (n=1232)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4266 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.162 (n=386)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 213.0 (IC base=+0.138)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.215 (n=641)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.2371` → IC=+0.218 (n=943)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2371 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1472)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.279 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2027` → IC=+0.204 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2027 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.7994` → IC=+0.198 (n=593)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.7994 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.7756` → IC=+0.214 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7756 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.209 (n=1669)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.232 (n=1193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.0995` → IC=+0.258 (n=398)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0995 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.273 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.247 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.703` → IC=+0.257 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.703 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3546` → IC=+0.256 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3546 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.220 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `3.3667` → IC=+0.240 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3667 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.217 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.219)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.218 (n=449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.4224` → IC=+0.160 (n=1345)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4224 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.3713` → IC=+0.197 (n=1345)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3713 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1492` → IC=+0.177 (n=883)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1492 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.229 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.0335` → IC=+0.149 (n=1185)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0335 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6204` → IC=+0.147 (n=1345)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6204 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.200 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.4294` → IC=+0.158 (n=440)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4294 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.169 (n=439)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `5859.5882` → IC=+0.186 (n=897)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 5859.5882 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.149 (n=1283)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 160.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.156 (n=1420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0071 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3796` → IC=+0.145 (n=1418)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3796 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6485` → IC=+0.172 (n=1418)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6485 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.1535` → IC=+0.141 (n=1393)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1535 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.160 (n=504)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.851` → IC=+0.151 (n=946)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.851 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.184 (n=213)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.8095` → IC=+0.139 (n=864)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8095 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.5251` → IC=+0.124 (n=432)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.5251 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `10077.5355` → IC=+0.162 (n=643)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 10077.5355 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.121 (n=1234)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 157.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.151 (n=700)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.01 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=1578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.5066` → IC=+0.207 (n=1532)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5066 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.836` → IC=+0.208 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.836 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.76` → IC=+0.256 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.76 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.131 (n=1532)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.2036 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.124 (n=1532)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6434 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1636` → IC=+0.126 (n=1538)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1636 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.124 (n=645)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.5413` → IC=+0.138 (n=652)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5413 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1588)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2897.8254` → IC=+0.193 (n=695)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2897.8254 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.134 (n=1190)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 49.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.158 (n=686)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0061 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.171 (n=520)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.213 (n=1558)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.0073` → IC=+0.126 (n=225)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 1.0073 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.2013` → IC=+0.143 (n=1419)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2013 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.13` → IC=+0.139 (n=253)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.13 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.6359` → IC=+0.144 (n=521)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6359 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2754` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2754 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.137 (n=469)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.4248` → IC=+0.133 (n=469)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4248 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2761.3271` → IC=+0.165 (n=706)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2761.3271 (IC base=+0.116)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0187` → IC=+0.216 (n=973)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0187 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.293` → IC=+0.205 (n=974)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.293 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.7386` → IC=+0.260 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7386 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.5174` → IC=+0.215 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5174 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.240 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.207 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2068 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.8551` → IC=+0.224 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8551 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2308` → IC=+0.268 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2308 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.1464` → IC=+0.212 (n=1243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1464 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4035` → IC=+0.211 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4035 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.205 (n=1516)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2819.637` → IC=+0.208 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2819.637 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.227 (n=503)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0174` → IC=+0.213 (n=1007)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0174 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0946` → IC=+0.225 (n=503)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0946 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.0208` → IC=+0.303 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0208 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `1.1962` → IC=+0.227 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1962 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.2068` → IC=+0.207 (n=1517)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2068 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.43` → IC=+0.247 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.43 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.633` → IC=+0.216 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.633 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.289 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.2062` → IC=+0.200 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2062 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4272` → IC=+0.203 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4272 (IC base=+0.207)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=707)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.160)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.175 (n=706)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0086 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.342` → IC=+0.167 (n=1862)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.342 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=1078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.7477` → IC=+0.212 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7477 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.6074` → IC=+0.174 (n=443)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.6074 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` < `0.1487` → IC=+0.164 (n=1533)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1487 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.75` → IC=+0.187 (n=948)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.75 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `0.8708` → IC=+0.182 (n=1255)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.8708 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.167 (n=628)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.2084 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.1655` → IC=+0.185 (n=575)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1655 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.4459` → IC=+0.171 (n=682)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4459 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `1.8284` → IC=+0.168 (n=1364)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.8284 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.166 (n=2394)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `2650.3071` → IC=+0.162 (n=1891)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2650.3071 (IC base=+0.160)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.179 (n=1894)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 150.0 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.138 (n=1439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0056 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.3404` → IC=+0.129 (n=1895)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.3404 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.126 (n=2176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.06` → IC=+0.189 (n=719)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.06 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2074` → IC=+0.121 (n=1928)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2074 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6989` → IC=+0.132 (n=859)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.6989 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.132 (n=536)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4517` → IC=+0.147 (n=693)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4517 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2771.2508` → IC=+0.123 (n=1923)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2771.2508 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.132 (n=667)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 19.0 (IC base=+0.113)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.148 (n=464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0047 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.154 (n=232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.172 (n=498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 8.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.6598` → IC=+0.197 (n=351)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.6598 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.284` → IC=+0.158 (n=188)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.284 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.134 (n=454)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.181` → IC=+0.143 (n=239)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.181 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.17` → IC=+0.133 (n=491)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.17 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.9116` → IC=+0.161 (n=352)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.9116 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.0916` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0916 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.2117` → IC=+0.138 (n=451)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.2117 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.5179` → IC=+0.141 (n=457)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.5179 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `10893.4165` → IC=+0.145 (n=527)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 10893.4165 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.171 (n=171)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 146.0 (IC base=+0.131)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.210 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.3366` → IC=+0.156 (n=666)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3366 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=684)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.185 (n=586)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6112 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.2995` → IC=+0.154 (n=701)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2995 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.494` → IC=+0.153 (n=252)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.494 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.238` → IC=+0.137 (n=604)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.238 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2213` → IC=+0.142 (n=666)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2213 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.7161` → IC=+0.148 (n=595)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7161 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.196 (n=179)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.1142` → IC=+0.160 (n=577)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1142 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4219` → IC=+0.147 (n=656)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4219 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `322.0` → IC=+0.152 (n=558)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 322.0 (IC base=+0.137)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.272 (n=292)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.231 (n=221)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=695)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.9681` → IC=+0.267 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9681 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.1411` → IC=+0.213 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1411 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.2089` → IC=+0.212 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2089 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.02` → IC=+0.239 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.02 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.0081` → IC=+0.211 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0081 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `1.1584` → IC=+0.231 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1584 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.1539` → IC=+0.269 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1539 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.4055` → IC=+0.223 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4055 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.4505` → IC=+0.250 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4505 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `12377.2518` → IC=+0.213 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12377.2518 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.0839` → IC=+0.159 (n=206)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.0839 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6876` → IC=+0.139 (n=272)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6876 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2266` → IC=+0.133 (n=96)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2266 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `9693.0592` → IC=+0.126 (n=412)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 9693.0592 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.171 (n=235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0089 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.5376` → IC=+0.141 (n=516)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5376 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.173 (n=484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 8.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.9284` → IC=+0.207 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9284 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1792` → IC=+0.141 (n=413)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1792 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.556` → IC=+0.196 (n=278)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.556 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.0674` → IC=+0.160 (n=454)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0674 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.7217` → IC=+0.148 (n=461)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7217 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1794` → IC=+0.164 (n=141)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1794 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.4824` → IC=+0.153 (n=165)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4824 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.2151` → IC=+0.174 (n=225)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.2151 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=545)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `3108.4588` → IC=+0.195 (n=172)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3108.4588 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.126 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 16.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.4167` → IC=+0.168 (n=410)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.4167 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.7028` → IC=+0.152 (n=205)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.7028 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.5789` → IC=+0.182 (n=193)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5789 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2620.7147` → IC=+0.141 (n=310)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2620.7147 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.141 (n=410)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 40.0 (IC base=+0.094)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.174 (n=3635)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0047 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.210 (n=3623)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=11378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=3657)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.944` → IC=+0.201 (n=1534)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.944 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.365` → IC=+0.246 (n=2730)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.365 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `0.88` → IC=+0.169 (n=4849)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.88 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.203 (n=1491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.5948` → IC=+0.192 (n=3491)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5948 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `1798.2686` → IC=+0.176 (n=10869)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1798.2686 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.200 (n=8353)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 83.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=6560)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1487` → IC=+0.190 (n=4326)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1487 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=3748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.183 (n=4514)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.569` → IC=+0.237 (n=9832)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.569 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2484` → IC=+0.163 (n=6103)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2484 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.055` → IC=+0.200 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.055 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.732` → IC=+0.184 (n=9502)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.732 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7039` → IC=+0.164 (n=2958)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7039 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.239 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6155` → IC=+0.191 (n=3025)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6155 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.198 (n=5893)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 47.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.218 (n=612)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.209 (n=1225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.3502` → IC=+0.198 (n=1825)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3502 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.211 (n=879)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.201 (n=1231)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.328 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.593` → IC=+0.350 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.593 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.254 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.5623` → IC=+0.201 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5623 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=1843)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.264 (n=971)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.265 (n=1456)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.1244` → IC=+0.283 (n=640)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1244 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=1316)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.3548` → IC=+0.283 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3548 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.475` → IC=+0.263 (n=1532)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.475 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.286 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.4379` → IC=+0.260 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4379 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `2.6294` → IC=+0.277 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6294 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1819.3` → IC=+0.264 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1819.3 (IC base=+0.260)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.206 (n=580)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1124` → IC=+0.164 (n=765)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1124 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.3078` → IC=+0.204 (n=1739)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3078 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.1246` → IC=+0.186 (n=980)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1246 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.709` → IC=+0.172 (n=395)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.709 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.169` → IC=+0.156 (n=1570)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.169 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6267` → IC=+0.181 (n=581)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6267 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2669` → IC=+0.201 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2669 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.1195` → IC=+0.162 (n=1482)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1195 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.7583` → IC=+0.160 (n=1122)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7583 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `11232.5288` → IC=+0.160 (n=1554)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11232.5288 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `472.0` → IC=+0.163 (n=1620)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 472.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.165 (n=1495)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.32` → IC=+0.162 (n=1495)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.32 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.176 (n=498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=667)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.2835` → IC=+0.237 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2835 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.6698` → IC=+0.157 (n=240)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6698 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1309` → IC=+0.165 (n=1356)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1309 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.52` → IC=+0.160 (n=251)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.52 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.315` → IC=+0.153 (n=1358)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.315 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.1894` → IC=+0.165 (n=1495)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1894 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.194 (n=400)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.408` → IC=+0.161 (n=1396)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.408 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.7587` → IC=+0.159 (n=931)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7587 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `418.0` → IC=+0.154 (n=1148)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 418.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.254 (n=591)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=1862)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1793)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.349` → IC=+0.301 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.349 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.2091` → IC=+0.221 (n=1763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2091 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.7701` → IC=+0.230 (n=1514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7701 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1918.9386` → IC=+0.221 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1918.9386 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.240 (n=1654)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1734` → IC=+0.240 (n=729)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1734 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.239 (n=771)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3593` → IC=+0.266 (n=1456)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3593 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.748` → IC=+0.274 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.748 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3428` → IC=+0.301 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3428 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7482` → IC=+0.231 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7482 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.17` → IC=+0.237 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.17 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1910.4284` → IC=+0.242 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.4284 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.233 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.189 (n=815)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4298` → IC=+0.151 (n=1849)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4298 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=1936)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.8747` → IC=+0.263 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8747 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3572` → IC=+0.163 (n=717)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3572 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.171` → IC=+0.165 (n=765)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 4.171 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.158 (n=1233)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8725 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.219 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5208` → IC=+0.157 (n=790)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5208 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1542` → IC=+0.158 (n=813)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1542 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7950.223` → IC=+0.236 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7950.223 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.172 (n=762)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 87.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.151 (n=1506)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0075 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4377` → IC=+0.147 (n=1506)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4377 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=683)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.5844` → IC=+0.198 (n=1325)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5844 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1579` → IC=+0.137 (n=1308)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1579 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.298` → IC=+0.162 (n=226)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.298 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6962` → IC=+0.151 (n=663)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6962 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `1.1993` → IC=+0.137 (n=502)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.1993 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.237 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.146 (n=1433)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `7167.7864` → IC=+0.192 (n=683)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7167.7864 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `173.0` → IC=+0.138 (n=1429)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 173.0 (IC base=+0.133)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.139 (n=1234)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0081 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=1907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4674` → IC=+0.194 (n=1848)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.4674 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.0829` → IC=+0.203 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0829 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.522` → IC=+0.238 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.522 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.8928` → IC=+0.140 (n=1232)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8928 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1622` → IC=+0.120 (n=1894)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_pendiente_norm` < 0.1622 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.848` → IC=+0.121 (n=1199)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.848 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=1858)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2897.5388` → IC=+0.252 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2897.5388 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.135 (n=1440)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 53.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.176 (n=593)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0058 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.1332` → IC=+0.157 (n=593)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1332 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.205 (n=1777)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2216` → IC=+0.134 (n=1443)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.2216 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.463` → IC=+0.125 (n=1712)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.463 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.7128` → IC=+0.154 (n=782)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7128 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.169 (n=279)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4381` → IC=+0.143 (n=538)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4381 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2803.9375` → IC=+0.175 (n=592)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2803.9375 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.125 (n=1408)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 51.0 (IC base=+0.114)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.231 (n=1642)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=1925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.214 (n=1640)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.261 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.2117` → IC=+0.233 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2117 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.275` → IC=+0.271 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.275 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.2484` → IC=+0.215 (n=1838)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2484 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.222 (n=1838)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6398 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.253 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.5001` → IC=+0.236 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5001 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.219 (n=1880)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2820.7088` → IC=+0.220 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2820.7088 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.219 (n=650)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.227 (n=649)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.216 (n=1380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.267 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `1.2224` → IC=+0.210 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2224 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.9142` → IC=+0.208 (n=2175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9142 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.87` → IC=+0.265 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.87 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.2355` → IC=+0.237 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2355 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.271 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.1829` → IC=+0.203 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1829 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.4288` → IC=+0.203 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4288 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=3309)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.200 (n=1096)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.5106` → IC=+0.181 (n=3270)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.5106 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.184 (n=1095)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.172 (n=1092)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 4.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.9477` → IC=+0.234 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9477 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.1811` → IC=+0.182 (n=1221)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1811 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.463` → IC=+0.168 (n=2040)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.463 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.2` → IC=+0.200 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.2 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6263` → IC=+0.170 (n=2178)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6263 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.1706` → IC=+0.203 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1706 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.4562` → IC=+0.178 (n=1077)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4562 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `1.8777` → IC=+0.179 (n=2152)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8777 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=2342)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.206 (n=836)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4847` → IC=+0.170 (n=2494)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.4847 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.170 (n=942)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.1819` → IC=+0.179 (n=1097)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1819 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.6718` → IC=+0.177 (n=478)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6718 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.224` → IC=+0.161 (n=2487)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.224 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.1015` → IC=+0.160 (n=2080)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1015 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.155 (n=2265)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2204` → IC=+0.153 (n=528)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2204 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.5394` → IC=+0.163 (n=1084)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5394 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.8235` → IC=+0.156 (n=1642)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.8235 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3309)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `6248.5078` → IC=+0.158 (n=2228)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 6248.5078 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.154 (n=1615)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 90.0 (IC base=+0.151)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.199 (n=367)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.180 (n=373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0033 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0869` → IC=+0.231 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0869 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.190 (n=185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 8.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5463` → IC=+0.204 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5463 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1436` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1436 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.3655` → IC=+0.187 (n=404)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.3655 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.517` → IC=+0.185 (n=440)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 2.517 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.8402` → IC=+0.210 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8402 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.3007` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3007 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.209 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6311` → IC=+0.209 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6311 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `12563.2849` → IC=+0.222 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12563.2849 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.217 (n=425)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3673` → IC=+0.152 (n=958)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3673 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.174 (n=366)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.180 (n=423)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1409 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.6103` → IC=+0.148 (n=435)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6103 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6922` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6922 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.372` → IC=+0.162 (n=938)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.372 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8795` → IC=+0.185 (n=640)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8795 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0686` → IC=+0.166 (n=447)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0686 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.4209` → IC=+0.145 (n=319)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4209 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.149 (n=637)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `14911.0423` → IC=+0.161 (n=435)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 14911.0423 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `705.0` → IC=+0.145 (n=913)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 705.0 (IC base=+0.139)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.181 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0099 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.574` → IC=+0.174 (n=624)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.574 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.3498` → IC=+0.170 (n=750)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.3498 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `2.8576` → IC=+0.167 (n=548)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.8576 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.8313` → IC=+0.169 (n=556)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.8313 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `2426.4931` → IC=+0.198 (n=283)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2426.4931 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.318 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.250 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` > `0.4634` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4634 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` > `0.1043` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1043 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` < `2.564` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.564 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `4.0788` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 4.0788 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `2362.8582` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2362.8582 (IC base=+0.246)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.246)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.181 (n=929)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0072 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3766` → IC=+0.181 (n=926)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3766 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.182 (n=360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 4.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.5305` → IC=+0.190 (n=702)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5305 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.8827` → IC=+0.183 (n=351)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.8827 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` < `0.2131` → IC=+0.182 (n=873)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2131 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.178` → IC=+0.185 (n=940)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 4.178 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.0845` → IC=+0.176 (n=926)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0845 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6393` → IC=+0.176 (n=1052)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6393 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.192 (n=319)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.4732` → IC=+0.179 (n=1033)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.4732 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.176 (n=923)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=1048)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.202 (n=287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.4837` → IC=+0.184 (n=859)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4837 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.160 (n=604)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 11.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.7466` → IC=+0.160 (n=860)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.7466 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.0954` → IC=+0.164 (n=858)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.0954 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.6041` → IC=+0.172 (n=187)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.6041 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.399` → IC=+0.165 (n=780)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 4.399 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.647` → IC=+0.196 (n=287)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.647 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.7253` → IC=+0.157 (n=767)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7253 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.175 (n=364)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.1996` → IC=+0.170 (n=741)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.1996 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `7506.7691` → IC=+0.172 (n=858)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7506.7691 (IC base=+0.156)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.159 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0111 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.3886` → IC=+0.136 (n=201)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.3886 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.159 (n=297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 3.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.2142` → IC=+0.188 (n=219)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2142 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `1.2717` → IC=+0.134 (n=312)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 1.2717 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.177` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.177 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8864` → IC=+0.170 (n=201)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8864 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.1626` → IC=+0.214 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1626 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.5495` → IC=+0.149 (n=129)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5495 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4285` → IC=+0.152 (n=291)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4285 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.139 (n=353)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `3390.7542` → IC=+0.170 (n=268)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3390.7542 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.152 (n=248)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 55.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.183 (n=257)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0069 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3939` → IC=+0.190 (n=172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3939 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.163 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 16.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.184 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 10.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.1364` → IC=+0.250 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1364 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.5982` → IC=+0.230 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5982 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.639` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.639 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.281` → IC=+0.164 (n=248)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 5.281 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.3617` → IC=+0.164 (n=257)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.3617 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.1103` → IC=+0.220 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1103 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.6109` → IC=+0.170 (n=110)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.6109 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.1932` → IC=+0.172 (n=114)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1932 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `3305.7742` → IC=+0.183 (n=257)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3305.7742 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.200 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.154)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0065` → IC=-0.206 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0065
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=404)

- **FILTRO** `dist_vwap_pct` > `0.1773` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1773
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=369)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.167 (n=446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.084)

- **PATRÓN** `ibs_20min` > `0.6568` → IC=+0.190 (n=823)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.6568 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.1425` → IC=+0.145 (n=496)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1425 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.465` → IC=+0.185 (n=214)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.465 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.183 (n=121)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.084)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.121 (n=270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0045 (IC base=+0.022)

- **PATRÓN** `ibs_20min` < `0.0476` → IC=+0.301 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0476 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.1773` → IC=+0.128 (n=369)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1773 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.187` → IC=+0.130 (n=125)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 3.187 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.1383` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1383 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.5569` → IC=+0.137 (n=268)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5569 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.7169` → IC=+0.139 (n=178)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.7169 (IC base=+0.022)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.147 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0058 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.4702` → IC=+0.184 (n=318)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.4702 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1286` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1286 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `2.4916` → IC=+0.141 (n=279)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.4916 (IC base=+0.097)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.136 (n=152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0043 (IC base=+0.067)

- **PATRÓN** `drift_60min` |x|≤ `0.051` → IC=+0.146 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.051 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.082` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.082 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.0631` → IC=+0.139 (n=156)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.0631 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.585` → IC=+0.154 (n=131)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.585 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` < `0.9523` → IC=+0.132 (n=131)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.9523 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.0636` → IC=+0.173 (n=111)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.0636 (IC base=+0.067)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0059` → IC=-0.214 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0059
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=124)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=129)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.136 (n=229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0049 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.127 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.6598` → IC=+0.219 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6598 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.3316` → IC=+0.178 (n=119)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.3316 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.499` → IC=+0.294 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.499 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.7371` → IC=+0.146 (n=173)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.7371 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `1121.8591` → IC=+0.153 (n=275)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1121.8591 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.1674` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1674 (IC base=+0.000)

- **PATRÓN** `dist_vwap_pct` < `0.1269` → IC=+0.136 (n=105)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1269 (IC base=+0.000)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.258` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.258 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.268` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.268 (IC base=+0.000)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.000)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.265 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=96)

- **FILTRO** `ibs_20min` > `0.2051` → IC=-0.311 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2051
  - _Potencial_: sin este filtro IC_bueno=+0.232 (n=69)

- **PATRÓN** `ibs_20min` > `0.6471` → IC=+0.150 (n=261)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6471 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.497` → IC=+0.123 (n=120)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 5.497 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.057)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.200 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=-0.024)

- **PATRÓN** `ibs_20min` < `0.2051` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2051 (IC base=-0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.93` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.93 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.0903` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0903 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.5975 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.4883` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4883 (IC base=-0.024)

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

- **FILTRO** `sigma_h` > `0.005` → IC=-0.357 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=119)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=158)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=150)

- **FILTRO** `volumen_pendiente_norm` > `0.0895` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0895
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=78)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2175` → IC=-0.269 (n=37)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2175
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=38)

- **FILTRO** `volumen_spike_ratio` > `3.276` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.276
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=35)

- **FILTRO** `sigma_h` < `0.0018` → IC=-0.300 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **FILTRO** `dist_vwap_pct` < `0.0689` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0689
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=30)

- **FILTRO** `volumen_regimen` > `0.9258` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9258
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=56)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6783` → IC=-0.443 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6783
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=34)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.441 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=48)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.367 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=35)

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
- **FILTRO** `ibs_20min` > `0.1681` → IC=-0.134 (n=129)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1681
  - _Potencial_: sin este filtro IC_bueno=+0.177 (n=252)

- **FILTRO** `dist_vwap_pct` > `0.6226` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6226
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=354)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.159 (n=127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0058 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.641` → IC=+0.144 (n=276)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.641 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.4919` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.4919 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.1681` → IC=+0.177 (n=252)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1681 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.105` → IC=+0.155 (n=117)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 6.105 (IC base=+0.072)

- **PATRÓN** `libro_liquidez` > `3751.1947` → IC=+0.174 (n=130)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3751.1947 (IC base=+0.072)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=98)

- **FILTRO** `ibs_20min` < `0.5964` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5964
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=90)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.136 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0043 (IC base=+0.129)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.163 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0033 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.2285` → IC=+0.155 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.2285 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.206 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.146 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.1026` → IC=+0.209 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1026 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1752` → IC=+0.138 (n=150)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1752 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.645` → IC=+0.145 (n=105)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.645 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.1369` → IC=+0.144 (n=130)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1369 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.1907` → IC=+0.190 (n=98)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1907 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.2913` → IC=+0.174 (n=87)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.2913 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `4223.4853` → IC=+0.140 (n=87)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 4223.4853 (IC base=+0.129)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.6191` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6191
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=76)

- **FILTRO** `ibs_20min` > `0.1644` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1644
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=84)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.194 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0022 (IC base=+0.015)

- **PATRÓN** `ibs_20min` > `0.8782` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.8782 (IC base=+0.015)

- **PATRÓN** `libro_liquidez` > `1624.9844` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1624.9844 (IC base=+0.015)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.122 (n=96)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0053 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.1644` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1644 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` < `0.8247` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.8247 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.0753` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.0753 (IC base=+0.062)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=62)

- **FILTRO** `dist_vwap_pct` > `0.1415` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1415
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=57)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.218 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.231 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.212 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.6875` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6875 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.289 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.0812` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0812 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.3996` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3996 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.213 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.209)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3583` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3583 (IC base=+0.217)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.217)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.321 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `1768.0` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1768.0 (IC base=+0.217)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3583` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3583 (IC base=+0.217)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.217)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.321 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `1768.0` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1768.0 (IC base=+0.217)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=781)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2905.4554` → IC=+0.165 (n=267)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2905.4554 (IC base=+0.109)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=781)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2905.4554` → IC=+0.165 (n=267)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2905.4554 (IC base=+0.109)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.208 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=84)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=138)

- **FILTRO** `libro_liquidez` < `2474.0326` → IC=-0.250 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 2474.0326
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=116)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=217)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=203)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=42)

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

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=1921)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=50)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=61)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=80)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.139 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 14.0 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 17.0 (IC base=+0.047)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35750.18` → IC=-0.123 (n=67)

  - _Acción_: SKIP cuando `liq_usd_total` < 35750.18
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=139)

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

- **PATRÓN** `liq_n` > `18.0` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.024)

- **PATRÓN** `liq_usd_total` > `70501.1` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `liq_usd_total` > 70501.1 (IC base=+0.024)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=141)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=840)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=794)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=439)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=205)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.495 (IC base=+0.016)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=658)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=658)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=392)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=392)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=176)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=176)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=111)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.132 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=67)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=94)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=118)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=218)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9815` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9815
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=89)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=93)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=96)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=249)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=249)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.152 (n=67)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=212)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=141)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.137 (n=293)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=744)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `profundidad_ratio` < `235.5` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `profundidad_ratio` < 235.5
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=68)

- **PATRÓN** `py_entrada` > `0.44` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.44 (IC base=+0.022)

- **PATRÓN** `restante_min` > `12.73` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 12.73 (IC base=+0.022)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.57` → IC=+0.130 (n=79)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.57 (IC base=+0.064)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `restante_min` > `13.45` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `restante_min` > 13.45
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=56)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=56)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=61)

- **FILTRO** `restante_min` < `3.99` → IC=-0.155 (n=56)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `lag_apertura_s` > `61.78` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `lag_apertura_s` > 61.78
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.122 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 9.0 (IC base=+0.061)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=66)

- **FILTRO** `profundidad_ratio` < `78.4` → IC=-0.198 (n=41)

  - _Acción_: SKIP cuando `profundidad_ratio` < 78.4
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=41)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=81)

- **PATRÓN** `py_entrada` > `0.53` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.53 (IC base=-0.024)

- **PATRÓN** `profundidad_ratio` > `78.4` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `profundidad_ratio` > 78.4 (IC base=-0.024)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.51 (IC base=-0.015)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=90)

- **FILTRO** `restante_min` < `3.82` → IC=-0.250 (n=54)

  - _Acción_: SKIP cuando `restante_min` < 3.82
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=57)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=84)

- **FILTRO** `lag_apertura_s` > `70.6` → IC=-0.254 (n=55)

  - _Acción_: SKIP cuando `lag_apertura_s` > 70.6
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=56)

- **FILTRO** `profundidad_ratio` < `81.9` → IC=-0.202 (n=55)

  - _Acción_: SKIP cuando `profundidad_ratio` < 81.9
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=56)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.44 (IC base=+0.061)

- **PATRÓN** `profundidad_ratio` > `26.3` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `profundidad_ratio` > 26.3 (IC base=+0.061)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `restante_min` < `13.48` → IC=-0.151 (n=61)

  - _Acción_: SKIP cuando `restante_min` < 13.48
  - _Potencial_: sin este filtro IC_bueno=+0.242 (n=29)

- **FILTRO** `lag_apertura_s` > `90.91` → IC=-0.138 (n=67)

  - _Acción_: SKIP cuando `lag_apertura_s` > 90.91
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=23)

- **PATRÓN** `restante_min` > `13.48` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 13.48 (IC base=-0.022)

- **PATRÓN** `lag_apertura_s` < `90.91` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 90.91 (IC base=-0.022)

- **PATRÓN** `restante_min` > `13.48` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `restante_min` > 13.48 (IC base=+0.000)

- **PATRÓN** `lag_apertura_s` < `90.99` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 90.99 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.151 (n=84)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=51)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.5 (IC base=-0.033)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.189 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=85)

- **FILTRO** `restante_min` < `2.76` → IC=-0.134 (n=39)

  - _Acción_: SKIP cuando `restante_min` < 2.76
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=118)

- **FILTRO** `lag_apertura_s` > `112.83` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `lag_apertura_s` > 112.83
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=104)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7770)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.167 (n=3765)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=11644)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.163 (n=3935)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=12022)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.465` → IC=-0.199 (n=673)

  - _Acción_: SKIP cuando `py_entrada` < 0.465
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=2019)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.186 (n=674)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=2066)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=693)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2179)

- **PATRÓN** `libro_liquidez` > `1790.9` → IC=+0.121 (n=932)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1790.9 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.175 (n=657)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=2027)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.174 (n=716)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=2157)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2222)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2312)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3052)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=409)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=400)

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
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=262)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.214 (n=82)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=260)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=10701)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=24327)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.274 (n=8641)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=26387)

- **FILTRO** `ibs_7min` < `0.2768` → IC=-0.234 (n=8757)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2768
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=26271)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=11764)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=23264)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.231 (n=10829)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=33356)

- **FILTRO** `ibs_7min` > `0.2922` → IC=-0.179 (n=11042)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2922
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=33143)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=1746)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4097)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=1385)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=4458)

- **FILTRO** `ibs_7min` < `0.7109` → IC=-0.252 (n=1928)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7109
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=3915)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.176 (n=1446)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=4397)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.259 (n=1884)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=5711)

- **FILTRO** `drift_7min_pct` |x|> `0.1361` → IC=-0.129 (n=1897)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1361
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5698)

- **FILTRO** `ibs_7min` > `0.7901` → IC=-0.208 (n=1898)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7901
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=5697)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.139 (n=1404)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4632)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.250 (n=1466)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4570)

- **FILTRO** `ibs_7min` < `0.7471` → IC=-0.193 (n=1508)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7471
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=4528)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.176 (n=1507)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=4529)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=1414)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4711)

- **FILTRO** `ibs_7min` > `0.2612` → IC=-0.185 (n=1531)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2612
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4594)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.180 (n=1531)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4594)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.169 (n=1347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=4216)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.303 (n=1386)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4177)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.242 (n=1827)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3736)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.212 (n=1385)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=4178)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.243 (n=1885)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=6258)

- **FILTRO** `ibs_7min` > `0.75` → IC=-0.174 (n=2031)

  - _Acción_: SKIP cuando `ibs_7min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6112)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=1843)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=3931)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.241 (n=1418)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=4356)

- **FILTRO** `ibs_7min` < `0.7407` → IC=-0.183 (n=1442)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4332)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.174 (n=1409)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4365)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.256 (n=1474)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=4441)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.179 (n=1477)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4438)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.183 (n=1472)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4443)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.263 (n=1408)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4634)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.234 (n=1497)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=4545)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.179 (n=1992)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=6433)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.254 (n=1902)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=3868)

- **FILTRO** `ibs_7min` < `0.2971` → IC=-0.225 (n=1442)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2971
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4328)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1379)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4391)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.207 (n=1871)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=6111)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1137)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=567)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=328)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=571)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.132 (n=796)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=720)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `464.449` → IC=+0.145 (n=266)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 464.449 (IC base=+0.116)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4374` → IC=+0.135 (n=61)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.4374 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.197 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `445.688` → IC=+0.136 (n=160)

  - _Acción_: Kelly boost +0.68€ cuando `total_vol_5m` < 445.688 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 14.0 (IC base=+0.131)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.167 (n=70)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 11.0 (IC base=+0.107)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4137` → IC=+0.194 (n=109)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio` |x|> 0.4137 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.124 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 4.0 (IC base=+0.104)

- **PATRÓN** `total_vol_5m` < `384.339` → IC=+0.203 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 384.339 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 75.0 (IC base=+0.104)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.171 (n=138)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.229 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `5032.488` → IC=+0.160 (n=92)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 5032.488 (IC base=+0.132)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.130 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 13.0 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3589.6144` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3589.6144 (IC base=+0.102)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0046` → IC=-0.266 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=137)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `54.581` → IC=-0.315 (n=63)

  - _Acción_: SKIP cuando `T_h` > 54.581
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=65)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.250 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.115)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `39.9918` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `T_h` < 39.9918
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=58)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `2.719` → IC=-0.228 (n=200)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.719
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=210)

- **FILTRO** `sigma_h` > `0.0095` → IC=-0.320 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.293 (n=264)

- **FILTRO** `sigma_h` < `0.0044` → IC=-0.332 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=264)

- **FILTRO** `T_h` > `61.3303` → IC=-0.330 (n=263)

  - _Acción_: SKIP cuando `T_h` > 61.3303
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **PATRÓN** `pct_vs_K` |x|≤ `1.0396` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `pct_vs_K` |x|≤ 1.0396 (IC base=-0.114)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `79.6334` → IC=-0.146 (n=97)

  - _Acción_: SKIP cuando `T_h` > 79.6334
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

- **FILTRO** `pct_vs_K` |x|> `2.84` → IC=-0.368 (n=36)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.84
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=109)

- **FILTRO** `T_h` < `97.926` → IC=-0.389 (n=43)

  - _Acción_: SKIP cuando `T_h` < 97.926
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=90)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.4229` → IC=-0.357 (n=54)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4229
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=62)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.328 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=84)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.328 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=84)

- **FILTRO** `T_h` > `60.9515` → IC=-0.329 (n=74)

  - _Acción_: SKIP cuando `T_h` > 60.9515
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=37)

- **PATRÓN** `pct_vs_K` |x|≤ `1.3415` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.3415 (IC base=-0.203)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0073` → IC=-0.167 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0073
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=75)

- **FILTRO** `T_h` > `132.7892` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `T_h` > 132.7892
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=67)

- **FILTRO** `pct_vs_K` |x|> `4.8556` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.8556
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=76)

- **FILTRO** `sigma_h` < `0.0146` → IC=-0.375 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0146
  - _Potencial_: sin este filtro IC_bueno=-0.315 (n=25)

- **FILTRO** `T_h` > `58.2361` → IC=-0.373 (n=53)

  - _Acción_: SKIP cuando `T_h` > 58.2361
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=18)

- **PATRÓN** `pct_vs_K` |x|≤ `1.14` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.14 (IC base=-0.039)

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

- **PATRÓN** `edge` > `0.1118` → IC=+0.456 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1118 (IC base=+0.416)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.416)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.443 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.416)

- **PATRÓN** `T_h` < `0.6208` → IC=+0.424 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6208 (IC base=+0.416)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.462 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.416)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.480 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.416)

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

- **PATRÓN** `dist_50` > `0.4178` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4178 (IC base=+0.414)

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

- **PATRÓN** `edge` > `0.114` → IC=+0.467 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.114 (IC base=+0.460)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.486 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.460)

- **PATRÓN** `T_h` > `0.9563` → IC=+0.467 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9563 (IC base=+0.460)

- **PATRÓN** `dist_50` > `0.5` → IC=+0.482 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.5 (IC base=+0.460)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.465 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.460)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=198)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=308)

- **FILTRO** `streak_estiramiento` > `0.8566` → IC=-0.162 (n=66)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8566
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=201)

- **PATRÓN** `streak_estiramiento` < `0.4787` → IC=+0.123 (n=67)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.4787 (IC base=+0.030)

- **PATRÓN** `streak_estiramiento` < `0.7314` → IC=+0.120 (n=177)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.7314 (IC base=+0.035)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=19)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `2331737.7` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 2331737.7
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=46)

- **FILTRO** `streak_estiramiento` > `0.479` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.479
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=37)

- **PATRÓN** `streak_estiramiento` < `0.479` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.479 (IC base=-0.008)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.121 (n=93)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 49.0 (IC base=+0.053)

### STREAK_FADE_5M#ETH#5min
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
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=797)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=803)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=430)

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

- **FILTRO** `streak_estiramiento` > `0.9124` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.9124
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

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
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=652)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1202)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=809)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=782)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3065)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1553)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1561)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.193 (n=597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0043 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.226 (n=596)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.201 (n=787)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2165` → IC=+0.192 (n=596)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2165 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.233 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=1679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=1856)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.6087` → IC=+0.268 (n=1787)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6087 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1185` → IC=+0.183 (n=899)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1185 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.6071` → IC=+0.180 (n=1695)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.6071 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.833` → IC=+0.274 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.833 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `8780.1789` → IC=+0.196 (n=596)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 8780.1789 (IC base=+0.188)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=714)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.218 (n=395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.291 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.208)

- **PATRÓN** `drift_15min` |x|≤ `0.3838` → IC=+0.216 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3838 (IC base=+0.208)

- **PATRÓN** `delta_ratio_macro` |x|> `0.255` → IC=+0.246 (n=132)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.255 (IC base=+0.208)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1084` → IC=+0.280 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1084 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.276 (n=395)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.267 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.55` → IC=+0.272 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.55 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `16060.5409` → IC=+0.231 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16060.5409 (IC base=+0.208)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.723` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.723
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=439)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.169 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0035 (IC base=+0.130)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.133 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.005 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0674` → IC=+0.160 (n=183)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0674 (IC base=+0.130)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2346` → IC=+0.171 (n=138)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.2346 (IC base=+0.130)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1217` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1217 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.135 (n=434)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_15` > `0.6586` → IC=+0.253 (n=370)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6586 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1133` → IC=+0.148 (n=296)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1133 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.257` → IC=+0.219 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.257 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `9475.4181` → IC=+0.147 (n=188)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 9475.4181 (IC base=+0.130)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.281 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.1481` → IC=+0.195 (n=188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1481 (IC base=+0.171)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0606` → IC=+0.188 (n=213)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.0606 (IC base=+0.171)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2673` → IC=+0.216 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2673 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.189 (n=204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.171)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.255 (n=214)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.177 (n=122)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.175 (n=207)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.286` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.286 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=154)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `3071.8702` → IC=+0.258 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3071.8702 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.213 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.171)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.68` → IC=-0.154 (n=105)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=1098)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.784` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.784 (IC base=-0.003)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0234` → IC=+0.271 (n=155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0234 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.225 (n=205)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.196)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0403` → IC=+0.200 (n=465)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0403 (IC base=+0.196)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.260 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `ibs_15` > `0.5695` → IC=+0.286 (n=465)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5695 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `0.3546` → IC=+0.209 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3546 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` < `0.8342` → IC=+0.199 (n=539)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.8342 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.251` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.251 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.374` → IC=+0.199 (n=423)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 7.374 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2911.0954` → IC=+0.283 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2911.0954 (IC base=+0.196)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.150 (n=524)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1176 (IC base=+0.054)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.355 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.349)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.373 (n=148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.349)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.352 (n=296)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.349)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.362 (n=441)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.349)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1326` → IC=+0.387 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1326 (IC base=+0.349)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.369 (n=449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.349)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.390 (n=442)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.349)

- **PATRÓN** `dist_vwap_pct` > `0.4241` → IC=+0.389 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4241 (IC base=+0.349)

- **PATRÓN** `dist_vwap_pct` < `0.1081` → IC=+0.350 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1081 (IC base=+0.349)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.247` → IC=+0.356 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.247 (IC base=+0.349)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.350 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.349)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.353 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.349)

- **PATRÓN** `libro_liquidez` > `3425.1488` → IC=+0.360 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3425.1488 (IC base=+0.349)

- **PATRÓN** `ballena_activa_n` < `459.0` → IC=+0.371 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 459.0 (IC base=+0.349)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.362 (n=216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.381 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.354)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.369 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.354)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.364 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.354)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.373 (n=163)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.354)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1241` → IC=+0.394 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1241 (IC base=+0.354)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.380 (n=247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.354)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.387 (n=245)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.405 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.360 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.356 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.354)

- **PATRÓN** `libro_liquidez` > `11121.9309` → IC=+0.373 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11121.9309 (IC base=+0.354)

- **PATRÓN** `ballena_activa_n` < `571.0` → IC=+0.399 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 571.0 (IC base=+0.354)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.340 (n=198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.342)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.370 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.342)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.351 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.342)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.366 (n=177)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.342)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.367 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.342)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.405 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.342)

- **PATRÓN** `ibs_15` > `0.743` → IC=+0.395 (n=198)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.743 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` > `0.4534` → IC=+0.375 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4534 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` < `0.1133` → IC=+0.353 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1133 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.358 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.344 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.342)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.349 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.342)

- **PATRÓN** `libro_liquidez` > `3456.6166` → IC=+0.351 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3456.6166 (IC base=+0.342)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.352 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.342)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.223 (n=705)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2119)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=980)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1844)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.250 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.6409` → IC=+0.273 (n=672)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6409 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.191 (n=541)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0765` → IC=+0.247 (n=1778)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0765 (IC base=-0.028)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1785` → IC=+0.243 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1785 (IC base=-0.028)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.275 (n=1992)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.6792` → IC=+0.300 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6792 (IC base=-0.028)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.216 (n=424)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=1274)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.228 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=1274)

- **FILTRO** `sigma_ewma_delta_pct` > `19.574` → IC=-0.253 (n=302)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.574
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1396)

- **FILTRO** `libro_liquidez` < `14486.8794` → IC=-0.206 (n=560)

  - _Acción_: SKIP cuando `libro_liquidez` < 14486.8794
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=1138)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.167 (n=163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0027 (IC base=+0.082)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2051` → IC=+0.275 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2051 (IC base=+0.082)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.341 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.082)

- **PATRÓN** `ibs_15` > `0.7496` → IC=+0.334 (n=191)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7496 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.0982` → IC=+0.280 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0982 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` < `0.3564` → IC=+0.275 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3564 (IC base=+0.082)

- **PATRÓN** `ibs_15` < `0.213` → IC=+0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.213 (IC base=-0.199)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=408)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.151 (n=319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0067 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.172 (n=285)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.004 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0736` → IC=+0.220 (n=141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0736 (IC base=+0.149)

- **PATRÓN** `drift_15min` |x|≤ `0.4169` → IC=+0.179 (n=107)

  - _Acción_: Kelly boost +0.89€ cuando `drift_15min` |x|≤ 0.4169 (IC base=+0.149)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0901` → IC=+0.148 (n=285)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio_macro` |x|> 0.0901 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.232 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.6647` → IC=+0.260 (n=319)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6647 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.181 (n=230)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.042` → IC=+0.150 (n=115)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 14.042 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.024` → IC=+0.151 (n=273)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 9.024 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=408)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11052.2058` → IC=+0.180 (n=145)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 11052.2058 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.248 (n=760)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.3563` → IC=+0.242 (n=668)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3563 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `0.4735` → IC=+0.256 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4735 (IC base=+0.236)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2044` → IC=+0.264 (n=345)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2044 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.253 (n=285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.236)

- **PATRÓN** `ibs_15` < `0.2705` → IC=+0.284 (n=668)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2705 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.7528` → IC=+0.325 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7528 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.652` → IC=+0.257 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.652 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.283` → IC=+0.243 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.283 (IC base=+0.236)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.256 (n=166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=500)

- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.224 (n=226)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=440)

- **FILTRO** `drift_15min` |x|> `0.8849` → IC=-0.274 (n=166)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8849
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=500)

- **PATRÓN** `ibs_15` > `0.9` → IC=+0.309 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9 (IC base=-0.174)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0771` → IC=+0.229 (n=304)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0771 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.260 (n=340)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7388` → IC=+0.240 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7388 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1863` → IC=+0.222 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1863 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.259 (n=409)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=411)

- **FILTRO** `drift_15min` |x|> `1.2549` → IC=-0.267 (n=204)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2549
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=616)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.260 (n=215)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=605)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1379` → IC=+0.300 (n=238)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1379 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1078` → IC=+0.334 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1078 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.3391` → IC=+0.305 (n=525)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3391 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.8999` → IC=+0.340 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8999 (IC base=-0.039)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

- **PATRÓN** `dist_vwap_pct` > `0.1645` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1645 (IC base=+0.049)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

- **PATRÓN** `dist_vwap_pct` > `0.1645` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1645 (IC base=+0.049)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.299 (n=626)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.333 (n=238)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2402` → IC=+0.307 (n=237)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2402 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.337 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8411` → IC=+0.329 (n=711)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8411 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.4333` → IC=+0.339 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4333 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.347 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.292 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `13022.3239` → IC=+0.297 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13022.3239 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.292 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.289 (n=349)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.003 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.350 (n=131)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2605` → IC=+0.311 (n=130)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2605 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3906` → IC=+0.311 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3906 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.319 (n=390)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.356 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.365 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `16113.4131` → IC=+0.326 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16113.4131 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.312 (n=322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.069` → IC=+0.312 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.069 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.301 (n=214)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.326 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.314 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8539` → IC=+0.339 (n=321)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8539 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.4406` → IC=+0.302 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4406 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` < `0.1135` → IC=+0.294 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1135 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.333 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.301 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2527` → IC=-0.162 (n=72)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2527
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=217)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.134 (n=192)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=65)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.121` → IC=-0.173 (n=111)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.121
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=336)

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
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=129)

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
- **PATRÓN** `T_h` > `79.3918` → IC=+0.219 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 79.3918 (IC base=+0.202)

- **PATRÓN** `ratio` < `0.9775` → IC=+0.472 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9775 (IC base=+0.202)

- **PATRÓN** `T_h` > `145.7785` → IC=+0.394 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7785 (IC base=+0.333)

- **PATRÓN** `ratio` > `1.0115` → IC=+0.290 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0115 (IC base=+0.333)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `122.1058` → IC=+0.214 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 122.1058 (IC base=+0.180)

- **PATRÓN** `ratio` < `0.973` → IC=+0.448 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.180)

- **PATRÓN** `T_h` > `103.3918` → IC=+0.289 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.284)

- **PATRÓN** `ratio` > `1.0468` → IC=+0.357 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0468 (IC base=+0.284)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `93.6267` → IC=+0.278 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 93.6267 (IC base=+0.240)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.425 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.240)

- **PATRÓN** `T_h` > `105.6124` → IC=+0.327 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 105.6124 (IC base=+0.314)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.333 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.314)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1332` → IC=+0.459 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1332 (IC base=+0.402)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6087 sube el IC de +0.188 a +0.268 en UPDOWN_GBM#15min (n=1787). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.208 a +0.276 en UPDOWN_GBM#BTC#15min (n=395). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6586 sube el IC de +0.130 a +0.253 en UPDOWN_GBM#ETH#15min (n=370). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.171 a +0.255 en UPDOWN_GBM#SOL#15min (n=214). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5695 sube el IC de +0.196 a +0.286 en UPDOWN_GBM#XRP#15min (n=465). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.054 a +0.150 en UPDOWN_GBM#XRP#15min (n=524). Ya aplicado como kelly_boost=+0.75€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6409 sube el IC de -0.067 a +0.273 en UPDOWN_GBM_15M_TARDIO (n=672). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.028 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=1992). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7496 sube el IC de +0.082 a +0.334 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=191). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.213 sube el IC de -0.199 a +0.382 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6647 sube el IC de +0.149 a +0.260 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=319). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2705 sube el IC de +0.236 a +0.284 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=668). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9 sube el IC de -0.174 a +0.309 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.042 a +0.260 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=340). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3391 sube el IC de -0.039 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=525). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8411 sube el IC de +0.292 a +0.329 en UPDOWN_GBM_IBS_ALTO (n=711). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.287 a +0.319 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=390). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8539 sube el IC de +0.295 a +0.339 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=321). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.349 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=442). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.354 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=245). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.743 sube el IC de +0.342 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=198). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `LIQUIDACIONES_DEPTH_FASE0#BNB#15min` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1377 | +0.100 | +199.45€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1377 | +0.100 | +199.45€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1036 | +0.110 | +171.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1036 | +0.110 | +171.75€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 29707 | -0.083 | -3960.33€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1566 | -0.028 | -212.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 28141 | -0.086 | -3747.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3870 | -0.097 | -642.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3870 | -0.097 | -642.40€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1566 | -0.028 | -212.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1566 | -0.028 | -212.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3508 | -0.098 | -807.53€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3508 | -0.098 | -807.53€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7667 | -0.015 | -719.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7667 | -0.015 | -719.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7261 | -0.088 | -455.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7261 | -0.088 | -455.45€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5835 | -0.163 | -1123.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5835 | -0.163 | -1123.34€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 20268 | -0.025 | +3892.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5253 | +0.001 | +1794.70€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 15015 | -0.034 | +2098.02€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 20268 | -0.025 | +3892.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5253 | +0.001 | +1794.70€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 15015 | -0.034 | +2098.02€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 99299 | +0.113 | -4800.31€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 14698 | +0.185 | -424.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 403 | -0.070 | -51.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 77843 | +0.101 | -4106.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6355 | +0.107 | -217.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 12939 | +0.099 | -1044.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 47 | -0.173 | -2.03€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 12877 | +0.101 | -1030.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 20014 | +0.132 | -343.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4613 | +0.203 | -127.59€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 12905 | +0.114 | -164.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2454 | +0.100 | -28.89€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 12979 | +0.091 | -1154.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 54 | -0.107 | -8.00€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 12910 | +0.092 | -1135.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 21090 | +0.124 | -369.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5728 | +0.177 | -61.93€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 13049 | +0.106 | -240.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2301 | +0.100 | -57.98€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 19326 | +0.114 | -1120.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4208 | +0.188 | -232.60€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 306 | -0.029 | +2.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 13212 | +0.091 | -759.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1600 | +0.129 | -130.27€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 12951 | +0.100 | -768.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 48 | -0.040 | +7.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 12890 | +0.101 | -776.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 15764 | +0.193 | -1005.48€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 15764 | +0.193 | -1005.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3734 | +0.168 | -391.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3734 | +0.168 | -391.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1433 | +0.203 | -6.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1433 | +0.203 | -6.22€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3674 | +0.180 | -309.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3674 | +0.180 | -309.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3241 | +0.241 | -100.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3241 | +0.241 | -100.65€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3603 | +0.193 | -211.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3603 | +0.193 | -211.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 744 | +0.429 | -21.93€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 744 | +0.429 | -21.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 289 | +0.438 | -2.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 289 | +0.438 | -2.64€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 282 | +0.430 | -7.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 282 | +0.430 | -7.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 163 | +0.409 | -9.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 163 | +0.409 | -9.53€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 54478 | +0.198 | -4202.93€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 54478 | +0.198 | -4202.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9404 | +0.178 | -1063.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9404 | +0.178 | -1063.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 8715 | +0.224 | -312.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 8715 | +0.224 | -312.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 9405 | +0.174 | -1096.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 9405 | +0.174 | -1096.88€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 8807 | +0.218 | -349.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 8807 | +0.218 | -349.35€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9010 | +0.203 | -590.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9010 | +0.203 | -590.56€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9137 | +0.193 | -790.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9137 | +0.193 | -790.42€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 20596 | +0.117 | +161.35€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 20596 | +0.117 | +161.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 10226 | +0.120 | +127.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 10226 | +0.120 | +127.97€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 10370 | +0.114 | +33.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 10370 | +0.114 | +33.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1553 | +0.288 | -22.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1553 | +0.288 | -22.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 695 | +0.278 | -18.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 695 | +0.278 | -18.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 745 | +0.288 | -6.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 745 | +0.288 | -6.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 113 | +0.344 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 113 | +0.344 | +2.86€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 688 | +0.435 | -5.13€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 688 | +0.435 | -5.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 328 | +0.433 | -3.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 328 | +0.433 | -3.87€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 315 | +0.437 | -1.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 315 | +0.437 | -1.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 45 | +0.394 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 45 | +0.394 | +0.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1179 | +0.069 | -57.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 414 | +0.051 | -40.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 765 | +0.079 | -17.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 62 | +0.109 | +2.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 62 | +0.109 | +2.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 931 | +0.077 | -26.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 166 | +0.066 | -8.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 765 | +0.079 | -17.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 186 | +0.016 | -33.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 186 | +0.016 | -33.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 38595 | +0.098 | -1100.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3167 | +0.090 | +25.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 35428 | +0.099 | -1126.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 21575 | +0.103 | -304.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3167 | +0.090 | +25.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 18408 | +0.105 | -329.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 7376 | +0.109 | -22.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 7376 | +0.109 | -22.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 9644 | +0.080 | -773.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 9644 | +0.080 | -773.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 844 | +0.216 | -102.02€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 844 | +0.216 | -102.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 844 | +0.216 | -102.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 844 | +0.216 | -102.02€ | 2 | 4 |
| ✅ GBM_LATE_15M | 27445 | +0.084 | +13226.98€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 27445 | +0.084 | +13226.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4585 | +0.197 | +3410.91€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4585 | +0.197 | +3410.91€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 4074 | +0.179 | +2891.31€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4074 | +0.179 | +2891.31€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 4821 | +0.198 | +3599.36€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4821 | +0.198 | +3599.36€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 3970 | +0.024 | +894.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3970 | +0.024 | +894.90€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 3929 | -0.033 | +892.14€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3929 | -0.033 | +892.14€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6066 | -0.040 | +1538.36€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6066 | -0.040 | +1538.36€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 29190 | +0.086 | +15307.99€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 29190 | +0.086 | +15307.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5553 | +0.013 | +2901.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5553 | +0.013 | +2901.54€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6095 | +0.015 | +1272.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6095 | +0.015 | +1272.87€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4150 | +0.265 | +4215.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4150 | +0.265 | +4215.08€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4802 | +0.005 | +924.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4802 | +0.005 | +924.31€ | 2 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4714 | +0.029 | +1813.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4714 | +0.029 | +1813.82€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3876 | +0.279 | +4180.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3876 | +0.279 | +4180.38€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 22015 | +0.169 | +16614.72€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 22015 | +0.169 | +16614.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3321 | +0.209 | +2670.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3321 | +0.209 | +2670.99€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3462 | +0.150 | +2533.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3462 | +0.150 | +2533.07€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3474 | +0.209 | +2775.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3474 | +0.209 | +2775.30€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3683 | +0.133 | +2586.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3683 | +0.133 | +2586.27€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4118 | +0.118 | +2895.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4118 | +0.118 | +2895.53€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3957 | +0.205 | +3153.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3957 | +0.205 | +3153.55€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 5691 | +0.136 | +2590.19€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 5691 | +0.136 | +2590.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 211 | +0.110 | +81.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 211 | +0.110 | +81.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1589 | +0.134 | +786.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1589 | +0.134 | +786.92€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1705 | +0.153 | +822.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1705 | +0.153 | +822.35€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1306 | +0.118 | +507.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1306 | +0.118 | +507.09€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 27596 | +0.178 | +20874.80€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 27596 | +0.178 | +20874.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4369 | +0.224 | +3752.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4369 | +0.224 | +3752.10€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4310 | +0.152 | +2869.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4310 | +0.152 | +2869.75€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4568 | +0.226 | +3938.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4568 | +0.226 | +3938.80€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4472 | +0.137 | +3080.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4472 | +0.137 | +3080.97€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4831 | +0.116 | +3176.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4831 | +0.116 | +3176.95€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5046 | +0.210 | +4056.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5046 | +0.210 | +4056.23€ | 0 | 24 |
| ✅ GBM_LATE_5M | 7683 | +0.163 | +4797.17€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 7683 | +0.163 | +4797.17€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 736 | +0.218 | +610.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 736 | +0.218 | +610.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1831 | +0.151 | +1221.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1831 | +0.151 | +1221.83€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 892 | +0.171 | +566.39€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 892 | +0.171 | +566.39€ | 0 | 21 |
| ✅ GBM_LATE_5M#ETH | 2546 | +0.166 | +1571.90€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2546 | +0.166 | +1571.90€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 742 | +0.144 | +384.69€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 742 | +0.144 | +384.69€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 936 | +0.137 | +442.01€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 936 | +0.137 | +442.01€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1888 | +0.066 | +727.93€ | 2 | 12 |
| ✅ GBM_LATE_60M#60min | 1888 | +0.066 | +727.93€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 694 | +0.088 | +257.94€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 694 | +0.088 | +257.94€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 620 | +0.069 | +290.94€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 620 | +0.069 | +290.94€ | 2 | 14 |
| ✅ GBM_LATE_60M#SOL | 574 | +0.036 | +179.05€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 574 | +0.036 | +179.05€ | 2 | 9 |
| 🚫 GBM_LATE_60M_FADE | 393 | -0.254 | -19.93€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 393 | -0.254 | -19.93€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 149 | -0.222 | -7.12€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 149 | -0.222 | -7.12€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 130 | -0.258 | -6.98€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 130 | -0.258 | -6.98€ | 3 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 114 | -0.284 | -5.83€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 114 | -0.284 | -5.83€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 748 | +0.076 | +174.55€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 748 | +0.076 | +174.55€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 293 | +0.066 | +60.90€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 293 | +0.066 | +60.90€ | 2 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 227 | +0.042 | +13.76€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 227 | +0.042 | +13.76€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 228 | +0.122 | +99.89€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 228 | +0.122 | +99.89€ | 2 | 12 |
| ✅ LATE_WINDOW_5MIN | 103 | +0.262 | +87.89€ | 0 | 10 |
| ✅ LATE_WINDOW_5MIN#5min | 103 | +0.262 | +87.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 103 | +0.262 | +87.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 103 | +0.262 | +87.89€ | 0 | 10 |
| ✅ LEADLAG_BTC_XRP_15M | 2160 | +0.105 | +599.84€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2160 | +0.105 | +599.84€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2160 | +0.105 | +599.84€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2160 | +0.105 | +599.84€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 392 | -0.076 | -33.33€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 392 | -0.076 | -33.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 100 | -0.059 | -4.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 100 | -0.059 | -4.97€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 143 | -0.017 | -3.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 143 | -0.017 | -3.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2120 | +0.010 | +26.68€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2120 | +0.010 | +26.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 110 | +0.027 | +0.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 110 | +0.027 | +0.19€ | 1 | 2 |
| ✅ LIQUIDACIONES_5M#BTC | 241 | -0.006 | +11.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 241 | -0.006 | +11.21€ | 5 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 169 | -0.021 | -4.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 169 | -0.021 | -4.84€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 887 | +0.023 | +21.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 887 | +0.023 | +21.67€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 479 | +0.003 | -3.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 479 | +0.003 | -3.33€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 234 | +0.004 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 234 | +0.004 | +1.79€ | 1 | 1 |
| ✅ LIQUIDACIONES_60M | 1145 | -0.044 | -27.84€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1145 | -0.044 | -27.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 324 | -0.046 | -14.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 324 | -0.046 | -14.46€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 386 | -0.028 | -1.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 386 | -0.028 | -1.62€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 435 | -0.056 | -11.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 435 | -0.056 | -11.76€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 2105 | -0.012 | +73.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1011 | -0.011 | +31.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1094 | -0.013 | +41.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 56 | +0.052 | +9.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 32 | +0.088 | +8.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 24 | +0.000 | +1.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 497 | +0.017 | +46.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 232 | +0.013 | +14.08€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 265 | +0.021 | +32.81€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 277 | -0.041 | -2.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 137 | -0.054 | -5.19€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 140 | -0.028 | +2.20€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 397 | -0.024 | -3.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 181 | -0.019 | +1.29€ | 3 | 3 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 216 | -0.028 | -4.90€ | 5 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 382 | -0.005 | +22.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 194 | -0.010 | +10.15€ | 2 | 4 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 188 | +0.000 | +11.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 496 | -0.028 | +1.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 235 | -0.019 | +3.08€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 261 | -0.036 | -1.76€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 14634 | -0.012 | -219.07€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14634 | -0.012 | -219.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3351 | -0.022 | -72.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3351 | -0.022 | -72.25€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 31366 | -0.006 | +1366.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 31366 | -0.006 | +1366.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5540 | +0.019 | +684.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5540 | +0.019 | +684.12€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4803 | -0.030 | -73.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4803 | -0.030 | -73.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5612 | +0.015 | +491.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5612 | +0.015 | +491.88€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4588 | -0.053 | -156.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4588 | -0.053 | -156.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5266 | -0.010 | +205.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5266 | -0.010 | +205.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5557 | +0.009 | +214.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5557 | +0.009 | +214.28€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5992 | -0.060 | -150.60€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5992 | -0.060 | -150.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1445 | -0.084 | -40.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1445 | -0.084 | -40.56€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 676 | -0.122 | -29.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 676 | -0.122 | -29.33€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1757 | -0.079 | -35.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1757 | -0.079 | -35.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 854 | -0.015 | -25.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 854 | -0.015 | -25.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3345 | +0.004 | -2.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3345 | +0.004 | -2.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1315 | +0.007 | +7.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1315 | +0.007 | +7.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 79213 | -0.073 | +1708.51€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 79213 | -0.073 | +1708.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 13438 | -0.077 | +787.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 13438 | -0.077 | +787.00€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 12161 | -0.094 | -595.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 12161 | -0.094 | -595.39€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 13706 | -0.067 | +720.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 13706 | -0.067 | +720.40€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 11689 | -0.093 | -220.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 11689 | -0.093 | -220.60€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 14467 | -0.048 | +394.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 14467 | -0.048 | +394.23€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 13752 | -0.063 | +622.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 13752 | -0.063 | +622.87€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7763 | -0.027 | -135.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7763 | -0.027 | -135.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1765 | -0.036 | -16.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1765 | -0.036 | -16.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2193 | -0.021 | -24.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2193 | -0.021 | -24.96€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1056 | -0.045 | -20.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1056 | -0.045 | -20.70€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 750 | -0.019 | -22.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 750 | -0.019 | -22.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1197 | +0.110 | +412.02€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 1061 | +0.116 | +399.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 242 | +0.131 | +114.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 242 | +0.131 | +114.58€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 204 | +0.107 | +56.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 204 | +0.107 | +56.52€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 218 | +0.104 | +80.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 218 | +0.104 | +80.29€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 183 | +0.132 | +84.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 183 | +0.132 | +84.61€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 214 | +0.102 | +63.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 214 | +0.102 | +63.43€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 591 | -0.050 | -56.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 591 | -0.050 | -56.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 121 | -0.012 | +1.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 121 | -0.012 | +1.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 78 | -0.100 | -16.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 78 | -0.100 | -16.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 171 | -0.061 | -26.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 171 | -0.061 | -26.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 120 | -0.025 | -4.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 120 | -0.025 | -4.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 101 | -0.063 | -11.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 101 | -0.063 | -11.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 598 | -0.110 | -51.30€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 275 | -0.161 | -65.48€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 227 | -0.203 | -68.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 48 | +0.040 | +2.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 206 | -0.072 | +1.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 162 | -0.079 | -6.75€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 44 | -0.043 | +8.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 117 | -0.055 | +12.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 95 | -0.077 | +6.09€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 484 | -0.138 | -68.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 761 | -0.201 | -33.33€ | 4 | 1 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 315 | -0.200 | -29.44€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 278 | -0.196 | -29.04€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 259 | -0.216 | -23.73€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 227 | -0.225 | -28.39€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 187 | -0.177 | +19.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 171 | -0.176 | +15.17€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 676 | -0.202 | -42.26€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 313 | +0.408 | +227.18€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 32 | +0.088 | -2.58€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 32 | +0.088 | -2.58€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 81 | +0.380 | +59.35€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 81 | +0.380 | +59.35€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 200 | +0.465 | +170.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 200 | +0.465 | +170.41€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 313 | +0.408 | +227.18€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 544 | +0.033 | +17.42€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 544 | +0.033 | +17.42€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 260 | +0.034 | +6.25€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 260 | +0.034 | +6.25€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 36 | +0.079 | +2.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 36 | +0.079 | +2.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 57 | -0.009 | -1.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 57 | -0.009 | -1.59€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 191 | +0.034 | +10.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 191 | +0.034 | +10.66€ | 2 | 3 |
| ✅ STREAK_FADE_5M | 2835 | -0.022 | -114.09€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2835 | -0.022 | -114.09€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 822 | -0.018 | -26.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 822 | -0.018 | -26.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 570 | -0.023 | -23.26€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 570 | -0.023 | -23.26€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1287 | -0.021 | -49.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1287 | -0.021 | -49.62€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 76 | -0.051 | -6.76€ | 4 | 0 |
| ✅ STREAK_FADE_60M#60min | 76 | -0.051 | -6.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 38 | +0.000 | -2.32€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 38 | +0.000 | -2.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 8353 | +0.024 | +132.60€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8353 | +0.024 | +132.60€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2279 | +0.025 | +32.94€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2279 | +0.025 | +32.94€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1893 | +0.033 | +51.62€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1893 | +0.033 | +51.62€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2548 | +0.013 | +8.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2548 | +0.013 | +8.14€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1633 | +0.029 | +39.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1633 | +0.029 | +39.90€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7694 | +0.014 | -31.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7694 | +0.014 | -31.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3084 | +0.017 | -5.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3084 | +0.017 | -5.31€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3025 | +0.013 | -14.84€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3025 | +0.013 | -14.84€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1585 | +0.008 | -11.74€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1585 | +0.008 | -11.74€ | 2 | 0 |
| ✅ UPDOWN_GBM | 42214 | +0.034 | +2685.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 11127 | +0.071 | +2090.44€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1507 | +0.004 | +6.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 26879 | +0.025 | +570.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2543 | +0.002 | +20.39€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4371 | +0.074 | +529.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 789 | +0.160 | +340.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3549 | +0.056 | +190.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 7944 | +0.040 | +574.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1409 | +0.087 | +318.58€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 403 | +0.016 | +6.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 4926 | +0.040 | +221.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1146 | +0.003 | +27.37€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 60 | -0.097 | +0.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4937 | +0.041 | +313.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 746 | +0.138 | +260.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4163 | +0.024 | +54.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 9114 | +0.022 | +363.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2801 | +0.048 | +304.65€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 395 | +0.006 | +7.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 5012 | +0.015 | +57.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 854 | -0.002 | -8.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 52 | -0.130 | +3.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 9675 | +0.015 | +248.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2678 | +0.027 | +187.04€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 387 | -0.004 | -2.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6023 | +0.013 | +65.21€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 543 | +0.006 | +1.97€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 44 | -0.174 | -3.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 6171 | +0.040 | +658.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2704 | +0.086 | +679.27€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 261 | -0.002 | -3.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3206 | +0.003 | -17.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 156 | -0.133 | +0.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 589 | +0.349 | +193.44€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 589 | +0.349 | +193.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 326 | +0.354 | +104.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 326 | +0.354 | +104.07€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 263 | +0.342 | +89.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 263 | +0.342 | +89.38€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 12937 | -0.036 | +2827.87€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 12937 | -0.036 | +2827.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 887 | -0.046 | +379.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 887 | -0.046 | +379.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2349 | -0.121 | +18.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2349 | -0.121 | +18.02€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 471 | +0.187 | +329.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 471 | +0.187 | +329.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1437 | +0.210 | +881.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1437 | +0.210 | +881.54€ | 1 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3881 | -0.064 | +581.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3881 | -0.064 | +581.14€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3912 | -0.073 | +638.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3912 | -0.073 | +638.93€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 148 | +0.040 | +8.49€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 148 | +0.040 | +8.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 148 | +0.040 | +8.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 148 | +0.040 | +8.49€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 948 | +0.292 | +756.31€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 948 | +0.292 | +756.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 520 | +0.287 | +395.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 520 | +0.287 | +395.43€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 428 | +0.295 | +360.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 428 | +0.295 | +360.87€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 736 | -0.113 | -84.24€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 736 | -0.113 | -84.24€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 216 | -0.083 | -16.24€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 216 | -0.083 | -16.24€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 71 | -0.199 | -8.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 71 | -0.199 | -8.62€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2526 | +0.301 | +1260.63€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 876 | +0.252 | +123.78€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 954 | +0.291 | +411.49€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 696 | +0.377 | +725.36€ | 0 | 1 |