# Hipótesis automáticas — 2026-09-30 10:41 UTC
_Generado por shadow_postmortem.py sobre 680587 resoluciones (PNL=+80422.74€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=548)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.236 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.138)

- **PATRÓN** `n_total_lado` > `74.0` → IC=+0.213 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 74.0 (IC base=+0.138)

- **PATRÓN** `banda_hit_calibrado` > `0.8032` → IC=+0.255 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8032 (IC base=+0.138)

- **PATRÓN** `banda_z` > `9.581` → IC=+0.200 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.581 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.157 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=608)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4766.038` → IC=+0.163 (n=191)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4766.038 (IC base=+0.138)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=548)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.139 (n=203)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 93.0 (IC base=+0.059)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.142 (n=171)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.259 (n=441)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=413)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.259 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.147)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.209 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.147)

- **PATRÓN** `banda_hit_calibrado` > `0.7998` → IC=+0.266 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7998 (IC base=+0.147)

- **PATRÓN** `banda_z` > `4.287` → IC=+0.169 (n=460)

  - _Acción_: Kelly boost +0.84€ cuando `banda_z` > 4.287 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.169 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=518)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `3317.318` → IC=+0.153 (n=306)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3317.318 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `8317.7389` → IC=+0.121 (n=233)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 8317.7389 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.153 (n=165)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 94.0 (IC base=+0.063)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
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

- **PATRÓN** `py_entrada` > `0.35` → IC=+0.218 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.35 (IC base=+0.110)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.110)

- **PATRÓN** `banda_z` > `8.424` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.424 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1195.1095` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1195.1095 (IC base=+0.110)

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
- **FILTRO** `restante_s_al_confirmar` < `145.74` → IC=-0.217 (n=7699)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.74
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=23104)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `137.45` → IC=-0.247 (n=1003)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 137.45
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3009)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `127.76` → IC=-0.305 (n=899)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.76
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2699)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.41` → IC=-0.204 (n=1889)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.41
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=5670)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `126.9` → IC=-0.330 (n=1506)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 126.9
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=4518)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.209 (n=15121)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=3707)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5553.0459` → IC=+0.174 (n=2388)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 5553.0459 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=12868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=15856)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.231 (n=12150)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=6047)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7753.9545` → IC=+0.170 (n=2305)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 7753.9545 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=1742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.204 (n=1788)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=2249)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `15968.2024` → IC=+0.232 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15968.2024 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.200 (n=1610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1799)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.261 (n=1590)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2300)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `15889.5889` → IC=+0.215 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15889.5889 (IC base=+0.196)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.170 (n=356)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.615 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `4566.8958` → IC=+0.137 (n=243)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 4566.8958 (IC base=+0.094)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.148 (n=396)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.101)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=876)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.157 (n=228)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.101)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=3107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.348 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.235 (n=1396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.366 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.232 (n=1612)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `4240.0828` → IC=+0.229 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4240.0828 (IC base=+0.228)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.136 (n=739)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.248 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=839)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1318.0949` → IC=+0.147 (n=734)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1318.0949 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.078)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.405 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.153 (n=1165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.160 (n=630)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` < `0.285` → IC=+0.308 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.285 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=776)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.151)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.179 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.369 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `1222.0032` → IC=+0.155 (n=233)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1222.0032 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.225 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.117)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=12957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=12396)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.229 (n=4162)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `5024.6381` → IC=+0.335 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5024.6381 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=3090)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=2930)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=2950)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.171)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.249 (n=1126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.243 (n=1126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.240)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.345 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.240)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=3042)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=2907)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2456)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.252 (n=2678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.326 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.310 (n=56)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=2965)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.192 (n=2857)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.193 (n=2237)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.193 (n=1094)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.73 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `11452.1989` → IC=+0.459 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11452.1989 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.446 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.453 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `14442.7712` → IC=+0.448 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14442.7712 (IC base=+0.441)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.442 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.464 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `3366.033` → IC=+0.447 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3366.033 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.414 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.411)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.413 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.411)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.425 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.411)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.412 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.411)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=38512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.234 (n=20545)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=7825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=5355)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=7249)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=6950)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.264 (n=3939)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=7021)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=7024)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=3469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.267 (n=2384)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=6389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=2548)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=2761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=2975)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=5870)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.125 (n=5503)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5582)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=7289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.55` → IC=+0.137 (n=5463)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.55 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=2951)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.15` → IC=+0.125 (n=2708)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.15 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=2761)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=3599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.25` → IC=+0.138 (n=2716)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.25 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.185 (n=2919)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.112)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.133 (n=3085)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.112)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.137 (n=2761)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.25 (IC base=+0.112)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1545.7265` → IC=+0.294 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1545.7265 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.291 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.346 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `5084.4032` → IC=+0.313 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5084.4032 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.322 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.295 (n=612)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.394 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1447.4658` → IC=+0.303 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1447.4658 (IC base=+0.286)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.352 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.345)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.362 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.345)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.386 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.345)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.349 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.345)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.373 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.345)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.441 (n=537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.435 (n=478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.436 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.438 (n=238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.436 (n=263)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.435 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.455 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.451 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.439 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `1966.3827` → IC=+0.456 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1966.3827 (IC base=+0.439)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=62)

- **FILTRO** `py_entrada` > `0.75` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=54)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=62)

- **FILTRO** `py_entrada` > `0.75` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=54)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4919` → IC=+0.128 (n=9178)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4919 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.9834` → IC=+0.243 (n=3059)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9834 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.3798` → IC=+0.256 (n=2360)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3798 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.36` → IC=+0.190 (n=2417)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 8.36 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.8556` → IC=+0.254 (n=1691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8556 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` > `0.6161` → IC=+0.253 (n=2536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6161 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.3016` → IC=+0.229 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3016 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.3263` → IC=+0.216 (n=2887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3263 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.5694` → IC=+0.135 (n=11139)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5694 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.6013` → IC=+0.205 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6013 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.1556` → IC=+0.177 (n=3673)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1556 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.185 (n=1758)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6986 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `0.8704` → IC=+0.179 (n=2662)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.8704 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.1671` → IC=+0.225 (n=1917)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1671 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.4486` → IC=+0.199 (n=6807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4486 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.214 (n=6610)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 126.0 (IC base=+0.068)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.204 (n=684)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.179 (n=686)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0081 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.3537` → IC=+0.177 (n=2050)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3537 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=985)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.179 (n=1383)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 11.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.275 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.212` → IC=+0.273 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.212 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.211 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.174 (n=1929)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.189 (n=2078)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.04 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.242 (n=1438)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0915` → IC=+0.274 (n=537)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0915 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.242 (n=1452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0542` → IC=+0.287 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0542 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.569` → IC=+0.245 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.569 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.479` → IC=+0.241 (n=1677)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.479 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.094` → IC=+0.230 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.094 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.270 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.612` → IC=+0.243 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.612 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=1753)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1663.46` → IC=+0.248 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1663.46 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.237 (n=714)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.3538` → IC=+0.228 (n=1613)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3538 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=1695)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.219 (n=1644)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.8982` → IC=+0.261 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8982 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.1858` → IC=+0.220 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1858 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.1291` → IC=+0.222 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1291 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.529` → IC=+0.257 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.529 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.2558` → IC=+0.223 (n=1613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2558 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `1.0901` → IC=+0.224 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0901 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.240 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.4011` → IC=+0.219 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4011 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.3798` → IC=+0.238 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3798 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `11027.9657` → IC=+0.223 (n=1613)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11027.9657 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.166 (n=1102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0038 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0745` → IC=+0.163 (n=550)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0745 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=753)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.3385` → IC=+0.194 (n=1099)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3385 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.361` → IC=+0.155 (n=262)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.361 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.31` → IC=+0.144 (n=1518)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.31 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2134` → IC=+0.148 (n=1648)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2134 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.861` → IC=+0.142 (n=1098)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.861 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1566` → IC=+0.180 (n=435)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1566 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4376` → IC=+0.148 (n=1537)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4376 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.149 (n=1025)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `14054.4357` → IC=+0.140 (n=1098)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 14054.4357 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.172 (n=642)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 231.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.214 (n=686)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=2164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=1851)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.302` → IC=+0.258 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.302 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.193 (n=1800)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.202 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.1761` → IC=+0.202 (n=1312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1761 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2446)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `1918.9386` → IC=+0.188 (n=932)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1918.9386 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.221 (n=1580)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.6268` → IC=+0.215 (n=1795)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6268 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=847)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.0636` → IC=+0.240 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0636 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.695` → IC=+0.228 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.695 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.57` → IC=+0.212 (n=1944)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.57 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3474` → IC=+0.252 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3474 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.7339` → IC=+0.210 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7339 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `3.2386` → IC=+0.224 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2386 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1983.3` → IC=+0.219 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1983.3 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.212 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.211)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.158 (n=112)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=2479)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.148 (n=399)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0037 (IC base=+0.040)

- **PATRÓN** `ibs_20min` > `0.9581` → IC=+0.226 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9581 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` < `0.1947` → IC=+0.334 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1947 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.854` → IC=+0.171 (n=815)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 4.854 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.340 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.341 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.358 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.359 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4124 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `2.1835` → IC=+0.333 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1835 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.334 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.040)

- **PATRÓN** `ibs_20min` < `0.1017` → IC=+0.152 (n=648)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1017 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.6715` → IC=+0.204 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6715 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `0.6885` → IC=+0.161 (n=434)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6885 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `1.1643` → IC=+0.146 (n=329)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1643 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.205 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5223` → IC=+0.165 (n=834)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5223 (IC base=+0.023)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.176 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=373)

- **FILTRO** `ibs_20min` < `0.3056` → IC=-0.205 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3056
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=332)

- **FILTRO** `ibs_20min` > `0.2424` → IC=-0.124 (n=2485)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2424
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=1225)

- **FILTRO** `sigma_ewma_delta_pct` > `8.705` → IC=-0.209 (n=393)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.705
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3317)

- **PATRÓN** `ibs_20min` > `0.6129` → IC=+0.164 (n=221)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.6129 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `1.695` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.695 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.6571` → IC=+0.285 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6571 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `1.0233` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0233 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.4963` → IC=+0.283 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4963 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `1.4704` → IC=+0.266 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4704 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.292 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.2424` → IC=+0.129 (n=1225)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.2424 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7235` → IC=+0.250 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7235 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.4505` → IC=+0.239 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4505 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` < `0.6774` → IC=+0.276 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6774 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` > `0.8907` → IC=+0.234 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8907 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.159` → IC=+0.295 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.159 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.285 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.041)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.273 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=-0.041)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6568` → IC=-0.181 (n=644)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1933)

- **FILTRO** `ibs_20min` < `0.7222` → IC=-0.156 (n=1700)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7222
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=877)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.206 (n=579)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1998)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.210 (n=946)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=2895)

- **PATRÓN** `dist_vwap_pct` > `0.4614` → IC=+0.322 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4614 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2828` → IC=+0.317 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2828 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` < `0.9729` → IC=+0.295 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9729 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.312 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6226 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.303 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `2.4239` → IC=+0.303 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4239 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.8015` → IC=+0.299 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8015 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.5597` → IC=+0.282 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5597 (IC base=-0.018)

- **PATRÓN** `volumen_regimen` < `0.7286` → IC=+0.257 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7286 (IC base=-0.018)

