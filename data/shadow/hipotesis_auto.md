# Hipótesis automáticas — 2026-09-30 14:58 UTC
_Generado por shadow_postmortem.py sobre 683464 resoluciones (PNL=+80948.54€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=553)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.235 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `74.0` → IC=+0.213 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 74.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.803` → IC=+0.257 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.803 (IC base=+0.139)

- **PATRÓN** `banda_z` > `9.568` → IC=+0.201 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.568 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.158 (n=398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=609)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4766.038` → IC=+0.165 (n=192)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4766.038 (IC base=+0.139)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.123 (n=553)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.058)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.138 (n=172)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.259 (n=442)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=418)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.259 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.148)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.209 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.148)

- **PATRÓN** `banda_hit_calibrado` > `0.7998` → IC=+0.267 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7998 (IC base=+0.148)

- **PATRÓN** `banda_z` > `4.287` → IC=+0.170 (n=461)

  - _Acción_: Kelly boost +0.85€ cuando `banda_z` > 4.287 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=519)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `3319.4656` → IC=+0.154 (n=307)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3319.4656 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `8385.9934` → IC=+0.124 (n=235)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 8385.9934 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.145 (n=167)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 94.0 (IC base=+0.061)

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

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.124 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 4.0 (IC base=+0.110)

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
- **FILTRO** `restante_s_al_confirmar` < `145.79` → IC=-0.217 (n=7727)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.79
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=23184)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `137.22` → IC=-0.249 (n=1008)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 137.22
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3025)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `127.82` → IC=-0.305 (n=902)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.82
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2706)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.52` → IC=-0.205 (n=1897)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.52
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=5694)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `126.94` → IC=-0.329 (n=1508)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 126.94
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=4524)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.209 (n=15160)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=3710)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5547.2126` → IC=+0.174 (n=2391)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 5547.2126 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=12868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=15856)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.230 (n=12185)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=6056)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7767.3061` → IC=+0.169 (n=2309)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7767.3061 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=1743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.204 (n=1789)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2250)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `15969.9705` → IC=+0.232 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15969.9705 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.200 (n=1613)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.294 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2303)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `15892.8673` → IC=+0.213 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15892.8673 (IC base=+0.196)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.171 (n=357)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.615 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `4566.8958` → IC=+0.137 (n=243)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 4566.8958 (IC base=+0.093)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.148 (n=396)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.101)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=879)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.157 (n=228)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.101)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=3121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.347 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.366 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.231 (n=1616)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.227)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.136 (n=742)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.249 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=842)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1317.494` → IC=+0.146 (n=736)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1317.494 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.211 (n=1394)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.405 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.157 (n=659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 14.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.160 (n=630)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=778)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.151)

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
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.226 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=13015)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=12454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.230 (n=4170)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `3571.1845` → IC=+0.332 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3571.1845 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=3102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=2942)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=2961)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.171)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.250 (n=1137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.244 (n=1137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.346 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.241)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=3055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=2920)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=2462)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=2689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.326 (n=890)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=2976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.191 (n=2868)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 17.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.192 (n=2244)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.193 (n=1097)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.73 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `11452.1989` → IC=+0.460 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11452.1989 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.446 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.453 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `14504.3208` → IC=+0.448 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14504.3208 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.443 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.464 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `3366.033` → IC=+0.447 (n=150)

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
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

- **FILTRO** `libro_liquidez` < `6345.2155` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 6345.2155
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=38722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.237 (n=17093)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=6662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=5374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=7273)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=6987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.264 (n=3953)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=7058)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=7047)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.267 (n=2388)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=6423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.258 (n=2556)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=2761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=2980)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=5896)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.125 (n=5522)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.19 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5615)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=7289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.53` → IC=+0.138 (n=5474)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.53 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=2968)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.125 (n=2736)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.16 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=2775)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=3599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.25` → IC=+0.138 (n=2730)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.25 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.185 (n=2928)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.38 (IC base=+0.112)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.133 (n=3104)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.112)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.137 (n=2780)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.25 (IC base=+0.112)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `4160.4948` → IC=+0.305 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4160.4948 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.292 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.347 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5084.4032` → IC=+0.314 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5084.4032 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.322 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.295 (n=613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.394 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1447.2132` → IC=+0.304 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1447.2132 (IC base=+0.286)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.441 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.436 (n=479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.436 (n=643)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.451 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.439 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `1966.3827` → IC=+0.456 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1966.3827 (IC base=+0.440)

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
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=63)

- **FILTRO** `py_entrada` > `0.75` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=55)

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
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=63)

- **FILTRO** `py_entrada` > `0.75` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=55)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4935` → IC=+0.128 (n=9217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4935 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.9831` → IC=+0.243 (n=3074)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9831 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.2176` → IC=+0.257 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2176 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.986` → IC=+0.180 (n=3513)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.986 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.254 (n=1699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` > `0.6163` → IC=+0.254 (n=2546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6163 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.3017` → IC=+0.230 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3017 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.3272` → IC=+0.217 (n=2900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3272 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.5689` → IC=+0.136 (n=11188)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5689 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.6021` → IC=+0.204 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6021 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.156` → IC=+0.177 (n=3684)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.156 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6987` → IC=+0.185 (n=1766)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6987 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `0.8704` → IC=+0.179 (n=2675)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.8704 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.1671` → IC=+0.226 (n=1925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1671 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.448` → IC=+0.200 (n=6843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.448 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.214 (n=6635)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 125.0 (IC base=+0.068)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.205 (n=686)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.182 (n=689)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0081 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.3557` → IC=+0.178 (n=2058)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3557 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=985)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.179 (n=1387)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 11.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.206` → IC=+0.272 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.206 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.212 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `1.4344` → IC=+0.175 (n=1937)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.4344 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.189 (n=2088)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.04 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.242 (n=1450)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0913` → IC=+0.273 (n=540)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0913 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.242 (n=1464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.287 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.544` → IC=+0.245 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.544 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.464` → IC=+0.241 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.464 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0939` → IC=+0.231 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0939 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.271 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6054` → IC=+0.244 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6054 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1665.6812` → IC=+0.247 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1665.6812 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.238 (n=715)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3554` → IC=+0.228 (n=1621)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3554 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.239 (n=1622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.220 (n=1654)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.8982` → IC=+0.263 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8982 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.1866` → IC=+0.222 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1866 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.3463` → IC=+0.223 (n=1510)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3463 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.529` → IC=+0.258 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.529 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2572` → IC=+0.223 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2572 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.0901` → IC=+0.226 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0901 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.242 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.3839` → IC=+0.241 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3839 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `11046.4069` → IC=+0.224 (n=1620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11046.4069 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.166 (n=1104)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0038 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0749` → IC=+0.164 (n=552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0749 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=753)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.3383` → IC=+0.196 (n=1104)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.3383 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1307` → IC=+0.154 (n=1495)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1307 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.348` → IC=+0.153 (n=263)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 11.348 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.304` → IC=+0.145 (n=1526)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.304 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2117` → IC=+0.149 (n=1655)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2117 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.8628` → IC=+0.142 (n=1103)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.8628 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.182 (n=438)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.150 (n=1545)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.77` → IC=+0.149 (n=1030)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.77 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `14067.2635` → IC=+0.142 (n=1103)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 14067.2635 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.173 (n=643)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 231.0 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.207 (n=690)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=2177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.189 (n=1864)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.302` → IC=+0.256 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.302 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.193 (n=1810)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.203 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.1729` → IC=+0.203 (n=1318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1729 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=2457)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `1993.7386` → IC=+0.187 (n=689)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1993.7386 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.220 (n=1588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6301` → IC=+0.214 (n=1805)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6301 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=847)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0636` → IC=+0.241 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0636 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.695` → IC=+0.231 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.695 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.581` → IC=+0.212 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.581 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3474` → IC=+0.254 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3474 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7339` → IC=+0.209 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7339 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `3.2363` → IC=+0.222 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2363 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1985.3184` → IC=+0.220 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1985.3184 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.211 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=114)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=2486)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.142 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0037 (IC base=+0.041)

- **PATRÓN** `ibs_20min` > `0.9556` → IC=+0.225 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9556 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` < `0.5438` → IC=+0.335 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5438 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.846` → IC=+0.170 (n=820)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 4.846 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.341 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.342 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.360 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.360 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `1.8361` → IC=+0.331 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8361 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.334 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.1017` → IC=+0.152 (n=651)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1017 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.6715` → IC=+0.204 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6715 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.6137` → IC=+0.163 (n=330)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6137 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.1641` → IC=+0.148 (n=330)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.1641 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.205 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.5223` → IC=+0.166 (n=835)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5223 (IC base=+0.022)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.176 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=373)

- **FILTRO** `ibs_20min` < `0.3056` → IC=-0.205 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3056
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=332)

- **FILTRO** `ibs_20min` > `0.2419` → IC=-0.125 (n=2495)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2419
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=1229)

- **FILTRO** `sigma_ewma_delta_pct` > `8.709` → IC=-0.211 (n=393)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.709
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3331)

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

- **PATRÓN** `ibs_20min` < `0.2419` → IC=+0.130 (n=1229)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.2419 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7158` → IC=+0.253 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7158 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.4503` → IC=+0.241 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4503 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` < `0.6774` → IC=+0.277 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6774 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.298 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.286 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.041)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6576` → IC=-0.181 (n=646)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6576
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1942)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.207 (n=585)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2003)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.208 (n=950)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=2908)

- **PATRÓN** `dist_vwap_pct` > `0.4614` → IC=+0.324 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4614 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2843` → IC=+0.317 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2843 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` < `0.9729` → IC=+0.296 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9729 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.313 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6226 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.303 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `2.4239` → IC=+0.303 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4239 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.8015` → IC=+0.300 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8015 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.5629` → IC=+0.282 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5629 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` < `0.7286` → IC=+0.256 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7286 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` > `1.2443` → IC=+0.287 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2443 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.275 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `2.1396` → IC=+0.261 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1396 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.4224` → IC=+0.255 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4224 (IC base=-0.017)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.196 (n=3959)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0097 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4737` → IC=+0.187 (n=10601)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4737 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `1.0203` → IC=+0.290 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0203 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.637` → IC=+0.158 (n=5456)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.637 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.1809` → IC=+0.243 (n=4279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1809 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.253 (n=3823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.271 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `1.4632` → IC=+0.240 (n=2305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4632 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.6398` → IC=+0.253 (n=2305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6398 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.273 (n=6441)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.169 (n=3855)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0092 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5461` → IC=+0.157 (n=10176)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5461 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.7151` → IC=+0.250 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7151 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2499` → IC=+0.248 (n=3331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2499 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.7103` → IC=+0.248 (n=1533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7103 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.2033` → IC=+0.256 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2033 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.305 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5925` → IC=+0.273 (n=2081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5925 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2812` → IC=+0.263 (n=2145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2812 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.276 (n=4626)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2558` → IC=-0.152 (n=820)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2558
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=2460)

- **FILTRO** `ibs_20min` > `0.7572` → IC=-0.155 (n=671)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7572
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2017)

- **FILTRO** `sigma_ewma_delta_pct` > `4.561` → IC=-0.171 (n=611)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.561
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2077)

