# Hipótesis automáticas — 2026-11-07 22:43 UTC
_Generado por shadow_postmortem.py sobre 1237801 resoluciones (PNL=+168635.14€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=693)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.198 (n=1011)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.505 (IC base=+0.129)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.183 (n=317)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 63.0 (IC base=+0.129)

- **PATRÓN** `banda_hit_calibrado` > `0.6133` → IC=+0.242 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6133 (IC base=+0.129)

- **PATRÓN** `banda_z` > `8.626` → IC=+0.202 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.626 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.129 (n=683)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 12.0 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1036)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.129)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.605` → IC=-0.301 (n=164)

  - _Acción_: SKIP cuando `py_entrada` > 0.605
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=494)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.196 (n=876)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.132)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.186 (n=275)

  - _Acción_: Kelly boost +0.93€ cuando `n_total_lado` > 66.0 (IC base=+0.132)

- **PATRÓN** `banda_hit_calibrado` > `0.8129` → IC=+0.273 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8129 (IC base=+0.132)

- **PATRÓN** `banda_z` > `8.976` → IC=+0.209 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.976 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.140 (n=742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 8.0 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=936)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.132)

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
- **FILTRO** `ballenas_wallet_edge_medio` < `2.833` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `ballenas_wallet_edge_medio` < 2.833
  - _Potencial_: sin este filtro IC_bueno=+0.375 (n=6)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.495 (IC base=+0.162)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 26.0 (IC base=+0.162)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.162)

- **PATRÓN** `banda_hit_calibrado` > `0.6068` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `banda_hit_calibrado` > 0.6068 (IC base=+0.162)

- **PATRÓN** `banda_z` > `2.495` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.495 (IC base=+0.162)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.729` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `ballenas_wallet_edge_medio` > 0.729 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.269 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 7.0 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `2453.7234` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2453.7234 (IC base=+0.162)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `133.23` → IC=-0.221 (n=11569)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.23
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=34707)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.3` → IC=-0.258 (n=1190)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.3
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=3573)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.68` → IC=-0.295 (n=1199)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.68
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3603)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `117.61` → IC=-0.166 (n=3156)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.61
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=9474)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `154.67` → IC=-0.239 (n=3131)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 154.67
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=9395)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `129.19` → IC=-0.263 (n=2192)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 129.19
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=6576)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=26785)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `8394.4376` → IC=+0.160 (n=2284)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 8394.4376 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=22981)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=27844)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.223 (n=21084)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=8137)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6659.2597` → IC=+0.147 (n=3141)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 6659.2597 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.184 (n=2086)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=2677)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `9413.2764` → IC=+0.181 (n=1862)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9413.2764 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=2128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2727)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `16078.4757` → IC=+0.184 (n=704)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16078.4757 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=2138)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.171 (n=582)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=1369)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.167 (n=4858)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 6.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.168 (n=4328)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.376 (n=1650)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.214 (n=2318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.330 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=2691)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.148 (n=1115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.256 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.256 (n=935)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.421 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=1401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=721)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `950.557` → IC=-0.131 (n=155)

  - _Acción_: SKIP cuando `libro_liquidez` < 950.557
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=316)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.160 (n=457)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.55 (IC base=+0.047)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.243 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=151)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.263 (n=167)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=23029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=19453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.227 (n=9593)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.179 (n=4441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.174 (n=5225)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 18.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.182 (n=5294)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.74 (IC base=+0.174)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.213 (n=3057)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.215 (n=2033)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.252 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.210)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=5147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=4367)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=5319)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=4021)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.256 (n=4353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.250 (n=3688)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.365 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.249)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=5066)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=3768)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.428 (n=833)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `3177.3107` → IC=+0.437 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3177.3107 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.450 (n=256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.457 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `12430.0394` → IC=+0.446 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12430.0394 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.430 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=371)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4712.9023` → IC=+0.436 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4712.9023 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.401 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.398)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.404 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.398)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.413 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.398)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `14.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=35)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

- **FILTRO** `libro_liquidez` < `6112.397` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `libro_liquidez` < 6112.397
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=17)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.209 (n=25931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=30390)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=4502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=9590)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=13755)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=6262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=4288)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.192 (n=4451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.198 (n=10684)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.227 (n=4229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=4804)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.268 (n=4222)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `3176.5987` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3176.5987
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=4294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.257 (n=4408)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=5026)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=4974)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=5235)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=10821)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=11245)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.49` → IC=+0.137 (n=13159)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.49 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5278)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.142 (n=5086)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6591)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.61` → IC=+0.142 (n=4975)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.61 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=5543)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.136 (n=6851)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.23` → IC=+0.139 (n=5047)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.23 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.306 (n=1341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.283 (n=902)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.367 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=955)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.396 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.298 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.362 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.341)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.430 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.341)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.372 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.341)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.444 (n=913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=427)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.436 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.432 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.439 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.433)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.466 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.447)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.449 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.447)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.447)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.448 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.447)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.419 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.417 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.406)

- **PATRÓN** `libro_liquidez` > `779.6536` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 779.6536 (IC base=+0.406)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.265 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=67)

- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.242 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=69)

- **FILTRO** `libro_liquidez` < `1798.9075` → IC=-0.233 (n=99)

  - _Acción_: SKIP cuando `libro_liquidez` < 1798.9075
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.265 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=67)

- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.242 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=69)