- **PATRÓN** `volumen_regimen` > `1.2443` → IC=+0.288 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2443 (IC base=-0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.273 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `2.1392` → IC=+0.261 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1392 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` > `1.5239` → IC=+0.258 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5239 (IC base=-0.018)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.198 (n=3942)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0097 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4733` → IC=+0.187 (n=10550)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4733 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `1.018` → IC=+0.290 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.018 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.644` → IC=+0.158 (n=5430)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.644 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.179` → IC=+0.243 (n=4258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.179 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.6921` → IC=+0.253 (n=3803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6921 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.270 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `1.4631` → IC=+0.241 (n=2293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4631 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.6398` → IC=+0.252 (n=2293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6398 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.273 (n=6409)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.166 (n=3847)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0091 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5464` → IC=+0.156 (n=10141)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5464 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.7158` → IC=+0.249 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7158 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2496` → IC=+0.247 (n=3322)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2496 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.7103` → IC=+0.247 (n=1526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7103 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.2035` → IC=+0.256 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2035 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.304 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5933` → IC=+0.272 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5933 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.276 (n=4602)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2558` → IC=-0.152 (n=816)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2558
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=2449)

- **FILTRO** `ibs_20min` > `0.7573` → IC=-0.155 (n=668)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7573
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2008)

- **FILTRO** `sigma_ewma_delta_pct` > `4.561` → IC=-0.171 (n=609)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.561
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2067)

- **PATRÓN** `ibs_20min` > `0.8971` → IC=+0.272 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8971 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.272` → IC=+0.199 (n=585)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 7.272 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2244` → IC=+0.262 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2244 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4388` → IC=+0.198 (n=349)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4388 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.1623` → IC=+0.218 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1623 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.217 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.0951` → IC=+0.436 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0951 (IC base=-0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2235` → IC=+0.443 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2235 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4701` → IC=+0.443 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4701 (IC base=-0.021)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.469 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8659` → IC=+0.167 (n=791)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8659 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.2962` → IC=+0.183 (n=417)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2962 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6774` → IC=+0.177 (n=980)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6774 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.229 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.198 (n=359)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.397` → IC=+0.173 (n=359)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.397 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.217 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 234.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.224 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `0.863` → IC=+0.234 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.863 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2671` → IC=+0.305 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2671 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.242 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `452.0` → IC=+0.219 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 452.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.283 (n=1214)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.256 (n=1828)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.252 (n=1839)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.741` → IC=+0.281 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.741 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.0994` → IC=+0.266 (n=1553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0994 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `2.1934` → IC=+0.263 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1934 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.263 (n=2144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `1915.1184` → IC=+0.266 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.1184 (IC base=+0.251)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.314 (n=677)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.1839` → IC=+0.297 (n=657)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1839 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.325 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.3522` → IC=+0.291 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3522 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.693` → IC=+0.291 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.693 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.805` → IC=+0.287 (n=1596)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.805 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.1193` → IC=+0.290 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1193 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` < `1.5806` → IC=+0.297 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5806 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.6625` → IC=+0.292 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6625 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `1908.1032` → IC=+0.306 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1908.1032 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.288 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.285)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7744` → IC=-0.186 (n=685)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7744
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=2058)

- **PATRÓN** `ibs_20min` > `0.9092` → IC=+0.185 (n=599)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.9092 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.1824` → IC=+0.230 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1824 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.0011` → IC=+0.244 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0011 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `0.5902` → IC=+0.221 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5902 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.0834` → IC=+0.256 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0834 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4046` → IC=+0.263 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4046 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.7601` → IC=+0.235 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7601 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.255 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.1481` → IC=+0.223 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1481 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.1677` → IC=+0.216 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1677 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2772` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2772 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.8106` → IC=+0.260 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8106 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1331` → IC=+0.235 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1331 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.260 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7536` → IC=-0.185 (n=1252)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7536
  - _Potencial_: sin este filtro IC_bueno=+0.280 (n=1252)

- **FILTRO** `ibs_20min` > `0.6774` → IC=-0.234 (n=629)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6774
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=1891)

- **FILTRO** `sigma_ewma_delta_pct` > `4.71` → IC=-0.189 (n=548)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.71
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1972)

- **PATRÓN** `ibs_20min` > `0.7536` → IC=+0.280 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7536 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `0.8327` → IC=+0.326 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8327 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.69` → IC=+0.170 (n=395)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.69 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` < `0.8622` → IC=+0.307 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8622 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` > `0.639` → IC=+0.300 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.639 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.299 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.4306` → IC=+0.321 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4306 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.325 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.5773` → IC=+0.128 (n=1664)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.5773 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` < `0.2225` → IC=+0.238 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2225 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.259 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.226 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.237 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.456` → IC=+0.243 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.456 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.257 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.019)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.325 (n=1336)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.298 (n=707)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` > `0.7396` → IC=+0.321 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7396 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2171` → IC=+0.315 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2171 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.675` → IC=+0.300 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.675 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.294 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` < `0.0785` → IC=+0.283 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0785 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.327 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `1.43` → IC=+0.290 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.43 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2462.6516` → IC=+0.290 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2462.6516 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.318 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.307 (n=1058)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.1975` → IC=+0.289 (n=699)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1975 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.292 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` < `0.1364` → IC=+0.332 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1364 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.3209` → IC=+0.290 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3209 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.119` → IC=+0.303 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.119 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.284 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` > `1.2435` → IC=+0.312 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2435 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` > `0.2352` → IC=+0.332 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2352 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` < `2.4906` → IC=+0.280 (n=1420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4906 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `2.1403` → IC=+0.279 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1403 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `2409.4925` → IC=+0.284 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2409.4925 (IC base=+0.281)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.177 (n=2993)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0048 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.203 (n=2986)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.3643` → IC=+0.178 (n=7876)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3643 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=9345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.222 (n=8955)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.1755` → IC=+0.193 (n=3847)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1755 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.38` → IC=+0.252 (n=1811)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.38 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.163 (n=5953)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2089 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.63` → IC=+0.160 (n=5953)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.63 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.198 (n=1333)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.5597` → IC=+0.169 (n=3785)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5597 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6066` → IC=+0.175 (n=2867)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6066 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `1950.2802` → IC=+0.172 (n=7994)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 1950.2802 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.184 (n=7867)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 109.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.185 (n=5737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0821` → IC=+0.211 (n=2871)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0821 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=3281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.4844` → IC=+0.226 (n=8602)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4844 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.329` → IC=+0.198 (n=1446)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.329 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.157 (n=6182)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1776 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.216 (n=1245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.5576` → IC=+0.171 (n=3483)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5576 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6103` → IC=+0.172 (n=2637)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6103 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.179 (n=7566)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 109.0 (IC base=+0.170)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.229 (n=508)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.196 (n=501)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0083 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.3425` → IC=+0.215 (n=1501)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3425 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=1583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.202 (n=1013)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.904` → IC=+0.282 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.904 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.192` → IC=+0.311 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.192 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.243 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.190 (n=1398)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.207 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.241 (n=1007)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.246 (n=1020)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1861` → IC=+0.284 (n=761)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1861 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=1098)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.237 (n=1055)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.3485` → IC=+0.259 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3485 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.325` → IC=+0.247 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.325 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.232 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.259 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.258 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4231 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1557.0938` → IC=+0.247 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1557.0938 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.238 (n=449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.0719` → IC=+0.191 (n=448)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0719 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=1345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.395` → IC=+0.225 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.395 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.1973` → IC=+0.208 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1973 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.224 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `0.6929` → IC=+0.174 (n=591)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6929 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.205 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.5031` → IC=+0.181 (n=574)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5031 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `2.4674` → IC=+0.161 (n=435)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.4674 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `10668.8677` → IC=+0.167 (n=1341)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 10668.8677 (IC base=+0.160)

- **PATRÓN** `ballena_activa_n` < `382.0` → IC=+0.159 (n=1111)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 382.0 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.160 (n=1429)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2932` → IC=+0.165 (n=1429)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2932 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.140 (n=684)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.5859` → IC=+0.190 (n=1429)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5859 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.924` → IC=+0.207 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.924 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2166` → IC=+0.157 (n=1429)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2166 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.151 (n=436)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4507` → IC=+0.145 (n=1318)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4507 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.4235` → IC=+0.138 (n=1317)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4235 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `210.0` → IC=+0.168 (n=414)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 210.0 (IC base=+0.139)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.221 (n=679)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.2482` → IC=+0.221 (n=997)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2482 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.279 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2012` → IC=+0.210 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2012 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.7946` → IC=+0.204 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7946 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.7374` → IC=+0.211 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7374 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.210 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `1915.9532` → IC=+0.204 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.9532 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.235 (n=1126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1433` → IC=+0.256 (n=563)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1433 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.275 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.3521` → IC=+0.245 (n=1280)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3521 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.677` → IC=+0.253 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.677 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.251 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7484` → IC=+0.226 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7484 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `3.2847` → IC=+0.231 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2847 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.219 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1910.1836` → IC=+0.222 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.1836 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.213 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.218)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.178 (n=1267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0065 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.4327` → IC=+0.161 (n=1438)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4327 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=1501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.3549` → IC=+0.198 (n=1437)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3549 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1492` → IC=+0.178 (n=935)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1492 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.953` → IC=+0.224 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.953 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.855` → IC=+0.157 (n=959)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.855 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6208` → IC=+0.145 (n=1437)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.6208 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1012` → IC=+0.186 (n=609)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1012 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.4303` → IC=+0.156 (n=469)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4303 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.5102` → IC=+0.169 (n=469)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5102 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `5311.2129` → IC=+0.188 (n=958)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 5311.2129 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.149 (n=1375)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 157.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.158 (n=1510)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0072 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.3855` → IC=+0.147 (n=1510)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3855 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6567` → IC=+0.171 (n=1510)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6567 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.162 (n=530)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8556` → IC=+0.152 (n=1007)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8556 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.177 (n=224)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.8106` → IC=+0.140 (n=924)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8106 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.5231` → IC=+0.125 (n=462)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.5231 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `9450.9644` → IC=+0.165 (n=685)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 9450.9644 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `129.0` → IC=+0.127 (n=1164)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 129.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.159 (n=740)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0101 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=1671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.5045` → IC=+0.208 (n=1631)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5045 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.8302` → IC=+0.208 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8302 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.821` → IC=+0.255 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.821 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2087` → IC=+0.132 (n=1631)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.2087 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.0708` → IC=+0.124 (n=681)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0708 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.5431` → IC=+0.136 (n=693)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.5431 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1704)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2881.368` → IC=+0.200 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2881.368 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.140 (n=1260)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 47.0 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.163 (n=728)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0062 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1064` → IC=+0.166 (n=552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1064 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.215 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.211` → IC=+0.146 (n=1528)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.211 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.439` → IC=+0.131 (n=678)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 3.439 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.6382` → IC=+0.150 (n=553)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6382 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2289` → IC=+0.161 (n=290)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2289 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4516` → IC=+0.144 (n=501)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4516 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4248` → IC=+0.132 (n=501)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4248 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2734.1208` → IC=+0.170 (n=750)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2734.1208 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.125 (n=1444)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 52.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.225 (n=1380)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.1833` → IC=+0.207 (n=680)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1833 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=1614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.208 (n=700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.6486` → IC=+0.244 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6486 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.524` → IC=+0.211 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.524 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.3009` → IC=+0.202 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3009 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.594` → IC=+0.240 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.594 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.1991` → IC=+0.207 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1991 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.6293` → IC=+0.213 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6293 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.265 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.1464` → IC=+0.211 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1464 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.7991` → IC=+0.208 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7991 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.208 (n=1544)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2446.4744` → IC=+0.202 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2446.4744 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.230 (n=531)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0175` → IC=+0.211 (n=1061)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0175 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.230 (n=531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=742)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.02` → IC=+0.300 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.02 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `1.2367` → IC=+0.222 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2367 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.402` → IC=+0.250 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.402 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `0.6338` → IC=+0.219 (n=1590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6338 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.283 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `2.1921` → IC=+0.202 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1921 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.206 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2378.577` → IC=+0.214 (n=1421)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2378.577 (IC base=+0.209)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.187 (n=1017)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0043 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.168 (n=770)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0085 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3469` → IC=+0.168 (n=2029)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3469 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.182 (n=2099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.5124` → IC=+0.198 (n=2059)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.5124 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.6074` → IC=+0.178 (n=479)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6074 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.726` → IC=+0.188 (n=1017)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.726 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `0.871` → IC=+0.184 (n=1380)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.871 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `1.2057` → IC=+0.172 (n=690)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.2057 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.1631` → IC=+0.176 (n=627)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1631 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.173 (n=745)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.8204` → IC=+0.165 (n=1489)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8204 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.167 (n=2625)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `2682.644` → IC=+0.167 (n=2059)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2682.644 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.178 (n=2087)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 146.0 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.142 (n=1577)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0056 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.3452` → IC=+0.128 (n=2081)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3452 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=2205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.0594` → IC=+0.190 (n=789)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0594 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2241` → IC=+0.121 (n=2159)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2241 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.142 (n=588)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4434` → IC=+0.154 (n=763)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4434 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2785.0364` → IC=+0.122 (n=2112)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2785.0364 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.132 (n=982)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 28.0 (IC base=+0.113)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.179 (n=263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0029 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3302` → IC=+0.153 (n=595)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3302 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.656` → IC=+0.207 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.656 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.2838` → IC=+0.167 (n=205)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2838 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.141 (n=522)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.137` → IC=+0.152 (n=268)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.137 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.834` → IC=+0.139 (n=621)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 6.834 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.623` → IC=+0.192 (n=199)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.623 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` < `0.1546` → IC=+0.138 (n=619)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.1546 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0911` → IC=+0.153 (n=211)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0911 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.2005` → IC=+0.147 (n=511)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.2005 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.5046` → IC=+0.140 (n=518)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.5046 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=769)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `10596.8161` → IC=+0.153 (n=595)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 10596.8161 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `161.0` → IC=+0.171 (n=250)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 161.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.205 (n=249)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.2718` → IC=+0.163 (n=653)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2718 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.150 (n=704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6155` → IC=+0.179 (n=653)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6155 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.183` → IC=+0.152 (n=736)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.183 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.41` → IC=+0.151 (n=276)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.41 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.158` → IC=+0.138 (n=680)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.158 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2266` → IC=+0.145 (n=742)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2266 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.7161` → IC=+0.151 (n=663)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.7161 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.213 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1115` → IC=+0.157 (n=645)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1115 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4135` → IC=+0.144 (n=732)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4135 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `306.0` → IC=+0.151 (n=625)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 306.0 (IC base=+0.138)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.250 (n=486)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.2111` → IC=+0.221 (n=486)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2111 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.9505` → IC=+0.271 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9505 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.3803` → IC=+0.217 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3803 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.948` → IC=+0.234 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.948 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.217 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8331 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `1.1643` → IC=+0.231 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1643 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.1539` → IC=+0.253 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1539 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.4055` → IC=+0.227 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4055 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.4387` → IC=+0.244 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4387 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.121 (n=602)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0062 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.084` → IC=+0.148 (n=228)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.084 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6877` → IC=+0.139 (n=300)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6877 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.142 (n=107)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.152 (n=510)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0058 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.5405` → IC=+0.139 (n=569)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5405 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.177 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 8.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.260 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.9873` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9873 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.505` → IC=+0.186 (n=297)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.505 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.0674` → IC=+0.156 (n=501)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0674 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.7219` → IC=+0.145 (n=508)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7219 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1748` → IC=+0.163 (n=158)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1748 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.2078` → IC=+0.165 (n=249)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.2078 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=599)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2963.2526` → IC=+0.185 (n=258)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2963.2526 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.0441` → IC=+0.244 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0441 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.7083` → IC=+0.137 (n=235)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.7083 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `1.836` → IC=+0.162 (n=338)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.836 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2918.7797` → IC=+0.147 (n=242)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2918.7797 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.137 (n=483)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 40.0 (IC base=+0.095)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.174 (n=3855)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0047 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.209 (n=3856)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=12082)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.219 (n=11567)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4615 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.9305` → IC=+0.201 (n=1624)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9305 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.367` → IC=+0.244 (n=2875)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.367 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.171 (n=5170)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8803 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.200 (n=1575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.5862` → IC=+0.193 (n=3720)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5862 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `1788.16` → IC=+0.177 (n=11563)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1788.16 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.200 (n=9002)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.197 (n=4606)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.5054` → IC=+0.186 (n=10442)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.5054 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=3928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.449` → IC=+0.247 (n=9189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.449 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2507` → IC=+0.163 (n=6530)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2507 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.071` → IC=+0.205 (n=1478)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.071 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.755` → IC=+0.183 (n=10073)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.755 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.6337` → IC=+0.164 (n=2373)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6337 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.242 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6065` → IC=+0.193 (n=3227)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6065 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.201 (n=6296)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.229 (n=643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.221 (n=646)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.3604` → IC=+0.204 (n=1924)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3604 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.219 (n=920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=1307)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.332 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.352 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2285` → IC=+0.254 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2285 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.5626` → IC=+0.207 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5626 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.223 (n=1934)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.262 (n=1040)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.263 (n=1565)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1274` → IC=+0.282 (n=687)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1274 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.064` → IC=+0.305 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.064 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.369` → IC=+0.263 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.369 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.507` → IC=+0.260 (n=1636)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.507 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2841` → IC=+0.291 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2841 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.5535` → IC=+0.261 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5535 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.6294` → IC=+0.271 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6294 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=1701)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1663.76` → IC=+0.271 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1663.76 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.207 (n=620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.1128` → IC=+0.163 (n=817)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1128 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.3027` → IC=+0.205 (n=1854)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3027 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.1252` → IC=+0.188 (n=1033)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1252 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.172 (n=410)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.181` → IC=+0.157 (n=1688)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.181 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.629` → IC=+0.184 (n=619)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.629 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.0731` → IC=+0.156 (n=1632)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0731 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2672` → IC=+0.186 (n=269)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2672 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.1136` → IC=+0.162 (n=1583)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1136 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `11277.2096` → IC=+0.158 (n=1657)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 11277.2096 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `278.0` → IC=+0.175 (n=762)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 278.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.165 (n=1582)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.3231` → IC=+0.161 (n=1582)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3231 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.2861` → IC=+0.235 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2861 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6528` → IC=+0.152 (n=251)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.6528 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.534` → IC=+0.168 (n=266)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.534 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.315` → IC=+0.150 (n=1443)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.315 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.2003` → IC=+0.162 (n=1582)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2003 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1527` → IC=+0.201 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1527 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.4046` → IC=+0.156 (n=1484)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4046 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7588` → IC=+0.163 (n=989)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7588 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `413.0` → IC=+0.152 (n=1224)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 413.0 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.259 (n=629)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=1980)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=1915)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.371` → IC=+0.302 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.371 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.1328` → IC=+0.221 (n=1728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1328 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.7731` → IC=+0.229 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7731 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1919.3669` → IC=+0.226 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.3669 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.238 (n=1765)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.233 (n=1577)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.6074` → IC=+0.237 (n=1765)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6074 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.237 (n=840)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0138` → IC=+0.302 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0138 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.154` → IC=+0.279 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.154 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3403` → IC=+0.296 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3403 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7339` → IC=+0.231 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7339 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.1505` → IC=+0.240 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1505 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.244 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1909.982` → IC=+0.247 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1909.982 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.233 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.233)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.192 (n=663)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4373` → IC=+0.149 (n=1978)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4373 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=2064)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.2811` → IC=+0.186 (n=1977)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.2811 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.3665` → IC=+0.162 (n=766)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3665 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.166` → IC=+0.158 (n=811)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.166 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8705` → IC=+0.159 (n=1319)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8705 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.209 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5214` → IC=+0.149 (n=845)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5214 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.1579` → IC=+0.156 (n=870)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1579 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7641.8798` → IC=+0.236 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7641.8798 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.173 (n=621)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 73.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.172 (n=1067)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0052 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.3574` → IC=+0.143 (n=1408)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3574 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=740)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.5853` → IC=+0.197 (n=1408)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5853 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.134 (n=1398)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.298` → IC=+0.172 (n=239)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.298 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6987` → IC=+0.149 (n=704)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6987 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.221 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.444` → IC=+0.141 (n=1526)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.444 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `9690.488` → IC=+0.199 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9690.488 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.134 (n=1344)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 147.0 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.144 (n=1314)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0082 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=2027)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.4667` → IC=+0.196 (n=1971)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.4667 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0765` → IC=+0.206 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0765 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.558` → IC=+0.236 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.558 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.8911` → IC=+0.143 (n=1315)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8911 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1615` → IC=+0.123 (n=2022)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1615 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.1924` → IC=+0.132 (n=869)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.1924 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=1998)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2882.8084` → IC=+0.254 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2882.8084 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.143 (n=1551)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 52.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.182 (n=630)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0058 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1372` → IC=+0.160 (n=628)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1372 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.208 (n=1887)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2221` → IC=+0.139 (n=1556)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2221 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.463` → IC=+0.129 (n=1810)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.463 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.7154` → IC=+0.159 (n=828)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7154 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2207` → IC=+0.178 (n=293)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2207 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4366` → IC=+0.150 (n=573)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4366 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2767.152` → IC=+0.184 (n=627)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2767.152 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.133 (n=1509)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 51.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.230 (n=1742)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=2041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.213 (n=1753)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.261 (n=1748)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.2179` → IC=+0.231 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2179 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.251 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.063` → IC=+0.216 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.063 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.6419` → IC=+0.221 (n=1950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6419 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2344` → IC=+0.241 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2344 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.4984` → IC=+0.232 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4984 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=1922)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2435.6312` → IC=+0.218 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2435.6312 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.222 (n=686)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.228 (n=686)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.221 (n=1441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.264 (n=1811)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `1.2401` → IC=+0.212 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2401 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.2182` → IC=+0.213 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2182 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.876` → IC=+0.266 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.876 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.241 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.273 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `2.1818` → IC=+0.203 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1818 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.4324` → IC=+0.205 (n=1869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4324 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2385.287` → IC=+0.209 (n=1838)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2385.287 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.197 (n=1779)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 37.0 (IC base=+0.208)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=3558)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.212 (n=1180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.5113` → IC=+0.188 (n=3531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.5113 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=1335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=1622)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.9439` → IC=+0.237 (n=1177)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9439 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1763` → IC=+0.185 (n=1282)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1763 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` < `0.4678` → IC=+0.176 (n=2278)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.4678 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.212` → IC=+0.208 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.212 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `0.7072` → IC=+0.178 (n=1049)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.7072 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.8942` → IC=+0.181 (n=1589)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.8942 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.1692` → IC=+0.207 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1692 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.4541` → IC=+0.187 (n=1163)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.4541 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.8667` → IC=+0.185 (n=2324)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.8667 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2571)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2854.0182` → IC=+0.183 (n=3154)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2854.0182 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.215 (n=897)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.180 (n=2359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3854 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=940)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=1233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.1827` → IC=+0.185 (n=1181)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1827 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.6774` → IC=+0.178 (n=501)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6774 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.201` → IC=+0.169 (n=2676)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.201 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.2546` → IC=+0.163 (n=2517)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2546 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.165 (n=2445)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.222` → IC=+0.160 (n=560)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.222 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.5395` → IC=+0.167 (n=1165)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5395 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.827` → IC=+0.168 (n=1765)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.827 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=3558)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `4964.8256` → IC=+0.163 (n=2394)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4964.8256 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.164 (n=1738)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 83.0 (IC base=+0.159)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.215 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0032` → IC=+0.193 (n=399)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0032 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.0804` → IC=+0.255 (n=149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0804 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.202 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.207 (n=203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.539` → IC=+0.220 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.539 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.1349` → IC=+0.200 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1349 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.976` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.976 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.554` → IC=+0.197 (n=467)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 2.554 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` > `0.849` → IC=+0.219 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.849 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.304 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.4398` → IC=+0.222 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4398 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.6148` → IC=+0.202 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6148 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `12563.2849` → IC=+0.230 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12563.2849 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.222 (n=437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.366` → IC=+0.159 (n=994)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.366 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.198 (n=339)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 4.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.186 (n=438)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1409 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.6091` → IC=+0.151 (n=451)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6091 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.6795` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6795 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.2181` → IC=+0.145 (n=1016)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2181 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.372` → IC=+0.167 (n=973)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.372 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8869` → IC=+0.186 (n=663)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8869 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.0682` → IC=+0.172 (n=462)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0682 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.42` → IC=+0.149 (n=331)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.42 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.8256` → IC=+0.162 (n=660)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8256 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `12120.3122` → IC=+0.154 (n=888)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 12120.3122 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `706.0` → IC=+0.148 (n=948)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 706.0 (IC base=+0.145)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.209 (n=376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1516` → IC=+0.202 (n=495)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1516 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.189 (n=512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 6.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.5313` → IC=+0.196 (n=750)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5313 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.8838` → IC=+0.192 (n=375)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.8838 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.207` → IC=+0.193 (n=943)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.207 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.174` → IC=+0.192 (n=1008)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 4.174 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.7064` → IC=+0.188 (n=495)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.7064 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.184 (n=1030)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.199 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `2.4777` → IC=+0.188 (n=1102)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.4777 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `1.5229` → IC=+0.184 (n=985)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.5229 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=1123)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.213 (n=308)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.3831` → IC=+0.196 (n=800)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.3831 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.175 (n=611)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 10.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.7588` → IC=+0.170 (n=910)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7588 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.0954` → IC=+0.170 (n=909)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.0954 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.6081` → IC=+0.187 (n=199)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6081 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.376` → IC=+0.173 (n=824)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 4.376 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.6452` → IC=+0.199 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6452 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.7253` → IC=+0.166 (n=813)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.7253 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.166 (n=852)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.177 (n=382)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.1996` → IC=+0.180 (n=785)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.1996 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `7798.7113` → IC=+0.182 (n=813)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 7798.7113 (IC base=+0.164)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.172 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0109 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.172 (n=352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 3.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.147 (n=364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 14.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.246 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.2317` → IC=+0.193 (n=239)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2317 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.7086` → IC=+0.194 (n=158)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.7086 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.2801` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.2801 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7715` → IC=+0.187 (n=231)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.7715 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.155 (n=424)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3000.3223` → IC=+0.171 (n=357)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3000.3223 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.169 (n=300)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 51.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.190 (n=298)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0068 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.6689` → IC=+0.177 (n=298)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.6689 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.160 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 16.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.6782` → IC=+0.191 (n=263)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6782 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.6343` → IC=+0.225 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6343 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.639` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.639 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.281` → IC=+0.163 (n=289)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 5.281 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.3839` → IC=+0.167 (n=298)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.3839 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.218 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.6095` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.6095 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.1939` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1939 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `3191.6314` → IC=+0.197 (n=298)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3191.6314 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.203 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.159)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.169 (n=481)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.082)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.124 (n=987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 8.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.6439` → IC=+0.180 (n=890)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6439 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1429` → IC=+0.147 (n=530)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1429 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.428` → IC=+0.189 (n=233)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.428 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.199 (n=134)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.082)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.120 (n=443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0063 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.0431` → IC=+0.305 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0431 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` < `0.1862` → IC=+0.148 (n=413)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1862 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.034` → IC=+0.153 (n=142)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.034 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.09` → IC=+0.145 (n=311)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.09 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.136` → IC=+0.220 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.136 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `2.5298` → IC=+0.163 (n=307)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.5298 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` > `1.4436` → IC=+0.156 (n=274)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.4436 (IC base=+0.047)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=312)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.047)

- **PATRÓN** `libro_liquidez` > `3560.4084` → IC=+0.176 (n=109)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3560.4084 (IC base=+0.047)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.202 (n=166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.4395` → IC=+0.164 (n=343)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.4395 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1239` → IC=+0.170 (n=177)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1239 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `2.0731` → IC=+0.139 (n=267)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.0731 (IC base=+0.092)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.155 (n=169)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0043 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.0543` → IC=+0.191 (n=53)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.0543 (IC base=+0.097)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.121 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 3.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.279` → IC=+0.265 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.279 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.0682` → IC=+0.156 (n=178)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.0682 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.92` → IC=+0.199 (n=164)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 6.92 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.1357` → IC=+0.149 (n=169)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.1357 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.824` → IC=+0.149 (n=112)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.824 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.0668` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0668 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `2.0501` → IC=+0.202 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0501 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `3644.8509` → IC=+0.164 (n=105)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3644.8509 (IC base=+0.097)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6845` → IC=-0.122 (n=146)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6845
  - _Potencial_: sin este filtro IC_bueno=+0.212 (n=297)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=144)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.133 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0049 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.6845` → IC=+0.212 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6845 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.3368` → IC=+0.197 (n=130)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3368 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.74` → IC=+0.288 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.74 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2829` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2829 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `1.7588` → IC=+0.145 (n=187)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.7588 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `1133.0595` → IC=+0.151 (n=293)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1133.0595 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.1674` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1674 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` < `0.1269` → IC=+0.147 (n=117)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1269 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.256` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.256 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.558` → IC=+0.148 (n=89)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.558 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.0788` → IC=+0.136 (n=97)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.0788 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.1353` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1353 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `1.3422` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.3422 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `2.1925` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.1925 (IC base=+0.019)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.019)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0123` → IC=-0.275 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0123
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=117)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.186 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=106)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=78)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.124 (n=155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0061 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.7778` → IC=+0.181 (n=214)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.7778 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `1.0159` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 1.0159 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.076` → IC=+0.156 (n=91)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.076 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2389` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2389 (IC base=+0.059)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.163 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0066 (IC base=-0.003)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.250 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=-0.003)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.815` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.815 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.0903` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0903 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.1906` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.1906 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.4436` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.4436 (IC base=-0.003)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.365 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=180)

- **FILTRO** `dist_vwap_pct` > `0.1615` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1615
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=206)

- **FILTRO** `volumen_regimen` < `0.7251` → IC=-0.347 (n=57)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7251
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=173)

- **FILTRO** `volumen_spike_ratio` > `3.1125` → IC=-0.250 (n=38)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.1125
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=118)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.364 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=125)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=167)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=159)