- **PATRÓN** `ibs_20min` > `0.8974` → IC=+0.274 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8974 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.942` → IC=+0.207 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.942 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2248` → IC=+0.267 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2248 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4388` → IC=+0.200 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4388 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.1651` → IC=+0.220 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1651 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.215 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.2221` → IC=+0.436 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2221 (IC base=-0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.1478` → IC=+0.441 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1478 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4701` → IC=+0.444 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4701 (IC base=-0.021)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.470 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8659` → IC=+0.168 (n=794)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8659 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.2979` → IC=+0.186 (n=421)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.2979 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6774` → IC=+0.177 (n=984)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6774 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.231 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.199 (n=360)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.4012` → IC=+0.177 (n=360)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.4012 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.216 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 235.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.224 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `0.8607` → IC=+0.236 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8607 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2677` → IC=+0.305 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2677 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.4316` → IC=+0.220 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4316 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.244 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `456.0` → IC=+0.221 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 456.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.282 (n=1221)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.255 (n=1839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.252 (n=1850)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.725` → IC=+0.281 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.725 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.0994` → IC=+0.265 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0994 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `2.192` → IC=+0.264 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.192 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.263 (n=2154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `1915.9532` → IC=+0.264 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.9532 (IC base=+0.251)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.316 (n=681)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.1841` → IC=+0.298 (n=660)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1841 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.325 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.3543` → IC=+0.292 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3543 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.7` → IC=+0.292 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.7 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.8` → IC=+0.287 (n=1601)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.8 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.1195` → IC=+0.291 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1195 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` < `1.5806` → IC=+0.298 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5806 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.6641` → IC=+0.291 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6641 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `1908.841` → IC=+0.305 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1908.841 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.288 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.285)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7744` → IC=-0.186 (n=687)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7744
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=2064)

- **PATRÓN** `ibs_20min` > `0.9077` → IC=+0.186 (n=603)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.9077 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.1858` → IC=+0.227 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1858 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.0031` → IC=+0.246 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0031 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.5902` → IC=+0.222 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5902 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.0834` → IC=+0.257 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0834 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4046` → IC=+0.265 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4046 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.7588` → IC=+0.235 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7588 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.253 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 145.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.1481` → IC=+0.222 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1481 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` < `1.1663` → IC=+0.216 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1663 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2771` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2771 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.8034` → IC=+0.262 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8034 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.238 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.259 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7536` → IC=-0.185 (n=1258)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7536
  - _Potencial_: sin este filtro IC_bueno=+0.280 (n=1259)

- **FILTRO** `ibs_20min` > `0.6774` → IC=-0.235 (n=631)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6774
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=1895)

- **FILTRO** `sigma_ewma_delta_pct` > `4.71` → IC=-0.190 (n=550)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.71
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=1976)

