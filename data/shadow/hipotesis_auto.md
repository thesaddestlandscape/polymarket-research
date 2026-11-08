# Hipótesis automáticas — 2026-11-08 03:07 UTC
_Generado por shadow_postmortem.py sobre 1240382 resoluciones (PNL=+168760.85€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=694)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.198 (n=1011)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.505 (IC base=+0.128)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.183 (n=317)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 63.0 (IC base=+0.128)

- **PATRÓN** `banda_hit_calibrado` > `0.6133` → IC=+0.242 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6133 (IC base=+0.128)

- **PATRÓN** `banda_z` > `8.626` → IC=+0.202 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.626 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.128 (n=684)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 12.0 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1037)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.128)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.605` → IC=-0.301 (n=164)

  - _Acción_: SKIP cuando `py_entrada` > 0.605
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=495)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.196 (n=876)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.131)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.186 (n=275)

  - _Acción_: Kelly boost +0.93€ cuando `n_total_lado` > 66.0 (IC base=+0.131)

- **PATRÓN** `banda_hit_calibrado` > `0.8129` → IC=+0.273 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8129 (IC base=+0.131)

- **PATRÓN** `banda_z` > `8.922` → IC=+0.206 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.922 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.138 (n=834)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=937)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.131)

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
- **FILTRO** `restante_s_al_confirmar` < `133.11` → IC=-0.222 (n=11585)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.11
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=34757)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.14` → IC=-0.259 (n=1191)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.14
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=3576)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.68` → IC=-0.294 (n=1202)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.68
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3606)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `117.45` → IC=-0.167 (n=3161)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.45
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=9484)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `154.36` → IC=-0.240 (n=3139)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 154.36
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=9418)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=26855)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `8390.6367` → IC=+0.160 (n=2286)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 8390.6367 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=23027)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=27942)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.223 (n=21119)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=8148)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6635.7006` → IC=+0.147 (n=3146)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 6635.7006 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.184 (n=2086)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2678)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `9412.9736` → IC=+0.181 (n=1863)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9412.9736 (IC base=+0.178)

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
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=2141)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.171 (n=584)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=1372)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=5133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.168 (n=4335)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.376 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.214 (n=2320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.330 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=2697)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=1312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.148 (n=1115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.256 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1064)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.256 (n=935)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.421 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=1402)
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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=468)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.243 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=23054)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=19488)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.227 (n=9625)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=5253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.173 (n=5236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 18.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.182 (n=5299)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.74 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.173 (n=4416)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.71 (IC base=+0.173)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.213 (n=3062)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.215 (n=2040)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.252 (n=1548)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.210)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=5153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=4374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=5325)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=4031)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.256 (n=4357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.250 (n=3692)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.365 (n=1382)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=5072)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=4299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=3775)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=939)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.428 (n=833)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4472.0597` → IC=+0.444 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4472.0597 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.450 (n=256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.457 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `12430.0394` → IC=+0.446 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12430.0394 (IC base=+0.440)

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

- **FILTRO** `py_entrada` > `0.76` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.208 (n=26010)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=30485)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=4516)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.181 (n=9621)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=13797)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=6274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=4294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.192 (n=4465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.198 (n=10705)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.227 (n=4243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=4826)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.268 (n=4234)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `3176.5987` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3176.5987
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=4307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4425)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=5038)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=4998)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=5250)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=10848)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=11269)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.5` → IC=+0.137 (n=13210)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.5 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5287)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=5090)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6622)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.61` → IC=+0.142 (n=4979)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.61 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=5561)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.136 (n=6872)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.23` → IC=+0.139 (n=5067)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.23 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.306 (n=1345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.284 (n=904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.367 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.320 (n=653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=955)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.396 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.299 (n=803)

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
- **PATRÓN** `drift_60min` |x|≤ `0.475` → IC=+0.139 (n=17022)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.475 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=17216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=11838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.978` → IC=+0.246 (n=5676)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.978 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.7978` → IC=+0.283 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7978 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.514` → IC=+0.184 (n=8507)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.514 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6247` → IC=+0.264 (n=5062)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6247 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3036` → IC=+0.251 (n=1763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3036 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7456` → IC=+0.235 (n=4073)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7456 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=8480)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.122 (n=10618)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0061 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.143 (n=21231)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5652 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.6156` → IC=+0.191 (n=1442)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6156 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.1631` → IC=+0.189 (n=8360)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.1631 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `0.6965` → IC=+0.196 (n=3794)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6965 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.296` → IC=+0.229 (n=2130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.296 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` > `2.6772` → IC=+0.209 (n=4883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6772 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.226 (n=14560)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.081)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3627` → IC=+0.212 (n=3636)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3627 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=1769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2435)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9865` → IC=+0.280 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9865 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.52` → IC=+0.279 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.52 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.266 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.214 (n=3483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=3996)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.225 (n=2226)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.243 (n=3187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.243 (n=1448)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.0891` → IC=+0.280 (n=1064)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0891 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=1189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=1472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.5597` → IC=+0.258 (n=3185)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5597 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0944` → IC=+0.245 (n=2882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0944 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.252 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4457` → IC=+0.246 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4457 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.8556` → IC=+0.243 (n=2023)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8556 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.244 (n=3658)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1784.3481` → IC=+0.246 (n=2123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1784.3481 (IC base=+0.241)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.235 (n=1019)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.0811` → IC=+0.260 (n=1013)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0811 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.226 (n=2154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9085` → IC=+0.260 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9085 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.186` → IC=+0.234 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.186 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.3358` → IC=+0.224 (n=2998)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3358 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.963` → IC=+0.263 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.963 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.228 (n=3036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.270 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.4011` → IC=+0.223 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4011 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4332` → IC=+0.253 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4332 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.152 (n=3234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0063 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0769` → IC=+0.152 (n=1078)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0769 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.144 (n=2302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.5745` → IC=+0.176 (n=2845)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.5745 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.943` → IC=+0.137 (n=2953)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.943 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.2012` → IC=+0.135 (n=3233)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2012 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.154 (n=1314)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.4376` → IC=+0.138 (n=3108)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.4376 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=4195)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.168 (n=1355)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 204.0 (IC base=+0.129)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.212 (n=1751)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4046)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=1499)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.034` → IC=+0.278 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.034 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.198 (n=3450)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.223 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.7296` → IC=+0.213 (n=1705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7296 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=4658)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2029.4984` → IC=+0.204 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2029.4984 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.226 (n=3116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1755` → IC=+0.236 (n=1558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1755 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=1607)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.0426` → IC=+0.271 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0426 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.908` → IC=+0.264 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.908 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.251 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.765` → IC=+0.221 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.765 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.1593` → IC=+0.227 (n=2265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1593 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1789)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1909.461` → IC=+0.227 (n=1604)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1909.461 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.223 (n=3353)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.219)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=196)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=4639)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.156 (n=647)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.9435` → IC=+0.232 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9435 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.1401` → IC=+0.339 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1401 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.5452` → IC=+0.334 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5452 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.069` → IC=+0.202 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.069 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `0.7027` → IC=+0.339 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7027 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.167` → IC=+0.336 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.167 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.3024` → IC=+0.333 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3024 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.344 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.2749` → IC=+0.338 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2749 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.338 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.0903` → IC=+0.185 (n=1209)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.0903 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.3356` → IC=+0.159 (n=593)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3356 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` < `0.1401` → IC=+0.150 (n=2153)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1401 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.159 (n=1527)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8331 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.209 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.7747` → IC=+0.152 (n=1470)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.7747 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `1.5133` → IC=+0.153 (n=1969)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5133 (IC base=+0.049)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=731)

- **FILTRO** `ibs_20min` < `0.2647` → IC=-0.168 (n=215)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2647
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=652)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.132 (n=4552)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=2245)

- **FILTRO** `sigma_ewma_delta_pct` > `8.312` → IC=-0.224 (n=730)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.312
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6067)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.180 (n=298)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.9638` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9638 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` < `0.6032` → IC=+0.266 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6032 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.021` → IC=+0.159 (n=203)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 5.021 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `0.6265` → IC=+0.282 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6265 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.0815` → IC=+0.280 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0815 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.4484` → IC=+0.280 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4484 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.5401` → IC=+0.267 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5401 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.276 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.019)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.155 (n=2245)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.2 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.22` → IC=+0.289 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.22 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.6993` → IC=+0.303 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6993 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.300 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.4729` → IC=+0.301 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4729 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7826` → IC=-0.153 (n=3438)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7826
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=1773)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.168 (n=1147)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=4064)

- **FILTRO** `ibs_20min` > `0.7431` → IC=-0.195 (n=1815)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7431
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=5449)

- **PATRÓN** `ibs_20min` > `0.7826` → IC=+0.123 (n=1773)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.7826 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `1.0296` → IC=+0.359 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0296 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1854` → IC=+0.300 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1854 (IC base=-0.059)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.318 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` < `0.1074` → IC=+0.303 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1074 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.169` → IC=+0.305 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.169 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.5863` → IC=+0.306 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5863 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.5272` → IC=+0.323 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5272 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `0.8102` → IC=+0.277 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8102 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` < `0.2243` → IC=+0.263 (n=2081)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2243 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` < `0.6419` → IC=+0.271 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6419 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `1.0635` → IC=+0.284 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0635 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.1702` → IC=+0.284 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1702 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `2.1777` → IC=+0.266 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1777 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.270 (n=1979)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.198 (n=7357)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0106 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.8704` → IC=+0.287 (n=10006)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8704 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.9447` → IC=+0.301 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9447 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.491` → IC=+0.167 (n=9878)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.491 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `0.6928` → IC=+0.276 (n=7234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6928 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.292 (n=1836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.6532` → IC=+0.286 (n=4271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6532 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.308 (n=12436)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.089)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.158 (n=7094)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.6419` → IC=+0.154 (n=21272)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.6419 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` < `0.2566` → IC=+0.278 (n=7156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2566 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` < `0.6991` → IC=+0.279 (n=3075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6991 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` > `1.1928` → IC=+0.279 (n=2330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1928 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.325 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `1.5758` → IC=+0.302 (n=4531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5758 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` > `2.2821` → IC=+0.300 (n=4666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2821 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.308 (n=10266)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 73.0 (IC base=+0.082)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8012` → IC=-0.126 (n=3944)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8012
  - _Potencial_: sin este filtro IC_bueno=+0.296 (n=2032)

- **FILTRO** `ibs_20min` > `0.7197` → IC=-0.233 (n=1308)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7197
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=3933)

- **FILTRO** `sigma_ewma_delta_pct` > `4.13` → IC=-0.232 (n=1127)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.13
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=4114)

- **PATRÓN** `ibs_20min` > `0.9341` → IC=+0.336 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9341 (IC base=+0.018)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.992` → IC=+0.189 (n=1997)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 2.992 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.327 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4466` → IC=+0.280 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4466 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` > `2.242` → IC=+0.301 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.242 (IC base=+0.018)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.316 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.018)

- **PATRÓN** `ibs_20min` < `0.1726` → IC=+0.164 (n=1311)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1726 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1515` → IC=+0.401 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1515 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4222` → IC=+0.424 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4222 (IC base=-0.024)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.397 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.024)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.3003` → IC=+0.225 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3003 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.208 (n=2149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1954 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.214 (n=1919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6949 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.243 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.417` → IC=+0.230 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.417 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.243 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 263.0 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.1345` → IC=+0.253 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1345 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.6194` → IC=+0.251 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6194 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.304 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5263` → IC=+0.254 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5263 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1487` → IC=+0.258 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1487 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.266 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 212.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.319 (n=2078)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.291 (n=3113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=1693)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.622` → IC=+0.313 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.622 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.295 (n=2732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `1.6063` → IC=+0.290 (n=3021)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6063 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=3730)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2029.4984` → IC=+0.297 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2029.4984 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.308 (n=1880)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.323 (n=2509)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.304)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.323 (n=1236)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.304)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.326 (n=1080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.306 (n=1269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.304)

- **PATRÓN** `ibs_20min` > `0.1415` → IC=+0.315 (n=1872)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1415 (IC base=+0.304)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.202` → IC=+0.312 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.202 (IC base=+0.304)

- **PATRÓN** `volumen_pendiente_norm` < `0.1997` → IC=+0.305 (n=2761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1997 (IC base=+0.304)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.309 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` < `1.5947` → IC=+0.306 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5947 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` > `2.7378` → IC=+0.319 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7378 (IC base=+0.304)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.306 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.304)

- **PATRÓN** `libro_liquidez` > `1911.3596` → IC=+0.314 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.3596 (IC base=+0.304)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.311 (n=2347)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.304)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7273` → IC=-0.183 (n=1381)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7273
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=4147)

- **PATRÓN** `ibs_20min` > `0.8489` → IC=+0.158 (n=1355)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.8489 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.1447` → IC=+0.235 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1447 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.36` → IC=+0.234 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.36 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1593` → IC=+0.233 (n=1951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1593 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6724` → IC=+0.231 (n=1743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6724 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.234 (n=2047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.239 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4657` → IC=+0.237 (n=1891)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4657 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.5074` → IC=+0.233 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5074 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.253 (n=1930)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.022)

- **PATRÓN** `ibs_20min` < `0.093` → IC=+0.155 (n=1384)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.093 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` > `0.7318` → IC=+0.248 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7318 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` < `0.3517` → IC=+0.250 (n=1555)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3517 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.255 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1951 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.317 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.5219` → IC=+0.293 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5219 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.4276` → IC=+0.276 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4276 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.280 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7419` → IC=-0.244 (n=2289)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7419
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2290)

- **FILTRO** `ibs_20min` > `0.6216` → IC=-0.228 (n=1088)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6216
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=3266)

- **FILTRO** `sigma_ewma_delta_pct` > `8.276` → IC=-0.252 (n=497)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.276
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=3857)

- **PATRÓN** `ibs_20min` > `0.7419` → IC=+0.312 (n=2290)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7419 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `1.0465` → IC=+0.356 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0465 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.461` → IC=+0.152 (n=1857)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 2.461 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8456` → IC=+0.341 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8456 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `0.6986` → IC=+0.335 (n=1491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6986 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` < `0.1566` → IC=+0.335 (n=1726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1566 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.365 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `1.4306` → IC=+0.362 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4306 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.354 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.034)

- **PATRÓN** `ibs_20min` < `0.6216` → IC=+0.149 (n=3266)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.6216 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.3058` → IC=+0.260 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3058 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.013` → IC=+0.128 (n=3072)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.013 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.693` → IC=+0.281 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.693 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.281 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `2.4448` → IC=+0.267 (n=1564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4448 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.282 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.055)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.359 (n=2084)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.344 (n=2334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` > `0.2123` → IC=+0.339 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2123 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.802` → IC=+0.333 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.802 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `0.8705` → IC=+0.334 (n=1555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8705 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.347 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `1.4314` → IC=+0.326 (n=2244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4314 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `2978.5249` → IC=+0.327 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2978.5249 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.344 (n=2089)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.315)

- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.337 (n=2222)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.317)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.323 (n=1263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.317)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.318 (n=1204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.317)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.336 (n=2484)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.317)

- **PATRÓN** `dist_vwap_pct` < `0.2414` → IC=+0.322 (n=2408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2414 (IC base=+0.317)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.64` → IC=+0.331 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.64 (IC base=+0.317)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.320 (n=1095)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.317)

- **PATRÓN** `volumen_regimen` > `1.2113` → IC=+0.346 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2113 (IC base=+0.317)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.363 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.317)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.323 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4124 (IC base=+0.317)

- **PATRÓN** `volumen_spike_ratio` > `2.1367` → IC=+0.317 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1367 (IC base=+0.317)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.224 (n=5500)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.1219` → IC=+0.191 (n=7248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1219 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=17090)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.5385` → IC=+0.231 (n=16483)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5385 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.1628` → IC=+0.206 (n=6348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1628 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.818` → IC=+0.258 (n=3208)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.818 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.1828` → IC=+0.155 (n=10966)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1828 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6256` → IC=+0.153 (n=10966)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6256 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.206 (n=2392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.6099` → IC=+0.189 (n=5339)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6099 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.193 (n=15404)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 88.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.192 (n=7120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0058 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0802` → IC=+0.221 (n=5379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0802 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=6112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5231` → IC=+0.239 (n=16135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5231 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.1821` → IC=+0.176 (n=11673)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1821 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.574` → IC=+0.192 (n=2575)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.574 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.527` → IC=+0.189 (n=14355)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 2.527 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1821` → IC=+0.163 (n=11495)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1821 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.217 (n=2416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6337` → IC=+0.192 (n=5112)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6337 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.196 (n=15117)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 92.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.227 (n=907)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1042` → IC=+0.258 (n=1195)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1042 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=2824)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.230 (n=1838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.813` → IC=+0.274 (n=2423)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.813 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.53` → IC=+0.331 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.53 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.296 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.834` → IC=+0.224 (n=1724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.834 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.229 (n=2585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=3004)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.258 (n=2196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.255 (n=994)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.097` → IC=+0.310 (n=966)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.097 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.259 (n=2261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.261 (n=1044)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.0492` → IC=+0.299 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0492 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.258 (n=1924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.3015` → IC=+0.275 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3015 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4466` → IC=+0.276 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4466 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.7028` → IC=+0.258 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7028 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=2527)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1785.4165` → IC=+0.261 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1785.4165 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.254 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.199 (n=843)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0648` → IC=+0.177 (n=838)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0648 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.2619` → IC=+0.209 (n=2509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2619 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1844` → IC=+0.212 (n=1269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1844 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.721` → IC=+0.207 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.721 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6953` → IC=+0.138 (n=1104)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6953 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `1.0587` → IC=+0.136 (n=1138)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.0587 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.175 (n=392)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.5038` → IC=+0.141 (n=1085)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5038 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.4677` → IC=+0.148 (n=822)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.4677 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `401.0` → IC=+0.136 (n=2433)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 401.0 (IC base=+0.131)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.172 (n=2659)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0064 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.2365` → IC=+0.169 (n=2339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.2365 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=1274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6098` → IC=+0.207 (n=2658)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6098 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.899` → IC=+0.173 (n=497)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 10.899 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.001` → IC=+0.151 (n=2318)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.001 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.2024` → IC=+0.159 (n=2658)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2024 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.0937` → IC=+0.148 (n=2300)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0937 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4576` → IC=+0.150 (n=2533)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4576 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `211.0` → IC=+0.184 (n=1085)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 211.0 (IC base=+0.146)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.232 (n=1271)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3907` → IC=+0.225 (n=2458)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3907 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=1481)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.1` → IC=+0.303 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.1 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.353` → IC=+0.236 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.353 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7154` → IC=+0.225 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7154 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=3376)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1915.9532` → IC=+0.223 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.9532 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.249 (n=2155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.4139` → IC=+0.261 (n=2155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4139 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.282 (n=942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0339` → IC=+0.291 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0339 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.068` → IC=+0.282 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.068 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3584` → IC=+0.283 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3584 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7719` → IC=+0.239 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7719 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.1845` → IC=+0.249 (n=1575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1845 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1902.41` → IC=+0.250 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1902.41 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.243 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.207 (n=908)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0783` → IC=+0.184 (n=903)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0783 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.2535` → IC=+0.192 (n=2706)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2535 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1392` → IC=+0.186 (n=1580)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1392 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.337` → IC=+0.197 (n=467)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.337 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8447` → IC=+0.137 (n=1805)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8447 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.172 (n=409)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.824` → IC=+0.129 (n=1767)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.824 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.5215` → IC=+0.149 (n=884)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.5215 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6876.6558` → IC=+0.196 (n=1227)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6876.6558 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.135 (n=2649)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 128.0 (IC base=+0.131)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.165 (n=2538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0066 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3937` → IC=+0.145 (n=2881)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3937 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6746` → IC=+0.186 (n=2882)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6746 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.16` → IC=+0.156 (n=2904)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.16 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.272` → IC=+0.141 (n=689)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.272 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6847` → IC=+0.159 (n=1268)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6847 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.177 (n=429)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.8035` → IC=+0.132 (n=1821)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8035 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.5328` → IC=+0.132 (n=910)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.5328 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `6314.0593` → IC=+0.189 (n=1306)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 6314.0593 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.150 (n=907)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 49.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.166 (n=1373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0112 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.158 (n=1443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.4731` → IC=+0.207 (n=3017)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4731 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.1966` → IC=+0.189 (n=1646)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1966 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.06` → IC=+0.286 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.06 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1747` → IC=+0.133 (n=3017)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1747 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.121 (n=3017)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.6297 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.127 (n=3073)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.7798` → IC=+0.128 (n=1951)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7798 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=3155)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2660.8307` → IC=+0.197 (n=1368)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2660.8307 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.145 (n=1285)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 20.0 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.141 (n=3152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0118 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1111` → IC=+0.162 (n=1051)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1111 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=3220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.218 (n=3155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.65 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.2125` → IC=+0.142 (n=3081)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2125 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.271` → IC=+0.137 (n=2785)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.271 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.174` → IC=+0.126 (n=3152)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.174 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.137 (n=431)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4331` → IC=+0.130 (n=992)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4331 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.4306` → IC=+0.127 (n=992)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4306 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2903.4398` → IC=+0.192 (n=1051)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2903.4398 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.123 (n=1350)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 19.0 (IC base=+0.117)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.247 (n=2735)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1665` → IC=+0.238 (n=1204)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1665 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=2842)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2464)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.257 (n=2737)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1817` → IC=+0.234 (n=1701)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1817 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.8086` → IC=+0.225 (n=2815)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8086 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.577` → IC=+0.255 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.577 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6234` → IC=+0.234 (n=2735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6234 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2351` → IC=+0.271 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2351 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `2.472` → IC=+0.228 (n=2667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.472 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.815` → IC=+0.233 (n=1778)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.815 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2842.8404` → IC=+0.231 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2842.8404 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.241 (n=1235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.248 (n=1272)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0228 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.5739` → IC=+0.247 (n=2806)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5739 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=1255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.264 (n=2818)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `1.1358` → IC=+0.260 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1358 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.033` → IC=+0.267 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.033 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `0.8643` → IC=+0.243 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8643 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `0.64` → IC=+0.242 (n=2805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.64 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.290 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `2.5284` → IC=+0.235 (n=2641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5284 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.4366` → IC=+0.240 (n=2640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4366 (IC base=+0.239)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.209 (n=1418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.1325` → IC=+0.175 (n=1870)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.1325 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=4451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.3091` → IC=+0.198 (n=4246)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3091 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.2208` → IC=+0.185 (n=1655)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.2208 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.632` → IC=+0.211 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.632 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.171 (n=2581)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8616 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `1.1931` → IC=+0.170 (n=1290)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1931 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.0982` → IC=+0.173 (n=1521)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0982 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.5284` → IC=+0.167 (n=1822)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5284 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.8129` → IC=+0.163 (n=2758)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8129 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=4757)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `8030.3267` → IC=+0.184 (n=1925)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 8030.3267 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.171 (n=3055)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.3846 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.136 (n=1965)

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

- **PATRÓN** `volumen_pendiente_norm` > `0.1607` → IC=+0.137 (n=362)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1607 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.179 (n=599)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 162.0 (IC base=+0.090)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.239 (n=580)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.2091` → IC=+0.167 (n=878)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2091 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=1371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.804` → IC=+0.261 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.804 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.8171` → IC=+0.192 (n=222)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.8171 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.87` → IC=+0.214 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.87 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.8313` → IC=+0.175 (n=878)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8313 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `1.156` → IC=+0.167 (n=439)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.156 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2183` → IC=+0.207 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2183 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.4778` → IC=+0.185 (n=433)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4778 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `8271.6703` → IC=+0.174 (n=597)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 8271.6703 (IC base=+0.165)

- **PATRÓN** `ibs_20min` < `0.0901` → IC=+0.196 (n=429)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.0901 (IC base=+0.083)

- **PATRÓN** `libro_liquidez` > `5151.7169` → IC=+0.135 (n=857)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 5151.7169 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.124 (n=546)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 42.0 (IC base=+0.083)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.155 (n=468)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0073 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.168 (n=749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.4571` → IC=+0.183 (n=1065)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.4571 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.9447` → IC=+0.185 (n=182)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.9447 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.876` → IC=+0.230 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.876 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.0475` → IC=+0.136 (n=935)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.0475 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `0.7037` → IC=+0.139 (n=949)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.7037 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2257` → IC=+0.158 (n=194)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2257 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `2.4017` → IC=+0.133 (n=1027)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.4017 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.802` → IC=+0.126 (n=685)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.802 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=1117)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2731.7361` → IC=+0.165 (n=482)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2731.7361 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.3667` → IC=+0.182 (n=775)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.3667 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `2614.2777` → IC=+0.150 (n=526)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2614.2777 (IC base=+0.065)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0174` → IC=+0.241 (n=245)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0174 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=171)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.725` → IC=+0.217 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.725 (IC base=+0.195)

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
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.230 (n=7184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=22479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.4314` → IC=+0.228 (n=21554)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4314 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.8853` → IC=+0.213 (n=2596)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8853 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.963` → IC=+0.256 (n=5276)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.963 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2166` → IC=+0.159 (n=14507)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2166 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2412` → IC=+0.207 (n=3881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2412 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6203` → IC=+0.194 (n=7013)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6203 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.202 (n=20214)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 104.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.199 (n=8694)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.006 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.201 (n=6592)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.4806` → IC=+0.197 (n=19755)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4806 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=7410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` < `0.591` → IC=+0.243 (n=19756)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.591 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.1797` → IC=+0.175 (n=12400)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1797 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.196 (n=2675)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.396` → IC=+0.198 (n=19240)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 3.396 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `0.7019` → IC=+0.174 (n=5840)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7019 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.2923` → IC=+0.251 (n=2717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2923 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.6296` → IC=+0.205 (n=6294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6296 (IC base=+0.194)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.209 (n=18658)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.194)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1677)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=2324)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.9738` → IC=+0.323 (n=1566)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9738 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.554` → IC=+0.337 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.554 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.298 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.2898` → IC=+0.242 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2898 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.251 (n=3782)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2047.52` → IC=+0.237 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2047.52 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.258 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.269 (n=3063)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1215` → IC=+0.293 (n=1349)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1215 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=2823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.268 (n=2773)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.5421` → IC=+0.284 (n=3062)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5421 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.270 (n=2784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.285 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.5595` → IC=+0.269 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5595 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.6526` → IC=+0.276 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6526 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.269 (n=3520)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `1784.2` → IC=+0.274 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1784.2 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.277 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.164 (n=2356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0045 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0784` → IC=+0.149 (n=1175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0784 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=3674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.199` → IC=+0.188 (n=3524)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.199 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3207` → IC=+0.198 (n=1165)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3207 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.193` → IC=+0.163 (n=565)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.193 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6354` → IC=+0.154 (n=1175)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6354 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0691` → IC=+0.141 (n=1599)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.0691 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.178 (n=501)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1558` → IC=+0.140 (n=3044)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.1558 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5162` → IC=+0.140 (n=3090)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.5162 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `303.0` → IC=+0.150 (n=2267)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 303.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.163 (n=3021)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0064 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.168 (n=1007)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=1113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6801` → IC=+0.185 (n=3019)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6801 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.997` → IC=+0.138 (n=2730)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.997 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.0503` → IC=+0.149 (n=2657)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0503 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2191` → IC=+0.193 (n=558)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2191 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4238` → IC=+0.142 (n=2909)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4238 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7696` → IC=+0.141 (n=1939)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7696 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=3920)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `226.0` → IC=+0.153 (n=949)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 226.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.243 (n=2395)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=3213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.04` → IC=+0.325 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.04 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.229 (n=3215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.3498` → IC=+0.227 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3498 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.7332` → IC=+0.242 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7332 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=4335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `1919.501` → IC=+0.238 (n=1629)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.501 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.250 (n=3012)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1777` → IC=+0.266 (n=1505)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1777 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.0581` → IC=+0.302 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0581 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.158` → IC=+0.302 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.158 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.349` → IC=+0.300 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.349 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.1738` → IC=+0.254 (n=2194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1738 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.250 (n=1744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1906.6648` → IC=+0.256 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1906.6648 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.253 (n=2218)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.243)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.193 (n=1246)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0037 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4307` → IC=+0.144 (n=3728)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4307 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=3869)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.8899` → IC=+0.272 (n=1243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8899 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.1961` → IC=+0.167 (n=1705)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1961 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.959` → IC=+0.155 (n=1658)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.959 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6176` → IC=+0.155 (n=1243)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6176 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.185 (n=665)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5199` → IC=+0.149 (n=1605)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5199 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.1809` → IC=+0.143 (n=1652)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.1809 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5516.8147` → IC=+0.226 (n=1690)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5516.8147 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.143 (n=2419)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 89.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.169 (n=2747)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0067 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.4356` → IC=+0.154 (n=3121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4356 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=1154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.5791` → IC=+0.210 (n=2747)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5791 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1533` → IC=+0.158 (n=2910)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1533 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.843` → IC=+0.152 (n=461)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 10.843 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.044` → IC=+0.147 (n=2719)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.044 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.6889` → IC=+0.160 (n=1374)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6889 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.212 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.2097` → IC=+0.146 (n=2651)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.2097 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.5337` → IC=+0.152 (n=2691)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5337 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `6363.1832` → IC=+0.216 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6363.1832 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.155 (n=2054)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 92.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.150 (n=1717)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0112 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=2674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4324` → IC=+0.191 (n=3777)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4324 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.01` → IC=+0.201 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.01 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.264` → IC=+0.268 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.264 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2155` → IC=+0.125 (n=3778)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.2155 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1012` → IC=+0.121 (n=3584)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1012 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `2.4921` → IC=+0.121 (n=3691)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4921 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2714.6923` → IC=+0.240 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2714.6923 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.152 (n=3136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0108 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.1366` → IC=+0.153 (n=1187)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1366 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=1678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.214 (n=3579)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.141 (n=3216)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.045` → IC=+0.148 (n=3446)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.045 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.6376` → IC=+0.152 (n=1187)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6376 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.175 (n=620)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.4341` → IC=+0.155 (n=1125)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4341 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2620.7147` → IC=+0.209 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2620.7147 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.139 (n=3026)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 43.0 (IC base=+0.126)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.258 (n=3479)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=3639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.240 (n=3117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.6152` → IC=+0.271 (n=3108)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6152 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.1948` → IC=+0.253 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1948 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.173` → IC=+0.287 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.173 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2203` → IC=+0.239 (n=3480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2203 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.242 (n=3479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2382` → IC=+0.258 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2382 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.4972` → IC=+0.257 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4972 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2970.8526` → IC=+0.243 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2970.8526 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0259` → IC=+0.266 (n=1194)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0259 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.6292` → IC=+0.242 (n=3577)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6292 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.247 (n=3371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.4372` → IC=+0.276 (n=3147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4372 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` < `0.2201` → IC=+0.249 (n=3389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2201 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.162` → IC=+0.281 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.162 (IC base=+0.242)

- **PATRÓN** `volumen_regimen` > `1.2193` → IC=+0.264 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2193 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.303 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.4351` → IC=+0.245 (n=3366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4351 (IC base=+0.242)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=5787)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.244 (n=1989)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.5046` → IC=+0.227 (n=5964)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5046 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=2160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9351` → IC=+0.255 (n=1988)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9351 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.4287` → IC=+0.221 (n=4339)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4287 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.557` → IC=+0.225 (n=1957)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.557 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `0.7085` → IC=+0.229 (n=1934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7085 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.8836` → IC=+0.219 (n=2931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8836 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.219 (n=5564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.225 (n=1682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `2.2564` → IC=+0.222 (n=5166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2564 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.224 (n=4650)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `2880.2512` → IC=+0.223 (n=5327)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2880.2512 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.236 (n=1451)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.211 (n=4352)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.214 (n=1924)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.7297` → IC=+0.207 (n=4352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7297 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.657` → IC=+0.210 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.657 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.764` → IC=+0.211 (n=3907)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.764 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.0948` → IC=+0.205 (n=3652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0948 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.200 (n=4009)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.201 (n=1941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.5315` → IC=+0.203 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5315 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.1859` → IC=+0.206 (n=1945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1859 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=5787)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.214 (n=2861)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.199)

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
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.225 (n=613)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.5868` → IC=+0.210 (n=920)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5868 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.229 (n=426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.3947` → IC=+0.202 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3947 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.248 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.424` → IC=+0.251 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.424 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2054` → IC=+0.235 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2054 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `3.3701` → IC=+0.202 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.3701 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.8037` → IC=+0.209 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8037 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2777.751` → IC=+0.238 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2777.751 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.210 (n=647)

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
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.217 (n=1631)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.4542` → IC=+0.211 (n=1630)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4542 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.5015` → IC=+0.216 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5015 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.8556` → IC=+0.205 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8556 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.3955` → IC=+0.213 (n=1633)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3955 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.529` → IC=+0.209 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.529 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.209 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `1.2249` → IC=+0.205 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2249 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` < `0.1029` → IC=+0.208 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1029 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.1597` → IC=+0.214 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1597 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.242 (n=452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.484` → IC=+0.221 (n=1356)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.484 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.209 (n=513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.218 (n=917)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.7445` → IC=+0.203 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7445 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.0937` → IC=+0.205 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0937 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.6225` → IC=+0.219 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6225 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.855` → IC=+0.201 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.855 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.346` → IC=+0.205 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.346 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.6387` → IC=+0.227 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6387 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.228 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.1859` → IC=+0.206 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1859 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `6408.237` → IC=+0.206 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6408.237 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.201 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.200)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.224 (n=636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.235 (n=670)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.7677` → IC=+0.239 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7677 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.202` → IC=+0.224 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.202 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.6421` → IC=+0.247 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6421 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.207 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.0792` → IC=+0.204 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0792 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `2.1469` → IC=+0.205 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1469 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.4745` → IC=+0.204 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4745 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.208 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4320.729` → IC=+0.244 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4320.729 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.204 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.220 (n=613)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.234 (n=464)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.5947` → IC=+0.237 (n=697)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5947 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.250 (n=482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.6522` → IC=+0.252 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6522 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.5279` → IC=+0.222 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5279 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.776` → IC=+0.235 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.776 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `0.9181` → IC=+0.224 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9181 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.2706` → IC=+0.227 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2706 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.0838` → IC=+0.236 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0838 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.6023` → IC=+0.259 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6023 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `3782.8762` → IC=+0.234 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3782.8762 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.256 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.220)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` > `0.5106` → IC=-0.122 (n=636)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5106
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=1236)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.150 (n=716)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0038 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.185 (n=1382)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.75 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1458` → IC=+0.139 (n=1027)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1458 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.462` → IC=+0.147 (n=457)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.462 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.266 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.1463` → IC=+0.134 (n=386)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1463 (IC base=+0.045)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.536` → IC=-0.125 (n=286)

  - _Acción_: SKIP cuando `ibs_20min` < 0.536
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=583)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.127 (n=601)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0052 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.536` → IC=+0.167 (n=583)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.536 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.165 (n=314)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.070)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.131 (n=258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0034 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.0742` → IC=+0.275 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0742 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2173` → IC=+0.164 (n=111)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2173 (IC base=+0.046)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.5456` → IC=-0.120 (n=293)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5456
  - _Potencial_: sin este filtro IC_bueno=+0.170 (n=595)

- **FILTRO** `ibs_20min` > `0.686` → IC=-0.173 (n=151)

  - _Acción_: SKIP cuando `ibs_20min` > 0.686
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=454)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.144 (n=307)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0041 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.5456` → IC=+0.170 (n=595)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.5456 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1272` → IC=+0.173 (n=328)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1272 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.717` → IC=+0.202 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.717 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.266 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.593` → IC=+0.200 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.593 (IC base=+0.019)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.195 (n=247)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 1.0 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.7189` → IC=+0.132 (n=172)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.7189 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.688` → IC=+0.142 (n=160)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 8.688 (IC base=+0.020)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.145 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0112 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.173 (n=390)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.1874` → IC=+0.131 (n=375)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1874 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.852` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.852 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.0862` → IC=+0.174 (n=130)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.0862 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1539` → IC=+0.173 (n=111)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1539 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.8478` → IC=+0.143 (n=242)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8478 (IC base=+0.073)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0058` → IC=-0.243 (n=185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=185)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.338 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=292)

- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=354)

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
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=89)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=114)

- **FILTRO** `dist_vwap_pct` > `0.0702` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0702
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=103)

- **FILTRO** `volumen_pendiente_norm` > `0.1329` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1329
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=76)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=102)

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

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.238 (n=227)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.193 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.6786` → IC=+0.179 (n=680)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6786 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.8076` → IC=+0.278 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8076 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.153 (n=373)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.564` → IC=+0.144 (n=692)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 8.564 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.181 (n=227)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6249 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.2094` → IC=+0.166 (n=639)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.2094 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.3906` → IC=+0.191 (n=192)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.3906 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.53` → IC=+0.156 (n=190)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 10.53 (IC base=+0.034)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7797` → IC=-0.133 (n=88)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7797
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=181)

- **PATRÓN** `ibs_20min` > `0.7797` → IC=+0.123 (n=181)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.7797 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.6135` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6135 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.215` → IC=+0.147 (n=383)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.215 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.339` → IC=+0.133 (n=88)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 11.339 (IC base=+0.088)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.145 (n=150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0042 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1025` → IC=+0.134 (n=99)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1025 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.171 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 18.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.127 (n=108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 8.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.7964` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.7964 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.0973` → IC=+0.154 (n=183)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.0973 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.502` → IC=+0.148 (n=234)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 9.502 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.175 (n=75)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6244 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `1.1935` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1935 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.187` → IC=+0.151 (n=236)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.187 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.7623` → IC=+0.169 (n=131)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.7623 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=192)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.584` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.584 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2839` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2839 (IC base=+0.014)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=127)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=1433)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.098)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=1433)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.098)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=714)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3900)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1592)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1546)

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
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=977)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=977)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1193)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1193)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=273)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=273)

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
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=392)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=392)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=237)

