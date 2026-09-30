# Hipótesis automáticas — 2026-09-30 21:26 UTC
_Generado por shadow_postmortem.py sobre 687693 resoluciones (PNL=+81598.85€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=556)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.237 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `74.0` → IC=+0.213 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 74.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.803` → IC=+0.257 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.803 (IC base=+0.140)

- **PATRÓN** `banda_z` > `9.563` → IC=+0.197 (n=193)

  - _Acción_: Kelly boost +0.99€ cuando `banda_z` > 9.563 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.160 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 11.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=611)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2242.094` → IC=+0.151 (n=516)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2242.094 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=556)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.057)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.138 (n=172)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.260 (n=443)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=421)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.260 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.148)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.209 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.148)

- **PATRÓN** `banda_hit_calibrado` > `0.7998` → IC=+0.268 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7998 (IC base=+0.148)

- **PATRÓN** `banda_z` > `10.429` → IC=+0.211 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.429 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.171 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=520)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `3319.4656` → IC=+0.155 (n=308)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3319.4656 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.140 (n=170)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 94.0 (IC base=+0.060)

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
- **FILTRO** `restante_s_al_confirmar` < `145.68` → IC=-0.218 (n=7759)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.68
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=23283)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `136.42` → IC=-0.252 (n=1015)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 136.42
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3045)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `127.03` → IC=-0.307 (n=909)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.03
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2729)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.71` → IC=-0.205 (n=1908)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.71
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=5724)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `126.94` → IC=-0.329 (n=1510)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 126.94
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=4530)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.210 (n=15208)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=3715)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5542.3853` → IC=+0.173 (n=2396)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 5542.3853 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=13055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=15856)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.230 (n=12251)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=6068)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7747.6147` → IC=+0.168 (n=2317)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7747.6147 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=1745)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.204 (n=1790)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `15969.9705` → IC=+0.231 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15969.9705 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.199 (n=1617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=1804)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.295 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2307)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `15900.7734` → IC=+0.210 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15900.7734 (IC base=+0.195)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.171 (n=357)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.615 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `4988.4492` → IC=+0.141 (n=218)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 4988.4492 (IC base=+0.093)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.148 (n=396)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.101)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.144 (n=882)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5784.0902` → IC=+0.152 (n=228)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 5784.0902 (IC base=+0.101)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=3139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.348 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` < `0.23` → IC=+0.365 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.23 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.232 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.227)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.137 (n=744)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.249 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=845)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1318.0949` → IC=+0.146 (n=739)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1318.0949 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.078)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.406 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.154 (n=591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.160 (n=630)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=779)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.227 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=13101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=12502)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.230 (n=4183)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `5024.6381` → IC=+0.336 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5024.6381 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.174 (n=2944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=2951)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=2976)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.249 (n=1155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.243 (n=1147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.344 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.241)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.189 (n=2907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=2929)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=2475)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=2706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.327 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.314 (n=57)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=2994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.191 (n=2878)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 17.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.192 (n=2256)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.194 (n=1101)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.73 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `11452.1989` → IC=+0.460 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11452.1989 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.445 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.446 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.454 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `14504.3208` → IC=+0.449 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14504.3208 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.443 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.464 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `3369.9988` → IC=+0.447 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3369.9988 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.414 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.411)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.413 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.411)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.426 (n=66)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=39054)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.237 (n=17173)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=6721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=5374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=7319)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=7038)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.265 (n=3977)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=7109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=7088)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=3523)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.267 (n=2396)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=6480)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.258 (n=2563)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=6529)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=2992)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=5934)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5663)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=7289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.52` → IC=+0.137 (n=5511)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.52 (IC base=+0.115)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=2987)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.125 (n=2752)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.16 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.138 (n=2801)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.133 (n=3159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.24` → IC=+0.139 (n=2740)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.24 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.183 (n=2947)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.38 (IC base=+0.112)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.131 (n=3128)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.112)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.137 (n=2797)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.25 (IC base=+0.112)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=869)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1545.7265` → IC=+0.295 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1545.7265 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.293 (n=572)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.348 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `5115.2204` → IC=+0.320 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5115.2204 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.323 (n=416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=615)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1447.2132` → IC=+0.305 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1447.2132 (IC base=+0.287)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.441 (n=542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.436 (n=480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.437 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.440 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.436 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.456 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.925` → IC=+0.454 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.925 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.439 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `1966.3827` → IC=+0.457 (n=113)

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
- **PATRÓN** `drift_60min` |x|≤ `0.495` → IC=+0.129 (n=9272)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.495 (IC base=+0.112)

- **PATRÓN** `ibs_20min` > `0.9831` → IC=+0.244 (n=3092)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9831 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.2184` → IC=+0.259 (n=2063)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2184 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.993` → IC=+0.181 (n=3529)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.993 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.854` → IC=+0.254 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.854 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` > `0.6148` → IC=+0.256 (n=2564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6148 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.3019` → IC=+0.231 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3019 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `2.3272` → IC=+0.218 (n=2918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3272 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.5682` → IC=+0.135 (n=11257)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5682 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.6054` → IC=+0.203 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6054 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.1571` → IC=+0.177 (n=3726)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1571 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.187 (n=1779)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6973 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `0.8688` → IC=+0.178 (n=2695)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.8688 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.167` → IC=+0.225 (n=1944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.167 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.200 (n=6899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.214 (n=6699)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 125.0 (IC base=+0.068)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.206 (n=695)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.182 (n=694)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0081 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3565` → IC=+0.179 (n=2069)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3565 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=999)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.179 (n=1387)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 11.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.206` → IC=+0.273 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.206 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.214 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.176 (n=1949)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.191 (n=2102)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.243 (n=1457)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0903` → IC=+0.275 (n=544)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0903 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.242 (n=1481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0571` → IC=+0.285 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0571 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.526` → IC=+0.247 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.526 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.448` → IC=+0.241 (n=1702)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.448 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.269 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.5798` → IC=+0.245 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5798 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1563.08` → IC=+0.244 (n=1631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1563.08 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.238 (n=719)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.357` → IC=+0.228 (n=1632)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.357 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.239 (n=1637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.220 (n=1663)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.8976` → IC=+0.263 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8976 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.3461` → IC=+0.223 (n=1525)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3461 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.604` → IC=+0.255 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.604 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2558` → IC=+0.223 (n=1632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2558 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6193` → IC=+0.223 (n=1632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6193 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.244 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.3817` → IC=+0.239 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3817 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `11046.4721` → IC=+0.225 (n=1632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11046.4721 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.166 (n=1110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0038 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2557` → IC=+0.149 (n=1464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.2557 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=753)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.3382` → IC=+0.196 (n=1109)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.3382 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1308` → IC=+0.154 (n=1507)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1308 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.356` → IC=+0.153 (n=263)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 11.356 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.303` → IC=+0.145 (n=1533)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.303 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.149 (n=1663)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2089 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.8607` → IC=+0.141 (n=1110)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.8607 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1566` → IC=+0.181 (n=440)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1566 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.149 (n=1553)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.77` → IC=+0.150 (n=1035)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.77 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `14091.9548` → IC=+0.142 (n=1109)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 14091.9548 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.173 (n=649)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 231.0 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.209 (n=692)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.195 (n=2078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=1868)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.305` → IC=+0.258 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.305 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.193 (n=1821)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.203 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.7724` → IC=+0.198 (n=1776)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.7724 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2469)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `1996.9984` → IC=+0.193 (n=692)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 1996.9984 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.219 (n=1600)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6333` → IC=+0.215 (n=1818)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6333 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=847)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0636` → IC=+0.240 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0636 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.693` → IC=+0.229 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.693 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.57` → IC=+0.212 (n=1968)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.57 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3484` → IC=+0.248 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3484 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7289` → IC=+0.211 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7289 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.1534` → IC=+0.214 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1534 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1986.95` → IC=+0.217 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1986.95 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.212 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=114)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=2499)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.151 (n=402)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0037 (IC base=+0.041)

- **PATRÓN** `ibs_20min` > `0.9556` → IC=+0.225 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9556 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` < `0.553` → IC=+0.337 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.553 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.854` → IC=+0.171 (n=825)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 4.854 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.342 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8553 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.343 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2985` → IC=+0.361 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2985 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.361 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4124 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `1.8361` → IC=+0.333 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8361 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.335 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.1017` → IC=+0.152 (n=654)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1017 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.6717` → IC=+0.204 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6717 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.8475` → IC=+0.155 (n=664)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8475 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.1639` → IC=+0.147 (n=332)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1639 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.208 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.518` → IC=+0.166 (n=841)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.518 (IC base=+0.022)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=377)

- **FILTRO** `ibs_20min` < `0.3056` → IC=-0.208 (n=111)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3056
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=336)

- **FILTRO** `ibs_20min` > `0.2424` → IC=-0.125 (n=2509)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2424
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=1237)

- **FILTRO** `sigma_ewma_delta_pct` > `8.716` → IC=-0.210 (n=394)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.716
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3352)

- **PATRÓN** `ibs_20min` > `0.6129` → IC=+0.164 (n=224)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.6129 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `1.695` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.695 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.6571` → IC=+0.289 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6571 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `1.0815` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0815 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.4963` → IC=+0.284 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4963 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `1.4704` → IC=+0.270 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4704 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.293 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.2424` → IC=+0.130 (n=1237)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.2424 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7235` → IC=+0.250 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7235 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.4505` → IC=+0.241 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4505 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` < `0.6806` → IC=+0.274 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6806 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1591` → IC=+0.298 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1591 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.286 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.041)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6579` → IC=-0.184 (n=649)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6579
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1958)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.207 (n=595)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2012)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.207 (n=954)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=2929)

- **PATRÓN** `dist_vwap_pct` > `0.7959` → IC=+0.326 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7959 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.21` → IC=+0.322 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.21 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` < `0.9729` → IC=+0.297 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9729 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.314 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.305 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `2.442` → IC=+0.305 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.442 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.8027` → IC=+0.305 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8027 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.5658` → IC=+0.279 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5658 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` < `0.7265` → IC=+0.259 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7265 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.280 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.1677` → IC=+0.269 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1677 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `2.1399` → IC=+0.261 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1399 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.5237` → IC=+0.256 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5237 (IC base=-0.017)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.198 (n=3986)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0098 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4733` → IC=+0.187 (n=10676)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4733 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `1.018` → IC=+0.291 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.018 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.64` → IC=+0.158 (n=5487)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.64 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.1808` → IC=+0.244 (n=4316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1808 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.691` → IC=+0.255 (n=3856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.691 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.271 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `1.4638` → IC=+0.241 (n=2323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4638 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.268` → IC=+0.252 (n=3158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.268 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.274 (n=6493)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.169 (n=3882)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0092 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5459` → IC=+0.157 (n=10240)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5459 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.7158` → IC=+0.249 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7158 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2507` → IC=+0.248 (n=3358)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2507 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.7084` → IC=+0.248 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7084 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.2011` → IC=+0.257 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2011 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.304 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5907` → IC=+0.274 (n=2097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5907 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.278 (n=4643)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 81.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2578` → IC=-0.149 (n=826)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2578
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=2479)

- **FILTRO** `ibs_20min` > `0.7566` → IC=-0.158 (n=676)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7566
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2029)

- **FILTRO** `sigma_ewma_delta_pct` > `4.561` → IC=-0.172 (n=613)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.561
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2092)

- **PATRÓN** `ibs_20min` > `0.8974` → IC=+0.276 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8974 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.272` → IC=+0.199 (n=589)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 7.272 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.269 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4393` → IC=+0.201 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4393 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.1694` → IC=+0.222 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1694 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.220 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.2221` → IC=+0.438 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2221 (IC base=-0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.1456` → IC=+0.442 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1456 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4701` → IC=+0.446 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4701 (IC base=-0.022)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.471 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8648` → IC=+0.165 (n=800)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8648 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.299` → IC=+0.187 (n=420)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.299 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6774` → IC=+0.178 (n=990)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6774 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.233 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.199 (n=363)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.4028` → IC=+0.174 (n=363)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.4028 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.221 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 234.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.226 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `0.8583` → IC=+0.235 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8583 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2677` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2677 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5529` → IC=+0.223 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5529 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.246 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `455.0` → IC=+0.222 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 455.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.283 (n=1226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.252)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.256 (n=1851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.252 (n=1857)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.252)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.281 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` < `0.0997` → IC=+0.266 (n=1570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0997 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` > `2.192` → IC=+0.265 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.192 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.263 (n=2164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.252)

- **PATRÓN** `libro_liquidez` > `1917.67` → IC=+0.266 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.67 (IC base=+0.252)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.317 (n=686)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.1847` → IC=+0.296 (n=665)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1847 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.324 (n=510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.3548` → IC=+0.291 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3548 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.7` → IC=+0.291 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.7 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.805` → IC=+0.287 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.805 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.195` → IC=+0.280 (n=1454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.195 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.1203` → IC=+0.289 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1203 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` < `1.5792` → IC=+0.297 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5792 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.6641` → IC=+0.290 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6641 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `1910.1836` → IC=+0.302 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.1836 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.289 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.285)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7744` → IC=-0.189 (n=692)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7744
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=2078)

- **PATRÓN** `ibs_20min` > `0.9077` → IC=+0.184 (n=609)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.9077 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.187` → IC=+0.235 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.187 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.0011` → IC=+0.250 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0011 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.0834` → IC=+0.258 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0834 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4024` → IC=+0.268 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4024 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.7595` → IC=+0.239 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7595 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.260 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 144.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1481` → IC=+0.222 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1481 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.1663` → IC=+0.215 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1663 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.808` → IC=+0.259 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.808 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1331` → IC=+0.233 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1331 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.258 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7547` → IC=-0.186 (n=1267)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7547
  - _Potencial_: sin este filtro IC_bueno=+0.283 (n=1269)

- **FILTRO** `ibs_20min` > `0.6774` → IC=-0.235 (n=633)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6774
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=1907)

- **FILTRO** `sigma_ewma_delta_pct` > `4.709` → IC=-0.192 (n=553)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.709
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=1987)

- **PATRÓN** `ibs_20min` > `0.7547` → IC=+0.283 (n=1269)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7547 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `1.0905` → IC=+0.329 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0905 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.678` → IC=+0.166 (n=402)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.678 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8622` → IC=+0.307 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8622 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.6364` → IC=+0.303 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6364 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.0998` → IC=+0.301 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0998 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.4306` → IC=+0.321 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4306 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.325 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.5773` → IC=+0.128 (n=1677)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.5773 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` < `0.2236` → IC=+0.236 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2236 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.262 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7056 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.222 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.239 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.4547` → IC=+0.242 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4547 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.256 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.019)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.325 (n=1350)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.298 (n=707)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` > `0.6321` → IC=+0.310 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6321 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2186` → IC=+0.313 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2186 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.69` → IC=+0.301 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.69 (IC base=+0.279)

- **PATRÓN** `volumen_regimen` > `0.6263` → IC=+0.292 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6263 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.328 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `1.4303` → IC=+0.290 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4303 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.283 (n=1517)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `2464.8952` → IC=+0.290 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2464.8952 (IC base=+0.279)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.318 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.309 (n=1068)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.1967` → IC=+0.289 (n=705)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1967 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.294 (n=548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` < `0.1379` → IC=+0.334 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1379 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.3215` → IC=+0.290 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3215 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` < `0.2317` → IC=+0.282 (n=1471)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2317 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.095` → IC=+0.306 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.095 (IC base=+0.282)

- **PATRÓN** `volumen_regimen` < `0.6412` → IC=+0.286 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6412 (IC base=+0.282)

- **PATRÓN** `volumen_regimen` > `1.243` → IC=+0.312 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.243 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.235` → IC=+0.335 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.235 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` < `1.4234` → IC=+0.290 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4234 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `2.139` → IC=+0.280 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.139 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `2411.6046` → IC=+0.286 (n=1432)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2411.6046 (IC base=+0.282)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.177 (n=3013)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0048 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.204 (n=3012)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.3662` → IC=+0.178 (n=7951)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3662 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=9459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.223 (n=9044)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.1761` → IC=+0.194 (n=3878)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1761 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.381` → IC=+0.252 (n=1827)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.381 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.2091` → IC=+0.163 (n=6012)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2091 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.160 (n=6012)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6285 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.199 (n=1342)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5597` → IC=+0.169 (n=3822)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5597 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.6068` → IC=+0.177 (n=2896)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.6068 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `1954.82` → IC=+0.173 (n=8071)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 1954.82 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.185 (n=7954)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 109.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.185 (n=5801)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0822` → IC=+0.212 (n=2903)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0822 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=3348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4851` → IC=+0.226 (n=8701)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4851 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.1761` → IC=+0.166 (n=6099)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1761 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.197 (n=1461)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1764` → IC=+0.158 (n=6254)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1764 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.216 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5561` → IC=+0.171 (n=3525)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5561 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.6045` → IC=+0.173 (n=2670)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6045 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.179 (n=7670)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 109.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.231 (n=510)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.200 (n=508)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.3449` → IC=+0.215 (n=1515)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3449 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=1601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.202 (n=1017)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.9061` → IC=+0.284 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9061 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.192` → IC=+0.310 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.192 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.2305` → IC=+0.246 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2305 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `1.4332` → IC=+0.191 (n=1411)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.4332 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.208 (n=1544)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.241 (n=1019)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.246 (n=1033)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1848` → IC=+0.284 (n=771)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1848 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=1035)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=572)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.3503` → IC=+0.258 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3503 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.288` → IC=+0.246 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.288 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.256 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4206` → IC=+0.259 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4206 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1560.5772` → IC=+0.248 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1560.5772 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.237 (n=455)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.192 (n=453)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.183 (n=1365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.3944` → IC=+0.224 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3944 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.1993` → IC=+0.209 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1993 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.223 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.172 (n=598)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6892 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.0769` → IC=+0.160 (n=615)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.0769 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.204 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.5038` → IC=+0.181 (n=581)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5038 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.4711` → IC=+0.158 (n=440)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4711 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `11874.9267` → IC=+0.162 (n=1212)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11874.9267 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `383.0` → IC=+0.158 (n=1125)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 383.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.159 (n=1449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0057 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2936` → IC=+0.165 (n=1447)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2936 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.171 (n=698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.140 (n=684)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.5859` → IC=+0.190 (n=1447)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5859 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.889` → IC=+0.203 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.889 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2113` → IC=+0.158 (n=1447)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2113 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.150 (n=441)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.449` → IC=+0.146 (n=1336)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.449 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.4211` → IC=+0.139 (n=1335)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4211 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `209.0` → IC=+0.168 (n=419)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 209.0 (IC base=+0.139)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.222 (n=684)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.2509` → IC=+0.220 (n=1006)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2509 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.451` → IC=+0.278 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.451 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2012` → IC=+0.212 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2012 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.7909` → IC=+0.202 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7909 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `2.7374` → IC=+0.213 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7374 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1782)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `1991.3` → IC=+0.207 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1991.3 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.233 (n=1140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1023` → IC=+0.260 (n=432)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1023 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.274 (n=445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.3521` → IC=+0.245 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3521 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.666` → IC=+0.254 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.666 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2891` → IC=+0.246 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2891 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7487` → IC=+0.226 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7487 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.1766` → IC=+0.225 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1766 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.219 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1912.2459` → IC=+0.222 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.2459 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.214 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.218)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.179 (n=1280)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0065 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4326` → IC=+0.163 (n=1452)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4326 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.3502` → IC=+0.199 (n=1452)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3502 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1502` → IC=+0.181 (n=940)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1502 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.936` → IC=+0.224 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.936 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8532` → IC=+0.161 (n=968)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8532 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2914` → IC=+0.196 (n=225)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2914 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4299` → IC=+0.158 (n=474)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4299 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5102` → IC=+0.170 (n=473)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5102 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5311.2129` → IC=+0.191 (n=968)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 5311.2129 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.151 (n=1389)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 157.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.158 (n=1528)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0072 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3891` → IC=+0.148 (n=1528)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3891 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6584` → IC=+0.174 (n=1528)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.6584 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.1588` → IC=+0.143 (n=1498)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1588 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.957` → IC=+0.160 (n=534)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 6.957 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.8548` → IC=+0.151 (n=1019)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8548 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.183 (n=228)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8013` → IC=+0.140 (n=936)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8013 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.5177` → IC=+0.128 (n=468)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.5177 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `9409.9269` → IC=+0.166 (n=693)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 9409.9269 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `129.0` → IC=+0.127 (n=1183)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 129.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.161 (n=749)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0101 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.5045` → IC=+0.209 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5045 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.0933` → IC=+0.215 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0933 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.836` → IC=+0.258 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.836 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.2151` → IC=+0.134 (n=1647)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2151 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.127 (n=1656)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.124 (n=687)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.5436` → IC=+0.137 (n=700)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.5436 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=1721)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2883.9504` → IC=+0.202 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2883.9504 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.142 (n=1276)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 47.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.164 (n=737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0062 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1071` → IC=+0.168 (n=558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1071 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.216 (n=1674)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.2134` → IC=+0.147 (n=1546)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2134 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.617` → IC=+0.135 (n=349)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 7.617 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6381` → IC=+0.152 (n=558)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6381 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.168 (n=209)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4487` → IC=+0.146 (n=507)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4487 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4212` → IC=+0.135 (n=507)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4212 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2743.5149` → IC=+0.174 (n=758)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2743.5149 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.127 (n=1460)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 52.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.225 (n=1392)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.1834` → IC=+0.208 (n=686)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1834 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.208 (n=700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.243 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.5272` → IC=+0.211 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5272 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.3027` → IC=+0.201 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3027 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.596` → IC=+0.241 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.596 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2016` → IC=+0.207 (n=1558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2016 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.213 (n=1558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.266 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.210 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.7991` → IC=+0.209 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7991 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2449.1286` → IC=+0.201 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2449.1286 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.227 (n=708)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.218 (n=731)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.233 (n=537)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=742)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.02` → IC=+0.299 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.02 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `1.2326` → IC=+0.222 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2326 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.409` → IC=+0.252 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.409 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.7024` → IC=+0.217 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7024 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.282 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `2.1966` → IC=+0.202 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1966 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4348` → IC=+0.206 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4348 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2382.2656` → IC=+0.215 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2382.2656 (IC base=+0.210)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.189 (n=1038)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0043 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.173 (n=781)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0086 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.3484` → IC=+0.169 (n=2059)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3484 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.205 (n=1173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.5066` → IC=+0.197 (n=2090)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.5066 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.816` → IC=+0.181 (n=377)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.816 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.1496` → IC=+0.166 (n=1738)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1496 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.731` → IC=+0.189 (n=1032)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.731 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.8708` → IC=+0.185 (n=1395)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8708 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.2058` → IC=+0.175 (n=697)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.2058 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.1634` → IC=+0.177 (n=630)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1634 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.4378` → IC=+0.173 (n=757)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4378 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.8216` → IC=+0.170 (n=1511)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8216 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.168 (n=2658)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.02 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `2677.4245` → IC=+0.169 (n=2090)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2677.4245 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.178 (n=2118)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 144.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.144 (n=1604)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0056 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.3457` → IC=+0.129 (n=2117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3457 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=2260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.0613` → IC=+0.193 (n=802)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0613 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2142` → IC=+0.121 (n=2180)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` < 0.2142 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2227` → IC=+0.121 (n=2188)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2227 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.1648` → IC=+0.140 (n=595)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.1648 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4426` → IC=+0.150 (n=776)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4426 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2778.617` → IC=+0.124 (n=2149)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2778.617 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.135 (n=1005)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 28.0 (IC base=+0.113)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.178 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0029 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3325` → IC=+0.156 (n=602)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3325 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.184 (n=558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.6508` → IC=+0.210 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6508 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.2846` → IC=+0.170 (n=207)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.2846 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.145 (n=528)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.137` → IC=+0.156 (n=271)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.137 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.835` → IC=+0.141 (n=628)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.835 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.9016` → IC=+0.173 (n=402)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.9016 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.155` → IC=+0.141 (n=627)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.155 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0914` → IC=+0.154 (n=212)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0914 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.2054` → IC=+0.151 (n=517)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.2054 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.5058` → IC=+0.144 (n=524)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5058 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=778)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `10611.6905` → IC=+0.157 (n=602)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 10611.6905 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `161.0` → IC=+0.173 (n=255)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 161.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.208 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3426` → IC=+0.158 (n=756)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3426 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.151 (n=722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6155` → IC=+0.179 (n=665)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6155 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1841` → IC=+0.154 (n=752)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1841 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.351` → IC=+0.149 (n=283)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.351 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.114` → IC=+0.139 (n=693)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.114 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2242` → IC=+0.146 (n=756)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2242 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.7151` → IC=+0.150 (n=675)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.7151 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.214 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1106` → IC=+0.155 (n=657)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1106 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4106` → IC=+0.147 (n=746)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4106 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `361.0` → IC=+0.148 (n=725)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 361.0 (IC base=+0.138)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.264 (n=328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.209 (n=249)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.4065` → IC=+0.216 (n=742)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4065 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=778)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.6705` → IC=+0.251 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6705 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.1466` → IC=+0.215 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1466 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.064` → IC=+0.235 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.064 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.8322` → IC=+0.216 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8322 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `1.1625` → IC=+0.232 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1625 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.155` → IC=+0.253 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.155 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.4105` → IC=+0.232 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4105 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.4427` → IC=+0.248 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4427 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.212 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.124 (n=610)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0062 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.121 (n=473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 11.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.0866` → IC=+0.148 (n=231)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.0866 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.6865` → IC=+0.151 (n=305)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6865 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.142 (n=107)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `3863.6748` → IC=+0.123 (n=618)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 3863.6748 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.125 (n=222)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 34.0 (IC base=+0.095)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.154 (n=512)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0058 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.178 (n=526)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.261 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.9964` → IC=+0.236 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9964 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.496` → IC=+0.188 (n=299)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.496 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.069` → IC=+0.157 (n=502)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.069 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.7219` → IC=+0.146 (n=510)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7219 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1735` → IC=+0.163 (n=158)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1735 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.2097` → IC=+0.169 (n=249)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2097 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=601)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2963.2526` → IC=+0.186 (n=259)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2963.2526 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.56` → IC=+0.142 (n=540)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.56 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.7083` → IC=+0.129 (n=238)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.7083 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `2.4397` → IC=+0.123 (n=512)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4397 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `2514.2377` → IC=+0.135 (n=360)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2514.2377 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.135 (n=485)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 40.0 (IC base=+0.088)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.175 (n=3905)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0047 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.209 (n=3902)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=12242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.220 (n=11687)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4615 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.9309` → IC=+0.202 (n=1638)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9309 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.363` → IC=+0.246 (n=2897)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.363 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `0.8801` → IC=+0.172 (n=5223)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8801 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.200 (n=1587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.5852` → IC=+0.195 (n=3759)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.5852 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `1791.0969` → IC=+0.178 (n=11683)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1791.0969 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.200 (n=9108)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.193 (n=7041)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.007 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.3933` → IC=+0.188 (n=9294)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3933 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=3994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.4493` → IC=+0.247 (n=9291)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4493 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2526` → IC=+0.163 (n=6599)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2526 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.063` → IC=+0.205 (n=1492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.063 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.751` → IC=+0.183 (n=10183)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.751 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.7053` → IC=+0.163 (n=3165)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7053 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.243 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6017` → IC=+0.193 (n=3265)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6017 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.201 (n=6385)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.231 (n=652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.226 (n=648)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.3632` → IC=+0.204 (n=1943)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3632 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.222 (n=934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=1311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.333 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.354 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2734` → IC=+0.260 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2734 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `2.5626` → IC=+0.210 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5626 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=1957)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.259 (n=1055)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.263 (n=1583)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1272` → IC=+0.283 (n=695)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1272 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3558` → IC=+0.281 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3558 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.339` → IC=+0.260 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.339 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.467` → IC=+0.260 (n=1658)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.467 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.294 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.549` → IC=+0.259 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.549 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.621` → IC=+0.274 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.621 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1563.08` → IC=+0.268 (n=1580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1563.08 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.205 (n=626)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1131` → IC=+0.163 (n=826)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1131 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1971)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.3023` → IC=+0.205 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3023 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.1263` → IC=+0.187 (n=1044)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1263 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.709` → IC=+0.174 (n=412)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 9.709 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.181` → IC=+0.157 (n=1712)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.181 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6287` → IC=+0.181 (n=626)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6287 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0731` → IC=+0.157 (n=1654)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.0731 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2676` → IC=+0.191 (n=270)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2676 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.1149` → IC=+0.163 (n=1602)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1149 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.4105` → IC=+0.156 (n=1821)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.4105 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `11309.5324` → IC=+0.159 (n=1676)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 11309.5324 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `278.0` → IC=+0.176 (n=773)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 278.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.165 (n=1597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.3265` → IC=+0.162 (n=1597)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3265 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=616)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.2861` → IC=+0.236 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2861 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.6515` → IC=+0.155 (n=253)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.6515 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1331` → IC=+0.164 (n=1463)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1331 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.534` → IC=+0.167 (n=268)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.534 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.314` → IC=+0.152 (n=1459)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.314 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.163 (n=1597)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1954 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1527` → IC=+0.202 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1527 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.4003` → IC=+0.158 (n=1499)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4003 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.7569` → IC=+0.165 (n=999)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.7569 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `259.0` → IC=+0.162 (n=468)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 259.0 (IC base=+0.150)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.257 (n=636)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=2006)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1934)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.36` → IC=+0.304 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.36 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.1337` → IC=+0.221 (n=1748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1337 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.7781` → IC=+0.230 (n=1634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7781 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1997.475` → IC=+0.229 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1997.475 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.238 (n=1573)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.6153` → IC=+0.237 (n=1787)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6153 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.237 (n=840)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0146` → IC=+0.303 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0146 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.157` → IC=+0.278 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.157 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3408` → IC=+0.290 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3408 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7308` → IC=+0.231 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7308 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.1505` → IC=+0.240 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1505 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1979.4784` → IC=+0.244 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1979.4784 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.233 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.194 (n=668)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0034 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4379` → IC=+0.150 (n=1998)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4379 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=2091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.277` → IC=+0.188 (n=1998)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.277 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3704` → IC=+0.162 (n=771)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3704 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.181` → IC=+0.159 (n=820)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.181 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8693` → IC=+0.162 (n=1332)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8693 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.206 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5221` → IC=+0.149 (n=854)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5221 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.158 (n=879)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1598 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7649.1944` → IC=+0.241 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7649.1944 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.175 (n=629)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 73.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.170 (n=1076)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0052 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4464` → IC=+0.145 (n=1614)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4464 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=740)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.5853` → IC=+0.198 (n=1420)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5853 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1609` → IC=+0.134 (n=1412)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1609 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.297` → IC=+0.168 (n=242)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.297 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.146 (n=710)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6973 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.224 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.443` → IC=+0.141 (n=1540)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.443 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6331.5198` → IC=+0.194 (n=732)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 6331.5198 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.132 (n=1352)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 146.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.147 (n=1328)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0082 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=2054)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4667` → IC=+0.197 (n=1994)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.4667 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.0784` → IC=+0.206 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0784 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.559` → IC=+0.238 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.559 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8911` → IC=+0.144 (n=1328)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8911 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.124 (n=2046)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.1932` → IC=+0.132 (n=878)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.1932 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=2021)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2883.9504` → IC=+0.255 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2883.9504 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.143 (n=1565)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 52.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.183 (n=636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0058 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1374` → IC=+0.159 (n=635)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1374 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=702)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.208 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2242` → IC=+0.139 (n=1575)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2242 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.468` → IC=+0.129 (n=1829)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.468 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.7154` → IC=+0.158 (n=838)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7154 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2203` → IC=+0.183 (n=298)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2203 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4358` → IC=+0.148 (n=580)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4358 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2798.604` → IC=+0.186 (n=635)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2798.604 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.133 (n=1525)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 51.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.229 (n=1760)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2067)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.212 (n=1767)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.260 (n=1768)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.2183` → IC=+0.229 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2183 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.252 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.0643` → IC=+0.216 (n=1734)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0643 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.64` → IC=+0.220 (n=1970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.64 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.235` → IC=+0.243 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.235 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.4852` → IC=+0.234 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4852 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=1936)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2615.934` → IC=+0.219 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2615.934 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.221 (n=693)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.230 (n=694)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.221 (n=1469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.264 (n=1829)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `1.2401` → IC=+0.210 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2401 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.2201` → IC=+0.213 (n=1843)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2201 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.87` → IC=+0.266 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.87 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.238 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.276 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `2.1835` → IC=+0.203 (n=1664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1835 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.4324` → IC=+0.207 (n=1890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4324 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2390.297` → IC=+0.210 (n=1857)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2390.297 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.198 (n=1801)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 37.0 (IC base=+0.208)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=3606)

- **PATRÓN** `sigma_h` < `0.009` → IC=+0.194 (n=3135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.009 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.5137` → IC=+0.188 (n=3561)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.5137 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=1347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=1622)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.238 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1778` → IC=+0.186 (n=1296)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1778 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` < `0.466` → IC=+0.177 (n=2306)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.466 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.206` → IC=+0.209 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.206 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `0.7061` → IC=+0.181 (n=1062)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.7061 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.892` → IC=+0.181 (n=1609)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.892 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.1697` → IC=+0.208 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1697 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `1.455` → IC=+0.188 (n=1172)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.455 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.866` → IC=+0.185 (n=2343)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.866 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2609)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2863.389` → IC=+0.184 (n=3181)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2863.389 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.218 (n=906)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.182 (n=2390)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3854 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=1233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.1827` → IC=+0.186 (n=1196)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1827 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.6734` → IC=+0.183 (n=509)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6734 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.193` → IC=+0.171 (n=2711)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.193 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.25` → IC=+0.165 (n=2552)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.25 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.167 (n=2480)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.5357` → IC=+0.169 (n=1181)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5357 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.8237` → IC=+0.172 (n=1788)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8237 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=3606)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `5122.641` → IC=+0.165 (n=2427)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5122.641 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.166 (n=1765)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 85.0 (IC base=+0.161)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.213 (n=412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.196 (n=419)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0033 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.261 (n=157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=472)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.210 (n=212)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.516` → IC=+0.222 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.516 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.7622` → IC=+0.207 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7622 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.3378` → IC=+0.206 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3378 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.96` → IC=+0.218 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.96 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.566` → IC=+0.199 (n=489)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 2.566 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `0.5858` → IC=+0.208 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5858 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.236 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.5976` → IC=+0.203 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5976 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `12570.0288` → IC=+0.232 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12570.0288 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.225 (n=449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.192 (n=342)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.181 (n=393)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.187 (n=449)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.1409 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.156 (n=463)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.6084 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6725` → IC=+0.197 (n=97)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6725 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.2178` → IC=+0.148 (n=1041)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2178 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.170 (n=1000)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8802` → IC=+0.191 (n=681)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8802 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.0691` → IC=+0.170 (n=471)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0691 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4164` → IC=+0.151 (n=339)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4164 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.8156` → IC=+0.165 (n=678)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.8156 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `12132.1528` → IC=+0.159 (n=912)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12132.1528 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `702.0` → IC=+0.156 (n=975)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 702.0 (IC base=+0.148)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.210 (n=377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1524` → IC=+0.201 (n=497)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1524 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.196 (n=422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.189 (n=512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 6.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.5319` → IC=+0.195 (n=753)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5319 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.8839` → IC=+0.193 (n=376)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.8839 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2066` → IC=+0.194 (n=946)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.2066 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.178` → IC=+0.193 (n=1014)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 4.178 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.6294` → IC=+0.191 (n=377)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6294 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.1669` → IC=+0.198 (n=336)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1669 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `2.4777` → IC=+0.189 (n=1107)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.4777 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=1128)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.214 (n=309)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3831` → IC=+0.198 (n=808)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3831 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.170 (n=653)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 11.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` < `0.7607` → IC=+0.172 (n=919)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7607 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.0945` → IC=+0.171 (n=918)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.0945 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.6082` → IC=+0.191 (n=202)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6082 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.639` → IC=+0.172 (n=942)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.639 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.6427` → IC=+0.199 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6427 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `0.7215` → IC=+0.168 (n=821)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.7215 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.167 (n=860)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.181 (n=387)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `2.1956` → IC=+0.182 (n=793)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.1956 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `7789.3412` → IC=+0.184 (n=821)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 7789.3412 (IC base=+0.166)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.171 (n=317)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0109 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.374` → IC=+0.145 (n=240)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.374 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.170 (n=355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 3.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.147 (n=364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 14.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.246 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.2317` → IC=+0.193 (n=239)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2317 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.097` → IC=+0.220 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.097 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.7088` → IC=+0.196 (n=159)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.7088 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `1.2654` → IC=+0.147 (n=120)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.2654 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.4144` → IC=+0.203 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4144 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.154 (n=426)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3257.6056` → IC=+0.175 (n=321)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3257.6056 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.170 (n=301)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 51.0 (IC base=+0.144)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.169 (n=484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.083)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.125 (n=1001)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 8.0 (IC base=+0.083)

- **PATRÓN** `ibs_20min` > `0.6471` → IC=+0.183 (n=899)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.6471 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.1435` → IC=+0.145 (n=536)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1435 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.45` → IC=+0.188 (n=235)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.45 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.2792` → IC=+0.186 (n=135)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2792 (IC base=+0.083)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.122 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0063 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.0417` → IC=+0.307 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0417 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` < `0.1862` → IC=+0.148 (n=418)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1862 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.034` → IC=+0.160 (n=145)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.034 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.136` → IC=+0.229 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.136 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `2.5184` → IC=+0.162 (n=312)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.5184 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `1.7085` → IC=+0.157 (n=208)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7085 (IC base=+0.049)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.147 (n=318)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.049)

- **PATRÓN** `libro_liquidez` > `3644.8509` → IC=+0.164 (n=111)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3644.8509 (IC base=+0.049)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.141 (n=377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0058 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.4395` → IC=+0.164 (n=346)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.4395 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.169 (n=179)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `2.0809` → IC=+0.143 (n=270)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.0809 (IC base=+0.093)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.157 (n=173)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0044 (IC base=+0.099)

- **PATRÓN** `drift_60min` |x|≤ `0.0561` → IC=+0.202 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0561 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.128 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 4.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.308 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1654` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1654 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` < `0.0682` → IC=+0.158 (n=182)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.0682 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.876` → IC=+0.194 (n=168)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.876 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `1.1259` → IC=+0.146 (n=173)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1259 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `0.8238` → IC=+0.158 (n=115)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.8238 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.0668` → IC=+0.202 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0668 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `2.3987` → IC=+0.193 (n=151)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.3987 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `3267.3803` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3267.3803 (IC base=+0.099)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6869` → IC=-0.124 (n=147)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6869
  - _Potencial_: sin este filtro IC_bueno=+0.216 (n=301)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=144)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.132 (n=245)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0049 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.134 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.6869` → IC=+0.216 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6869 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.3424` → IC=+0.202 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3424 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.74` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.74 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `1.7588` → IC=+0.149 (n=189)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.7588 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `1133.2011` → IC=+0.155 (n=297)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1133.2011 (IC base=+0.095)

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

- **PATRÓN** `ibs_20min` > `0.7805` → IC=+0.183 (n=216)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7805 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `1.0104` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 1.0104 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.104` → IC=+0.149 (n=92)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.104 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.188 (n=62)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.059)

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
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=126)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.278 (n=61)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=129)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.253 (n=168)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=160)

- **FILTRO** `volumen_pendiente_norm` > `0.0781` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0781
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=87)

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
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=52)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=48)

- **FILTRO** `volumen_spike_ratio` < `1.4749` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4749
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=18)

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
- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.146 (n=204)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0045 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.149 (n=306)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6522 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.5141` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.5141 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `1.8223` → IC=+0.124 (n=139)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.8223 (IC base=+0.085)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.124 (n=317)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0059 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.198 (n=279)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.156 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.126` → IC=+0.185 (n=128)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.126 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2694` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2694 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `2.5723` → IC=+0.141 (n=243)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5723 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` > `1.5807` → IC=+0.135 (n=217)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.5807 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=335)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `3936.7645` → IC=+0.212 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3936.7645 (IC base=+0.094)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6599` → IC=-0.244 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6599
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=86)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.187 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0034 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.232 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.179 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.228 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1622 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.668` → IC=+0.177 (n=131)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 6.668 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.1644` → IC=+0.173 (n=145)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.1644 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `0.6961` → IC=+0.174 (n=130)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6961 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.1895` → IC=+0.224 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1895 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `2.5856` → IC=+0.224 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5856 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.190 (n=114)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `4472.275` → IC=+0.187 (n=97)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 4472.275 (IC base=+0.162)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.6645` → IC=-0.219 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6645
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=92)

- **FILTRO** `libro_liquidez` < `1374.2652` → IC=-0.219 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 1374.2652
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=92)

- **FILTRO** `ibs_20min` > `0.1644` → IC=-0.140 (n=48)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1644
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=96)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.167 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0021 (IC base=+0.024)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.122 (n=96)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0048 (IC base=+0.082)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.126 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 8.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.1644` → IC=+0.194 (n=96)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1644 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.769` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.769 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` < `0.9994` → IC=+0.133 (n=96)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.9994 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.0745` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.0745 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `2277.014` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2277.014 (IC base=+0.082)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.1837` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1837
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=43)

- **FILTRO** `dist_vwap_pct` > `0.2902` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2902
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=68)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.274 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.271 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.235 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.9583` → IC=+0.256 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9583 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.261 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `579.6494` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 579.6494 (IC base=+0.233)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=846)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2918.2518` → IC=+0.155 (n=291)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2918.2518 (IC base=+0.107)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=846)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2918.2518` → IC=+0.155 (n=291)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2918.2518 (IC base=+0.107)

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
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=227)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=213)

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

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=2190)

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

- **PATRÓN** `liq_usd_total` > `98013.51` → IC=+0.136 (n=97)

  - _Acción_: Kelly boost +0.68€ cuando `liq_usd_total` > 98013.51 (IC base=+0.045)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.045)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=152)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=913)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=867)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=517)

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
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=219)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.027)

- **PATRÓN** `libro_liquidez` > `4039.6046` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4039.6046 (IC base=+0.027)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=710)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=710)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=436)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=436)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=104)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=128)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=233)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=111)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=114)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=270)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=270)

- **FILTRO** `libro_liquidez` < `535.3587` → IC=-0.124 (n=99)

  - _Acción_: SKIP cuando `libro_liquidez` < 535.3587
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=201)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=157)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.122 (n=860)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=862)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.135 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=82)

- **PATRÓN** `py_entrada` > `0.52` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.52 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.46 (IC base=+0.045)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=94)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.184 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=79)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.143 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 9.0 (IC base=+0.087)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.138 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.191 (n=40)

- **FILTRO** `profundidad_ratio` < `54.9` → IC=-0.235 (n=47)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.9
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=96)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=127)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `restante_min` < `3.39` → IC=-0.250 (n=62)

  - _Acción_: SKIP cuando `restante_min` < 3.39
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=128)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.153 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=97)

- **FILTRO** `lag_apertura_s` > `95.78` → IC=-0.258 (n=64)

  - _Acción_: SKIP cuando `lag_apertura_s` > 95.78
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `profundidad_ratio` < `77.2` → IC=-0.201 (n=95)

  - _Acción_: SKIP cuando `profundidad_ratio` < 77.2
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=95)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=118)

- **FILTRO** `restante_min` < `13.48` → IC=-0.121 (n=101)

  - _Acción_: SKIP cuando `restante_min` < 13.48
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=53)

- **PATRÓN** `restante_min` > `13.36` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `restante_min` > 13.36 (IC base=-0.006)

- **PATRÓN** `lag_apertura_s` < `95.05` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `lag_apertura_s` < 95.05 (IC base=-0.006)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.164 (n=129)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=69)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.162 (n=69)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.5 (IC base=-0.050)

- **PATRÓN** `profundidad_ratio` > `13.0` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `profundidad_ratio` > 13.0 (IC base=+0.031)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.242 (n=64)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=173)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.166 (n=4108)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=12467)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.163 (n=4177)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=12998)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.197 (n=718)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=2193)

- **PATRÓN** `libro_liquidez` > `1565.4334` → IC=+0.139 (n=1044)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1565.4334 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.184 (n=723)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2244)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=738)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2367)

- **PATRÓN** `libro_liquidez` > `1791.0584` → IC=+0.123 (n=1009)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1791.0584 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.167 (n=710)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=2195)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2366)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3106)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=403)

- **FILTRO** `libro_liquidez` < `17076.8097` → IC=-0.144 (n=231)

  - _Acción_: SKIP cuando `libro_liquidez` < 17076.8097
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=695)

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
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=25962)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=8687)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=28825)

- **FILTRO** `ibs_7min` < `0.2667` → IC=-0.235 (n=9364)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=28148)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=12465)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=25047)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=11617)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=35909)

- **FILTRO** `ibs_7min` > `0.2913` → IC=-0.180 (n=11878)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2913
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=35648)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.141 (n=1877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4421)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.311 (n=1513)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4785)

- **FILTRO** `ibs_7min` < `0.7075` → IC=-0.254 (n=2078)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7075
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=4220)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.180 (n=1490)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4808)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.262 (n=2022)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=6175)

- **FILTRO** `ibs_7min` > `0.7929` → IC=-0.210 (n=2049)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7929
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6148)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.142 (n=1516)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=4923)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.252 (n=1576)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4863)

- **FILTRO** `ibs_7min` < `0.744` → IC=-0.197 (n=1609)

  - _Acción_: SKIP cuando `ibs_7min` < 0.744
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4830)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.181 (n=1599)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=4840)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=1521)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5032)

- **FILTRO** `ibs_7min` > `0.2614` → IC=-0.186 (n=1638)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2614
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4915)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.184 (n=1636)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4917)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.162 (n=1473)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4532)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=1401)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4604)

- **FILTRO** `ibs_7min` < `0.7054` → IC=-0.244 (n=1981)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7054
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=4024)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.208 (n=1445)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4560)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.246 (n=2013)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=6751)

- **FILTRO** `ibs_7min` > `0.7456` → IC=-0.177 (n=2190)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7456
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=6574)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=1981)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=4194)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.233 (n=1820)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4355)

- **FILTRO** `ibs_7min` < `0.7407` → IC=-0.181 (n=1542)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4633)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.171 (n=1541)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4634)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.258 (n=1574)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=4776)

- **FILTRO** `ibs_7min` > `0.2745` → IC=-0.178 (n=1586)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2745
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4764)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.182 (n=1537)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4813)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.264 (n=1554)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4880)

- **FILTRO** `ibs_7min` < `0.2667` → IC=-0.233 (n=1608)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4826)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.173 (n=2259)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=6820)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.254 (n=1925)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4236)

- **FILTRO** `ibs_7min` < `0.2702` → IC=-0.222 (n=1540)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2702
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4621)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.212 (n=1451)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=4710)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.208 (n=2016)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=6567)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1167)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=582)

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
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.131 (n=839)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `453.526` → IC=+0.149 (n=280)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 453.526 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.122 (n=712)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 55.0 (IC base=+0.116)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4376` → IC=+0.136 (n=64)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.4376 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.199 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2571.3862` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2571.3862 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 14.0 (IC base=+0.134)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 11.0 (IC base=+0.111)

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
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.147 (n=148)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.127 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 13.0 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `3589.6144` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3589.6144 (IC base=+0.099)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0046` → IC=-0.254 (n=299)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=149)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0049` → IC=-0.226 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0049
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=35)

- **FILTRO** `T_h` > `95.4629` → IC=-0.417 (n=34)

  - _Acción_: SKIP cuando `T_h` > 95.4629
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=105)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.257 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.103)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0081` → IC=-0.221 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.176 (n=325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=109)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.330 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=279)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.330 (n=92)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=279)

- **FILTRO** `T_h` > `60.9549` → IC=-0.318 (n=278)

  - _Acción_: SKIP cuando `T_h` > 60.9549
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=93)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `68.7654` → IC=-0.152 (n=113)

  - _Acción_: SKIP cuando `T_h` > 68.7654
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=39)

- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.372 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=115)