- **PATRÓN** `ibs_20min` > `0.7536` → IC=+0.280 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7536 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `1.0858` → IC=+0.330 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0858 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.678` → IC=+0.168 (n=398)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.678 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.307 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8646 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` > `0.6396` → IC=+0.301 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6396 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.0998` → IC=+0.300 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0998 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.4314` → IC=+0.322 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4314 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.324 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.5773` → IC=+0.128 (n=1668)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.5773 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` < `0.2225` → IC=+0.238 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2225 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` < `0.7092` → IC=+0.261 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7092 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.225 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.239 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.46` → IC=+0.245 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.46 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.257 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.019)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.324 (n=1342)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.298 (n=707)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` > `0.7398` → IC=+0.321 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7398 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2186` → IC=+0.313 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2186 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.683` → IC=+0.301 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.683 (IC base=+0.279)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.293 (n=1502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.329 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `1.4303` → IC=+0.289 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4303 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `2463.6549` → IC=+0.289 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2463.6549 (IC base=+0.279)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.318 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.308 (n=1063)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.1967` → IC=+0.288 (n=701)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1967 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.292 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.281)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.281 (n=797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` < `0.1341` → IC=+0.333 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1341 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.3215` → IC=+0.290 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3215 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` < `0.2317` → IC=+0.281 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2317 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.119` → IC=+0.304 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.119 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` < `0.6418` → IC=+0.284 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6418 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` > `1.2434` → IC=+0.312 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2434 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` > `0.2357` → IC=+0.332 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2357 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` < `2.4899` → IC=+0.280 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4899 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `2.1415` → IC=+0.278 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1415 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `2411.0916` → IC=+0.285 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2411.0916 (IC base=+0.281)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.177 (n=3011)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0048 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.203 (n=2997)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.3657` → IC=+0.178 (n=7911)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3657 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=9399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.222 (n=8996)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.1761` → IC=+0.194 (n=3874)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1761 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.386` → IC=+0.252 (n=1820)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.386 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.2117` → IC=+0.164 (n=5980)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2117 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6308` → IC=+0.161 (n=5980)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6308 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.199 (n=1340)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5596` → IC=+0.169 (n=3803)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5596 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.6066` → IC=+0.176 (n=2881)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6066 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `1952.4954` → IC=+0.172 (n=8030)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 1952.4954 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.184 (n=7906)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 109.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.185 (n=5765)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0821` → IC=+0.211 (n=2884)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0821 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=3281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4843` → IC=+0.226 (n=8641)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4843 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.1752` → IC=+0.165 (n=6039)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1752 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.323` → IC=+0.199 (n=1452)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.323 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1777` → IC=+0.157 (n=6212)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1777 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2914` → IC=+0.216 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2914 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5571` → IC=+0.171 (n=3498)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5571 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.6069` → IC=+0.172 (n=2650)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6069 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.179 (n=7605)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 109.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.229 (n=508)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.198 (n=505)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0083 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.3439` → IC=+0.214 (n=1507)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3439 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=1591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.202 (n=1017)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.9049` → IC=+0.282 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9049 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.192` → IC=+0.310 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.192 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.244 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `1.4334` → IC=+0.191 (n=1404)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4334 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.207 (n=1535)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.242 (n=1009)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.245 (n=1025)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1866` → IC=+0.284 (n=765)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1866 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=1105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.237 (n=1062)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.3492` → IC=+0.259 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3492 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.305` → IC=+0.246 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.305 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.255 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.257 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1559.11` → IC=+0.248 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1559.11 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.239 (n=454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.0719` → IC=+0.191 (n=451)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.0719 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=1355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.3944` → IC=+0.225 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3944 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.1987` → IC=+0.211 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1987 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.482` → IC=+0.226 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.482 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `0.6926` → IC=+0.174 (n=594)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6926 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.206 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.503` → IC=+0.180 (n=577)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.503 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `2.4677` → IC=+0.163 (n=437)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.4677 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `10679.1014` → IC=+0.168 (n=1349)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 10679.1014 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `383.0` → IC=+0.160 (n=1118)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 383.0 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.159 (n=1437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0057 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2936` → IC=+0.163 (n=1436)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2936 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.140 (n=684)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.5859` → IC=+0.191 (n=1436)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5859 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.901` → IC=+0.208 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.901 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.157 (n=1436)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2145 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1567` → IC=+0.150 (n=438)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1567 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4481` → IC=+0.146 (n=1324)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4481 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.4211` → IC=+0.138 (n=1324)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4211 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `210.0` → IC=+0.169 (n=415)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 210.0 (IC base=+0.139)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.220 (n=684)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.2505` → IC=+0.220 (n=1002)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2505 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.451` → IC=+0.278 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.451 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.201` → IC=+0.211 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.201 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.7872` → IC=+0.200 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7872 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.7374` → IC=+0.212 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7374 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.210 (n=1775)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `1917.5696` → IC=+0.203 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.5696 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.234 (n=1131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1437` → IC=+0.255 (n=565)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1437 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.275 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.3521` → IC=+0.246 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3521 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.676` → IC=+0.254 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.676 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.251 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.75` → IC=+0.226 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.75 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.1786` → IC=+0.226 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1786 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.219 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1911.3596` → IC=+0.224 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.3596 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.214 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.219)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.179 (n=1271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0065 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.4335` → IC=+0.162 (n=1444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4335 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=1509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.9433` → IC=+0.285 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9433 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1502` → IC=+0.181 (n=940)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1502 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.953` → IC=+0.225 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.953 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.157 (n=963)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8554 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6214` → IC=+0.146 (n=1443)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6214 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1012` → IC=+0.185 (n=611)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1012 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4303` → IC=+0.158 (n=471)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4303 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.5072` → IC=+0.168 (n=471)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5072 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `5380.0822` → IC=+0.190 (n=962)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 5380.0822 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.150 (n=1379)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 157.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.157 (n=1518)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.3879` → IC=+0.147 (n=1518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3879 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6569` → IC=+0.172 (n=1518)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6569 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.158` → IC=+0.143 (n=1484)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.158 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.965` → IC=+0.162 (n=531)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.965 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8556` → IC=+0.152 (n=1012)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8556 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.180 (n=226)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.8074` → IC=+0.140 (n=929)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8074 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.5177` → IC=+0.125 (n=465)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.5177 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `9441.0647` → IC=+0.165 (n=688)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 9441.0647 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.123 (n=1331)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 154.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.160 (n=744)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0101 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1681)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.5045` → IC=+0.208 (n=1638)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5045 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.833` → IC=+0.210 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.833 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.836` → IC=+0.258 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.836 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2173` → IC=+0.133 (n=1639)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2173 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6441` → IC=+0.127 (n=1638)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6441 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1633` → IC=+0.127 (n=1647)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1633 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.0711` → IC=+0.124 (n=684)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0711 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.5436` → IC=+0.136 (n=696)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.5436 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1713)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2883.9504` → IC=+0.201 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2883.9504 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.140 (n=1285)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 48.0 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.164 (n=732)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0062 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1064` → IC=+0.166 (n=554)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1064 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.215 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.211` → IC=+0.146 (n=1531)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.211 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.334` → IC=+0.134 (n=509)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 5.334 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.6382` → IC=+0.152 (n=555)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6382 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2277` → IC=+0.162 (n=291)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2277 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4516` → IC=+0.144 (n=504)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4516 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4234` → IC=+0.134 (n=503)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4234 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2735.7982` → IC=+0.170 (n=753)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2735.7982 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.125 (n=1461)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 53.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.224 (n=1387)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.1833` → IC=+0.208 (n=683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1833 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=1622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.208 (n=700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.6494` → IC=+0.244 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6494 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.5295` → IC=+0.211 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5295 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.3041` → IC=+0.202 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3041 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.596` → IC=+0.240 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.596 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2034` → IC=+0.208 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2034 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.6293` → IC=+0.212 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6293 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.266 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.146` → IC=+0.210 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.146 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.7988` → IC=+0.210 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7988 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=1549)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2825.737` → IC=+0.202 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2825.737 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.228 (n=535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.217 (n=727)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.0929` → IC=+0.233 (n=533)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0929 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=742)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.02` → IC=+0.301 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.02 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `1.2288` → IC=+0.222 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2288 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.392` → IC=+0.251 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.392 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `0.635` → IC=+0.220 (n=1599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.635 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.289 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `2.1933` → IC=+0.202 (n=1280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1933 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4348` → IC=+0.207 (n=1454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4348 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2381.1966` → IC=+0.215 (n=1428)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2381.1966 (IC base=+0.209)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.187 (n=1019)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0043 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.169 (n=772)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0086 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3479` → IC=+0.167 (n=2036)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3479 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.202 (n=1141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.51` → IC=+0.197 (n=2067)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.51 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.8162` → IC=+0.180 (n=376)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.8162 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.714` → IC=+0.188 (n=1020)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.714 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.183 (n=1384)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.8725 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `1.2081` → IC=+0.174 (n=692)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.2081 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.163` → IC=+0.177 (n=629)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.163 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.4377` → IC=+0.172 (n=748)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4377 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.165 (n=1495)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.167 (n=2634)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `2681.708` → IC=+0.167 (n=2067)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2681.708 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.177 (n=2095)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 146.0 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.142 (n=1589)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0056 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.3462` → IC=+0.127 (n=2094)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.3462 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=2224)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.06` → IC=+0.191 (n=793)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.06 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2266` → IC=+0.122 (n=2170)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2266 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.1653` → IC=+0.141 (n=592)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1653 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4434` → IC=+0.151 (n=767)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4434 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `3963.1458` → IC=+0.128 (n=1586)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3963.1458 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.133 (n=988)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 28.0 (IC base=+0.113)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.179 (n=263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0029 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3322` → IC=+0.153 (n=598)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3322 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.180 (n=552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.656` → IC=+0.207 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.656 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.2846` → IC=+0.170 (n=207)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.2846 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.141 (n=522)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.137` → IC=+0.153 (n=269)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.137 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.834` → IC=+0.139 (n=624)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 6.834 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.623` → IC=+0.188 (n=200)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.623 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` < `0.1548` → IC=+0.138 (n=622)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.1548 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0911` → IC=+0.154 (n=212)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0911 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.2024` → IC=+0.148 (n=513)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.2024 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.5048` → IC=+0.140 (n=520)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.5048 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=772)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `10600.6989` → IC=+0.154 (n=597)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 10600.6989 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `161.0` → IC=+0.168 (n=251)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 161.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.205 (n=249)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3426` → IC=+0.157 (n=747)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3426 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.150 (n=710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6155` → IC=+0.180 (n=657)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6155 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1832` → IC=+0.153 (n=739)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1832 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.406` → IC=+0.152 (n=277)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.406 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.123` → IC=+0.138 (n=686)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.123 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.227` → IC=+0.146 (n=747)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.227 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.716` → IC=+0.152 (n=667)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.716 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.216 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1115` → IC=+0.158 (n=649)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1115 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4135` → IC=+0.145 (n=737)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4135 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `306.0` → IC=+0.151 (n=629)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 306.0 (IC base=+0.138)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.262 (n=322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.2132` → IC=+0.220 (n=488)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2132 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.6782` → IC=+0.248 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6782 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.1422` → IC=+0.217 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1422 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.2183` → IC=+0.208 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2183 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.93` → IC=+0.234 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.93 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `0.8358` → IC=+0.218 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8358 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `1.1649` → IC=+0.232 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1649 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.1538` → IC=+0.253 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1538 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.4064` → IC=+0.228 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4064 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.4384` → IC=+0.245 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4384 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.0847` → IC=+0.145 (n=229)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.0847 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6885` → IC=+0.141 (n=302)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6885 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.142 (n=107)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.153 (n=511)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0058 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.5423` → IC=+0.140 (n=570)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5423 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.177 (n=525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.261 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.9943` → IC=+0.236 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9943 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.496` → IC=+0.187 (n=298)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.496 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.0674` → IC=+0.156 (n=501)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0674 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.7219` → IC=+0.146 (n=509)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7219 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1735` → IC=+0.163 (n=158)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1735 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.2078` → IC=+0.165 (n=249)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.2078 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=600)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2963.0907` → IC=+0.182 (n=259)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2963.0907 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.0444` → IC=+0.246 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0444 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.8823` → IC=+0.128 (n=358)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8823 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `1.5787` → IC=+0.178 (n=225)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.5787 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2917.7982` → IC=+0.149 (n=243)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2917.7982 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.137 (n=483)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 40.0 (IC base=+0.092)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.175 (n=3880)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0047 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.208 (n=3876)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=12149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.220 (n=11616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4615 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.9312` → IC=+0.202 (n=1638)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9312 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.364` → IC=+0.245 (n=2886)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.364 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `0.8811` → IC=+0.171 (n=5191)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8811 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.200 (n=1585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.5862` → IC=+0.194 (n=3736)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.5862 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `1789.16` → IC=+0.177 (n=11613)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1789.16 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.199 (n=9042)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.193 (n=7007)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.007 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.5078` → IC=+0.186 (n=10494)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.5078 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=3928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.449` → IC=+0.247 (n=9234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.449 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2517` → IC=+0.163 (n=6545)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2517 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.063` → IC=+0.206 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.063 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.751` → IC=+0.183 (n=10121)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.751 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.6344` → IC=+0.165 (n=2384)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6344 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.243 (n=1384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6049` → IC=+0.193 (n=3243)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6049 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.201 (n=6330)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.230 (n=649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.225 (n=644)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.3627` → IC=+0.204 (n=1932)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3627 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.219 (n=920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=1311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.332 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.353 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2282` → IC=+0.255 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2282 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.5626` → IC=+0.208 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5626 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.223 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.261 (n=1046)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.263 (n=1569)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1274` → IC=+0.282 (n=691)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1274 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3551` → IC=+0.282 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3551 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.339` → IC=+0.258 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.339 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.483` → IC=+0.260 (n=1644)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.483 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.292 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.5513` → IC=+0.260 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5513 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.622` → IC=+0.272 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.622 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=1712)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1666.3972` → IC=+0.271 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1666.3972 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.206 (n=625)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1128` → IC=+0.163 (n=821)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1128 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1954)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.3027` → IC=+0.206 (n=1863)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3027 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.1263` → IC=+0.189 (n=1042)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1263 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.707` → IC=+0.173 (n=411)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 9.707 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.181` → IC=+0.157 (n=1696)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.181 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.63` → IC=+0.184 (n=622)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.63 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0731` → IC=+0.157 (n=1641)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0731 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2671` → IC=+0.188 (n=270)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2671 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.1136` → IC=+0.161 (n=1590)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1136 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.7596` → IC=+0.157 (n=1205)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7596 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `11295.2956` → IC=+0.159 (n=1665)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11295.2956 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `279.0` → IC=+0.177 (n=768)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 279.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.165 (n=1591)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.3263` → IC=+0.161 (n=1590)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3263 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.2865` → IC=+0.236 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2865 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.655` → IC=+0.155 (n=253)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.655 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1329` → IC=+0.164 (n=1452)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1329 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.534` → IC=+0.169 (n=267)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.534 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.327` → IC=+0.150 (n=1451)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.327 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.2003` → IC=+0.163 (n=1590)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2003 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1517` → IC=+0.202 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1517 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.4038` → IC=+0.157 (n=1492)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4038 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.757` → IC=+0.164 (n=994)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.757 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `260.0` → IC=+0.163 (n=473)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 260.0 (IC base=+0.150)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.256 (n=632)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=1992)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1927)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.371` → IC=+0.302 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.371 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` < `0.1336` → IC=+0.220 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1336 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.230 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2250)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1664.8391` → IC=+0.221 (n=1694)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1664.8391 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.239 (n=1561)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.233 (n=1587)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.6109` → IC=+0.236 (n=1774)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6109 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.237 (n=840)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0146` → IC=+0.301 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0146 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.766` → IC=+0.270 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.766 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3404` → IC=+0.297 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3404 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7339` → IC=+0.229 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7339 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.240 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.244 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1910.6184` → IC=+0.245 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.6184 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.232 (n=1574)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.233)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.192 (n=664)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4384` → IC=+0.149 (n=1986)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4384 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=2075)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.277` → IC=+0.186 (n=1986)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.277 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.3692` → IC=+0.162 (n=773)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3692 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.596` → IC=+0.164 (n=322)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.596 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8705` → IC=+0.160 (n=1324)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8705 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.207 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5214` → IC=+0.149 (n=848)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5214 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.1574` → IC=+0.158 (n=874)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1574 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7649.1944` → IC=+0.239 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7649.1944 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.172 (n=622)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 73.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.170 (n=1072)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0052 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4456` → IC=+0.145 (n=1606)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4456 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=740)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.5844` → IC=+0.197 (n=1414)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5844 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.135 (n=1401)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.297` → IC=+0.174 (n=240)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.297 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6225` → IC=+0.151 (n=536)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6225 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.223 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.142 (n=1533)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `9675.8313` → IC=+0.201 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9675.8313 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.133 (n=1349)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 147.0 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.145 (n=1322)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0082 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=2039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.4667` → IC=+0.196 (n=1980)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.4667 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `1.0784` → IC=+0.206 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0784 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.558` → IC=+0.237 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.558 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.8932` → IC=+0.142 (n=1321)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8932 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.123 (n=2032)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.1924` → IC=+0.131 (n=873)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.1924 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2009)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2882.8084` → IC=+0.255 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2882.8084 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.143 (n=1556)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 52.0 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.183 (n=636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0058 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1373` → IC=+0.159 (n=631)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1373 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.208 (n=1895)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2238` → IC=+0.139 (n=1559)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2238 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.46` → IC=+0.128 (n=1817)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.46 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6478` → IC=+0.164 (n=631)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6478 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2207` → IC=+0.180 (n=295)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2207 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4358` → IC=+0.150 (n=576)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4358 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2772.1243` → IC=+0.182 (n=630)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2772.1243 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.133 (n=1514)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 51.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.228 (n=1749)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=2051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.212 (n=1419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.261 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.2188` → IC=+0.229 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2188 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.251 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.0648` → IC=+0.216 (n=1723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0648 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.6419` → IC=+0.219 (n=1958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6419 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2344` → IC=+0.242 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2344 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.4852` → IC=+0.232 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4852 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=1928)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2439.7868` → IC=+0.216 (n=1749)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2439.7868 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.221 (n=690)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.230 (n=690)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.221 (n=1453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.4214` → IC=+0.264 (n=1819)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4214 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `1.2377` → IC=+0.210 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2377 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.2197` → IC=+0.213 (n=1826)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2197 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.876` → IC=+0.266 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.876 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `1.2355` → IC=+0.241 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2355 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.277 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `2.1829` → IC=+0.203 (n=1653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1829 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.4324` → IC=+0.206 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4324 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2387.4052` → IC=+0.209 (n=1846)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2387.4052 (IC base=+0.208)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=3577)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.194 (n=3123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0091 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.5139` → IC=+0.187 (n=3545)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.5139 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=1335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=1622)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.237 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1781` → IC=+0.186 (n=1294)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1781 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` < `0.4689` → IC=+0.176 (n=2287)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.4689 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.212` → IC=+0.209 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.212 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `0.7082` → IC=+0.177 (n=1055)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.7082 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.8944` → IC=+0.181 (n=1598)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.8944 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.1701` → IC=+0.208 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1701 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.4557` → IC=+0.186 (n=1168)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.4557 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.8681` → IC=+0.184 (n=2333)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.8681 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2589)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2857.8582` → IC=+0.183 (n=3167)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2857.8582 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.216 (n=902)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.4933` → IC=+0.175 (n=2696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.4933 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=940)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=1233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.1829` → IC=+0.183 (n=1186)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1829 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.6774` → IC=+0.180 (n=505)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6774 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.203` → IC=+0.170 (n=2692)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.203 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.2546` → IC=+0.163 (n=2531)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2546 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.166 (n=2459)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.5391` → IC=+0.168 (n=1171)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5391 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.8256` → IC=+0.170 (n=1774)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8256 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=3577)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `4995.9681` → IC=+0.163 (n=2407)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4995.9681 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `84.0` → IC=+0.165 (n=1750)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 84.0 (IC base=+0.159)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.211 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.0811` → IC=+0.255 (n=153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0811 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.207 (n=203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.5204` → IC=+0.214 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5204 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.7702` → IC=+0.200 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7702 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.3479` → IC=+0.202 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3479 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.976` → IC=+0.211 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.976 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.584` → IC=+0.196 (n=478)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 2.584 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` > `0.8593` → IC=+0.217 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8593 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2983` → IC=+0.318 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2983 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.229 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.6272` → IC=+0.203 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6272 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `12565.4829` → IC=+0.230 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12565.4829 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.224 (n=443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.188 (n=338)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.198 (n=339)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 4.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.183 (n=443)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1435 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.153 (n=456)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6084 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.6795` → IC=+0.191 (n=95)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6795 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.377` → IC=+0.167 (n=987)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.377 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8869` → IC=+0.186 (n=671)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8869 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.0686` → IC=+0.171 (n=466)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0686 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4202` → IC=+0.147 (n=335)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4202 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.8221` → IC=+0.164 (n=668)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.8221 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `12131.3108` → IC=+0.156 (n=898)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 12131.3108 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `705.0` → IC=+0.150 (n=961)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 705.0 (IC base=+0.145)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1517` → IC=+0.203 (n=496)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1517 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.189 (n=512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 6.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.2849` → IC=+0.199 (n=496)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.2849 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.8838` → IC=+0.192 (n=375)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.8838 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2089` → IC=+0.192 (n=944)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.2089 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.178` → IC=+0.192 (n=1011)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 4.178 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.082` → IC=+0.185 (n=991)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.082 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.1669` → IC=+0.198 (n=336)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1669 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `2.4779` → IC=+0.188 (n=1105)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.4779 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=1124)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.216 (n=304)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.4897` → IC=+0.190 (n=912)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.4897 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.176 (n=612)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 10.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` < `0.7588` → IC=+0.171 (n=912)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7588 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.0954` → IC=+0.171 (n=912)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.0954 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.6082` → IC=+0.191 (n=202)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6082 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.639` → IC=+0.172 (n=937)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.639 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.6452` → IC=+0.199 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6452 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `0.7257` → IC=+0.167 (n=815)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.7257 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.167 (n=855)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.178 (n=383)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `2.1958` → IC=+0.182 (n=787)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.1958 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `7791.0091` → IC=+0.183 (n=815)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 7791.0091 (IC base=+0.165)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.169 (n=482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0039 (IC base=+0.082)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.123 (n=994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 8.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.6464` → IC=+0.181 (n=894)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6464 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1435` → IC=+0.144 (n=535)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1435 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.442` → IC=+0.186 (n=234)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.442 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.188 (n=136)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.082)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.122 (n=445)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0063 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.0417` → IC=+0.306 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0417 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` < `0.1862` → IC=+0.149 (n=414)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1862 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.036` → IC=+0.158 (n=144)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.036 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.09` → IC=+0.148 (n=313)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.09 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.226 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `2.5298` → IC=+0.166 (n=309)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.5298 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `1.4444` → IC=+0.158 (n=276)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4444 (IC base=+0.050)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.149 (n=314)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.050)

- **PATRÓN** `libro_liquidez` > `3575.5947` → IC=+0.179 (n=110)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 3575.5947 (IC base=+0.050)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.202 (n=166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.4395` → IC=+0.163 (n=345)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.4395 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1239` → IC=+0.169 (n=179)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1239 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `2.0731` → IC=+0.141 (n=268)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.0731 (IC base=+0.092)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.153 (n=171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0044 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.196 (n=54)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.128 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 4.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.279` → IC=+0.267 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.279 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.1654` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1654 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.0682` → IC=+0.158 (n=179)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.0682 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.92` → IC=+0.201 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.92 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.1357` → IC=+0.151 (n=170)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1357 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.825` → IC=+0.152 (n=113)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.825 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.0668` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0668 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `2.4035` → IC=+0.193 (n=148)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.4035 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3655.3629` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3655.3629 (IC base=+0.100)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6845` → IC=-0.122 (n=146)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6845
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=299)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=144)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.134 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0049 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.134 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.6845` → IC=+0.214 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6845 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.3424` → IC=+0.202 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3424 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.74` → IC=+0.288 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.74 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.7588` → IC=+0.147 (n=188)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7588 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `1133.0595` → IC=+0.153 (n=295)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1133.0595 (IC base=+0.094)

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
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=118)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.186 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=107)

- **FILTRO** `ibs_20min` > `0.1837` → IC=-0.305 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1837
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=76)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.127 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0061 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.7778` → IC=+0.179 (n=216)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7778 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0104` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 1.0104 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.076` → IC=+0.149 (n=92)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.076 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.2389` → IC=+0.192 (n=63)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2389 (IC base=+0.057)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.167 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0066 (IC base=+0.000)

