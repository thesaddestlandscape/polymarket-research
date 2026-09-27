# Hipótesis automáticas — 2026-09-27 19:43 UTC
_Generado por shadow_postmortem.py sobre 639828 resoluciones (PNL=+74018.77€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=521)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.237 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.210 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.8032` → IC=+0.255 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8032 (IC base=+0.139)

- **PATRÓN** `banda_z` > `4.143` → IC=+0.166 (n=555)

  - _Acción_: Kelly boost +0.83€ cuando `banda_z` > 4.143 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.155 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 11.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=594)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4928.6279` → IC=+0.158 (n=185)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4928.6279 (IC base=+0.139)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.125 (n=521)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.056)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=386)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.239 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.148)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.209 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.148)

- **PATRÓN** `banda_hit_calibrado` > `0.7976` → IC=+0.266 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7976 (IC base=+0.148)

- **PATRÓN** `banda_z` > `4.334` → IC=+0.172 (n=446)

  - _Acción_: Kelly boost +0.86€ cuando `banda_z` > 4.334 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.168 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=505)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `8596.0083` → IC=+0.124 (n=219)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 8596.0083 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.167 (n=151)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 94.0 (IC base=+0.059)

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
- **FILTRO** `restante_s_al_confirmar` < `146.12` → IC=-0.217 (n=7407)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.12
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=22222)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `138.26` → IC=-0.246 (n=965)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.26
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=2896)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.44` → IC=-0.308 (n=874)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.44
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2624)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.41` → IC=-0.202 (n=1809)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.41
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=5430)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.34` → IC=-0.337 (n=1455)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.34
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=4367)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.207 (n=14534)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3632)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5629.5267` → IC=+0.178 (n=2322)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 5629.5267 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.137 (n=12148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=14797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.232 (n=11515)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=5884)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7837.3595` → IC=+0.174 (n=2233)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7837.3595 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1753)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=2210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `15920.3308` → IC=+0.236 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15920.3308 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=1584)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.206 (n=1763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.263 (n=1583)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=2252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `15869.986` → IC=+0.214 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15869.986 (IC base=+0.200)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.175 (n=337)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.62 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `4566.8958` → IC=+0.145 (n=240)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4566.8958 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.101)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.143 (n=853)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.165 (n=225)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.101)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=2970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.148 (n=2526)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.346 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.365 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.235 (n=1553)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.232)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=631)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.254 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.139 (n=798)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `1302.9991` → IC=+0.149 (n=698)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1302.9991 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.404 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.165 (n=609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 7.0 (IC base=+0.157)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=748)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.157)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.209 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.116)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=12275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=11723)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.227 (n=4000)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `5111.8837` → IC=+0.335 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5111.8837 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=2953)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.172 (n=2803)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.176 (n=2800)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.167)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.251 (n=996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.250 (n=989)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.245)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.344 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.245)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=2747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=2769)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=2353)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.250 (n=2558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.325 (n=828)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.195 (n=2710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.198 (n=2101)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.193)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.435 (n=564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `11135.4127` → IC=+0.457 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11135.4127 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.444 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `14120.495` → IC=+0.445 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14120.495 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.443 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.461 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.427 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `3355.2252` → IC=+0.444 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3355.2252 (IC base=+0.429)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=36510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.236 (n=16237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.179 (n=6295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=5044)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=6831)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=6568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=6543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.264 (n=3732)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=6647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=6633)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=3293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=2469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.265 (n=2266)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=6048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.258 (n=2435)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.197 (n=6100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.253 (n=2281)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5545)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.125 (n=5158)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=5165)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=6790)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.66` → IC=+0.140 (n=5133)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.66 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=2795)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.12` → IC=+0.127 (n=2547)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.12 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.141 (n=2833)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.94 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.137 (n=2940)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 6.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `3.31` → IC=+0.144 (n=2557)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.31 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=2750)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.127 (n=2592)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.2 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.133 (n=2868)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.26` → IC=+0.139 (n=2596)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.26 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `4103.5959` → IC=+0.305 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4103.5959 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.287 (n=548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.332 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `4254.8679` → IC=+0.297 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4254.8679 (IC base=+0.277)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.328 (n=394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1725.6011` → IC=+0.316 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1725.6011 (IC base=+0.291)

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
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.438 (n=466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.435 (n=459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.435 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `2547.1781` → IC=+0.433 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2547.1781 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.434 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.437 (n=252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=265)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4847` → IC=+0.126 (n=8637)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.4847 (IC base=+0.108)

- **PATRÓN** `ibs_20min` > `0.9839` → IC=+0.244 (n=2879)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9839 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` < `0.2184` → IC=+0.256 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2184 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.968` → IC=+0.181 (n=3303)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 5.968 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `1.2074` → IC=+0.251 (n=2369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2074 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` > `0.6139` → IC=+0.255 (n=2369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6139 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.227 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` > `1.9024` → IC=+0.212 (n=3977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9024 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.134 (n=10453)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5714 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.5999` → IC=+0.205 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5999 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` < `0.6967` → IC=+0.186 (n=1628)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6967 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `1.0502` → IC=+0.175 (n=1676)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.0502 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.225 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.5694` → IC=+0.200 (n=5599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5694 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `129.0` → IC=+0.213 (n=6059)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 129.0 (IC base=+0.066)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.194 (n=654)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0049 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.173 (n=647)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0081 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3472` → IC=+0.172 (n=1936)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3472 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.175 (n=931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.173 (n=1303)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.138` → IC=+0.268 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.138 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.210 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.44` → IC=+0.169 (n=1818)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.44 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.180 (n=1969)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.04 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.247 (n=1337)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.1971` → IC=+0.259 (n=994)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1971 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.248 (n=1024)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.290 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.523` → IC=+0.239 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.523 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.464` → IC=+0.244 (n=1558)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.464 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.0922` → IC=+0.232 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0922 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.264 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.6131` → IC=+0.247 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6131 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=1640)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1820.04` → IC=+0.236 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1820.04 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.239 (n=664)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1109` → IC=+0.244 (n=661)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1109 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.236 (n=1501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=1527)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.9018` → IC=+0.264 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9018 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.3455` → IC=+0.224 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3455 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.547` → IC=+0.265 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.547 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2569` → IC=+0.223 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2569 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.0825` → IC=+0.230 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0825 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.250 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.3852` → IC=+0.236 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3852 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `11116.6074` → IC=+0.224 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11116.6074 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.179 (n=515)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0745` → IC=+0.165 (n=515)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0745 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.146 (n=687)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.708` → IC=+0.168 (n=1544)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.708 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1271` → IC=+0.152 (n=1379)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1271 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.289` → IC=+0.148 (n=245)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 11.289 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.31` → IC=+0.144 (n=1414)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.31 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.150 (n=1544)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2035 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.174 (n=409)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.152 (n=1434)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.144 (n=956)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `14067.2635` → IC=+0.146 (n=1029)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 14067.2635 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.168 (n=597)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 233.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.212 (n=645)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=2031)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=1733)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.269` → IC=+0.259 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.269 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.189 (n=1679)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.3569` → IC=+0.201 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3569 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.7734` → IC=+0.196 (n=1646)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.7734 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=2297)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.222 (n=1471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6119` → IC=+0.214 (n=1672)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6119 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=775)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.241 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.707` → IC=+0.234 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.707 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.534` → IC=+0.212 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.534 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3506` → IC=+0.262 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3506 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7564` → IC=+0.208 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7564 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.1782` → IC=+0.216 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1782 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.219 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1979.96` → IC=+0.212 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1979.96 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.218 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.212)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=105)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=2343)

- **PATRÓN** `ibs_20min` > `0.9471` → IC=+0.216 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9471 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `0.3545` → IC=+0.328 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3545 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.524` → IC=+0.331 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.524 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.789` → IC=+0.168 (n=762)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 4.789 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.335 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `1.2107` → IC=+0.328 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2107 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.356 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.21` → IC=+0.331 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.21 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.334 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `0.6576` → IC=+0.210 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6576 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` < `0.6874` → IC=+0.163 (n=402)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6874 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.2286` → IC=+0.215 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2286 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.5312` → IC=+0.168 (n=768)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.5312 (IC base=+0.019)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.182 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=352)

- **FILTRO** `ibs_20min` < `0.2941` → IC=-0.207 (n=104)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=312)

- **FILTRO** `ibs_20min` > `0.25` → IC=-0.126 (n=2330)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=1165)

- **FILTRO** `sigma_ewma_delta_pct` > `8.719` → IC=-0.213 (n=371)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.719
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=3124)

- **PATRÓN** `ibs_20min` > `0.7834` → IC=+0.229 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7834 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `1.024` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.024 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` < `0.5572` → IC=+0.280 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5572 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.289` → IC=+0.127 (n=148)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 2.289 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` > `0.5663` → IC=+0.279 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5663 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.7487` → IC=+0.295 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7487 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.291 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.045)

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.125 (n=1165)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.25 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` > `0.7235` → IC=+0.265 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7235 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` < `0.4545` → IC=+0.227 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4545 (IC base=-0.043)

- **PATRÓN** `volumen_regimen` < `0.6728` → IC=+0.271 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6728 (IC base=-0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.1582` → IC=+0.272 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1582 (IC base=-0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.278 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=-0.043)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6536` → IC=-0.184 (n=606)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6536
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1831)

- **FILTRO** `ibs_20min` < `0.7191` → IC=-0.157 (n=1608)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7191
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=829)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.203 (n=486)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1951)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.207 (n=896)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=2703)

- **PATRÓN** `dist_vwap_pct` > `0.4566` → IC=+0.315 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4566 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2822` → IC=+0.310 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2822 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.307 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.296 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.4239` → IC=+0.297 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4239 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.7985` → IC=+0.295 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7985 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.5572` → IC=+0.273 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5572 (IC base=-0.021)

- **PATRÓN** `volumen_regimen` < `0.7292` → IC=+0.257 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7292 (IC base=-0.021)