- **FILTRO** `T_h` > `144.5168` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `T_h` > 144.5168
  - _Potencial_: sin este filtro IC_bueno=-0.285 (n=105)

- **FILTRO** `pct_vs_K` |x|> `2.9616` → IC=-0.439 (n=47)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9616
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=92)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.9836` → IC=-0.219 (n=30)

  - _Acción_: SKIP cuando `T_h` > 135.9836
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=92)

- **FILTRO** `T_h` < `87.9866` → IC=-0.286 (n=40)

  - _Acción_: SKIP cuando `T_h` < 87.9866
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=82)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.339 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=88)

- **FILTRO** `sigma_h` < `0.0048` → IC=-0.339 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=88)

- **FILTRO** `T_h` > `57.801` → IC=-0.338 (n=78)

  - _Acción_: SKIP cuando `T_h` > 57.801
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=39)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0141` → IC=-0.179 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0141
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=82)

- **FILTRO** `sigma_h` < `0.008` → IC=-0.155 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=81)

- **FILTRO** `T_h` > `135.6166` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `T_h` > 135.6166
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=82)

- **FILTRO** `T_h` > `49.3826` → IC=-0.379 (n=56)

  - _Acción_: SKIP cuando `T_h` > 49.3826
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **PATRÓN** `pct_vs_K` |x|≤ `1.14` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.14 (IC base=-0.054)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1255` → IC=+0.468 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1255 (IC base=+0.353)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.387 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.353)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.391 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.353)

- **PATRÓN** `T_h` < `0.5922` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5922 (IC base=+0.353)

- **PATRÓN** `T_h` > `1.2259` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2259 (IC base=+0.353)

- **PATRÓN** `dist_50` > `0.4086` → IC=+0.457 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4086 (IC base=+0.353)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.377 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.353)

- **PATRÓN** `edge` > `0.097` → IC=+0.453 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.097 (IC base=+0.419)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.431 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.419)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.447 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.419)

- **PATRÓN** `T_h` < `0.5967` → IC=+0.431 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5967 (IC base=+0.419)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.449 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.419)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.482 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.419)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.474 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.419)

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

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1155 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.487 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.463)

- **PATRÓN** `T_h` > `0.8021` → IC=+0.465 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8021 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4923` → IC=+0.487 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4923 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.468 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=218)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=319)

