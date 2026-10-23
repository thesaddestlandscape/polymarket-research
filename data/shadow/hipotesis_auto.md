# Hipótesis automáticas — 2026-10-23 16:12 UTC
_Generado por shadow_postmortem.py sobre 1024315 resoluciones (PNL=+134345.42€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.255 (n=194)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=630)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.230 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.134)

- **PATRÓN** `n_total_lado` > `55.0` → IC=+0.176 (n=393)

  - _Acción_: Kelly boost +0.88€ cuando `n_total_lado` > 55.0 (IC base=+0.134)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.265 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.134)

- **PATRÓN** `banda_z` > `9.03` → IC=+0.210 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.03 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.135 (n=420)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 8.0 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=944)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.134)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.226 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.202 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.616` → IC=+0.256 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.616 (IC base=+0.139)

- **PATRÓN** `banda_z` > `9.464` → IC=+0.200 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.464 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=845)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `9753.7972` → IC=+0.135 (n=206)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 9753.7972 (IC base=+0.017)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.355` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=109)

- **FILTRO** `banda_hit_calibrado` < `0.8028` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8028
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=97)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=117)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=108)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=107)

- **PATRÓN** `py_entrada` > `0.355` → IC=+0.239 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.355 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.8028` → IC=+0.258 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8028 (IC base=+0.130)

- **PATRÓN** `banda_z` > `7.17` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 7.17 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.135 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 4.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.140 (n=98)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 14.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=117)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `911.0736` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 911.0736 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.130)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `30.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 30.0 (IC base=+0.149)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.149)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.149)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.719` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `ballenas_wallet_edge_medio` > 0.719 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `2466.3517` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2466.3517 (IC base=+0.149)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `141.8` → IC=-0.199 (n=10352)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.8
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=31058)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.62` → IC=-0.256 (n=1136)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.62
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3408)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.61` → IC=-0.288 (n=1113)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.61
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3342)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.58` → IC=-0.201 (n=2750)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.58
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8252)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.39` → IC=-0.276 (n=1997)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.39
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=5994)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.214 (n=22458)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=4425)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `8982.0569` → IC=+0.171 (n=2019)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 8982.0569 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=19116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.130 (n=34531)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=17947)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=7349)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7018.3548` → IC=+0.156 (n=2838)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 7018.3548 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=2058)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.191 (n=2519)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `16441.1339` → IC=+0.195 (n=654)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 16441.1339 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.188 (n=1806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 7.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=2014)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.285` → IC=+0.317 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.285 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=2581)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `16209.2525` → IC=+0.187 (n=665)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16209.2525 (IC base=+0.182)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.174 (n=482)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.61 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `6765.2427` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 6765.2427 (IC base=+0.081)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.138 (n=1160)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.081)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.162 (n=3708)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.371 (n=1445)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.217 (n=1945)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.349 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=2267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=1100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=939)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.265 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=862)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `2210.9325` → IC=+0.157 (n=476)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2210.9325 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=1007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=1307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=688)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=866)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.164 (n=141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.114)

- **PATRÓN** `py_entrada` > `0.56` → IC=+0.191 (n=383)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.56 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=212)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=1137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.245 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=149)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.293 (n=138)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=73)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=19075)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=16220)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.236 (n=7820)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=4386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=3692)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.184 (n=4307)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.73 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=3583)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.223 (n=2302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=1538)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.301 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.221)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=4315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=3678)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.181 (n=4495)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=3374)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=3731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.361 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.248)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.248)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=4225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=3620)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=3122)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.432 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4242.4895` → IC=+0.438 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4242.4895 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.444 (n=211)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `20878.8113` → IC=+0.444 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 20878.8113 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.436 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `3610.6662` → IC=+0.443 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3610.6662 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.404 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.400)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.402 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.400)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.428 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.400)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `12.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=25)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=27)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=24687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=24941)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=4256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.187 (n=7927)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=11140)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=5155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.227 (n=3945)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=3601)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.189 (n=4229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.213 (n=5640)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=5198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=3972)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.275 (n=3510)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=9499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=3673)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=4099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=4143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=4315)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=9010)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=8923)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.72` → IC=+0.137 (n=10827)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.72 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=4456)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=4079)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=5421)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.69` → IC=+0.144 (n=4078)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.69 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=4554)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=4844)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.31` → IC=+0.135 (n=5440)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.31 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.311 (n=1151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.383 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.291 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.356 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `5061.412` → IC=+0.287 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5061.412 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.323 (n=553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=812)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.300 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.349 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.347)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.372 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.347)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.383 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.347)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.351 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.347)

- **PATRÓN** `libro_liquidez` > `763.8012` → IC=+0.369 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 763.8012 (IC base=+0.347)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.444 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.444 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.443)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.438 (n=256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.440 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `5384.9318` → IC=+0.443 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5384.9318 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.469 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.450)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.453 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.450)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.453 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.450)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.452 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.450)

- **PATRÓN** `libro_liquidez` > `1990.0457` → IC=+0.469 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1990.0457 (IC base=+0.450)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.389 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.398)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.393 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.398)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.398)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.283 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=60)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.302 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.255)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.379 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.272 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `987.2299` → IC=+0.270 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 987.2299 (IC base=+0.255)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.283 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=60)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.302 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.255)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.379 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.272 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `987.2299` → IC=+0.270 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 987.2299 (IC base=+0.255)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.3654` → IC=+0.143 (n=12257)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3654 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=14080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=9742)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.3778` → IC=+0.166 (n=13931)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3778 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.8005` → IC=+0.274 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8005 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.653` → IC=+0.183 (n=6931)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.653 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6188` → IC=+0.266 (n=4060)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6188 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3031` → IC=+0.242 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3031 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.3504` → IC=+0.230 (n=4501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3504 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=11551)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `5042.0614` → IC=+0.147 (n=4642)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 5042.0614 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6842` → IC=+0.129 (n=19520)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6842 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.618` → IC=+0.187 (n=1141)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.618 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.6964` → IC=+0.189 (n=2967)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6964 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.0523` → IC=+0.181 (n=3058)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0523 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.231 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `2.6846` → IC=+0.207 (n=3820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6846 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.222 (n=11324)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.076)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.206 (n=1010)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.3473` → IC=+0.207 (n=3026)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3473 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=1466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.208 (n=2030)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.9831` → IC=+0.281 (n=1373)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9831 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.803` → IC=+0.285 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.803 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2349` → IC=+0.253 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2349 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4413` → IC=+0.205 (n=2888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4413 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=3271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2068.09` → IC=+0.209 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2068.09 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.220 (n=1782)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.241 (n=2539)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.240 (n=1155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.274 (n=850)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.255 (n=927)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5366` → IC=+0.256 (n=2539)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5366 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0949` → IC=+0.241 (n=2277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0949 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.259 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.242 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6907` → IC=+0.243 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6907 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=2876)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1598.2759` → IC=+0.245 (n=2268)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1598.2759 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.238 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.240 (n=1095)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.234 (n=1130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1059` → IC=+0.259 (n=1094)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1059 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=2607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.9462` → IC=+0.277 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9462 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.1316` → IC=+0.235 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1316 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.321` → IC=+0.269 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.321 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` < `1.231` → IC=+0.229 (n=2487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.231 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6224` → IC=+0.234 (n=2488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6224 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.274 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.4423` → IC=+0.258 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4423 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.151 (n=2567)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0058 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.168 (n=857)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.725` → IC=+0.175 (n=2565)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.725 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1371` → IC=+0.152 (n=2406)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1371 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.071` → IC=+0.148 (n=418)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 11.071 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.171` → IC=+0.142 (n=2337)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.171 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.2042` → IC=+0.142 (n=2565)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2042 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.162 (n=700)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4531` → IC=+0.143 (n=2444)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4531 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.7907` → IC=+0.135 (n=1629)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.7907 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.174 (n=1048)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 214.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.222 (n=1052)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=3306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=2828)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.184` → IC=+0.271 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.184 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.201 (n=2793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3513` → IC=+0.212 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3513 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.703` → IC=+0.211 (n=1387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.703 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=3784)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1958.5384` → IC=+0.202 (n=1428)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1958.5384 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.221 (n=2837)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1774` → IC=+0.233 (n=1248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1774 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1062)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.217 (n=997)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.025` → IC=+0.274 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.025 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.306` → IC=+0.259 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.306 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.258 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7347` → IC=+0.227 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7347 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1942.5784` → IC=+0.221 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1942.5784 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.221 (n=2347)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.146 (n=156)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=3811)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.164 (n=557)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0037 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.9529` → IC=+0.232 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9529 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.1404` → IC=+0.335 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1404 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.1962` → IC=+0.329 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1962 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.146` → IC=+0.194 (n=1205)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 5.146 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.8627` → IC=+0.336 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8627 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` > `1.236` → IC=+0.350 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.236 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` < `0.1677` → IC=+0.332 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1677 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.3004` → IC=+0.343 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3004 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.356 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4124 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.335 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 130.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.093` → IC=+0.180 (n=993)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.093 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` > `0.7534` → IC=+0.153 (n=226)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.7534 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` < `0.8408` → IC=+0.151 (n=1187)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8408 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` > `1.1689` → IC=+0.138 (n=594)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.1689 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2843` → IC=+0.201 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2843 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.7781` → IC=+0.141 (n=1139)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.7781 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `2.1569` → IC=+0.155 (n=774)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1569 (IC base=+0.038)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.176 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=578)

- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.182 (n=171)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=513)

- **FILTRO** `ibs_20min` > `0.2162` → IC=-0.132 (n=3730)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2162
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=1840)

- **FILTRO** `sigma_ewma_delta_pct` > `8.632` → IC=-0.233 (n=585)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.632
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=4985)

- **PATRÓN** `ibs_20min` > `0.7812` → IC=+0.185 (n=233)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.7812 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.0156` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0156 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.4916` → IC=+0.267 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4916 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.383` → IC=+0.141 (n=240)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 2.383 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `1.0233` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0233 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1597` → IC=+0.280 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1597 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.5444` → IC=+0.292 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5444 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.272 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.270 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.2162` → IC=+0.147 (n=1840)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.2162 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.1911` → IC=+0.281 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1911 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.302 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.1048` → IC=+0.287 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1048 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.295 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.4341` → IC=+0.302 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4341 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6085` → IC=-0.183 (n=1027)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6085
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3084)

- **FILTRO** `ibs_20min` < `0.7576` → IC=-0.152 (n=2713)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7576
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=1398)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.163 (n=996)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3115)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.204 (n=1469)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=4435)