- **PATRÓN** `ibs_20min` < `0.1837` → IC=+0.269 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1837 (IC base=+0.000)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.93` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.93 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.0953` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0953 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `1.4444` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.4444 (IC base=+0.000)

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

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.157 (n=138)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0058 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6508` → IC=+0.147 (n=304)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6508 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.5164` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.5164 (IC base=+0.085)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.125 (n=313)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.006 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.193 (n=275)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1524 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.12` → IC=+0.185 (n=128)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.12 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `2.5856` → IC=+0.138 (n=238)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5856 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` > `1.4597` → IC=+0.125 (n=238)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.4597 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=330)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `3925.9695` → IC=+0.215 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3925.9695 (IC base=+0.093)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6599` → IC=-0.244 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6599
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=85)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.194 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0034 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.222 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.179 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 5.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.226 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1622 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.794` → IC=+0.172 (n=129)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.794 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `1.1737` → IC=+0.171 (n=144)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.1737 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.8617` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.8617 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` < `0.1895` → IC=+0.219 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1895 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.5856` → IC=+0.219 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5856 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.184 (n=112)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `4433.8504` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 4433.8504 (IC base=+0.158)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.6645` → IC=-0.219 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6645
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=91)

- **FILTRO** `libro_liquidez` < `1374.2652` → IC=-0.219 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 1374.2652
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=91)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.167 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0025 (IC base=+0.020)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.120 (n=106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0053 (IC base=+0.085)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.153 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 12.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.1558` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1558 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.769` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.769 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` < `0.9994` → IC=+0.132 (n=93)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.9994 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.0745` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.0745 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `2175.2667` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2175.2667 (IC base=+0.085)

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
- **PATRÓN** `drift_ventana_pct` |x|> `0.4522` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4522 (IC base=+0.271)

- **PATRÓN** `elapsed_s` > `210.3` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.3 (IC base=+0.271)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.8301` → IC=+0.354 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8301 (IC base=+0.271)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.271)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.219)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.219)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.219)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.333 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `1508.0` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1508.0 (IC base=+0.219)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4522` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4522 (IC base=+0.271)

- **PATRÓN** `elapsed_s` > `210.3` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.3 (IC base=+0.271)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.8301` → IC=+0.354 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8301 (IC base=+0.271)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.271)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.219)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.219)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.219)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.333 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `1508.0` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1508.0 (IC base=+0.219)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=840)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2916.268` → IC=+0.158 (n=290)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2916.268 (IC base=+0.106)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=840)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2916.268` → IC=+0.158 (n=290)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2916.268 (IC base=+0.106)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=2167)

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
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=95)

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

- **PATRÓN** `liq_usd_total` > `100330.87` → IC=+0.149 (n=95)

  - _Acción_: Kelly boost +0.75€ cuando `liq_usd_total` > 100330.87 (IC base=+0.048)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.164 (n=126)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.495 (IC base=+0.048)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=152)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=907)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=861)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=508)

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
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=218)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.163 (n=87)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.495 (IC base=+0.025)

- **PATRÓN** `libro_liquidez` > `4034.3706` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4034.3706 (IC base=+0.025)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=708)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=708)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=432)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=432)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=192)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=192)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.127 (n=81)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=126)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=103)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=127)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=233)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=110)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=113)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=268)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=268)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=155)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.122 (n=826)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=843)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.134 (n=69)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=81)

- **PATRÓN** `py_entrada` > `0.52` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.52 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.137 (n=111)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.56 (IC base=+0.050)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=90)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=82)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.148 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 9.0 (IC base=+0.090)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.128 (n=100)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.183 (n=39)

- **FILTRO** `profundidad_ratio` < `51.8` → IC=-0.245 (n=45)

  - _Acción_: SKIP cuando `profundidad_ratio` < 51.8
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=94)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=122)

- **FILTRO** `profundidad_ratio` < `19.0` → IC=-0.147 (n=49)

  - _Acción_: SKIP cuando `profundidad_ratio` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=103)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.324 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=152)

- **FILTRO** `restante_min` < `3.39` → IC=-0.274 (n=60)

  - _Acción_: SKIP cuando `restante_min` < 3.39
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=124)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.163 (n=81)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=103)

- **FILTRO** `lag_apertura_s` > `95.78` → IC=-0.281 (n=62)

  - _Acción_: SKIP cuando `lag_apertura_s` > 95.78
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=122)

- **FILTRO** `profundidad_ratio` < `76.0` → IC=-0.213 (n=92)

  - _Acción_: SKIP cuando `profundidad_ratio` < 76.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=92)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=113)

- **PATRÓN** `restante_min` > `13.36` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `restante_min` > 13.36 (IC base=+0.006)

- **PATRÓN** `lag_apertura_s` < `95.05` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `lag_apertura_s` < 95.05 (IC base=+0.006)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.47` → IC=+0.132 (n=55)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.47 (IC base=+0.009)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.161 (n=125)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=69)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.162 (n=69)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.5 (IC base=-0.046)