- **PATRÓN** `streak_estiramiento` < `0.4493` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `streak_estiramiento` < 0.4493 (IC base=+0.032)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=466)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=703)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1273)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=853)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=835)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3185)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1615)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1623)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.202 (n=639)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.232 (n=639)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.1594` → IC=+0.198 (n=1687)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1594 (IC base=+0.193)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2181` → IC=+0.199 (n=639)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio_macro` |x|> 0.2181 (IC base=+0.193)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1268` → IC=+0.234 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1268 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.203 (n=1788)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=1995)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_15` > `0.6133` → IC=+0.273 (n=1917)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6133 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.1189` → IC=+0.187 (n=964)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1189 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.833` → IC=+0.282 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.833 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `8753.6365` → IC=+0.204 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8753.6365 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.209 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.193)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=818)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.234 (n=284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.278 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.211)

- **PATRÓN** `drift_15min` |x|≤ `0.3831` → IC=+0.222 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3831 (IC base=+0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2011` → IC=+0.240 (n=194)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2011 (IC base=+0.211)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4024` → IC=+0.244 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4024 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_15` > `0.7112` → IC=+0.278 (n=425)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7112 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.276 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.588` → IC=+0.271 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.588 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `16113.4131` → IC=+0.243 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16113.4131 (IC base=+0.211)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.418` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.418
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=496)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6602` → IC=-0.123 (n=197)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6602
  - _Potencial_: sin este filtro IC_bueno=+0.262 (n=401)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.178 (n=150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0035 (IC base=+0.135)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.141 (n=299)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.005 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0669` → IC=+0.155 (n=198)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0669 (IC base=+0.135)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.178 (n=150)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1251` → IC=+0.155 (n=166)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1251 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.153 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.135 (n=450)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 16.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.6602` → IC=+0.262 (n=401)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6602 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1154` → IC=+0.151 (n=322)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1154 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.307` → IC=+0.234 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.307 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `8733.4432` → IC=+0.146 (n=204)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 8733.4432 (IC base=+0.135)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=137)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.285 (n=77)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.1481` → IC=+0.206 (n=202)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1481 (IC base=+0.181)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0592` → IC=+0.193 (n=229)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.0592 (IC base=+0.181)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3238` → IC=+0.228 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3238 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.193 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.181)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.266 (n=229)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.192 (n=128)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.181 (n=224)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.128` → IC=+0.400 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.128 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.181 (n=252)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.02 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `3077.8574` → IC=+0.283 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3077.8574 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.215 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.181)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.6767` → IC=-0.157 (n=106)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6767
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=1247)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.781` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.781 (IC base=-0.012)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0233` → IC=+0.283 (n=164)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0233 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.225 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.197)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0605` → IC=+0.198 (n=439)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio_macro` |x|> 0.0605 (IC base=+0.197)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0834` → IC=+0.261 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0834 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `ibs_15` > `0.5745` → IC=+0.287 (n=491)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5745 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.3637` → IC=+0.209 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3637 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.981` → IC=+0.228 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.981 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.857` → IC=+0.197 (n=499)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 10.857 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `2915.737` → IC=+0.277 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2915.737 (IC base=+0.197)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.354 (n=313)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.351)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.380 (n=156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.351)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.354 (n=313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.351)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1462` → IC=+0.376 (n=312)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1462 (IC base=+0.351)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.389 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.351)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.371 (n=477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.351)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.389 (n=468)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.351)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.387 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.351)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.363 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.351)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.351 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.351)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.355 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.351)