- **PATRÓN** `dist_vwap_pct` > `1.1371` → IC=+0.344 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1371 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2555` → IC=+0.305 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2555 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` < `1.1484` → IC=+0.300 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1484 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` > `0.702` → IC=+0.319 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.702 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.305 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.303 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.4138` → IC=+0.322 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4138 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.8402` → IC=+0.310 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8402 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.8181` → IC=+0.285 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8181 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.263 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` > `1.0687` → IC=+0.285 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0687 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.287 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.1859` → IC=+0.262 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1859 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `1.4309` → IC=+0.266 (n=1512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4309 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.210 (n=6105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.3158` → IC=+0.168 (n=18275)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3158 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.9628` → IC=+0.302 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9628 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.587` → IC=+0.163 (n=8190)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.587 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `1.1722` → IC=+0.265 (n=6740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1722 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` > `0.6893` → IC=+0.271 (n=6021)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6893 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` < `0.0792` → IC=+0.264 (n=9856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0792 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.278 (n=2016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `1.4598` → IC=+0.264 (n=3580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4598 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` > `2.6512` → IC=+0.273 (n=3578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6512 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.297 (n=10330)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.095)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.155 (n=5871)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0094 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.6558` → IC=+0.144 (n=17611)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6558 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.265 (n=2460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1967` → IC=+0.266 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1967 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.315 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5782` → IC=+0.291 (n=3547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5782 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.6252` → IC=+0.285 (n=2687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6252 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.295 (n=7985)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5801` → IC=-0.136 (n=2499)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5801
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=2501)

- **FILTRO** `ibs_20min` > `0.7363` → IC=-0.217 (n=1062)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7363
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=3189)

- **FILTRO** `sigma_ewma_delta_pct` > `4.345` → IC=-0.213 (n=926)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.345
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=3325)

- **PATRÓN** `ibs_20min` > `0.9222` → IC=+0.320 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9222 (IC base=+0.029)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.957` → IC=+0.219 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.957 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.304 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4428` → IC=+0.255 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4428 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.2589` → IC=+0.282 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2589 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.287 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.029)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.160 (n=1064)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1667 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.0738` → IC=+0.414 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0738 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.6476` → IC=+0.404 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6476 (IC base=-0.030)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.402 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.030)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1166` → IC=+0.216 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1166 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1952` → IC=+0.196 (n=1789)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 1.1952 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6856` → IC=+0.204 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6856 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.0752` → IC=+0.195 (n=1641)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0752 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.238 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.425` → IC=+0.219 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.425 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.4911` → IC=+0.197 (n=588)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.4911 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `271.0` → IC=+0.232 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 271.0 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1716` → IC=+0.231 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1716 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` > `0.6206` → IC=+0.235 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6206 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.272` → IC=+0.296 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.272 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.5351` → IC=+0.241 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5351 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1623` → IC=+0.253 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1623 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `199.0` → IC=+0.243 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 199.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.314 (n=884)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.278 (n=2779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.310 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.681` → IC=+0.302 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.681 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` < `0.1318` → IC=+0.281 (n=2441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1318 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.274 (n=2560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.280 (n=3158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `2044.9328` → IC=+0.289 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2044.9328 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.289 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.269)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.325 (n=1052)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.311 (n=1018)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=878)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.293 (n=808)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` < `0.3719` → IC=+0.295 (n=2313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3719 (IC base=+0.292)

- **PATRÓN** `ibs_20min` > `0.2647` → IC=+0.299 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2647 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.461` → IC=+0.306 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.461 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` < `0.1967` → IC=+0.292 (n=2263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1967 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` > `0.3406` → IC=+0.303 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3406 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` < `1.7255` → IC=+0.299 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7255 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `2.6617` → IC=+0.303 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6617 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.295 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1940.5956` → IC=+0.306 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1940.5956 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.294 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.292)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.736` → IC=-0.186 (n=1112)

  - _Acción_: SKIP cuando `ibs_20min` > 0.736
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=3337)

- **PATRÓN** `ibs_20min` > `0.8742` → IC=+0.167 (n=1065)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8742 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.1555` → IC=+0.233 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1555 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.2178` → IC=+0.230 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2178 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.0083` → IC=+0.239 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0083 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.667` → IC=+0.231 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.667 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.164` → IC=+0.236 (n=1595)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.164 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.242 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.4616` → IC=+0.238 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4616 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.254 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 122.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1979` → IC=+0.236 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1979 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `1.0289` → IC=+0.244 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0289 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.1012` → IC=+0.251 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1012 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.291 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.794` → IC=+0.277 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.794 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.4337` → IC=+0.253 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4337 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.262 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 124.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7576` → IC=-0.218 (n=1920)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7576
  - _Potencial_: sin este filtro IC_bueno=+0.308 (n=1927)

- **FILTRO** `ibs_20min` > `0.6442` → IC=-0.233 (n=934)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6442
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=2804)

- **FILTRO** `sigma_ewma_delta_pct` > `8.468` → IC=-0.244 (n=432)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.468
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=3306)

- **PATRÓN** `ibs_20min` > `0.7576` → IC=+0.308 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7576 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.2146` → IC=+0.339 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2146 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.444` → IC=+0.186 (n=600)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.444 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.8488` → IC=+0.335 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8488 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` > `0.7021` → IC=+0.329 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7021 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` < `0.1585` → IC=+0.326 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1585 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.350 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.4408` → IC=+0.350 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4408 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.343 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.045)

- **PATRÓN** `ibs_20min` < `0.6442` → IC=+0.121 (n=2804)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.6442 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.7047` → IC=+0.264 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7047 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1018` → IC=+0.243 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1018 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0777` → IC=+0.251 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0777 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.4318` → IC=+0.248 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4318 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.267 (n=1238)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.032)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.350 (n=1793)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.306)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.310 (n=777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.306)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.316 (n=954)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.306)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.338 (n=2009)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.306)

- **PATRÓN** `dist_vwap_pct` > `0.2098` → IC=+0.332 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2098 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.82` → IC=+0.325 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.82 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.072` → IC=+0.308 (n=2284)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.072 (IC base=+0.306)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.315 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.345 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.306)

- **PATRÓN** `volumen_spike_ratio` > `1.8021` → IC=+0.323 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8021 (IC base=+0.306)

- **PATRÓN** `libro_liquidez` > `2964.5226` → IC=+0.311 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2964.5226 (IC base=+0.306)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.340 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.306)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.338 (n=1418)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.317 (n=822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.307 (n=1042)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` < `0.37` → IC=+0.330 (n=2128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.37 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.618` → IC=+0.319 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.618 (IC base=+0.307)

- **PATRÓN** `volumen_regimen` < `0.7188` → IC=+0.313 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7188 (IC base=+0.307)

- **PATRÓN** `volumen_regimen` > `1.2242` → IC=+0.337 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2242 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.2841` → IC=+0.357 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2841 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` < `1.4152` → IC=+0.318 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4152 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.1376` → IC=+0.309 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1376 (IC base=+0.307)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.220 (n=6129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0868` → IC=+0.203 (n=4501)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0868 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=14019)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.5571` → IC=+0.235 (n=13503)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5571 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1652` → IC=+0.209 (n=5433)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1652 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.326` → IC=+0.257 (n=3540)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.326 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.189` → IC=+0.167 (n=8959)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.189 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.164 (n=8959)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6237 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.205 (n=1966)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6089` → IC=+0.192 (n=4368)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6089 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1961.64` → IC=+0.181 (n=12063)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1961.64 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.198 (n=12422)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 93.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.185 (n=11437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0092 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.227 (n=4330)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=4822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5052` → IC=+0.237 (n=12990)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5052 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.965` → IC=+0.197 (n=2118)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.965 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.668` → IC=+0.183 (n=11486)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 2.668 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1832` → IC=+0.164 (n=9266)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1832 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.225 (n=1936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6402` → IC=+0.187 (n=4076)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6402 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.193 (n=11964)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 99.0 (IC base=+0.181)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.234 (n=757)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.3321` → IC=+0.234 (n=2263)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3321 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.225 (n=1531)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9291` → IC=+0.294 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9291 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.71` → IC=+0.312 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.71 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.279 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.218 (n=2146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2471)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.227 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.253 (n=1754)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.261 (n=797)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.0656` → IC=+0.309 (n=584)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0656 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=1800)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.252 (n=841)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` < `0.3084` → IC=+0.275 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3084 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.254 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.285 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.4369` → IC=+0.273 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4369 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.7247` → IC=+0.255 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7247 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=1987)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `1461.94` → IC=+0.258 (n=1752)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1461.94 (IC base=+0.250)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.251 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.250)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.218 (n=682)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0647` → IC=+0.194 (n=680)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0647 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=2144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.3301` → IC=+0.223 (n=2037)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3301 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.1368` → IC=+0.214 (n=1212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1368 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.252` → IC=+0.221 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.252 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6924` → IC=+0.163 (n=897)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6924 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `1.0648` → IC=+0.153 (n=924)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.0648 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.193 (n=324)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.4139` → IC=+0.175 (n=666)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4139 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.4971` → IC=+0.169 (n=666)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.4971 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `418.0` → IC=+0.156 (n=1962)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 418.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.173 (n=2132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0059 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2348` → IC=+0.173 (n=1876)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2348 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.189 (n=1011)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6182` → IC=+0.208 (n=2132)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6182 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.49` → IC=+0.192 (n=404)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.49 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.202` → IC=+0.148 (n=1848)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.202 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.162 (n=2132)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.204 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.07` → IC=+0.150 (n=1732)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.07 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4919` → IC=+0.154 (n=2012)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4919 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `225.0` → IC=+0.180 (n=854)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 225.0 (IC base=+0.147)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.240 (n=761)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.3954` → IC=+0.223 (n=2008)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3954 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.342` → IC=+0.302 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.342 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0991` → IC=+0.214 (n=1962)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0991 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3513` → IC=+0.230 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3513 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7659` → IC=+0.214 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7659 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7088` → IC=+0.226 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7088 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.219 (n=2737)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1946.335` → IC=+0.224 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1946.335 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.241 (n=1975)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.2467` → IC=+0.264 (n=1316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2467 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0141` → IC=+0.300 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0141 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.409` → IC=+0.274 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.409 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3584` → IC=+0.281 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3584 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7477` → IC=+0.236 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7477 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.154` → IC=+0.238 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.154 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1933.8384` → IC=+0.241 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.8384 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.233 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.202 (n=971)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0769` → IC=+0.201 (n=733)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0769 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=2279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.304` → IC=+0.210 (n=2197)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.304 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1453` → IC=+0.197 (n=1329)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1453 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.665` → IC=+0.206 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.665 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.0244` → IC=+0.153 (n=1933)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0244 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `0.6162` → IC=+0.147 (n=2196)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6162 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1032` → IC=+0.172 (n=901)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1032 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.8238` → IC=+0.147 (n=1436)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.8238 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5085` → IC=+0.165 (n=718)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5085 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `7512.304` → IC=+0.188 (n=996)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 7512.304 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.153 (n=2139)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 137.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.156 (n=2310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0073 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3933` → IC=+0.144 (n=2308)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3933 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1092)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6819` → IC=+0.185 (n=2308)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6819 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.788` → IC=+0.151 (n=813)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 6.788 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.157 (n=1539)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8554 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.3001` → IC=+0.194 (n=351)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3001 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.811` → IC=+0.136 (n=1445)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.811 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.5555` → IC=+0.133 (n=722)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.5555 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7204.7935` → IC=+0.191 (n=1047)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7204.7935 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.134 (n=1883)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 115.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.179 (n=1117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0104 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=1168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.4865` → IC=+0.217 (n=2463)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4865 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1958` → IC=+0.192 (n=1422)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1958 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.474` → IC=+0.281 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.474 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.1761` → IC=+0.143 (n=2461)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1761 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.1602` → IC=+0.133 (n=2499)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1602 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4359` → IC=+0.148 (n=797)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4359 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=2575)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2730.6754` → IC=+0.211 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2730.6754 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.155 (n=792)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 19.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.141 (n=2518)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0109 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1082` → IC=+0.175 (n=840)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1082 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=2571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6111` → IC=+0.220 (n=2522)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6111 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.467` → IC=+0.135 (n=2226)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.467 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1789` → IC=+0.130 (n=2518)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1789 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1648` → IC=+0.125 (n=2442)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1648 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.147 (n=341)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.443` → IC=+0.131 (n=784)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.443 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.4306` → IC=+0.137 (n=784)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4306 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2615.4701` → IC=+0.187 (n=1142)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2615.4701 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.128 (n=2039)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 41.0 (IC base=+0.121)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.247 (n=2024)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1721` → IC=+0.242 (n=997)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1721 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2043)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.259 (n=2271)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1851` → IC=+0.229 (n=1456)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1851 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.643` → IC=+0.251 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.643 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.1768` → IC=+0.226 (n=2266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1768 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6198` → IC=+0.232 (n=2265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6198 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2308` → IC=+0.265 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2308 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.230 (n=2206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.8099` → IC=+0.234 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8099 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=2952)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2583.2746` → IC=+0.226 (n=1510)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2583.2746 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.234 (n=1016)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.231)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.242 (n=1047)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.263 (n=770)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.231 (n=1028)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.4279` → IC=+0.258 (n=2309)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4279 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` > `0.2992` → IC=+0.242 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2992 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.304` → IC=+0.265 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.304 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` < `0.87` → IC=+0.233 (n=1540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.87 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` > `0.639` → IC=+0.236 (n=2309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.639 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.286 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `1.4384` → IC=+0.233 (n=2152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4384 (IC base=+0.231)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.206 (n=1521)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.190 (n=1148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.009 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1298` → IC=+0.203 (n=1514)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1298 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.214 (n=1697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4911` → IC=+0.218 (n=3073)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4911 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.7982` → IC=+0.205 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7982 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.605` → IC=+0.213 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.605 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.8628` → IC=+0.204 (n=2066)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8628 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `0.6945` → IC=+0.186 (n=2768)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6945 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0998` → IC=+0.191 (n=1235)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0998 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.4272` → IC=+0.194 (n=1115)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4272 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.4819` → IC=+0.188 (n=1115)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4819 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=3888)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2666.351` → IC=+0.189 (n=3073)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2666.351 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.130 (n=1246)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0039 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.7201` → IC=+0.122 (n=3734)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.7201 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.124 (n=1616)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 27.0 (IC base=+0.085)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.209 (n=418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.0989` → IC=+0.238 (n=418)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0989 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.212 (n=865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.6402` → IC=+0.241 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6402 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.203 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.079` → IC=+0.202 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.079 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `0.8745` → IC=+0.210 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8745 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.0925` → IC=+0.186 (n=911)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.0925 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.187 (n=375)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `2.1959` → IC=+0.195 (n=817)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.1959 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `14694.0598` → IC=+0.188 (n=632)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 14694.0598 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `161.0` → IC=+0.203 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 161.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.132 (n=1136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0057 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.6342` → IC=+0.156 (n=998)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.6342 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.1609` → IC=+0.158 (n=302)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1609 (IC base=+0.106)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.172 (n=486)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 159.0 (IC base=+0.106)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.242 (n=716)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.209 (n=356)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.1257` → IC=+0.225 (n=470)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1257 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=1118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.3792` → IC=+0.251 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3792 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.805` → IC=+0.209 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.805 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.2147` → IC=+0.215 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2147 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.884` → IC=+0.253 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.884 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `0.8344` → IC=+0.217 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8344 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.6042` → IC=+0.210 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6042 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2663` → IC=+0.247 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2663 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.223 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.7736` → IC=+0.218 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7736 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.1077` → IC=+0.161 (n=361)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1077 (IC base=+0.066)

- **PATRÓN** `libro_liquidez` > `5525.052` → IC=+0.128 (n=721)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 5525.052 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.124 (n=458)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 43.0 (IC base=+0.066)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.191 (n=289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0109 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=778)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.989` → IC=+0.275 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.989 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.9658` → IC=+0.247 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9658 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.092` → IC=+0.238 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.092 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8886` → IC=+0.193 (n=577)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8886 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.714` → IC=+0.176 (n=773)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.714 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2307` → IC=+0.193 (n=164)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2307 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4312` → IC=+0.190 (n=279)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4312 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.1499` → IC=+0.172 (n=379)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1499 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.180 (n=892)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `3010.8204` → IC=+0.191 (n=289)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3010.8204 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.131 (n=838)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.5652 (IC base=+0.052)

- **PATRÓN** `libro_liquidez` > `2649.8672` → IC=+0.147 (n=432)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2649.8672 (IC base=+0.052)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0239` → IC=+0.161 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0239 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.203 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2536` → IC=+0.176 (n=146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2536 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 16.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.207 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.176 (n=220)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.4 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.2021` → IC=+0.167 (n=115)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2021 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.738` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 7.738 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.275` → IC=+0.182 (n=187)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.275 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `0.6893` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6893 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.1109` → IC=+0.169 (n=182)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.1109 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.5669` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.5669 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.177 (n=255)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.03 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `2474.2976` → IC=+0.176 (n=146)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2474.2976 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.175 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0228 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.129 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.614` → IC=+0.128 (n=253)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.614 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.1964` → IC=+0.318 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1964 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.225` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.225 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.9016` → IC=+0.134 (n=170)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.9016 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.3609` → IC=+0.127 (n=108)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.3609 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.130 (n=233)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 19.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.223 (n=7986)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=18338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.4456` → IC=+0.232 (n=17591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4456 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.9073` → IC=+0.215 (n=2143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9073 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.212` → IC=+0.254 (n=4305)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.212 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.2214` → IC=+0.169 (n=11794)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2214 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2405` → IC=+0.206 (n=3191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2405 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.6143` → IC=+0.197 (n=5708)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6143 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `1953.8` → IC=+0.185 (n=15714)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1953.8 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.210 (n=14276)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.196 (n=7031)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0056 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3772` → IC=+0.193 (n=14059)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3772 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=5915)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5855` → IC=+0.242 (n=15976)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5855 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.787` → IC=+0.205 (n=2225)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.787 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.545` → IC=+0.192 (n=15462)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 3.545 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.6328` → IC=+0.167 (n=3595)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6328 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.251 (n=2174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.6242` → IC=+0.199 (n=5047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6242 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.234 (n=5047)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.228 (n=958)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.347` → IC=+0.231 (n=2866)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.347 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=1387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.231 (n=1933)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.348` → IC=+0.356 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.348 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.291 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.2907` → IC=+0.241 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2907 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=3086)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2067.92` → IC=+0.231 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2067.92 (IC base=+0.228)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.253 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.268 (n=2445)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1192` → IC=+0.286 (n=1077)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1192 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=2246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.5152` → IC=+0.287 (n=2446)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5152 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.073` → IC=+0.265 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.073 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.0956` → IC=+0.264 (n=2195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0956 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.288` → IC=+0.284 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.288 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5582` → IC=+0.265 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5582 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6459` → IC=+0.272 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6459 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2775)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1475.9` → IC=+0.268 (n=2444)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1475.9 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.271 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.199 (n=952)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1041` → IC=+0.165 (n=1256)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1041 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3621` → IC=+0.221 (n=2549)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3621 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1279` → IC=+0.195 (n=1465)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1279 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.472` → IC=+0.163 (n=467)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.472 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.182` → IC=+0.152 (n=2627)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.182 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.6306` → IC=+0.175 (n=951)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6306 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.154 (n=2543)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.272` → IC=+0.184 (n=410)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.272 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1716` → IC=+0.158 (n=2457)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1716 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5284` → IC=+0.155 (n=2494)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5284 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `237.0` → IC=+0.182 (n=911)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 237.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.165 (n=2406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.0777` → IC=+0.182 (n=801)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0777 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=889)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.6942` → IC=+0.195 (n=2402)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6942 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1412` → IC=+0.162 (n=2264)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1412 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.232` → IC=+0.153 (n=399)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.232 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.454` → IC=+0.143 (n=2419)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.454 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.194` → IC=+0.153 (n=2402)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.194 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2185` → IC=+0.200 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2185 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.149 (n=2297)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7816` → IC=+0.152 (n=1531)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7816 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=3118)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `270.0` → IC=+0.156 (n=972)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 270.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.257 (n=978)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3064)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2632)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.252` → IC=+0.321 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.252 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.230 (n=2745)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `3.1763` → IC=+0.245 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1763 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=3513)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1957.842` → IC=+0.238 (n=1329)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1957.842 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.245 (n=2428)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1797` → IC=+0.262 (n=1214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1797 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1034)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.240 (n=975)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0361` → IC=+0.309 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0361 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.537` → IC=+0.300 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.537 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3458` → IC=+0.301 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3458 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1367` → IC=+0.250 (n=1752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1367 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.246 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1938.1775` → IC=+0.252 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1938.1775 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.256 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.197 (n=1336)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0039 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4209` → IC=+0.158 (n=3025)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4209 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=3141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2446` → IC=+0.192 (n=3024)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2446 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1446` → IC=+0.172 (n=1595)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1446 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.12` → IC=+0.161 (n=1230)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.12 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.163 (n=2018)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8641 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.188 (n=399)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5231` → IC=+0.163 (n=1299)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5231 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1755` → IC=+0.155 (n=1338)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1755 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5770.8976` → IC=+0.241 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5770.8976 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.166 (n=1278)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 72.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.154 (n=2520)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0075 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4362` → IC=+0.139 (n=2520)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4362 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=917)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.7346` → IC=+0.186 (n=2520)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7346 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1516` → IC=+0.145 (n=2307)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1516 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.144` → IC=+0.163 (n=384)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.144 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.148` → IC=+0.132 (n=2193)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.148 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6942` → IC=+0.147 (n=1109)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6942 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.218 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.2249` → IC=+0.133 (n=2134)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.2249 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.4282` → IC=+0.137 (n=2425)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4282 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6915.1167` → IC=+0.213 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6915.1167 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.132 (n=1640)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 100.0 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.161 (n=1383)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0104 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=1117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.44` → IC=+0.200 (n=3051)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.44 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.0499` → IC=+0.208 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0499 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.348` → IC=+0.245 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.348 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8838` → IC=+0.146 (n=2033)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8838 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.125 (n=3171)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.129 (n=394)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `2.4804` → IC=+0.126 (n=2978)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.4804 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.1874` → IC=+0.126 (n=1350)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.1874 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=3178)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2765.4937` → IC=+0.245 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2765.4937 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.140 (n=1016)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 24.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.153 (n=2540)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0101 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1348` → IC=+0.156 (n=965)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1348 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=2976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6538` → IC=+0.213 (n=2886)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6538 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.222` → IC=+0.137 (n=2775)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.222 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.144 (n=962)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6417 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2245` → IC=+0.170 (n=495)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2245 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.150 (n=904)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4384 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2648.2907` → IC=+0.203 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2648.2907 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.132 (n=2373)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 46.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.255 (n=2565)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=2997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.238 (n=2076)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.6111` → IC=+0.273 (n=2565)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6111 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.1931` → IC=+0.250 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1931 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.737` → IC=+0.273 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.737 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` < `1.2283` → IC=+0.240 (n=2870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2283 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` > `0.7085` → IC=+0.237 (n=2564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7085 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.256 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `1.5463` → IC=+0.242 (n=2498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5463 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=3731)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2950.9416` → IC=+0.236 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2950.9416 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.254 (n=990)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.240 (n=2798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.5156` → IC=+0.266 (n=2971)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5156 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.222` → IC=+0.270 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.222 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `1.2286` → IC=+0.259 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2286 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.299 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `1.4316` → IC=+0.234 (n=2766)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4316 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.230 (n=2684)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.233)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=5070)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.246 (n=1755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.5079` → IC=+0.220 (n=5253)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5079 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=1894)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9411` → IC=+0.252 (n=1752)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9411 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.7011` → IC=+0.213 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7011 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.2469` → IC=+0.213 (n=3310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2469 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.941` → IC=+0.217 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.941 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.576` → IC=+0.211 (n=4678)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.576 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.7061` → IC=+0.224 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7061 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.1067` → IC=+0.211 (n=4909)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1067 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.1665` → IC=+0.221 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1665 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.4546` → IC=+0.220 (n=1724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4546 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.8464` → IC=+0.211 (n=3447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8464 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=4014)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `3716.6491` → IC=+0.220 (n=3502)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3716.6491 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.240 (n=1274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.4897` → IC=+0.209 (n=3815)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4897 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.210 (n=1697)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.1857` → IC=+0.207 (n=1679)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1857 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6743` → IC=+0.201 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6743 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.806` → IC=+0.203 (n=3430)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.806 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.095` → IC=+0.202 (n=3186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.095 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.197 (n=3502)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.196 (n=768)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5334` → IC=+0.198 (n=1653)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5334 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.1921` → IC=+0.202 (n=1704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1921 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=5070)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.209 (n=1650)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.193)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.274 (n=675)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.295 (n=256)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.271 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.260 (n=769)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.2568` → IC=+0.288 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2568 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.051` → IC=+0.275 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.051 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` < `1.2148` → IC=+0.267 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2148 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` > `0.8676` → IC=+0.272 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8676 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.343 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.8249` → IC=+0.268 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8249 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `16312.8746` → IC=+0.275 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16312.8746 (IC base=+0.260)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.253 (n=586)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.1108` → IC=+0.206 (n=587)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1108 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.197 (n=489)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.1386` → IC=+0.206 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1386 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.177 (n=604)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6084 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.7048` → IC=+0.181 (n=117)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.7048 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.38` → IC=+0.195 (n=1315)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.38 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.190 (n=1332)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.2212 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.1532` → IC=+0.198 (n=405)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1532 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `2.4957` → IC=+0.182 (n=1324)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.4957 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.166` → IC=+0.185 (n=601)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.166 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14916.9219` → IC=+0.186 (n=604)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 14916.9219 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `692.0` → IC=+0.187 (n=1286)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 692.0 (IC base=+0.176)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.196 (n=363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.007 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.215 (n=373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.587` → IC=+0.204 (n=820)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.587 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.7037` → IC=+0.196 (n=547)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.7037 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.239 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.492` → IC=+0.234 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.492 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2099` → IC=+0.238 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2099 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.8704` → IC=+0.205 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8704 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2543.292` → IC=+0.219 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2543.292 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.197 (n=553)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 10.0 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.275 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.4518` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4518 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.227)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.215 (n=1390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1478` → IC=+0.214 (n=611)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1478 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.5189` → IC=+0.211 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5189 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.7596` → IC=+0.199 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7596 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.109` → IC=+0.207 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.109 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.8752` → IC=+0.203 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8752 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `1.2312` → IC=+0.205 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2312 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.202 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `2.4495` → IC=+0.206 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4495 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=1425)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.239 (n=381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.210 (n=1138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.201 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.199 (n=761)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 10.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.3986` → IC=+0.194 (n=759)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3986 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.6238` → IC=+0.191 (n=516)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.6238 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.6649` → IC=+0.198 (n=200)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6649 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.6394` → IC=+0.220 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6394 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` > `0.721` → IC=+0.187 (n=1017)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.721 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.210 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.1925` → IC=+0.195 (n=980)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.1925 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `1.7855` → IC=+0.191 (n=742)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.7855 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `6695.679` → IC=+0.197 (n=1138)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6695.679 (IC base=+0.187)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.207 (n=687)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.204 (n=808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.925` → IC=+0.253 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.925 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.7421` → IC=+0.240 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7421 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.23` → IC=+0.203 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.23 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7016` → IC=+0.228 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7016 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.193 (n=702)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.0788` → IC=+0.191 (n=347)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.0788 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.5649` → IC=+0.193 (n=333)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.5649 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.4815` → IC=+0.201 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4815 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.187 (n=911)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `4314.892` → IC=+0.225 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4314.892 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.197 (n=767)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 52.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.216 (n=385)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.211 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.6042` → IC=+0.229 (n=578)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6042 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.245 (n=391)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.7304` → IC=+0.232 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7304 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.5153` → IC=+0.212 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5153 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.3069` → IC=+0.210 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3069 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.1288` → IC=+0.211 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1288 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.9335` → IC=+0.210 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9335 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.227 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.2075` → IC=+0.242 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2075 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `3032.781` → IC=+0.225 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3032.781 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.252 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.208)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.156 (n=778)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0041 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.3889` → IC=+0.140 (n=1675)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.3889 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1486` → IC=+0.144 (n=870)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1486 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.907` → IC=+0.146 (n=487)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 8.907 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.148 (n=231)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0296` → IC=+0.267 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0296 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.336` → IC=+0.165 (n=156)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 10.336 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.146` → IC=+0.156 (n=271)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.146 (IC base=+0.053)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.135 (n=584)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0057 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.3596` → IC=+0.170 (n=553)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.3596 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.1276` → IC=+0.166 (n=279)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1276 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.278 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.2123` → IC=+0.194 (n=83)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2123 (IC base=+0.064)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.129 (n=510)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.006 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.4221` → IC=+0.172 (n=546)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.4221 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.1272` → IC=+0.190 (n=279)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1272 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.09` → IC=+0.232 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.09 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.1087` → IC=+0.246 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1087 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.021)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7353` → IC=+0.155 (n=384)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.7353 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.7372` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.7372 (IC base=+0.029)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.265` → IC=+0.142 (n=121)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.265 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2775` → IC=+0.142 (n=79)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2775 (IC base=+0.029)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.152 (n=257)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0108 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.210 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.1716` → IC=+0.136 (n=215)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1716 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.739` → IC=+0.300 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.739 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.0779` → IC=+0.192 (n=76)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 1.0779 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1499` → IC=+0.218 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1499 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.1848` → IC=+0.146 (n=179)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.1848 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.4913` → IC=+0.152 (n=182)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4913 (IC base=+0.073)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.139 (n=203)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.06 (IC base=+0.073)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.326 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=253)

- **FILTRO** `dist_vwap_pct` > `0.2334` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2334
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=303)

- **FILTRO** `volumen_regimen` < `0.7708` → IC=-0.305 (n=80)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7708
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=240)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.343 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=208)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.280 (n=257)

- **FILTRO** `sigma_ewma_delta_pct` > `10.358` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.358
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=250)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=159)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.271 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=53)

- **FILTRO** `volumen_regimen` < `0.8402` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8402
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=75)

- **FILTRO** `volumen_spike_ratio` > `3.276` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.276
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=58)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.344 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=94)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=94)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.466 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=81)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=82)

- **FILTRO** `ibs_20min` > `0.538` → IC=-0.387 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` > 0.538
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=53)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=54)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.291 (n=89)

- **FILTRO** `libro_liquidez` < `1289.9986` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 1289.9986
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=78)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 1.0 (IC base=-0.154)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=95)

- **FILTRO** `volumen_regimen` < `0.7468` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=85)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.316 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=33)

- **FILTRO** `dist_vwap_pct` < `0.2328` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2328
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1452` → IC=-0.123 (n=295)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1452
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=575)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.188 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0075 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.6686` → IC=+0.157 (n=566)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.6686 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `0.5397` → IC=+0.244 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5397 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.68` → IC=+0.136 (n=127)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 10.68 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.6187` → IC=+0.175 (n=189)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6187 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` < `0.1517` → IC=+0.147 (n=474)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.1517 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.3996` → IC=+0.175 (n=155)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.3996 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.1452` → IC=+0.145 (n=575)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.1452 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.178 (n=150)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `3242.4514` → IC=+0.127 (n=435)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3242.4514 (IC base=+0.054)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6946` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6946
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=171)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.183 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0049 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.135 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 12.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.152 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 6.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.1681` → IC=+0.190 (n=304)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.1681 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.168` → IC=+0.160 (n=95)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 10.168 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.144 (n=304)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.6182 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.136 (n=240)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.4397` → IC=+0.140 (n=273)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4397 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `5396.839` → IC=+0.139 (n=203)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 5396.839 (IC base=+0.127)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=182)

- **FILTRO** `ibs_20min` > `0.1754` → IC=-0.148 (n=106)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1754
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=206)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.122 (n=191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0061 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.147 (n=171)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.8015 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.0908` → IC=+0.136 (n=160)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.0908 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.022` → IC=+0.146 (n=142)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.022 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.6141` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6141 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.152 (n=182)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.176 (n=109)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=159)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.957` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.016)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2391` → IC=-0.259 (n=52)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2391
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=101)

- **FILTRO** `dist_vwap_pct` > `0.1696` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1696
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=115)

- **FILTRO** `volumen_pendiente_norm` < `0.0941` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0941
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=55)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.292 (n=94)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.322 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.6154` → IC=+0.254 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6154 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.6667` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6667 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` < `0.2335` → IC=+0.227 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2335 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.233` → IC=+0.325 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.233 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `0.7871` → IC=+0.270 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7871 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.319 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4815` → IC=+0.355 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4815 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.061)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=73)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.321)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.391 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.321)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.321)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.391 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.321)

- **PATRÓN** `ballena_activa_n` < `1107.0` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1107.0 (IC base=+0.321)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.262 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.228)

- **PATRÓN** `elapsed_s` > `186.2` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 186.2 (IC base=+0.228)

- **PATRÓN** `elapsed_s` < `216.4` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.4 (IC base=+0.228)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.290 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.292 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.228)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.313 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.228)

- **PATRÓN** `ballena_activa_n` < `1862.0` → IC=+0.286 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1862.0 (IC base=+0.228)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=73)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.321)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.391 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.321)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.321)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.391 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.321)

- **PATRÓN** `ballena_activa_n` < `1107.0` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1107.0 (IC base=+0.321)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.262 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.228)

- **PATRÓN** `elapsed_s` > `186.2` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 186.2 (IC base=+0.228)

- **PATRÓN** `elapsed_s` < `216.4` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.4 (IC base=+0.228)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.290 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.292 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.228)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.313 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.228)

- **PATRÓN** `ballena_activa_n` < `1862.0` → IC=+0.286 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1862.0 (IC base=+0.228)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1245)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2938.7046` → IC=+0.135 (n=436)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2938.7046 (IC base=+0.104)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1245)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2938.7046` → IC=+0.135 (n=436)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2938.7046 (IC base=+0.104)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=201)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=200)

- **FILTRO** `libro_liquidez` < `5477.3482` → IC=-0.173 (n=108)

  - _Acción_: SKIP cuando `libro_liquidez` < 5477.3482
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=108)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=384)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12324.2702` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `libro_liquidez` < 12324.2702
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=66)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=61)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `ballena_activa_n` > `63.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 63.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **PATRÓN** `liq_n` > `5.0` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 5.0 (IC base=+0.059)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.132 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 17.0 (IC base=+0.059)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3614)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=106)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=63)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=106)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.133 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=132)

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

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=1367)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=1321)

- **FILTRO** `liq_usd_total` < `12056.79` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `liq_usd_total` < 12056.79
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=717)

- **FILTRO** `liq_n` < `11.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `liq_n` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `liq_usd_total` < `13082.51` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `liq_usd_total` < 13082.51
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=430)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=411)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.145 (n=181)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=866)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=866)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=889)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=889)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=227)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=227)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.141 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=166)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=258)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=282)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=267)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.120 (n=77)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=244)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=357)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=357)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=202)