- **FILTRO** `libro_liquidez` < `1798.9075` → IC=-0.233 (n=99)

  - _Acción_: SKIP cuando `libro_liquidez` < 1798.9075
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4757` → IC=+0.139 (n=16991)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4757 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=17196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=11817)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9781` → IC=+0.246 (n=5666)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9781 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8003` → IC=+0.282 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8003 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.517` → IC=+0.184 (n=8490)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.517 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6249` → IC=+0.264 (n=5049)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6249 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.250 (n=1753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7407` → IC=+0.235 (n=4066)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7407 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=8468)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.122 (n=10601)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0061 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.5654` → IC=+0.143 (n=21190)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5654 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.6171` → IC=+0.191 (n=1439)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6171 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.1628` → IC=+0.189 (n=8336)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.1628 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `0.6964` → IC=+0.196 (n=3787)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6964 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.229 (n=2125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` > `2.676` → IC=+0.209 (n=4873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.676 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.226 (n=14526)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.081)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.363` → IC=+0.212 (n=3633)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.363 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=1767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2433)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9865` → IC=+0.279 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9865 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.523` → IC=+0.279 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.523 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.266 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4359` → IC=+0.214 (n=3480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4359 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=3993)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.225 (n=2223)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.243 (n=3179)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.241 (n=1444)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.0891` → IC=+0.279 (n=1060)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0891 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=1185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=1466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.559` → IC=+0.258 (n=3179)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.559 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0943` → IC=+0.245 (n=2874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0943 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2878` → IC=+0.251 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2878 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4457` → IC=+0.245 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4457 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.8558` → IC=+0.244 (n=2018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8558 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=3649)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1785.4165` → IC=+0.246 (n=2118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1785.4165 (IC base=+0.241)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.229 (n=2672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.0811` → IC=+0.259 (n=1011)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0811 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.226 (n=2152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9085` → IC=+0.260 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9085 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1859` → IC=+0.234 (n=1397)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1859 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.336` → IC=+0.224 (n=2993)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.336 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.964` → IC=+0.265 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.964 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.2256` → IC=+0.224 (n=3032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2256 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.228 (n=3032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.269 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.4011` → IC=+0.223 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4011 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4315` → IC=+0.254 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4315 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.151 (n=3227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0064 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0773` → IC=+0.152 (n=1076)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0773 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.144 (n=2299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.5745` → IC=+0.175 (n=2839)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.5745 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.944` → IC=+0.136 (n=2947)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.944 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.0544` → IC=+0.137 (n=2839)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.0544 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.153 (n=1311)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.138 (n=3101)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=4186)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.167 (n=1351)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 204.0 (IC base=+0.128)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.213 (n=1743)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=3441)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.041` → IC=+0.278 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.041 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.197 (n=3443)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.3525` → IC=+0.223 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3525 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.7278` → IC=+0.214 (n=1701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7278 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=4647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2029.82` → IC=+0.204 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2029.82 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.226 (n=3108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1751` → IC=+0.236 (n=1554)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1751 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=1599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.0426` → IC=+0.271 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0426 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.915` → IC=+0.263 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.915 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.253 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.7646` → IC=+0.221 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7646 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.1568` → IC=+0.227 (n=2261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1568 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1786)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1909.982` → IC=+0.226 (n=1601)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1909.982 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.222 (n=3344)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.219)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.165 (n=195)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=4632)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.149 (n=651)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0039 (IC base=+0.056)

- **PATRÓN** `ibs_20min` > `0.9435` → IC=+0.232 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9435 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.340 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` < `0.5452` → IC=+0.333 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5452 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.069` → IC=+0.202 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.069 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` > `0.7027` → IC=+0.339 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7027 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` < `0.1664` → IC=+0.336 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1664 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.333 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` < `1.4169` → IC=+0.343 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4169 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.2694` → IC=+0.337 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2694 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.338 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.0909` → IC=+0.186 (n=1207)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.0909 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.3371` → IC=+0.159 (n=593)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3371 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` < `0.1397` → IC=+0.150 (n=2147)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1397 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.160 (n=1525)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8331 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.206 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.7746` → IC=+0.152 (n=1468)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.7746 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `1.5127` → IC=+0.152 (n=1966)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5127 (IC base=+0.049)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=728)

- **FILTRO** `ibs_20min` < `0.2647` → IC=-0.168 (n=215)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2647
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=649)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.132 (n=4545)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=2241)

- **FILTRO** `sigma_ewma_delta_pct` > `8.314` → IC=-0.224 (n=729)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.314
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=6057)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.178 (n=296)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.75 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` > `0.9668` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9668 (IC base=+0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.026` → IC=+0.157 (n=202)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 5.026 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` > `0.6262` → IC=+0.281 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6262 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` < `0.0797` → IC=+0.282 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0797 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` < `2.4484` → IC=+0.279 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4484 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.5387` → IC=+0.265 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5387 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.273 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.017)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.156 (n=2241)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.2 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.2197` → IC=+0.286 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2197 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.6968` → IC=+0.302 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6968 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.300 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.4729` → IC=+0.302 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4729 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7818` → IC=-0.153 (n=3430)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7818
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=1768)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.167 (n=1146)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=4052)

- **FILTRO** `ibs_20min` > `0.7432` → IC=-0.195 (n=1812)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7432
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=5437)

- **PATRÓN** `ibs_20min` > `0.7818` → IC=+0.123 (n=1768)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.7818 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `1.0308` → IC=+0.359 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0308 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1852` → IC=+0.301 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1852 (IC base=-0.059)

- **PATRÓN** `volumen_regimen` > `0.7047` → IC=+0.317 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7047 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` < `0.1068` → IC=+0.305 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1068 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.169` → IC=+0.304 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.169 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.5853` → IC=+0.307 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5853 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.5272` → IC=+0.325 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5272 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `0.8119` → IC=+0.277 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8119 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` < `0.2233` → IC=+0.263 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2233 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` < `0.6419` → IC=+0.272 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6419 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `1.0635` → IC=+0.283 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0635 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.1065` → IC=+0.282 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1065 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `2.1776` → IC=+0.266 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1776 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.270 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.198 (n=7351)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0106 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.9708` → IC=+0.313 (n=7344)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9708 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.6752` → IC=+0.299 (n=2091)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6752 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.495` → IC=+0.167 (n=9866)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.495 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `0.6927` → IC=+0.276 (n=7224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6927 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.292 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.6493` → IC=+0.285 (n=4265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6493 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.308 (n=12424)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.089)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.158 (n=7087)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.642` → IC=+0.154 (n=21237)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.642 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.2566` → IC=+0.278 (n=7133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2566 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `0.6993` → IC=+0.280 (n=3068)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6993 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` > `1.193` → IC=+0.278 (n=2325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.193 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.326 (n=1549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` < `1.4543` → IC=+0.303 (n=3424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4543 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` > `2.2801` → IC=+0.300 (n=4654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2801 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.308 (n=10241)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 73.0 (IC base=+0.081)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8018` → IC=-0.125 (n=3938)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8018
  - _Potencial_: sin este filtro IC_bueno=+0.296 (n=2029)

- **FILTRO** `ibs_20min` > `0.7197` → IC=-0.233 (n=1308)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7197
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=3928)

- **FILTRO** `sigma_ewma_delta_pct` > `4.138` → IC=-0.231 (n=1126)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.138
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=4110)

- **PATRÓN** `ibs_20min` > `0.9348` → IC=+0.336 (n=1492)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9348 (IC base=+0.018)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.0` → IC=+0.189 (n=1995)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.0 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.327 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4466` → IC=+0.280 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4466 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` > `2.242` → IC=+0.301 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.242 (IC base=+0.018)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.316 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.018)

- **PATRÓN** `ibs_20min` < `0.1726` → IC=+0.165 (n=1310)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1726 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1515` → IC=+0.400 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1515 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4225` → IC=+0.424 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4225 (IC base=-0.025)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.397 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.025)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.3003` → IC=+0.225 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3003 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `1.1952` → IC=+0.207 (n=2145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1952 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.214 (n=1916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6949 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.245 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.417` → IC=+0.230 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.417 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `2.4477` → IC=+0.208 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4477 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.243 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 263.0 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.1336` → IC=+0.254 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1336 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.6195` → IC=+0.250 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6195 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.303 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5263` → IC=+0.255 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5263 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1438` → IC=+0.259 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1438 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.265 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 212.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.319 (n=2076)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.291 (n=3112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.607` → IC=+0.303 (n=2072)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.607 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.295 (n=2731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `1.6039` → IC=+0.289 (n=3020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6039 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=3728)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2029.4984` → IC=+0.297 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2029.4984 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.307 (n=1879)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.323 (n=2509)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.304)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.323 (n=1233)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.304)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.326 (n=1080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.306 (n=1262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.304)

- **PATRÓN** `ibs_20min` > `0.1401` → IC=+0.316 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1401 (IC base=+0.304)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.221` → IC=+0.312 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.221 (IC base=+0.304)

- **PATRÓN** `volumen_pendiente_norm` < `0.1993` → IC=+0.305 (n=2756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1993 (IC base=+0.304)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.313 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` < `1.594` → IC=+0.305 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.594 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` > `2.7268` → IC=+0.320 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7268 (IC base=+0.304)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.307 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.304)

- **PATRÓN** `libro_liquidez` > `1911.7298` → IC=+0.314 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.7298 (IC base=+0.304)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.311 (n=2385)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.304)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7266` → IC=-0.181 (n=1379)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7266
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=4138)

- **PATRÓN** `ibs_20min` > `0.8492` → IC=+0.159 (n=1351)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.8492 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.144` → IC=+0.235 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.144 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.36` → IC=+0.233 (n=1907)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.36 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1593` → IC=+0.233 (n=1947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1593 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6723` → IC=+0.231 (n=1739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6723 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1619` → IC=+0.235 (n=2043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1619 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.0762` → IC=+0.236 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0762 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4598` → IC=+0.237 (n=1886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4598 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.5053` → IC=+0.232 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5053 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.253 (n=1926)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.7339` → IC=+0.253 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7339 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` < `0.3536` → IC=+0.250 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3536 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `1.1965` → IC=+0.254 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1965 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.318 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.7888` → IC=+0.284 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7888 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.426` → IC=+0.275 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.426 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.279 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7429` → IC=-0.243 (n=2283)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2286)

- **FILTRO** `ibs_20min` > `0.6226` → IC=-0.228 (n=1087)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6226
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=3263)

- **FILTRO** `sigma_ewma_delta_pct` > `8.282` → IC=-0.253 (n=496)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.282
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=3854)

- **PATRÓN** `ibs_20min` > `0.7429` → IC=+0.312 (n=2286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7429 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `1.0473` → IC=+0.356 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0473 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.463` → IC=+0.152 (n=1853)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 2.463 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8458` → IC=+0.341 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8458 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.6986` → IC=+0.334 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6986 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.1567` → IC=+0.334 (n=1725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1567 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.364 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.362 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.351 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.6226` → IC=+0.149 (n=3263)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.6226 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.3052` → IC=+0.261 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3052 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.013` → IC=+0.128 (n=3069)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.013 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.6916` → IC=+0.281 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6916 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.282 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.8044` → IC=+0.275 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8044 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.283 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.055)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.359 (n=2081)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.344 (n=2331)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` > `0.2128` → IC=+0.339 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2128 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.806` → IC=+0.333 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.806 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `0.8706` → IC=+0.334 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8706 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.347 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `1.4313` → IC=+0.327 (n=2242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4313 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `2979.0544` → IC=+0.327 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2979.0544 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.344 (n=2086)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.315)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.348 (n=1654)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.317)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.323 (n=1260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.317)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.317)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.336 (n=2480)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.317)

- **PATRÓN** `dist_vwap_pct` < `0.2412` → IC=+0.322 (n=2402)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2412 (IC base=+0.317)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.64` → IC=+0.331 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.64 (IC base=+0.317)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.321 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.317)

- **PATRÓN** `volumen_regimen` > `1.2113` → IC=+0.346 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2113 (IC base=+0.317)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.363 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.317)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.324 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.317)

- **PATRÓN** `volumen_spike_ratio` > `2.1375` → IC=+0.317 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1375 (IC base=+0.317)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.224 (n=5486)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.1219` → IC=+0.191 (n=7235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1219 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=17069)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.5386` → IC=+0.231 (n=16443)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5386 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.1626` → IC=+0.206 (n=6348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1626 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.827` → IC=+0.259 (n=3203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.827 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.1825` → IC=+0.155 (n=10948)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1825 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6256` → IC=+0.154 (n=10947)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6256 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.206 (n=2384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.6086` → IC=+0.189 (n=5330)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6086 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.193 (n=15371)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 88.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.192 (n=7107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0058 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0803` → IC=+0.221 (n=5365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0803 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=6100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5228` → IC=+0.239 (n=16094)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5228 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.1819` → IC=+0.176 (n=11631)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1819 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.585` → IC=+0.192 (n=2570)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.585 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.535` → IC=+0.189 (n=14318)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 2.535 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1823` → IC=+0.163 (n=11467)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1823 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.217 (n=2412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6319` → IC=+0.191 (n=5099)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6319 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.196 (n=15068)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 92.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.227 (n=907)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1042` → IC=+0.257 (n=1192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1042 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=2822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.230 (n=1836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.8117` → IC=+0.274 (n=2421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8117 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.531` → IC=+0.331 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.531 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.295 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.834` → IC=+0.224 (n=1722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.834 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4341` → IC=+0.228 (n=2582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4341 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=3001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.259 (n=2189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.0971` → IC=+0.309 (n=962)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0971 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.259 (n=2259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.260 (n=1038)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.0487` → IC=+0.299 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0487 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.257 (n=1919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.3015` → IC=+0.273 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3015 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4462` → IC=+0.275 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4462 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.7028` → IC=+0.258 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7028 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=2520)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1786.645` → IC=+0.261 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1786.645 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.254 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.199 (n=843)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0648` → IC=+0.177 (n=837)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0648 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.2615` → IC=+0.209 (n=2507)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2615 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1843` → IC=+0.212 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1843 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.726` → IC=+0.206 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.726 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6953` → IC=+0.139 (n=1103)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6953 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `1.0584` → IC=+0.136 (n=1137)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.0584 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.177 (n=391)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.5031` → IC=+0.141 (n=1084)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5031 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.4674` → IC=+0.148 (n=821)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.4674 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `401.0` → IC=+0.135 (n=2431)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 401.0 (IC base=+0.131)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.172 (n=2655)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0064 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.237` → IC=+0.169 (n=2335)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.237 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=1272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6098` → IC=+0.207 (n=2653)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6098 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.918` → IC=+0.173 (n=496)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 10.918 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.001` → IC=+0.151 (n=2314)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.001 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.2024` → IC=+0.159 (n=2653)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2024 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.0934` → IC=+0.148 (n=2296)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0934 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4531` → IC=+0.151 (n=2528)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4531 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `211.0` → IC=+0.184 (n=1082)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 211.0 (IC base=+0.146)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.232 (n=1266)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3908` → IC=+0.225 (n=2453)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3908 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.101` → IC=+0.304 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.101 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3532` → IC=+0.236 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3532 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7137` → IC=+0.227 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7137 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=3368)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1917.0236` → IC=+0.223 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.0236 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.249 (n=2150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.4145` → IC=+0.261 (n=2150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4145 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.282 (n=942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0333` → IC=+0.291 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0333 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.089` → IC=+0.282 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.089 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3581` → IC=+0.285 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3581 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7682` → IC=+0.238 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7682 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.1823` → IC=+0.249 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1823 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1903.1828` → IC=+0.251 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1903.1828 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.242 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.207 (n=903)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0783` → IC=+0.184 (n=901)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0783 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.2532` → IC=+0.192 (n=2702)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2532 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.139` → IC=+0.186 (n=1580)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.139 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.337` → IC=+0.197 (n=466)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.337 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8447` → IC=+0.137 (n=1802)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8447 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `1.1831` → IC=+0.131 (n=901)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.1831 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.170 (n=407)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.8237` → IC=+0.130 (n=1764)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.8237 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.5248` → IC=+0.148 (n=882)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.5248 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6882.1647` → IC=+0.196 (n=1225)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6882.1647 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.135 (n=2643)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 128.0 (IC base=+0.131)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.165 (n=2532)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0066 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3945` → IC=+0.145 (n=2877)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3945 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6746` → IC=+0.186 (n=2877)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6746 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.157 (n=2896)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.274` → IC=+0.141 (n=689)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.274 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6847` → IC=+0.160 (n=1266)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6847 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.177 (n=429)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.8035` → IC=+0.132 (n=1818)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8035 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.5324` → IC=+0.131 (n=909)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.5324 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `6325.8714` → IC=+0.190 (n=1304)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6325.8714 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.149 (n=905)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 49.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.166 (n=1373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0112 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.157 (n=1439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.4737` → IC=+0.206 (n=3012)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4737 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.1964` → IC=+0.190 (n=1648)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1964 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.063` → IC=+0.286 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.063 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1741` → IC=+0.133 (n=3010)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1741 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.7037` → IC=+0.122 (n=2690)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.7037 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.127 (n=3067)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4373` → IC=+0.132 (n=974)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4373 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=3149)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2664.3504` → IC=+0.196 (n=1365)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2664.3504 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.145 (n=1278)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 20.0 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.141 (n=3145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0118 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.111` → IC=+0.162 (n=1048)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.111 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.218 (n=3145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.65 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2118` → IC=+0.143 (n=3065)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2118 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.277` → IC=+0.138 (n=2776)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.277 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.127 (n=3143)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.1753 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2739` → IC=+0.139 (n=430)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2739 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.432` → IC=+0.131 (n=989)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.432 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.4253` → IC=+0.127 (n=989)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4253 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2552.1243` → IC=+0.182 (n=1424)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2552.1243 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.124 (n=2947)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 45.0 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.248 (n=2730)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1665` → IC=+0.239 (n=1201)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1665 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=2838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2461)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.257 (n=2731)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1817` → IC=+0.234 (n=1701)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1817 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.8106` → IC=+0.226 (n=2808)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8106 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.577` → IC=+0.254 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.577 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6235` → IC=+0.234 (n=2730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6235 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.267 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4718` → IC=+0.228 (n=2662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4718 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.815` → IC=+0.233 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.815 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2843.5154` → IC=+0.231 (n=1238)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2843.5154 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0129` → IC=+0.241 (n=1234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0129 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0229` → IC=+0.247 (n=1268)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0229 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.576` → IC=+0.247 (n=2797)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.576 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=1246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.264 (n=2809)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `1.1415` → IC=+0.259 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1415 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.038` → IC=+0.266 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.038 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `0.8653` → IC=+0.242 (n=1866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8653 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `0.6409` → IC=+0.242 (n=2796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6409 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.289 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `2.5274` → IC=+0.236 (n=2632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5274 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.239 (n=2631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.239)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.210 (n=1416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.1325` → IC=+0.175 (n=1868)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.1325 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=4450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.31` → IC=+0.198 (n=4243)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.31 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.2206` → IC=+0.185 (n=1656)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.2206 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.638` → IC=+0.211 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.638 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.171 (n=2578)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8616 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `1.1931` → IC=+0.171 (n=1289)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1931 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.0982` → IC=+0.173 (n=1520)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0982 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.5283` → IC=+0.167 (n=1819)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5283 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.8117` → IC=+0.163 (n=2756)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8117 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=4752)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `8031.121` → IC=+0.184 (n=1924)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 8031.121 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.3856` → IC=+0.170 (n=3047)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.3856 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.137 (n=1955)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 25.0 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.195 (n=1127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0061 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.3283` → IC=+0.197 (n=1125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3283 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.213 (n=1016)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.2144` → IC=+0.212 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2144 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.3086` → IC=+0.213 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3086 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.949` → IC=+0.206 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.949 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.356` → IC=+0.179 (n=1183)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 6.356 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.192 (n=752)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8803 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.1499` → IC=+0.181 (n=1184)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1499 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.192 (n=443)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.1675` → IC=+0.195 (n=971)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.1675 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `15815.8495` → IC=+0.191 (n=510)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 15815.8495 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.165 (n=463)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0031 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.1965` → IC=+0.201 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1965 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.1604` → IC=+0.135 (n=362)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1604 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.179 (n=599)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 162.0 (IC base=+0.090)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.243 (n=581)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.2096` → IC=+0.169 (n=878)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.2096 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=1371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.8043` → IC=+0.263 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8043 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.821` → IC=+0.192 (n=222)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.821 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.882` → IC=+0.213 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.882 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.8313` → IC=+0.176 (n=877)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8313 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.156` → IC=+0.168 (n=438)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.156 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2192` → IC=+0.207 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2192 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.7833` → IC=+0.180 (n=864)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.7833 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `8278.9168` → IC=+0.174 (n=596)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 8278.9168 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.0901` → IC=+0.195 (n=428)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.0901 (IC base=+0.083)

- **PATRÓN** `libro_liquidez` > `5154.5272` → IC=+0.135 (n=856)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 5154.5272 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.121 (n=558)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 43.0 (IC base=+0.083)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.155 (n=468)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0073 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.168 (n=748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.4571` → IC=+0.183 (n=1064)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.4571 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.9447` → IC=+0.185 (n=182)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.9447 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.876` → IC=+0.229 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.876 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.0478` → IC=+0.135 (n=935)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.0478 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.7037` → IC=+0.139 (n=948)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.7037 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2259` → IC=+0.158 (n=194)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2259 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `2.4087` → IC=+0.132 (n=1026)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.4087 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=1115)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2731.8228` → IC=+0.167 (n=481)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2731.8228 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.3667` → IC=+0.182 (n=769)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.3667 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `2616.434` → IC=+0.151 (n=522)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2616.434 (IC base=+0.065)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0174` → IC=+0.241 (n=245)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0174 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=171)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.5524` → IC=+0.218 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5524 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.2223` → IC=+0.217 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2223 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.732` → IC=+0.215 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.732 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` > `1.1874` → IC=+0.268 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1874 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.1036` → IC=+0.206 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1036 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `1.8284` → IC=+0.219 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8284 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.5387` → IC=+0.205 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5387 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.203 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `3014.8723` → IC=+0.204 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3014.8723 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.161 (n=399)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0113 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.3039` → IC=+0.151 (n=267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3039 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.162 (n=353)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.5 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `1.2295` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2295 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.17` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.17 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.238` → IC=+0.147 (n=358)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.238 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.8805` → IC=+0.188 (n=267)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8805 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.1134` → IC=+0.162 (n=368)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.1134 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.5142` → IC=+0.208 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5142 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.6761` → IC=+0.162 (n=128)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.6761 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.159 (n=382)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 20.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.231 (n=7172)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=22457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4318` → IC=+0.228 (n=21515)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4318 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8868` → IC=+0.213 (n=2591)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8868 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.967` → IC=+0.255 (n=5265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.967 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2166` → IC=+0.159 (n=14479)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2166 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.241` → IC=+0.207 (n=3872)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.241 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6185` → IC=+0.194 (n=6999)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6185 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.202 (n=20170)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 104.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.198 (n=8678)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.006 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.201 (n=6573)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.4812` → IC=+0.197 (n=19712)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4812 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=7394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.243 (n=19709)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5909 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.1794` → IC=+0.175 (n=12355)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1794 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.454` → IC=+0.195 (n=2671)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.454 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.4` → IC=+0.198 (n=19196)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 3.4 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.702` → IC=+0.174 (n=5827)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.702 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.292` → IC=+0.251 (n=2709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.292 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.6265` → IC=+0.205 (n=6280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6265 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.209 (n=18607)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.193)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=2322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.9737` → IC=+0.323 (n=1565)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9737 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.559` → IC=+0.337 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.559 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2325` → IC=+0.298 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2325 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.2896` → IC=+0.241 (n=1510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2896 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.251 (n=3779)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2047.52` → IC=+0.237 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2047.52 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.258 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.269 (n=3059)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1215` → IC=+0.293 (n=1344)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1215 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=2819)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.268 (n=2767)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.5408` → IC=+0.284 (n=3055)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5408 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.270 (n=2776)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.283 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.5607` → IC=+0.268 (n=1289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5607 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.6495` → IC=+0.276 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6495 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.272 (n=2127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `1785.195` → IC=+0.274 (n=2036)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1785.195 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.275 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.164 (n=2350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0045 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.149 (n=1174)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=3670)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.1994` → IC=+0.188 (n=3519)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.1994 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.1804` → IC=+0.192 (n=1525)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1804 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.209` → IC=+0.164 (n=563)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.209 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6358` → IC=+0.154 (n=1175)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6358 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0691` → IC=+0.140 (n=1596)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.0691 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2705` → IC=+0.178 (n=498)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2705 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.155` → IC=+0.140 (n=3040)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.155 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5154` → IC=+0.140 (n=3086)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.5154 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `303.0` → IC=+0.150 (n=2265)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 303.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.162 (n=3012)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0064 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.169 (n=1004)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=1110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6803` → IC=+0.185 (n=3012)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6803 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.001` → IC=+0.138 (n=2724)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.001 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.0503` → IC=+0.149 (n=2650)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0503 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.219` → IC=+0.193 (n=559)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.219 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4215` → IC=+0.141 (n=2902)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4215 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7688` → IC=+0.141 (n=1936)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.7688 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=3911)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `226.0` → IC=+0.152 (n=946)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 226.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.251 (n=1195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3758)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=3208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.045` → IC=+0.325 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.045 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.229 (n=3208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.35` → IC=+0.227 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.35 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.7319` → IC=+0.242 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7319 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=4325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2029.9632` → IC=+0.239 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2029.9632 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.250 (n=3005)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1776` → IC=+0.266 (n=1502)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1776 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.0571` → IC=+0.303 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0571 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.175` → IC=+0.304 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.175 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.3489` → IC=+0.303 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3489 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.1731` → IC=+0.255 (n=2189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1731 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.250 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1907.66` → IC=+0.256 (n=1548)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1907.66 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.248 (n=2865)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.243)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.193 (n=1242)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0037 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4312` → IC=+0.144 (n=3721)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4312 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=3865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.8899` → IC=+0.272 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8899 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.1958` → IC=+0.167 (n=1707)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1958 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.963` → IC=+0.156 (n=1653)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.963 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8602` → IC=+0.149 (n=2480)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8602 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2329` → IC=+0.183 (n=661)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2329 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5194` → IC=+0.149 (n=1600)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5194 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.178` → IC=+0.143 (n=1648)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.178 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `5518.7722` → IC=+0.226 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5518.7722 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.143 (n=2411)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 89.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.168 (n=2746)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0067 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.4359` → IC=+0.153 (n=3116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4359 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=1153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.5803` → IC=+0.210 (n=2742)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5803 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1525` → IC=+0.157 (n=2902)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1525 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.853` → IC=+0.151 (n=460)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 10.853 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.043` → IC=+0.147 (n=2715)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.043 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.6887` → IC=+0.161 (n=1371)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6887 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.211 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.2086` → IC=+0.145 (n=2647)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.2086 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.5327` → IC=+0.151 (n=2687)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.5327 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `6365.6846` → IC=+0.217 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6365.6846 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.154 (n=2047)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 92.0 (IC base=+0.142)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.148 (n=1708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0112 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=2670)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4324` → IC=+0.191 (n=3769)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4324 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.011` → IC=+0.201 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.011 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.289` → IC=+0.268 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.289 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2155` → IC=+0.125 (n=3768)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.2155 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1012` → IC=+0.122 (n=3578)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1012 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `2.491` → IC=+0.122 (n=3681)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.491 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=3957)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2718.2425` → IC=+0.241 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2718.2425 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.152 (n=3126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0108 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.1364` → IC=+0.153 (n=1183)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1364 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.214 (n=3570)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.2173` → IC=+0.142 (n=3200)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2173 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.054` → IC=+0.149 (n=3436)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.054 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.6376` → IC=+0.153 (n=1184)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6376 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.177 (n=618)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4337` → IC=+0.155 (n=1122)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4337 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2624.3797` → IC=+0.210 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2624.3797 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.139 (n=3014)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 43.0 (IC base=+0.127)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.259 (n=3475)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=3635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.243 (n=2318)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `0.615` → IC=+0.272 (n=3104)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.615 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.196` → IC=+0.253 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.196 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.188` → IC=+0.286 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.188 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `1.2203` → IC=+0.240 (n=3474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2203 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.242 (n=3473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2382` → IC=+0.259 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2382 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.4962` → IC=+0.258 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4962 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `2971.3853` → IC=+0.242 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2971.3853 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0259` → IC=+0.267 (n=1189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0259 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.247 (n=3368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.5207` → IC=+0.273 (n=3567)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5207 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` < `0.2194` → IC=+0.248 (n=3374)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2194 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.163` → IC=+0.280 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.163 (IC base=+0.242)

- **PATRÓN** `volumen_regimen` < `0.7156` → IC=+0.242 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7156 (IC base=+0.242)

- **PATRÓN** `volumen_regimen` > `1.2193` → IC=+0.263 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2193 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.300 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.4345` → IC=+0.245 (n=3357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4345 (IC base=+0.242)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=5784)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.245 (n=1987)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.5048` → IC=+0.227 (n=5958)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5048 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=2156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9351` → IC=+0.256 (n=1986)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9351 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.4291` → IC=+0.221 (n=4339)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4291 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.556` → IC=+0.226 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.556 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `0.7086` → IC=+0.229 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7086 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.8836` → IC=+0.219 (n=2929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8836 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.219 (n=5559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.224 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `2.2564` → IC=+0.222 (n=5162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2564 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.224 (n=4646)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `2881.4571` → IC=+0.223 (n=5322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2881.4571 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.237 (n=1450)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.211 (n=4350)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.214 (n=1922)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.73` → IC=+0.207 (n=4350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.73 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6573` → IC=+0.210 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6573 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.772` → IC=+0.210 (n=3905)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.772 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.095` → IC=+0.205 (n=3651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.095 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.200 (n=4006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.201 (n=1941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.5312` → IC=+0.203 (n=1887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5312 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.1857` → IC=+0.206 (n=1944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1857 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=5784)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.218 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.199)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.276 (n=814)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.297 (n=309)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.279 (n=925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.8328` → IC=+0.278 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.8328 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` < `0.6679` → IC=+0.277 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6679 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.118` → IC=+0.300 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.118 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.271 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2212 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `0.8749` → IC=+0.288 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8749 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.351 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.276 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.1895` → IC=+0.269 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1895 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `12909.5134` → IC=+0.279 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12909.5134 (IC base=+0.269)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.263 (n=509)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.189 (n=1519)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3854 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.184 (n=565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.138` → IC=+0.197 (n=668)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.138 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.6955` → IC=+0.197 (n=140)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6955 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.315` → IC=+0.198 (n=1488)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 6.315 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.0915` → IC=+0.188 (n=1336)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.0915 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.195 (n=463)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.194 (n=504)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.1703` → IC=+0.180 (n=685)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.1703 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14605.0565` → IC=+0.179 (n=689)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 14605.0565 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `686.0` → IC=+0.188 (n=1473)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 686.0 (IC base=+0.176)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.225 (n=612)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.587` → IC=+0.211 (n=918)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.587 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.230 (n=424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.3929` → IC=+0.204 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3929 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.247 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.428` → IC=+0.250 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.428 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2054` → IC=+0.235 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2054 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `3.3851` → IC=+0.203 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.3851 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.8037` → IC=+0.208 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8037 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2777.94` → IC=+0.237 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2777.94 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.210 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.286 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.216` → IC=+0.258 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.216 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.971` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.971 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `2.3165` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3165 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.7721` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7721 (IC base=+0.228)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.218 (n=1629)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.4542` → IC=+0.212 (n=1628)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4542 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.5006` → IC=+0.216 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5006 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.8555` → IC=+0.206 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8555 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.3956` → IC=+0.214 (n=1631)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3956 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.521` → IC=+0.209 (n=1653)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.521 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.209 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `1.2249` → IC=+0.205 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2249 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.208 (n=1499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.1597` → IC=+0.214 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1597 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.241 (n=454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.484` → IC=+0.221 (n=1355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.484 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.210 (n=512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.218 (n=917)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.7445` → IC=+0.204 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7445 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.0937` → IC=+0.205 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0937 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.6221` → IC=+0.216 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6221 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.345` → IC=+0.205 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.345 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.6391` → IC=+0.227 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6391 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.228 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.1876` → IC=+0.207 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1876 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `6408.237` → IC=+0.206 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6408.237 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.202 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.201)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.224 (n=635)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.234 (n=668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.7666` → IC=+0.240 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7666 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.202` → IC=+0.223 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.202 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.247 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.207 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.0792` → IC=+0.203 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0792 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `2.1458` → IC=+0.205 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1458 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.4746` → IC=+0.203 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4746 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=1122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4323.865` → IC=+0.243 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4323.865 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.204 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.234 (n=464)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.5947` → IC=+0.236 (n=695)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5947 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.249 (n=480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.6522` → IC=+0.251 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6522 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.5279` → IC=+0.222 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5279 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.788` → IC=+0.234 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.788 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `0.7541` → IC=+0.227 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7541 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.2706` → IC=+0.227 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2706 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.0825` → IC=+0.235 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0825 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.588` → IC=+0.259 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.588 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `3788.9662` → IC=+0.235 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3788.9662 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.256 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.220)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.150 (n=715)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0038 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.184 (n=1380)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.75 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1457` → IC=+0.139 (n=1027)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1457 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.453` → IC=+0.145 (n=457)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 10.453 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.265 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.1463` → IC=+0.136 (n=385)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.1463 (IC base=+0.045)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.536` → IC=-0.125 (n=286)

  - _Acción_: SKIP cuando `ibs_20min` < 0.536
  - _Potencial_: sin este filtro IC_bueno=+0.166 (n=582)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.126 (n=600)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0052 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.536` → IC=+0.166 (n=582)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.536 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.165 (n=314)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.070)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.128 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0034 (IC base=+0.045)

- **PATRÓN** `ibs_20min` < `0.0755` → IC=+0.271 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0755 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2173` → IC=+0.164 (n=111)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2173 (IC base=+0.045)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.5448` → IC=-0.122 (n=292)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5448
  - _Potencial_: sin este filtro IC_bueno=+0.170 (n=595)

- **FILTRO** `ibs_20min` > `0.6879` → IC=-0.171 (n=150)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6879
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=451)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.125 (n=465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0052 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.5448` → IC=+0.170 (n=595)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.5448 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1269` → IC=+0.173 (n=328)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1269 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.677` → IC=+0.200 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.677 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.265 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.617` → IC=+0.209 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.617 (IC base=+0.019)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.195 (n=247)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 1.0 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.7189` → IC=+0.132 (n=172)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.7189 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.688` → IC=+0.142 (n=160)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 8.688 (IC base=+0.020)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.182 (n=281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0094 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.3437` → IC=+0.203 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3437 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.1874` → IC=+0.132 (n=373)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1874 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.887` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.887 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.0831` → IC=+0.174 (n=130)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.0831 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1535` → IC=+0.175 (n=112)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1535 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.4564` → IC=+0.125 (n=361)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4564 (IC base=+0.073)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0058` → IC=-0.242 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=185)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.338 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=291)

- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=353)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.309 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=176)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=307)

- **FILTRO** `sigma_ewma_delta_pct` > `9.697` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.697
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=299)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=206)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.280 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=60)

- **FILTRO** `ibs_20min` < `0.0048` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=81)

- **FILTRO** `volumen_regimen` < `0.89` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=81)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.257 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=74)

- **FILTRO** `ibs_20min` > `0.7502` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7502
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=97)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=110)

- **FILTRO** `volumen_spike_ratio` > `1.4782` → IC=-0.310 (n=56)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4782
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=57)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5857` → IC=-0.471 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5857
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=98)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.368 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=91)

- **FILTRO** `ibs_20min` > `0.681` → IC=-0.389 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.681
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=84)

- **FILTRO** `volumen_spike_ratio` > `2.0968` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.0968
  - _Potencial_: sin este filtro IC_bueno=-0.309 (n=61)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=69)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.298 (n=112)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0074` → IC=-0.322 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=88)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=113)

- **FILTRO** `volumen_pendiente_norm` > `0.1329` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1329
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=75)

- **FILTRO** `sigma_h` < `0.0107` → IC=-0.329 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **FILTRO** `sigma_ewma_delta_pct` > `2.412` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.412
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=32)

- **FILTRO** `volumen_regimen` < `0.9051` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9051
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=36)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=32)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.238 (n=227)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.192 (n=352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.6786` → IC=+0.178 (n=679)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6786 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.8076` → IC=+0.278 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8076 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.633` → IC=+0.153 (n=373)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.633 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.617` → IC=+0.143 (n=692)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 8.617 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.625` → IC=+0.181 (n=227)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.625 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.2094` → IC=+0.166 (n=638)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.2094 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.388` → IC=+0.189 (n=191)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.388 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.53` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 10.53 (IC base=+0.035)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7797` → IC=-0.133 (n=88)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7797
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=181)

- **PATRÓN** `ibs_20min` > `0.7797` → IC=+0.123 (n=181)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.7797 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.6135` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6135 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.215` → IC=+0.148 (n=382)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.215 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.348` → IC=+0.129 (n=87)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 11.348 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.125 (n=62)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` > `2.1083` → IC=+0.140 (n=159)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.1083 (IC base=+0.090)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.187` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.187
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=235)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.141 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0042 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.134 (n=99)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.127 (n=108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 8.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.7964` → IC=+0.158 (n=200)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.7964 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.0973` → IC=+0.152 (n=182)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.0973 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.502` → IC=+0.147 (n=233)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 9.502 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6249 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.187` → IC=+0.150 (n=235)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.187 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.769` → IC=+0.169 (n=131)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.769 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=191)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.578` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.578 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2839` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2839 (IC base=+0.014)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=126)

- **FILTRO** `volumen_spike_ratio` > `2.0334` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.0334
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=98)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.292 (n=181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.278 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.6973` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6973 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.354 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` < `0.5849` → IC=+0.293 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5849 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4721` → IC=+0.332 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4721 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.241)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.319 (n=103)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3975` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3975 (IC base=+0.332)

- **PATRÓN** `elapsed_s` > `207.7` → IC=+0.391 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.7 (IC base=+0.332)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.377 (n=79)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.332)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `1208.0` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1208.0 (IC base=+0.332)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.254)

- **PATRÓN** `elapsed_s` > `185.6` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.6 (IC base=+0.254)

- **PATRÓN** `elapsed_s` < `203.0` → IC=+0.262 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.0 (IC base=+0.254)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.305 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.294 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.254)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.319 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `1750.0` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1750.0 (IC base=+0.254)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.319 (n=103)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3975` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3975 (IC base=+0.332)

- **PATRÓN** `elapsed_s` > `207.7` → IC=+0.391 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.7 (IC base=+0.332)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.377 (n=79)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.332)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `1208.0` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1208.0 (IC base=+0.332)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.254)

- **PATRÓN** `elapsed_s` > `185.6` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.6 (IC base=+0.254)

- **PATRÓN** `elapsed_s` < `203.0` → IC=+0.262 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.0 (IC base=+0.254)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.305 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.294 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.254)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.319 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `1750.0` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1750.0 (IC base=+0.254)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1432)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.099)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1432)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.099)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=243)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=243)

- **FILTRO** `libro_liquidez` < `6868.5329` → IC=-0.149 (n=129)

  - _Acción_: SKIP cuando `libro_liquidez` < 6868.5329
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=130)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=699)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12112.4745` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `libro_liquidez` < 12112.4745
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=87)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4006.09` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `liq_usd_total` < 4006.09
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=28)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=38)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.052)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3899)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=137)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=94)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=124)