- **PATRÓN** `volumen_regimen` > `1.2467` → IC=+0.289 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2467 (IC base=-0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.1023` → IC=+0.277 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1023 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.1375` → IC=+0.266 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1375 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.5229` → IC=+0.252 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5229 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.198 (n=3666)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0097 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.475` → IC=+0.187 (n=9813)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.475 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `1.0358` → IC=+0.290 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0358 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.628` → IC=+0.158 (n=5106)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.628 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6894` → IC=+0.252 (n=3510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6894 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.271 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4647` → IC=+0.238 (n=2126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4647 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6649` → IC=+0.249 (n=2125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6649 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.271 (n=5896)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.160 (n=3604)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0091 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.5502` → IC=+0.153 (n=9515)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5502 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.7088` → IC=+0.243 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7088 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2458` → IC=+0.244 (n=3055)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2458 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `0.6335` → IC=+0.245 (n=1073)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6335 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.205` → IC=+0.250 (n=1073)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.205 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2416` → IC=+0.308 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2416 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.5983` → IC=+0.265 (n=1893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5983 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `2.2956` → IC=+0.261 (n=1951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2956 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.271 (n=4176)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 83.0 (IC base=+0.073)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2567` → IC=-0.150 (n=758)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2567
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=2274)

- **FILTRO** `sigma_ewma_delta_pct` > `4.528` → IC=-0.163 (n=576)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.528
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1917)

- **PATRÓN** `ibs_20min` > `0.8964` → IC=+0.270 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8964 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.823` → IC=+0.208 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.823 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2226` → IC=+0.267 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2226 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4393` → IC=+0.181 (n=324)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4393 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.185` → IC=+0.210 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.185 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.201 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.2144` → IC=+0.468 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2144 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4197` → IC=+0.456 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4197 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.0444` → IC=+0.452 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0444 (IC base=-0.023)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8669` → IC=+0.166 (n=735)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8669 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.2979` → IC=+0.174 (n=397)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.2979 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.6747` → IC=+0.176 (n=909)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6747 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.246 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.425` → IC=+0.193 (n=333)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.425 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.4118` → IC=+0.183 (n=332)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.4118 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.195 (n=437)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 239.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1506` → IC=+0.219 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1506 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `0.857` → IC=+0.229 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.857 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2671` → IC=+0.305 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2671 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.219 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4386 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1626` → IC=+0.229 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1626 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `460.0` → IC=+0.218 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 460.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.289 (n=571)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.248)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.252 (n=1715)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.249 (n=1730)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.248)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.772` → IC=+0.283 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.772 (IC base=+0.248)

- **PATRÓN** `volumen_pendiente_norm` < `0.1014` → IC=+0.261 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1014 (IC base=+0.248)

- **PATRÓN** `volumen_spike_ratio` > `3.3381` → IC=+0.268 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3381 (IC base=+0.248)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=2017)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.248)

- **PATRÓN** `libro_liquidez` > `1913.4832` → IC=+0.258 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1913.4832 (IC base=+0.248)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.314 (n=632)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.6123` → IC=+0.286 (n=1390)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6123 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.324 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.3448` → IC=+0.292 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3448 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.299 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.3376` → IC=+0.300 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3376 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.7371` → IC=+0.288 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7371 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.6935` → IC=+0.291 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6935 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `1906.4295` → IC=+0.299 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1906.4295 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.287 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.283)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.3022` → IC=-0.167 (n=547)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3022
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1647)

- **FILTRO** `ibs_20min` > `0.7732` → IC=-0.186 (n=645)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7732
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=1936)

- **PATRÓN** `ibs_20min` > `0.9124` → IC=+0.181 (n=549)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.9124 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` < `0.1812` → IC=+0.225 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1812 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` < `0.9978` → IC=+0.243 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9978 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` > `0.5875` → IC=+0.219 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5875 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.264 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` < `1.506` → IC=+0.261 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.506 (IC base=+0.016)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.276 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 70.0 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` > `0.1453` → IC=+0.217 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1453 (IC base=-0.006)

- **PATRÓN** `dist_vwap_pct` < `0.3286` → IC=+0.207 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3286 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` < `0.6371` → IC=+0.237 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6371 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.8148` → IC=+0.258 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8148 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.1439` → IC=+0.246 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1439 (IC base=-0.006)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.259 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 137.0 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7391` → IC=-0.192 (n=1165)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7391
  - _Potencial_: sin este filtro IC_bueno=+0.279 (n=1165)

- **FILTRO** `ibs_20min` > `0.6842` → IC=-0.235 (n=590)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6842
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1776)

- **FILTRO** `sigma_ewma_delta_pct` > `4.766` → IC=-0.189 (n=515)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.766
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=1851)