- **PATRÓN** `libro_liquidez` > `3820.3005` → IC=+0.369 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3820.3005 (IC base=+0.351)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.364 (n=226)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.357)

- **PATRÓN** `sigma_h` > `0.0025` → IC=+0.360 (n=256)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0025 (IC base=+0.357)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.375 (n=86)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.357)

- **PATRÓN** `drift_15min` |x|≤ `0.4175` → IC=+0.370 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4175 (IC base=+0.357)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.368 (n=256)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.357)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1241` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1241 (IC base=+0.357)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.381 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.357)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.388 (n=256)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.357)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.397 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.859` → IC=+0.364 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.859 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.763` → IC=+0.358 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.763 (IC base=+0.357)

- **PATRÓN** `libro_liquidez` > `11281.6823` → IC=+0.373 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11281.6823 (IC base=+0.357)

- **PATRÓN** `ballena_activa_n` < `568.0` → IC=+0.400 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 568.0 (IC base=+0.357)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.379 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.342)

- **PATRÓN** `drift_60min` |x|≤ `0.1054` → IC=+0.354 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1054 (IC base=+0.342)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.365 (n=190)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.342)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.372 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.342)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.403 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.342)

- **PATRÓN** `ibs_15` > `0.7485` → IC=+0.393 (n=213)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7485 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.394 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` < `0.1186` → IC=+0.347 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1186 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.357 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.587` → IC=+0.343 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.587 (IC base=+0.342)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.348 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.342)

- **PATRÓN** `libro_liquidez` > `4305.62` → IC=+0.363 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4305.62 (IC base=+0.342)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.225 (n=747)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2242)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.208 (n=1039)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1950)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1365` → IC=+0.233 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1365 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.6429` → IC=+0.272 (n=727)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6429 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.190 (n=594)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1224` → IC=+0.251 (n=1449)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1224 (IC base=-0.024)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1804` → IC=+0.248 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1804 (IC base=-0.024)

- **PATRÓN** `ibs_15` < `0.3482` → IC=+0.277 (n=2174)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3482 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.6808` → IC=+0.295 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6808 (IC base=-0.024)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.242 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 61.0 (IC base=-0.024)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.217 (n=454)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1364)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.219 (n=454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1364)