- **FILTRO** `ballena_activa_n` > `21.0` → IC=-0.160 (n=92)

  - _Acción_: SKIP cuando `ballena_activa_n` > 21.0
  - _Potencial_: sin este filtro IC_bueno=+0.265 (n=32)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.087)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.141 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=143)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=273)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.256)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.256)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1591)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1545)

- **FILTRO** `liq_usd_total` < `6520.36` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 6520.36
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=726)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=441)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=422)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.149 (n=186)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=974)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=974)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1190)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1190)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=271)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=271)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.146 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=333)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=381)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=297)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=391)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=391)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=236)

- **FILTRO** `libro_liquidez` < `659.869` → IC=-0.136 (n=138)

  - _Acción_: SKIP cuando `libro_liquidez` < 659.869
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=283)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=339)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=77)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.192 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=90)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.179 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=90)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=44)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.145 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=23)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.152 (n=231)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=654)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.134 (n=312)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.51 (IC base=-0.010)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.152 (n=159)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=332)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.123 (n=332)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=349)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.121 (n=328)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=388)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.169 (n=143)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=625)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=515)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=274)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.135 (n=113)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=346)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.139 (n=463)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=465)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7798)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1058)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.173 (n=7601)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=24309)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.174 (n=8091)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=24799)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.183 (n=1460)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=4437)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.148 (n=1952)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=3884)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.124 (n=2982)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.505 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.171 (n=1051)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=3412)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.179 (n=1156)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3482)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=1446)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4524)