- **FILTRO** `libro_liquidez` < `662.0335` → IC=-0.131 (n=139)

  - _Acción_: SKIP cuando `libro_liquidez` < 662.0335
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=283)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=340)

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
- **FILTRO** `py_entrada` > `0.57` → IC=-0.121 (n=333)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=349)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.122 (n=329)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=388)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.169 (n=143)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=629)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.123 (n=518)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=274)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.135 (n=113)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=348)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.173 (n=7620)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=24368)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.175 (n=8106)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=24861)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.183 (n=1465)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=4447)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.148 (n=1955)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=3891)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.133 (n=1534)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.124 (n=2986)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.505 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.171 (n=1054)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=3418)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.180 (n=1159)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3490)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=1450)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4533)

- **PATRÓN** `ibs_20min` > `0.9635` → IC=+0.133 (n=2011)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.9635 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1751.66` → IC=+0.123 (n=2010)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1751.66 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.181 (n=1101)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=3605)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.159 (n=1467)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4479)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2432)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2356)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3006)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3958)

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
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1055)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

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
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=779)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.134 (n=21780)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=49035)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=16904)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=53911)

- **FILTRO** `ibs_7min` < `0.2195` → IC=-0.232 (n=17703)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2195
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=53112)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=23263)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=47552)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.251 (n=20684)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=68016)

- **FILTRO** `ibs_7min` > `0.283` → IC=-0.184 (n=22167)

  - _Acción_: SKIP cuando `ibs_7min` > 0.283
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=66533)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.155 (n=3060)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=9520)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.319 (n=3093)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=9487)

- **FILTRO** `ibs_7min` < `0.7104` → IC=-0.251 (n=4150)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7104
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=8430)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.152 (n=2762)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=9818)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.276 (n=3716)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=11611)

- **FILTRO** `ibs_7min` > `0.775` → IC=-0.212 (n=3831)

  - _Acción_: SKIP cuando `ibs_7min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=11496)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2831)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=8972)