- **PATRÓN** `ibs_20min` > `0.7391` → IC=+0.279 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7391 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `0.8494` → IC=+0.327 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8494 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.658` → IC=+0.171 (n=366)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.658 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` < `0.8642` → IC=+0.304 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8642 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.297 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.296 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2714` → IC=+0.305 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2714 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4355` → IC=+0.323 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4355 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.319 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.582` → IC=+0.123 (n=1562)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.582 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.2196` → IC=+0.226 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2196 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `0.6965` → IC=+0.256 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6965 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.219 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.220 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.481` → IC=+0.232 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.481 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.240 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.015)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0167` → IC=+0.315 (n=934)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0167 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.295 (n=658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` > `0.7396` → IC=+0.323 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7396 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2148` → IC=+0.314 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2148 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.662` → IC=+0.303 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.662 (IC base=+0.279)

- **PATRÓN** `volumen_regimen` > `0.8606` → IC=+0.304 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8606 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.329 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.288 (n=1332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.282 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `2468.3035` → IC=+0.288 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2468.3035 (IC base=+0.279)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.319 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.306 (n=999)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.1975` → IC=+0.280 (n=660)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1975 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.288 (n=513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.277)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.281 (n=743)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` < `0.2903` → IC=+0.317 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2903 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.3139` → IC=+0.284 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3139 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.279 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2288 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.477` → IC=+0.292 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.477 (IC base=+0.277)

- **PATRÓN** `volumen_regimen` < `0.6412` → IC=+0.283 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6412 (IC base=+0.277)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.309 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` > `0.2352` → IC=+0.341 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2352 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` < `1.4225` → IC=+0.287 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4225 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `2.1452` → IC=+0.276 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1452 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `2614.9946` → IC=+0.279 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2614.9946 (IC base=+0.277)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.177 (n=2817)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.202 (n=2804)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3577` → IC=+0.177 (n=7399)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3577 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=8798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.5738` → IC=+0.220 (n=8408)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5738 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.1753` → IC=+0.194 (n=3644)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1753 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.362` → IC=+0.255 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.362 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.162 (n=5576)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2089 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.628` → IC=+0.161 (n=5575)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.628 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2429` → IC=+0.197 (n=1702)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2429 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.5584` → IC=+0.168 (n=3555)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5584 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.613` → IC=+0.177 (n=2693)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.613 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `1956.263` → IC=+0.171 (n=7511)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1956.263 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.183 (n=7316)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 110.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.184 (n=5366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0066 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.0807` → IC=+0.211 (n=2682)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0807 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=3078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.4828` → IC=+0.227 (n=8047)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4828 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` < `0.233` → IC=+0.161 (n=5819)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.233 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.342` → IC=+0.194 (n=1363)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.342 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.1735` → IC=+0.154 (n=5800)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1735 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.214 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.5593` → IC=+0.168 (n=3236)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5593 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6212` → IC=+0.171 (n=2452)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.6212 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.176 (n=7014)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 112.0 (IC base=+0.169)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.219 (n=482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.189 (n=477)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0083 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.3396` → IC=+0.211 (n=1424)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3396 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=1503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=956)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.154` → IC=+0.327 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.154 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.237 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.185 (n=1323)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=1450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.241 (n=931)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.248 (n=945)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1823` → IC=+0.284 (n=706)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1823 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=950)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=522)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3455` → IC=+0.259 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3455 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.305` → IC=+0.248 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.305 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.236 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.248 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4211` → IC=+0.266 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4211 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1820.92` → IC=+0.244 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1820.92 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.236 (n=418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0729` → IC=+0.199 (n=417)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0729 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=1255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.4047` → IC=+0.227 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4047 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2046` → IC=+0.210 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2046 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.481` → IC=+0.234 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.481 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.6862` → IC=+0.170 (n=550)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6862 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.0742` → IC=+0.168 (n=567)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0742 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.204 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.5038` → IC=+0.179 (n=534)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5038 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.4602` → IC=+0.166 (n=405)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.4602 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `10620.0277` → IC=+0.171 (n=1249)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10620.0277 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `446.0` → IC=+0.161 (n=1174)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 446.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.198 (n=451)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0026 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2905` → IC=+0.160 (n=1339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.2905 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5752` → IC=+0.189 (n=1339)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5752 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1308` → IC=+0.162 (n=1329)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1308 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.889` → IC=+0.200 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.889 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1967` → IC=+0.159 (n=1339)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1967 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1558` → IC=+0.151 (n=408)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.1558 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4481` → IC=+0.148 (n=1227)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4481 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4259` → IC=+0.136 (n=1228)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4259 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.163 (n=384)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 213.0 (IC base=+0.137)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.214 (n=639)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.2374` → IC=+0.219 (n=940)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2374 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.278 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2028` → IC=+0.206 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2028 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.7994` → IC=+0.199 (n=592)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.7994 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.7847` → IC=+0.215 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7847 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.209 (n=1664)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.232 (n=1186)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.0995` → IC=+0.256 (n=396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0995 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.273 (n=408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.3486` → IC=+0.247 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3486 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.704` → IC=+0.256 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.704 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3546` → IC=+0.255 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3546 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.218 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.1999` → IC=+0.232 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1999 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.216 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.219)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.220 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.4227` → IC=+0.160 (n=1343)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4227 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.3707` → IC=+0.197 (n=1343)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3707 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1491` → IC=+0.177 (n=883)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1491 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.995` → IC=+0.229 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.995 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.0335` → IC=+0.150 (n=1182)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0335 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6204` → IC=+0.147 (n=1343)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6204 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1011` → IC=+0.186 (n=571)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1011 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.4275` → IC=+0.160 (n=439)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4275 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.5102` → IC=+0.171 (n=439)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5102 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `5983.7933` → IC=+0.186 (n=895)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 5983.7933 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.150 (n=1280)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 160.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.156 (n=1412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0071 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3801` → IC=+0.144 (n=1412)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3801 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6485` → IC=+0.173 (n=1412)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6485 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.1533` → IC=+0.141 (n=1384)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1533 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.159 (n=502)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.149 (n=942)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8509 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.181 (n=211)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.8092` → IC=+0.139 (n=860)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8092 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `10015.5876` → IC=+0.162 (n=640)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 10015.5876 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.155 (n=693)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0101 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=1572)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.5098` → IC=+0.207 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5098 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.8396` → IC=+0.208 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8396 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.8` → IC=+0.256 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.8 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.2058` → IC=+0.131 (n=1528)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2058 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.6433` → IC=+0.123 (n=1527)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6433 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1637` → IC=+0.126 (n=1533)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1637 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.0983` → IC=+0.126 (n=581)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0983 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.5419` → IC=+0.137 (n=650)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.5419 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1585)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2898.521` → IC=+0.194 (n=693)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2898.521 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.134 (n=1185)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 49.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.157 (n=684)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0061 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1048` → IC=+0.167 (n=518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1048 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.213 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.0073` → IC=+0.126 (n=225)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 1.0073 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.2019` → IC=+0.143 (n=1411)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2019 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.111` → IC=+0.138 (n=252)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 9.111 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.6352` → IC=+0.146 (n=518)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6352 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.163 (n=194)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.138 (n=467)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.4215` → IC=+0.133 (n=467)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4215 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2758.8364` → IC=+0.165 (n=703)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2758.8364 (IC base=+0.116)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.228 (n=1302)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.2933` → IC=+0.203 (n=972)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2933 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=1521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.7381` → IC=+0.260 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7381 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.5174` → IC=+0.215 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5174 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.240 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.206 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2068 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.8543` → IC=+0.223 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8543 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2308` → IC=+0.268 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2308 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.146` → IC=+0.213 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.146 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4035` → IC=+0.211 (n=1409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4035 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.205 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2820.0323` → IC=+0.207 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2820.0323 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.228 (n=501)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.213 (n=680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.224 (n=501)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.0233` → IC=+0.307 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0233 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `1.2175` → IC=+0.222 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2175 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.2068` → IC=+0.207 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2068 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.43` → IC=+0.243 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.43 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.6328` → IC=+0.216 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6328 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.288 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1914` → IC=+0.198 (n=1194)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1914 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4265` → IC=+0.203 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4265 (IC base=+0.207)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.196 (n=704)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.173 (n=702)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0086 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.344` → IC=+0.165 (n=1848)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.344 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.195 (n=1056)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.7488` → IC=+0.213 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7488 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.6074` → IC=+0.174 (n=443)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.6074 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` < `0.149` → IC=+0.162 (n=1513)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.149 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.737` → IC=+0.185 (n=939)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.737 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.8707` → IC=+0.182 (n=1244)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.8707 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `0.6964` → IC=+0.163 (n=1666)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6964 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.185 (n=576)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.4459` → IC=+0.172 (n=677)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4459 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.8277` → IC=+0.167 (n=1354)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8277 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.164 (n=2375)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `2639.7171` → IC=+0.161 (n=1876)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2639.7171 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.178 (n=1882)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 151.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.137 (n=1426)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0056 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.3406` → IC=+0.127 (n=1881)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3406 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.126 (n=2155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.06` → IC=+0.193 (n=714)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.06 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.2074` → IC=+0.121 (n=1908)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` < 0.2074 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.6256` → IC=+0.131 (n=645)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.6256 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.130 (n=531)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.4526` → IC=+0.146 (n=688)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4526 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2764.7951` → IC=+0.123 (n=1909)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2764.7951 (IC base=+0.112)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.132 (n=691)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 20.0 (IC base=+0.112)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.152 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0038 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.1084` → IC=+0.152 (n=231)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1084 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.170 (n=492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 8.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.6598` → IC=+0.197 (n=348)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.6598 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.2846` → IC=+0.161 (n=187)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.2846 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.16` → IC=+0.130 (n=449)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.16 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.139 (n=236)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.167` → IC=+0.133 (n=489)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.167 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.9061` → IC=+0.161 (n=349)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.9061 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.0916` → IC=+0.153 (n=188)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0916 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.223` → IC=+0.137 (n=447)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.223 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.5157` → IC=+0.137 (n=453)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.5157 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `10902.4411` → IC=+0.143 (n=522)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 10902.4411 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.167 (n=169)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 146.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.208 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3366` → IC=+0.154 (n=662)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3366 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.185 (n=583)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6112 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.2995` → IC=+0.153 (n=696)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2995 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.494` → IC=+0.152 (n=251)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.494 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.238` → IC=+0.136 (n=600)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.238 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2185` → IC=+0.143 (n=662)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2185 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.716` → IC=+0.148 (n=591)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.716 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.194 (n=178)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1137` → IC=+0.160 (n=574)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1137 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4219` → IC=+0.147 (n=652)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4219 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `322.0` → IC=+0.151 (n=554)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 322.0 (IC base=+0.136)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.275 (n=291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.0953` → IC=+0.233 (n=219)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0953 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.9681` → IC=+0.269 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9681 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.1394` → IC=+0.214 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1394 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.207` → IC=+0.211 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.207 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.007` → IC=+0.237 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.007 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.214 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8331 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `1.1584` → IC=+0.229 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1584 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.1528` → IC=+0.271 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1528 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.4027` → IC=+0.229 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4027 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.7564` → IC=+0.235 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7564 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `12380.0176` → IC=+0.215 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12380.0176 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.084` → IC=+0.162 (n=205)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.084 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6874` → IC=+0.140 (n=270)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6874 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.227` → IC=+0.129 (n=95)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.227 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.153 (n=456)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0057 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.5405` → IC=+0.141 (n=510)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5405 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.172 (n=476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 8.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.932` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.932 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.556` → IC=+0.197 (n=275)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.556 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.069` → IC=+0.161 (n=449)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.069 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.7162` → IC=+0.145 (n=455)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7162 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.4824` → IC=+0.154 (n=163)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4824 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.2214` → IC=+0.174 (n=222)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.2214 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=539)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `3108.4588` → IC=+0.192 (n=170)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3108.4588 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.5217` → IC=+0.152 (n=458)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.5217 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6929` → IC=+0.147 (n=202)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6929 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `1.5789` → IC=+0.182 (n=190)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5789 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `2616.434` → IC=+0.135 (n=305)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2616.434 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.140 (n=401)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 40.0 (IC base=+0.093)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.173 (n=3612)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0047 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.209 (n=3608)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=11318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=3653)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.9453` → IC=+0.202 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9453 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.363` → IC=+0.245 (n=2723)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.363 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `0.8799` → IC=+0.168 (n=4832)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8799 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.203 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.5941` → IC=+0.191 (n=3477)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5941 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `1796.98` → IC=+0.175 (n=10824)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1796.98 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `84.0` → IC=+0.199 (n=8339)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 84.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.191 (n=6534)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1487` → IC=+0.189 (n=4310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1487 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=3696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.183 (n=4514)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5687` → IC=+0.237 (n=9790)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5687 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2483` → IC=+0.162 (n=6072)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2483 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.053` → IC=+0.199 (n=1372)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.053 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.731` → IC=+0.184 (n=9472)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.731 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7031` → IC=+0.164 (n=2948)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7031 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2876` → IC=+0.236 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2876 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6128` → IC=+0.189 (n=3012)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6128 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.197 (n=5853)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 47.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.216 (n=607)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.208 (n=1222)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.3504` → IC=+0.197 (n=1818)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.3504 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.208 (n=870)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.201 (n=1231)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.584` → IC=+0.349 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.584 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.253 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.8445` → IC=+0.195 (n=1147)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.8445 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=1834)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.262 (n=966)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.264 (n=1448)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1251` → IC=+0.282 (n=637)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1251 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=1312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=1316)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.3544` → IC=+0.283 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3544 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.467` → IC=+0.262 (n=1525)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.467 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.284 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.4366` → IC=+0.261 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4366 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6332` → IC=+0.276 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6332 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=1595)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1818.48` → IC=+0.263 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1818.48 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.204 (n=579)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.163 (n=763)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=1815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.3085` → IC=+0.204 (n=1731)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3085 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.1252` → IC=+0.186 (n=980)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1252 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.172 (n=395)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.174` → IC=+0.155 (n=1562)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.174 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6265` → IC=+0.181 (n=578)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6265 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2669` → IC=+0.204 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2669 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.1166` → IC=+0.162 (n=1475)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1166 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.7577` → IC=+0.160 (n=1117)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7577 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `11253.359` → IC=+0.159 (n=1547)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11253.359 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `472.0` → IC=+0.162 (n=1611)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 472.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.3218` → IC=+0.161 (n=1489)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3218 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=667)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.282` → IC=+0.237 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.282 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.6722` → IC=+0.157 (n=240)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6722 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1309` → IC=+0.163 (n=1349)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1309 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.5` → IC=+0.156 (n=248)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.5 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.511` → IC=+0.151 (n=1510)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 6.511 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.1888` → IC=+0.163 (n=1489)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1888 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1509` → IC=+0.192 (n=397)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1509 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.4071` → IC=+0.160 (n=1391)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4071 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.7569` → IC=+0.158 (n=927)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7569 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `418.0` → IC=+0.152 (n=1143)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 418.0 (IC base=+0.150)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.253 (n=588)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=1851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1793)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.825` → IC=+0.295 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.825 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.2097` → IC=+0.220 (n=1753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2097 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.230 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2097)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1917.9762` → IC=+0.222 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.9762 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.239 (n=1648)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1734` → IC=+0.239 (n=727)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1734 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.260 (n=626)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.239 (n=771)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.3586` → IC=+0.266 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3586 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.746` → IC=+0.273 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.746 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3426` → IC=+0.300 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3426 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.232 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.1698` → IC=+0.236 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1698 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.242 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1909.982` → IC=+0.240 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1909.982 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.232 (n=1445)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.233)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.190 (n=811)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4298` → IC=+0.151 (n=1841)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4298 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=1925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.8757` → IC=+0.265 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8757 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3554` → IC=+0.165 (n=720)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3554 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.567` → IC=+0.170 (n=304)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.567 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8727` → IC=+0.159 (n=1228)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8727 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2798` → IC=+0.216 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2798 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5207` → IC=+0.156 (n=786)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5207 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.4714` → IC=+0.157 (n=595)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.4714 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7942.2025` → IC=+0.235 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7942.2025 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.171 (n=755)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 87.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.157 (n=1320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0065 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4388` → IC=+0.146 (n=1500)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4388 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=683)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.5838` → IC=+0.197 (n=1320)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5838 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.3631` → IC=+0.135 (n=1518)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.3631 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.3` → IC=+0.164 (n=224)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.3 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.149 (n=660)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.695 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `1.1988` → IC=+0.136 (n=500)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.1988 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.231 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.145 (n=1428)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `7158.0464` → IC=+0.192 (n=680)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7158.0464 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `173.0` → IC=+0.137 (n=1421)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 173.0 (IC base=+0.133)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.139 (n=1229)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0081 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=1897)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.4694` → IC=+0.194 (n=1840)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.4694 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0841` → IC=+0.203 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0841 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.522` → IC=+0.238 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.522 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8919` → IC=+0.140 (n=1227)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8919 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.8515` → IC=+0.121 (n=1195)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` < 1.8515 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=1853)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2896.6553` → IC=+0.253 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2896.6553 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.134 (n=1431)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 53.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.174 (n=591)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0058 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.1326` → IC=+0.159 (n=590)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1326 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.205 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2216` → IC=+0.133 (n=1435)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.2216 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.468` → IC=+0.126 (n=1707)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.468 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.7128` → IC=+0.153 (n=779)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7128 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.168 (n=278)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4366` → IC=+0.143 (n=536)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4366 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2804.5712` → IC=+0.176 (n=590)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2804.5712 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.124 (n=1399)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 51.0 (IC base=+0.114)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.230 (n=1636)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=1916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.214 (n=1640)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.261 (n=1646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.2117` → IC=+0.233 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2117 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.248` → IC=+0.269 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.248 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.2447` → IC=+0.214 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2447 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.6395` → IC=+0.221 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6395 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.253 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.5001` → IC=+0.235 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5001 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.219 (n=1877)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2615.1096` → IC=+0.220 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2615.1096 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.221 (n=647)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.226 (n=647)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.215 (n=1369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.4214` → IC=+0.267 (n=1707)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4214 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `1.2245` → IC=+0.208 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2245 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.9159` → IC=+0.208 (n=2164)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9159 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.857` → IC=+0.263 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.857 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.2347` → IC=+0.240 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2347 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.271 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.1751` → IC=+0.203 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1751 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.4266` → IC=+0.202 (n=1753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4266 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=3293)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.198 (n=1082)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0048 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.5113` → IC=+0.180 (n=3241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.5113 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=1263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.175 (n=1428)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.9474` → IC=+0.230 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9474 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.1798` → IC=+0.182 (n=1219)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1798 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` < `0.463` → IC=+0.165 (n=2020)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.463 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.195` → IC=+0.198 (n=538)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.195 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.7023` → IC=+0.165 (n=952)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7023 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6248` → IC=+0.168 (n=2163)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.6248 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1703` → IC=+0.204 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1703 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4558` → IC=+0.176 (n=1068)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4558 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `1.8727` → IC=+0.178 (n=2134)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.8727 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=2320)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3797.5592` → IC=+0.170 (n=2160)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3797.5592 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.206 (n=831)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4847` → IC=+0.168 (n=2482)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4847 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.170 (n=942)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.1825` → IC=+0.178 (n=1092)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1825 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.671` → IC=+0.178 (n=479)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.671 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.224` → IC=+0.161 (n=2475)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.224 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.1015` → IC=+0.159 (n=2075)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1015 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.154 (n=2252)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2204` → IC=+0.152 (n=527)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2204 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.5388` → IC=+0.162 (n=1079)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5388 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.156 (n=1634)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3293)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `6458.5699` → IC=+0.158 (n=2217)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 6458.5699 (IC base=+0.150)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.198 (n=366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0054 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.180 (n=373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0033 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0875` → IC=+0.223 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0875 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.190 (n=185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 8.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.5463` → IC=+0.203 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5463 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1455` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1455 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.3655` → IC=+0.186 (n=403)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.3655 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.517` → IC=+0.185 (n=439)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 2.517 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `0.8402` → IC=+0.210 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8402 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.3007` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3007 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.209 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6311` → IC=+0.209 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6311 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `12563.2849` → IC=+0.221 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12563.2849 (IC base=+0.179)

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
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.181 (n=928)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0072 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3766` → IC=+0.181 (n=925)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3766 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.182 (n=360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 4.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.5305` → IC=+0.190 (n=701)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5305 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.8827` → IC=+0.183 (n=351)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.8827 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` < `0.2131` → IC=+0.182 (n=872)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2131 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.178` → IC=+0.185 (n=940)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 4.178 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.0845` → IC=+0.175 (n=925)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0845 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.177 (n=1051)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6398 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.194 (n=318)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.4736` → IC=+0.179 (n=1033)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.4736 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.176 (n=923)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=1047)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.174)

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
- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.157 (n=263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0111 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.157 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 3.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.2132` → IC=+0.186 (n=218)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.2132 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8918` → IC=+0.168 (n=200)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8918 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.211 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.5495` → IC=+0.149 (n=129)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5495 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.7686` → IC=+0.162 (n=193)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7686 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=351)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `3372.8412` → IC=+0.169 (n=267)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3372.8412 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.149 (n=246)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 55.0 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.182 (n=256)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0069 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.3939` → IC=+0.188 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3939 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.160 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 16.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.184 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 10.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.1364` → IC=+0.250 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1364 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.5982` → IC=+0.230 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5982 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.639` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.639 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.281` → IC=+0.163 (n=247)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 5.281 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.3617` → IC=+0.163 (n=256)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.3617 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.1103` → IC=+0.220 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1103 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.611` → IC=+0.170 (n=110)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.611 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.170 (n=113)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `3305.7742` → IC=+0.182 (n=256)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3305.7742 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.199 (n=217)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 46.0 (IC base=+0.153)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0065` → IC=-0.204 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0065
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=402)

- **FILTRO** `dist_vwap_pct` > `0.1776` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1776
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=366)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.170 (n=447)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0039 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6598` → IC=+0.192 (n=819)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.6598 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1429` → IC=+0.145 (n=494)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1429 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.471` → IC=+0.182 (n=212)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 11.471 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.183 (n=121)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `1380.3758` → IC=+0.121 (n=595)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1380.3758 (IC base=+0.085)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.120 (n=177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0033 (IC base=+0.020)

- **PATRÓN** `ibs_20min` < `0.0482` → IC=+0.293 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0482 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.1776` → IC=+0.125 (n=366)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1776 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.187` → IC=+0.130 (n=125)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 3.187 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.138` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.138 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.5523` → IC=+0.133 (n=265)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.5523 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.7169` → IC=+0.137 (n=177)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.7169 (IC base=+0.020)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.148 (n=347)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0058 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.4702` → IC=+0.185 (n=316)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4702 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `2.0813` → IC=+0.153 (n=243)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.0813 (IC base=+0.099)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.132 (n=150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0043 (IC base=+0.063)

- **PATRÓN** `ibs_20min` < `0.082` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.082 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.557` → IC=+0.149 (n=129)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.557 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` < `1.1168` → IC=+0.124 (n=147)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.1168 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` < `2.3987` → IC=+0.159 (n=124)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.3987 (IC base=+0.063)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0059` → IC=-0.214 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0059
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=124)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=129)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.143 (n=228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0049 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.6606` → IC=+0.224 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6606 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.3289` → IC=+0.172 (n=120)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3289 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.658` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.658 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2766` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2766 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.7369` → IC=+0.149 (n=172)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.7369 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `1125.4271` → IC=+0.154 (n=273)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1125.4271 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.7041` → IC=+0.154 (n=102)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.7041 (IC base=+0.000)

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
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.280 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=96)

- **FILTRO** `ibs_20min` > `0.2051` → IC=-0.311 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2051
  - _Potencial_: sin este filtro IC_bueno=+0.229 (n=68)

- **PATRÓN** `ibs_20min` > `0.6471` → IC=+0.153 (n=260)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6471 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.606` → IC=+0.139 (n=59)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.606 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.057)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.200 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=-0.027)

- **PATRÓN** `ibs_20min` < `0.2051` → IC=+0.229 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2051 (IC base=-0.027)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.202` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.202 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.1002` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1002 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.6676` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.6676 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` > `1.4883` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4883 (IC base=-0.027)

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

- **FILTRO** `volumen_regimen` > `1.1069` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.1069
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=51)

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
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=251)

- **FILTRO** `dist_vwap_pct` > `0.6226` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6226
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=353)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.164 (n=126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0058 (IC base=+0.083)

- **PATRÓN** `ibs_20min` > `0.641` → IC=+0.149 (n=274)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.641 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.4857` → IC=+0.202 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4857 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.1681` → IC=+0.176 (n=251)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.1681 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.105` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 6.105 (IC base=+0.071)

- **PATRÓN** `libro_liquidez` > `3751.1947` → IC=+0.174 (n=130)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3751.1947 (IC base=+0.071)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.5882` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5882
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=90)

- **FILTRO** `volumen_regimen` < `0.7797` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7797
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=90)

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
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=75)

- **FILTRO** `volumen_pendiente_norm` > `0.0671` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0671
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

- **FILTRO** `ibs_20min` > `0.1644` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1644
  - _Potencial_: sin este filtro IC_bueno=+0.171 (n=83)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.194 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0022 (IC base=+0.020)

- **PATRÓN** `ibs_20min` > `0.8853` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8853 (IC base=+0.020)

- **PATRÓN** `libro_liquidez` > `1627.214` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 1627.214 (IC base=+0.020)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.144 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0029 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.1644` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1644 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.8233` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.8233 (IC base=+0.059)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=776)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2906.827` → IC=+0.164 (n=266)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2906.827 (IC base=+0.109)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=776)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2906.827` → IC=+0.164 (n=266)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2906.827 (IC base=+0.109)

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
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=657)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=657)

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
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=217)

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
- **FILTRO** `py_entrada` < `0.43` → IC=-0.122 (n=479)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=498)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.134 (n=39)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=46)

- **FILTRO** `profundidad_ratio` < `255.7` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `profundidad_ratio` < 255.7
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=64)

- **PATRÓN** `py_entrada` > `0.44` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` > 0.44 (IC base=+0.017)

- **PATRÓN** `restante_min` > `12.73` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 12.73 (IC base=+0.017)

- **PATRÓN** `profundidad_ratio` > `801.2` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `profundidad_ratio` > 801.2 (IC base=+0.017)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.57` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.57 (IC base=+0.059)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `restante_min` > `13.45` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `restante_min` > 13.45
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=54)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.220 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=47)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=53)

- **FILTRO** `profundidad_ratio` < `56.9` → IC=-0.179 (n=54)

  - _Acción_: SKIP cuando `profundidad_ratio` < 56.9
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `profundidad_ratio` < `125.2` → IC=-0.141 (n=51)

  - _Acción_: SKIP cuando `profundidad_ratio` < 125.2
  - _Potencial_: sin este filtro IC_bueno=+0.190 (n=27)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.188 (n=30)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=65)

- **PATRÓN** `py_entrada` > `0.53` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.53 (IC base=-0.025)

- **PATRÓN** `profundidad_ratio` > `125.2` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `profundidad_ratio` > 125.2 (IC base=-0.025)

- **PATRÓN** `py_entrada` < `0.52` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.52 (IC base=-0.026)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=82)

- **FILTRO** `restante_min` < `3.89` → IC=-0.236 (n=51)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=51)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=80)

- **FILTRO** `lag_apertura_s` > `86.42` → IC=-0.278 (n=34)

  - _Acción_: SKIP cuando `lag_apertura_s` > 86.42
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=68)

- **FILTRO** `profundidad_ratio` < `85.6` → IC=-0.179 (n=51)

  - _Acción_: SKIP cuando `profundidad_ratio` < 85.6
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=51)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.44 (IC base=+0.052)

- **PATRÓN** `profundidad_ratio` > `24.5` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `profundidad_ratio` > 24.5 (IC base=+0.052)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.167 (n=40)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=46)

- **FILTRO** `restante_min` < `13.48` → IC=-0.156 (n=59)

  - _Acción_: SKIP cuando `restante_min` < 13.48
  - _Potencial_: sin este filtro IC_bueno=+0.224 (n=27)

- **FILTRO** `lag_apertura_s` > `90.92` → IC=-0.151 (n=64)

  - _Acción_: SKIP cuando `lag_apertura_s` > 90.92
  - _Potencial_: sin este filtro IC_bueno=+0.292 (n=22)

- **PATRÓN** `restante_min` > `13.48` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 13.48 (IC base=-0.034)

- **PATRÓN** `lag_apertura_s` < `90.92` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 90.92 (IC base=-0.034)

- **PATRÓN** `restante_min` > `13.48` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 13.48 (IC base=-0.005)

- **PATRÓN** `lag_apertura_s` < `90.99` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 90.99 (IC base=-0.005)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.46 (IC base=+0.015)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.171 (n=80)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=46)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.204 (n=69)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=79)

- **FILTRO** `restante_min` < `3.12` → IC=-0.140 (n=48)

  - _Acción_: SKIP cuando `restante_min` < 3.12
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=100)

- **FILTRO** `lag_apertura_s` > `107.92` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `lag_apertura_s` > 107.92
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=98)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.130 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=56)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7753)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.167 (n=3756)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=11584)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.164 (n=3913)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=11956)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.203 (n=647)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=2029)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.187 (n=673)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=2053)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.208 (n=689)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2167)

- **PATRÓN** `libro_liquidez` > `1789.3696` → IC=+0.122 (n=927)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1789.3696 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.174 (n=655)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=2016)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.174 (n=712)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=2144)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2221)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2310)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3050)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=408)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=399)

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
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=24157)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.275 (n=8604)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=26254)

- **FILTRO** `ibs_7min` < `0.277` → IC=-0.235 (n=8713)

  - _Acción_: SKIP cuando `ibs_7min` < 0.277
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=26145)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=11723)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=23135)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.232 (n=10774)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=33222)

- **FILTRO** `ibs_7min` > `0.2922` → IC=-0.179 (n=10996)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2922
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=33000)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=1746)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=4069)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=1383)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4432)

- **FILTRO** `ibs_7min` < `0.7104` → IC=-0.253 (n=1918)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7104
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3897)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.177 (n=1445)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=4370)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.259 (n=1872)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=5690)

- **FILTRO** `drift_7min_pct` |x|> `0.1364` → IC=-0.130 (n=1890)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1364
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=5672)

- **FILTRO** `ibs_7min` > `0.7881` → IC=-0.208 (n=1890)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7881
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=5672)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.139 (n=1404)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=4605)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1459)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4550)

- **FILTRO** `ibs_7min` < `0.7468` → IC=-0.194 (n=1501)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=4508)

- **FILTRO** `ballena_activa_n` > `158.0` → IC=-0.177 (n=1495)

  - _Acción_: SKIP cuando `ballena_activa_n` > 158.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=4514)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=1411)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4689)

- **FILTRO** `ibs_7min` > `0.262` → IC=-0.185 (n=1524)

  - _Acción_: SKIP cuando `ibs_7min` > 0.262
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4576)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.181 (n=1515)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=4585)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.169 (n=1347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=4181)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.303 (n=1380)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=4148)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.244 (n=1814)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3714)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.223 (n=1209)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4319)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.243 (n=1871)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=6236)

- **FILTRO** `ibs_7min` > `0.75` → IC=-0.174 (n=2022)

  - _Acción_: SKIP cuando `ibs_7min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6085)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=1843)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=3901)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.241 (n=1412)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4332)