- **FILTRO** `libro_liquidez` < `631.7738` → IC=-0.128 (n=127)

  - _Acción_: SKIP cuando `libro_liquidez` < 631.7738
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=260)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=271)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=199)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `profundidad_ratio` < `11.3` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `profundidad_ratio` < 11.3
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=61)

- **PATRÓN** `py_entrada` < `0.58` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.58 (IC base=+0.032)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=36)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.169 (n=164)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` < 0.46 (IC base=+0.014)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.156 (n=62)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=282)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.170 (n=116)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=238)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.5 (IC base=+0.056)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.125 (n=350)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=195)

- **FILTRO** `profundidad_ratio` < `42.5` → IC=-0.174 (n=136)

  - _Acción_: SKIP cuando `profundidad_ratio` < 42.5
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=409)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.136 (n=215)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=243)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.156 (n=94)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=414)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.133 (n=137)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=506)

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

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.163 (n=6379)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=19477)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.177 (n=6402)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=20161)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.190 (n=1155)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3579)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.177 (n=1095)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=3640)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.141 (n=1242)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `1205.5548` → IC=+0.135 (n=2368)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1205.5548 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.126 (n=2217)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.5 (IC base=+0.010)

- **PATRÓN** `libro_liquidez` > `1418.1196` → IC=+0.149 (n=1610)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1418.1196 (IC base=+0.010)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.150 (n=894)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=2858)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.179 (n=919)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2846)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=1125)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=3718)

- **PATRÓN** `ibs_20min` > `0.965` → IC=+0.130 (n=1608)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.965 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1486.6868` → IC=+0.122 (n=2365)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1486.6868 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.156 (n=1165)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=3558)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2407)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2331)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.191 (n=898)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=2722)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3599)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.257 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=430)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.234 (n=287)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=911)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.192 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=303)