- **FILTRO** `ibs_7min` < `0.7153` → IC=-0.207 (n=2948)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7153
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=8855)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.198 (n=2942)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8861)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2764)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9300)

- **FILTRO** `ibs_7min` > `0.2662` → IC=-0.195 (n=3015)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2662
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=9049)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.182 (n=3008)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=9056)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.165 (n=2910)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9134)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.324 (n=2859)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=9185)

- **FILTRO** `ibs_7min` < `0.2883` → IC=-0.249 (n=3974)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2883
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=8070)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.200 (n=2449)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=9595)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.257 (n=3920)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=12312)

- **FILTRO** `ibs_7min` > `0.7321` → IC=-0.183 (n=4056)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7321
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=12176)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.260 (n=2831)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=8631)

- **FILTRO** `ibs_7min` < `0.7171` → IC=-0.194 (n=2865)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7171
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8597)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.188 (n=2810)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8652)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=2758)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=9186)

- **FILTRO** `ibs_7min` > `0.2744` → IC=-0.176 (n=2985)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2744
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=8959)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.170 (n=2924)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=9020)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=2676)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8697)

- **FILTRO** `ibs_7min` < `0.7027` → IC=-0.230 (n=3750)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7027
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=7623)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.216 (n=2825)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8548)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.197 (n=4152)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=13000)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=3715)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=7838)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.307 (n=2733)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=8820)