- **PATRÓN** `ibs_20min` > `0.9635` → IC=+0.133 (n=2005)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.9635 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1752.6484` → IC=+0.123 (n=2005)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1752.6484 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.181 (n=1100)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=3594)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.159 (n=1466)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=4463)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2432)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2356)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3002)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3954)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.157 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=437)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.198 (n=336)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1053)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=356)

- **FILTRO** `ballena_activa_n` > `85.0` → IC=-0.186 (n=154)

  - _Acción_: SKIP cuando `ballena_activa_n` > 85.0
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=307)

- **FILTRO** `libro_liquidez` < `3209.4551` → IC=-0.179 (n=154)

  - _Acción_: SKIP cuando `libro_liquidez` < 3209.4551
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=315)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=968)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.191 (n=390)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=777)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=238)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=91)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 15.0 (IC base=+0.024)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=21677)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=48974)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=16850)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=53801)

- **FILTRO** `ibs_7min` < `0.2199` → IC=-0.232 (n=17659)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2199
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=52992)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=23217)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=47434)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.251 (n=20640)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=67872)

- **FILTRO** `ibs_7min` > `0.2832` → IC=-0.184 (n=22122)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2832
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=66390)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.155 (n=3042)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=9510)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.319 (n=3079)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=9473)

- **FILTRO** `ibs_7min` < `0.7105` → IC=-0.250 (n=4139)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7105
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=8413)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.152 (n=2762)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=9790)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3706)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=11594)

- **FILTRO** `ibs_7min` > `0.7754` → IC=-0.212 (n=3823)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7754
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=11477)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2823)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=8956)

- **FILTRO** `ibs_7min` < `0.7155` → IC=-0.208 (n=2943)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7155
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8836)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.198 (n=2938)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8841)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2756)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=9281)

- **FILTRO** `ibs_7min` > `0.2661` → IC=-0.196 (n=3008)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2661
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=9029)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.182 (n=3002)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9035)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.164 (n=2894)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9120)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.324 (n=2853)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=9161)

- **FILTRO** `ibs_7min` < `0.2868` → IC=-0.249 (n=3964)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2868
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=8050)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.200 (n=2448)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=9566)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.258 (n=3911)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=12286)

- **FILTRO** `ibs_7min` > `0.7326` → IC=-0.183 (n=4049)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7326
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=12148)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.260 (n=2824)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=8612)

- **FILTRO** `ibs_7min` < `0.7171` → IC=-0.194 (n=2858)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7171
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8578)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.187 (n=2805)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=8631)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=2753)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=9165)

- **FILTRO** `ibs_7min` > `0.2745` → IC=-0.176 (n=2979)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2745
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8939)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.170 (n=2919)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=8999)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=2668)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8677)

- **FILTRO** `ibs_7min` < `0.7037` → IC=-0.230 (n=3741)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7037
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=7604)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.216 (n=2818)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8527)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.197 (n=4144)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=12968)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=3696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=7829)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.307 (n=2724)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8801)

- **FILTRO** `ibs_7min` < `0.1667` → IC=-0.230 (n=2874)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1667
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8651)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=2577)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=8948)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=3697)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=12251)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.160 (n=301)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1007)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1293)

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
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=884)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.123 (n=221)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=333)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=450)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=98)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=671)

- **FILTRO** `libro_liquidez` < `3302.3462` → IC=-0.155 (n=192)

  - _Acción_: SKIP cuando `libro_liquidez` < 3302.3462
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=577)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=394)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4306` → IC=+0.152 (n=664)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4306 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.130 (n=750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `418.1326` → IC=+0.162 (n=489)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 418.1326 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3556.2094` → IC=+0.140 (n=664)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3556.2094 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.180 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 14.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `503.672` → IC=+0.150 (n=352)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 503.672 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `2520.4138` → IC=+0.239 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2520.4138 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.133 (n=167)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 6.0 (IC base=+0.132)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.160 (n=101)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=280)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4165` → IC=+0.183 (n=184)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio` |x|> 0.4165 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.173 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `498.2784` → IC=+0.163 (n=185)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 498.2784 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.180 (n=95)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 59.0 (IC base=+0.127)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.168 (n=251)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.84€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.176 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.143)

- **PATRÓN** `total_vol_5m` < `4632.142` → IC=+0.182 (n=168)

  - _Acción_: Kelly boost +0.91€ cuando `total_vol_5m` < 4632.142 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3698.2852` → IC=+0.163 (n=167)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3698.2852 (IC base=+0.143)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=201)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.094)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.4417` → IC=-0.272 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.4417
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=167)

- **FILTRO** `sigma_h` > `0.0054` → IC=-0.226 (n=411)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=412)

- **FILTRO** `T_h` > `129.6211` → IC=-0.189 (n=204)

  - _Acción_: SKIP cuando `T_h` > 129.6211
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=619)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.150 (n=272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0044 (IC base=-0.078)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `4.2538` → IC=-0.262 (n=61)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2538
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=185)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.277 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.032)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7112` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `pct_vs_K` |x|≤ 1.7112 (IC base=-0.032)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `251.7955` → IC=-0.210 (n=60)

  - _Acción_: SKIP cuando `T_h` < 251.7955
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0151` → IC=-0.225 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0151
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=118)

- **FILTRO** `T_h` < `66.0811` → IC=-0.198 (n=51)

  - _Acción_: SKIP cuando `T_h` < 66.0811
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=105)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` > `0.0096` → IC=-0.196 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0096
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0102` → IC=-0.237 (n=500)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.169 (n=258)

- **FILTRO** `T_h` > `70.1154` → IC=-0.225 (n=507)

  - _Acción_: SKIP cuando `T_h` > 70.1154
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=251)

- **FILTRO** `pct_vs_K` |x|> `3.0996` → IC=-0.407 (n=160)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0996
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=491)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.207 (n=186)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=63)

- **FILTRO** `sigma_h` > `0.0062` → IC=-0.277 (n=119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=120)

- **FILTRO** `sigma_h` < `0.0044` → IC=-0.221 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=180)

- **FILTRO** `T_h` > `143.6315` → IC=-0.254 (n=59)

  - _Acción_: SKIP cuando `T_h` > 143.6315
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=180)

- **FILTRO** `T_h` < `87.9565` → IC=-0.237 (n=78)

  - _Acción_: SKIP cuando `T_h` < 87.9565
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=161)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `sigma_h` < `0.0066` → IC=-0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

- **FILTRO** `T_h` > `148.7378` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `T_h` > 148.7378
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.308 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=73)

- **FILTRO** `T_h` > `95.4524` → IC=-0.285 (n=105)

  - _Acción_: SKIP cuando `T_h` > 95.4524
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=107)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.363 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=151)

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.211 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=150)

- **FILTRO** `T_h` > `57.2198` → IC=-0.233 (n=133)

  - _Acción_: SKIP cuando `T_h` > 57.2198
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=67)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8095` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `pct_vs_K` |x|≤ 0.8095 (IC base=-0.158)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `T_h` < `132.3532` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `T_h` < 132.3532
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.264 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=160)