- **FILTRO** `ibs_7min` < `0.7409` → IC=-0.184 (n=1436)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7409
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4308)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.174 (n=1406)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=4338)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.257 (n=1470)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=4423)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.179 (n=1473)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4420)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.183 (n=1471)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4422)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.265 (n=1399)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4619)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.236 (n=1485)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=4533)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.180 (n=1980)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=6406)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.255 (n=1890)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=3854)

- **FILTRO** `ibs_7min` < `0.2971` → IC=-0.226 (n=1436)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2971
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4308)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1376)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4368)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.207 (n=1862)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=6086)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=1134)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=563)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=327)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=570)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.132 (n=795)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `464.449` → IC=+0.148 (n=265)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 464.449 (IC base=+0.116)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4374` → IC=+0.135 (n=61)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.4374 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.202 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `451.687` → IC=+0.136 (n=160)

  - _Acción_: Kelly boost +0.68€ cuando `total_vol_5m` < 451.687 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.151 (n=81)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 15.0 (IC base=+0.134)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.162 (n=69)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 11.0 (IC base=+0.105)

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
- **FILTRO** `sigma_h` > `0.0083` → IC=-0.200 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=39)

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
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=197)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=308)

- **FILTRO** `streak_estiramiento` > `0.8566` → IC=-0.162 (n=66)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8566
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=201)

- **PATRÓN** `streak_estiramiento` < `0.4763` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `streak_estiramiento` < 0.4763 (IC base=+0.028)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=426)

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
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=648)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1196)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=806)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=777)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3060)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1552)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1560)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.195 (n=592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0043 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.224 (n=592)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.202 (n=782)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2173` → IC=+0.191 (n=591)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2173 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1283` → IC=+0.234 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1283 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.199 (n=1662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=1856)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.6087` → IC=+0.269 (n=1774)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6087 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1185` → IC=+0.182 (n=895)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1185 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.6071` → IC=+0.181 (n=1683)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.6071 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.837` → IC=+0.274 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.837 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `8803.312` → IC=+0.197 (n=592)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 8803.312 (IC base=+0.188)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=709)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.222 (n=394)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.0602` → IC=+0.298 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0602 (IC base=+0.211)