- **FILTRO** `ibs_7min` < `0.1667` → IC=-0.229 (n=2881)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1667
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8672)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=2582)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=8971)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=3704)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=12277)

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
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=885)

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
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=672)

- **FILTRO** `libro_liquidez` < `3302.3462` → IC=-0.155 (n=192)

  - _Acción_: SKIP cuando `libro_liquidez` < 3302.3462
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=578)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=394)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4307` → IC=+0.152 (n=665)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4307 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.131 (n=752)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 6.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `418.1326` → IC=+0.162 (n=489)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 418.1326 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3556.2094` → IC=+0.140 (n=665)

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
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.141 (n=263)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 14.0 (IC base=+0.120)

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
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.169 (n=252)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.142)

- **PATRÓN** `total_vol_5m` < `4621.455` → IC=+0.178 (n=169)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 4621.455 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.147 (n=114)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 27.0 (IC base=+0.142)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=201)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.094)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `2.8683` → IC=-0.193 (n=148)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8683
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=74)

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
- **FILTRO** `sigma_h` > `0.0049` → IC=-0.191 (n=163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0049
  - _Potencial_: sin este filtro IC_bueno=+0.277 (n=83)

- **FILTRO** `T_h` > `88.1766` → IC=-0.230 (n=61)

  - _Acción_: SKIP cuando `T_h` > 88.1766
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=185)

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
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=400)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=474)