- **FILTRO** `volumen_pendiente_norm` > `0.0781` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0781
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=86)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.256 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=39)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.232 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=53)

- **FILTRO** `volumen_spike_ratio` > `3.276` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.276
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=37)

- **FILTRO** `volumen_regimen` > `0.9045` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9045
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=60)

- **FILTRO** `volumen_spike_ratio` > `1.4666` → IC=-0.333 (n=22)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4666
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.389 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=51)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=47)

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.375 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=45)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=-0.220)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.405 (n=19)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=59)

- **FILTRO** `ibs_20min` < `0.125` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.125
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=60)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=53)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.169 (n=140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0058 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6472` → IC=+0.146 (n=303)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6472 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.5141` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.5141 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `1.8098` → IC=+0.123 (n=136)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.8098 (IC base=+0.085)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.123 (n=311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0059 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.192 (n=274)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1524 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.12` → IC=+0.182 (n=127)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 6.12 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.0753` → IC=+0.124 (n=115)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0753 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` < `2.5892` → IC=+0.136 (n=237)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.5892 (IC base=+0.091)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=328)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `3925.9695` → IC=+0.213 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3925.9695 (IC base=+0.091)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6599` → IC=-0.244 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6599
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=84)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.191 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0034 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.222 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.179 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.224 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1622 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.794` → IC=+0.172 (n=129)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.794 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `1.1644` → IC=+0.169 (n=143)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1644 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.8617` → IC=+0.160 (n=95)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.8617 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.1895` → IC=+0.219 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1895 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.5892` → IC=+0.219 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5892 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.181 (n=111)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `4433.8504` → IC=+0.180 (n=95)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 4433.8504 (IC base=+0.156)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.6645` → IC=-0.219 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6645
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=90)

- **FILTRO** `libro_liquidez` < `1374.2652` → IC=-0.219 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 1374.2652
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=90)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.167 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0025 (IC base=+0.016)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.126 (n=105)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0053 (IC base=+0.082)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.149 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 12.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1429 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.769` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.769 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` < `0.9961` → IC=+0.138 (n=92)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.9961 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.0745` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.0745 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `2175.2667` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2175.2667 (IC base=+0.082)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.1837` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1837
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=43)

- **FILTRO** `dist_vwap_pct` > `0.2902` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2902
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=68)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.271 (n=81)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.269 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.233 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.9583` → IC=+0.256 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9583 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` > `0.6943` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6943 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.257 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.305 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.242 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `579.6494` → IC=+0.232 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 579.6494 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.040)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `193.7` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.7 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `1.2733` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2733 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.346 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1695.0` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1695.0 (IC base=+0.289)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3583` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3583 (IC base=+0.232)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.232)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.232)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.333 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `1750.0` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1750.0 (IC base=+0.232)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `193.7` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.7 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `1.2733` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2733 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.346 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1695.0` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1695.0 (IC base=+0.289)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3583` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3583 (IC base=+0.232)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.232)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.232)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.333 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `1750.0` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1750.0 (IC base=+0.232)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.120 (n=1012)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.495 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2910.1242` → IC=+0.162 (n=288)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2910.1242 (IC base=+0.108)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.120 (n=1012)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.495 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2910.1242` → IC=+0.162 (n=288)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2910.1242 (IC base=+0.108)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `9.0` → IC=-0.175 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=81)

- **FILTRO** `py_entrada` < `0.435` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=121)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=143)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=224)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=210)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=44)

- **FILTRO** `libro_liquidez` < `10452.0502` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 10452.0502
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=47)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.133 (n=28)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=92)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2135)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=94)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=51)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=83)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=94)

- **FILTRO** `ballena_activa_n` > `555.0` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 555.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=61)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=91)

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

- **PATRÓN** `liq_usd_total` > `99462.85` → IC=+0.132 (n=93)

  - _Acción_: Kelly boost +0.66€ cuando `liq_usd_total` > 99462.85 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.159 (n=124)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.495 (IC base=+0.040)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=148)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=902)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=856)

- **FILTRO** `liq_usd_total` < `12056.79` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `liq_usd_total` < 12056.79
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9855` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `ballena_activa_n` > `142.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 142.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=499)

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
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=213)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.155 (n=82)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.019)

- **PATRÓN** `libro_liquidez` > `3983.3207` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3983.3207 (IC base=+0.019)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=706)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=706)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=430)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=430)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=191)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=191)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.127 (n=81)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=125)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=103)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=127)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=232)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=109)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=112)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=268)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=268)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=154)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.125 (n=792)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=822)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.161 (n=54)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=142)

- **PATRÓN** `py_entrada` > `0.52` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.52 (IC base=+0.007)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.46 (IC base=+0.055)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=82)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.147 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 9.0 (IC base=+0.087)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.130 (n=98)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.218 (n=37)

- **FILTRO** `profundidad_ratio` < `54.8` → IC=-0.261 (n=44)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.8
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=91)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.274 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=115)

- **FILTRO** `profundidad_ratio` < `19.0` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `profundidad_ratio` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=97)

- **PATRÓN** `py_entrada` > `0.53` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.53 (IC base=-0.033)

- **PATRÓN** `py_entrada` < `0.48` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.48 (IC base=-0.041)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.324 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=144)

- **FILTRO** `restante_min` < `3.4` → IC=-0.263 (n=57)

  - _Acción_: SKIP cuando `restante_min` < 3.4
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=119)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.200 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=138)

- **FILTRO** `lag_apertura_s` > `93.56` → IC=-0.271 (n=59)

  - _Acción_: SKIP cuando `lag_apertura_s` > 93.56
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=117)

- **FILTRO** `profundidad_ratio` < `77.2` → IC=-0.200 (n=88)

  - _Acción_: SKIP cuando `profundidad_ratio` < 77.2
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=88)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **PATRÓN** `restante_min` > `13.42` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `restante_min` > 13.42 (IC base=+0.014)

- **PATRÓN** `lag_apertura_s` < `93.77` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `lag_apertura_s` < 93.77 (IC base=+0.014)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.42` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.42 (IC base=+0.010)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.159 (n=121)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.171 (n=68)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.5 (IC base=-0.039)

- **PATRÓN** `profundidad_ratio` > `20.0` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `profundidad_ratio` > 20.0 (IC base=+0.007)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.262 (n=61)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=159)