- **PATRÓN** `profundidad_ratio` > `13.0` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `profundidad_ratio` > 13.0 (IC base=+0.028)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.254 (n=63)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=165)

- **FILTRO** `restante_min` < `3.26` → IC=-0.127 (n=73)

  - _Acción_: SKIP cuando `restante_min` < 3.26
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=155)

- **FILTRO** `lag_apertura_s` > `102.62` → IC=-0.133 (n=77)

  - _Acción_: SKIP cuando `lag_apertura_s` > 102.62
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=151)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.165 (n=4067)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=12399)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.162 (n=4155)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=12913)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.196 (n=714)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=2174)

- **PATRÓN** `libro_liquidez` > `1566.75` → IC=+0.138 (n=1036)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1566.75 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.183 (n=717)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2231)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=734)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2349)

- **PATRÓN** `libro_liquidez` > `1789.3696` → IC=+0.122 (n=1003)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1789.3696 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.168 (n=700)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=2182)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2224)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2363)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3103)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=411)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=402)

- **FILTRO** `libro_liquidez` < `17076.8097` → IC=-0.144 (n=231)

  - _Acción_: SKIP cuando `libro_liquidez` < 17076.8097
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=694)

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
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=25713)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=8620)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=28643)

- **FILTRO** `ibs_7min` < `0.2682` → IC=-0.235 (n=9315)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2682
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=27948)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=12402)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=24861)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=11555)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=35683)

- **FILTRO** `ibs_7min` > `0.2917` → IC=-0.180 (n=11790)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2917
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=35448)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.141 (n=1877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4373)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.311 (n=1500)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4750)

- **FILTRO** `ibs_7min` < `0.708` → IC=-0.256 (n=2061)

  - _Acción_: SKIP cuando `ibs_7min` < 0.708
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=4189)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.179 (n=1484)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4766)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.263 (n=2009)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=6140)

- **FILTRO** `ibs_7min` > `0.7937` → IC=-0.210 (n=2037)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7937
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6112)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.142 (n=1516)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=4885)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1566)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4835)

- **FILTRO** `ibs_7min` < `0.7452` → IC=-0.196 (n=1600)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7452
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4801)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.181 (n=1592)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=4809)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=1512)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=5001)

- **FILTRO** `ibs_7min` > `0.2621` → IC=-0.186 (n=1627)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2621
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4886)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.183 (n=1625)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4888)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.162 (n=1688)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=4270)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.304 (n=1489)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4469)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.244 (n=1965)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3993)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.208 (n=1439)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4519)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.245 (n=2005)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=6704)

- **FILTRO** `ibs_7min` > `0.7468` → IC=-0.177 (n=2177)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7468
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=6532)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=1981)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=4150)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.234 (n=1804)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=4327)

- **FILTRO** `ibs_7min` < `0.7413` → IC=-0.182 (n=1532)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7413
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4599)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.175 (n=1471)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=4660)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.257 (n=1568)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=4749)

- **FILTRO** `ibs_7min` > `0.2747` → IC=-0.178 (n=1579)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2747
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4738)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.180 (n=1531)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4786)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.264 (n=1543)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4854)

- **FILTRO** `ibs_7min` < `0.2667` → IC=-0.233 (n=1592)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4805)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.172 (n=2244)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=6779)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.273 (n=1427)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=4699)

- **FILTRO** `ibs_7min` < `0.274` → IC=-0.223 (n=1531)

  - _Acción_: SKIP cuando `ibs_7min` < 0.274
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4595)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.214 (n=1445)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=4681)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.208 (n=2002)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=6525)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1166)

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
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=333)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=577)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.133 (n=837)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.117)

- **PATRÓN** `total_vol_5m` < `453.526` → IC=+0.151 (n=279)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 453.526 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.124 (n=709)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 55.0 (IC base=+0.117)

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
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.158 (n=147)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.180 (n=101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 11.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `6272.013` → IC=+0.149 (n=129)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 6272.013 (IC base=+0.124)

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
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.286 (n=218)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=220)

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
- **FILTRO** `sigma_h` > `0.013` → IC=-0.227 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=61)

- **FILTRO** `T_h` > `123.7153` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `T_h` > 123.7153
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=61)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0099` → IC=-0.172 (n=321)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

- **FILTRO** `T_h` > `71.1632` → IC=-0.136 (n=319)

  - _Acción_: SKIP cuando `T_h` > 71.1632
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=109)

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
- **FILTRO** `sigma_h` > `0.0137` → IC=-0.179 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0137
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=80)

- **FILTRO** `sigma_h` < `0.0083` → IC=-0.139 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=72)

- **FILTRO** `T_h` > `135.6166` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `T_h` > 135.6166
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=80)

- **FILTRO** `sigma_h` < `0.0158` → IC=-0.357 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0158
  - _Potencial_: sin este filtro IC_bueno=-0.309 (n=19)

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

- **PATRÓN** `edge` > `0.2065` → IC=+0.474 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2065 (IC base=+0.463)

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
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=217)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=317)

- **PATRÓN** `streak_estiramiento` < `0.5782` → IC=+0.145 (n=139)

  - _Acción_: Kelly boost +0.73€ cuando `streak_estiramiento` < 0.5782 (IC base=+0.032)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.000)

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
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=699)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1263)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=849)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=829)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3178)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1610)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1618)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.201 (n=636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.233 (n=635)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.1592` → IC=+0.197 (n=1676)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1592 (IC base=+0.193)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2178` → IC=+0.200 (n=635)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2178 (IC base=+0.193)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1267` → IC=+0.232 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1267 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.202 (n=1771)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=1987)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_15` > `0.6129` → IC=+0.272 (n=1905)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6129 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.189 (n=963)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.803` → IC=+0.283 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.803 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `8753.6365` → IC=+0.203 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8753.6365 (IC base=+0.193)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=808)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.233 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.278 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `0.3831` → IC=+0.222 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3831 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2012` → IC=+0.242 (n=192)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2012 (IC base=+0.212)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4004` → IC=+0.248 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4004 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` > `0.7141` → IC=+0.277 (n=423)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7141 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.274 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.588` → IC=+0.276 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.588 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `16113.4131` → IC=+0.241 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16113.4131 (IC base=+0.212)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.297` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.297
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=491)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.5788` → IC=-0.153 (n=148)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5788
  - _Potencial_: sin este filtro IC_bueno=+0.228 (n=446)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.175 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0035 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.139 (n=297)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.005 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0669` → IC=+0.153 (n=197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0669 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.175 (n=149)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.133)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1229` → IC=+0.159 (n=165)

  - _Acción_: Kelly boost +0.79€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1229 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.133 (n=448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 16.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.5788` → IC=+0.228 (n=446)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5788 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1154` → IC=+0.147 (n=318)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1154 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.307` → IC=+0.232 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.307 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `8733.4432` → IC=+0.142 (n=202)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 8733.4432 (IC base=+0.133)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=136)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.282 (n=76)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1481` → IC=+0.204 (n=201)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1481 (IC base=+0.180)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0592` → IC=+0.191 (n=228)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.0592 (IC base=+0.180)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3238` → IC=+0.227 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3238 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.191 (n=215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.180)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.265 (n=228)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.192 (n=128)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.180 (n=223)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.263` → IC=+0.400 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.263 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.180 (n=251)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `3075.9018` → IC=+0.274 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3075.9018 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.213 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.180)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.6747` → IC=-0.161 (n=107)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6747
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=1225)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.784` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.784 (IC base=-0.012)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0234` → IC=+0.287 (n=162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0234 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.227 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.199)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0605` → IC=+0.200 (n=435)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0605 (IC base=+0.199)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0815` → IC=+0.258 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0815 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_15` > `0.5745` → IC=+0.289 (n=486)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5745 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.3623` → IC=+0.210 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3623 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.1` → IC=+0.226 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.1 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.305` → IC=+0.199 (n=443)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 7.305 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2915.737` → IC=+0.287 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2915.737 (IC base=+0.199)

- **PATRÓN** `ibs_15` < `0.1184` → IC=+0.144 (n=548)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.72€ cuando `ibs_15` < 0.1184 (IC base=+0.056)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.353 (n=312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.351)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.380 (n=156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.351)

- **PATRÓN** `drift_60min` |x|≤ `0.1114` → IC=+0.353 (n=312)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1114 (IC base=+0.351)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1462` → IC=+0.375 (n=311)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1462 (IC base=+0.351)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1326` → IC=+0.388 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1326 (IC base=+0.351)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.370 (n=475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.351)

- **PATRÓN** `ibs_15` > `0.7873` → IC=+0.389 (n=467)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7873 (IC base=+0.351)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.387 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.351)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.363 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.351)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.350 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.351)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.355 (n=562)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.342)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.354 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.342)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.364 (n=189)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.342)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.372 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.342)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.402 (n=100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.342)

- **PATRÓN** `ibs_15` > `0.7485` → IC=+0.393 (n=212)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7485 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.394 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` < `0.1186` → IC=+0.346 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1186 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.357 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.343 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.342)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.348 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.342)