- **PATRÓN** `drift_15min` |x|≤ `0.3839` → IC=+0.216 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3839 (IC base=+0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.255` → IC=+0.252 (n=131)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.255 (IC base=+0.211)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1084` → IC=+0.287 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1084 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.244 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_15` > `0.7077` → IC=+0.277 (n=393)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7077 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.267 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.55` → IC=+0.272 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.55 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `16060.5409` → IC=+0.237 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16060.5409 (IC base=+0.211)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `24.23` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 24.23
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=430)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6559` → IC=-0.123 (n=181)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6559
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=370)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.171 (n=138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0035 (IC base=+0.131)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.133 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.005 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.158 (n=182)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2346` → IC=+0.171 (n=138)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.2346 (IC base=+0.131)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1229` → IC=+0.167 (n=151)

  - _Acción_: Kelly boost +0.83€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1229 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.6559` → IC=+0.255 (n=370)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6559 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1109` → IC=+0.152 (n=294)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1109 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.257` → IC=+0.219 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.257 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `9475.4181` → IC=+0.147 (n=188)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 9475.4181 (IC base=+0.131)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.278 (n=70)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.1511` → IC=+0.199 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1511 (IC base=+0.171)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0767` → IC=+0.182 (n=187)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio_macro` |x|> 0.0767 (IC base=+0.171)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2673` → IC=+0.222 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2673 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.171)

- **PATRÓN** `ibs_15` > `0.6111` → IC=+0.258 (n=209)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6111 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.178 (n=119)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.172 (n=202)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.367` → IC=+0.394 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.367 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `3071.8702` → IC=+0.263 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3071.8702 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.215 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.171)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.68` → IC=-0.154 (n=105)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=1095)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.784` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.784 (IC base=-0.003)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0234` → IC=+0.271 (n=155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0234 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.223 (n=204)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.195)

- **PATRÓN** `delta_ratio_macro` |x|> `0.099` → IC=+0.201 (n=309)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.099 (IC base=+0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0898` → IC=+0.260 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0898 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.195)

- **PATRÓN** `ibs_15` > `0.5695` → IC=+0.285 (n=463)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5695 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.352` → IC=+0.207 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.352 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` < `0.8177` → IC=+0.197 (n=536)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.8177 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.188` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.188 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.797` → IC=+0.196 (n=468)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 10.797 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2911.0954` → IC=+0.283 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2911.0954 (IC base=+0.195)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.153 (n=519)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.76€ cuando `ibs_15` < 0.1176 (IC base=+0.054)

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

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.224 (n=702)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2110)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=975)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1837)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.253 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.6409` → IC=+0.274 (n=670)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6409 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.193 (n=538)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0765` → IC=+0.247 (n=1762)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0765 (IC base=-0.028)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1785` → IC=+0.243 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1785 (IC base=-0.028)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.277 (n=1973)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.6792` → IC=+0.300 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6792 (IC base=-0.028)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.219 (n=422)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=1267)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.226 (n=557)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1132)

- **FILTRO** `sigma_ewma_delta_pct` > `19.521` → IC=-0.256 (n=301)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.521
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1388)