- **FILTRO** `restante_min` < `3.26` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `restante_min` < 3.26
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=150)

- **FILTRO** `lag_apertura_s` > `102.62` → IC=-0.132 (n=74)

  - _Acción_: SKIP cuando `lag_apertura_s` > 102.62
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=146)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.166 (n=4044)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=12345)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.162 (n=4144)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=12859)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.195 (n=709)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=2165)

- **PATRÓN** `libro_liquidez` > `1563.46` → IC=+0.136 (n=1032)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1563.46 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.182 (n=716)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2219)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=731)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2340)

- **PATRÓN** `libro_liquidez` > `1789.24` → IC=+0.123 (n=998)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1789.24 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.169 (n=698)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=2170)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2224)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2359)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3099)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=411)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=402)

- **FILTRO** `libro_liquidez` < `17036.5309` → IC=-0.147 (n=230)

  - _Acción_: SKIP cuando `libro_liquidez` < 17036.5309
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=693)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ballena_activa_n` > `89.0` → IC=-0.218 (n=115)

  - _Acción_: SKIP cuando `ballena_activa_n` > 89.0
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=229)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.136 (n=42)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.032)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=11550)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=25558)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=8584)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=28524)

- **FILTRO** `ibs_7min` < `0.2679` → IC=-0.236 (n=9276)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2679
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=27832)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=12344)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=24764)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=11508)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=35525)

- **FILTRO** `ibs_7min` > `0.2917` → IC=-0.181 (n=11739)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2917
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=35294)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.141 (n=1877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4345)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.311 (n=1493)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4729)

- **FILTRO** `ibs_7min` < `0.708` → IC=-0.256 (n=2053)

  - _Acción_: SKIP cuando `ibs_7min` < 0.708
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=4169)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.178 (n=1478)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=4744)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.263 (n=2003)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=6111)

- **FILTRO** `ibs_7min` > `0.7931` → IC=-0.211 (n=2028)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7931
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6086)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.142 (n=1516)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=4861)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.252 (n=1560)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=4817)

- **FILTRO** `ibs_7min` < `0.7454` → IC=-0.196 (n=1594)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7454
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4783)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.180 (n=1584)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=4793)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=1500)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4985)

- **FILTRO** `ibs_7min` > `0.2616` → IC=-0.185 (n=1621)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2616
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4864)

- **FILTRO** `ballena_activa_n` > `149.0` → IC=-0.180 (n=1619)

  - _Acción_: SKIP cuando `ballena_activa_n` > 149.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4866)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.162 (n=1688)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=4240)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=1384)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=4544)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.243 (n=1956)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3972)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.209 (n=1433)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4495)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.246 (n=2000)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=6673)

- **FILTRO** `ibs_7min` > `0.7474` → IC=-0.178 (n=2168)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7474
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=6505)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=1981)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=4128)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.234 (n=1798)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4311)

- **FILTRO** `ibs_7min` < `0.741` → IC=-0.183 (n=1527)

  - _Acción_: SKIP cuando `ibs_7min` < 0.741
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4582)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.170 (n=1527)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4582)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.257 (n=1560)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=4727)

- **FILTRO** `ibs_7min` > `0.2745` → IC=-0.178 (n=1571)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2745
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4716)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.180 (n=1520)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4767)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.265 (n=1536)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4837)

- **FILTRO** `ibs_7min` < `0.2667` → IC=-0.235 (n=1586)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=4787)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.172 (n=2232)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=6749)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.274 (n=1420)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=4679)

- **FILTRO** `ibs_7min` < `0.2727` → IC=-0.223 (n=1524)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4575)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.214 (n=1440)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=4659)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.208 (n=1994)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=6499)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1165)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=578)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=332)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=577)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.134 (n=834)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.118)

- **PATRÓN** `total_vol_5m` < `453.526` → IC=+0.151 (n=279)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 453.526 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.125 (n=707)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 55.0 (IC base=+0.118)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4376` → IC=+0.136 (n=64)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.4376 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.232 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2571.3862` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2571.3862 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.157 (n=68)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 11.0 (IC base=+0.137)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.122 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 11.0 (IC base=+0.114)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4137` → IC=+0.189 (n=117)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio` |x|> 0.4137 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.128 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.104)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.209 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 74.0 (IC base=+0.104)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.167 (n=145)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.186 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 11.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `5032.488` → IC=+0.157 (n=97)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 5032.488 (IC base=+0.126)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.151 (n=147)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.127 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 13.0 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3584.1484` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3584.1484 (IC base=+0.102)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0046` → IC=-0.256 (n=293)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=145)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0049` → IC=-0.238 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0049
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=35)