- **FILTRO** `T_h` > `67.5112` → IC=-0.221 (n=159)

  - _Acción_: SKIP cuando `T_h` > 67.5112
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=54)

- **FILTRO** `sigma_h` > `0.0142` → IC=-0.300 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=96)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.263 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=108)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1195` → IC=+0.461 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1195 (IC base=+0.332)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.383 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.332)

- **PATRÓN** `T_h` < `0.3261` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3261 (IC base=+0.332)

- **PATRÓN** `T_h` > `0.8789` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8789 (IC base=+0.332)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.332)

- **PATRÓN** `edge` > `0.0997` → IC=+0.427 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0997 (IC base=+0.392)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.399 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.392)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.409 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.392)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.422 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.392)

- **PATRÓN** `T_h` > `1.4833` → IC=+0.399 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4833 (IC base=+0.392)

- **PATRÓN** `dist_50` > `0.3751` → IC=+0.443 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3751 (IC base=+0.392)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=326)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.392)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1161` → IC=+0.264 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1161 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.214 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.171)

- **PATRÓN** `T_h` > `1.3612` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.3612 (IC base=+0.171)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.219 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.171)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.464 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.406)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.419 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.406)

- **PATRÓN** `T_h` < `1.2415` → IC=+0.435 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2415 (IC base=+0.406)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.482 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.406)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.175` → IC=+0.486 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.175 (IC base=+0.436)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.468 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.436)

- **PATRÓN** `T_h` > `0.5264` → IC=+0.452 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5264 (IC base=+0.436)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.471 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.436)

- **PATRÓN** `edge` > `0.2005` → IC=+0.470 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.473 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.462)

- **PATRÓN** `T_h` < `0.8229` → IC=+0.455 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8229 (IC base=+0.462)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.462)

- **PATRÓN** `dist_50` > `0.4597` → IC=+0.492 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4597 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.467 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=397)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=474)

- **PATRÓN** `streak_estiramiento` < `0.2918` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.2918 (IC base=+0.029)

- **PATRÓN** `streak_estiramiento` < `0.5343` → IC=+0.185 (n=217)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.5343 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.128 (n=240)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 29.0 (IC base=+0.059)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.061)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=+0.025)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `regimen_ma_toques` < `2.0` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `regimen_ma_toques` < 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=154)

- **PATRÓN** `streak_estiramiento` < `0.2236` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.2236 (IC base=+0.041)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.097)

- **PATRÓN** `streak_estiramiento` < `0.4354` → IC=+0.183 (n=137)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.4354 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.162 (n=149)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 31.0 (IC base=+0.097)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `streak_len` > `5.0` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=111)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=112)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.210 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=51)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

- **FILTRO** `volumen_racha` > `3677.1957` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `volumen_racha` > 3677.1957
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=21)

- **FILTRO** `libro_liquidez` < `3449.8988` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 3449.8988
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

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
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.045)

- **PATRÓN** `volumen_racha` < `16919.513` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 16919.513 (IC base=+0.045)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1060)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1338)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1293)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4766)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2744)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.189 (n=1681)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0053 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.217` → IC=+0.162 (n=5038)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.217 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3563` → IC=+0.155 (n=4688)

  - _Acción_: Kelly boost +0.78€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3563 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.156 (n=4664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 6.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5884` → IC=+0.233 (n=4501)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5884 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1325` → IC=+0.140 (n=2397)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1325 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.507` → IC=+0.134 (n=4680)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.507 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.392` → IC=+0.259 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.392 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=2957)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `4666.4786` → IC=+0.171 (n=1680)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4666.4786 (IC base=+0.147)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1937)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.220 (n=767)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.257 (n=257)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.225 (n=256)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.220 (n=800)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.201)

- **PATRÓN** `ibs_15` > `0.7086` → IC=+0.275 (n=767)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7086 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.3749` → IC=+0.225 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3749 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.5123` → IC=+0.205 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5123 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.56` → IC=+0.300 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.56 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `11927.4558` → IC=+0.217 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11927.4558 (IC base=+0.201)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.147 (n=943)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.007 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.143 (n=629)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.130)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1407` → IC=+0.132 (n=629)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.1407 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.134 (n=863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.133 (n=993)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.216 (n=943)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.1169` → IC=+0.150 (n=592)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1169 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.4294` → IC=+0.131 (n=998)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.4294 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.854` → IC=+0.282 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.854 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `5881.5817` → IC=+0.161 (n=428)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 5881.5817 (IC base=+0.130)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2521` → IC=-0.122 (n=199)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2521
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=387)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.6` → IC=+0.135 (n=916)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` > 0.6 (IC base=+0.061)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0253` → IC=+0.178 (n=1223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0253 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.171 (n=1223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0133 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.2194` → IC=+0.181 (n=1223)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.2194 (IC base=+0.166)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0978` → IC=+0.221 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0978 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=1124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.174 (n=1082)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 14.0 (IC base=+0.166)

- **PATRÓN** `ibs_15` > `0.5556` → IC=+0.247 (n=1095)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5556 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.1318` → IC=+0.193 (n=666)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1318 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.939` → IC=+0.220 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.939 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2743.8258` → IC=+0.192 (n=815)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2743.8258 (IC base=+0.166)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.156 (n=968)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1111 (IC base=+0.067)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.387 (n=245)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1122` → IC=+0.364 (n=490)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1122 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.376 (n=489)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.107` → IC=+0.376 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.107 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.370 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.363 (n=493)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.392 (n=735)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.378 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.976` → IC=+0.398 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.976 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `9875.3038` → IC=+0.381 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9875.3038 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.371 (n=122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2175` → IC=+0.374 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2175 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.397 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.379 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.385 (n=363)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.391 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.114` → IC=+0.389 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.114 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `9173.8264` → IC=+0.378 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9173.8264 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.403 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.366 (n=372)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.377 (n=169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.361)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.364 (n=249)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0824` → IC=+0.371 (n=332)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0824 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2951` → IC=+0.372 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2951 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.364 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.361)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.7604` → IC=+0.390 (n=372)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7604 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.1202` → IC=+0.370 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1202 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.363 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.402 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.361)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `4132.469` → IC=+0.377 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4132.469 (IC base=+0.361)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `libro_spread` > `0.01` → IC=-0.217 (n=2182)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3053)