- **FILTRO** `libro_liquidez` < `3742.1782` → IC=-0.167 (n=223)

  - _Acción_: SKIP cuando `libro_liquidez` < 3742.1782
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=943)

- **FILTRO** `libro_liquidez` < `1786.4389` → IC=-0.161 (n=240)

  - _Acción_: SKIP cuando `libro_liquidez` < 1786.4389
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=722)

- **FILTRO** `ibs_20min` > `0.8947` → IC=-0.137 (n=521)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8947
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=541)

- **FILTRO** `libro_liquidez` < `2090.2217` → IC=-0.168 (n=350)

  - _Acción_: SKIP cuando `libro_liquidez` < 2090.2217
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=712)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=233)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=43)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.037)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=39)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=68)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=17800)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=39744)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.286 (n=14276)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=43268)

- **FILTRO** `ibs_7min` < `0.2343` → IC=-0.230 (n=14386)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2343
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=43158)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.153 (n=19012)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=38532)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.241 (n=17751)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=54477)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.183 (n=17841)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=54387)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.149 (n=2870)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7231)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=2408)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=7693)

- **FILTRO** `ibs_7min` < `0.7132` → IC=-0.243 (n=3333)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7132
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6768)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.181 (n=2066)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8035)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.272 (n=3122)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=9402)