- **FILTRO** `T_h` > `98.7549` → IC=-0.414 (n=33)

  - _Acción_: SKIP cuando `T_h` > 98.7549
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=103)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.257 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.109)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0083` → IC=-0.214 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=41)

- **FILTRO** `T_h` > `123.7153` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `T_h` > 123.7153
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=61)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0099` → IC=-0.172 (n=321)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.328 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=275)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.328 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=275)

- **FILTRO** `T_h` > `61.3189` → IC=-0.315 (n=274)

  - _Acción_: SKIP cuando `T_h` > 61.3189
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `63.9952` → IC=-0.149 (n=112)

  - _Acción_: SKIP cuando `T_h` > 63.9952
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.372 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=113)

- **FILTRO** `T_h` > `144.5168` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `T_h` > 144.5168
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=104)

- **FILTRO** `pct_vs_K` |x|> `2.9891` → IC=-0.436 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9891
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=93)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `3.4756` → IC=-0.400 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4756
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=92)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.333 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=87)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.333 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=87)

- **FILTRO** `T_h` > `57.801` → IC=-0.335 (n=77)

  - _Acción_: SKIP cuando `T_h` > 57.801
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=38)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.139 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=72)

- **FILTRO** `T_h` > `135.6166` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `T_h` > 135.6166
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=80)

- **FILTRO** `pct_vs_K` |x|> `3.8` → IC=-0.230 (n=35)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=71)

- **FILTRO** `sigma_h` > `0.0081` → IC=-0.360 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.315 (n=25)

- **FILTRO** `T_h` > `54.2531` → IC=-0.375 (n=54)

  - _Acción_: SKIP cuando `T_h` > 54.2531
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=19)

- **PATRÓN** `pct_vs_K` |x|≤ `1.0286` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.0286 (IC base=-0.046)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1357` → IC=+0.466 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1357 (IC base=+0.356)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.381 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.356)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.411 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.356)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.396 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.356)

- **PATRÓN** `dist_50` > `0.4172` → IC=+0.478 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4172 (IC base=+0.356)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.385 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.356)

- **PATRÓN** `edge` > `0.096` → IC=+0.452 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.418)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.431 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.418)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.447 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.418)

- **PATRÓN** `T_h` < `0.608` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.608 (IC base=+0.418)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.448 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.418)

- **PATRÓN** `dist_50` > `0.4085` → IC=+0.482 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4085 (IC base=+0.418)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.474 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.418)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1072` → IC=+0.449 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1072 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.400 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.452 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.417)

- **PATRÓN** `T_h` < `0.8618` → IC=+0.447 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8618 (IC base=+0.417)

- **PATRÓN** `T_h` > `0.5062` → IC=+0.397 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5062 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.4172` → IC=+0.474 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4172 (IC base=+0.417)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.409 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.429 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.474 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.448)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.474 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.448)

- **PATRÓN** `T_h` < `1.0409` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0409 (IC base=+0.448)

- **PATRÓN** `T_h` > `0.8566` → IC=+0.449 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8566 (IC base=+0.448)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.466 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.448)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.448)

- **PATRÓN** `edge` > `0.1155` → IC=+0.470 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1155 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.487 (n=74)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.463)

- **PATRÓN** `T_h` > `0.8021` → IC=+0.465 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8021 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4939` → IC=+0.487 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4939 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.468 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=214)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=317)

- **PATRÓN** `streak_estiramiento` < `0.5782` → IC=+0.145 (n=139)

  - _Acción_: Kelly boost +0.73€ cuando `streak_estiramiento` < 0.5782 (IC base=+0.032)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=22)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `2331737.7` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 2331737.7
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=48)

- **FILTRO** `streak_estiramiento` > `0.4576` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4576
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=38)

- **PATRÓN** `streak_estiramiento` < `0.4576` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.4576 (IC base=-0.008)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 49.0 (IC base=+0.056)

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
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=797)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=803)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=465)

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
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=695)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1256)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=848)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=826)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3165)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1603)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1611)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.201 (n=633)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.232 (n=633)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.1593` → IC=+0.196 (n=1670)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1593 (IC base=+0.192)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2175` → IC=+0.199 (n=633)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2175 (IC base=+0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1268` → IC=+0.233 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1268 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.201 (n=1763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.193 (n=1979)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `ibs_15` > `0.6133` → IC=+0.272 (n=1898)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6133 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.1186` → IC=+0.188 (n=957)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1186 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.791` → IC=+0.283 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.791 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `8754.682` → IC=+0.202 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8754.682 (IC base=+0.192)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=805)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.232 (n=282)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.276 (n=141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.211)

- **PATRÓN** `drift_15min` |x|≤ `0.3811` → IC=+0.220 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3811 (IC base=+0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2012` → IC=+0.242 (n=192)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2012 (IC base=+0.211)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4004` → IC=+0.247 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4004 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_15` > `0.7112` → IC=+0.277 (n=423)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7112 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.274 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.582` → IC=+0.275 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.582 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `16111.0352` → IC=+0.241 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16111.0352 (IC base=+0.211)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.418` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.418
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=489)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.173 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0035 (IC base=+0.132)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.138 (n=296)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.005 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.151 (n=196)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.173 (n=148)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1251` → IC=+0.157 (n=164)

  - _Acción_: Kelly boost +0.78€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1251 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.133 (n=445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 16.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.5788` → IC=+0.227 (n=444)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5788 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.1135` → IC=+0.149 (n=317)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1135 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.386` → IC=+0.230 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.386 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `8758.263` → IC=+0.145 (n=201)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 8758.263 (IC base=+0.132)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=136)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.282 (n=76)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1481` → IC=+0.203 (n=200)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1481 (IC base=+0.179)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0561` → IC=+0.191 (n=228)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.0561 (IC base=+0.179)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3249` → IC=+0.227 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3249 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_15` > `0.5926` → IC=+0.265 (n=228)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5926 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1223` → IC=+0.192 (n=128)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1223 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.263` → IC=+0.400 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.263 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.180 (n=251)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `3074.7539` → IC=+0.274 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3074.7539 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.213 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.179)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.6755` → IC=-0.161 (n=107)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6755
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=1220)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.781` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.781 (IC base=-0.015)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0234` → IC=+0.287 (n=162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0234 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.227 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.198)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0403` → IC=+0.200 (n=485)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0403 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0815` → IC=+0.258 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0815 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.5728` → IC=+0.286 (n=485)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5728 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.3602` → IC=+0.209 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3602 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.04` → IC=+0.226 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.04 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.318` → IC=+0.198 (n=441)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 7.318 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2914.5894` → IC=+0.281 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2914.5894 (IC base=+0.198)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.143 (n=545)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.72€ cuando `ibs_15` < 0.1176 (IC base=+0.055)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.353 (n=311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.351)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.380 (n=156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.351)