- **FILTRO** `sigma_ewma_delta_pct` > `23.595` → IC=-0.255 (n=255)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.595
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1563)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.163 (n=176)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0028 (IC base=+0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1979` → IC=+0.270 (n=98)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1979 (IC base=+0.085)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.317 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.085)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.122 (n=358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 12.0 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.7503` → IC=+0.325 (n=215)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7503 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1269` → IC=+0.288 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1269 (IC base=+0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0923` → IC=+0.136 (n=31)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.0923 (IC base=-0.195)

- **PATRÓN** `ibs_15` < `0.5567` → IC=+0.288 (n=31)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.5567 (IC base=-0.195)

- **PATRÓN** `ballena_activa_n` < `305.0` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 305.0 (IC base=-0.195)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=446)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.151 (n=348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0066 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.168 (n=311)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.004 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.211 (n=154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.147)

- **PATRÓN** `drift_15min` |x|≤ `0.4157` → IC=+0.170 (n=116)

  - _Acción_: Kelly boost +0.85€ cuando `drift_15min` |x|≤ 0.4157 (IC base=+0.147)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0609` → IC=+0.150 (n=349)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio_macro` |x|> 0.0609 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2962` → IC=+0.219 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2962 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.173 (n=252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.6625` → IC=+0.260 (n=348)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6625 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1047` → IC=+0.176 (n=251)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1047 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.049` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 23.049 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=446)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `10550.3134` → IC=+0.188 (n=158)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 10550.3134 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.248 (n=843)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4445` → IC=+0.240 (n=843)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4445 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.7869` → IC=+0.246 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7869 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2075` → IC=+0.255 (n=382)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2075 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.242 (n=320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.2735` → IC=+0.278 (n=742)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2735 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.7586` → IC=+0.315 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7586 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.213` → IC=+0.267 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.213 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.411` → IC=+0.238 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.411 (IC base=+0.234)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.234 (n=239)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=465)

- **FILTRO** `drift_15min` |x|> `0.907` → IC=-0.274 (n=175)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.907
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=529)

- **PATRÓN** `ibs_15` > `0.9167` → IC=+0.309 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9167 (IC base=-0.173)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0776` → IC=+0.233 (n=327)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0776 (IC base=-0.040)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1822` → IC=+0.225 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1822 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.268 (n=368)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.7364` → IC=+0.247 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7364 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.1775` → IC=+0.232 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1775 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1996` → IC=-0.212 (n=286)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1996
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=556)