- **FILTRO** `ibs_7min` > `0.7699` → IC=-0.211 (n=3130)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7699
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9394)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=2327)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=7356)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.266 (n=2270)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7413)

- **FILTRO** `ibs_7min` < `0.7232` → IC=-0.201 (n=2420)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7232
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7263)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.191 (n=2410)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7273)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=2422)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=7427)

- **FILTRO** `ibs_7min` > `0.2672` → IC=-0.193 (n=2462)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2672
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=7387)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.182 (n=2446)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7403)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.160 (n=2355)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=7216)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2366)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=7205)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.246 (n=3154)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=6417)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.196 (n=2235)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7336)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.255 (n=3103)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=10205)

- **FILTRO** `ibs_7min` > `0.7321` → IC=-0.178 (n=3326)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7321
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=9982)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.125 (n=3059)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=6308)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2211)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7156)

- **FILTRO** `ibs_7min` < `0.7253` → IC=-0.190 (n=2341)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7253
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7026)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.191 (n=2282)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7085)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.264 (n=2190)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=7518)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.178 (n=2426)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7282)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.177 (n=2345)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7363)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=2295)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7102)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.222 (n=3049)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=6348)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.218 (n=2262)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=7135)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.192 (n=3387)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=10406)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.294 (n=2256)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=7169)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.224 (n=2348)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=7077)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.199 (n=2326)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=7099)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.220 (n=3195)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9851)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=986)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1270)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.121 (n=209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=501)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=554)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=853)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.475` → IC=-0.122 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=334)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=329)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=446)

- **FILTRO** `libro_liquidez` < `3257.9143` → IC=-0.156 (n=181)

  - _Acción_: SKIP cuando `libro_liquidez` < 3257.9143
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=543)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.138 (n=1212)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.135 (n=630)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `3825.72` → IC=+0.146 (n=806)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 3825.72 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3574.1299` → IC=+0.145 (n=548)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3574.1299 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.144 (n=408)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 11.0 (IC base=+0.129)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4385` → IC=+0.135 (n=94)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.4385 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.188 (n=136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 14.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `372.075` → IC=+0.144 (n=248)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 372.075 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2543.343` → IC=+0.198 (n=94)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2543.343 (IC base=+0.134)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.138 (n=249)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.137 (n=224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 14.0 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.129 (n=300)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.04 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2064.8398` → IC=+0.131 (n=223)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2064.8398 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.136 (n=163)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 12.0 (IC base=+0.120)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.191 (n=160)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `total_vol_5m` < `385.7846` → IC=+0.222 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 385.7846 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7599.7355` → IC=+0.142 (n=160)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 7599.7355 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.188 (n=107)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 69.0 (IC base=+0.140)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4324` → IC=+0.245 (n=96)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4324 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.170 (n=195)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.150)

- **PATRÓN** `total_vol_5m` < `4950.202` → IC=+0.178 (n=141)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 4950.202 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3218.4716` → IC=+0.170 (n=189)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3218.4716 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 27.0 (IC base=+0.150)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.139 (n=153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 10.0 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `3571.4392` → IC=+0.151 (n=104)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3571.4392 (IC base=+0.097)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.9794` → IC=-0.266 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.9794
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=139)

- **FILTRO** `sigma_h` > `0.0073` → IC=-0.327 (n=171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=515)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.151 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0042 (IC base=-0.084)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.308 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=154)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.296 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.034)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.197 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

- **FILTRO** `pct_vs_K` |x|> `9.8932` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.8932
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0137` → IC=-0.250 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0137
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=93)

- **FILTRO** `T_h` < `87.7913` → IC=-0.177 (n=60)

  - _Acción_: SKIP cuando `T_h` < 87.7913
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=63)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.227 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=-0.108)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.232 (n=416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=215)

- **FILTRO** `T_h` > `87.0918` → IC=-0.203 (n=422)

  - _Acción_: SKIP cuando `T_h` > 87.0918
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=209)

- **FILTRO** `sigma_h` > `0.0095` → IC=-0.244 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=409)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.246 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=408)

- **FILTRO** `T_h` > `54.2531` → IC=-0.263 (n=407)

  - _Acción_: SKIP cuando `T_h` > 54.2531
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=137)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `71.159` → IC=-0.186 (n=138)

  - _Acción_: SKIP cuando `T_h` > 71.159
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=69)

- **FILTRO** `pct_vs_K` |x|> `2.7791` → IC=-0.368 (n=51)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7791
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=156)

- **FILTRO** `T_h` > `73.0783` → IC=-0.269 (n=145)

  - _Acción_: SKIP cuando `T_h` > 73.0783
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=49)

- **FILTRO** `pct_vs_K` |x|> `2.9778` → IC=-0.439 (n=47)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9778
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=147)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.007` → IC=-0.285 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=91)

- **FILTRO** `T_h` > `69.4221` → IC=-0.261 (n=136)

  - _Acción_: SKIP cuando `T_h` > 69.4221
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=46)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.364 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=128)

- **FILTRO** `T_h` > `57.7851` → IC=-0.272 (n=112)

  - _Acción_: SKIP cuando `T_h` > 57.7851
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=58)

- **PATRÓN** `pct_vs_K` |x|≤ `0.7672` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `pct_vs_K` |x|≤ 0.7672 (IC base=-0.180)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.008` → IC=-0.278 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=132)

- **FILTRO** `T_h` > `87.9882` → IC=-0.206 (n=117)

  - _Acción_: SKIP cuando `T_h` > 87.9882
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

- **FILTRO** `sigma_h` > `0.0152` → IC=-0.375 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0152
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=91)

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.281 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=82)

- **FILTRO** `T_h` > `63.9197` → IC=-0.290 (n=60)

  - _Acción_: SKIP cuando `T_h` > 63.9197
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=61)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1236` → IC=+0.477 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1236 (IC base=+0.344)

- **PATRÓN** `sigma_h` < `0.0138` → IC=+0.359 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0138 (IC base=+0.344)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.396 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.344)

- **PATRÓN** `T_h` < `0.3604` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3604 (IC base=+0.344)

- **PATRÓN** `T_h` > `0.7606` → IC=+0.381 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7606 (IC base=+0.344)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.344)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.359 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.344)

- **PATRÓN** `edge` > `0.0992` → IC=+0.443 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0992 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.436 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.417)

- **PATRÓN** `T_h` > `1.484` → IC=+0.422 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.3767` → IC=+0.452 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3767 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1831` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1831 (IC base=+0.186)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.186)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.459 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.420)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.419 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.420)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.423 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.420)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.420)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.407 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.420)

- **PATRÓN** `dist_50` > `0.3792` → IC=+0.459 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3792 (IC base=+0.420)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.431 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.420)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.420)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1884` → IC=+0.484 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1884 (IC base=+0.441)

- **PATRÓN** `sigma_h` < `0.0164` → IC=+0.468 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0164 (IC base=+0.441)

- **PATRÓN** `T_h` > `0.4292` → IC=+0.452 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4292 (IC base=+0.441)

- **PATRÓN** `dist_50` > `0.3553` → IC=+0.468 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3553 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.439 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.441)

- **PATRÓN** `edge` > `0.2005` → IC=+0.479 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.466)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.479 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.466)

- **PATRÓN** `T_h` > `1.4874` → IC=+0.480 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4874 (IC base=+0.466)

- **PATRÓN** `dist_50` > `0.4658` → IC=+0.492 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4658 (IC base=+0.466)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.473 (n=145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.466)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=322)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=396)

- **PATRÓN** `streak_estiramiento` < `0.8365` → IC=+0.124 (n=267)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.8365 (IC base=+0.051)

- **PATRÓN** `libro_liquidez` > `2508.1541` → IC=+0.141 (n=143)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2508.1541 (IC base=+0.051)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=28)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.2204` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.2204 (IC base=+0.008)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.093)

- **PATRÓN** `streak_estiramiento` < `0.4376` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `streak_estiramiento` < 0.4376 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 35.0 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `2208.5143` → IC=+0.142 (n=135)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2208.5143 (IC base=+0.093)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=95)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=104)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=748)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `volumen_racha` > `3677.1957` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_racha` > 3677.1957
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `libro_liquidez` < `3338.6704` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 3338.6704
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `streak_estiramiento` > `1.1496` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1496
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=43)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `hora_utc` > `3.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `streak_len` > `4.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### STREAK_FADE_60M#SOL#60min
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.056)