- **PATRÓN** `drift_60min` |x|≤ `0.1114` → IC=+0.353 (n=311)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1114 (IC base=+0.351)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1462` → IC=+0.375 (n=310)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1462 (IC base=+0.351)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.388 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.351)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.370 (n=474)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.351)

- **PATRÓN** `ibs_15` > `0.7873` → IC=+0.389 (n=466)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7873 (IC base=+0.351)

- **PATRÓN** `dist_vwap_pct` > `0.4248` → IC=+0.387 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4248 (IC base=+0.351)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.363 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.351)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.350 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.351)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.354 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.351)

- **PATRÓN** `libro_liquidez` > `3820.3005` → IC=+0.369 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3820.3005 (IC base=+0.351)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.363 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.357)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.374 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.357)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.364 (n=86)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.357)

- **PATRÓN** `drift_15min` |x|≤ `0.4175` → IC=+0.370 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4175 (IC base=+0.357)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.368 (n=256)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.357)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1241` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1241 (IC base=+0.357)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.381 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.357)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.387 (n=255)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.357)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.397 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.859` → IC=+0.364 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.859 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.358 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.357)

- **PATRÓN** `libro_liquidez` > `11281.6823` → IC=+0.372 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11281.6823 (IC base=+0.357)

- **PATRÓN** `ballena_activa_n` < `568.0` → IC=+0.400 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 568.0 (IC base=+0.357)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.379 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.341)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.353 (n=141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.341)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0842` → IC=+0.359 (n=189)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0842 (IC base=+0.341)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.371 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.341)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.402 (n=100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.341)

- **PATRÓN** `ibs_15` > `0.7485` → IC=+0.392 (n=211)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7485 (IC base=+0.341)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.379 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.341)

- **PATRÓN** `dist_vwap_pct` < `0.1186` → IC=+0.346 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1186 (IC base=+0.341)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.357 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.341)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.343 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.341)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `4304.5454` → IC=+0.363 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4304.5454 (IC base=+0.341)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.225 (n=739)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=2219)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=1020)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1938)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1365` → IC=+0.235 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1365 (IC base=-0.065)

- **PATRÓN** `ibs_15` > `0.6429` → IC=+0.271 (n=722)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6429 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.266` → IC=+0.192 (n=588)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.266 (IC base=-0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1219` → IC=+0.251 (n=1420)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1219 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1797` → IC=+0.248 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1797 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.3469` → IC=+0.277 (n=2130)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3469 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.6808` → IC=+0.295 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6808 (IC base=-0.025)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.242 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=-0.025)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.216 (n=449)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1348)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.221 (n=449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1348)

- **FILTRO** `sigma_ewma_delta_pct` > `23.552` → IC=-0.255 (n=251)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.552
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1546)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.161 (n=175)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0028 (IC base=+0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2011` → IC=+0.278 (n=97)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2011 (IC base=+0.085)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.085)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.123 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 12.0 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.7533` → IC=+0.328 (n=213)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7533 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1267` → IC=+0.294 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1267 (IC base=+0.085)

- **PATRÓN** `ibs_15` < `0.199` → IC=+0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.199 (IC base=-0.194)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.194)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=441)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.150 (n=344)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0066 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.167 (n=307)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.004 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.208 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.146)

- **PATRÓN** `drift_15min` |x|≤ `0.4133` → IC=+0.167 (n=115)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.4133 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0609` → IC=+0.145 (n=345)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio_macro` |x|> 0.0609 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.220 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.171 (n=247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.6625` → IC=+0.257 (n=344)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6625 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.176 (n=248)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.1` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 23.1 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=441)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `10584.3604` → IC=+0.183 (n=156)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 10584.3604 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.248 (n=831)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.4445` → IC=+0.239 (n=831)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4445 (IC base=+0.233)

- **PATRÓN** `drift_15min` |x|≤ `0.7857` → IC=+0.246 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7857 (IC base=+0.233)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2081` → IC=+0.252 (n=377)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2081 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.242 (n=320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.233)

- **PATRÓN** `ibs_15` < `0.2735` → IC=+0.276 (n=731)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2735 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.7574` → IC=+0.312 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7574 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.074` → IC=+0.269 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.074 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.411` → IC=+0.237 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.411 (IC base=+0.233)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.231 (n=236)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=461)

- **FILTRO** `drift_15min` |x|> `0.9048` → IC=-0.267 (n=174)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9048
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=523)

- **PATRÓN** `ibs_15` > `0.9167` → IC=+0.309 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9167 (IC base=-0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0771` → IC=+0.235 (n=322)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0771 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.183` → IC=+0.225 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.183 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.267 (n=363)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.7364` → IC=+0.247 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7364 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.1775` → IC=+0.231 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1775 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.230 (n=582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=251)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.268 (n=226)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=607)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1385` → IC=+0.298 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1385 (IC base=-0.037)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1053` → IC=+0.331 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1053 (IC base=-0.037)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.305 (n=542)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.8999` → IC=+0.340 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8999 (IC base=-0.037)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.302 (n=504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0533` → IC=+0.323 (n=252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0533 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2394` → IC=+0.303 (n=252)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2394 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2227` → IC=+0.321 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2227 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.312 (n=792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8408` → IC=+0.327 (n=756)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8408 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.436` → IC=+0.336 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.436 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.349 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `13022.3239` → IC=+0.297 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13022.3239 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.300 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.330 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.286)

- **PATRÓN** `drift_15min` |x|≤ `0.4185` → IC=+0.289 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4185 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2556` → IC=+0.308 (n=139)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2556 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3977` → IC=+0.310 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3977 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.318 (n=416)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.4139` → IC=+0.356 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4139 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.363 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16163.1166` → IC=+0.323 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16163.1166 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.304 (n=299)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0525` → IC=+0.310 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0525 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1481` → IC=+0.295 (n=227)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1481 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.326 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.322 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.339 (n=340)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.308 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.335 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.295 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.293)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2527` → IC=-0.162 (n=72)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2527
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=220)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.138 (n=194)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=66)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.167 (n=112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=338)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.197 (n=64)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=125)

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
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=115)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1259` → IC=-0.167 (n=43)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1259
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=131)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1819` → IC=-0.260 (n=23)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1819
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

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
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0943` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0943
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.210 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

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
- **PATRÓN** `T_h` > `79.3918` → IC=+0.218 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 79.3918 (IC base=+0.206)

- **PATRÓN** `ratio` < `0.9771` → IC=+0.469 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9771 (IC base=+0.206)

- **PATRÓN** `T_h` > `145.7579` → IC=+0.393 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7579 (IC base=+0.333)