- **PATRÓN** `streak_estiramiento` < `0.2898` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.2898 (IC base=+0.028)

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
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=156)

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
- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4771)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2748)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.190 (n=1689)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0053 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2172` → IC=+0.162 (n=5057)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2172 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3567` → IC=+0.155 (n=4706)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3567 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.156 (n=4675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 6.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5882` → IC=+0.232 (n=4522)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5882 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1327` → IC=+0.140 (n=2396)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1327 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.5055` → IC=+0.133 (n=4703)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.5055 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.394` → IC=+0.258 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.394 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=2962)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `4653.0512` → IC=+0.170 (n=1686)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4653.0512 (IC base=+0.147)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1940)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.220 (n=768)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.257 (n=257)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2674` → IC=+0.221 (n=256)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2674 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.219 (n=801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.201)

- **PATRÓN** `ibs_15` > `0.7086` → IC=+0.274 (n=768)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7086 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.3749` → IC=+0.225 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3749 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.5123` → IC=+0.205 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5123 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.596` → IC=+0.300 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.596 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `11907.94` → IC=+0.218 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11907.94 (IC base=+0.201)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.147 (n=945)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.007 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.144 (n=630)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1407` → IC=+0.134 (n=631)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.1407 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.134 (n=865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.133 (n=993)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.217 (n=945)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1169` → IC=+0.150 (n=592)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1169 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.4287` → IC=+0.131 (n=999)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.4287 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.857` → IC=+0.282 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.857 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5881.5817` → IC=+0.161 (n=429)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5881.5817 (IC base=+0.131)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2521` → IC=-0.122 (n=199)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2521
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=387)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.6` → IC=+0.135 (n=919)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` > 0.6 (IC base=+0.060)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0252` → IC=+0.175 (n=1232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0252 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.169 (n=1232)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0133 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.2194` → IC=+0.180 (n=1232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.2194 (IC base=+0.164)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0978` → IC=+0.220 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0978 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.172 (n=1129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.171 (n=1089)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 14.0 (IC base=+0.164)

- **PATRÓN** `ibs_15` > `0.5542` → IC=+0.246 (n=1101)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5542 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.1322` → IC=+0.193 (n=665)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1322 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.942` → IC=+0.214 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.942 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `2739.8268` → IC=+0.192 (n=822)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2739.8268 (IC base=+0.164)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.156 (n=973)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1111 (IC base=+0.067)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.387 (n=245)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1122` → IC=+0.364 (n=491)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1122 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.376 (n=490)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.107` → IC=+0.376 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.107 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.370 (n=777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.363 (n=493)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.7903` → IC=+0.393 (n=735)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7903 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.378 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.976` → IC=+0.398 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.976 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `9788.5606` → IC=+0.381 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9788.5606 (IC base=+0.362)

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

- **PATRÓN** `libro_liquidez` > `8119.484` → IC=+0.385 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8119.484 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.403 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.367 (n=373)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.377 (n=169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.361)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.365 (n=250)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0824` → IC=+0.372 (n=333)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0824 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.372 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.364 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.361)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.762` → IC=+0.390 (n=372)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.762 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.1212` → IC=+0.369 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1212 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` < `0.2798` → IC=+0.364 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2798 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.402 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.361)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `4132.469` → IC=+0.377 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4132.469 (IC base=+0.361)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.192 (n=2623)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2625)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.217 (n=2190)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3058)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.220 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.080)

- **PATRÓN** `ibs_15` > `0.6296` → IC=+0.278 (n=1199)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6296 (IC base=-0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1102` → IC=+0.202 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1102 (IC base=-0.080)

- **PATRÓN** `dist_vwap_pct` < `0.5575` → IC=+0.198 (n=1267)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.5575 (IC base=-0.080)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2353` → IC=+0.272 (n=1582)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2353 (IC base=-0.005)

- **PATRÓN** `ibs_15` < `0.3684` → IC=+0.285 (n=4748)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3684 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` > `0.6531` → IC=+0.281 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6531 (IC base=-0.005)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0318` → IC=-0.222 (n=2473)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0318
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=825)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.218 (n=824)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2474)

- **FILTRO** `sigma_ewma_delta_pct` > `22.231` → IC=-0.257 (n=472)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.231
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=2826)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.151 (n=319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.003 (IC base=+0.070)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.279 (n=138)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.070)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.267 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.070)

- **PATRÓN** `ibs_15` > `0.7593` → IC=+0.325 (n=414)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7593 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1039` → IC=+0.278 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1039 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.4928` → IC=+0.284 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4928 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.409` → IC=+0.147 (n=216)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 22.409 (IC base=+0.070)

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
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=784)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.159 (n=529)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0059 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.178 (n=265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3021` → IC=+0.194 (n=469)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3021 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.157 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5684` → IC=+0.240 (n=601)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5684 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1135` → IC=+0.152 (n=374)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1135 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.2713` → IC=+0.148 (n=561)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2713 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.028` → IC=+0.263 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.028 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=784)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `5050.7283` → IC=+0.155 (n=401)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 5050.7283 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.252 (n=1807)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.356` → IC=+0.249 (n=1590)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.356 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7762` → IC=+0.260 (n=1590)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7762 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2145` → IC=+0.266 (n=820)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2145 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.244 (n=1229)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.2974` → IC=+0.285 (n=1590)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2974 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6025` → IC=+0.273 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6025 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.253` → IC=+0.248 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.253 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.183` → IC=-0.258 (n=304)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.183
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=913)

- **FILTRO** `drift_60min` |x|> `0.1723` → IC=-0.257 (n=413)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1723
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=804)

- **FILTRO** `drift_15min` |x|> `0.9075` → IC=-0.281 (n=304)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9075
  - _Potencial_: sin este filtro IC_bueno=-0.166 (n=913)

- **FILTRO** `sigma_ewma_delta_pct` > `6.159` → IC=-0.201 (n=282)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.159
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=935)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.217 (n=238)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.0639` → IC=+0.232 (n=807)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0639 (IC base=-0.031)

- **PATRÓN** `ibs_15` < `0.383` → IC=+0.294 (n=807)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.383 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.6765` → IC=+0.238 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6765 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.193` → IC=+0.243 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.193 (IC base=-0.031)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0131` → IC=-0.241 (n=1106)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0131
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=369)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.216)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.216)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1192` → IC=+0.278 (n=738)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1192 (IC base=-0.019)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0947` → IC=+0.298 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0947 (IC base=-0.019)