- **FILTRO** `sigma_h` > `0.0196` → IC=-0.263 (n=420)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0196
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=422)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.268 (n=231)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=611)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1402` → IC=+0.290 (n=250)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1402 (IC base=-0.036)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.107` → IC=+0.331 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.107 (IC base=-0.036)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.304 (n=553)
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
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.302 (n=508)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.324 (n=254)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2394` → IC=+0.305 (n=254)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2394 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2224` → IC=+0.321 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2224 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=800)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8408` → IC=+0.329 (n=762)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8408 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.4372` → IC=+0.337 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4372 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.346 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `13022.3239` → IC=+0.296 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13022.3239 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.301 (n=279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0549` → IC=+0.331 (n=140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0549 (IC base=+0.285)

- **PATRÓN** `drift_15min` |x|≤ `0.4196` → IC=+0.285 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4196 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2556` → IC=+0.308 (n=139)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2556 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3977` → IC=+0.309 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3977 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.319 (n=418)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.4139` → IC=+0.357 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4139 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.356 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `16193.642` → IC=+0.317 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16193.642 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.307 (n=303)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.312 (n=115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.297 (n=230)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.328 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.314 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.341 (n=344)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.6363` → IC=+0.310 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6363 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.339 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.296 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.296)

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

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `79.3918` → IC=+0.222 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 79.3918 (IC base=+0.209)

- **PATRÓN** `ratio` < `0.9771` → IC=+0.470 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9771 (IC base=+0.209)

- **PATRÓN** `T_h` > `145.7579` → IC=+0.393 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7579 (IC base=+0.334)

- **PATRÓN** `ratio` > `1.0104` → IC=+0.309 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0104 (IC base=+0.334)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.3604` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 144.3604 (IC base=+0.189)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.467 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.189)

- **PATRÓN** `T_h` > `103.5964` → IC=+0.295 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.5964 (IC base=+0.285)

- **PATRÓN** `ratio` > `1.0467` → IC=+0.371 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0467 (IC base=+0.285)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `80.0063` → IC=+0.267 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 80.0063 (IC base=+0.245)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.425 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.245)

- **PATRÓN** `T_h` > `106.9285` → IC=+0.333 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 106.9285 (IC base=+0.316)