- **PATRÓN** `volumen_racha` < `17126.646` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 17126.646 (IC base=+0.056)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1034)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1332)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1204)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=1245)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `19.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=26)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=4132)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=26)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2312)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.192 (n=1679)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0054 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.189 (n=1272)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0122 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1772` → IC=+0.188 (n=3359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1772 (IC base=+0.172)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3485` → IC=+0.179 (n=3476)

  - _Acción_: Kelly boost +0.90€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3485 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=3528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.174 (n=3530)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `ibs_15` > `0.5417` → IC=+0.247 (n=3818)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5417 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1298` → IC=+0.169 (n=1835)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1298 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.3195` → IC=+0.158 (n=3052)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.3195 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.438` → IC=+0.259 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.438 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `4629.3821` → IC=+0.191 (n=1272)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 4629.3821 (IC base=+0.172)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1508)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.251 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.265 (n=215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.216)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.245 (n=214)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.284 (n=643)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.1397` → IC=+0.232 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1397 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.114` → IC=+0.293 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.114 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.217 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `8615.9433` → IC=+0.227 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8615.9433 (IC base=+0.216)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.186 (n=253)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0035 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.1078` → IC=+0.159 (n=506)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1078 (IC base=+0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1412` → IC=+0.152 (n=506)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1412 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2808` → IC=+0.149 (n=602)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2808 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.149 (n=792)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5357` → IC=+0.238 (n=759)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5357 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.160 (n=469)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.707` → IC=+0.274 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.707 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3225.814` → IC=+0.150 (n=759)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3225.814 (IC base=+0.145)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.597` → IC=-0.167 (n=40)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.597
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=360)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8831` → IC=+0.243 (n=302)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8831 (IC base=+0.088)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=484)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.088)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.781` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 15.781 (IC base=+0.002)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0241` → IC=+0.228 (n=288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0241 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1304` → IC=+0.222 (n=576)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1304 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3415` → IC=+0.224 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3415 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.208 (n=772)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.5294` → IC=+0.274 (n=864)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5294 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1291` → IC=+0.213 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1291 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.324` → IC=+0.230 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.324 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2955.9488` → IC=+0.293 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2955.9488 (IC base=+0.198)

- **PATRÓN** `ibs_15` < `0.1089` → IC=+0.166 (n=792)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` < 0.1089 (IC base=+0.069)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.391 (n=218)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1482` → IC=+0.383 (n=435)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1482 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1386` → IC=+0.389 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1386 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.377 (n=658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7863` → IC=+0.401 (n=654)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7863 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1521` → IC=+0.381 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1521 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.228` → IC=+0.389 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.228 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3859.8614` → IC=+0.374 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3859.8614 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.365 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.404 (n=112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.368 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2158` → IC=+0.383 (n=152)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2158 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.395 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.381 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8057` → IC=+0.390 (n=335)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8057 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2485` → IC=+0.387 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2485 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.365` → IC=+0.381 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.365 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `8065.6565` → IC=+0.387 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8065.6565 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.406 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.374 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.366)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.384 (n=145)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.366)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.366 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.382 (n=285)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.384 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.390 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.366)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.378 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.7485` → IC=+0.410 (n=319)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7485 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.388 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` < `0.2948` → IC=+0.369 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2948 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.356` → IC=+0.396 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.356 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.372 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `4019.374` → IC=+0.398 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4019.374 (IC base=+0.366)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.375 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.366)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.175 (n=2241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=2243)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=1758)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2726)

- **PATRÓN** `ibs_15` > `0.6332` → IC=+0.280 (n=1084)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6332 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1124` → IC=+0.207 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1124 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2696` → IC=+0.197 (n=926)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2696 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2301` → IC=+0.271 (n=1254)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2301 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.3659` → IC=+0.283 (n=3762)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3659 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.6639` → IC=+0.279 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6639 (IC base=-0.012)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.214 (n=663)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1991)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.229 (n=662)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1992)

- **FILTRO** `sigma_ewma_delta_pct` > `23.321` → IC=-0.266 (n=383)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.321
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=2271)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=66)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=2588)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.169 (n=264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0028 (IC base=+0.094)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.279 (n=238)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=+0.094)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1125` → IC=+0.271 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1125 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.120 (n=791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 5.0 (IC base=+0.094)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.333 (n=357)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1071` → IC=+0.284 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1071 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` < `0.3722` → IC=+0.291 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3722 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.603` → IC=+0.131 (n=396)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 8.603 (IC base=+0.094)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.223 (n=63)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1432` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1432 (IC base=-0.194)

- **PATRÓN** `ibs_15` < `0.6128` → IC=+0.315 (n=63)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6128 (IC base=-0.194)

- **PATRÓN** `dist_vwap_pct` < `0.0415` → IC=+0.311 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0415 (IC base=-0.194)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.194)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=710)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.162 (n=480)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.159 (n=364)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0049 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0718` → IC=+0.186 (n=240)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0718 (IC base=+0.152)

- **PATRÓN** `drift_15min` |x|≤ `0.4004` → IC=+0.152 (n=182)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.4004 (IC base=+0.152)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.194 (n=420)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_15` > `0.5905` → IC=+0.248 (n=546)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5905 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.4686` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.4686 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.152 (n=429)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.379` → IC=+0.250 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.379 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=710)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `5210.4456` → IC=+0.153 (n=364)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 5210.4456 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.254 (n=927)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.246)

- **PATRÓN** `drift_15min` |x|≤ `0.7722` → IC=+0.257 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7722 (IC base=+0.246)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1556` → IC=+0.262 (n=927)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1556 (IC base=+0.246)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3263` → IC=+0.246 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3263 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.247 (n=1238)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.246)

- **PATRÓN** `ibs_15` < `0.3774` → IC=+0.279 (n=1390)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3774 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` > `0.1596` → IC=+0.261 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1596 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.394` → IC=+0.254 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.394 (IC base=+0.246)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.232 (n=259)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=780)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.251 (n=352)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=687)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.282 (n=259)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=780)

- **FILTRO** `sigma_ewma_delta_pct` > `6.602` → IC=-0.198 (n=240)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.602
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=799)

- **FILTRO** `sigma_ewma_delta_pct` > `17.794` → IC=-0.147 (n=542)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.794
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4324)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.189)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.189)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.189)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.189)

- **PATRÓN** `delta_ratio_macro` |x|> `0.082` → IC=+0.230 (n=550)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.082 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.290 (n=617)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.2577` → IC=+0.239 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2577 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.247 (n=552)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=682)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.210)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.210)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0695` → IC=+0.277 (n=796)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0695 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1173` → IC=+0.294 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1173 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.137` → IC=+0.317 (n=594)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.137 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7845` → IC=+0.353 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7845 (IC base=-0.025)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.167 (n=25)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.088)

- **PATRÓN** `drift_15min` |x|≤ `0.3976` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `drift_15min` |x|≤ 0.3976 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 59.0 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.198` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.198 (IC base=+0.045)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.167 (n=25)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.088)

- **PATRÓN** `drift_15min` |x|≤ `0.3976` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `drift_15min` |x|≤ 0.3976 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 59.0 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.198` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.198 (IC base=+0.045)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.296 (n=991)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0537` → IC=+0.323 (n=376)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0537 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2402` → IC=+0.309 (n=375)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2402 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2242` → IC=+0.303 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2242 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=1172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.320 (n=1126)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2735` → IC=+0.324 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2735 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.378 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `13914.1536` → IC=+0.312 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13914.1536 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.313 (n=201)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.307 (n=273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.318 (n=201)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.312 (n=200)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3852` → IC=+0.293 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3852 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.306 (n=602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.313 (n=601)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.1479` → IC=+0.323 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1479 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.377 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `16196.8854` → IC=+0.328 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16196.8854 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.303 (n=526)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0524` → IC=+0.320 (n=176)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0524 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1424` → IC=+0.301 (n=350)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1424 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3023` → IC=+0.310 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3023 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.313 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.297 (n=477)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.324 (n=525)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2911` → IC=+0.321 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2911 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.373 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1232` → IC=-0.155 (n=85)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1232
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=257)

- **FILTRO** `ballena_activa_n` > `43.0` → IC=-0.133 (n=232)

  - _Acción_: SKIP cuando `ballena_activa_n` > 43.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=78)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.180 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=363)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.209 (n=108)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=114)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1342` → IC=-0.154 (n=50)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1342
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=150)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2395` → IC=-0.121 (n=93)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2395
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=95)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2021` → IC=-0.250 (n=26)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2021
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=27)

- **FILTRO** `ballena_activa_n` > `528.0` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `ballena_activa_n` > 528.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1254` → IC=-0.200 (n=18)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1254
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=39)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.3147` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3147
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0611` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0611
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=38)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0905` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### UPDOWN_OU_5M#XRP#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0898` → IC=-0.227 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0898
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `sigma_h` > `0.0058` → IC=-0.250 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `87.7391` → IC=+0.194 (n=502)

  - _Acción_: Kelly boost +0.97€ cuando `T_h` > 87.7391 (IC base=+0.189)