- **FILTRO** `libro_liquidez` < `14486.8794` → IC=-0.207 (n=557)

  - _Acción_: SKIP cuando `libro_liquidez` < 14486.8794
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=1132)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.167 (n=163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0028 (IC base=+0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.286 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.085)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.341 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.085)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.123 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 12.0 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.7497` → IC=+0.333 (n=190)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7497 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.0982` → IC=+0.280 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0982 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` < `0.3564` → IC=+0.279 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3564 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.200)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.163 (n=407)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.151 (n=319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0068 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.172 (n=285)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.004 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.225 (n=140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.150)

- **PATRÓN** `drift_15min` |x|≤ `0.4169` → IC=+0.179 (n=107)

  - _Acción_: Kelly boost +0.89€ cuando `drift_15min` |x|≤ 0.4169 (IC base=+0.150)

- **PATRÓN** `delta_ratio_macro` |x|> `0.09` → IC=+0.152 (n=285)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.09 (IC base=+0.150)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.237 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.202 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.6647` → IC=+0.263 (n=318)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6647 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.184 (n=229)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.422` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 23.422 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.024` → IC=+0.153 (n=272)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 9.024 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=407)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `11052.2058` → IC=+0.180 (n=145)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 11052.2058 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.250 (n=753)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.3574` → IC=+0.241 (n=663)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3574 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `0.4725` → IC=+0.260 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4725 (IC base=+0.236)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2044` → IC=+0.265 (n=342)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2044 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.253 (n=285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.236)

- **PATRÓN** `ibs_15` < `0.2705` → IC=+0.286 (n=662)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2705 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.7509` → IC=+0.327 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7509 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.646` → IC=+0.262 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.646 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.262` → IC=+0.244 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.262 (IC base=+0.236)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_15min` |x|> `0.8849` → IC=-0.273 (n=165)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8849
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=496)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.223 (n=265)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=396)

- **FILTRO** `sigma_ewma_delta_pct` > `18.184` → IC=-0.139 (n=353)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.184
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2845)