- **PATRÓN** `libro_liquidez` > `4304.5454` → IC=+0.363 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4304.5454 (IC base=+0.342)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.226 (n=743)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=2233)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.207 (n=1032)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1944)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1365` → IC=+0.236 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1365 (IC base=-0.065)

- **PATRÓN** `ibs_15` > `0.6429` → IC=+0.271 (n=724)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6429 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.2663` → IC=+0.192 (n=588)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.2663 (IC base=-0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1224` → IC=+0.251 (n=1433)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1224 (IC base=-0.024)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1804` → IC=+0.247 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1804 (IC base=-0.024)

- **PATRÓN** `ibs_15` < `0.3488` → IC=+0.277 (n=2150)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3488 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.68` → IC=+0.295 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.68 (IC base=-0.024)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.217 (n=451)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1354)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.220 (n=451)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1354)

- **FILTRO** `sigma_ewma_delta_pct` > `23.552` → IC=-0.257 (n=253)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.552
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1552)

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

- **PATRÓN** `ibs_15` < `0.5567` → IC=+0.281 (n=30)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.5567 (IC base=-0.195)

- **PATRÓN** `ballena_activa_n` < `305.0` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 305.0 (IC base=-0.195)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=443)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.152 (n=346)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0066 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.169 (n=309)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.004 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.214 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.147)

- **PATRÓN** `drift_15min` |x|≤ `0.4157` → IC=+0.170 (n=116)

  - _Acción_: Kelly boost +0.85€ cuando `drift_15min` |x|≤ 0.4157 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2962` → IC=+0.221 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2962 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.173 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.6642` → IC=+0.261 (n=345)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6642 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1047` → IC=+0.176 (n=248)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1047 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.1` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 23.1 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=443)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.185 (n=157)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.248 (n=836)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.445` → IC=+0.239 (n=836)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.445 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.7842` → IC=+0.247 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7842 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2077` → IC=+0.253 (n=379)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2077 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.242 (n=320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.2735` → IC=+0.278 (n=736)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2735 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.7586` → IC=+0.315 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7586 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.2` → IC=+0.270 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.2 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.432` → IC=+0.238 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.432 (IC base=+0.234)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.233 (n=238)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=464)

- **FILTRO** `drift_15min` |x|> `0.9054` → IC=-0.268 (n=175)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9054
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=527)

- **PATRÓN** `ibs_15` > `0.9167` → IC=+0.309 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9167 (IC base=-0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0776` → IC=+0.231 (n=325)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0776 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.183` → IC=+0.223 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.183 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.266 (n=365)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.7325` → IC=+0.247 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7325 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.1775` → IC=+0.229 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1775 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.263 (n=419)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=420)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.267 (n=230)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=609)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1401` → IC=+0.292 (n=248)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1401 (IC base=-0.036)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.107` → IC=+0.333 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.107 (IC base=-0.036)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.305 (n=547)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.036)