- **FILTRO** `libro_liquidez` < `4433.059` → IC=-0.160 (n=3455)

  - _Acción_: SKIP cuando `libro_liquidez` < 4433.059
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1780)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.220 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.080)

- **PATRÓN** `ibs_15` > `0.6296` → IC=+0.278 (n=1197)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6296 (IC base=-0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1103` → IC=+0.202 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1103 (IC base=-0.080)

- **PATRÓN** `dist_vwap_pct` < `0.5575` → IC=+0.199 (n=1265)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.5575 (IC base=-0.080)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2353` → IC=+0.271 (n=1579)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2353 (IC base=-0.005)

- **PATRÓN** `ibs_15` < `0.3684` → IC=+0.285 (n=4736)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3684 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` > `0.6573` → IC=+0.281 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6573 (IC base=-0.005)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0319` → IC=-0.222 (n=2467)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0319
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=826)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.218 (n=823)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2470)

- **FILTRO** `sigma_ewma_delta_pct` > `22.233` → IC=-0.257 (n=472)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.233
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=2821)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.152 (n=320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.003 (IC base=+0.070)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2668` → IC=+0.279 (n=138)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2668 (IC base=+0.070)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.267 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.070)

- **PATRÓN** `ibs_15` > `0.7591` → IC=+0.327 (n=414)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7591 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1039` → IC=+0.278 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1039 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.4928` → IC=+0.286 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4928 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.371` → IC=+0.147 (n=216)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 22.371 (IC base=+0.070)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.233 (n=73)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0866` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0866 (IC base=-0.186)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.300 (n=73)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.186)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.186)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.186)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=783)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.157 (n=529)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0059 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.178 (n=265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3006` → IC=+0.194 (n=468)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3006 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.157 (n=429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 11.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5684` → IC=+0.239 (n=600)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5684 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1135` → IC=+0.152 (n=374)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1135 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.2726` → IC=+0.148 (n=560)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2726 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.049` → IC=+0.261 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.049 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=783)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `5050.7283` → IC=+0.154 (n=400)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 5050.7283 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.252 (n=1805)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.3568` → IC=+0.249 (n=1587)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3568 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7773` → IC=+0.261 (n=1587)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7773 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2147` → IC=+0.266 (n=818)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2147 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.245 (n=1225)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.2974` → IC=+0.285 (n=1587)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2974 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6047` → IC=+0.272 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6047 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.253` → IC=+0.249 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.253 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1833` → IC=-0.257 (n=303)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1833
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=911)

- **FILTRO** `drift_60min` |x|> `0.1723` → IC=-0.259 (n=412)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1723
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=802)

- **FILTRO** `drift_15min` |x|> `0.9082` → IC=-0.280 (n=303)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9082
  - _Potencial_: sin este filtro IC_bueno=-0.166 (n=911)

- **FILTRO** `sigma_ewma_delta_pct` > `6.141` → IC=-0.203 (n=281)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.141
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=933)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.217 (n=235)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=979)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.195)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.195)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.195)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.195)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0639` → IC=+0.232 (n=804)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0639 (IC base=-0.031)

- **PATRÓN** `ibs_15` < `0.383` → IC=+0.294 (n=804)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.383 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.6772` → IC=+0.236 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6772 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.1942` → IC=+0.245 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1942 (IC base=-0.031)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0131` → IC=-0.240 (n=1100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0131
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=368)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.215)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.215)

- **PATRÓN** `delta_ratio_macro` |x|> `0.119` → IC=+0.278 (n=735)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.119 (IC base=-0.019)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0946` → IC=+0.297 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0946 (IC base=-0.019)

- **PATRÓN** `ibs_15` < `0.1351` → IC=+0.311 (n=735)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1351 (IC base=-0.019)

- **PATRÓN** `dist_vwap_pct` > `0.7735` → IC=+0.339 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7735 (IC base=-0.019)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.167 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0061 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.1564` → IC=+0.144 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1564 (IC base=+0.097)

- **PATRÓN** `drift_15min` |x|≤ `0.3763` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3763 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.340 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.4735` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4735 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.081` → IC=+0.172 (n=59)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.081 (IC base=+0.053)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.167 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0061 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.1564` → IC=+0.144 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1564 (IC base=+0.097)

- **PATRÓN** `drift_15min` |x|≤ `0.3763` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3763 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.340 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.4735` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4735 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.081` → IC=+0.172 (n=59)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.081 (IC base=+0.053)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.298 (n=438)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0722` → IC=+0.311 (n=576)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0722 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1516` → IC=+0.285 (n=872)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1516 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.223` → IC=+0.292 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.223 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.297 (n=1350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.311 (n=1308)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.266` → IC=+0.314 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.266 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.1` → IC=+0.388 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.1 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `13320.6058` → IC=+0.306 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13320.6058 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.302 (n=306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.276)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.316 (n=232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.276)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2694` → IC=+0.278 (n=232)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2694 (IC base=+0.276)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.282 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.276)

- **PATRÓN** `ibs_15` > `0.8612` → IC=+0.311 (n=621)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8612 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.2504` → IC=+0.314 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2504 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.915` → IC=+0.391 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.915 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `14793.6456` → IC=+0.308 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14793.6456 (IC base=+0.276)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.300 (n=614)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0504` → IC=+0.312 (n=205)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0504 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1409` → IC=+0.293 (n=409)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1409 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1008` → IC=+0.324 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1008 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.294 (n=435)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8479` → IC=+0.318 (n=614)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8479 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.315 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.34` → IC=+0.377 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.34 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.156 (n=91)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=279)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.129 (n=251)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=87)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.211 (n=119)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=369)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.183 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=367)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1387` → IC=-0.136 (n=53)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1387
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=161)

- **FILTRO** `sigma_h` < `0.0053` → IC=-0.184 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=20)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2127` → IC=-0.233 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2127
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=28)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1149` → IC=-0.206 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1149
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.306` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.306
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0094` → IC=-0.167 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

- **FILTRO** `drift_15min` |x|> `0.2309` → IC=-0.225 (n=38)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2309
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

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
- **PATRÓN** `T_h` > `87.9957` → IC=+0.178 (n=609)

  - _Acción_: Kelly boost +0.89€ cuando `T_h` > 87.9957 (IC base=+0.177)

- **PATRÓN** `ratio` < `0.9704` → IC=+0.397 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9704 (IC base=+0.177)

- **PATRÓN** `T_h` > `119.9477` → IC=+0.355 (n=2728)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 119.9477 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0219` → IC=+0.389 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0219 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9936` → IC=+0.146 (n=258)

  - _Acción_: Kelly boost +0.73€ cuando `T_h` > 111.9936 (IC base=+0.137)

- **PATRÓN** `ratio` < `0.9933` → IC=+0.270 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.137)

- **PATRÓN** `T_h` > `111.9838` → IC=+0.316 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.302)

- **PATRÓN** `ratio` > `1.0182` → IC=+0.359 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0182 (IC base=+0.302)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `85.7585` → IC=+0.228 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 85.7585 (IC base=+0.224)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.404 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.224)

- **PATRÓN** `T_h` > `111.9969` → IC=+0.355 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9969 (IC base=+0.323)