- **PATRÓN** `ratio` > `1.015` → IC=+0.345 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.015 (IC base=+0.316)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1132` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.402)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6133 sube el IC de +0.193 a +0.273 en UPDOWN_GBM#15min (n=1917). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7112 sube el IC de +0.211 a +0.278 en UPDOWN_GBM#BTC#15min (n=425). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6602 sube el IC de +0.135 a +0.262 en UPDOWN_GBM#ETH#15min (n=401). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.181 a +0.266 en UPDOWN_GBM#SOL#15min (n=229). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5745 sube el IC de +0.197 a +0.287 en UPDOWN_GBM#XRP#15min (n=491). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6429 sube el IC de -0.066 a +0.272 en UPDOWN_GBM_15M_TARDIO (n=727). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3482 sube el IC de -0.024 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=2174). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7503 sube el IC de +0.085 a +0.325 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=215). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.5567 sube el IC de -0.195 a +0.288 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=31). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6625 sube el IC de +0.147 a +0.260 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=348). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2735 sube el IC de +0.234 a +0.278 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=742). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9167 sube el IC de -0.173 a +0.309 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.040 a +0.268 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=368). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.036 a +0.304 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=553). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8408 sube el IC de +0.291 a +0.329 en UPDOWN_GBM_IBS_ALTO (n=762). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.285 a +0.319 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=418). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.296 a +0.341 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=344). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.351 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=468). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.357 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=256). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7485 sube el IC de +0.342 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=213). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.134 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.134 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH#15min` — IC=+0.085 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH` — IC=+0.085 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1438 | +0.101 | +211.54€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1438 | +0.101 | +211.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1088 | +0.110 | +179.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1088 | +0.110 | +179.90€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 4 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 64 | +0.151 | +22.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 64 | +0.151 | +22.93€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 31042 | -0.086 | -4058.11€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1610 | -0.025 | -217.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 29432 | -0.090 | -3841.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4060 | -0.105 | -670.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4060 | -0.105 | -670.85€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1610 | -0.025 | -217.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1610 | -0.025 | -217.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3638 | -0.101 | -821.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3638 | -0.101 | -821.20€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8062 | -0.018 | -769.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8062 | -0.018 | -769.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7632 | -0.093 | -449.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7632 | -0.093 | -449.96€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6040 | -0.163 | -1129.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6040 | -0.163 | -1129.29€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 22222 | -0.023 | +3803.45€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5756 | +0.001 | +1771.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 16466 | -0.031 | +2032.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 22222 | -0.023 | +3803.45€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5756 | +0.001 | +1771.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 16466 | -0.031 | +2032.22€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 105303 | +0.112 | -5149.56€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15271 | +0.184 | -480.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 439 | -0.065 | -57.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 82937 | +0.101 | -4374.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6656 | +0.107 | -238.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 13780 | +0.100 | -1070.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 49 | -0.147 | +8.51€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 13716 | +0.101 | -1067.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 21089 | +0.130 | -425.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4705 | +0.199 | -152.97€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 13756 | +0.113 | -199.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2586 | +0.097 | -50.64€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 13825 | +0.091 | -1213.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 56 | -0.103 | -7.23€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 13754 | +0.092 | -1195.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 22355 | +0.124 | -428.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6027 | +0.177 | -80.64€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 13904 | +0.105 | -284.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2412 | +0.101 | -55.34€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 20456 | +0.114 | -1175.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4383 | +0.188 | -258.86€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 342 | -0.026 | -3.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 14073 | +0.092 | -781.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1658 | +0.131 | -132.12€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 13798 | +0.099 | -835.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 51 | -0.028 | +11.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 13734 | +0.100 | -846.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 16744 | +0.194 | -1039.15€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 16744 | +0.194 | -1039.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3926 | +0.172 | -381.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3926 | +0.172 | -381.15€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1630 | +0.205 | -9.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1630 | +0.205 | -9.11€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3875 | +0.181 | -318.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3875 | +0.181 | -318.54€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3420 | +0.243 | -103.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3420 | +0.243 | -103.72€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3814 | +0.190 | -240.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3814 | +0.190 | -240.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 786 | +0.431 | -19.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 786 | +0.431 | -19.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 307 | +0.442 | -0.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 307 | +0.442 | -0.36€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 300 | +0.430 | -7.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 300 | +0.430 | -7.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 167 | +0.411 | -8.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 167 | +0.411 | -8.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 58009 | +0.198 | -4489.90€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 58009 | +0.198 | -4489.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9990 | +0.179 | -1119.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9990 | +0.179 | -1119.21€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9290 | +0.222 | -350.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9290 | +0.222 | -350.53€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10006 | +0.174 | -1156.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10006 | +0.174 | -1156.96€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9379 | +0.218 | -376.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9379 | +0.218 | -376.03€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9608 | +0.203 | -633.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9608 | +0.203 | -633.73€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9736 | +0.192 | -853.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9736 | +0.192 | -853.44€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 22036 | +0.115 | +120.23€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 22036 | +0.115 | +120.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 10938 | +0.119 | +114.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 10938 | +0.119 | +114.09€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 11098 | +0.112 | +6.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 11098 | +0.112 | +6.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1621 | +0.289 | -24.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1621 | +0.289 | -24.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 724 | +0.280 | -16.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 724 | +0.280 | -16.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 783 | +0.287 | -10.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 783 | +0.287 | -10.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 114 | +0.345 | +3.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 114 | +0.345 | +3.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 721 | +0.436 | -3.27€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 721 | +0.436 | -3.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 346 | +0.434 | -3.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 346 | +0.434 | -3.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 330 | +0.440 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 330 | +0.440 | +0.24€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 45 | +0.394 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 45 | +0.394 | +0.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1243 | +0.066 | -67.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 437 | +0.051 | -40.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 806 | +0.073 | -26.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 64 | +0.121 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 64 | +0.121 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 982 | +0.071 | -36.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 176 | +0.062 | -10.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 806 | +0.073 | -26.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 197 | +0.018 | -34.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 197 | +0.018 | -34.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 41648 | +0.098 | -1194.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3411 | +0.088 | +17.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 38237 | +0.099 | -1212.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 23211 | +0.102 | -345.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3411 | +0.088 | +17.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 19800 | +0.104 | -362.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8083 | +0.108 | -29.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8083 | +0.108 | -29.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 10354 | +0.081 | -820.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 10354 | +0.081 | -820.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 855 | +0.212 | -100.84€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 855 | +0.212 | -100.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 855 | +0.212 | -100.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 855 | +0.212 | -100.84€ | 2 | 4 |
| ✅ GBM_LATE_15M | 29418 | +0.087 | +14442.41€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 29418 | +0.087 | +14442.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4932 | +0.200 | +3744.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4932 | +0.200 | +3744.67€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 4392 | +0.179 | +3154.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4392 | +0.179 | +3154.03€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 5191 | +0.199 | +3885.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5191 | +0.199 | +3885.20€ | 0 | 23 |
| ✅ GBM_LATE_15M#ETH | 4220 | +0.029 | +1028.80€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4220 | +0.029 | +1028.80€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 4193 | -0.032 | +931.84€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4193 | -0.032 | +931.84€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6490 | -0.038 | +1697.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6490 | -0.038 | +1697.87€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 31446 | +0.088 | +16707.88€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 31446 | +0.088 | +16707.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6010 | +0.014 | +3126.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6010 | +0.014 | +3126.42€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6546 | +0.016 | +1392.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6546 | +0.016 | +1392.68€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4465 | +0.267 | +4580.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4465 | +0.267 | +4580.25€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5199 | +0.008 | +1088.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5199 | +0.008 | +1088.44€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5076 | +0.034 | +2016.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5076 | +0.034 | +2016.10€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4150 | +0.281 | +4503.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4150 | +0.281 | +4503.99€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 23646 | +0.171 | +18074.91€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 23646 | +0.171 | +18074.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3559 | +0.212 | +2917.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3559 | +0.212 | +2917.64€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3737 | +0.149 | +2727.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3737 | +0.149 | +2727.86€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3735 | +0.210 | +3005.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3735 | +0.210 | +3005.52€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3971 | +0.135 | +2867.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3971 | +0.135 | +2867.02€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4424 | +0.121 | +3196.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4424 | +0.121 | +3196.41€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4220 | +0.205 | +3360.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4220 | +0.205 | +3360.46€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6326 | +0.138 | +2958.03€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6326 | +0.138 | +2958.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 247 | +0.127 | +123.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 247 | +0.127 | +123.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1809 | +0.139 | +940.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1809 | +0.139 | +940.42€ | 0 | 29 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1911 | +0.154 | +937.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1911 | +0.154 | +937.46€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1479 | +0.114 | +564.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1479 | +0.114 | +564.11€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 29653 | +0.179 | +22665.34€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 29653 | +0.179 | +22665.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4696 | +0.228 | +4110.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4696 | +0.228 | +4110.66€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4630 | +0.152 | +3085.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4630 | +0.152 | +3085.65€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4924 | +0.226 | +4249.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4924 | +0.226 | +4249.12€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4814 | +0.136 | +3358.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4814 | +0.136 | +3358.72€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5192 | +0.120 | +3512.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5192 | +0.120 | +3512.49€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5397 | +0.210 | +4348.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5397 | +0.210 | +4348.70€ | 0 | 25 |
| ✅ GBM_LATE_5M | 8368 | +0.171 | +5514.50€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 8368 | +0.171 | +5514.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1984 | +0.164 | +1428.32€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1984 | +0.164 | +1428.32€ | 0 | 30 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2728 | +0.175 | +1790.14€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2728 | +0.175 | +1790.14€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 876 | +0.151 | +493.36€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 876 | +0.151 | +493.36€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2060 | +0.073 | +765.51€ | 0 | 15 |
| ✅ GBM_LATE_60M#60min | 2060 | +0.073 | +765.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 764 | +0.095 | +276.29€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 764 | +0.095 | +276.29€ | 0 | 17 |
| ✅ GBM_LATE_60M#ETH | 668 | +0.075 | +304.65€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 668 | +0.075 | +304.65€ | 2 | 17 |
| ✅ GBM_LATE_60M#SOL | 628 | +0.044 | +184.58€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 628 | +0.044 | +184.58€ | 3 | 9 |
| 🚫 GBM_LATE_60M_FADE | 420 | -0.249 | -16.93€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 420 | -0.249 | -16.93€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 157 | -0.217 | -4.98€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 157 | -0.217 | -4.98€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 141 | -0.248 | -5.38€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 141 | -0.248 | -5.38€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 122 | -0.282 | -6.57€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 122 | -0.282 | -6.57€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 830 | +0.090 | +203.11€ | 0 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 830 | +0.090 | +203.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 320 | +0.081 | +65.40€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 320 | +0.081 | +65.40€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 266 | +0.056 | +30.58€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 266 | +0.056 | +30.58€ | 3 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 244 | +0.138 | +107.12€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 244 | +0.138 | +107.12€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 114 | +0.250 | +94.41€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 114 | +0.250 | +94.41€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 114 | +0.250 | +94.41€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 114 | +0.250 | +94.41€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2372 | +0.104 | +639.09€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2372 | +0.104 | +639.09€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2372 | +0.104 | +639.09€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2372 | +0.104 | +639.09€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 407 | -0.077 | -34.70€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 407 | -0.077 | -34.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 105 | -0.051 | -4.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 105 | -0.051 | -4.32€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 153 | -0.029 | -5.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 153 | -0.029 | -5.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2390 | +0.017 | +51.53€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2390 | +0.017 | +51.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 125 | +0.012 | -3.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 125 | +0.012 | -3.55€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 319 | +0.020 | +21.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 319 | +0.020 | +21.69€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 180 | -0.017 | -4.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 180 | -0.017 | -4.39€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 961 | +0.026 | +26.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 961 | +0.026 | +26.40€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 557 | +0.012 | +0.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 557 | +0.012 | +0.80€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 248 | +0.016 | +10.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 248 | +0.016 | +10.59€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1241 | -0.041 | -24.35€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1241 | -0.041 | -24.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 350 | -0.040 | -12.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 350 | -0.040 | -12.42€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 419 | -0.025 | +0.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 419 | -0.025 | +0.12€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 472 | -0.057 | -12.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 472 | -0.057 | -12.05€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 3291 | -0.017 | +74.32€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1550 | -0.019 | +23.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1741 | -0.015 | +50.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 92 | +0.021 | +9.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 47 | +0.071 | +11.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 45 | -0.032 | -1.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 774 | +0.000 | +40.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 363 | +0.004 | +17.68€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 411 | -0.004 | +22.62€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 392 | -0.010 | +21.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 187 | -0.029 | +3.41€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 205 | +0.007 | +17.70€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 657 | -0.043 | -34.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 300 | -0.050 | -21.54€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 357 | -0.038 | -12.69€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 645 | -0.022 | +10.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 312 | -0.029 | +3.67€ | 2 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 333 | -0.016 | +7.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 731 | -0.014 | +27.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 341 | -0.016 | +9.66€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 390 | -0.013 | +17.40€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 33750 | -0.005 | +1518.43€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 33750 | -0.005 | +1518.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5980 | +0.021 | +752.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5980 | +0.021 | +752.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5112 | -0.031 | -73.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5112 | -0.031 | -73.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6072 | +0.017 | +540.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6072 | +0.017 | +540.50€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4896 | -0.054 | -170.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4896 | -0.054 | -170.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5688 | -0.009 | +201.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5688 | -0.009 | +201.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6002 | +0.011 | +268.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6002 | +0.011 | +268.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6049 | -0.061 | -152.88€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6049 | -0.061 | -152.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1461 | -0.084 | -41.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1461 | -0.084 | -41.97€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 686 | -0.125 | -32.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 686 | -0.125 | -32.13€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1787 | -0.078 | -34.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1787 | -0.078 | -34.55€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 85038 | -0.073 | +1776.73€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 85038 | -0.073 | +1776.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 14495 | -0.076 | +854.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 14495 | -0.076 | +854.43€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 12992 | -0.096 | -690.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 12992 | -0.096 | -690.42€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 14769 | -0.067 | +763.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 14769 | -0.067 | +763.99€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 12525 | -0.092 | -215.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 12525 | -0.092 | -215.62€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 15513 | -0.049 | +378.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 15513 | -0.049 | +378.68€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 14744 | -0.063 | +685.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 14744 | -0.063 | +685.68€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7870 | -0.028 | -133.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7870 | -0.028 | -133.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1810 | -0.036 | -10.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1810 | -0.036 | -10.24€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2228 | -0.024 | -28.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2228 | -0.024 | -28.48€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1067 | -0.044 | -18.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1067 | -0.044 | -18.85€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 766 | -0.022 | -24.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 766 | -0.022 | -24.97€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1253 | +0.110 | +432.29€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1117 | +0.116 | +419.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 255 | +0.134 | +124.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 255 | +0.134 | +124.22€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 214 | +0.111 | +63.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 214 | +0.111 | +63.38€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 233 | +0.104 | +84.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 233 | +0.104 | +84.73€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 195 | +0.124 | +84.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 195 | +0.124 | +84.25€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 220 | +0.099 | +63.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 220 | +0.099 | +63.12€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 691 | -0.040 | -46.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 691 | -0.040 | -46.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 139 | -0.004 | +4.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 139 | -0.004 | +4.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 99 | -0.064 | -11.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 99 | -0.064 | -11.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 197 | -0.053 | -21.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 197 | -0.053 | -21.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 142 | -0.028 | -8.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 142 | -0.028 | -8.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 114 | -0.052 | -10.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 114 | -0.052 | -10.17€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 642 | -0.104 | -54.80€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 294 | -0.155 | -68.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 241 | -0.191 | -68.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 53 | +0.009 | +0.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 223 | -0.069 | -0.28€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 173 | -0.071 | -6.51€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 50 | -0.058 | +6.23€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 125 | -0.043 | +13.49€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 101 | -0.063 | +7.26€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 24 | +0.038 | +6.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 515 | -0.127 | -68.01€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 127 | -0.012 | +13.21€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 805 | -0.200 | -36.85€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 332 | -0.198 | -29.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 291 | -0.196 | -29.68€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 41 | -0.198 | +0.21€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 274 | -0.217 | -26.09€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 239 | -0.226 | -31.18€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 35 | -0.149 | +5.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 199 | -0.177 | +18.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 183 | -0.176 | +14.04€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 713 | -0.202 | -46.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 92 | -0.181 | +9.98€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 346 | +0.402 | +266.13€ | 0 | 14 |
| ✅ RESOLUTION_SNIPER#BTC | 39 | +0.134 | +0.80€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 39 | +0.134 | +0.80€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 86 | +0.364 | +71.63€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 86 | +0.364 | +71.63€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 221 | +0.460 | +193.70€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 221 | +0.460 | +193.70€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 346 | +0.402 | +266.13€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 575 | +0.032 | +17.20€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 575 | +0.032 | +17.20€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 280 | +0.028 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 280 | +0.028 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 39 | +0.085 | +3.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 39 | +0.085 | +3.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 62 | +0.000 | -1.18€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 62 | +0.000 | -1.18€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 194 | +0.036 | +11.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 194 | +0.036 | +11.78€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 2948 | -0.021 | -117.00€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2948 | -0.021 | -117.00€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 896 | -0.020 | -30.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 896 | -0.020 | -30.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 573 | -0.024 | -23.73€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 573 | -0.024 | -23.73€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1323 | -0.018 | -48.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1323 | -0.018 | -48.20€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 77 | -0.044 | -5.84€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 77 | -0.044 | -5.84€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 39 | +0.012 | -1.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 39 | +0.012 | -1.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 8941 | +0.022 | +122.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8941 | +0.022 | +122.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2466 | +0.024 | +31.75€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2466 | +0.024 | +31.75€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2036 | +0.030 | +50.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2036 | +0.030 | +50.63€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2709 | +0.013 | +9.59€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2709 | +0.013 | +9.59€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1730 | +0.022 | +30.44€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1730 | +0.022 | +30.44€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8038 | +0.013 | -40.76€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8038 | +0.013 | -40.76€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3204 | +0.017 | -5.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3204 | +0.017 | -5.96€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3187 | +0.012 | -19.16€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3187 | +0.012 | -19.16€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1647 | +0.006 | -15.64€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1647 | +0.006 | -15.64€ | 2 | 0 |
| ✅ UPDOWN_GBM | 46499 | +0.037 | +3096.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 12051 | +0.073 | +2309.58€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1631 | +0.004 | +7.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 29838 | +0.029 | +756.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2803 | +0.002 | +24.00€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4719 | +0.075 | +586.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 864 | +0.161 | +380.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3822 | +0.056 | +206.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 8932 | +0.045 | +685.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1574 | +0.088 | +357.64€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 437 | +0.013 | +4.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 5587 | +0.047 | +291.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1268 | +0.004 | +30.96€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 66 | -0.088 | +0.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 5356 | +0.043 | +364.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 816 | +0.142 | +297.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4512 | +0.026 | +68.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 10206 | +0.027 | +460.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3041 | +0.050 | +351.43€ | 1 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 430 | +0.007 | +9.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 5732 | +0.022 | +105.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 945 | -0.002 | -8.98€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 58 | -0.117 | +3.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 10506 | +0.017 | +300.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2892 | +0.028 | +209.49€ | 0 | 13 |
| ✅ UPDOWN_GBM#SOL#240min | 421 | -0.004 | -1.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6553 | +0.017 | +93.62€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 590 | +0.005 | +2.02€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 50 | -0.154 | -3.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 6778 | +0.040 | +700.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2864 | +0.088 | +712.92€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 282 | +0.000 | -3.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3632 | +0.006 | -9.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 174 | -0.119 | +0.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 624 | +0.351 | +209.89€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 624 | +0.351 | +209.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 341 | +0.357 | +113.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 341 | +0.357 | +113.37€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 283 | +0.342 | +96.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 283 | +0.342 | +96.52€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 13771 | -0.033 | +3016.36€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 13771 | -0.033 | +3016.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 967 | -0.052 | +368.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 967 | -0.052 | +368.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2519 | -0.117 | +45.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2519 | -0.117 | +45.51€ | 3 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 515 | +0.196 | +379.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 515 | +0.196 | +379.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1586 | +0.209 | +969.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1586 | +0.209 | +969.18€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4111 | -0.062 | +585.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4111 | -0.062 | +585.85€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4073 | -0.071 | +667.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4073 | -0.071 | +667.89€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 157 | +0.035 | +7.28€ | 1 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 157 | +0.035 | +7.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 157 | +0.035 | +7.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 157 | +0.035 | +7.28€ | 1 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1015 | +0.291 | +815.08€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1015 | +0.291 | +815.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 557 | +0.285 | +423.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 557 | +0.285 | +423.64€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 458 | +0.296 | +391.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 458 | +0.296 | +391.44€ | 0 | 9 |
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
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 2686 | +0.303 | +1314.66€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 941 | +0.255 | +137.45€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1022 | +0.294 | +439.08€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 723 | +0.377 | +738.13€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.054) — sin ventaja clara. oversold(IBS<0.3): IC=+0.049 n=16343 | neutral: IC=+0.036 n=17328 | overbought(IBS>0.7): IC=+0.090 n=16615
  - _Datos_: n=52096 IC=+0.059 PNL=+6637.19€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 585 celda(s) pasan gate riguroso completo de 2348 evaluadas (n>=40) y 3323 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.028 < 0.08 — monitorear
  - _Datos_: n=2892 IC=+0.028 PNL=+209.49€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1022/15 IC=+0.294 PNL=+439.08€ | BTC: n=941/15 IC=+0.255 PNL=+137.45€ | SOL: n=723/15 IC=+0.377 PNL=+738.13€

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
  - _Estado_: 46437 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.126 n=420/60 | contraria IC=+0.178 n=399 | gap=-0.053 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

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
  - _Estado_: ETH#60min: n=945/40 IC=-0.002 PNL=-8.98€ | BTC#60min: n=1268/40 IC=+0.004 PNL=+30.96€ | SOL#60min: n=590/40 IC=+0.005 PNL=+2.02€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=387951 | tras_1loss IC=+0.084 n=299447 | tras_2loss IC=+0.053 n=124529/40 | gap=-0.004 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.018 n=5698 | contrario_BTC IC=+0.035 n=5036/40 | gap=+0.017 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.08 con n=454 PNL=+335.34€
  - _Datos_: n=454 IC=+0.210 PNL=+335.34€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.330 > 0.1 con n=2193 PNL=+1194.85€
  - _Datos_: n=2193 IC=+0.330 PNL=+1194.85€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=375 IC=+0.070 PNL=+41.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=375 IC=+0.070 PNL=+41.13€

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
  - _Estado_: n=44481 IC=+0.036 PNL=+2957.59€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=44481 IC=+0.036 PNL=+2957.59€

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
  - _Estado_: n=1931 IC=+0.004 PNL=-4.27€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1931 IC=+0.004 PNL=-4.27€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=872 IC=-0.002 PNL=+28.26€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=872 IC=-0.002 PNL=+28.26€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=605 IC=+0.017 PNL=+26.45€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=605 IC=+0.017 PNL=+26.45€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.193 > 0.1 con n=2555 PNL=+1679.40€
  - _Datos_: n=2555 IC=+0.193 PNL=+1679.40€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1457 IC=+0.055 PNL=+105.66€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1457 IC=+0.055 PNL=+105.66€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1574 IC=+0.088 PNL=+357.64€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1574 IC=+0.088 PNL=+357.64€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=6865 PNL=+1734.75€
  - _Datos_: n=6865 IC=+0.090 PNL=+1734.75€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=185 IC=-0.254 PNL=-7.48€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=185 IC=-0.254 PNL=-7.48€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=308 IC=-0.035 PNL=-3.81€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=308 IC=-0.035 PNL=-3.81€

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
  - _Estado_: n=6315 IC=+0.000 PNL=+5.55€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6315 IC=+0.000 PNL=+5.55€

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
  - _Estado_: n=8526 IC=+0.039 PNL=+556.45€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=8526 IC=+0.039 PNL=+556.45€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=2863 IC=+0.059 PNL=+362.92€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2863 IC=+0.059 PNL=+362.92€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=399 PNL=+122.71€
  - _Datos_: n=399 IC=+0.111 PNL=+122.71€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.148 > 0.08 con n=720 PNL=+187.66€
  - _Datos_: n=720 IC=+0.148 PNL=+187.66€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.107 > 0.08 con n=545 PNL=+257.19€
  - _Datos_: n=545 IC=+0.107 PNL=+257.19€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=64087 IC=+0.118 PNL=+23843.63€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=64087 IC=+0.118 PNL=+23843.63€

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
  - _Estado_: n=6841 IC=+0.042 PNL=+538.64€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6841 IC=+0.042 PNL=+538.64€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.02 con n=714 PNL=+269.53€
  - _Datos_: n=714 IC=+0.119 PNL=+269.53€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.449 > 0.1 con n=1256 PNL=+1230.93€
  - _Datos_: n=1256 IC=+0.449 PNL=+1230.93€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=16883 IC=+0.059 PNL=+2094.92€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=16883 IC=+0.059 PNL=+2094.92€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.1 con n=4150 PNL=+2311.07€
  - _Datos_: n=4150 IC=+0.203 PNL=+2311.07€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.151 < -0.1 con n=282 PNL=+27.19€
  - _Datos_: n=282 IC=-0.151 PNL=+27.19€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2210 IC=+0.055 PNL=+230.77€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2210 IC=+0.055 PNL=+230.77€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=95 IC=-0.108 PNL=+4.21€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=95 IC=-0.108 PNL=+4.21€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.1 con n=520 PNL=+142.91€
  - _Datos_: n=520 IC=+0.123 PNL=+142.91€

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
  - _Estado_: n=21212 IC=-0.137 PNL=+1503.40€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=21212 IC=-0.137 PNL=+1503.40€

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
  - _Estado_: n=2217 IC=+0.139 PNL=+1261.34€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2217 IC=+0.139 PNL=+1261.34€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.195 > 0.08 con n=2516 PNL=+1666.76€
  - _Datos_: n=2516 IC=+0.195 PNL=+1666.76€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.211 > 0.08 con n=565 PNL=+296.05€
  - _Datos_: n=565 IC=+0.211 PNL=+296.05€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.231 < -0.1 con n=2093 PNL=-187.01€
  - _Datos_: n=2093 IC=-0.231 PNL=-187.01€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=6210 IC=+0.181 PNL=+4356.95€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=6210 IC=+0.181 PNL=+4356.95€

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
  - _Estado_: n=2244 IC=+0.070 PNL=+689.96€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2244 IC=+0.070 PNL=+689.96€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.08 con n=2046 PNL=+1442.70€
  - _Datos_: n=2046 IC=+0.180 PNL=+1442.70€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3405 IC=-0.032 PNL=+875.88€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3405 IC=-0.032 PNL=+875.88€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.238 > 0.08 con n=3664 PNL=-319.76€
  - _Datos_: n=3664 IC=+0.238 PNL=-319.76€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=44 IC=+0.000 PNL=+5.87€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=44 IC=+0.000 PNL=+5.87€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1209) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1209 IC=+0.101 PNL=+284.30€

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
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.409 n=461) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=461 IC=+0.409 PNL=+649.06€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=9990 IC=+0.179 PNL=-1119.21€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=9990 IC=+0.179 PNL=-1119.21€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.1 con n=158 PNL=+97.19€
  - _Datos_: n=158 IC=+0.206 PNL=+97.19€