- **PATRÓN** `ibs_15` < `0.1351` → IC=+0.311 (n=738)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1351 (IC base=-0.019)

- **PATRÓN** `dist_vwap_pct` > `0.7727` → IC=+0.339 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7727 (IC base=-0.019)

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
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.297 (n=437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0725` → IC=+0.310 (n=577)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0725 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.285 (n=873)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.223` → IC=+0.291 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.223 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.296 (n=1353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.311 (n=1311)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.2631` → IC=+0.314 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2631 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.011` → IC=+0.388 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.011 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `13318.0241` → IC=+0.306 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13318.0241 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.303 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.275)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.277 (n=316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.316 (n=232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2694` → IC=+0.275 (n=233)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2694 (IC base=+0.275)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3948` → IC=+0.280 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3948 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.294 (n=727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.275)

- **PATRÓN** `ibs_15` > `0.8612` → IC=+0.309 (n=622)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8612 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2502` → IC=+0.311 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2502 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.915` → IC=+0.391 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.915 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `14792.3098` → IC=+0.308 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14792.3098 (IC base=+0.275)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.301 (n=616)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.312 (n=206)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1412` → IC=+0.294 (n=410)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1412 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1008` → IC=+0.324 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1008 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.302 (n=589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.295 (n=564)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8486` → IC=+0.319 (n=615)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8486 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.315 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.34` → IC=+0.377 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.34 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0848` → IC=-0.157 (n=246)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0848
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=83)

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
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=48)

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

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0863` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0863
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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5882 sube el IC de +0.147 a +0.232 en UPDOWN_GBM#15min (n=4522). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7086 sube el IC de +0.201 a +0.274 en UPDOWN_GBM#BTC#15min (n=768). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.131 a +0.217 en UPDOWN_GBM#ETH#15min (n=945). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5542 sube el IC de +0.164 a +0.246 en UPDOWN_GBM#XRP#15min (n=1101). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.067 a +0.156 en UPDOWN_GBM#XRP#15min (n=973). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6296 sube el IC de -0.080 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1199). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3684 sube el IC de -0.005 a +0.285 en UPDOWN_GBM_15M_TARDIO (n=4748). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.070 a +0.325 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=414). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.186 a +0.300 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=73). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5684 sube el IC de +0.145 a +0.240 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=601). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2974 sube el IC de +0.244 a +0.285 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1590). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.195 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.383 sube el IC de -0.031 a +0.294 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=807). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.216 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1351 sube el IC de -0.019 a +0.311 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=738). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.097 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7 (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.097 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.282 a +0.311 en UPDOWN_GBM_IBS_ALTO (n=1311). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8612 sube el IC de +0.275 a +0.309 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=622). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8486 sube el IC de +0.289 a +0.319 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=615). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7903 sube el IC de +0.362 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=735). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.385 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=363). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.762 sube el IC de +0.361 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=372). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2157 | +0.085 | +230.09€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2157 | +0.085 | +230.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1752 | +0.085 | +190.80€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1752 | +0.085 | +190.80€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 90 | +0.130 | +28.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 90 | +0.130 | +28.32€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1092 | -0.024 | +68.91€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1092 | -0.024 | +68.91€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 844 | -0.038 | +55.64€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 844 | -0.038 | +55.64€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 164 | +0.048 | +16.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 164 | +0.048 | +16.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 46342 | -0.086 | -5892.20€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2797 | +0.061 | -296.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 43545 | -0.095 | -5596.12€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4767 | -0.112 | -801.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4767 | -0.112 | -801.24€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2797 | +0.061 | -296.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2797 | +0.061 | -296.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4808 | -0.109 | -929.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4808 | -0.109 | -929.78€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12645 | -0.043 | -1168.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12645 | -0.043 | -1168.47€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12557 | -0.113 | -1263.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12557 | -0.113 | -1263.48€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8768 | -0.128 | -1433.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8768 | -0.128 | -1433.14€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 46999 | -0.012 | +2935.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 12137 | +0.005 | +1548.52€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 34862 | -0.018 | +1387.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 46999 | -0.012 | +2935.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 12137 | +0.005 | +1548.52€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 34862 | -0.018 | +1387.35€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 181634 | +0.113 | -7612.59€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21371 | +0.180 | -680.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 831 | +0.004 | -78.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 148999 | +0.105 | -6478.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10433 | +0.093 | -375.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 24693 | +0.102 | -1739.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 75 | -0.175 | +11.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 24603 | +0.104 | -1738.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 34550 | +0.124 | -591.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5593 | +0.179 | -226.13€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 24671 | +0.120 | -191.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4244 | +0.079 | -151.52€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 24741 | +0.098 | -1815.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 84 | -0.116 | +5.91€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 24642 | +0.099 | -1810.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 38771 | +0.123 | -822.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9808 | +0.177 | -234.67€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 25052 | +0.105 | -529.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3899 | +0.103 | -49.30€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 34162 | +0.112 | -1528.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5726 | +0.199 | -244.06€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 734 | +0.031 | -24.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 25412 | +0.096 | -1085.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2290 | +0.102 | -174.35€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 24717 | +0.106 | -1114.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 85 | -0.121 | +7.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 24619 | +0.107 | -1122.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 29421 | +0.193 | -1990.68€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 29421 | +0.193 | -1990.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6651 | +0.173 | -644.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6651 | +0.173 | -644.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4181 | +0.197 | -153.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4181 | +0.197 | -153.62€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6543 | +0.176 | -561.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6543 | +0.176 | -561.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5515 | +0.249 | -202.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5515 | +0.249 | -202.79€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6452 | +0.185 | -442.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6452 | +0.185 | -442.50€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1210 | +0.426 | -44.47€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1210 | +0.426 | -44.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 494 | +0.440 | -4.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 494 | +0.440 | -4.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 489 | +0.425 | -17.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 489 | +0.425 | -17.89€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 103884 | +0.199 | -7670.58€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 103884 | +0.199 | -7670.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 17936 | +0.179 | -2014.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 17936 | +0.179 | -2014.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 16748 | +0.224 | -559.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 16748 | +0.224 | -559.83€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 17833 | +0.180 | -1899.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 17833 | +0.180 | -1899.84€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 16887 | +0.217 | -686.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 16887 | +0.217 | -686.41€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 17174 | +0.202 | -1105.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 17174 | +0.202 | -1105.75€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 17306 | +0.196 | -1404.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 17306 | +0.196 | -1404.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 39965 | +0.117 | +310.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 39965 | +0.117 | +310.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 19900 | +0.117 | +188.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 19900 | +0.117 | +188.52€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 20065 | +0.116 | +122.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 20065 | +0.116 | +122.09€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2507 | +0.293 | -10.54€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2507 | +0.293 | -10.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1147 | +0.280 | -32.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1147 | +0.280 | -32.36€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1224 | +0.298 | +17.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1224 | +0.298 | +17.83€ | 0 | 4 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1908 | +0.068 | -83.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1183 | +0.081 | -19.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1474 | +0.076 | -38.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1183 | +0.081 | -19.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 80805 | +0.100 | -1954.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6517 | +0.095 | +125.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 74288 | +0.101 | -2079.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 44206 | +0.105 | -457.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6517 | +0.095 | +125.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 37689 | +0.107 | -582.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 17095 | +0.109 | -93.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 17095 | +0.109 | -93.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 19504 | +0.082 | -1403.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 19504 | +0.082 | -1403.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 54863 | +0.098 | +30337.64€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 54863 | +0.098 | +30337.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9093 | +0.225 | +7841.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9093 | +0.225 | +7841.97€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 8358 | +0.175 | +6510.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8358 | +0.175 | +6510.21€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 9851 | +0.207 | +7751.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9851 | +0.207 | +7751.04€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7422 | +0.052 | +2315.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7422 | +0.052 | +2315.03€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 7664 | -0.031 | +1990.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7664 | -0.031 | +1990.44€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 12475 | -0.024 | +3928.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 12475 | -0.024 | +3928.94€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 57787 | +0.085 | +33488.03€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 57787 | +0.085 | +33488.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 11217 | -0.002 | +6038.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 11217 | -0.002 | +6038.07€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 12382 | +0.004 | +3264.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 12382 | +0.004 | +3264.15€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7890 | +0.293 | +8959.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7890 | +0.293 | +8959.46€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 10947 | +0.014 | +3375.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 10947 | +0.014 | +3375.40€ | 1 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8933 | +0.044 | +3994.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8933 | +0.044 | +3994.10€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6418 | +0.316 | +7856.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6418 | +0.316 | +7856.85€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 43474 | +0.178 | +35768.16€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 43474 | +0.178 | +35768.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6538 | +0.240 | +6090.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6538 | +0.240 | +6090.36€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6888 | +0.139 | +5070.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6888 | +0.139 | +5070.46€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6989 | +0.224 | +6036.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6989 | +0.224 | +6036.05€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7449 | +0.130 | +5769.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7449 | +0.130 | +5769.23€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8224 | +0.119 | +6143.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8224 | +0.119 | +6143.16€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7386 | +0.232 | +6658.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7386 | +0.232 | +6658.90€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 11768 | +0.126 | +5865.68€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 11768 | +0.126 | +5865.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 468 | +0.157 | +308.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 468 | +0.157 | +308.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3344 | +0.130 | +1824.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3344 | +0.130 | +1824.17€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 505 | +0.159 | +279.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 505 | +0.159 | +279.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3468 | +0.125 | +1666.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3468 | +0.125 | +1666.81€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2962 | +0.095 | +1156.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2962 | +0.095 | +1156.28€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1021 | +0.169 | +630.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1021 | +0.169 | +630.22€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 55074 | +0.187 | +45125.20€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 55074 | +0.187 | +45125.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8686 | +0.251 | +8417.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8686 | +0.251 | +8417.98€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8722 | +0.136 | +5987.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8722 | +0.136 | +5987.34€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 9350 | +0.235 | +8442.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 9350 | +0.235 | +8442.10€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9131 | +0.139 | +6706.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9131 | +0.139 | +6706.64€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 9780 | +0.122 | +6882.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 9780 | +0.122 | +6882.62€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9405 | +0.240 | +8688.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9405 | +0.240 | +8688.52€ | 0 | 20 |
| ✅ GBM_LATE_5M | 13752 | +0.210 | +11127.54€ | 1 | 27 |
| ✅ GBM_LATE_5M#5min | 13752 | +0.210 | +11127.54€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3257 | +0.211 | +2804.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3257 | +0.211 | +2804.80€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1305 | +0.204 | +1010.70€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1305 | +0.204 | +1010.70€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3979 | +0.202 | +2959.23€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3979 | +0.202 | +2959.23€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 2198 | +0.208 | +1815.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2198 | +0.208 | +1815.40€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1959 | +0.209 | +1537.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1959 | +0.209 | +1537.13€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4833 | +0.049 | +1317.98€ | 1 | 6 |
| ✅ GBM_LATE_60M#60min | 4833 | +0.049 | +1317.98€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1690 | +0.059 | +531.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1690 | +0.059 | +531.34€ | 1 | 6 |
| ✅ GBM_LATE_60M#ETH | 1563 | +0.050 | +465.37€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1563 | +0.050 | +465.37€ | 2 | 6 |
| ✅ GBM_LATE_60M#SOL | 1580 | +0.039 | +321.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1580 | +0.039 | +321.27€ | 0 | 10 |
| 🚫 GBM_LATE_60M_FADE | 696 | -0.251 | -37.28€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 696 | -0.251 | -37.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 254 | -0.254 | -21.80€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 254 | -0.254 | -21.80€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 257 | -0.241 | -5.52€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 257 | -0.241 | -5.52€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 185 | -0.254 | -9.97€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 185 | -0.254 | -9.97€ | 8 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2004 | +0.083 | +516.56€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2004 | +0.083 | +516.56€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 779 | +0.071 | +192.61€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 779 | +0.071 | +192.61€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 702 | +0.060 | +129.36€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 702 | +0.060 | +129.36€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 523 | +0.131 | +194.60€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 523 | +0.131 | +194.60€ | 1 | 8 |
| ✅ LATE_WINDOW_5MIN | 225 | +0.293 | +252.39€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN#5min | 225 | +0.293 | +252.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 225 | +0.293 | +252.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 225 | +0.293 | +252.39€ | 1 | 13 |
| ✅ LEADLAG_BTC_XRP_15M | 4271 | +0.098 | +976.31€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4271 | +0.098 | +976.31€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4271 | +0.098 | +976.31€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4271 | +0.098 | +976.31€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 994 | -0.012 | +12.85€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 994 | -0.012 | +12.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 53 | +0.009 | +0.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 53 | +0.009 | +0.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 264 | -0.015 | +4.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 264 | -0.015 | +4.77€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 34 | -0.167 | -6.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 34 | -0.167 | -6.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 267 | +0.020 | +17.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 267 | +0.020 | +17.67€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 300 | -0.007 | +3.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 300 | -0.007 | +3.20€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 76 | -0.077 | -6.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 76 | -0.077 | -6.74€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4143 | +0.017 | +124.69€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4143 | +0.017 | +124.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 200 | +0.025 | -1.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 200 | +0.025 | -1.25€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 825 | +0.015 | +40.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 825 | +0.015 | +40.47€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 236 | +0.025 | +24.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 236 | +0.025 | +24.39€ | 0 | 2 |
| ✅ LIQUIDACIONES_5M#ETH | 1644 | +0.019 | +28.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1644 | +0.019 | +28.41€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 767 | +0.011 | +1.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 767 | +0.011 | +1.87€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 471 | +0.016 | +30.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 471 | +0.016 | +30.81€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2265 | -0.033 | -11.22€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2265 | -0.033 | -11.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 684 | -0.032 | -12.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 684 | -0.032 | -12.60€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 804 | -0.009 | +17.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 804 | -0.009 | +17.61€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 777 | -0.060 | -16.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 777 | -0.060 | -16.23€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 14386 | -0.032 | -133.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 6895 | -0.034 | -84.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 7491 | -0.030 | -48.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 509 | -0.048 | -23.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 260 | -0.015 | +7.72€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 249 | -0.082 | -30.94€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3764 | -0.025 | -10.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1789 | -0.023 | +4.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1975 | -0.027 | -14.75€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1425 | -0.028 | +13.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 728 | -0.034 | -1.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 697 | -0.022 | +15.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3250 | -0.035 | -61.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1526 | -0.038 | -39.24€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1724 | -0.033 | -22.09€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2770 | -0.026 | +19.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1339 | -0.032 | -9.42€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1431 | -0.021 | +28.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2668 | -0.043 | -71.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1253 | -0.050 | -46.98€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1415 | -0.036 | -24.84€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 64955 | -0.000 | +3479.32€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 64955 | -0.000 | +3479.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 11758 | +0.027 | +1596.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 11758 | +0.027 | +1596.85€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9121 | -0.036 | -108.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9121 | -0.036 | -108.74€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 11893 | +0.025 | +1291.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 11893 | +0.025 | +1291.08€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9036 | -0.051 | -203.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9036 | -0.051 | -203.64€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 11053 | -0.004 | +307.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 11053 | -0.004 | +307.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 12094 | +0.018 | +596.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 12094 | +0.018 | +596.46€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7108 | -0.055 | -116.79€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7108 | -0.055 | -116.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1244 | -0.002 | -15.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1244 | -0.002 | -15.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1963 | -0.065 | -28.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1963 | -0.065 | -28.52€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 71 | -0.007 | +0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 71 | -0.007 | +0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 803 | -0.119 | -34.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 803 | -0.119 | -34.10€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2165 | -0.068 | -12.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2165 | -0.068 | -12.11€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 159515 | -0.077 | +2342.96€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 159515 | -0.077 | +2342.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 27907 | -0.078 | +1575.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 27907 | -0.078 | +1575.77€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 23867 | -0.101 | -1167.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 23867 | -0.101 | -1167.90€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 28276 | -0.068 | +1417.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 28276 | -0.068 | +1417.47€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 23406 | -0.098 | -668.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 23406 | -0.098 | -668.46€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 28525 | -0.058 | +341.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 28525 | -0.058 | +341.01€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 27534 | -0.069 | +845.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 27534 | -0.069 | +845.07€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9005 | -0.035 | -181.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9005 | -0.035 | -181.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2078 | -0.047 | -28.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2078 | -0.047 | -28.27€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2636 | -0.025 | -37.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2636 | -0.025 | -37.18€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1270 | -0.065 | -32.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1270 | -0.065 | -32.51€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1010 | -0.031 | -32.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1010 | -0.031 | -32.49€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2091 | +0.119 | +824.86€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1955 | +0.123 | +812.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 468 | +0.132 | +224.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 468 | +0.132 | +224.04€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 398 | +0.120 | +141.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 398 | +0.120 | +141.62€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 368 | +0.127 | +167.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 368 | +0.127 | +167.79€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 336 | +0.142 | +173.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 336 | +0.142 | +173.14€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 385 | +0.094 | +105.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 385 | +0.094 | +105.68€ | 0 | 1 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2078 | -0.017 | -23.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2078 | -0.017 | -23.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 388 | +0.015 | +26.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 388 | +0.015 | +26.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 380 | -0.044 | -25.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 380 | -0.044 | -25.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 518 | -0.038 | -31.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 518 | -0.038 | -31.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 428 | -0.005 | -3.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 428 | -0.005 | -3.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 364 | -0.005 | +10.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 364 | -0.005 | +10.43€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1112 | -0.077 | -52.46€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 511 | -0.110 | -78.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 399 | -0.126 | -60.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 112 | -0.053 | -18.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 391 | -0.037 | +19.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 280 | -0.021 | +28.68€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 111 | -0.075 | -9.44€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 210 | -0.071 | +6.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 174 | -0.068 | +4.94€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 853 | -0.080 | -26.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 259 | -0.067 | -26.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1409 | -0.207 | -89.05€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 555 | -0.207 | -50.44€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 488 | -0.206 | -46.13€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 67 | -0.210 | -4.31€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 470 | -0.210 | -37.54€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 412 | -0.220 | -44.45€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 58 | -0.133 | +6.91€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 384 | -0.202 | -1.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 357 | -0.199 | -3.48€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 27 | -0.224 | +2.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1257 | -0.209 | -94.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 152 | -0.188 | +5.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 528 | +0.376 | +484.78€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 104 | +0.141 | +73.22€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 104 | +0.141 | +73.22€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 123 | +0.364 | +103.53€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 123 | +0.364 | +103.53€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 301 | +0.457 | +308.04€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 301 | +0.457 | +308.04€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 528 | +0.376 | +484.78€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 912 | +0.045 | +84.86€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 912 | +0.045 | +84.86€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 344 | +0.029 | +9.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 344 | +0.029 | +9.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 71 | +0.007 | +0.21€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 71 | +0.007 | +0.21€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 414 | +0.070 | +69.19€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 414 | +0.070 | +69.19€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 3561 | -0.023 | -142.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3561 | -0.023 | -142.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 609 | -0.029 | -27.28€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 609 | -0.029 | -27.28€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 170 | -0.041 | -14.29€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 170 | -0.041 | -14.29€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1655 | -0.020 | -60.91€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1655 | -0.020 | -60.91€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 116 | -0.042 | -10.16€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 116 | -0.042 | -10.16€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 72 | -0.013 | -5.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 72 | -0.013 | -5.54€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11474 | +0.014 | +72.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11474 | +0.014 | +72.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2994 | +0.018 | +23.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2994 | +0.018 | +23.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2986 | +0.017 | +35.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2986 | +0.017 | +35.17€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2915 | +0.008 | -3.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2915 | +0.008 | -3.30€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 11521 | +0.017 | -18.10€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 11521 | +0.017 | -18.10€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4790 | +0.021 | +4.49€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4790 | +0.021 | +4.49€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3949 | +0.016 | -9.29€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3949 | +0.016 | -9.29€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2782 | +0.010 | -13.30€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2782 | +0.010 | -13.30€ | 1 | 0 |
| ✅ UPDOWN_GBM | 101987 | +0.060 | +9724.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 24843 | +0.080 | +5141.12€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3058 | +0.000 | +31.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 67711 | +0.061 | +4449.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6024 | +0.000 | +105.65€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 8489 | +0.105 | +1568.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1781 | +0.164 | +820.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6618 | +0.091 | +750.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 23241 | +0.057 | +2030.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3334 | +0.080 | +753.01€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 864 | +0.001 | +14.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 16216 | +0.066 | +1187.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2699 | -0.003 | +70.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 128 | -0.061 | +4.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 11078 | +0.079 | +1289.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 9231 | +0.065 | +551.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 24211 | +0.049 | +1676.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5889 | +0.072 | +893.95€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 834 | +0.005 | +16.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 15155 | +0.051 | +736.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2216 | +0.002 | +28.02€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 117 | -0.105 | +1.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 21751 | +0.039 | +1231.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 6572 | +0.032 | +427.47€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 787 | -0.009 | +4.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 13179 | +0.050 | +799.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1109 | +0.003 | +7.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 104 | -0.141 | -7.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 13215 | +0.073 | +1930.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 5506 | +0.096 | +1508.05€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7312 | +0.060 | +424.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 349 | -0.101 | -1.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 980 | +0.362 | +351.78€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 980 | +0.362 | +351.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 484 | +0.362 | +168.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 484 | +0.362 | +168.39€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 496 | +0.361 | +183.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 496 | +0.361 | +183.39€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 24532 | -0.021 | +6063.67€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 24532 | -0.021 | +6063.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4573 | -0.114 | +232.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4573 | -0.114 | +232.44€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3210 | +0.220 | +2053.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3210 | +0.220 | +2053.73€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6939 | -0.060 | +1043.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6939 | -0.060 | +1043.87€ | 5 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6758 | -0.062 | +1272.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6758 | -0.062 | +1272.59€ | 1 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 298 | +0.063 | +25.19€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 298 | +0.063 | +25.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 298 | +0.063 | +25.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 298 | +0.063 | +25.19€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1747 | +0.282 | +1458.46€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1747 | +0.282 | +1458.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 927 | +0.275 | +721.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 927 | +0.275 | +721.30€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 820 | +0.289 | +737.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 820 | +0.289 | +737.16€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 859 | -0.113 | -85.36€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 859 | -0.113 | -85.36€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 270 | -0.081 | -20.33€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 270 | -0.081 | -20.33€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 96 | -0.173 | -11.45€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 96 | -0.173 | -11.45€ | 2 | 0 |
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

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.037) — sin ventaja clara. oversold(IBS<0.3): IC=+0.071 n=35502 | neutral: IC=+0.062 n=37624 | overbought(IBS>0.7): IC=+0.099 n=35322
  - _Datos_: n=112867 IC=+0.078 PNL=+17207.96€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 793 celda(s) pasan gate riguroso completo de 2860 evaluadas (n>=40) y 3984 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.032 < 0.08 — monitorear
  - _Datos_: n=6572 IC=+0.032 PNL=+427.47€

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

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 11 ops más en GBM@18h (IC actual=-0.067)
  - _Datos_: n=4 IC=-0.067 PNL=-3.02€

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: 101925 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.143 n=1036/60 | contraria IC=+0.184 n=1090 | gap=-0.042 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=573, boost estimado=+0.014. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 336 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2216/40 IC=+0.002 PNL=+28.02€ | BTC#60min: n=2699/40 IC=-0.003 PNL=+70.48€ | SOL#60min: n=1109/40 IC=+0.003 PNL=+7.16€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.045 n=704929 | tras_1loss IC=+0.099 n=535152 | tras_2loss IC=+0.069 n=214479/40 | gap=-0.024 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.043 n=15137 | contrario_BTC IC=+0.053 n=13296/40 | gap=+0.011 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: n=104 IC=+0.179 PNL=+68.26€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=104 IC=+0.179 PNL=+68.26€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=97941 IC=+0.059 PNL=+9427.33€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=97941 IC=+0.059 PNL=+9427.33€

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
  - _Estado_: n=4030 IC=+0.002 PNL=-12.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4030 IC=+0.002 PNL=-12.77€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1994 IC=-0.004 PNL=+118.41€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1994 IC=-0.004 PNL=+118.41€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.147 > 0.1 con n=6741 PNL=+3525.11€
  - _Datos_: n=6741 IC=+0.147 PNL=+3525.11€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=2932 IC=+0.068 PNL=+220.19€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2932 IC=+0.068 PNL=+220.19€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3334 IC=+0.080 PNL=+753.01€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3334 IC=+0.080 PNL=+753.01€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 1/50 ops en el filtro definido (IC actual=+0.008 PNL=+1.17€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.17€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.093 > 0.08 con n=14417 PNL=+3703.74€
  - _Datos_: n=14417 IC=+0.093 PNL=+3703.74€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=673 IC=-0.223 PNL=-2.02€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=673 IC=-0.223 PNL=-2.02€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=579 IC=-0.013 PNL=+7.52€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=579 IC=-0.013 PNL=+7.52€

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

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=13596 IC=+0.041 PNL=+697.67€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=13596 IC=+0.041 PNL=+697.67€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.108 > 0.08 con n=480 PNL=+92.46€
  - _Datos_: n=480 IC=+0.108 PNL=+92.46€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.293 n=225) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=225 IC=+0.293 PNL=+252.39€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=16393 IC=+0.055 PNL=+1481.62€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=16393 IC=+0.055 PNL=+1481.62€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=6015 IC=+0.059 PNL=+898.28€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6015 IC=+0.059 PNL=+898.28€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=698 PNL=+232.45€
  - _Datos_: n=698 IC=+0.113 PNL=+232.45€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.08 con n=1568 PNL=+420.23€
  - _Datos_: n=1568 IC=+0.126 PNL=+420.23€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.089 > 0.08 con n=1262 PNL=+540.38€
  - _Datos_: n=1262 IC=+0.089 PNL=+540.38€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=94243 IC=+0.125 PNL=+38045.26€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=94243 IC=+0.125 PNL=+38045.26€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=80801 IC=+0.141 PNL=+36996.21€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=80801 IC=+0.141 PNL=+36996.21€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=15579 IC=+0.062 PNL=+1625.76€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=15579 IC=+0.062 PNL=+1625.76€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.02 con n=1226 PNL=+490.70€
  - _Datos_: n=1226 IC=+0.118 PNL=+490.70€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=251 IC=-0.117 PNL=+7.41€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=251 IC=-0.117 PNL=+7.41€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.451 > 0.1 con n=2055 PNL=+2001.33€
  - _Datos_: n=2055 IC=+0.451 PNL=+2001.33€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=41660 IC=+0.074 PNL=+5853.78€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=41660 IC=+0.074 PNL=+5853.78€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.198 > 0.1 con n=8647 PNL=+4945.01€
  - _Datos_: n=8647 IC=+0.198 PNL=+4945.01€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.138 < -0.1 con n=727 PNL=+100.32€
  - _Datos_: n=727 IC=-0.138 PNL=+100.32€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3864 IC=+0.067 PNL=+492.50€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3864 IC=+0.067 PNL=+492.50€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.1 con n=1066 PNL=+272.11€
  - _Datos_: n=1066 IC=+0.102 PNL=+272.11€

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
  - _Estado_: n=41787 IC=-0.137 PNL=+2737.37€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=41787 IC=-0.137 PNL=+2737.37€

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
  - _Estado_: n=4310 IC=+0.129 PNL=+2790.94€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4310 IC=+0.129 PNL=+2790.94€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.191 > 0.08 con n=5207 PNL=+3609.88€
  - _Datos_: n=5207 IC=+0.191 PNL=+3609.88€

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

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.201 > 0.08 con n=1020 PNL=+564.66€
  - _Datos_: n=1020 IC=+0.201 PNL=+564.66€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=4541 PNL=-381.73€
  - _Datos_: n=4541 IC=-0.220 PNL=-381.73€

**🟡 H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.220 > 0.2 con n=11230 PNL=+9252.29€
  - _Datos_: n=11230 IC=+0.220 PNL=+9252.29€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.114 > 0.08 con n=151 PNL=+62.62€
  - _Datos_: n=151 IC=+0.114 PNL=+62.62€

**🟡 H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=3991 PNL=+1494.48€
  - _Datos_: n=3991 IC=+0.087 PNL=+1494.48€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.170 > 0.08 con n=3870 PNL=+2960.54€
  - _Datos_: n=3870 IC=+0.170 PNL=+2960.54€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=6514 IC=-0.021 PNL=+1988.41€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6514 IC=-0.021 PNL=+1988.41€

**〰️ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: n=739 IC=+0.073 PNL=-28.58€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=739 IC=+0.073 PNL=-28.58€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.241 > 0.08 con n=5641 PNL=-439.38€
  - _Datos_: n=5641 IC=+0.241 PNL=-439.38€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.097 n=2167) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2167 IC=+0.097 PNL=+439.23€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.308 > 0.08 con n=643 PNL=+171.01€
  - _Datos_: n=643 IC=+0.308 PNL=+171.01€

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
  - _Estado_: n=17935 IC=+0.179 PNL=-2012.74€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=17935 IC=+0.179 PNL=-2012.74€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.231 > 0.1 con n=281 PNL=+196.78€
  - _Datos_: n=281 IC=+0.231 PNL=+196.78€