- **PATRÓN** `ratio` > `1.0314` → IC=+0.400 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0314 (IC base=+0.323)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0788` → IC=+0.419 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0788 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5884 sube el IC de +0.147 a +0.233 en UPDOWN_GBM#15min (n=4501). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7086 sube el IC de +0.201 a +0.275 en UPDOWN_GBM#BTC#15min (n=767). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.130 a +0.216 en UPDOWN_GBM#ETH#15min (n=943). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5556 sube el IC de +0.166 a +0.247 en UPDOWN_GBM#XRP#15min (n=1095). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.067 a +0.156 en UPDOWN_GBM#XRP#15min (n=968). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6296 sube el IC de -0.080 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1197). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3684 sube el IC de -0.005 a +0.285 en UPDOWN_GBM_15M_TARDIO (n=4736). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7591 sube el IC de +0.070 a +0.327 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=414). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.186 a +0.300 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=73). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5684 sube el IC de +0.145 a +0.239 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=600). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2974 sube el IC de +0.244 a +0.285 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1587). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.195 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.383 sube el IC de -0.031 a +0.294 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=804). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.215 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1351 sube el IC de -0.019 a +0.311 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=735). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.097 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7 (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.097 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.282 a +0.311 en UPDOWN_GBM_IBS_ALTO (n=1308). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8612 sube el IC de +0.276 a +0.311 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=621). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8479 sube el IC de +0.289 a +0.318 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=614). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.362 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=735). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.385 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=363). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7604 sube el IC de +0.361 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=372). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2155 | +0.085 | +232.61€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2155 | +0.085 | +232.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1750 | +0.086 | +193.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1750 | +0.086 | +193.32€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 90 | +0.130 | +28.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 90 | +0.130 | +28.32€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1088 | -0.025 | +67.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1088 | -0.025 | +67.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 840 | -0.039 | +54.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 840 | -0.039 | +54.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 164 | +0.048 | +16.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 164 | +0.048 | +16.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 46276 | -0.086 | -5878.73€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2787 | +0.060 | -295.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 43489 | -0.095 | -5583.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4763 | -0.112 | -796.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4763 | -0.112 | -796.96€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2787 | +0.060 | -295.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2787 | +0.060 | -295.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4802 | -0.109 | -929.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4802 | -0.109 | -929.23€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12630 | -0.043 | -1177.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12630 | -0.043 | -1177.16€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12526 | -0.113 | -1247.21€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12526 | -0.113 | -1247.21€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8768 | -0.128 | -1433.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8768 | -0.128 | -1433.14€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 46902 | -0.012 | +2952.93€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 12108 | +0.005 | +1551.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 34794 | -0.018 | +1401.21€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 46902 | -0.012 | +2952.93€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 12108 | +0.005 | +1551.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 34794 | -0.018 | +1401.21€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 181280 | +0.113 | -7559.39€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21345 | +0.180 | -682.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 829 | +0.004 | -77.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 148688 | +0.105 | -6426.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10418 | +0.093 | -373.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 24641 | +0.103 | -1717.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 74 | -0.171 | +12.42€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 24552 | +0.104 | -1717.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 34492 | +0.124 | -586.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5592 | +0.179 | -227.69€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 24621 | +0.120 | -187.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4237 | +0.079 | -149.48€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 24690 | +0.098 | -1808.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 84 | -0.116 | +5.91€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 24591 | +0.099 | -1803.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 38689 | +0.123 | -818.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9787 | +0.177 | -234.90€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 24998 | +0.105 | -523.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3892 | +0.103 | -51.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#SOL | 34102 | +0.112 | -1529.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5723 | +0.199 | -245.79€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 732 | +0.031 | -23.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 25358 | +0.096 | -1087.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2289 | +0.103 | -172.34€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 24666 | +0.106 | -1099.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 85 | -0.121 | +7.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 24568 | +0.107 | -1106.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 29361 | +0.193 | -1978.22€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 29361 | +0.193 | -1978.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6636 | +0.173 | -637.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6636 | +0.173 | -637.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4169 | +0.197 | -153.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4169 | +0.197 | -153.58€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6530 | +0.176 | -559.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6530 | +0.176 | -559.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5507 | +0.249 | -203.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5507 | +0.249 | -203.88€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6440 | +0.186 | -436.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6440 | +0.186 | -436.92€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1209 | +0.426 | -44.61€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1209 | +0.426 | -44.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 493 | +0.439 | -4.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 493 | +0.439 | -4.49€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 489 | +0.425 | -17.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 489 | +0.425 | -17.89€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 103661 | +0.200 | -7619.87€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 103661 | +0.200 | -7619.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 17891 | +0.180 | -1994.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 17891 | +0.180 | -1994.82€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 16714 | +0.225 | -553.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 16714 | +0.225 | -553.30€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 17796 | +0.180 | -1896.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 17796 | +0.180 | -1896.66€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 16851 | +0.218 | -679.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 16851 | +0.218 | -679.12€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 17139 | +0.203 | -1096.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 17139 | +0.203 | -1096.80€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 17270 | +0.196 | -1399.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 17270 | +0.196 | -1399.17€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 39871 | +0.117 | +318.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 39871 | +0.117 | +318.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 19853 | +0.117 | +192.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 19853 | +0.117 | +192.85€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 20018 | +0.116 | +125.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 20018 | +0.116 | +125.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2503 | +0.292 | -13.08€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2503 | +0.292 | -13.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1145 | +0.279 | -33.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1145 | +0.279 | -33.49€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1222 | +0.298 | +16.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1222 | +0.298 | +16.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 136 | +0.341 | +3.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 136 | +0.341 | +3.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1151 | +0.440 | +0.45€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1151 | +0.440 | +0.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 551 | +0.433 | -9.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 551 | +0.433 | -9.31€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 549 | +0.447 | +8.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 549 | +0.447 | +8.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 51 | +0.406 | +1.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 51 | +0.406 | +1.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1906 | +0.068 | -83.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1181 | +0.082 | -19.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1472 | +0.076 | -38.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1181 | +0.082 | -19.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 80611 | +0.100 | -1938.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6502 | +0.095 | +124.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 74109 | +0.101 | -2062.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 44104 | +0.105 | -453.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6502 | +0.095 | +124.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 37602 | +0.107 | -578.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 17046 | +0.109 | -93.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 17046 | +0.109 | -93.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 19461 | +0.082 | -1391.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 19461 | +0.082 | -1391.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 54760 | +0.098 | +30263.32€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 54760 | +0.098 | +30263.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9079 | +0.225 | +7818.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9079 | +0.225 | +7818.76€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 8343 | +0.174 | +6490.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8343 | +0.174 | +6490.87€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 9831 | +0.207 | +7731.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9831 | +0.207 | +7731.92€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 7410 | +0.051 | +2311.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7410 | +0.051 | +2311.63€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 7650 | -0.031 | +1992.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7650 | -0.031 | +1992.99€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 12447 | -0.024 | +3917.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 12447 | -0.024 | +3917.15€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 57686 | +0.085 | +33462.96€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 57686 | +0.085 | +33462.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 11203 | -0.002 | +6037.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 11203 | -0.002 | +6037.67€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 12353 | +0.004 | +3252.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 12353 | +0.004 | +3252.50€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7881 | +0.293 | +8949.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7881 | +0.293 | +8949.94€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 10920 | +0.014 | +3375.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 10920 | +0.014 | +3375.50€ | 1 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8919 | +0.044 | +3998.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8919 | +0.044 | +3998.31€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6410 | +0.316 | +7849.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6410 | +0.316 | +7849.04€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 43382 | +0.178 | +35720.60€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 43382 | +0.178 | +35720.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6526 | +0.239 | +6071.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6526 | +0.239 | +6071.07€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6878 | +0.139 | +5062.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6878 | +0.139 | +5062.98€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6973 | +0.224 | +6024.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6973 | +0.224 | +6024.76€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7437 | +0.130 | +5771.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7437 | +0.130 | +5771.09€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8201 | +0.119 | +6145.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8201 | +0.119 | +6145.61€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7367 | +0.232 | +6645.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7367 | +0.232 | +6645.07€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 11748 | +0.126 | +5860.59€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 11748 | +0.126 | +5860.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 468 | +0.157 | +308.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 468 | +0.157 | +308.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3342 | +0.130 | +1820.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3342 | +0.130 | +1820.25€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 505 | +0.159 | +279.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 505 | +0.159 | +279.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3463 | +0.125 | +1671.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3463 | +0.125 | +1671.57€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2949 | +0.095 | +1150.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2949 | +0.095 | +1150.35€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1021 | +0.169 | +630.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1021 | +0.169 | +630.22€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 54963 | +0.187 | +45045.11€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 54963 | +0.187 | +45045.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8673 | +0.250 | +8397.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8673 | +0.250 | +8397.73€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8707 | +0.136 | +5964.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8707 | +0.136 | +5964.05€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 9331 | +0.235 | +8420.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 9331 | +0.235 | +8420.93€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9113 | +0.139 | +6699.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9113 | +0.139 | +6699.14€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 9754 | +0.122 | +6886.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 9754 | +0.122 | +6886.53€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9385 | +0.240 | +8676.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9385 | +0.240 | +8676.73€ | 0 | 20 |
| ✅ GBM_LATE_5M | 13742 | +0.210 | +11123.78€ | 1 | 27 |
| ✅ GBM_LATE_5M#5min | 13742 | +0.210 | +11123.78€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3257 | +0.211 | +2804.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3257 | +0.211 | +2804.80€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1302 | +0.204 | +1008.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1302 | +0.204 | +1008.66€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3976 | +0.202 | +2965.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3976 | +0.202 | +2965.35€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 2194 | +0.207 | +1807.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2194 | +0.207 | +1807.56€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 1959 | +0.209 | +1537.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1959 | +0.209 | +1537.13€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4824 | +0.049 | +1316.89€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 4824 | +0.049 | +1316.89€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1688 | +0.059 | +529.28€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1688 | +0.059 | +529.28€ | 1 | 6 |
| ✅ GBM_LATE_60M#ETH | 1558 | +0.049 | +465.43€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1558 | +0.049 | +465.43€ | 2 | 6 |
| ✅ GBM_LATE_60M#SOL | 1578 | +0.039 | +322.19€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1578 | +0.039 | +322.19€ | 0 | 10 |
| 🚫 GBM_LATE_60M_FADE | 695 | -0.250 | -36.77€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 695 | -0.250 | -36.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 254 | -0.254 | -21.80€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 254 | -0.254 | -21.80€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 257 | -0.241 | -5.52€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 257 | -0.241 | -5.52€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 184 | -0.253 | -9.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 184 | -0.253 | -9.46€ | 7 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1998 | +0.084 | +517.47€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1998 | +0.084 | +517.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 777 | +0.072 | +195.91€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 777 | +0.072 | +195.91€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 699 | +0.059 | +126.45€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 699 | +0.059 | +126.45€ | 1 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 522 | +0.132 | +195.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 522 | +0.132 | +195.11€ | 2 | 8 |
| ✅ LATE_WINDOW_5MIN | 225 | +0.293 | +252.39€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN#5min | 225 | +0.293 | +252.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 225 | +0.293 | +252.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 225 | +0.293 | +252.39€ | 1 | 13 |
| ✅ LEADLAG_BTC_XRP_15M | 4265 | +0.098 | +977.16€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4265 | +0.098 | +977.16€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4265 | +0.098 | +977.16€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4265 | +0.098 | +977.16€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 979 | -0.013 | +12.91€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 979 | -0.013 | +12.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 53 | +0.009 | +0.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 53 | +0.009 | +0.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 264 | -0.015 | +4.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 264 | -0.015 | +4.77€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 34 | -0.167 | -6.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 34 | -0.167 | -6.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 263 | +0.025 | +19.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 263 | +0.025 | +19.49€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 293 | -0.005 | +3.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 293 | -0.005 | +3.48€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 72 | -0.108 | -8.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 72 | -0.108 | -8.79€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4142 | +0.017 | +124.16€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4142 | +0.017 | +124.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 200 | +0.025 | -1.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 200 | +0.025 | -1.25€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 825 | +0.015 | +40.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 825 | +0.015 | +40.47€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 236 | +0.025 | +24.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 236 | +0.025 | +24.39€ | 0 | 2 |
| ✅ LIQUIDACIONES_5M#ETH | 1643 | +0.019 | +27.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1643 | +0.019 | +27.87€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 767 | +0.011 | +1.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 767 | +0.011 | +1.87€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 471 | +0.016 | +30.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 471 | +0.016 | +30.81€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2259 | -0.033 | -11.53€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2259 | -0.033 | -11.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 682 | -0.032 | -12.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 682 | -0.032 | -12.71€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 802 | -0.009 | +17.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 802 | -0.009 | +17.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 775 | -0.060 | -16.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 775 | -0.060 | -16.39€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 14353 | -0.032 | -124.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 6877 | -0.034 | -84.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 7476 | -0.030 | -40.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 509 | -0.048 | -23.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 260 | -0.015 | +7.72€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 249 | -0.082 | -30.94€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3756 | -0.025 | -10.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1785 | -0.024 | +1.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1971 | -0.027 | -12.41€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1425 | -0.028 | +13.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 728 | -0.034 | -1.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 697 | -0.022 | +15.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3244 | -0.035 | -62.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1523 | -0.038 | -41.10€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1721 | -0.033 | -21.21€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2757 | -0.026 | +25.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1333 | -0.032 | -7.37€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1424 | -0.020 | +32.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2662 | -0.042 | -67.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1248 | -0.049 | -43.61€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1414 | -0.036 | -23.77€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 64800 | +0.000 | +3484.69€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 64800 | +0.000 | +3484.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 11733 | +0.027 | +1596.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 11733 | +0.027 | +1596.06€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9101 | -0.035 | -102.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9101 | -0.035 | -102.89€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 11866 | +0.025 | +1289.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 11866 | +0.025 | +1289.60€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9014 | -0.051 | -200.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9014 | -0.051 | -200.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 11025 | -0.004 | +302.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 11025 | -0.004 | +302.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 12061 | +0.018 | +599.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 12061 | +0.018 | +599.56€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7104 | -0.055 | -116.97€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7104 | -0.055 | -116.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1244 | -0.002 | -15.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1244 | -0.002 | -15.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1961 | -0.066 | -28.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1961 | -0.066 | -28.55€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 71 | -0.007 | +0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 71 | -0.007 | +0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 803 | -0.119 | -34.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 803 | -0.119 | -34.10€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2163 | -0.068 | -12.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2163 | -0.068 | -12.26€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 862 | -0.017 | -27.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 862 | -0.017 | -27.01€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3376 | +0.004 | -1.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3376 | +0.004 | -1.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 195 | +0.008 | -2.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 195 | +0.008 | -2.19€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 192 | -0.010 | -2.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 192 | -0.010 | -2.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 159163 | -0.077 | +2315.39€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 159163 | -0.077 | +2315.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 27852 | -0.078 | +1574.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 27852 | -0.078 | +1574.87€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 23816 | -0.101 | -1174.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 23816 | -0.101 | -1174.94€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 28211 | -0.068 | +1409.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 28211 | -0.068 | +1409.00€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 23354 | -0.098 | -666.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 23354 | -0.098 | -666.22€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 28457 | -0.059 | +332.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 28457 | -0.059 | +332.38€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 27473 | -0.069 | +840.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 27473 | -0.069 | +840.30€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9003 | -0.035 | -183.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9003 | -0.035 | -183.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2078 | -0.047 | -28.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2078 | -0.047 | -28.27€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2635 | -0.025 | -37.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2635 | -0.025 | -37.79€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1269 | -0.065 | -33.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1269 | -0.065 | -33.39€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1010 | -0.031 | -32.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1010 | -0.031 | -32.49€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2088 | +0.119 | +823.07€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1952 | +0.123 | +810.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 468 | +0.132 | +224.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 468 | +0.132 | +224.04€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 397 | +0.119 | +139.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 397 | +0.119 | +139.70€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 368 | +0.127 | +167.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 368 | +0.127 | +167.79€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 334 | +0.143 | +173.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 334 | +0.143 | +173.26€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 385 | +0.094 | +105.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 385 | +0.094 | +105.68€ | 0 | 1 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2074 | -0.017 | -23.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2074 | -0.017 | -23.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 387 | +0.017 | +27.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 387 | +0.017 | +27.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 380 | -0.044 | -25.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 380 | -0.044 | -25.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 517 | -0.040 | -32.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 517 | -0.040 | -32.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 426 | -0.005 | -3.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 426 | -0.005 | -3.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 364 | -0.005 | +10.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 364 | -0.005 | +10.43€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1112 | -0.077 | -52.46€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 511 | -0.110 | -78.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 399 | -0.126 | -60.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 112 | -0.053 | -18.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 391 | -0.037 | +19.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 280 | -0.021 | +28.68€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 111 | -0.075 | -9.44€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 210 | -0.071 | +6.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 174 | -0.068 | +4.94€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 853 | -0.080 | -26.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 259 | -0.067 | -26.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1409 | -0.207 | -89.05€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 555 | -0.207 | -50.44€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 488 | -0.206 | -46.13€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 67 | -0.210 | -4.31€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 470 | -0.210 | -37.54€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 412 | -0.220 | -44.45€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 58 | -0.133 | +6.91€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 384 | -0.202 | -1.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 357 | -0.199 | -3.48€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 27 | -0.224 | +2.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1257 | -0.209 | -94.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 152 | -0.188 | +5.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 528 | +0.376 | +484.78€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 104 | +0.141 | +73.22€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 104 | +0.141 | +73.22€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 123 | +0.364 | +103.53€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 123 | +0.364 | +103.53€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 301 | +0.457 | +308.04€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 301 | +0.457 | +308.04€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 528 | +0.376 | +484.78€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 909 | +0.046 | +86.29€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 909 | +0.046 | +86.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 343 | +0.028 | +8.11€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 343 | +0.028 | +8.11€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 71 | +0.007 | +0.21€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 71 | +0.007 | +0.21€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 412 | +0.072 | +71.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 412 | +0.072 | +71.92€ | 1 | 4 |
| ✅ STREAK_FADE_5M | 3560 | -0.023 | -143.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3560 | -0.023 | -143.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 609 | -0.029 | -27.28€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 609 | -0.029 | -27.28€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 170 | -0.041 | -14.29€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 170 | -0.041 | -14.29€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1654 | -0.020 | -61.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1654 | -0.020 | -61.43€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 116 | -0.042 | -10.16€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 116 | -0.042 | -10.16€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 72 | -0.013 | -5.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 72 | -0.013 | -5.54€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11472 | +0.014 | +71.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11472 | +0.014 | +71.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2993 | +0.018 | +23.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2993 | +0.018 | +23.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2985 | +0.017 | +34.64€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2985 | +0.017 | +34.64€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2915 | +0.008 | -3.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2915 | +0.008 | -3.30€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 11501 | +0.017 | -18.60€ | 3 | 0 |
| ✅ STRUCT_NO_15M#15min | 11501 | +0.017 | -18.60€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4785 | +0.021 | +5.06€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4785 | +0.021 | +5.06€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3938 | +0.015 | -11.42€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3938 | +0.015 | -11.42€ | 3 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2778 | +0.011 | -12.25€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2778 | +0.011 | -12.25€ | 1 | 0 |
| ✅ UPDOWN_GBM | 101624 | +0.060 | +9692.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 24768 | +0.080 | +5137.92€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3053 | +0.000 | +30.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 67444 | +0.061 | +4420.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6008 | +0.000 | +106.57€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 8486 | +0.105 | +1565.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1781 | +0.164 | +820.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6615 | +0.091 | +747.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 23160 | +0.057 | +2026.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3327 | +0.080 | +755.16€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 862 | +0.001 | +14.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 16151 | +0.066 | +1181.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2692 | -0.003 | +70.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 128 | -0.061 | +4.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 11039 | +0.079 | +1283.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 9192 | +0.065 | +545.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 24115 | +0.049 | +1666.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5875 | +0.072 | +888.83€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 833 | +0.004 | +15.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 15079 | +0.051 | +731.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2211 | +0.003 | +28.64€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 117 | -0.105 | +1.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 21673 | +0.039 | +1227.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 6547 | +0.032 | +429.04€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 785 | -0.009 | +4.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 13132 | +0.050 | +794.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1105 | +0.003 | +7.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 104 | -0.141 | -7.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 13149 | +0.073 | +1923.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 5477 | +0.096 | +1506.26€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7275 | +0.059 | +419.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 349 | -0.101 | -1.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 979 | +0.362 | +350.46€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 979 | +0.362 | +350.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 484 | +0.362 | +168.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 484 | +0.362 | +168.39€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 495 | +0.361 | +182.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 495 | +0.361 | +182.07€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 24480 | -0.021 | +6054.95€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 24480 | -0.021 | +6054.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4566 | -0.114 | +233.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4566 | -0.114 | +233.17€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3204 | +0.220 | +2050.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3204 | +0.220 | +2050.49€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6923 | -0.060 | +1047.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6923 | -0.060 | +1047.03€ | 5 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6735 | -0.062 | +1263.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6735 | -0.062 | +1263.21€ | 1 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 298 | +0.063 | +25.19€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 298 | +0.063 | +25.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 298 | +0.063 | +25.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 298 | +0.063 | +25.19€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1744 | +0.282 | +1457.34€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1744 | +0.282 | +1457.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 926 | +0.276 | +723.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 926 | +0.276 | +723.34€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 818 | +0.289 | +733.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 818 | +0.289 | +733.99€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 858 | -0.113 | -84.85€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 858 | -0.113 | -84.85€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 270 | -0.081 | -20.33€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 270 | -0.081 | -20.33€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 95 | -0.170 | -10.94€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 95 | -0.170 | -10.94€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 110 | -0.179 | -4.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 110 | -0.179 | -4.23€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4517 | +0.303 | +2082.79€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1714 | +0.260 | +233.47€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1738 | +0.297 | +752.37€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 1065 | +0.381 | +1096.95€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.021 n=1253 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1253 IC=+0.021 PNL=+60.95€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 793 celda(s) pasan gate riguroso completo de 2860 evaluadas (n>=40) y 3983 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.032 < 0.08 — monitorear
  - _Datos_: n=6541 IC=+0.032 PNL=+427.84€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1738/15 IC=+0.297 PNL=+752.37€ | BTC: n=1714/15 IC=+0.260 PNL=+233.47€ | SOL: n=1065/15 IC=+0.381 PNL=+1096.95€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.143 n=1031/60 | contraria IC=+0.185 n=1089 | gap=-0.042 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=571, boost estimado=+0.014. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2210/40 IC=+0.002 PNL=+28.18€ | BTC#60min: n=2691/40 IC=-0.003 PNL=+70.25€ | SOL#60min: n=1105/40 IC=+0.003 PNL=+7.23€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.045 n=703221 | tras_1loss IC=+0.099 n=533750 | tras_2loss IC=+0.069 n=213904/40 | gap=-0.024 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.168 > 0.08 con n=1002 PNL=+635.00€
  - _Datos_: n=1002 IC=+0.168 PNL=+635.00€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.140 > 0.08 con n=1192 PNL=+588.13€
  - _Datos_: n=1192 IC=+0.140 PNL=+588.13€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.147 > 0.08 con n=83 PNL=+39.55€
  - _Datos_: n=83 IC=+0.147 PNL=+39.55€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=3681 PNL=+2056.75€
  - _Datos_: n=3681 IC=+0.334 PNL=+2056.75€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1022 IC=+0.065 PNL=+99.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1022 IC=+0.065 PNL=+99.82€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=103 IC=+0.176 PNL=+66.34€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=103 IC=+0.176 PNL=+66.34€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 6/15 ops en el filtro definido (IC actual=+0.075 PNL=+7.10€)
  - _Datos_: n=6 IC=+0.075 PNL=+7.10€

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
  - _Estado_: n=4015 IC=+0.002 PNL=-12.86€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4015 IC=+0.002 PNL=-12.86€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1991 IC=-0.004 PNL=+118.54€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1991 IC=-0.004 PNL=+118.54€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1253 IC=+0.021 PNL=+60.95€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1253 IC=+0.021 PNL=+60.95€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.147 > 0.1 con n=6709 PNL=+3527.99€
  - _Datos_: n=6709 IC=+0.147 PNL=+3527.99€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3323 IC=+0.081 PNL=+754.96€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3323 IC=+0.081 PNL=+754.96€

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
  - _Estado_: n=1299 IC=+0.038 PNL=+105.37€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1299 IC=+0.038 PNL=+105.37€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=166 IC=-0.012 PNL=-2.61€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=166 IC=-0.012 PNL=-2.61€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.293 n=225) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=225 IC=+0.293 PNL=+252.39€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.02 con n=1224 PNL=+486.87€
  - _Datos_: n=1224 IC=+0.117 PNL=+486.87€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=251 IC=-0.117 PNL=+7.41€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=251 IC=-0.117 PNL=+7.41€

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
  - _Estado_: n=41448 IC=+0.074 PNL=+5837.60€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=41448 IC=+0.074 PNL=+5837.60€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.137 < -0.1 con n=725 PNL=+101.39€
  - _Datos_: n=725 IC=-0.137 PNL=+101.39€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3845 IC=+0.067 PNL=+486.00€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3845 IC=+0.067 PNL=+486.00€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=181 IC=-0.112 PNL=-1.84€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=181 IC=-0.112 PNL=-1.84€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.103 > 0.1 con n=1061 PNL=+272.47€
  - _Datos_: n=1061 IC=+0.103 PNL=+272.47€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 6/20 ops en el filtro definido (IC actual=-0.075 PNL=-1.82€)
  - _Datos_: n=6 IC=-0.075 PNL=-1.82€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=41672 IC=-0.137 PNL=+2733.28€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=41672 IC=-0.137 PNL=+2733.28€

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
  - _Estado_: n=4301 IC=+0.128 PNL=+2782.75€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4301 IC=+0.128 PNL=+2782.75€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=10436 IC=+0.058 PNL=+911.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=10436 IC=+0.058 PNL=+911.24€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.08 con n=4450 PNL=+2505.13€
  - _Datos_: n=4450 IC=+0.100 PNL=+2505.13€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=4531 PNL=-374.52€
  - _Datos_: n=4531 IC=-0.220 PNL=-374.52€

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
  - _Estado_: n=100 IC=+0.039 PNL=+17.70€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=100 IC=+0.039 PNL=+17.70€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=2163) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2163 IC=+0.096 PNL=+437.44€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.412 n=672) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=672 IC=+0.412 PNL=+976.00€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=17880 IC=+0.180 PNL=-1992.59€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=17880 IC=+0.180 PNL=-1992.59€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.229 > 0.1 con n=278 PNL=+192.09€
  - _Datos_: n=278 IC=+0.229 PNL=+192.09€