- **PATRÓN** `ratio` < `0.973` → IC=+0.407 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.189)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.354 (n=2295)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0229` → IC=+0.376 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0229 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `109.5528` → IC=+0.181 (n=208)

  - _Acción_: Kelly boost +0.90€ cuando `T_h` > 109.5528 (IC base=+0.157)

- **PATRÓN** `ratio` < `0.9838` → IC=+0.323 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9838 (IC base=+0.157)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.306 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.295)

- **PATRÓN** `ratio` > `1.0451` → IC=+0.407 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0451 (IC base=+0.295)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.236 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.229)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.397 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.229)

- **PATRÓN** `T_h` > `111.9928` → IC=+0.352 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.335 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0788` → IC=+0.439 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0788 (IC base=+0.399)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5417 sube el IC de +0.172 a +0.247 en UPDOWN_GBM#15min (n=3818). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.216 a +0.284 en UPDOWN_GBM#BTC#15min (n=643). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5357 sube el IC de +0.145 a +0.238 en UPDOWN_GBM#ETH#15min (n=759). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8831 sube el IC de +0.088 a +0.243 en UPDOWN_GBM#SOL#15min (n=302). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5294 sube el IC de +0.198 a +0.274 en UPDOWN_GBM#XRP#15min (n=864). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1089 sube el IC de +0.069 a +0.166 en UPDOWN_GBM#XRP#15min (n=792). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6332 sube el IC de -0.068 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1084). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3659 sube el IC de -0.012 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=3762). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.094 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=357). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6128 sube el IC de -0.194 a +0.315 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=63). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5905 sube el IC de +0.152 a +0.248 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=546). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3774 sube el IC de +0.246 a +0.279 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1390). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.189 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.038 a +0.290 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=617). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.210 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.137 sube el IC de -0.025 a +0.317 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=594). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.088 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7 (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.088 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.292 a +0.320 en UPDOWN_GBM_IBS_ALTO (n=1126). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.288 a +0.313 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=601). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.295 a +0.324 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=525). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7863 sube el IC de +0.365 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=654). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.362 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=335). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7485 sube el IC de +0.366 a +0.410 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=319). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1976 | +0.089 | +208.73€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1976 | +0.089 | +208.73€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1584 | +0.093 | +180.00€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1584 | +0.093 | +180.00€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 756 | -0.005 | +79.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 756 | -0.005 | +79.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 565 | -0.033 | +46.52€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 565 | -0.033 | +46.52€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 149 | +0.089 | +26.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 149 | +0.089 | +26.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 41410 | -0.081 | -5109.30€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2340 | +0.044 | -263.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 39070 | -0.088 | -4845.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4544 | -0.114 | -776.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4544 | -0.114 | -776.31€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2340 | +0.044 | -263.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2340 | +0.044 | -263.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4455 | -0.109 | -891.33€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4455 | -0.109 | -891.33€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11078 | -0.019 | -1040.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11078 | -0.019 | -1040.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 11002 | -0.107 | -812.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 11002 | -0.107 | -812.83€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7991 | -0.132 | -1325.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7991 | -0.132 | -1325.16€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 37151 | -0.015 | +3261.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 9605 | +0.004 | +1638.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 27546 | -0.021 | +1622.82€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 37151 | -0.015 | +3261.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 9605 | +0.004 | +1638.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 27546 | -0.021 | +1622.82€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 151650 | +0.115 | -6058.43€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 19162 | +0.182 | -623.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 673 | -0.013 | -71.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 122803 | +0.107 | -5022.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9012 | +0.098 | -340.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 20360 | +0.108 | -1249.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 62 | -0.156 | +10.44€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 20283 | +0.109 | -1247.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 29256 | +0.127 | -467.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5274 | +0.185 | -209.16€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 20344 | +0.121 | -115.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3596 | +0.081 | -119.68€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 20415 | +0.100 | -1415.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 77 | -0.120 | -4.86€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 20323 | +0.101 | -1399.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 32271 | +0.124 | -597.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8320 | +0.177 | -174.93€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 20628 | +0.107 | -365.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3311 | +0.101 | -48.36€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 28966 | +0.115 | -1405.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5359 | +0.198 | -249.17€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 576 | +0.019 | -17.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 20926 | +0.096 | -965.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2105 | +0.121 | -172.76€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 20382 | +0.107 | -924.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 70 | -0.097 | +4.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 20299 | +0.108 | -928.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 24403 | +0.197 | -1448.98€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 24403 | +0.197 | -1448.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5542 | +0.181 | -452.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5542 | +0.181 | -452.41€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3172 | +0.203 | -71.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3172 | +0.203 | -71.76€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5480 | +0.181 | -435.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5480 | +0.181 | -435.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4735 | +0.248 | -164.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4735 | +0.248 | -164.73€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5395 | +0.189 | -338.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5395 | +0.189 | -338.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1059 | +0.426 | -36.57€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1059 | +0.426 | -36.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 421 | +0.434 | -8.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 421 | +0.434 | -8.32€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 417 | +0.433 | -7.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 417 | +0.433 | -7.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 207 | +0.400 | -17.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 207 | +0.400 | -17.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 85517 | +0.202 | -6053.96€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 85517 | +0.202 | -6053.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 14697 | +0.186 | -1502.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 14697 | +0.186 | -1502.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13807 | +0.225 | -457.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13807 | +0.225 | -457.82€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 14653 | +0.181 | -1530.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 14653 | +0.181 | -1530.40€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13904 | +0.219 | -535.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13904 | +0.219 | -535.06€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 14188 | +0.202 | -918.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 14188 | +0.202 | -918.79€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 14268 | +0.198 | -1109.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 14268 | +0.198 | -1109.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 32783 | +0.116 | +195.45€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 32783 | +0.116 | +195.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 16302 | +0.119 | +166.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 16302 | +0.119 | +166.89€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 16481 | +0.114 | +28.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 16481 | +0.114 | +28.56€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2150 | +0.293 | -5.25€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2150 | +0.293 | -5.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 987 | +0.281 | -24.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 987 | +0.281 | -24.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1041 | +0.298 | +14.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1041 | +0.298 | +14.35€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 122 | +0.347 | +4.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 122 | +0.347 | +4.48€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 990 | +0.443 | +6.29€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 990 | +0.443 | +6.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 481 | +0.436 | -4.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 481 | +0.436 | -4.74€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 462 | +0.450 | +10.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 462 | +0.450 | +10.33€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 47 | +0.398 | +0.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 47 | +0.398 | +0.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1709 | +0.072 | -65.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 662 | +0.048 | -56.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1047 | +0.086 | -8.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 76 | +0.115 | +4.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 76 | +0.115 | +4.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1311 | +0.079 | -28.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 264 | +0.049 | -19.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1047 | +0.086 | -8.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 322 | +0.031 | -41.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 322 | +0.031 | -41.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 65044 | +0.101 | -1618.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5253 | +0.091 | +57.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 59791 | +0.101 | -1675.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 35737 | +0.105 | -398.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5253 | +0.091 | +57.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 30484 | +0.108 | -455.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 13461 | +0.109 | -77.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 13461 | +0.109 | -77.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 15846 | +0.083 | -1142.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 15846 | +0.083 | -1142.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 899 | +0.192 | -110.13€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 899 | +0.192 | -110.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 899 | +0.192 | -110.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 899 | +0.192 | -110.13€ | 1 | 4 |
| ✅ GBM_LATE_15M | 44593 | +0.095 | +23528.94€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 44593 | +0.095 | +23528.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7416 | +0.218 | +6179.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7416 | +0.218 | +6179.41€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6734 | +0.180 | +5186.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6734 | +0.180 | +5186.15€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 7980 | +0.205 | +6205.74€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7980 | +0.205 | +6205.74€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 6194 | +0.044 | +1780.27€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6194 | +0.044 | +1780.27€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 6254 | -0.032 | +1351.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6254 | -0.032 | +1351.37€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 10015 | -0.030 | +2825.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 10015 | -0.030 | +2825.99€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 47840 | +0.085 | +26219.26€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 47840 | +0.085 | +26219.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 9251 | +0.002 | +4688.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 9251 | +0.002 | +4688.44€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 10183 | +0.010 | +2477.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 10183 | +0.010 | +2477.52€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6612 | +0.280 | +7148.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6612 | +0.280 | +7148.91€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8699 | +0.013 | +2185.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8699 | +0.013 | +2185.03€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7585 | +0.039 | +3168.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7585 | +0.039 | +3168.20€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5510 | +0.307 | +6551.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5510 | +0.307 | +6551.15€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 35322 | +0.180 | +28715.65€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 35322 | +0.180 | +28715.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5352 | +0.232 | +4806.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5352 | +0.232 | +4806.70€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5558 | +0.150 | +4126.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5558 | +0.150 | +4126.63€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5672 | +0.222 | +4861.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5672 | +0.222 | +4861.84€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6005 | +0.137 | +4572.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6005 | +0.137 | +4572.64€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6637 | +0.125 | +4962.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6637 | +0.125 | +4962.49€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6098 | +0.228 | +5385.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6098 | +0.228 | +5385.36€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9564 | +0.132 | +4651.48€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9564 | +0.132 | +4651.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 409 | +0.154 | +256.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 409 | +0.154 | +256.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2776 | +0.141 | +1553.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2776 | +0.141 | +1553.11€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2864 | +0.136 | +1361.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2864 | +0.136 | +1361.64€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2421 | +0.107 | +959.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2421 | +0.107 | +959.43€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 627 | +0.133 | +281.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 627 | +0.133 | +281.63€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 44754 | +0.186 | +36006.50€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 44754 | +0.186 | +36006.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7079 | +0.244 | +6658.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7079 | +0.244 | +6658.93€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 7005 | +0.147 | +4818.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 7005 | +0.147 | +4818.21€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7582 | +0.233 | +6763.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7582 | +0.233 | +6763.22€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7391 | +0.139 | +5274.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7391 | +0.139 | +5274.34€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7911 | +0.121 | +5503.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7911 | +0.121 | +5503.62€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7786 | +0.233 | +6988.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7786 | +0.233 | +6988.18€ | 0 | 20 |
| ✅ GBM_LATE_5M | 12088 | +0.203 | +9481.81€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 12088 | +0.203 | +9481.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1026 | +0.242 | +956.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1026 | +0.242 | +956.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2796 | +0.207 | +2389.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2796 | +0.207 | +2389.72€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1167 | +0.196 | +861.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1167 | +0.196 | +861.83€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3368 | +0.193 | +2374.27€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3368 | +0.193 | +2374.27€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 1808 | +0.193 | +1401.89€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1808 | +0.193 | +1401.89€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1923 | +0.208 | +1497.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1923 | +0.208 | +1497.52€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3731 | +0.064 | +1166.96€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 3731 | +0.064 | +1166.96€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1375 | +0.080 | +470.64€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1375 | +0.080 | +470.64€ | 0 | 5 |
| ✅ GBM_LATE_60M#ETH | 1208 | +0.066 | +413.12€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1208 | +0.066 | +413.12€ | 0 | 7 |
| ✅ GBM_LATE_60M#SOL | 1148 | +0.042 | +283.21€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1148 | +0.042 | +283.21€ | 0 | 13 |
| 🚫 GBM_LATE_60M_FADE | 596 | -0.244 | -20.23€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 596 | -0.244 | -20.23€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 223 | -0.247 | -14.68€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 223 | -0.247 | -14.68€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 212 | -0.229 | +1.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 212 | -0.229 | +1.48€ | 6 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 161 | -0.255 | -7.03€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 161 | -0.255 | -7.03€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1624 | +0.083 | +407.55€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1624 | +0.083 | +407.55€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 632 | +0.079 | +148.75€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 632 | +0.079 | +148.75€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 566 | +0.056 | +90.55€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 566 | +0.056 | +90.55€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 426 | +0.124 | +168.25€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 426 | +0.124 | +168.25€ | 3 | 10 |
| ✅ LATE_WINDOW_5MIN | 172 | +0.276 | +168.39€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 172 | +0.276 | +168.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 172 | +0.276 | +168.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 172 | +0.276 | +168.39€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3544 | +0.103 | +879.96€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3544 | +0.103 | +879.96€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3544 | +0.103 | +879.96€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3544 | +0.103 | +879.96€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 621 | -0.026 | -9.06€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 621 | -0.026 | -9.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 181 | -0.003 | +3.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 181 | -0.003 | +3.97€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 132 | +0.015 | +5.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 132 | +0.015 | +5.11€ | 1 | 2 |
| ✅ LIQUIDACIONES_15M#SOL | 223 | -0.016 | -2.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 223 | -0.016 | -2.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 3826 | +0.015 | +85.23€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3826 | +0.015 | +85.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 185 | +0.029 | -0.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 185 | +0.029 | -0.77€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 797 | +0.007 | +28.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 797 | +0.007 | +28.91€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 209 | -0.007 | -2.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 209 | -0.007 | -2.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1417 | +0.023 | +29.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1417 | +0.023 | +29.23€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 758 | +0.012 | +2.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 758 | +0.012 | +2.16€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 460 | +0.015 | +28.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 460 | +0.015 | +28.00€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1850 | -0.039 | -27.89€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1850 | -0.039 | -27.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 539 | -0.029 | -10.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 539 | -0.029 | -10.98€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 638 | -0.019 | +4.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 638 | -0.019 | +4.32€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 673 | -0.067 | -21.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 673 | -0.067 | -21.23€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 9748 | -0.027 | +17.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4631 | -0.036 | -81.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 5117 | -0.019 | +98.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 296 | -0.027 | -0.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 151 | -0.003 | +6.35€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 145 | -0.051 | -7.25€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2472 | -0.020 | +17.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1166 | -0.025 | -5.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1306 | -0.015 | +22.61€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1051 | -0.028 | +6.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 530 | -0.045 | -16.53€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 521 | -0.011 | +23.08€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2154 | -0.038 | -53.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1003 | -0.050 | -55.69€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1151 | -0.027 | +2.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1890 | -0.017 | +44.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 910 | -0.030 | +0.24€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 980 | -0.006 | +44.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1885 | -0.032 | +2.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 871 | -0.040 | -10.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1014 | -0.026 | +12.95€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 52419 | -0.000 | +2663.63€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 52419 | -0.000 | +2663.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 9469 | +0.026 | +1214.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 9469 | +0.026 | +1214.25€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7517 | -0.034 | -103.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7517 | -0.034 | -103.82€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9572 | +0.024 | +1003.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9572 | +0.024 | +1003.63€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7363 | -0.048 | -145.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7363 | -0.048 | -145.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8868 | -0.004 | +253.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8868 | -0.004 | +253.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9630 | +0.016 | +441.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9630 | +0.016 | +441.40€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6724 | -0.058 | -152.48€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6724 | -0.058 | -152.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1231 | -0.001 | -16.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1231 | -0.001 | -16.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1770 | -0.074 | -39.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1770 | -0.074 | -39.16€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 61 | -0.024 | -0.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 61 | -0.024 | -0.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 781 | -0.121 | -34.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 781 | -0.121 | -34.67€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2024 | -0.072 | -36.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2024 | -0.072 | -36.23€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 857 | -0.016 | -25.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 857 | -0.016 | -25.51€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3368 | +0.004 | -1.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3368 | +0.004 | -1.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 131 | -0.034 | -0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 131 | -0.034 | -0.72€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 129772 | -0.077 | +1658.02€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 129772 | -0.077 | +1658.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 22625 | -0.077 | +1132.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 22625 | -0.077 | +1132.33€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 19532 | -0.101 | -1048.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 19532 | -0.101 | -1048.66€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 22879 | -0.067 | +1225.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 22879 | -0.067 | +1225.28€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 19075 | -0.098 | -620.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 19075 | -0.098 | -620.08€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 23190 | -0.057 | +324.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 23190 | -0.057 | +324.49€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 22471 | -0.068 | +644.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 22471 | -0.068 | +644.66€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8805 | -0.035 | -186.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8805 | -0.035 | -186.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1995 | -0.047 | -26.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1995 | -0.047 | -26.66€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2604 | -0.027 | -43.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2604 | -0.027 | -43.23€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1220 | -0.058 | -29.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1220 | -0.058 | -29.35€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 975 | -0.031 | -35.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 975 | -0.031 | -35.88€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1747 | +0.123 | +711.67€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1611 | +0.129 | +699.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 375 | +0.134 | +182.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 375 | +0.134 | +182.94€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 332 | +0.120 | +117.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 332 | +0.120 | +117.36€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#ETH | 320 | +0.140 | +160.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 320 | +0.140 | +160.31€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 281 | +0.150 | +153.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 281 | +0.150 | +153.53€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 303 | +0.097 | +84.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 303 | +0.097 | +84.93€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1577 | -0.019 | -32.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1577 | -0.019 | -32.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 306 | -0.003 | +8.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 306 | -0.003 | +8.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 272 | -0.025 | -2.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 272 | -0.025 | -2.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 405 | -0.048 | -35.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 405 | -0.048 | -35.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 337 | +0.002 | -3.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 337 | +0.002 | -3.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 257 | -0.010 | -0.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 257 | -0.010 | -0.17€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 937 | -0.074 | -50.60€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 436 | -0.112 | -80.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 340 | -0.140 | -67.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 329 | -0.032 | +23.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 238 | -0.021 | +25.94€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 91 | -0.059 | -2.46€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 172 | -0.058 | +6.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 141 | -0.066 | +2.00€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 31 | -0.015 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 719 | -0.087 | -39.93€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 218 | -0.032 | -10.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1175 | -0.206 | -70.86€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 458 | -0.209 | -43.58€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 401 | -0.212 | -43.35€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 400 | -0.206 | -31.19€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 352 | -0.217 | -38.20€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 48 | -0.120 | +7.01€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 317 | -0.199 | +3.91€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 296 | -0.195 | +1.79€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 21 | -0.239 | +2.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1049 | -0.210 | -79.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 126 | -0.172 | +8.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 462 | +0.397 | +440.30€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 69 | +0.162 | +55.45€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 69 | +0.162 | +55.45€ | 0 | 2 |
| ✅ RESOLUTION_SNIPER#ETH | 110 | +0.366 | +102.82€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 110 | +0.366 | +102.82€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 283 | +0.461 | +282.03€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 283 | +0.461 | +282.03€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 462 | +0.397 | +440.30€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 756 | +0.030 | +46.26€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 756 | +0.030 | +46.26€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 306 | +0.019 | +2.32€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 306 | +0.019 | +2.32€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 63 | -0.008 | -1.05€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 63 | -0.008 | -1.05€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 77 | -0.006 | +1.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 77 | -0.006 | +1.97€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 310 | +0.058 | +43.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 310 | +0.058 | +43.02€ | 0 | 5 |
| ✅ STREAK_FADE_5M | 3444 | -0.021 | -133.76€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3444 | -0.021 | -133.76€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1059 | -0.020 | -35.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1059 | -0.020 | -35.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 592 | -0.027 | -26.04€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 592 | -0.027 | -26.04€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 165 | -0.039 | -13.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 165 | -0.039 | -13.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1628 | -0.018 | -58.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1628 | -0.018 | -58.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 103 | -0.052 | -9.27€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 103 | -0.052 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 60 | -0.016 | -4.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 60 | -0.016 | -4.20€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11125 | +0.016 | +84.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11125 | +0.016 | +84.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2831 | +0.020 | +29.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2831 | +0.020 | +29.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2909 | +0.017 | +33.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2909 | +0.017 | +33.83€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2894 | +0.009 | -1.92€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2894 | +0.009 | -1.92€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2491 | +0.016 | +23.12€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2491 | +0.016 | +23.12€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10117 | +0.013 | -53.23€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10117 | +0.013 | -53.23€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4151 | +0.018 | -7.33€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4151 | +0.018 | -7.33€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3620 | +0.010 | -29.23€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3620 | +0.010 | -29.23€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2346 | +0.008 | -16.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2346 | +0.008 | -16.68€ | 1 | 0 |
| ✅ UPDOWN_GBM | 80431 | +0.054 | +7171.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 19948 | +0.083 | +4341.41€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2567 | +0.004 | +26.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 52858 | +0.051 | +2712.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4771 | +0.007 | +93.11€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 17707 | +0.056 | +1526.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2630 | +0.089 | +633.90€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 700 | +0.009 | +11.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 12140 | +0.062 | +814.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2133 | +0.004 | +63.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 104 | -0.066 | +3.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8673 | +0.070 | +918.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7040 | +0.054 | +309.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 18742 | +0.046 | +1233.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4781 | +0.068 | +708.15€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 679 | +0.007 | +16.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 11499 | +0.045 | +487.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1687 | +0.010 | +18.88€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 96 | -0.102 | +2.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 17704 | +0.034 | +909.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5089 | +0.035 | +411.67€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 645 | -0.009 | +1.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10934 | +0.040 | +491.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 951 | +0.007 | +10.53€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 85 | -0.132 | -6.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10752 | +0.066 | +1509.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4317 | +0.104 | +1278.66€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6047 | +0.043 | +231.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 285 | -0.099 | -0.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 871 | +0.365 | +319.34€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 871 | +0.365 | +319.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 446 | +0.362 | +152.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 446 | +0.362 | +152.66€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 425 | +0.366 | +166.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 425 | +0.366 | +166.68€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 20591 | -0.024 | +4843.59€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 20591 | -0.024 | +4843.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3706 | -0.112 | +143.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3706 | -0.112 | +143.98€ | 4 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2580 | +0.219 | +1687.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2580 | +0.219 | +1687.84€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5905 | -0.065 | +727.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5905 | -0.065 | +727.11€ | 5 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5734 | -0.065 | +1011.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5734 | -0.065 | +1011.40€ | 1 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 245 | +0.055 | +17.28€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 245 | +0.055 | +17.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 245 | +0.055 | +17.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 245 | +0.055 | +17.28€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1501 | +0.292 | +1287.40€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1501 | +0.292 | +1287.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 801 | +0.288 | +649.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 801 | +0.288 | +649.52€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 700 | +0.295 | +637.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 700 | +0.295 | +637.88€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 825 | -0.112 | -81.96€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 825 | -0.112 | -81.96€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 253 | -0.080 | -18.67€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 253 | -0.080 | -18.67€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 89 | -0.170 | -10.17€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 89 | -0.170 | -10.17€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 100 | -0.176 | -3.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 100 | -0.176 | -3.77€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 3773 | +0.304 | +1780.85€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1392 | +0.258 | +173.63€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1451 | +0.299 | +650.45€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 930 | +0.380 | +956.77€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.023 n=1003 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1003 IC=+0.023 PNL=+44.32€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 728 celda(s) pasan gate riguroso completo de 2733 evaluadas (n>=40) y 3787 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.035 < 0.08 — monitorear
  - _Datos_: n=5083 IC=+0.035 PNL=+410.64€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1435/15 IC=+0.299 PNL=+644.37€ | BTC: n=1376/15 IC=+0.258 PNL=+172.01€ | SOL: n=921/15 IC=+0.380 PNL=+943.72€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 31 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: alineada_con_outcome_prev IC=+0.140 n=817/60 | contraria IC=+0.192 n=853 | gap=-0.053 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=483, boost estimado=+0.017. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1686/40 IC=+0.010 PNL=+19.39€ | BTC#60min: n=2131/40 IC=+0.004 PNL=+63.80€ | SOL#60min: n=951/40 IC=+0.007 PNL=+10.53€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=581721 | tras_1loss IC=+0.096 n=441606 | tras_2loss IC=+0.066 n=178355/40 | gap=-0.018 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.193 > 0.08 con n=796 PNL=+583.53€
  - _Datos_: n=796 IC=+0.193 PNL=+583.53€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.169 > 0.08 con n=886 PNL=+505.98€
  - _Datos_: n=886 IC=+0.169 PNL=+505.98€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.157 > 0.08 con n=65 PNL=+31.12€
  - _Datos_: n=65 IC=+0.157 PNL=+31.12€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=3047 PNL=+1686.71€
  - _Datos_: n=3047 IC=+0.333 PNL=+1686.71€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=730 IC=+0.071 PNL=+81.25€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=730 IC=+0.071 PNL=+81.25€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=87 IC=+0.185 PNL=+58.89€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=87 IC=+0.185 PNL=+58.89€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 5/15 ops en el filtro definido (IC actual=+0.054 PNL=+5.10€)
  - _Datos_: n=5 IC=+0.054 PNL=+5.10€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 2/20 ops en el filtro definido (IC actual=+0.000 PNL=-0.08€)
  - _Datos_: n=2 IC=+0.000 PNL=-0.08€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=3207 IC=+0.010 PNL=+16.85€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3207 IC=+0.010 PNL=+16.85€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1561 IC=+0.000 PNL=+76.88€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1561 IC=+0.000 PNL=+76.88€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1003 IC=+0.023 PNL=+44.32€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1003 IC=+0.023 PNL=+44.32€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.173 > 0.1 con n=5080 PNL=+3091.24€
  - _Datos_: n=5080 IC=+0.173 PNL=+3091.24€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2626 IC=+0.089 PNL=+635.47€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2626 IC=+0.089 PNL=+635.47€

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
  - _Estado_: n=1033 IC=+0.037 PNL=+87.58€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1033 IC=+0.037 PNL=+87.58€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=130 IC=+0.008 PNL=+0.90€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=130 IC=+0.008 PNL=+0.90€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.276 n=172) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=172 IC=+0.276 PNL=+168.39€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.02 con n=1010 PNL=+419.28€
  - _Datos_: n=1010 IC=+0.123 PNL=+419.28€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=213 IC=-0.091 PNL=+19.65€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=213 IC=-0.091 PNL=+19.65€

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
  - _Estado_: n=31718 IC=+0.074 PNL=+4595.91€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=31718 IC=+0.074 PNL=+4595.91€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.141 < -0.1 con n=522 PNL=+61.44€
  - _Datos_: n=522 IC=-0.141 PNL=+61.44€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3165 IC=+0.069 PNL=+414.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3165 IC=+0.069 PNL=+414.99€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=150 IC=-0.099 PNL=+3.96€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=150 IC=-0.099 PNL=+3.96€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.1 con n=842 PNL=+229.17€
  - _Datos_: n=842 IC=+0.113 PNL=+229.17€

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
  - _Estado_: n=34007 IC=-0.133 PNL=+2815.93€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=34007 IC=-0.133 PNL=+2815.93€

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
  - _Estado_: n=3417 IC=+0.133 PNL=+2116.30€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3417 IC=+0.133 PNL=+2116.30€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=8281 IC=+0.053 PNL=+665.31€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8281 IC=+0.053 PNL=+665.31€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.095 > 0.08 con n=3644 PNL=+2015.28€
  - _Datos_: n=3644 IC=+0.095 PNL=+2015.28€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.223 < -0.1 con n=3532 PNL=-294.32€
  - _Datos_: n=3532 IC=-0.223 PNL=-294.32€

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

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=73 IC=+0.033 PNL=+10.66€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=73 IC=+0.033 PNL=+10.66€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1801) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1801 IC=+0.101 PNL=+391.92€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=579) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=579 IC=+0.410 PNL=+827.96€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=14690 IC=+0.186 PNL=-1503.25€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=14690 IC=+0.186 PNL=-1503.25€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.226 > 0.1 con n=235 PNL=+159.44€
  - _Datos_: n=235 IC=+0.226 PNL=+159.44€