- **PATRÓN** `ibs_15` > `0.9` → IC=+0.300 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9 (IC base=-0.176)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0771` → IC=+0.233 (n=301)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0771 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.264 (n=337)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7427` → IC=+0.240 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7427 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1869` → IC=+0.226 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1869 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.259 (n=408)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=410)

- **FILTRO** `sigma_ewma_delta_pct` > `7.048` → IC=-0.204 (n=255)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.048
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=563)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.263 (n=213)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=605)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1397` → IC=+0.298 (n=236)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1397 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1071` → IC=+0.337 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1071 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.3391` → IC=+0.305 (n=521)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3391 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.9013` → IC=+0.340 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9013 (IC base=-0.039)

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
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.302 (n=625)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0567` → IC=+0.333 (n=237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0567 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2402` → IC=+0.307 (n=237)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2402 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.341 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8411` → IC=+0.330 (n=710)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8411 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.4333` → IC=+0.339 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4333 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.347 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.294 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `13022.3239` → IC=+0.299 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13022.3239 (IC base=+0.293)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.295 (n=344)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.289 (n=348)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.003 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.356 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2605` → IC=+0.311 (n=130)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2605 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3906` → IC=+0.313 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3906 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.319 (n=390)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.356 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.365 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `16113.4131` → IC=+0.326 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16113.4131 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.314 (n=321)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.069` → IC=+0.312 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.069 (IC base=+0.297)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.301 (n=214)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.297)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3007` → IC=+0.330 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3007 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.316 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.297)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.342 (n=321)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.2797` → IC=+0.301 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2797 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` < `0.1133` → IC=+0.298 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1133 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.333 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.303 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

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

- **PATRÓN** `T_h` < `111.9965` → IC=+0.299 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9965 (IC base=+0.284)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6087 sube el IC de +0.188 a +0.269 en UPDOWN_GBM#15min (n=1774). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7077 sube el IC de +0.211 a +0.277 en UPDOWN_GBM#BTC#15min (n=393). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6559 sube el IC de +0.131 a +0.255 en UPDOWN_GBM#ETH#15min (n=370). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6111 sube el IC de +0.171 a +0.258 en UPDOWN_GBM#SOL#15min (n=209). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5695 sube el IC de +0.195 a +0.285 en UPDOWN_GBM#XRP#15min (n=463). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.054 a +0.153 en UPDOWN_GBM#XRP#15min (n=519). Ya aplicado como kelly_boost=+0.76€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6409 sube el IC de -0.067 a +0.274 en UPDOWN_GBM_15M_TARDIO (n=670). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.028 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=1973). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7497 sube el IC de +0.085 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=190). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6647 sube el IC de +0.150 a +0.263 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=318). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2705 sube el IC de +0.236 a +0.286 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=662). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9 sube el IC de -0.176 a +0.300 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=18). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.042 a +0.264 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=337). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3391 sube el IC de -0.039 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=521). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8411 sube el IC de +0.293 a +0.330 en UPDOWN_GBM_IBS_ALTO (n=710). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.289 a +0.319 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=390). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.297 a +0.342 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=321). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.349 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=442). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.354 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=245). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.743 sube el IC de +0.342 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=198). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1373 | +0.101 | +201.32€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1373 | +0.101 | +201.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1032 | +0.110 | +173.63€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1032 | +0.110 | +173.63€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 29629 | -0.083 | -3948.00€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1564 | -0.029 | -213.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 28065 | -0.086 | -3734.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3861 | -0.097 | -637.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3861 | -0.097 | -637.61€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1564 | -0.029 | -213.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1564 | -0.029 | -213.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3498 | -0.098 | -803.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3498 | -0.098 | -803.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7645 | -0.016 | -719.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7645 | -0.016 | -719.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7239 | -0.088 | -454.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7239 | -0.088 | -454.14€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5822 | -0.163 | -1119.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5822 | -0.163 | -1119.49€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 20146 | -0.025 | +3897.36€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5223 | +0.001 | +1795.27€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 14923 | -0.034 | +2102.08€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 20146 | -0.025 | +3897.36€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5223 | +0.001 | +1795.27€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 14923 | -0.034 | +2102.08€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 98932 | +0.113 | -4760.02€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 14668 | +0.185 | -421.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 402 | -0.072 | -52.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 77525 | +0.101 | -4072.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6337 | +0.107 | -214.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 12887 | +0.099 | -1035.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 47 | -0.173 | -2.03€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 12825 | +0.101 | -1022.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 19945 | +0.132 | -328.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4605 | +0.203 | -124.51€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 12852 | +0.114 | -155.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2446 | +0.101 | -26.56€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 12927 | +0.091 | -1148.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 54 | -0.107 | -8.00€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 12858 | +0.092 | -1129.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 21017 | +0.124 | -367.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5713 | +0.176 | -66.36€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 12997 | +0.106 | -235.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2295 | +0.100 | -57.25€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 19257 | +0.114 | -1121.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4201 | +0.188 | -228.13€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 305 | -0.031 | +1.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 13155 | +0.091 | -764.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1596 | +0.129 | -130.64€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 12899 | +0.100 | -757.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 48 | -0.040 | +7.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 12838 | +0.101 | -764.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 15703 | +0.193 | -1002.36€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 15703 | +0.193 | -1002.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3721 | +0.168 | -390.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3721 | +0.168 | -390.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1420 | +0.203 | -5.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1420 | +0.203 | -5.32€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3660 | +0.181 | -306.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3660 | +0.181 | -306.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3232 | +0.241 | -102.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3232 | +0.241 | -102.09€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3591 | +0.193 | -211.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3591 | +0.193 | -211.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 741 | +0.429 | -22.27€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 741 | +0.429 | -22.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 288 | +0.438 | -2.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 288 | +0.438 | -2.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 280 | +0.429 | -7.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 280 | +0.429 | -7.49€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 163 | +0.409 | -9.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 163 | +0.409 | -9.53€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 54254 | +0.198 | -4193.47€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 54254 | +0.198 | -4193.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9365 | +0.178 | -1063.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9365 | +0.178 | -1063.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 8681 | +0.224 | -309.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 8681 | +0.224 | -309.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 9366 | +0.174 | -1097.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 9366 | +0.174 | -1097.78€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 8773 | +0.218 | -350.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 8773 | +0.218 | -350.29€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 8969 | +0.204 | -584.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 8969 | +0.204 | -584.10€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9100 | +0.193 | -788.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9100 | +0.193 | -788.20€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 20510 | +0.117 | +167.80€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 20510 | +0.117 | +167.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 10184 | +0.121 | +133.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 10184 | +0.121 | +133.36€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 10326 | +0.114 | +34.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 10326 | +0.114 | +34.44€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1550 | +0.289 | -19.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1550 | +0.289 | -19.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 694 | +0.277 | -19.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 694 | +0.277 | -19.29€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 743 | +0.291 | -2.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 743 | +0.291 | -2.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 113 | +0.344 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 113 | +0.344 | +2.86€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 687 | +0.435 | -5.30€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 687 | +0.435 | -5.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 327 | +0.433 | -4.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 327 | +0.433 | -4.04€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 315 | +0.437 | -1.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 315 | +0.437 | -1.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 45 | +0.394 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 45 | +0.394 | +0.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1176 | +0.069 | -57.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 412 | +0.048 | -41.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 764 | +0.080 | -16.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 62 | +0.109 | +2.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 62 | +0.109 | +2.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 929 | +0.077 | -25.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 165 | +0.063 | -9.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 764 | +0.080 | -16.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 185 | +0.013 | -34.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 185 | +0.013 | -34.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 38406 | +0.098 | -1090.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3153 | +0.090 | +26.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 35253 | +0.099 | -1116.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 21473 | +0.103 | -299.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3153 | +0.090 | +26.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 18320 | +0.105 | -325.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 7335 | +0.109 | -21.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 7335 | +0.109 | -21.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 9598 | +0.081 | -769.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 9598 | +0.081 | -769.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 844 | +0.216 | -102.02€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 844 | +0.216 | -102.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 844 | +0.216 | -102.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 844 | +0.216 | -102.02€ | 2 | 4 |
| ✅ GBM_LATE_15M | 27327 | +0.084 | +13145.57€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 27327 | +0.084 | +13145.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4566 | +0.196 | +3381.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4566 | +0.196 | +3381.71€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 4058 | +0.179 | +2872.27€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4058 | +0.179 | +2872.27€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 4799 | +0.198 | +3580.52€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4799 | +0.198 | +3580.52€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 3957 | +0.024 | +892.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3957 | +0.024 | +892.18€ | 1 | 14 |
| ✅ GBM_LATE_15M#SOL | 3911 | -0.033 | +890.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3911 | -0.033 | +890.48€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6036 | -0.040 | +1528.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6036 | -0.040 | +1528.42€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 29059 | +0.086 | +15240.07€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 29059 | +0.086 | +15240.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5525 | +0.013 | +2894.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5525 | +0.013 | +2894.73€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6066 | +0.015 | +1269.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6066 | +0.015 | +1269.47€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4134 | +0.264 | +4187.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4134 | +0.264 | +4187.99€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4775 | +0.004 | +920.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4775 | +0.004 | +920.50€ | 2 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4696 | +0.029 | +1808.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4696 | +0.029 | +1808.40€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3863 | +0.278 | +4158.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3863 | +0.278 | +4158.97€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 21933 | +0.169 | +16538.03€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 21933 | +0.169 | +16538.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3308 | +0.208 | +2653.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3308 | +0.208 | +2653.51€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3449 | +0.150 | +2526.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3449 | +0.150 | +2526.38€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3460 | +0.209 | +2763.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3460 | +0.209 | +2763.93€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3672 | +0.133 | +2580.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3672 | +0.133 | +2580.96€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4102 | +0.117 | +2877.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4102 | +0.117 | +2877.23€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3942 | +0.205 | +3136.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3942 | +0.205 | +3136.02€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 5648 | +0.135 | +2556.80€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 5648 | +0.135 | +2556.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 211 | +0.110 | +81.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 211 | +0.110 | +81.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1578 | +0.133 | +773.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1578 | +0.133 | +773.54€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1690 | +0.152 | +814.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1690 | +0.152 | +814.50€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1289 | +0.117 | +494.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1289 | +0.117 | +494.93€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 27484 | +0.177 | +20727.58€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 27484 | +0.177 | +20727.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4351 | +0.223 | +3720.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4351 | +0.223 | +3720.86€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4293 | +0.151 | +2847.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4293 | +0.151 | +2847.96€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4549 | +0.225 | +3913.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4549 | +0.225 | +3913.84€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4453 | +0.137 | +3065.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4453 | +0.137 | +3065.48€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4812 | +0.116 | +3150.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4812 | +0.116 | +3150.47€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5026 | +0.209 | +4028.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5026 | +0.209 | +4028.98€ | 0 | 24 |
| ✅ GBM_LATE_5M | 7628 | +0.161 | +4720.81€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 7628 | +0.161 | +4720.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 714 | +0.214 | +579.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 714 | +0.214 | +579.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1830 | +0.151 | +1221.26€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1830 | +0.151 | +1221.26€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2545 | +0.166 | +1571.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2545 | +0.166 | +1571.45€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 739 | +0.142 | +378.77€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 739 | +0.142 | +378.77€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 911 | +0.130 | +405.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 911 | +0.130 | +405.52€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1878 | +0.067 | +729.22€ | 2 | 13 |
| ✅ GBM_LATE_60M#60min | 1878 | +0.067 | +729.22€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 689 | +0.088 | +259.05€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 689 | +0.088 | +259.05€ | 0 | 11 |
| ✅ GBM_LATE_60M#ETH | 618 | +0.071 | +294.63€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 618 | +0.071 | +294.63€ | 2 | 14 |
| ✅ GBM_LATE_60M#SOL | 571 | +0.036 | +175.54€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 571 | +0.036 | +175.54€ | 2 | 9 |
| 🚫 GBM_LATE_60M_FADE | 393 | -0.254 | -19.93€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 393 | -0.254 | -19.93€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 149 | -0.222 | -7.12€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 149 | -0.222 | -7.12€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 130 | -0.258 | -6.98€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 130 | -0.258 | -6.98€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 114 | -0.284 | -5.83€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 114 | -0.284 | -5.83€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 745 | +0.077 | +176.65€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 745 | +0.077 | +176.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 292 | +0.068 | +62.17€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 292 | +0.068 | +62.17€ | 2 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 225 | +0.042 | +14.59€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 225 | +0.042 | +14.59€ | 3 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 228 | +0.122 | +99.89€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 228 | +0.122 | +99.89€ | 2 | 12 |
| ✅ LATE_WINDOW_5MIN | 103 | +0.262 | +87.89€ | 0 | 10 |
| ✅ LATE_WINDOW_5MIN#5min | 103 | +0.262 | +87.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 103 | +0.262 | +87.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 103 | +0.262 | +87.89€ | 0 | 10 |
| ✅ LEADLAG_BTC_XRP_15M | 2149 | +0.106 | +601.81€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2149 | +0.106 | +601.81€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2149 | +0.106 | +601.81€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2149 | +0.106 | +601.81€ | 0 | 2 |
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
| ✅ LIQUIDACIONES_60M | 1144 | -0.044 | -27.33€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1144 | -0.044 | -27.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 324 | -0.046 | -14.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 324 | -0.046 | -14.46€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 385 | -0.027 | -1.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 385 | -0.027 | -1.11€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 435 | -0.056 | -11.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 435 | -0.056 | -11.76€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 2009 | -0.017 | +46.51€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 965 | -0.018 | +15.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1044 | -0.016 | +31.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 49 | +0.010 | +5.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 28 | +0.067 | +6.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 21 | -0.065 | -0.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 478 | +0.019 | +44.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 222 | +0.013 | +12.95€ | 2 | 3 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 256 | +0.023 | +32.02€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 268 | -0.044 | -5.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 132 | -0.052 | -4.84€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 136 | -0.036 | -0.31€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 378 | -0.024 | -3.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 173 | -0.026 | -1.05€ | 2 | 3 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 205 | -0.022 | -2.18€ | 5 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 365 | -0.009 | +16.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 187 | -0.018 | +5.69€ | 3 | 4 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 178 | +0.000 | +11.11€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 471 | -0.041 | -12.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 223 | -0.033 | -4.01€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 248 | -0.048 | -8.62€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M | 14617 | -0.012 | -218.48€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14617 | -0.012 | -218.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3334 | -0.022 | -71.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3334 | -0.022 | -71.66€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 31209 | -0.006 | +1372.01€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 31209 | -0.006 | +1372.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5508 | +0.019 | +676.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5508 | +0.019 | +676.98€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4784 | -0.029 | -60.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4784 | -0.029 | -60.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5582 | +0.015 | +484.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5582 | +0.015 | +484.49€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4567 | -0.053 | -150.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4567 | -0.053 | -150.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5241 | -0.009 | +205.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5241 | -0.009 | +205.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5527 | +0.009 | +216.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5527 | +0.009 | +216.09€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5989 | -0.060 | -150.25€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5989 | -0.060 | -150.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1444 | -0.084 | -40.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1444 | -0.084 | -40.05€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 676 | -0.122 | -29.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 676 | -0.122 | -29.33€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1755 | -0.079 | -36.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1755 | -0.079 | -36.04€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 78854 | -0.073 | +1647.81€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 78854 | -0.073 | +1647.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 13377 | -0.078 | +775.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 13377 | -0.078 | +775.07€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 12109 | -0.095 | -608.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 12109 | -0.095 | -608.05€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 13635 | -0.067 | +701.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 13635 | -0.067 | +701.07€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 11637 | -0.093 | -224.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 11637 | -0.093 | -224.65€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 14404 | -0.048 | +377.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 14404 | -0.048 | +377.48€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 13692 | -0.063 | +626.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 13692 | -0.063 | +626.89€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7748 | -0.027 | -134.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7748 | -0.027 | -134.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1758 | -0.036 | -15.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1758 | -0.036 | -15.94€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2187 | -0.021 | -24.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2187 | -0.021 | -24.51€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1054 | -0.045 | -20.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1054 | -0.045 | -20.80€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 750 | -0.019 | -22.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 750 | -0.019 | -22.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1195 | +0.110 | +412.10€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 1059 | +0.116 | +399.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 241 | +0.134 | +116.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 241 | +0.134 | +116.62€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 203 | +0.105 | +54.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 203 | +0.105 | +54.56€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 218 | +0.104 | +80.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 218 | +0.104 | +80.29€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 183 | +0.132 | +84.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 183 | +0.132 | +84.61€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 214 | +0.102 | +63.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 214 | +0.102 | +63.43€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 588 | -0.052 | -59.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 588 | -0.052 | -59.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 119 | -0.021 | -0.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 119 | -0.021 | -0.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 77 | -0.108 | -17.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 77 | -0.108 | -17.52€ | 0 | 0 |
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
| ✅ STREAK_FADE_15M | 543 | +0.032 | +16.93€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 543 | +0.032 | +16.93€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 259 | +0.033 | +5.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 259 | +0.033 | +5.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 36 | +0.079 | +2.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 36 | +0.079 | +2.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 57 | -0.009 | -1.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 57 | -0.009 | -1.59€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 191 | +0.034 | +10.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 191 | +0.034 | +10.66€ | 2 | 3 |
| ✅ STREAK_FADE_5M | 2828 | -0.022 | -114.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2828 | -0.022 | -114.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 820 | -0.017 | -25.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 820 | -0.017 | -25.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 570 | -0.023 | -23.26€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 570 | -0.023 | -23.26€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1283 | -0.021 | -50.55€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1283 | -0.021 | -50.55€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 75 | -0.058 | -7.51€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 75 | -0.058 | -7.51€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 37 | -0.013 | -3.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 37 | -0.013 | -3.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 8308 | +0.025 | +139.50€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8308 | +0.025 | +139.50€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2263 | +0.026 | +35.10€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2263 | +0.026 | +35.10€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1883 | +0.034 | +53.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1883 | +0.034 | +53.71€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2537 | +0.014 | +9.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2537 | +0.014 | +9.71€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1625 | +0.030 | +40.98€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1625 | +0.030 | +40.98€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7679 | +0.014 | -31.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7679 | +0.014 | -31.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3079 | +0.017 | -4.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3079 | +0.017 | -4.66€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3016 | +0.014 | -14.19€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3016 | +0.014 | -14.19€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1584 | +0.008 | -12.22€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1584 | +0.008 | -12.22€ | 2 | 0 |
| ✅ UPDOWN_GBM | 41906 | +0.034 | +2670.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 11041 | +0.072 | +2083.67€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1499 | +0.004 | +6.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 26681 | +0.024 | +560.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2527 | +0.003 | +22.03€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4339 | +0.074 | +523.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 779 | +0.161 | +336.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3527 | +0.055 | +188.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 7871 | +0.040 | +569.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1399 | +0.087 | +319.99€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 401 | +0.016 | +6.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 4873 | +0.039 | +215.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1138 | +0.003 | +26.85€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 60 | -0.097 | +0.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4901 | +0.042 | +315.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 735 | +0.140 | +261.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4138 | +0.024 | +55.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 9032 | +0.023 | +364.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2786 | +0.049 | +307.33€ | 1 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 393 | +0.006 | +7.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 4952 | +0.015 | +54.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 849 | -0.001 | -7.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 52 | -0.130 | +3.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 9640 | +0.015 | +245.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2656 | +0.027 | +184.39€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 385 | -0.004 | -2.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6015 | +0.013 | +64.87€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 540 | +0.007 | +2.54€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 44 | -0.174 | -3.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 6121 | +0.039 | +652.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2686 | +0.086 | +674.05€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 259 | -0.002 | -3.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3176 | +0.003 | -18.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 156 | -0.133 | +0.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 589 | +0.349 | +193.44€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 589 | +0.349 | +193.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 326 | +0.354 | +104.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 326 | +0.354 | +104.07€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 263 | +0.342 | +89.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 263 | +0.342 | +89.38€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 12859 | -0.036 | +2821.47€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 12859 | -0.036 | +2821.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 876 | -0.044 | +378.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 876 | -0.044 | +378.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2337 | -0.121 | +22.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2337 | -0.121 | +22.55€ | 4 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 467 | +0.187 | +324.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 467 | +0.187 | +324.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1427 | +0.211 | +877.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1427 | +0.211 | +877.12€ | 1 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3859 | -0.065 | +579.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3859 | -0.065 | +579.78€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3893 | -0.074 | +638.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3893 | -0.074 | +638.72€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 148 | +0.040 | +8.49€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 148 | +0.040 | +8.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 148 | +0.040 | +8.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 148 | +0.040 | +8.49€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 946 | +0.293 | +760.08€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 946 | +0.293 | +760.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 519 | +0.289 | +397.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 519 | +0.289 | +397.47€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 427 | +0.297 | +362.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 427 | +0.297 | +362.61€ | 0 | 10 |
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
| ✅ WEEKLY_PRICE | 2526 | +0.301 | +1260.63€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 876 | +0.252 | +123.78€ | 0 | 5 |
| ✅ WEEKLY_PRICE#ETH | 954 | +0.291 | +411.49€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 696 | +0.377 | +725.36€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.058) — sin ventaja clara. oversold(IBS<0.3): IC=+0.049 n=14807 | neutral: IC=+0.032 n=15612 | overbought(IBS>0.7): IC=+0.090 n=15003
  - _Datos_: n=47043 IC=+0.057 PNL=+5888.51€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 553 celda(s) pasan gate riguroso completo de 2294 evaluadas (n>=40) y 3271 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.027 < 0.08 — monitorear
  - _Datos_: n=2656 IC=+0.027 PNL=+184.39€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=954/15 IC=+0.291 PNL=+411.49€ | BTC: n=876/15 IC=+0.252 PNL=+123.78€ | SOL: n=696/15 IC=+0.377 PNL=+725.36€

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
  - _Estado_: 41844 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.124 n=378/60 | contraria IC=+0.160 n=351 | gap=-0.036 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=312, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 183 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=849/40 IC=-0.001 PNL=-7.36€ | BTC#60min: n=1138/40 IC=+0.003 PNL=+26.85€ | SOL#60min: n=540/40 IC=+0.007 PNL=+2.54€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.051 n=360570 | tras_1loss IC=+0.081 n=278967 | tras_2loss IC=+0.051 n=116813/40 | gap=-0.001 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.016 n=4913 | contrario_BTC IC=+0.029 n=4387/40 | gap=+0.013 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.188 > 0.08 con n=363 PNL=+236.61€
  - _Datos_: n=363 IC=+0.188 PNL=+236.61€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.213 > 0.08 con n=426 PNL=+317.04€
  - _Datos_: n=426 IC=+0.213 PNL=+317.04€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.239 > 0.08 con n=44 PNL=+32.90€
  - _Datos_: n=44 IC=+0.239 PNL=+32.90€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.329 > 0.1 con n=2064 PNL=+1148.56€
  - _Datos_: n=2064 IC=+0.329 PNL=+1148.56€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=328 IC=+0.064 PNL=+33.41€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=328 IC=+0.064 PNL=+33.41€

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
  - _Estado_: n=40051 IC=+0.034 PNL=+2542.25€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=40051 IC=+0.034 PNL=+2542.25€

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
  - _Estado_: n=1764 IC=+0.009 PNL=+5.57€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1764 IC=+0.009 PNL=+5.57€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=763 IC=-0.012 PNL=+16.47€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=763 IC=-0.012 PNL=+16.47€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=549 IC=+0.025 PNL=+29.38€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=549 IC=+0.025 PNL=+29.38€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.188 > 0.1 con n=2365 PNL=+1499.83€
  - _Datos_: n=2365 IC=+0.188 PNL=+1499.83€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1337 IC=+0.055 PNL=+101.19€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1337 IC=+0.055 PNL=+101.19€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1399 IC=+0.087 PNL=+319.99€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1399 IC=+0.087 PNL=+319.99€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.085 > 0.08 con n=6288 PNL=+1520.67€
  - _Datos_: n=6288 IC=+0.085 PNL=+1520.67€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=159 IC=-0.239 PNL=-4.51€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=159 IC=-0.239 PNL=-4.51€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=275 IC=-0.042 PNL=-5.50€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=275 IC=-0.042 PNL=-5.50€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=587 IC=+0.021 PNL=+42.06€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=587 IC=+0.021 PNL=+42.06€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=59 IC=+0.074 PNL=+5.01€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=59 IC=+0.074 PNL=+5.01€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=6109 IC=-0.001 PNL=+0.42€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6109 IC=-0.001 PNL=+0.42€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.262 n=103) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=103 IC=+0.262 PNL=+87.89€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=7827 IC=+0.039 PNL=+519.25€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=7827 IC=+0.039 PNL=+519.25€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=2579 IC=+0.058 PNL=+317.85€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2579 IC=+0.058 PNL=+317.85€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.109 > 0.08 con n=382 PNL=+114.20€
  - _Datos_: n=382 IC=+0.109 PNL=+114.20€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.150 > 0.08 con n=656 PNL=+167.82€
  - _Datos_: n=656 IC=+0.150 PNL=+167.82€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.08 con n=495 PNL=+234.52€
  - _Datos_: n=495 IC=+0.116 PNL=+234.52€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=53215 IC=+0.116 PNL=+19156.04€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=53215 IC=+0.116 PNL=+19156.04€

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
  - _Estado_: n=6224 IC=+0.041 PNL=+471.86€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6224 IC=+0.041 PNL=+471.86€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.02 con n=678 PNL=+259.17€
  - _Datos_: n=678 IC=+0.121 PNL=+259.17€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.447 > 0.1 con n=1195 PNL=+1185.53€
  - _Datos_: n=1195 IC=+0.447 PNL=+1185.53€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=15073 IC=+0.056 PNL=+1828.56€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=15073 IC=+0.056 PNL=+1828.56€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.1 con n=3838 PNL=+2098.12€
  - _Datos_: n=3838 IC=+0.203 PNL=+2098.12€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.147 < -0.1 con n=250 PNL=+25.42€
  - _Datos_: n=250 IC=-0.147 PNL=+25.42€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2069 IC=+0.054 PNL=+224.35€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2069 IC=+0.054 PNL=+224.35€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=86 IC=-0.136 PNL=+1.62€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=86 IC=-0.136 PNL=+1.62€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.129 > 0.1 con n=456 PNL=+138.56€
  - _Datos_: n=456 IC=+0.129 PNL=+138.56€

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
  - _Estado_: n=19382 IC=-0.138 PNL=+1209.58€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=19382 IC=-0.138 PNL=+1209.58€

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
  - _Estado_: n=2058 IC=+0.138 PNL=+1144.74€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2058 IC=+0.138 PNL=+1144.74€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.08 con n=2326 PNL=+1487.20€
  - _Datos_: n=2326 IC=+0.189 PNL=+1487.20€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=4411 IC=+0.024 PNL=+160.09€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4411 IC=+0.024 PNL=+160.09€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=2216 PNL=+1164.12€
  - _Datos_: n=2216 IC=+0.086 PNL=+1164.12€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.08 con n=523 PNL=+271.49€
  - _Datos_: n=523 IC=+0.210 PNL=+271.49€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.239 < -0.1 con n=1904 PNL=-229.96€
  - _Datos_: n=1904 IC=-0.239 PNL=-229.96€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=5708 IC=+0.172 PNL=+3847.26€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=5708 IC=+0.172 PNL=+3847.26€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.08 con n=79 PNL=+29.34€
  - _Datos_: n=79 IC=+0.105 PNL=+29.34€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2102 IC=+0.066 PNL=+619.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2102 IC=+0.066 PNL=+619.13€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.182 > 0.08 con n=1914 PNL=+1368.31€
  - _Datos_: n=1914 IC=+0.182 PNL=+1368.31€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3171 IC=-0.032 PNL=+818.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3171 IC=-0.032 PNL=+818.13€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.085 > 0.08 con n=574 PNL=-55.61€
  - _Datos_: n=574 IC=+0.085 PNL=-55.61€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.237 > 0.08 con n=3450 PNL=-306.26€
  - _Datos_: n=3450 IC=+0.237 PNL=-306.26€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=40 IC=+0.000 PNL=+5.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=40 IC=+0.000 PNL=+5.94€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.104 n=1088) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1088 IC=+0.104 PNL=+266.93€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.347 > 0.08 con n=285 PNL=+105.72€
  - _Datos_: n=285 IC=+0.347 PNL=+105.72€

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
  - _Estado_: n=9365 IC=+0.178 PNL=-1063.97€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=9365 IC=+0.178 PNL=-1063.97€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.198 > 0.1 con n=147 PNL=+87.05€
  - _Datos_: n=147 IC=+0.198 PNL=+87.05€