- **PATRÓN** `ratio` > `1.0098` → IC=+0.302 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0098 (IC base=+0.333)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.3604` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 144.3604 (IC base=+0.184)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.466 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.184)

- **PATRÓN** `T_h` > `103.3918` → IC=+0.295 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.284)

- **PATRÓN** `ratio` > `1.0466` → IC=+0.352 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0466 (IC base=+0.284)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `79.3918` → IC=+0.267 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 79.3918 (IC base=+0.242)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.422 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.242)

- **PATRÓN** `T_h` > `106.9024` → IC=+0.330 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 106.9024 (IC base=+0.314)

- **PATRÓN** `ratio` > `1.015` → IC=+0.341 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.015 (IC base=+0.314)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1332` → IC=+0.459 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1332 (IC base=+0.402)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6133 sube el IC de +0.192 a +0.272 en UPDOWN_GBM#15min (n=1898). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7112 sube el IC de +0.211 a +0.277 en UPDOWN_GBM#BTC#15min (n=423). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5788 sube el IC de +0.132 a +0.227 en UPDOWN_GBM#ETH#15min (n=444). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5926 sube el IC de +0.179 a +0.265 en UPDOWN_GBM#SOL#15min (n=228). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5728 sube el IC de +0.198 a +0.286 en UPDOWN_GBM#XRP#15min (n=485). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6429 sube el IC de -0.065 a +0.271 en UPDOWN_GBM_15M_TARDIO (n=722). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3469 sube el IC de -0.025 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=2130). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.085 a +0.328 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=213). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.199 sube el IC de -0.194 a +0.382 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6625 sube el IC de +0.146 a +0.257 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=344). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2735 sube el IC de +0.233 a +0.276 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=731). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9167 sube el IC de -0.172 a +0.309 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.039 a +0.267 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=363). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.037 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=542). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8408 sube el IC de +0.290 a +0.327 en UPDOWN_GBM_IBS_ALTO (n=756). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.286 a +0.318 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=416). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.293 a +0.339 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=340). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7873 sube el IC de +0.351 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=466). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.357 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=255). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7485 sube el IC de +0.341 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=211). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.105 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.105 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH#15min` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1423 | +0.101 | +206.94€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1423 | +0.101 | +206.94€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1077 | +0.111 | +178.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1077 | +0.111 | +178.08€ | 2 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 4 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 30803 | -0.085 | -4093.48€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1606 | -0.024 | -214.25€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 29197 | -0.089 | -3879.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4012 | -0.103 | -678.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4012 | -0.103 | -678.00€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1606 | -0.024 | -214.25€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1606 | -0.024 | -214.25€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3598 | -0.099 | -805.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3598 | -0.099 | -805.52€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8004 | -0.017 | -784.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8004 | -0.017 | -784.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7559 | -0.092 | -474.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7559 | -0.092 | -474.86€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6024 | -0.164 | -1136.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6024 | -0.164 | -1136.55€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 21915 | -0.023 | +3800.60€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5679 | +0.001 | +1773.71€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 16236 | -0.031 | +2026.89€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 21915 | -0.023 | +3800.60€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5679 | +0.001 | +1773.71€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 16236 | -0.031 | +2026.89€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 104374 | +0.113 | -5066.36€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15174 | +0.184 | -466.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 433 | -0.066 | -55.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 82154 | +0.101 | -4304.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6613 | +0.106 | -239.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 13650 | +0.101 | -1041.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 49 | -0.147 | +8.51€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 13586 | +0.102 | -1038.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 20927 | +0.131 | -404.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4695 | +0.200 | -142.55€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 13625 | +0.114 | -193.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2565 | +0.097 | -45.74€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 13696 | +0.090 | -1216.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 56 | -0.103 | -7.23€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 13625 | +0.092 | -1198.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 22161 | +0.124 | -417.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5979 | +0.176 | -80.07€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 13773 | +0.105 | -269.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2397 | +0.100 | -58.56€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 20273 | +0.114 | -1166.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4344 | +0.187 | -256.10€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 336 | -0.027 | -1.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 13942 | +0.092 | -773.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1651 | +0.130 | -135.11€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 13667 | +0.099 | -820.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 51 | -0.028 | +11.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 13603 | +0.100 | -831.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 16600 | +0.194 | -1039.25€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 16600 | +0.194 | -1039.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3898 | +0.171 | -383.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3898 | +0.171 | -383.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1601 | +0.204 | -10.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1601 | +0.204 | -10.47€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3845 | +0.181 | -315.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3845 | +0.181 | -315.46€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3392 | +0.242 | -107.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3392 | +0.242 | -107.83€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3785 | +0.191 | -235.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3785 | +0.191 | -235.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 780 | +0.431 | -19.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 780 | +0.431 | -19.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 305 | +0.441 | -0.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 305 | +0.441 | -0.66€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 297 | +0.430 | -7.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 297 | +0.430 | -7.69€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 166 | +0.411 | -9.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 166 | +0.411 | -9.18€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 57467 | +0.198 | -4452.41€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 57467 | +0.198 | -4452.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9897 | +0.178 | -1113.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9897 | +0.178 | -1113.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9202 | +0.222 | -350.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9202 | +0.222 | -350.26€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 9918 | +0.175 | -1144.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 9918 | +0.175 | -1144.51€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9290 | +0.218 | -373.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9290 | +0.218 | -373.81€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9517 | +0.203 | -629.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9517 | +0.203 | -629.36€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9643 | +0.192 | -841.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9643 | +0.192 | -841.44€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 21803 | +0.116 | +121.92€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 21803 | +0.116 | +121.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 10825 | +0.119 | +109.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 10825 | +0.119 | +109.36€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 10978 | +0.112 | +12.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 10978 | +0.112 | +12.57€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1613 | +0.288 | -28.48€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1613 | +0.288 | -28.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 720 | +0.278 | -18.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 720 | +0.278 | -18.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 779 | +0.286 | -12.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 779 | +0.286 | -12.87€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 114 | +0.345 | +3.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 114 | +0.345 | +3.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 716 | +0.436 | -3.81€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 716 | +0.436 | -3.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 343 | +0.433 | -4.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 343 | +0.433 | -4.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 328 | +0.439 | +0.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 328 | +0.439 | +0.01€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 45 | +0.394 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 45 | +0.394 | +0.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1236 | +0.065 | -67.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 437 | +0.051 | -40.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 799 | +0.073 | -26.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 64 | +0.121 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 64 | +0.121 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 975 | +0.071 | -36.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 176 | +0.062 | -10.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 799 | +0.073 | -26.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 197 | +0.018 | -34.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 197 | +0.018 | -34.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 41167 | +0.098 | -1180.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3372 | +0.088 | +20.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 37795 | +0.099 | -1200.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 22951 | +0.102 | -337.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3372 | +0.088 | +20.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 19579 | +0.105 | -357.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 7969 | +0.109 | -23.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 7969 | +0.109 | -23.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 10247 | +0.081 | -818.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 10247 | +0.081 | -818.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 854 | +0.211 | -101.94€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 854 | +0.211 | -101.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 854 | +0.211 | -101.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 854 | +0.211 | -101.94€ | 2 | 4 |
| ✅ GBM_LATE_15M | 29111 | +0.086 | +14256.89€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 29111 | +0.086 | +14256.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4877 | +0.199 | +3684.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4877 | +0.199 | +3684.78€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 4346 | +0.178 | +3106.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4346 | +0.178 | +3106.87€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 5134 | +0.199 | +3841.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5134 | +0.199 | +3841.47€ | 0 | 23 |
| ✅ GBM_LATE_15M#ETH | 4184 | +0.029 | +1015.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4184 | +0.029 | +1015.72€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 4152 | -0.032 | +934.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4152 | -0.032 | +934.87€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 6418 | -0.039 | +1673.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6418 | -0.039 | +1673.20€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 31108 | +0.087 | +16506.51€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 31108 | +0.087 | +16506.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5941 | +0.014 | +3106.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5941 | +0.014 | +3106.09€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6479 | +0.016 | +1375.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6479 | +0.016 | +1375.48€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4418 | +0.267 | +4524.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4418 | +0.267 | +4524.00€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5136 | +0.008 | +1048.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5136 | +0.008 | +1048.55€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5024 | +0.033 | +1998.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5024 | +0.033 | +1998.55€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4110 | +0.280 | +4453.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4110 | +0.280 | +4453.84€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 23400 | +0.170 | +17858.53€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 23400 | +0.170 | +17858.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3522 | +0.212 | +2876.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3522 | +0.212 | +2876.65€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3693 | +0.149 | +2707.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3693 | +0.149 | +2707.85€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3699 | +0.209 | +2966.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3699 | +0.209 | +2966.33€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3929 | +0.134 | +2817.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3929 | +0.134 | +2817.90€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4378 | +0.120 | +3161.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4378 | +0.120 | +3161.81€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4179 | +0.205 | +3327.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4179 | +0.205 | +3327.99€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6225 | +0.137 | +2889.69€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6225 | +0.137 | +2889.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 214 | +0.111 | +95.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 214 | +0.111 | +95.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1782 | +0.138 | +914.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1782 | +0.138 | +914.74€ | 0 | 29 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1880 | +0.152 | +910.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1880 | +0.152 | +910.63€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1469 | +0.117 | +576.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1469 | +0.117 | +576.39€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 29339 | +0.178 | +22370.54€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 29339 | +0.178 | +22370.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4644 | +0.227 | +4044.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4644 | +0.227 | +4044.65€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4581 | +0.151 | +3040.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4581 | +0.151 | +3040.97€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4868 | +0.226 | +4203.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4868 | +0.226 | +4203.35€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4768 | +0.135 | +3300.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4768 | +0.135 | +3300.94€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5136 | +0.119 | +3475.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5136 | +0.119 | +3475.47€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5342 | +0.210 | +4305.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5342 | +0.210 | +4305.15€ | 0 | 25 |
| ✅ GBM_LATE_5M | 8280 | +0.169 | +5417.01€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 8280 | +0.169 | +5417.01€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 825 | +0.226 | +709.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 825 | +0.226 | +709.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1918 | +0.160 | +1358.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1918 | +0.160 | +1358.45€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2710 | +0.174 | +1768.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2710 | +0.174 | +1768.16€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 873 | +0.153 | +489.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 873 | +0.153 | +489.73€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2039 | +0.072 | +764.02€ | 0 | 16 |
| ✅ GBM_LATE_60M#60min | 2039 | +0.072 | +764.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 754 | +0.094 | +275.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 754 | +0.094 | +275.51€ | 0 | 16 |
| ✅ GBM_LATE_60M#ETH | 663 | +0.073 | +302.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 663 | +0.073 | +302.30€ | 2 | 17 |
| ✅ GBM_LATE_60M#SOL | 622 | +0.043 | +186.21€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 622 | +0.043 | +186.21€ | 3 | 11 |
| 🚫 GBM_LATE_60M_FADE | 419 | -0.248 | -16.42€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 419 | -0.248 | -16.42€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 157 | -0.217 | -4.98€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 157 | -0.217 | -4.98€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 140 | -0.246 | -4.87€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 140 | -0.246 | -4.87€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 122 | -0.282 | -6.57€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 122 | -0.282 | -6.57€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 817 | +0.088 | +199.98€ | 0 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 817 | +0.088 | +199.98€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 315 | +0.080 | +66.79€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 315 | +0.080 | +66.79€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 259 | +0.052 | +26.42€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 259 | +0.052 | +26.42€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 243 | +0.137 | +106.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 243 | +0.137 | +106.77€ | 2 | 12 |
| ✅ LATE_WINDOW_5MIN | 109 | +0.266 | +95.86€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 109 | +0.266 | +95.86€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 109 | +0.266 | +95.86€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 109 | +0.266 | +95.86€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2341 | +0.105 | +638.01€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2341 | +0.105 | +638.01€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2341 | +0.105 | +638.01€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2341 | +0.105 | +638.01€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 404 | -0.076 | -34.19€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 404 | -0.076 | -34.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 105 | -0.051 | -4.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 105 | -0.051 | -4.32€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 150 | -0.026 | -5.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 150 | -0.026 | -5.05€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2335 | +0.016 | +40.59€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2335 | +0.016 | +40.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 121 | +0.012 | -3.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 121 | +0.012 | -3.49€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 307 | +0.015 | +17.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 307 | +0.015 | +17.08€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 176 | -0.022 | -5.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 176 | -0.022 | -5.35€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 950 | +0.026 | +26.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 950 | +0.026 | +26.01€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 539 | +0.014 | +1.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 539 | +0.014 | +1.94€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 242 | +0.008 | +4.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 242 | +0.008 | +4.40€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1231 | -0.043 | -26.03€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1231 | -0.043 | -26.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 348 | -0.040 | -12.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 348 | -0.040 | -12.51€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 416 | -0.026 | -0.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 416 | -0.026 | -0.49€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 467 | -0.059 | -13.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 467 | -0.059 | -13.03€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 3063 | -0.015 | +72.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1451 | -0.017 | +28.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1612 | -0.014 | +44.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 86 | +0.023 | +9.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 45 | +0.074 | +11.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 41 | -0.035 | -2.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 727 | +0.002 | +38.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 340 | +0.003 | +13.83€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 387 | +0.001 | +25.02€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 363 | -0.018 | +11.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 173 | -0.043 | -3.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 190 | +0.005 | +15.29€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 607 | -0.037 | -22.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 279 | -0.037 | -12.09€ | 4 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 328 | -0.036 | -10.83€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 592 | -0.013 | +22.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 289 | -0.015 | +13.31€ | 0 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 303 | -0.011 | +8.94€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 688 | -0.020 | +13.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 325 | -0.020 | +5.81€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 363 | -0.021 | +8.12€ | 3 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 33392 | -0.005 | +1497.81€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 33392 | -0.005 | +1497.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5909 | +0.021 | +746.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5909 | +0.021 | +746.58€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5067 | -0.032 | -84.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5067 | -0.032 | -84.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6006 | +0.017 | +538.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6006 | +0.017 | +538.06€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4850 | -0.054 | -166.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4850 | -0.054 | -166.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5626 | -0.010 | +203.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5626 | -0.010 | +203.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5934 | +0.011 | +260.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5934 | +0.011 | +260.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6041 | -0.060 | -152.08€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6041 | -0.060 | -152.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1457 | -0.085 | -42.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1457 | -0.085 | -42.13€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 686 | -0.125 | -32.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 686 | -0.125 | -32.13€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1783 | -0.078 | -33.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1783 | -0.078 | -33.60€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 854 | -0.015 | -25.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 854 | -0.015 | -25.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3347 | +0.004 | -3.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3347 | +0.004 | -3.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1317 | +0.006 | +6.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1317 | +0.006 | +6.68€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 84141 | -0.073 | +1732.31€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 84141 | -0.073 | +1732.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 14336 | -0.076 | +831.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 14336 | -0.076 | +831.97€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 12862 | -0.095 | -678.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 12862 | -0.095 | -678.06€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 14601 | -0.067 | +765.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 14601 | -0.067 | +765.03€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 12396 | -0.092 | -221.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 12396 | -0.092 | -221.22€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 15354 | -0.049 | +367.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 15354 | -0.049 | +367.44€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 14592 | -0.063 | +667.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 14592 | -0.063 | +667.14€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7859 | -0.028 | -134.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7859 | -0.028 | -134.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1804 | -0.036 | -12.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1804 | -0.036 | -12.45€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2225 | -0.023 | -26.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2225 | -0.023 | -26.95€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1066 | -0.045 | -19.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1066 | -0.045 | -19.44€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 765 | -0.021 | -24.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 765 | -0.021 | -24.46€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1248 | +0.111 | +438.07€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1112 | +0.118 | +425.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 254 | +0.137 | +126.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 254 | +0.137 | +126.26€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 213 | +0.114 | +65.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 213 | +0.114 | +65.22€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 233 | +0.104 | +84.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 233 | +0.104 | +84.73€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 193 | +0.126 | +84.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 193 | +0.126 | +84.33€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 219 | +0.102 | +64.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 219 | +0.102 | +64.94€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 673 | -0.042 | -50.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 673 | -0.042 | -50.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 135 | +0.004 | +6.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 135 | +0.004 | +6.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 95 | -0.077 | -14.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 95 | -0.077 | -14.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 193 | -0.054 | -21.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 193 | -0.054 | -21.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 138 | -0.029 | -7.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 138 | -0.029 | -7.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 112 | -0.061 | -12.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 112 | -0.061 | -12.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 632 | -0.107 | -54.19€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 289 | -0.156 | -66.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 236 | -0.193 | -67.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 53 | +0.009 | +0.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 220 | -0.072 | -0.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 170 | -0.076 | -6.56€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 50 | -0.058 | +6.23€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 123 | -0.052 | +12.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 99 | -0.074 | +6.55€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 24 | +0.038 | +6.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 505 | -0.131 | -67.40€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 127 | -0.012 | +13.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 794 | -0.200 | -34.62€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 329 | -0.198 | -28.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 288 | -0.197 | -29.11€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 41 | -0.198 | +0.21€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 270 | -0.217 | -25.15€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 235 | -0.226 | -30.24€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 35 | -0.149 | +5.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 195 | -0.175 | +19.42€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 179 | -0.174 | +14.75€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 702 | -0.202 | -44.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 92 | -0.181 | +9.98€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 338 | +0.403 | +260.58€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 36 | +0.105 | -1.22€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 36 | +0.105 | -1.22€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 86 | +0.364 | +71.63€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 86 | +0.364 | +71.63€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 216 | +0.463 | +190.17€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 216 | +0.463 | +190.17€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 338 | +0.403 | +260.58€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 569 | +0.032 | +17.26€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 569 | +0.032 | +17.26€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 277 | +0.030 | +3.93€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 277 | +0.030 | +3.93€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 61 | -0.008 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 61 | -0.008 | -1.63€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 194 | +0.036 | +11.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 194 | +0.036 | +11.78€ | 2 | 3 |
| ✅ STREAK_FADE_5M | 2947 | -0.021 | -117.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2947 | -0.021 | -117.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 896 | -0.020 | -30.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 896 | -0.020 | -30.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 573 | -0.024 | -23.73€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 573 | -0.024 | -23.73€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1322 | -0.019 | -48.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1322 | -0.019 | -48.68€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 77 | -0.044 | -5.84€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 77 | -0.044 | -5.84€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 39 | +0.012 | -1.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 39 | +0.012 | -1.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 8839 | +0.022 | +120.21€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8839 | +0.022 | +120.21€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2438 | +0.024 | +32.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2438 | +0.024 | +32.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2007 | +0.031 | +51.43€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2007 | +0.031 | +51.43€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2678 | +0.013 | +7.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2678 | +0.013 | +7.20€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1716 | +0.022 | +29.54€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1716 | +0.022 | +29.54€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7982 | +0.014 | -34.94€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7982 | +0.014 | -34.94€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3184 | +0.017 | -5.64€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3184 | +0.017 | -5.64€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3163 | +0.014 | -14.83€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3163 | +0.014 | -14.83€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1635 | +0.006 | -14.47€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1635 | +0.006 | -14.47€ | 2 | 0 |
| ✅ UPDOWN_GBM | 45792 | +0.037 | +3033.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 11873 | +0.073 | +2277.53€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1607 | +0.004 | +6.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 29374 | +0.028 | +725.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2768 | +0.002 | +23.97€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4625 | +0.075 | +574.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 841 | +0.162 | +373.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3751 | +0.056 | +201.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 8814 | +0.045 | +675.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1552 | +0.088 | +356.51€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 431 | +0.013 | +4.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 5515 | +0.046 | +281.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1252 | +0.004 | +31.37€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 64 | -0.091 | +0.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 5272 | +0.043 | +351.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 797 | +0.141 | +288.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4447 | +0.025 | +64.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 10046 | +0.026 | +445.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3006 | +0.051 | +345.06€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 424 | +0.007 | +7.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 5624 | +0.021 | +96.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 936 | -0.001 | -8.44€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 56 | -0.121 | +3.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 10370 | +0.017 | +291.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2855 | +0.028 | +206.18€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 415 | -0.004 | -1.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6472 | +0.016 | +88.99€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 580 | +0.003 | +1.05€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 48 | -0.160 | -3.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 6663 | +0.041 | +697.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2822 | +0.087 | +707.90€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 276 | +0.000 | -3.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3565 | +0.007 | -7.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 168 | -0.123 | +1.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 621 | +0.351 | +209.10€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 621 | +0.351 | +209.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 340 | +0.357 | +113.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 340 | +0.357 | +113.04€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 281 | +0.341 | +96.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 281 | +0.341 | +96.06€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 13597 | -0.034 | +2999.12€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 13597 | -0.034 | +2999.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 941 | -0.049 | +373.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 941 | -0.049 | +373.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2494 | -0.116 | +55.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2494 | -0.116 | +55.19€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 500 | +0.197 | +369.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 500 | +0.197 | +369.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1565 | +0.208 | +951.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1565 | +0.208 | +951.46€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4068 | -0.062 | +593.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4068 | -0.062 | +593.26€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4029 | -0.072 | +656.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4029 | -0.072 | +656.12€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 157 | +0.035 | +7.28€ | 1 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 157 | +0.035 | +7.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 157 | +0.035 | +7.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 157 | +0.035 | +7.28€ | 1 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1007 | +0.290 | +806.59€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1007 | +0.290 | +806.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 554 | +0.286 | +422.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 554 | +0.286 | +422.99€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 453 | +0.293 | +383.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 453 | +0.293 | +383.60€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 742 | -0.112 | -82.95€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 742 | -0.112 | -82.95€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 220 | -0.081 | -16.26€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 220 | -0.081 | -16.26€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 73 | -0.193 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 73 | -0.193 | -7.31€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2643 | +0.302 | +1285.15€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 927 | +0.254 | +133.10€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1002 | +0.292 | +425.04€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 714 | +0.377 | +727.01€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.055) — sin ventaja clara. oversold(IBS<0.3): IC=+0.049 n=16120 | neutral: IC=+0.036 n=17030 | overbought(IBS>0.7): IC=+0.090 n=16373
  - _Datos_: n=51312 IC=+0.059 PNL=+6517.80€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 576 celda(s) pasan gate riguroso completo de 2343 evaluadas (n>=40) y 3316 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.028 < 0.08 — monitorear
  - _Datos_: n=2855 IC=+0.028 PNL=+206.18€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1002/15 IC=+0.292 PNL=+425.04€ | BTC: n=927/15 IC=+0.254 PNL=+133.10€ | SOL: n=714/15 IC=+0.377 PNL=+727.01€

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
  - _Estado_: 45730 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.130 n=411/60 | contraria IC=+0.176 n=387 | gap=-0.047 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=334, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 193 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=936/40 IC=-0.001 PNL=-8.44€ | BTC#60min: n=1252/40 IC=+0.004 PNL=+31.37€ | SOL#60min: n=580/40 IC=+0.003 PNL=+1.05€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=383908 | tras_1loss IC=+0.084 n=296386 | tras_2loss IC=+0.053 n=123344/40 | gap=-0.004 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.018 n=5592 | contrario_BTC IC=+0.035 n=4950/40 | gap=+0.017 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.08 con n=399 PNL=+285.45€
  - _Datos_: n=399 IC=+0.206 PNL=+285.45€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.08 con n=443 PNL=+328.42€
  - _Datos_: n=443 IC=+0.210 PNL=+328.42€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.245 > 0.08 con n=45 PNL=+34.88€
  - _Datos_: n=45 IC=+0.245 PNL=+34.88€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.329 > 0.1 con n=2159 PNL=+1171.19€
  - _Datos_: n=2159 IC=+0.329 PNL=+1171.19€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=363 IC=+0.067 PNL=+40.55€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=363 IC=+0.067 PNL=+40.55€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=57 IC=+0.178 PNL=+35.97€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=57 IC=+0.178 PNL=+35.97€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=43779 IC=+0.036 PNL=+2895.49€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=43779 IC=+0.036 PNL=+2895.49€

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
  - _Estado_: n=1909 IC=+0.004 PNL=-3.91€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1909 IC=+0.004 PNL=-3.91€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=859 IC=-0.003 PNL=+27.89€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=859 IC=-0.003 PNL=+27.89€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=587 IC=+0.026 PNL=+31.61€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=587 IC=+0.026 PNL=+31.61€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.192 > 0.1 con n=2530 PNL=+1654.14€
  - _Datos_: n=2530 IC=+0.192 PNL=+1654.14€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1454 IC=+0.055 PNL=+105.17€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1454 IC=+0.055 PNL=+105.17€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1552 IC=+0.088 PNL=+356.51€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1552 IC=+0.088 PNL=+356.51€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.089 > 0.08 con n=6761 PNL=+1698.12€
  - _Datos_: n=6761 IC=+0.089 PNL=+1698.12€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=182 IC=-0.255 PNL=-8.23€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=182 IC=-0.255 PNL=-8.23€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=302 IC=-0.036 PNL=-3.76€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=302 IC=-0.036 PNL=-3.76€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=634 IC=+0.022 PNL=+44.99€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=634 IC=+0.022 PNL=+44.99€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=68 IC=+0.057 PNL=+4.37€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=68 IC=+0.057 PNL=+4.37€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=6213 IC=-0.000 PNL=+3.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6213 IC=-0.000 PNL=+3.32€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.266 n=109) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=109 IC=+0.266 PNL=+95.86€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=8380 IC=+0.040 PNL=+552.32€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=8380 IC=+0.040 PNL=+552.32€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=2821 IC=+0.057 PNL=+348.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2821 IC=+0.057 PNL=+348.44€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.114 > 0.08 con n=397 PNL=+126.36€
  - _Datos_: n=397 IC=+0.114 PNL=+126.36€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.151 > 0.08 con n=711 PNL=+188.37€
  - _Datos_: n=711 IC=+0.151 PNL=+188.37€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.106 > 0.08 con n=539 PNL=+251.44€
  - _Datos_: n=539 IC=+0.106 PNL=+251.44€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=64024 IC=+0.118 PNL=+23817.77€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=64024 IC=+0.118 PNL=+23817.77€

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
  - _Estado_: n=6779 IC=+0.042 PNL=+531.49€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6779 IC=+0.042 PNL=+531.49€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.02 con n=713 PNL=+271.35€
  - _Datos_: n=713 IC=+0.120 PNL=+271.35€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=156 IC=-0.063 PNL=+31.89€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=156 IC=-0.063 PNL=+31.89€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.448 > 0.1 con n=1237 PNL=+1209.51€
  - _Datos_: n=1237 IC=+0.448 PNL=+1209.51€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=16619 IC=+0.058 PNL=+2049.28€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=16619 IC=+0.058 PNL=+2049.28€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.204 > 0.1 con n=4100 PNL=+2279.85€
  - _Datos_: n=4100 IC=+0.204 PNL=+2279.85€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.150 < -0.1 con n=275 PNL=+28.08€
  - _Datos_: n=275 IC=-0.150 PNL=+28.08€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2176 IC=+0.055 PNL=+229.59€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2176 IC=+0.055 PNL=+229.59€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=92 IC=-0.096 PNL=+5.74€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=92 IC=-0.096 PNL=+5.74€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.1 con n=510 PNL=+142.52€
  - _Datos_: n=510 IC=+0.121 PNL=+142.52€

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
  - _Estado_: n=20917 IC=-0.137 PNL=+1451.46€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=20917 IC=-0.137 PNL=+1451.46€

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
  - _Estado_: n=2196 IC=+0.138 PNL=+1246.24€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2196 IC=+0.138 PNL=+1246.24€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.08 con n=2491 PNL=+1641.51€
  - _Datos_: n=2491 IC=+0.194 PNL=+1641.51€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=4867 IC=+0.028 PNL=+222.37€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4867 IC=+0.028 PNL=+222.37€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.089 > 0.08 con n=2387 PNL=+1280.39€
  - _Datos_: n=2387 IC=+0.089 PNL=+1280.39€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.211 > 0.08 con n=562 PNL=+295.40€
  - _Datos_: n=562 IC=+0.211 PNL=+295.40€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.233 < -0.1 con n=2056 PNL=-195.14€
  - _Datos_: n=2056 IC=-0.233 PNL=-195.14€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=6148 IC=+0.179 PNL=+4271.77€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=6148 IC=+0.179 PNL=+4271.77€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.08 con n=83 PNL=+29.22€
  - _Datos_: n=83 IC=+0.100 PNL=+29.22€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2225 IC=+0.069 PNL=+674.66€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2225 IC=+0.069 PNL=+674.66€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=2032 PNL=+1433.87€
  - _Datos_: n=2032 IC=+0.179 PNL=+1433.87€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3369 IC=-0.033 PNL=+863.52€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3369 IC=-0.033 PNL=+863.52€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=591 PNL=-53.34€
  - _Datos_: n=591 IC=+0.087 PNL=-53.34€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.237 > 0.08 con n=3634 PNL=-320.59€
  - _Datos_: n=3634 IC=+0.237 PNL=-320.59€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=42 IC=+0.000 PNL=+5.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=42 IC=+0.000 PNL=+5.94€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1190) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1190 IC=+0.102 PNL=+281.87€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.08 con n=305 PNL=+107.15€
  - _Datos_: n=305 IC=+0.334 PNL=+107.15€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=454) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=454 IC=+0.410 PNL=+639.66€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=9897 IC=+0.178 PNL=-1113.03€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=9897 IC=+0.178 PNL=-1113.03€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.204 > 0.1 con n=157 PNL=+95.67€
  - _Datos_: n=157 IC=+0.204 PNL=+95.67€