- **PATRÓN** `dist_vwap_pct` > `0.8964` → IC=+0.343 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8964 (IC base=-0.036)

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
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.301 (n=506)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.324 (n=253)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2394` → IC=+0.304 (n=253)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2394 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2223` → IC=+0.322 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2223 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8411` → IC=+0.329 (n=758)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8411 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.4372` → IC=+0.337 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4372 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.350 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `13022.3239` → IC=+0.298 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13022.3239 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.300 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0549` → IC=+0.330 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0549 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2556` → IC=+0.308 (n=139)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2556 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.310 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.312 (n=439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.319 (n=417)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.357 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.365 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16178.7073` → IC=+0.323 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16178.7073 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.305 (n=301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0518` → IC=+0.310 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0518 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1481` → IC=+0.296 (n=228)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1481 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.326 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.323 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.340 (n=342)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.6363` → IC=+0.310 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6363 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.337 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.296 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2527` → IC=-0.162 (n=72)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2527
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=220)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.138 (n=194)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=66)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6129 sube el IC de +0.193 a +0.272 en UPDOWN_GBM#15min (n=1905). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7141 sube el IC de +0.212 a +0.277 en UPDOWN_GBM#BTC#15min (n=423). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5788 sube el IC de +0.133 a +0.228 en UPDOWN_GBM#ETH#15min (n=446). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.180 a +0.265 en UPDOWN_GBM#SOL#15min (n=228). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5745 sube el IC de +0.199 a +0.289 en UPDOWN_GBM#XRP#15min (n=486). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6429 sube el IC de -0.065 a +0.271 en UPDOWN_GBM_15M_TARDIO (n=724). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3488 sube el IC de -0.024 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=2150). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.085 a +0.328 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=213). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.5567 sube el IC de -0.195 a +0.281 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6642 sube el IC de +0.147 a +0.261 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=345). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2735 sube el IC de +0.234 a +0.278 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=736). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9167 sube el IC de -0.172 a +0.309 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.039 a +0.266 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=365). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.036 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=547). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8411 sube el IC de +0.290 a +0.329 en UPDOWN_GBM_IBS_ALTO (n=758). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.286 a +0.319 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=417). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.294 a +0.340 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=342). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7873 sube el IC de +0.351 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=467). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.357 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=255). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7485 sube el IC de +0.342 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=212). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.105 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.105 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH#15min` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1432 | +0.101 | +209.30€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1432 | +0.101 | +209.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1084 | +0.111 | +180.67€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1084 | +0.111 | +180.67€ | 2 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 4 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 62 | +0.141 | +19.92€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 62 | +0.141 | +19.92€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 30911 | -0.086 | -4077.90€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1608 | -0.025 | -216.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 29303 | -0.089 | -3861.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4033 | -0.104 | -676.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4033 | -0.104 | -676.24€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1608 | -0.025 | -216.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1608 | -0.025 | -216.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3608 | -0.099 | -813.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3608 | -0.099 | -813.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8039 | -0.018 | -785.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8039 | -0.018 | -785.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7591 | -0.093 | -456.90€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7591 | -0.093 | -456.90€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6032 | -0.163 | -1129.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6032 | -0.163 | -1129.10€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 22040 | -0.023 | +3806.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5711 | +0.001 | +1779.82€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 16329 | -0.031 | +2026.90€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 22040 | -0.023 | +3806.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5711 | +0.001 | +1779.82€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 16329 | -0.031 | +2026.90€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 104743 | +0.112 | -5117.56€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15217 | +0.184 | -475.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 435 | -0.065 | -55.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 82463 | +0.101 | -4346.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6628 | +0.106 | -239.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 13701 | +0.100 | -1057.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 49 | -0.147 | +8.51€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 13637 | +0.102 | -1053.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 20990 | +0.130 | -414.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4699 | +0.199 | -147.45€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 13677 | +0.113 | -198.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2572 | +0.097 | -46.24€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 13746 | +0.091 | -1216.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 56 | -0.103 | -7.23€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 13675 | +0.092 | -1197.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 22241 | +0.124 | -429.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6000 | +0.176 | -83.63€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 13826 | +0.105 | -277.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2403 | +0.100 | -59.45€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 20346 | +0.114 | -1172.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4362 | +0.187 | -257.08€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 338 | -0.026 | -1.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 13993 | +0.092 | -779.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1653 | +0.130 | -134.11€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 13719 | +0.099 | -827.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 51 | -0.028 | +11.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 13655 | +0.100 | -838.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 16658 | +0.194 | -1044.37€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 16658 | +0.194 | -1044.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3910 | +0.171 | -384.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3910 | +0.171 | -384.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1612 | +0.204 | -9.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1612 | +0.204 | -9.08€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3858 | +0.181 | -319.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3858 | +0.181 | -319.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3403 | +0.242 | -105.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3403 | +0.242 | -105.09€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3796 | +0.190 | -240.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3796 | +0.190 | -240.18€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 783 | +0.431 | -19.57€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 783 | +0.431 | -19.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 306 | +0.442 | -0.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 306 | +0.442 | -0.51€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 299 | +0.430 | -7.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 299 | +0.430 | -7.44€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 166 | +0.411 | -9.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 166 | +0.411 | -9.18€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 57677 | +0.197 | -4474.94€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 57677 | +0.197 | -4474.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9931 | +0.178 | -1115.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9931 | +0.178 | -1115.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9239 | +0.222 | -352.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9239 | +0.222 | -352.08€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 9955 | +0.174 | -1151.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 9955 | +0.174 | -1151.18€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9323 | +0.218 | -378.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9323 | +0.218 | -378.48€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9551 | +0.203 | -632.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9551 | +0.203 | -632.36€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9678 | +0.192 | -845.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9678 | +0.192 | -845.54€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 21894 | +0.116 | +122.88€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 21894 | +0.116 | +122.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 10869 | +0.119 | +110.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 10869 | +0.119 | +110.46€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 11025 | +0.112 | +12.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 11025 | +0.112 | +12.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1615 | +0.288 | -27.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1615 | +0.288 | -27.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 721 | +0.279 | -18.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 721 | +0.279 | -18.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 780 | +0.286 | -12.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 780 | +0.286 | -12.47€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 114 | +0.345 | +3.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 114 | +0.345 | +3.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 717 | +0.436 | -3.67€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 717 | +0.436 | -3.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 343 | +0.433 | -4.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 343 | +0.433 | -4.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 329 | +0.440 | +0.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 329 | +0.440 | +0.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 45 | +0.394 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 45 | +0.394 | +0.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1238 | +0.065 | -67.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 437 | +0.051 | -40.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 801 | +0.073 | -27.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 64 | +0.121 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 64 | +0.121 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 977 | +0.071 | -37.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 176 | +0.062 | -10.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 801 | +0.073 | -27.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 197 | +0.018 | -34.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 197 | +0.018 | -34.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 41365 | +0.098 | -1188.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3389 | +0.088 | +17.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 37976 | +0.099 | -1205.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 23058 | +0.102 | -344.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3389 | +0.088 | +17.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 19669 | +0.104 | -361.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8015 | +0.109 | -19.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8015 | +0.109 | -19.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 10292 | +0.080 | -825.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 10292 | +0.080 | -825.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 855 | +0.212 | -100.84€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 855 | +0.212 | -100.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 855 | +0.212 | -100.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 855 | +0.212 | -100.84€ | 2 | 4 |
| ✅ GBM_LATE_15M | 29240 | +0.086 | +14347.89€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 29240 | +0.086 | +14347.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4900 | +0.200 | +3706.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4900 | +0.200 | +3706.00€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 4366 | +0.179 | +3137.28€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4366 | +0.179 | +3137.28€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 5160 | +0.198 | +3852.52€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5160 | +0.198 | +3852.52€ | 0 | 23 |
| ✅ GBM_LATE_15M#ETH | 4202 | +0.029 | +1029.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4202 | +0.029 | +1029.45€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 4166 | -0.032 | +932.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4166 | -0.032 | +932.75€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6446 | -0.038 | +1689.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6446 | -0.038 | +1689.88€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 31239 | +0.088 | +16609.79€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 31239 | +0.088 | +16609.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5968 | +0.014 | +3118.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5968 | +0.014 | +3118.72€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6506 | +0.016 | +1392.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6506 | +0.016 | +1392.13€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4438 | +0.266 | +4543.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4438 | +0.266 | +4543.29€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5159 | +0.008 | +1078.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5159 | +0.008 | +1078.66€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5043 | +0.034 | +2009.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5043 | +0.034 | +2009.73€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4125 | +0.280 | +4467.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4125 | +0.280 | +4467.25€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 23506 | +0.171 | +17966.52€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 23506 | +0.171 | +17966.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3537 | +0.212 | +2890.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3537 | +0.212 | +2890.31€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3712 | +0.149 | +2728.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3712 | +0.149 | +2728.48€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3714 | +0.210 | +2983.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3714 | +0.210 | +2983.98€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3947 | +0.135 | +2840.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3947 | +0.135 | +2840.37€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4398 | +0.120 | +3178.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4398 | +0.120 | +3178.12€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4198 | +0.205 | +3345.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4198 | +0.205 | +3345.24€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6255 | +0.137 | +2899.09€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6255 | +0.137 | +2899.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 223 | +0.113 | +100.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 223 | +0.113 | +100.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1791 | +0.138 | +921.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1791 | +0.138 | +921.18€ | 0 | 29 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1888 | +0.152 | +913.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1888 | +0.152 | +913.21€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1473 | +0.116 | +571.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1473 | +0.116 | +571.66€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 29474 | +0.178 | +22494.34€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 29474 | +0.178 | +22494.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4665 | +0.227 | +4069.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4665 | +0.227 | +4069.96€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4603 | +0.151 | +3067.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4603 | +0.151 | +3067.13€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4893 | +0.226 | +4216.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4893 | +0.226 | +4216.44€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4788 | +0.135 | +3331.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4788 | +0.135 | +3331.63€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5160 | +0.119 | +3490.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5160 | +0.119 | +3490.94€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5365 | +0.210 | +4318.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5365 | +0.210 | +4318.24€ | 0 | 24 |
| ✅ GBM_LATE_5M | 8318 | +0.170 | +5445.30€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 8318 | +0.170 | +5445.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1950 | +0.160 | +1380.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1950 | +0.160 | +1380.47€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2715 | +0.175 | +1772.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2715 | +0.175 | +1772.43€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 873 | +0.153 | +489.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 873 | +0.153 | +489.73€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2049 | +0.072 | +765.81€ | 0 | 16 |
| ✅ GBM_LATE_60M#60min | 2049 | +0.072 | +765.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 758 | +0.095 | +277.46€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 758 | +0.095 | +277.46€ | 0 | 17 |
| ✅ GBM_LATE_60M#ETH | 665 | +0.074 | +305.10€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 665 | +0.074 | +305.10€ | 2 | 17 |
| ✅ GBM_LATE_60M#SOL | 626 | +0.043 | +183.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 626 | +0.043 | +183.25€ | 3 | 10 |
| 🚫 GBM_LATE_60M_FADE | 419 | -0.248 | -16.42€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 419 | -0.248 | -16.42€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 157 | -0.217 | -4.98€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 157 | -0.217 | -4.98€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 140 | -0.246 | -4.87€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 140 | -0.246 | -4.87€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 122 | -0.282 | -6.57€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 122 | -0.282 | -6.57€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 821 | +0.089 | +201.53€ | 0 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 821 | +0.089 | +201.53€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 317 | +0.080 | +65.66€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 317 | +0.080 | +65.66€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 261 | +0.055 | +29.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 261 | +0.055 | +29.11€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 243 | +0.137 | +106.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 243 | +0.137 | +106.77€ | 2 | 12 |
| ✅ LATE_WINDOW_5MIN | 114 | +0.250 | +94.41€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 114 | +0.250 | +94.41€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 114 | +0.250 | +94.41€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 114 | +0.250 | +94.41€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2355 | +0.104 | +632.88€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2355 | +0.104 | +632.88€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2355 | +0.104 | +632.88€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2355 | +0.104 | +632.88€ | 0 | 2 |
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
| ✅ LIQUIDACIONES_5M | 2367 | +0.018 | +52.28€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2367 | +0.018 | +52.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 125 | +0.012 | -3.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 125 | +0.012 | -3.55€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 312 | +0.022 | +22.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 312 | +0.022 | +22.29€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 180 | -0.017 | -4.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 180 | -0.017 | -4.39€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 955 | +0.027 | +26.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 955 | +0.027 | +26.49€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 548 | +0.015 | +2.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 548 | +0.015 | +2.42€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 247 | +0.014 | +9.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 247 | +0.014 | +9.02€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1235 | -0.041 | -23.64€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1235 | -0.041 | -23.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 349 | -0.038 | -11.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 349 | -0.038 | -11.91€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 418 | -0.024 | +0.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 418 | -0.024 | +0.63€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 468 | -0.057 | -12.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 468 | -0.057 | -12.36€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 3204 | -0.016 | +81.48€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1510 | -0.017 | +30.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1694 | -0.014 | +51.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 92 | +0.021 | +9.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 47 | +0.071 | +11.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 45 | -0.032 | -1.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 761 | +0.001 | +39.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 355 | +0.001 | +14.20€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 406 | +0.000 | +25.21€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 379 | -0.014 | +16.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 181 | -0.035 | +0.13€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 198 | +0.005 | +16.48€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 639 | -0.041 | -29.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 291 | -0.043 | -15.92€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 348 | -0.040 | -13.72€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 619 | -0.015 | +20.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 300 | -0.020 | +9.89€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 319 | -0.011 | +10.83€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 714 | -0.015 | +25.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 336 | -0.015 | +10.74€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 378 | -0.016 | +14.52€ | 3 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 33534 | -0.005 | +1524.74€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 33534 | -0.005 | +1524.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5935 | +0.021 | +753.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5935 | +0.021 | +753.20€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5085 | -0.031 | -71.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5085 | -0.031 | -71.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6031 | +0.017 | +539.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6031 | +0.017 | +539.54€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4868 | -0.054 | -166.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4868 | -0.054 | -166.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5653 | -0.009 | +203.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5653 | -0.009 | +203.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5962 | +0.011 | +266.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5962 | +0.011 | +266.17€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6045 | -0.061 | -153.00€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6045 | -0.061 | -153.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1459 | -0.085 | -42.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1459 | -0.085 | -42.02€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 686 | -0.125 | -32.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 686 | -0.125 | -32.13€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1785 | -0.078 | -34.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1785 | -0.078 | -34.62€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 84501 | -0.073 | +1749.56€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 84501 | -0.073 | +1749.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 14399 | -0.076 | +843.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 14399 | -0.076 | +843.18€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 12914 | -0.096 | -672.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 12914 | -0.096 | -672.89€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 14667 | -0.067 | +766.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 14667 | -0.067 | +766.01€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 12448 | -0.092 | -222.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 12448 | -0.092 | -222.01€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 15420 | -0.049 | +370.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 15420 | -0.049 | +370.15€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 14653 | -0.063 | +665.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 14653 | -0.063 | +665.11€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7862 | -0.028 | -132.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7862 | -0.028 | -132.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1805 | -0.036 | -10.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1805 | -0.036 | -10.99€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2226 | -0.023 | -27.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2226 | -0.023 | -27.46€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1067 | -0.044 | -18.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1067 | -0.044 | -18.85€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 765 | -0.021 | -24.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 765 | -0.021 | -24.46€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1250 | +0.111 | +437.99€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1114 | +0.117 | +425.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 254 | +0.137 | +126.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 254 | +0.137 | +126.26€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 213 | +0.114 | +65.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 213 | +0.114 | +65.22€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 233 | +0.104 | +84.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 233 | +0.104 | +84.73€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 195 | +0.124 | +84.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 195 | +0.124 | +84.25€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 219 | +0.102 | +64.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 219 | +0.102 | +64.94€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 680 | -0.041 | -49.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 680 | -0.041 | -49.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 136 | +0.000 | +4.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 136 | +0.000 | +4.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 96 | -0.071 | -13.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 96 | -0.071 | -13.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 193 | -0.054 | -21.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 193 | -0.054 | -21.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 142 | -0.028 | -8.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 142 | -0.028 | -8.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 113 | -0.057 | -10.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 113 | -0.057 | -10.94€ | 0 | 0 |
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
| ✅ PRICE_TARGET_GBM_FADE | 794 | -0.200 | -34.62€ | 5 | 0 |
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
| ✅ STREAK_FADE_15M | 572 | +0.031 | +16.67€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 572 | +0.031 | +16.67€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 279 | +0.027 | +2.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 279 | +0.027 | +2.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 62 | +0.000 | -1.18€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 62 | +0.000 | -1.18€ | 2 | 1 |
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
| ✅ STREAK_MOM_5M | 8874 | +0.022 | +123.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8874 | +0.022 | +123.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2446 | +0.024 | +31.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2446 | +0.024 | +31.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2018 | +0.031 | +51.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2018 | +0.031 | +51.88€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2690 | +0.013 | +9.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2690 | +0.013 | +9.20€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1720 | +0.023 | +30.54€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1720 | +0.023 | +30.54€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8016 | +0.013 | -38.43€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8016 | +0.013 | -38.43€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3197 | +0.017 | -6.33€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3197 | +0.017 | -6.33€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3177 | +0.013 | -18.03€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3177 | +0.013 | -18.03€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1642 | +0.007 | -14.08€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1642 | +0.007 | -14.08€ | 2 | 0 |
| ✅ UPDOWN_GBM | 46043 | +0.037 | +3061.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 11942 | +0.073 | +2294.74€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1615 | +0.004 | +6.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 29537 | +0.028 | +735.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2779 | +0.003 | +25.30€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4661 | +0.075 | +579.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 852 | +0.162 | +377.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3776 | +0.056 | +202.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 8852 | +0.045 | +679.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1561 | +0.087 | +357.77€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 433 | +0.013 | +4.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 5537 | +0.046 | +284.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1257 | +0.004 | +31.66€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 64 | -0.091 | +0.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 5306 | +0.043 | +354.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 803 | +0.141 | +290.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4475 | +0.026 | +66.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 10101 | +0.027 | +450.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3019 | +0.051 | +347.05€ | 1 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 426 | +0.007 | +7.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 5661 | +0.021 | +100.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 939 | -0.001 | -7.89€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 56 | -0.121 | +3.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 10417 | +0.017 | +294.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2869 | +0.028 | +207.90€ | 0 | 13 |
| ✅ UPDOWN_GBM#SOL#240min | 417 | -0.004 | -1.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6500 | +0.016 | +89.98€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 583 | +0.004 | +1.53€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 48 | -0.160 | -3.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 6704 | +0.041 | +703.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2838 | +0.088 | +714.12€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 278 | +0.000 | -3.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3588 | +0.006 | -7.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 168 | -0.123 | +1.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 622 | +0.351 | +209.42€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 622 | +0.351 | +209.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 340 | +0.357 | +113.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 340 | +0.357 | +113.04€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 282 | +0.342 | +96.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 282 | +0.342 | +96.38€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 13673 | -0.033 | +3021.49€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 13673 | -0.033 | +3021.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 953 | -0.049 | +376.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 953 | -0.049 | +376.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2504 | -0.117 | +50.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2504 | -0.117 | +50.88€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 505 | +0.196 | +371.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 505 | +0.196 | +371.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1574 | +0.209 | +961.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1574 | +0.209 | +961.89€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4087 | -0.062 | +590.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4087 | -0.062 | +590.80€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4050 | -0.071 | +669.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4050 | -0.071 | +669.71€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 157 | +0.035 | +7.28€ | 1 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 157 | +0.035 | +7.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 157 | +0.035 | +7.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 157 | +0.035 | +7.28€ | 1 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1010 | +0.290 | +812.45€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1010 | +0.290 | +812.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 555 | +0.286 | +425.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 555 | +0.286 | +425.35€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 455 | +0.294 | +387.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 455 | +0.294 | +387.10€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 742 | -0.112 | -82.95€ | 3 | 0 |
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
  - _Estado_: Spread bajo (0.054) — sin ventaja clara. oversold(IBS<0.3): IC=+0.049 n=16216 | neutral: IC=+0.036 n=17150 | overbought(IBS>0.7): IC=+0.090 n=16436
  - _Datos_: n=51596 IC=+0.059 PNL=+6573.06€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 580 celda(s) pasan gate riguroso completo de 2344 evaluadas (n>=40) y 3322 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.028 < 0.08 — monitorear
  - _Datos_: n=2869 IC=+0.028 PNL=+207.90€

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
  - _Estado_: 45981 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.129 n=416/60 | contraria IC=+0.177 n=391 | gap=-0.048 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=336, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 195 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=939/40 IC=-0.001 PNL=-7.89€ | BTC#60min: n=1257/40 IC=+0.004 PNL=+31.66€ | SOL#60min: n=583/40 IC=+0.004 PNL=+1.53€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=385529 | tras_1loss IC=+0.084 n=297642 | tras_2loss IC=+0.053 n=123855/40 | gap=-0.004 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.018 n=5628 | contrario_BTC IC=+0.036 n=4972/40 | gap=+0.017 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: n=44030 IC=+0.036 PNL=+2923.65€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=44030 IC=+0.036 PNL=+2923.65€

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
  - _Estado_: n=1917 IC=+0.004 PNL=-3.87€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1917 IC=+0.004 PNL=-3.87€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=862 IC=-0.001 PNL=+29.17€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=862 IC=-0.001 PNL=+29.17€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.193 > 0.1 con n=2538 PNL=+1665.44€
  - _Datos_: n=2538 IC=+0.193 PNL=+1665.44€

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
  - _Estado_: n=1561 IC=+0.087 PNL=+357.77€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1561 IC=+0.087 PNL=+357.77€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=6798 PNL=+1710.84€
  - _Datos_: n=6798 IC=+0.090 PNL=+1710.84€

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
  - _Estado_: n=305 IC=-0.034 PNL=-3.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=305 IC=-0.034 PNL=-3.32€

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
  - _Estado_: n=6259 IC=-0.000 PNL=+3.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6259 IC=-0.000 PNL=+3.83€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.250 n=114) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=114 IC=+0.250 PNL=+94.41€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=8441 IC=+0.040 PNL=+558.23€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=8441 IC=+0.040 PNL=+558.23€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=2831 IC=+0.057 PNL=+349.06€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2831 IC=+0.057 PNL=+349.06€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.151 > 0.08 con n=714 PNL=+189.28€
  - _Datos_: n=714 IC=+0.151 PNL=+189.28€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.106 > 0.08 con n=544 PNL=+254.64€
  - _Datos_: n=544 IC=+0.106 PNL=+254.64€

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
  - _Estado_: n=6811 IC=+0.042 PNL=+533.70€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6811 IC=+0.042 PNL=+533.70€

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
  - _Estado_: n=16712 IC=+0.058 PNL=+2066.34€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=16712 IC=+0.058 PNL=+2066.34€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.204 > 0.1 con n=4120 PNL=+2296.37€
  - _Datos_: n=4120 IC=+0.204 PNL=+2296.37€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.149 < -0.1 con n=277 PNL=+28.67€
  - _Datos_: n=277 IC=-0.149 PNL=+28.67€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2190 IC=+0.056 PNL=+231.88€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2190 IC=+0.056 PNL=+231.88€

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
  - _Estado_: n=21034 IC=-0.136 PNL=+1516.71€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=21034 IC=-0.136 PNL=+1516.71€

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
  - _Estado_: n=2206 IC=+0.139 PNL=+1256.77€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2206 IC=+0.139 PNL=+1256.77€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.08 con n=2499 PNL=+1652.80€
  - _Datos_: n=2499 IC=+0.194 PNL=+1652.80€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.211 > 0.08 con n=563 PNL=+297.76€
  - _Datos_: n=563 IC=+0.211 PNL=+297.76€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.232 < -0.1 con n=2073 PNL=-187.35€
  - _Datos_: n=2073 IC=-0.232 PNL=-187.35€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=6173 IC=+0.179 PNL=+4296.35€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=6173 IC=+0.179 PNL=+4296.35€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.093 > 0.08 con n=84 PNL=+27.18€
  - _Datos_: n=84 IC=+0.093 PNL=+27.18€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2234 IC=+0.069 PNL=+688.41€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2234 IC=+0.069 PNL=+688.41€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.08 con n=2037 PNL=+1442.45€
  - _Datos_: n=2037 IC=+0.180 PNL=+1442.45€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3383 IC=-0.032 PNL=+874.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3383 IC=-0.032 PNL=+874.94€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.238 > 0.08 con n=3647 PNL=-318.77€
  - _Datos_: n=3647 IC=+0.238 PNL=-318.77€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1198) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1198 IC=+0.102 PNL=+283.69€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.08 con n=306 PNL=+107.39€
  - _Datos_: n=306 IC=+0.334 PNL=+107.39€

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
  - _Estado_: n=9931 IC=+0.178 PNL=-1115.30€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=9931 IC=+0.178 PNL=-1115.30€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.204 > 0.1 con n=157 PNL=+95.67€
  - _Datos_: n=157 IC=+0.204 PNL=+95.67€
